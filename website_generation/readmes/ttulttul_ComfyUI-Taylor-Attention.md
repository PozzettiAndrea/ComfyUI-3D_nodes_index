# Flux2TTR v2 Nodes for ComfyUI

This repository provides ComfyUI nodes for Flux2TTR v2 distillation and controller training. The legacy `TaylorAttentionBackend` and `HybridTaylorAttentionBackend` nodes, along with their support modules, have been retired and intentionally removed.

## Installation

Copy this folder into your ComfyUI `custom_nodes` directory and restart
ComfyUI.  For prerequisites, unless you are using ComfyUI's official installer
(unlikely), run `uv pip install -e custom_nodes/ComfyUI-Approximate-Attention`
to install all of the prerequisites you will need for training using this node
pack. Pre-requisites are found in `pyproject.toml`.

## Available Nodes

The package includes eight nodes. The core training pair is `Flux2TTRTrainingParameters` (shared configuration) and `Flux2TTRTrainer` (Phase 1 distillation), joined by `Flux2TTRControllerTrainer` (Phase 2 routing controller training) and `Flux2TTRController` (inference-time patching and routing). Four utility nodes round out the set: `RandomSeedBatch`, `LoadPromptListFromJSON`, `ClockedSweepValues`, and `Combinations`.

## Workflow

Training proceeds in two phases. In Phase 1, `Flux2TTRTrainingParameters` feeds into `Flux2TTRTrainer` to distill the TTR attention layers. In Phase 2, the same parameters node feeds into `Flux2TTRControllerTrainer` to train the routing controller. At inference time, a model is patched through `Flux2TTRController` and then passed to a `KSampler`.
By default, the Phase-1 and Phase-2 training nodes read/write checkpoints under `ComfyUI/models/approximate_attention` (`flux2_ttr.pt` and `flux2_ttr_controller.pt`), and create that folder automatically if it does not exist.

---

## Network Architecture

### Phase 1: TTR Attention Network

Each patched Flux single-attention block receives a trainable TTR layer (`Flux2HKRAttnLayer`) composed of two branches that are fused through a residual, strictly convex blend.

**Kernel-regression branch.** The `KernelRegressorAttention` module learns positive feature maps through a 3-layer MLP shaped `head_dim → hidden → hidden → feature_dim`, where `hidden = max(head_dim, 2 × feature_dim)`. It uses split Q/K phi networks by default. During evaluation, keys and values are streamed in chunks to build linear-time statistics (`Ksum`, `KᵀV`), and queries are likewise evaluated in chunks, giving the branch its computational advantage.

**Landmark softmax branch.** This branch always retains all conditioning tokens as landmarks. Image-token landmarks are drawn from a dynamic budget governed by `landmark_fraction`, `landmark_min`, and `landmark_max` (where `landmark_max=0` means unlimited). Runtime conditioning-token counts are accepted through `transformer_options` keys: `conditioning_token_count`, `cond_token_count`, or `prefix_token_count`.

**Sigma/CFG conditioner.** A small MLP predicts per-branch scale and bias modulation for both the kernel and landmark branches. It is initialized to identity behavior so that startup is backward-compatible.

**Branch fusion.** The two branches are combined as `out = out_kernel + α × (out_land − out_kernel)`, making α an interpolation weight toward the landmark branch rather than an unconditional residual. In non-adaptive mode, `α = α_max × sigmoid(base_logit)`. In adaptive mode, a per-token version `α_token = α_max × sigmoid(base_logit + γ × (d_norm − 0.5))` is used, where `d_norm` is the cosine disagreement (`1 − cosine_similarity`) between the kernel and landmark outputs — chosen over raw magnitude to avoid scale bias. Because α is always in `(0, α_max)` (default 0.2), the landmark branch stays a bounded correction and the blend remains strictly convex. Internally, α is stored in logit space and interpreted through sigmoid. Checkpoints now include `alpha_format`; legacy checkpoints without that marker are migrated from raw alpha on load, while new checkpoints skip migration to avoid double conversion.

### Phase 1: Training Mechanics (Online Distillation)

Training happens online during sampling. Teacher targets are the native Flux attention outputs computed on real prompts and sampling states.

**Replay buffer.** The replay store holds query-subsampled examples alongside full keys and values — specifically tuples of `(q_sub, k_full, v_full, teacher_sub, masks, sigma, cfg)`. Subsampling only the queries preserves global context while substantially reducing training cost. The buffer is CPU-offload friendly, with configurable storage dtype and a global byte budget backed by eviction.

**Layer selection and readiness.** Per-step layer selection is randomized between `min_swap_layers` and `max_swap_layers` to keep training coverage broad. Readiness gating is fail-closed: inference falls back to teacher attention until a layer accumulates enough updates and achieves a low EMA cosine distance. Hysteresis (exit threshold = readiness threshold × 1.2) prevents layers from flapping at the readiness boundary.

