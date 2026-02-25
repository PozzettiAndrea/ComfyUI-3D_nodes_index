## DGLS — Dynamic GPU Layer Swapping for ComfyUI

Smart dynamic layer swapping between GPU and CPU for optimal inference performance with target casting, and copy-compute overlap optimization. Enables running much larger models on limited VRAM setups.

---
## NOTE:
This is still under development. I am actively bug testing this atm. It's fully working on RTX 2060 and 2080ti. I havent promoted this or written about it due to some tests I want to carry out. I am currently getting between 10-30% speed improvement compared to official node.
---

## Features

* **Drop‑in ComfyUI integration.** Adds two nodes under the **loaders** category: `DGLS Model Loader` and `DGLS Swapping Loader`.
* **Architecture‑aware layer extraction.** Handles Cosmos, FLUX, WAN 2.1/2.2, HunyuanVideo, Qwen, and generic transformer layouts.
* **Buffers‑on‑GPU / params‑on‑CPU design.** Small buffers remain on GPU; master parameter tensors live on CPU and are **rebound** to GPU storage just‑in‑time per layer (via an optimized `_reassign_param`), avoiding redundant cloning.
* **Auto or manual GPU residency.** Leave it on **auto** (default) or pass an explicit comma‑separated `gpu_layer_indices` to pin chosen layers on GPU.
* **Predictive prefetch.** Chooses the next `prefetch` layers in ring order; optional CUDA streams and a conservative CPU helper thread can overlap H2D copies with compute.
* **CUDA Streams**: Uses CUDA streams to overlap memory transfers with computation
* **Target Casting**: Precision casting for specific Dtypes in  mixed layer models

---

## Requirements

* **ComfyUI** (CUDA‑enabled PyTorch).
* **GPU:** Any CUDA‑capable GPU.
* **System RAM:** 32GB+ recommended if you plan to enable overlap/pinning. 16GB can work, 64GB+ is best.
* **Currently only working with diffusion models: Any workflow with 'Load Diffusion Model' official node should be fine with this swapped for it. OmniGen not working atm.

  ---

## Updating (Custom Nodes)

-- If updating the node please recreate node through the menu to prevent comfy's cache system holding on to previous versions. 

---

## Installation (Custom Nodes)

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone or copy the DGLS files:
```bash
git clone https://github.com/obisin/dgls-comfyui
# or manually place the files in a new folder
```

3. Restart ComfyUI - the nodes should appear in the loaders category

## REMEMBER TO INSTALL THE REQUIREMENTS.TXT FOR BEST PERFORMANCE

---

## Nodes & Parameters

### 1) DGLS Model Loader

**Title:** `DGLS Model Loader`
**Returns:** `(MODEL, LAYERS)` for the next node.
**Category:** `loaders`

**Inputs (required):**

* `model_name` — selectable from Comfy paths (`unet` + `diffusion_models`).
* `model_type` — one of: `default | hunyuan | unet` (use `default` unless hunyuan).
* `cast_dtype` — one of: `default | fp32 | fp16 | bf16 | fp8_e4m3fn | fp8_e4m3fn_fast | fp8_e5m2` (applied at load time).
* `clear_model_cache` — boolean; force reload from disk, bypassing Comfy’s model cache.
* `verbose` — boolean; prints detection/dtype/extraction info (slower when enabled).

**Inputs (optional):**

* `nuke_all_caches` — boolean; CAUTION: aggressively clears assorted Comfy caches (can force other nodes to reload).

**What it does**

* Loads the model and extracts a consistent **LAYERS** sequence across supported architectures.

---

### 2) Dynamic Swapping Loader

**Title:** `Dynamic Swapping Loader`
**Input:** `(MODEL, LAYERS)` from the previous node.
**Returns:** `(MODEL)` with smart swapping enabled.
**Category:** `loaders`

**Inputs (required):**

* `prefetch` *(int, default 1, min 0, max 100)* — number of future layers to stage.
* `cpu_threading` *(bool, default False)* — background CPU helper for async staging (can help on some systems; may add overhead on others).
* `cuda_streams` *(bool, default False)* — enable CUDA streams/events for copy–compute overlap (needs a little VRAM headroom).
* `verbose` *(bool, default True)* — print layer sizes, timings, and decisions. Good for debugging and getting optimal settings when manually choosing layers

