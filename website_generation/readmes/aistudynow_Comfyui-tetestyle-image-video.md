# ComfyUI-TeleStyle

#

An unofficial, streamlined, and highly optimized ComfyUI implementation of [TeleStyle](https://github.com/Tele-AI/TeleStyle).

This node is specifically designed for **Video Style Transfer** using the **Wan2.1-T2V** architecture and TeleStyle custom weights. Unlike the original repository, this implementation strips away all heavy image-editing components (Qwen weights) to focus purely on video generation with speed/quality.

## Requirements
* **GPU VRAM**: 6GB minimum
* **Disk Space**: ~6GB for models and weights

https://aistudynow.com/how-to-fix-slow-style-transfer-in-comfyui-run-telestyle-on-6gb-vram/

**Youtube Tutorial:** https://www.youtube.com/watch?v=yHbaFDF083o

## ✨ Key Features

- **High Performance**:
  - **Acceleration**: Built-in support for **Flash Attention 2** and **SageAttention** for faster inference.
  - **Fast Mode**: Optimized memory management with aggressive cache cleanup to prevent conflicts between CPU offloading and GPU processing.

- **Simplified Workflow**: No need for complex external text encoding nodes. The model uses pre-computed stylistic embeddings (prompt_embeds.pth) for maximum efficiency.

##



<table style="width: 100%;">
  <tr>
    <td style="width: 50%; text-align: center;">
      <video src="https://github.com/user-attachments/assets/e10c2435-fc72-46d4-bfa0-5203a74b2a93" width="100%" controls></video>
    </td>
    <td style="width: 50%; text-align: center;">
      <video src="https://github.com/user-attachments/assets/3d6310fa-f1c4-4c04-bf34-1fe0c05d3457" width="100%" controls></video>
    </td>
    <td style="width: 50%; text-align: center;">
      <video src="https://github.com/user-attachments/assets/e65001fc-f181-4da7-bd97-4f36e7700ffe" width="100%" controls></video>
     <td style="width: 50%; text-align: center;">
      <video src="https://github.com/user-attachments/assets/11c504e5-bfee-4847-846f-87f1a567dfb8" width="100%" controls></video>
    </td>
    </td>
  </tr>
</table>





## 📦 Installation

Navigate to your ComfyUI custom nodes directory:

```bash
cd ComfyUI/custom_nodes/
```

Clone this repository:

```bash
git clone https://github.com/aistudynow/Comfyui-tetestyle-image-video.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

> **Note:** For SageAttention support, you may need to install `sageattention` manually.

## 📂 Model Setup

This node requires specific weights placed in the `ComfyUI/models/telestyle_models/` directory.

The weights are downloaded automatically at the first run

**Directory Structure:**

```
ComfyUI/
└── models/
    └── telestyle_models/
        ├── weights/
        │   ├── dit.ckpt            # Main Video Transformer weights
        │   └── prompt_embeds.pth   # Pre-computed style embeddings
        └── Wan2.1-T2V-1.3B-Diffusers/
        │   ├── transformer_config.json
        │   ├── vae/
        │   │   │   ├── diffusion_pytorch_model.safetensors
        │   │   │   └── config.json
        │   └── scheduler/
        │       └── scheduler_config.json
```

**Where to get weights:**

https://huggingface.co/Danzelus/TeleStyle_comfy/tree/main

## 🚀 Usage

### FP8 Qwen Image Workflow (Comfy Native)

Import:

- `workflow/TeleStyle_Qwen_FP8_Image.json`

Expected model files:

- `models/unet/Qwen-Image-Edit-2509_fp8_e4m3fn.safetensors`
- `models/clip/qwen_2.5_vl_7b.safetensors`
- `models/vae/qwen_image_vae.safetensors`
- `models/loras/diffsynth_Qwen-Image-Edit-2509-telestyle.safetensors`
- `models/loras/diffsynth_Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors`

### 1. TeleStyle Model Loader

This node loads the necessary model components.

| Parameter | Description |
|-----------|-------------|
| `dtype` | Choose between `bf16` (best quality), `fp16` |

### 2. TeleStyle Video Transfer

The main inference node.

| Parameter | Description |
|-----------|-------------|
| `model` | Connect the output from the Loader |
| `video_frames` | Input video batch (from Load Video or VHS_LoadVideo) |
| `style_image` | A reference image to guide the style transfer |
| `steps` | Inference steps (default: 12) |
| `cfg` | Guidance scale (default: 1) |
| `time_schedule` | Backward-compatibility selector for old workflows (`fixed`) |
| `scheduler` | Choose your sampler (`FlowMatchEuler`, `UniPC`, `DPM++`) |
| `fast_mode` | Keep `True` for speed. Set to `False` for low-VRAM offloading (slower) |
| `acceleration` | `sdpa` - PyTorch SDPA (safest default)<br>`flash_attn` - Force Flash SDP kernel when available<br>`sage_attn` - Use ComfyUI SageAttention backend (start ComfyUI with `--use-sage-attention`) |

### 3. TeleStyle Image Transfer (Official, Recommended)

These nodes wrap the official TeleStyle image architecture (Qwen Image Edit + TeleStyle LoRA):

- `TeleStyle Image Model Loader (Official)`
- `TeleStyle Image Transfer (Official)`

Install extra dependencies once:

```bash
pip install git+https://github.com/modelscope/DiffSynth-Studio.git@11315d7 transformers==4.57.3 accelerate==1.2.1
```

| Parameter | Description |
|-----------|-------------|
| `model` | Connect from `TeleStyle Image Model Loader (Official)` |
| `content_image` | Input content image |
| `style_image` | Style reference image |
| `prompt` | Style transfer instruction text |
| `steps` | Inference steps (official lightning default: 4) |
| `seed` | Random seed |
| `min_edge` | Resize target for the shorter edge (multiple of 16) |

`TeleStyle Image Model Loader (Official)` extra performance options:

| Parameter | Description |
|-----------|-------------|
| `attention_mode` | Default attention backend for this loaded pipeline (`sdpa`, `flash_attn`, `sage_attn`) |
| `auto_benchmark_attention` | Benchmarks `flash_attn` vs `sdpa` and auto-picks fastest stable mode for this load |
| `cache_policy` | `reuse_cached` keeps model in memory for faster next runs, `force_reload` clears and reloads |
| `vram_cleanup_before_load` | Optional Comfy cleanup before load: `none`, `soft_empty_cache`, `unload_all_models` |
| `compile_dit` | Enable `torch.compile` on Qwen DiT (first run slower, later runs can be faster) |
| `enable_tf32` | Enable TF32 matmul/cudnn speedups on supported NVIDIA GPUs |
| `enable_vram_management` | Enable DiffSynth offload/VRAM management for low-memory GPUs (slower but safer) |
| `vram_limit_gb` | Optional VRAM budget hint for DiffSynth (`0` = auto/default behavior) |
| `clear_result_cache` | Clears cached image outputs for this node run |

Official loader mode:

- HuggingFace-only pipeline for stability.
- Local model-file selection has been removed from this node.

Fast defaults:

- `dtype=fp16`
- `attention_mode=sdpa` (stable default)
- `auto_benchmark_attention=True` (if you want auto-pick for your GPU)
- `cache_policy=reuse_cached`
- `compile_dit=False` (set `True` only after a first successful run)
- `enable_vram_management=False`
- `steps=4`
- `min_edge=512`

Performance notes:

- Official image inference now has an in-memory result cache for repeated identical runs (same content/style/prompt/seed/steps/size).
- `auto_benchmark_attention` adds a short warmup benchmark on load; reload is slower once, then cached runs are faster.
- If `flash_attn` gives invalid/black output, the node now retries once automatically with `sdpa`.
- If PyTorch raises `CUDAMallocAsyncAllocator` internal assert at high resolution, the node auto-recovers once (soft cache cleanup + TF32 off + `sdpa` retry).
- If a run gets stuck or behaves wrong, set `cache_policy=force_reload` once to clear runtime cache and reload.
- `vram_cleanup_before_load=soft_empty_cache` or `unload_all_models` is for recovery/OOM situations, not for every run.
- `attention_mode=sage_attn` uses ComfyUI global SageAttention backend and requires launching ComfyUI with `--use-sage-attention`.
- `enable_vram_management=True` is useful for low VRAM but can be much slower because of extra CPU/GPU movement.
- If allocator asserts continue, launch ComfyUI with `--disable-cuda-malloc` to avoid CUDA async allocator issues.
- HuggingFace Space demos often run on much larger GPUs (for example H100-class), so local consumer GPUs can be significantly slower at the same resolution.
- Keep only one `TeleStyle Image Model Loader (Official)` in the graph. Changing loader options creates a new model config; this build now auto-clears old TeleStyle image caches to reduce OOM risk.
- Qwen Image Edit uses separate components (DiT + text encoder + VAE). A single merged DiT+text-encoder safetensors file is not the standard format for this official DiffSynth pipeline.

___
## To-Do List
- [x] Initial release
- [ ] More samplers
- [ ] Consistency for very long videos 
___
Guys, I’d really appreciate any support right now. I’m in a tough spot:



## 📜 Credits

This project is an unofficial implementation based on the amazing work by the original authors.
Please refer to their repository for the original research and model weights.
