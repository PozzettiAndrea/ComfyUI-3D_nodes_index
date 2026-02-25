# ComfyUI Attention Optimizer

**Automatically benchmark and optimize the attention mechanism in diffusion models for maximum generation speed.**

## Why This Matters

### The Problem

Modern diffusion models (SDXL, Flux, WAN, LTX-V, Hunyuan Video) are based on **transformer architecture**. The core operation - **attention** - computes relationships between all elements in the image/video latent space. This is:

- **The most expensive operation** - attention takes 40-70% of total generation time
- **O(n²) complexity** - cost grows quadratically with resolution/frames
- **GPU-dependent** - different GPUs perform best with different implementations

### The Solution

Multiple optimized attention backends exist:
- **PyTorch SDPA** - built-in, always available
- **Flash Attention** - CUDA kernels, memory efficient
- **SageAttention** - INT8 quantization, up to 2-4x faster
- **xFormers** - memory efficient attention

**But which one is fastest for YOUR specific GPU and model?**

This plugin **benchmarks all available backends** and **automatically applies the fastest one**.

## Real-World Speedups

Tested on RTX 4090 with head_dim=128 (SDXL, Flux):

| Backend | Time | Speedup |
|---------|------|---------|
| PyTorch SDPA | 5.0ms | 1.0x (baseline) |
| Flash Attention | 5.4ms | 0.93x |
| **SageAttention** | **2.7ms** | **1.9x** |

**Result: 1.9x faster generation** just by switching attention backend.

For video models (WAN, Hunyuan) with longer sequences, speedups can reach **2-4x**.

## Installation

### Option 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Click **"Install via Git URL"**
3. Paste: `https://github.com/D-Ogi/ComfyUI-Attention-Optimizer.git`
4. Restart ComfyUI

### Option 2: Manual Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/D-Ogi/ComfyUI-Attention-Optimizer.git
```

Restart ComfyUI.

### Optional: Install Optimized Backends

The plugin works out-of-the-box with PyTorch SDPA. For better performance, install additional backends:

```bash
# SageAttention - recommended for RTX 30xx/40xx (1.5-2x speedup)
pip install sageattention

# Flash Attention - alternative for Ampere+ GPUs
pip install flash-attn

# xFormers - memory efficient option
pip install xformers
```

> **Note:** On Windows, Flash Attention requires building from source or using prebuilt wheels.
> SageAttention is easier to install and often faster on consumer GPUs.

## Usage

### Basic Usage

1. Add **"Attention Optimizer"** node to your workflow (category: `model_patches`)
2. Connect your model to the `model` input
3. Run - it benchmarks once, caches results, and auto-applies the fastest backend

### How It Works

```
┌─────────────────┐     ┌──────────────────────────┐     ┌─────────────┐
│ Load Checkpoint │────▶│ Attention Optimizer      │────▶│ KSampler    │
└─────────────────┘     │                          │     └─────────────┘
                        │ 1. Detect model params   │
                        │ 2. Check cache           │
                        │ 3. Benchmark (if needed) │
                        │ 4. Clone model & apply   │
                        │    attention override    │
                        └──────────────────────────┘
