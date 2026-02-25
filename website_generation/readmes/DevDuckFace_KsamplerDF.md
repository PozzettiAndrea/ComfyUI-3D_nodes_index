# KSampler DF (with Refiner & Upscale)

![screenshot](/Screenshot_4.png)

A custom ComfyUI node that splits sampling steps between a main sampler and a refiner sampler, with latent upscale and optional model-based upscale.

## Changelog

### v1.0.2 (2026-01-27)
- 🔧 **IMPROVED**: Upscale model now selected directly via dropdown (no external node needed)
- 🔧 **IMPROVED**: VAE is now required for image output
- ✨ **NEW**: Automatic listing of all upscale models from `models/upscale_models/`

### v1.0.1 (2026-01-27)
- ✨ **NEW**: Latent upscale between main and refiner phases
- ✨ **NEW**: Separate CFG control for refiner phase (`cfg_refiner`)
- ✨ **NEW**: Optional model-based upscale after refinement
- ✨ **NEW**: Dual output: LATENT and IMAGE

### v1.0.0 (Initial Release)
- Basic KSampler with refiner functionality
- Split steps between main and refiner samplers
- Separate denoise control for each phase

## Features

- **Split Steps**: Divide total steps between main sampler and refiner sampler
- **Dual Sampler Support**: Use different samplers/schedulers for main and refiner phases
- **Independent CFG Control**: Separate CFG values for main and refiner phases
- **Independent Denoise Control**: Separate denoise parameters for main and refiner phases
- **Latent Upscale**: Optional upscale of latent between main and refiner phases
- **Model Upscale**: Built-in dropdown to select upscale models (ESRGAN, RealESRGAN, etc.)

## Installation

### Method 1: Git Clone (Recommended)

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/YOUR_USERNAME/ksamplerwithrefiner.git
```

Restart ComfyUI after installation.

### Method 2: Manual Installation

1. Download this repository as a ZIP file
2. Extract to `ComfyUI/custom_nodes/ksamplerwithrefiner/`
3. Restart ComfyUI

## Usage

Find the node under: `sampling` → `KSampler DF (with Refiner & Upscale)`

### Parameters

#### Main Sampling
| Parameter | Description |
|-----------|-------------|
| **model** | The diffusion model |
| **positive/negative** | Conditioning (prompts) |
| **latent_image** | Input latent |
| **seed** | Random seed |
| **steps** | Total steps (main + refiner) |
| **cfg** | CFG scale for main phase |
| **sampler_name** | Sampler for main phase |
| **scheduler** | Scheduler for main phase |
| **denoise** | Denoise for main phase |

#### Latent Upscale
| Parameter | Description |
|-----------|-------------|
| **latent_upscale_enabled** | Enable/disable |
| **latent_upscale_method** | nearest-exact, bilinear, area, bicubic, bislerp |
| **latent_upscale_factor** | Scale factor (e.g., 1.5) |

#### Refiner
| Parameter | Description |
|-----------|-------------|
| **refiner_at_step** | Step to switch to refiner |
| **sampler_refiner** | Sampler for refiner phase |
| **scheduler_refiner** | Scheduler for refiner phase |
| **cfg_refiner** | CFG scale for refiner phase |
| **denoise_refiner** | Denoise for refiner (0.0-1.0) |

#### Output & Upscale
| Parameter | Description |
|-----------|-------------|
| **vae** | VAE for decoding to image |
| **upscale_model_name** | Select upscale model or "none" to disable |

### Outputs

| Output | Description |
|--------|-------------|
| **LATENT** | Denoised latent |
| **IMAGE** | Decoded/upscaled image |

### Example

- **steps**: 20, **refiner_at_step**: 12

Result: 12 main steps → (latent upscale) → 8 refiner steps → VAE decode → (model upscale)

## Upscale Models

Place upscale models in `ComfyUI/models/upscale_models/`. They will appear automatically in the dropdown.

Supported models: ESRGAN, RealESRGAN, SwinIR, and other Spandrel-compatible models.

## Requirements

- ComfyUI (latest version)
- No additional dependencies

## License

MIT License