**EMA updates.** The EMA values for `ema_loss` and `ema_cosine_dist` are flushed once per sampling run (using the run-mean at sigma boundaries) rather than at every training step, which reduces prompt-to-prompt readiness oscillation. A periodic fallback flush fires every 20 training updates so that readiness progress continues even if sigma-boundary detection does not trigger. Each flush logs per-layer post-flush values to the console for debugging.

**Distillation loss.** The per-replay-update loss uses uncertainty-weighted multi-task optimization in the style of Kendall et al.:

```
huber = SmoothL1(student, teacher; β=huber_beta)
cosine_term = 1 − cosine_similarity(student, teacher, dim=−1).mean()

loss = huber / (2 × exp(log_var_huber)) + log_var_huber / 2
     + cosine_term / (2 × exp(log_var_cosine)) + log_var_cosine / 2
```

Here `log_var_huber` and `log_var_cosine` are learned scalars that let neither objective dominate. Initialization is asymmetric (`log_var_huber=0.0`, `log_var_cosine=−1.0`) so cosine alignment starts with higher effective weight before the Kendall balancing converges. Cosine alignment computes per-token, per-head similarity over the head dimension (`dim=−1`), preventing high-dimensional flattening from masking hard-token directional errors.

**Checkpointing.** Phase 1 checkpoints persist per-layer AdamW optimizer states and the loss-weight optimizer state for `log_var_huber` / `log_var_cosine`, so cross-run resume preserves momentum and variance estimates instead of restarting optimizer warmup. Layer and optimizer restoration strips inference-tensor metadata and auto-rebuilds stale inference-backed layers before replay training, preventing "inplace update to inference tensor" failures at run boundaries. Loss-balance parameters are likewise rebuilt as normal trainable tensors if they were created under `torch.inference_mode()`.
When `comet_experiment` is not provided, `Flux2TTRRuntime` now auto-generates a per-runtime Comet experiment key using `git rev-parse --short=7 HEAD` plus a start timestamp (`YYYYMMDD-HHMMSS`), and enables persistent experiment reuse for that key. The git hash is resolved from the directory containing `flux2_ttr.py`, so it tracks the extension repository rather than a parent repo. Comet display names are also set at experiment start to a human-readable run tag of the form `YYYY-MM-DD-HHMMSS-<git6>` (for example `2026-02-11-073025-b3ed63`) to make run identification easier in the Comet UI.
When resuming from checkpoint via `Flux2TTRTrainer`, Comet settings from the UI `training_config` take precedence over checkpoint metadata so changing the experiment key/project/workspace in the workflow is respected immediately.

**Inference-mode safety.** The codebase includes explicit `torch.inference_mode(False)` and grad-enabled guards, plus inference-tensor rebuild paths, to handle the ComfyUI runtime context cleanly.

### Phase 2: Controller Network

The `TTRController` predicts a per-layer routing logit for each diffusion step. Its inputs are `sigma`, `cfg_scale`, latent `width`, and latent `height`. Sigma and CFG are embedded with sinusoidal scalar embeddings; resolution gets a learned embedding constructed from sinusoidal width/height features. A 3-layer MLP head maps these embeddings to `num_layers` logits, where a high logit means full (native) attention and a low logit routes that layer through the Phase 1 TTR approximation.

### Phase 2: Training Mechanics

Controller training uses policy gradients with quality-driven rewards. A teacher path samples with the original model while a student path samples with the TTR model under controller routing. The quality objective (`compute_loss`) on latent or image outputs combines `rmse_weight × RMSE + cosine_weight × cosine_distance + lpips_weight × LPIPS + dreamsim_weight × DreamSim + hps_weight × HPS_penalty + biqa_quality_weight × BIQA_quality_penalty + biqa_aesthetic_weight × BIQA_aesthetic_penalty`.

For HPS/BIQA terms, the trainer compares teacher and student scores and penalizes only when the student is lower (`relu(teacher_score - student_score)`), so improving over the teacher baseline is not penalized.

**Reward shaping.** The reward signal is `reward = −quality_loss − λ_eff × efficiency_penalty + λ_entropy × entropy_bonus`, where the efficiency penalty is `abs(actual_full_attn_ratio − target_full_attn_ratio)` and `target_full_attn_ratio = 1 − target_ttr_ratio`.

**Stability guards.** Efficiency penalty uses symmetric deviation from target full-attention ratio (`abs(actual_full_attn_ratio - target_full_attn_ratio)`) so both over- and under-routing are penalized. Reward-baseline EMA updates are quality-floor clamped (`reward_baseline_quality_floor`, default `-0.3`) to prevent baseline drift from normalizing poor-quality rewards.

