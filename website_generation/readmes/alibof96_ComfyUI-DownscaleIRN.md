# ComfyUI Invertible Rescale (Downscale only)

A single-node ComfyUI wrapper for Invertible Image Rescaling (IRN) downscaling with:
- Auto-download of models (selected or all) from the official Google Drive folder
- Automatic discovery of local `.pt`/`.pth` models
- BasicSR `.pth` loader (vendored minimal IRN network) for IRN_x2/x3/x4
- Device and precision control
- Tiling for low VRAM
- Safe handling of sizes not divisible by the scale
- Alpha channel preservation
- Built-in bicubic/area fallback

## Install

1. Copy this folder to:
   ```
   ComfyUI/custom_nodes/comfyui_invertible_rescale
   ```
2. Restart ComfyUI.

Optional dependencies:
```
pip install torch torchvision
pip install gdown   # for Google Drive auto-download
```

## Models

Official IRN pretrained models (`IRN_x2.pth`, `IRN_x3.pth`, `IRN_x4.pth`) are hosted at:
- https://drive.google.com/drive/folders/1ym6DvYNQegDrOy_4z733HxrULa1XIN92

This node will:
- Auto-download the selected model if `auto_download_selected` is ON and missing.
- Optionally download all available models if `auto_download_all` is ON.
- Discover and list all `.pt`/`.pth` files in:
  ```
  ~/ComfyUI/models/invertible_rescale
  ```

You can also set direct URLs (and SHA256) in `model_registry.json` if you prefer non-GDrive hosting.

## Node: IRN Downscale

Inputs:
- `image`: an IMAGE tensor
- `model_key`:
  - `auto_best_match`: uses `IRN_x{scale}` if found (downloads if enabled), else builtin.
  - `builtin_bicubic`: standard PyTorch downscale (bicubic/area).
  - Any discovered local/registered model (dropdown).
- `scale`: 2 / 3 / 4
- `device`: auto / cuda / cpu / mps
- `precision`: fp16 / bf16 / fp32
- `tile_size`, `tile_overlap`: enable tiling to reduce memory load
- `not_divisible_mode`: pad / crop / resize_to_multiple
- `builtin_mode`: bicubic / area (only for builtin)
- `keep_alpha`: preserve alpha (downscaled with area)
- `auto_download_selected`, `auto_download_all`, `use_google_drive`, `models_dir_override`

Outputs:
- `image`: downscaled image
- `meta`: model used, device, timing, available models, and any load error

## License

MIT
