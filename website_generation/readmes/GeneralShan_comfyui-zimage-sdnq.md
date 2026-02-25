
# ComfyUI Z-Image SDNQ

Custom ComfyUI nodes for running Z-Image Turbo with SDNQ quantization (q8/q4). Supports text-to-image, image-to-image, inpaint, ControlNet, and LoRA.

## Layout

- `core/`: device selection, SDNQ helpers, image conversion.
- `zimage/`: adapted Z-Image pipelines/models.
- `vendor/`: upstream snapshots for reference only.
- `workflows/`: minimal ComfyUI graphs.

## Models

Put models so they show up in dropdowns:

- Diffusers models:
  - `models/diffusers/Z-Image-Turbo-SDNQ-int8`
  - `models/diffusers/Z-Image-Turbo-SDNQ-uint4-svd-r32`
- ControlNet weights:
  - `models/controlnet/Z-Image-Turbo-Fun-Controlnet-Union-2.1-8steps.safetensors`

The loader dropdown enumerates `models/diffusers/**/model_index.json`.

Put LoRAs under `models/loras`.