```

**First run:** Benchmarks all backends (~5-10 seconds), saves to cache.
**Subsequent runs:** Loads from cache (instant), applies optimal backend.

### Node Inputs

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| `model` | MODEL | required | The diffusion model to optimize |
| `attention_backend` | dropdown | `auto` | `auto` = benchmark & select best, or force specific backend |
| `force_refresh` | bool | False | Re-run benchmark even if cached |
| `auto_apply` | bool | True | Apply the selected backend to this model |
| `seq_len` | int | 8192 | Sequence length for benchmark |
| `num_heads` | int | 24 | Number of attention heads |

### Node Outputs

| Output | Type | Description |
|--------|------|-------------|
| `model` | MODEL | Cloned model with optimized attention applied |
| `best_attention` | STRING | Name of applied backend |
| `kjnodes_mode` | STRING | Compatible mode for KJNodes PatchSageAttention |
| `impl_type` | STRING | Implementation type (cuda/triton/pytorch) |
| `speedup` | FLOAT | Speedup vs PyTorch SDPA baseline |
| `time_ms` | FLOAT | Time per attention call in milliseconds |
| `head_dim` | INT | Detected head dimension from model |
| `report` | STRING | Full benchmark report text |

## Supported Backends

| Backend | Implementation | Best For |
|---------|---------------|----------|
| `pytorch` | PyTorch SDPA | Always available, baseline |
| `xformers` | xFormers CUDA | Memory efficiency |
| `sage_auto` | SageAttention auto | General use (auto-selects best variant) |
| `sage_cuda` | SageAttention CUDA | RTX 30xx/40xx |
| `sage_triton` | SageAttention Triton | When CUDA kernel unavailable |
| `sage_fp8_cuda` | SageAttention FP8 | Maximum speed, slight quality trade-off |
| `sage_fp8_cuda_fast` | SageAttention FP8++ | Even faster FP8 |
| `sage3` | SageAttention 3 | RTX 50xx (Blackwell) only |
| `flash` | Flash Attention 2 | H100, A100, RTX 30xx/40xx |

## Model Compatibility

| Model | Status | Notes |
|-------|--------|-------|
| SDXL | ✅ Full | head_dim=128, SageAttention optimal |
| SD 1.5 | ✅ Full | head_dim=64 |
| SD 3 | ✅ Full | |
| Flux | ✅ Full | Per-model attention override |
| LTX-V | ✅ Full | head_dim=160 |
| WAN 2.1/2.2 | ✅ Full | Per-model attention override |
| Hunyuan Video | ✅ Full | Per-model attention override |
| Cosmos | ✅ Full | Per-model attention override |
| SeedVR2 | ❌ N/A | Uses own attention system, not affected |

## GPU Recommendations

| GPU | Recommended Backend | Expected Speedup |
|-----|---------------------|------------------|
| RTX 4090/4080 | `sage_auto` or `sage_fp8_cuda_fast` | 1.5-2.0x |
| RTX 3090/3080 | `sage_auto` or `flash` | 1.3-1.8x |
| RTX 50xx (Blackwell) | `sage3` | 2-4x |
| H100/A100 | `flash` | 1.5-2.0x |
| AMD (ROCm) | `pytorch` | 1.0x (baseline) |

## Example Benchmark Report

```
=================================================================
BENCHMARK REPORT
=================================================================
dtype: float16 | head_dim: 128 | seq_len: 8192 | CUDA: 12.4 | Triton: 3.0.0
SageAttention: v2.1.1

>>> BEST: sage_fp8_cuda_fast (1.89x speedup) <<<
    impl: cuda | kjnodes mode: sageattn_qk_int8_pv_fp8_cuda++

Results (fastest first):
-----------------------------------------------------------------
 [v] sage_fp8_cuda_fast       2.671ms   1.89x  (cuda) <<<
 [v] sage_auto                2.679ms   1.88x  (auto)
 [v] sage_fp8_cuda            3.100ms   1.63x  (cuda)
 [v] sage_triton              3.446ms   1.47x  (triton)
 [v] sage_cuda                3.947ms   1.28x  (cuda)
 [v] pytorch                  5.049ms   1.00x  (pytorch)
 [v] xformers                 5.194ms   0.97x  (cuda/triton)
 [v] flash                    5.430ms   0.93x  (cuda)
 [ ] sage3                    ---       (N/A) Not installed
-----------------------------------------------------------------
[v] = validated (tested underlying library directly)
=================================================================
```

## Technical Details

### Why Different Backends?

**PyTorch SDPA** uses cuDNN/cuBLAS - general purpose, always works.

**Flash Attention** fuses operations into single CUDA kernel, reducing memory bandwidth. Great for long sequences.

**SageAttention** quantizes Q/K to INT8, reducing memory and compute. Works best for head_dim ≤ 128.

**xFormers** similar to Flash Attention, good memory efficiency.

### head_dim Matters

Models have different attention head dimensions:
- **SD 1.5:** head_dim=64
- **SDXL, Flux:** head_dim=128
- **LTX-V:** head_dim=160

SageAttention works best with head_dim ≤ 128. For larger dimensions, SDPA or Flash Attention may be faster.

### Cache System

Benchmark results are cached in `benchmark_db.json` based on:
- Model hash (architecture + weights)
- head_dim
- seq_len / num_heads parameters

Cache is per-machine - different GPUs will have different optimal backends.

## Troubleshooting

### "Backend X not available"
Install the missing package:
```bash
pip install sageattention  # for sage_*
pip install flash-attn     # for flash
pip install xformers       # for xformers
```

### No speedup observed
1. Check if `auto_apply` is enabled
2. Try `force_refresh=True` to re-benchmark
3. Check console for `[Benchmark] Applied: X` message

### Model not affected
Some models (like SeedVR2) use their own attention implementation and won't be affected by this plugin. Check the compatibility table above.

## License

MIT License - see [LICENSE](LICENSE)

## Credits

- [SageAttention](https://github.com/thu-ml/SageAttention) - THU-ML
- [Flash Attention](https://github.com/Dao-AILab/flash-attention) - Dao-AILab
- [xFormers](https://github.com/facebookresearch/xformers) - Meta
