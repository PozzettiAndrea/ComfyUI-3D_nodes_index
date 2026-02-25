# ComfyUI-Switti

Custom nodes for running the [Switti](https://github.com/yandex-research/switti) text-to-image model inside [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

## Nodes

- Load Switti Checkpoint
- Load Switti VAE Checkpoint
- Load Switti Dual CLIP
- Build Switti Pipeline
- Switti Sampler

## Required Models

You must provide three sets of weights:

1. Switti core checkpoint (`.safetensors`)  
2. Switti VQVAE checkpoint (`.safetensors`)  
3. Two text encoders:
   - `clip-vit-large-patch14`
   - `CLIP-ViT-bigG-14-laion2B-39B-b160k`

The CLIP entries can be folders placed in `ComfyUI/models/text_encoders` or
`.safetensors` files with matching names in that same folder.

## Workflow

Load `workflows/switti_basic.json` in ComfyUI and fill in:

- Switti core checkpoint (diffusion_models folder)
- Switti VAE checkpoint (vae folder)
- CLIP encoders (text_encoders folder)

Make sure core and VAE resolutions match (512 or 1024).

![Workflow](workflow.png)

## Notes

- Standard SD VAEs and SDXL CLIP weights are not compatible with Switti.
- If CLIP inputs are swapped, you will get a size mismatch error.