**Inputs (optional):**

* `gpu_layer_indices` *(string)* — comma‑separated layer indices to keep permanently on GPU, e.g. `0,1,2,28,29`. When set, this **overrides** auto selection. Best for models with some layers having difficulty swapping.
* `cast_target` *(string)* — one‑time recast mapping like `"f32 f16"` or multiple pairs: `"bf16 f16, f32 bf16"`. Float8/4‑bit require kernel support and are applied conservatively.

**How it swaps (overview)**

1. **Setup:** identify swappable layers; keep module **buffers** on GPU; maintain CPU **master** parameters.
2. **Per‑layer compute:** for layer `k`, compute the **needed set** = `{k, k+1…k+prefetch}` in a **ring order** over swappables.
3. **Evict & stage:** unneeded layers rebind back to CPU masters; needed layers copy CPU→GPU and `_reassign_param` binds the GPU storage (no extra clones when shapes/dtypes/devices already match).
4. **(Optional) overlap:** CUDA streams + events coordinate; an optional CPU thread can prepare upcoming transfers.

This design minimizes VRAM while keeping hot state local and avoiding parameter churn.

---

## Quick Start

**Minimal (safe defaults)**

1. `DGLS Model Loader` → choose your model → `verbose: off` (optional).
2. `Dynamic Swapping Loader`

   * `prefetch: 1`
   * `cpu_threading: off`
   * `cuda_streams: off`
   * leave `gpu_layer_indices` empty (auto GPU residency)
3. Connect to your sampler / Apply Model node and run.

**Balanced (mid‑VRAM)**

* Try `prefetch: 2`, enable `cuda_streams` if you have headroom. Keep `cpu_threading` off unless profiling shows benefit.
* If you know the bottlenecks (e.g., earliest/latest blocks), set `gpu_layer_indices` explicitly.
* For some model prefecth 0 might be preferable

**Manual GPU residency**

* Provide `gpu_layer_indices` like `0,1,2,28,29` to pin those layers on GPU; others will swap dynamically.

---

## Casting & Precision (optional)

* Use `cast_target` to convert specific *source → target* dtypes at start‑up, e.g.:

  * `"f32 f16"` (downcast FP32 → FP16)
  * `"bf16 f16, f32 bf16"` (multiple rules)
* Float8 and 4‑bit (`nf4`/`fp4`) paths are guarded: they’re only applied if kernels support them; otherwise the safer fallback (e.g., `bf16`) is used.
* For global model dtype at load time, use the Model Loader’s `cast_dtype` (separate from `cast_target`).

---

## Tips & Tuning

* **Auto vs manual GPU layers:** leaving `gpu_layer_indices` empty uses DGLS auto‑selection based on availability and layer sizes. Explicit indices take priority.
* **Prefetch:** start with `1`. Increase only if you see stalls and have spare VRAM. The ring order avoids wasteful wraps.
* **Overlap options:** try **CUDA streams** first if you have headroom. CPU threading is conservative (1 worker) and helps mainly where trasnfer latency dominates.
* **Verbose diagnostics:** enable `verbose` to print chosen residents, swappable indices, sizes (MB), and timing—useful for dialing in `prefetch` and residency.

---

## Troubleshooting

* **“Cannot fit layer X on GPU.”** Reduce `gpu_layer_indices`, lower `prefetch`. The emergency path will attempt cleanup/re‑stage; persistent failure means lowering residency.
* **Instability with overlap.** Turn off `cuda_streams` and `cpu_threading`; re‑run with `verbose` to inspect staging.
* **Odd dtype/buffers.** Prefer conservative `cast_target` rules; keep batch‑norm‑like stats in fp32 (the loader handles common cases).

---

## File Map

* `dgls_model_loader.py` — model loading, dtype at load, cache management, robust layer extraction, and tensor healing.
* `dynamic_swapping_loader.py` — swapping engine, auto or explicit GPU residency, prefetch/overlap options, and the ComfyUI loader node.

---

## License

(see repository license file).

---

