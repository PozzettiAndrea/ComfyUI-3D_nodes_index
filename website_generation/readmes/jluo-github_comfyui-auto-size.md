# ComfyUI Auto Size

[![GitHub](https://img.shields.io/github/license/jluo-github/comfyui-auto-size)](LICENSE)
[![GitHub](https://img.shields.io/github/stars/jluo-github/comfyui-auto-size)](https://github.com/jluo-github/comfyui-auto-size)

A ComfyUI custom node for handling image resolutions with smart, model-aware presets for **2026 diffusion models**.

## 🌟 Supported Models

| Model | Use Case | Resolution Multiple | Source |
|-------|----------|---------------------|--------|
| **Qwen-Image** | Text-image-to-image | 28px | [Official docs](https://qwen.ai/) |
| **Illustrious** | Anime | 32px | Community standard |
| **Z-Image** | Text-image-to-image | 32px | [Official docs](https://z.ai/) |
| **Flux2-Klein/Flux** | Text-image-to-image | 32px | Similar to Z-Image/Illustrious |

## ✨ Features

- **Dynamic Dropdowns**: Size dropdown filters to show only relevant presets for your selected model
- **Model-Aware Snapping**: Automatically rounds resolutions to required multiples (28px or 32px)
- **Robust Resizing**: Multiple resize modes—`Center Crop`, `Scale to Fit`, `Stretch to Fill`

## 📦 Nodes

### Auto Size Latent
**Category**: `latent/AutoSize`

Generates an empty latent tensor at a model-aligned resolution.

| Input | Description |
|-------|-------------|
| `model` | Target model (qwen-image, z-image, flux, illustrious) |
| `size` | Preset or "Full Custom" |
| `custom_longer_size` | Longer side in pixels (set to 0 to use preset) |
| `custom_ratio` | Aspect ratio for custom mode |
| `batch_size` | Number of latents |

**Outputs**: `latent`, `width`, `height`, `size`

### Auto Size (Image/Mask)
**Category**: `image/AutoSize`

Resizes an existing image and/or mask to target dimensions.

| Input | Description |
|-------|-------------|
| `crop_method` | Center Crop, Top-Left Crop, Scale to Fit, Stretch to Fill |
| `scale_method` | lanczos, bicubic, bilinear, nearest |
| `image` | Optional input image |
| `mask` | Optional input mask |

**Outputs**: `image`, `mask`, `width`, `height`, `size`

## 🛠️ Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/jluo-github/comfyui-auto-size.git
```

Restart ComfyUI and reload the browser.

## ⚙️ Resolution Logic

1. **Custom Override** (`custom_longer_size > 0`): Calculates resolution from longer side + ratio, snapped to model's multiple
2. **Preset Mode** (`custom_longer_size = 0`): Uses the Size dropdown value directly

## � Project Structure

```
nodes/     ComfyUI node definitions
utils/     Core logic (presets, resizing)
js/        Dynamic dropdown behavior
tests/     Unit tests
```

## License

[MIT License](LICENSE)

---

Made with ❤️ for the ComfyUI community