# Halo-TeaCache

**AMD Unified Memory TeaCache for LTX2 (LTXAV)**

Lean, single-file TeaCache implementation for LTX2 audio-video generation on AMD APUs with unified memory. No CPU offload, no device toggling — the cache stays on GPU where it belongs.

Built for AMD. By the AMD community.

## What It Does

Caches the output of LTX2's 48-layer dual-stream transformer blocks across denoising steps. When consecutive steps produce similar intermediate representations, all 48 layers are skipped and the cached residual is reused — for both video AND audio streams.

### Performance (AMD Strix Halo, LTX2 19B fp8, 121 frames @ 24fps)

| Metric | Without Cache | With Halo-TeaCache |
|--------|--------------|-------------------|
| Per-step (uncached) | ~16.5s | ~16.5s |
| Per-step (cached) | — | ~10.7s |
| Average | ~16.5s/it | ~14.0s/it |
| Total (15 steps) | ~4:07 | ~3:29 |

## Installation

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/bkpaine1/Halo-TeaCache.git
# Restart ComfyUI
```

No additional dependencies required.

## Usage

1. Add the **Halo-TeaCache** node to your workflow
2. Connect your LTX2 model through it (before CFGGuider/Sampler)
3. Adjust settings:

| Parameter | Default | Description |
|-----------|---------|-------------|
| `rel_l1_thresh` | 0.20 | Cache aggressiveness. Higher = more skipping (faster, lower quality). Try 0.10-0.25. |
| `start_percent` | 0.15 | Start caching after this % of steps (early steps need full compute). |
| `end_percent` | 1.0 | Stop caching after this % of steps. |

### Tuning Tips

- **Blurry output?** Lower `rel_l1_thresh` (try 0.10-0.12)
- **Want more speed?** Raise `rel_l1_thresh` (try 0.25-0.30)
- **Quality on early steps matters most** — keep `start_percent` at 0.10-0.20

## How It Works

1. Before each denoising step, computes a modulated input from the video timestep embedding
2. Compares L1 distance to previous step's modulated input using polynomial coefficients
3. If distance is below threshold → skip all 48 transformer layers, add cached residual
4. If above → run full computation, cache the new residual
5. Both video and audio residuals are cached together (they're coupled via cross-attention)

### Why AMD Unified Memory?

On AMD APUs (Strix Halo, etc.), CPU and GPU share the same physical memory. There's no PCIe transfer penalty for keeping the cache on "GPU" — it's all the same address space. This eliminates the `cache_device` toggle that other TeaCache implementations need.

## Compatibility

- **Models**: LTX2 (LTXAV), LTXv (LTXVModel)
- **Hardware**: AMD APUs with unified memory (designed for), discrete GPUs (works fine too)
- **ComfyUI**: Tested with latest (Jan 2026)

## vs Original TeaCache

| | TeaCache | Halo-TeaCache |
|---|---|---|
| LTX2 (LTXAV) support | ❌ Crashes | ✅ Works |
| Patch target | `forward` (full method) | `_process_transformer_blocks` (surgical) |
| Audio handling | N/A | Cached with video (cross-attn coupled) |
| Cache location | GPU or CPU toggle | GPU only (unified memory) |
| Code size | ~1000 lines | ~250 lines |
| Dependencies | unittest.mock | unittest.mock |

## Credits

Created by **Brent** & **Claude Code** (Anthropic Claude Opus 4.5)

License: MIT