**REINFORCE update.** The policy loss is `−(reward − baseline) × log_prob(actions)` computed over eligible (ready) layers only. An entropy bonus keeps policies from collapsing to saturated Bernoulli decisions. Routing ratios and penalties are computed over eligible layers, with forced-full layers tracked separately to avoid biased policy pressure. The reward baseline and AdamW optimizer state are checkpointed and restored for stable resume.

**Sigma-aware training.** When `sigma_aware_training` is enabled (the default), a trajectory wrapper logs per-step actions and recomputes sigma-weighted log-probs under a grad-enabled context, matching how routing is actually used during denoising.

**Trainer modularization.** The `Flux2TTRControllerTrainer` node now delegates its execution flow to `flux2_ttr_controller_trainer_node.py`, with small composable helper functions for sampling, policy updates, metrics, checkpointing, and Comet logging.

**Optional quality-model dependencies.** Additional controller quality terms are activated only when their weights are non-zero: `dreamsim` for DreamSim, `hpsv2` or `ImageReward` for HPS/ImageReward, and `pyiqa` (Q-Align or LIQE fallback) for BIQA metrics.
When DreamSim is enabled inside ComfyUI, the trainer now detects the known `from utils import trunc_normal_` namespace collision and retries import with DreamSim's bundled `utils` shim (package or single-module layouts), then falls back to a temporary `utils.trunc_normal_` patch if needed. Recovery is applied for both import-time and deferred `dreamsim(...)` call-time imports.

**Inference.** `Flux2TTRController` exposes a `quality_speed` knob to trade quality against speed through controller thresholding. It supports two policy modes: `stochastic` (the default) samples one controller mask per diffusion step — cached for all layer calls in that step — to match sigma-aware policy training behavior, while `threshold` mode uses a deterministic cutoff. For checkpoint consistency, controller inference now derives `feature_dim` directly from TTR checkpoint metadata rather than assuming a default. Per-step routing summaries (sigma, threshold, student-routed layer set) are logged once per step.

---

## Observability

Comet logging emits rich per-layer and cross-layer quantile metrics at each log tick, including a `flux2ttr/global/pareto_frontier` for ready-layer quality and coverage tracking, per-layer `alpha_sigmoid` values with cross-layer aggregates for adaptive alpha monitoring, and the learned loss-balance parameters (`log_var_huber`, `log_var_cosine`). Distill snapshot logs also print the current loss-weight parameters to the console for quick monitoring. Controller training also forces a first-step Comet log (`global_step == 1`) so long diffusion-step runs show immediate telemetry before the regular `log_every` cadence. Persistent Comet experiments can be maintained across ComfyUI sampling runs by setting `comet_experiment`, which reuses the same run key instead of ending at each cleanup.
Comet lifecycle handling is centralized in `flux2_comet_logging.py` and shared by both Phase-1 (`flux2_ttr.py`) and Phase-2 (`flux2_ttr_controller_trainer_node.py`) training flows so API-key resolution, experiment start/reuse, display naming, parameter logging, and metric logging failure behavior stay consistent.
Comet experiment keys are normalized to strict Comet constraints (alphanumeric, 32-50 chars) before start, and git hash discovery falls back to reading `.git` metadata (`HEAD` + refs) when `git rev-parse` is unavailable in the runtime environment.

## Design Highlights

Several implementation choices are worth calling out. Readiness gates are fail-closed at layer granularity with EMA cosine-distance hysteresis, so untrained layers never degrade output quality. Query-only replay subsampling retains the full K/V context, giving the student access to the same global information the teacher sees while dramatically cutting storage and compute. The adaptive blend is bounded by `alpha_max` and operates in logit space with cosine-disagreement modulation, keeping the landmark branch a principled correction rather than an uncontrolled residual. The dynamic landmark policy always preserves conditioning tokens and scales image landmarks with resolution. Finally, controller penalties and routing ratios are computed strictly over eligible layers, with forced-full layers excluded, so the policy gradient signal remains unbiased.

---

## Utility Nodes

**ClockedSweepValues** maps a clock list to evenly distributed sweep values; its output length matches the clock length. **RandomSeedBatch** generates a deterministic list of integer seeds from a base seed. **LoadPromptListFromJSON** loads a JSON `array<string>` file into a prompt-list output. **Combinations** builds repeated float-list outputs across up to four input value lists to cover Cartesian-style combinations.

## Tests

Run the test suite with `pytest -q`, or using `uv`:

```bash
uv sync --extra test
uv run pytest
```

## Building the Paper

Build `docs/flux2ttr_v2_paper.tex` into `docs/flux2ttr_v2_paper.pdf` with:

```bash
scripts/build_paper.sh
```

The script accepts `--dry-run`, `--engine latexmk`, and `--engine pdflatex --clean` as options.

The paper text is now aligned with current implementation details (Kendall-weighted Phase-1 loss, EMA-cosine readiness with hysteresis, and sigma-aware stochastic controller routing), and lists the author as `Skoogeer`.
