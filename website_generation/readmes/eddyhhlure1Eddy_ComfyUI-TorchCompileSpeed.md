<img width="913" height="904" alt="image" src="https://github.com/user-attachments/assets/b6b364a0-7d4d-40f2-bb66-fd7640d8c5e3" />


# ComfyUI-TorchCompileSpeed

A compact, non-intrusive ComfyUI node set that boosts torch.compile performance and cache hit rate. Designed to plug into WanVideo Cython Model Loader without touching its source.

Author: eddy

## Highlights

- Speed mode (recommended)
  - inductor + max-autotune-no-cudagraphs
  - dynamic=True for better shape tolerance and cache reuse
  - CUDA Graphs disabled to cut capture overhead
  - Triton autotune fully enabled
- Smarter reuse (inside our nodes only)
  - Optional reuse_if_similar to skip recompiles for the same model + config
- Experimental PTX assist (for no-CUDA-Graphs paths)
  - When experimental_ptx is on, a light warmup triggers PTX/kernel cache early
  - Fast-math toggle and optional TRITON_CACHE_DIR for cross-session reuse
- Drop‑in with WanVideo Cython Model Loader
  - Output type is WANCOMPILEARGS, so you can wire it straight into compile_args

## Installation

- Place this folder under ComfyUI/custom_nodes and restart ComfyUI

## Nodes and parameters

### Torch Compile Speed Settings
Output: WANCOMPILEARGS (torch_compile_args)

Required:
- backend: inductor/cudagraphs (default inductor)
- fullgraph: enable fullgraph (default False)
- mode: default/max-autotune/max-autotune-no-cudagraphs/reduce-overhead/speed (default speed)
- dynamic: dynamic compilation (default False; set True for speed mode)
- dynamo_cache_size_limit: torch._dynamo.config.cache_size_limit (default 64)
- compile_transformer_blocks_only: compile transformer blocks only (default True)
- reuse_if_similar: reuse compiled results for same model + config (default True)
- experimental_ptx: enable experimental PTX assist (default False)
- ptx_fast_math: enable fast-math when available (default True)
- warmup_runs: warmup iterations to trigger PTX/kernel cache (default 1, range 0–5)

Optional:
- dynamo_recompile_limit: torch._dynamo.config.recompile_limit (default 128)
- ptx_cache_dir: set TRITON_CACHE_DIR to help cross‑session reuse

Recommended (speed‑first):
- mode=speed, dynamic=True, fullgraph=False
- compile_transformer_blocks_only=True
- reuse_if_similar=True
- experimental_ptx=True, warmup_runs=1–2, ptx_fast_math=True

### Apply Torch Compile (optional)
Input: MODEL + WANCOMPILEARGS, Output: MODEL
- Wraps model forward with torch.compile
- With reuse_if_similar=True, repeated calls for the same model + config reuse the compiled forward
- With experimental_ptx=True:
  - Tries a lightweight triton.ops matmul warmup; if unavailable, falls back to a small torch.compile matmul warmup
  - You can set TRITON_CACHE_DIR; combined with warmup_runs it tends to make PTX/kernel cache available sooner

## WanVideo integration (non‑intrusive)
- Wire directly: Torch Compile Speed Settings → WanVideo Cython Model Loader.compile_args
- Or use with other models: Settings → Apply Torch Compile → MODEL

## Logs and verification
- With experimental_ptx enabled, console prints either:
  - [TorchCompileSpeed] PTX warmup via triton.ops.matmul, or
  - [TorchCompileSpeed] PTX warmup via torch.compile(matmul)
- When speed mode applies, you’ll see inductor config messages. If a knob isn’t available in your PyTorch/Triton build, a warning is printed and safely ignored.

## Troubleshooting
- Slow first run: includes compilation + autotune. Second and later runs should be much faster.
- triton.ops missing: falls back to torch.compile warmup and still produces PTX/kernel cache.
- Can’t connect to WanVideo Loader: ensure the Settings output type is WANCOMPILEARGS (this node already uses it).
- OOM or pressure: lower dynamo_cache_size_limit, or keep compile_transformer_blocks_only=True.

## Performance reference (RTX 5090, CUDA 12.0)
- default: first ~14.38s, second ~0ms, about 48,301×
- max-autotune-no-cudagraphs: first ~7.73s, second ~0ms, about 26,603×
- speed: first ~10.52s, second ~0ms, about 84,554×

Note: Numbers vary by system. experimental_ptx often reduces first‑run cost on no‑CUDA‑Graphs paths and improves second‑run hits.

## Disclaimer
- experimental_ptx is experimental. Behavior depends on your PyTorch/Triton build; unsupported knobs are ignored.

## Changelog
- v1.1.0
  - Added experimental_ptx, ptx_fast_math, warmup_runs, ptx_cache_dir
  - Added reuse_if_similar and compile_transformer_blocks_only controls
  - Kept non‑intrusive design and WanVideo Cython Model Loader compatibility
- v1.0.0
  - Initial release with speed mode and core torch.compile integration
