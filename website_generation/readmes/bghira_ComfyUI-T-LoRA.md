# ComfyUI-T-LoRA

Custom ComfyUI loaders for **timestep-masked T-LoRA inference**.

- Official T-LoRA reference implementation: https://github.com/ControlGenAI/T-LoRA
- Gold-standard training/inference integration reference (multi-model): https://github.com/bghira/SimpleTuner
- Extensive portable LyCORIS implementation (including T-LoRA training): https://github.com/KohakuBlueleaf/LyCORIS

## What This Repo Implements

Two inference paths are provided:

- `Load T-LoRA (Bypass)` / `Load T-LoRA (Bypass, Model Only)`
  - For official-style attn-processor checkpoints (`...to_q_lora.down.weight`, etc.)
  - Supports SDXL-style and Flux.1-dev-style official T-LoRA key layouts
  - Injected with ComfyUI bypass adapters
  - Per-step mask applied before UNet forward

- `Load T-LoRA (LyCORIS, Bypass)` / `Load T-LoRA (LyCORIS, Bypass, Model Only)`
  - For LyCORIS-style T-LoRA checkpoints (`q_layer/p_layer/lambda_layer`)
  - LyCORIS modules are parsed, then converted into ComfyUI bypass adapters
  - Per-step mask is set via LyCORIS timestep-mask APIs before each denoise step

## Install

```bash
ln -s ~/src/ComfyUI-T-LoRA $COMFYUI_PATH/custom_nodes/ComfyUI-T-LoRA
```

LyCORIS loader nodes require `lycoris-lora` with T-LoRA support from upstream `main`:

```bash
pip install -U git+https://github.com/KohakuBlueleaf/LyCORIS.git
```

Restart ComfyUI after updates.

## Quick Usage

1. Put base model weights in normal ComfyUI model locations.
2. Put T-LoRA checkpoint in `models/loras`.
3. Add one loader node:
   - Official checkpoint: `Load T-LoRA (Bypass)`
   - LyCORIS checkpoint: `Load T-LoRA (LyCORIS, Bypass)`
4. Feed returned `MODEL` (and `CLIP` when using non-model-only node) to your sampler path.

Recommended start params:

- `strength_model = 1.0`
- `max_rank = 0` (auto-infer)
- `min_rank = 1`
- `alpha = 1.0`
- `max_timestep = 0` (auto-infer)

## Debugging Mask Behavior

Set:

- `debug = true`
- `debug_every = 1`

You should see step logs with computed active rank.  
For adapter-level logs, the first adapter call per step reports active dimensions.

<details>
<summary>How Timestep Masking Is Applied</summary>

At each denoise step, the node computes an active rank:

`r = int(((max_timestep - t)/max_timestep)^alpha * (max_rank - min_rank)) + min_rank`

Then a binary mask activates ranks `[0:r)` and suppresses higher ranks for that step.

- Official path: mask is consumed by custom T-LoRA bypass adapters.
- LyCORIS path: mask is set with LyCORIS `set_timestep_mask(...)` and consumed by converted adapters.

</details>

<details>
<summary>Checkpoint Format Notes</summary>

Official node expects keys like:

- `...attn1.processor.to_q_lora.down.weight`
- `...attn1.processor.to_q_lora.up.weight`

LyCORIS node expects T-LoRA module keys (detected by `lambda_layer` / `q_layer` / `p_layer` entries).  
Non-T-LoRA LyCORIS modules in a mixed checkpoint are skipped.

</details>

## Current Limitations

- `strength_clip` is currently ignored for these T-LoRA loaders.
- This repo is inference-focused; training is out of scope.
- For broad multi-architecture training workflows, use upstream trainer repos directly (SimpleTuner / LyCORIS).
