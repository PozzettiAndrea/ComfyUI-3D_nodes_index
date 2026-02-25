# ComfyUI-Wanify: Adaptive Image Resize Node

This custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) provides adaptive image resizing based on target pixel counts, maintaining aspect ratio and supporting different quality levels. It is useful for workflows that require images to fit within specific pixel budgets (e.g., for video, AI models, or memory constraints).

## Features
- Resize images to target pixel counts (720p/480p, high/medium/low quality)
- Maintains aspect ratio
- Outputs resized image, width, height, and total pixel count
- Fast and quality modes

## Installation
1. Download or clone this repository:
   ```sh
   git clone https://github.com/blird/ComfyUI-Wanify.git
   ```
2. Copy the `comfyui-wanify` folder into your `ComfyUI/custom_nodes/` directory.
3. Restart ComfyUI. The node will appear as "Adaptive Image Resize" under the `image/transform` category.

## Usage
- **Inputs:**
  - `image`: Input image tensor (ComfyUI format)
  - `model`: Target resolution model (`720p` or `480p`)
  - `quality`: Quality setting (`high`, `medium`, `low`)
  - `fast_mode`: Boolean, use fast interpolation (default: True)
- **Outputs:**
  - `image`: Resized image
  - `width`: Output width
  - `height`: Output height
  - `total_pixels`: Output width * height

## Example
```
Adaptive Image Resize
  ├─ image: (input image)
  ├─ model: 720p
  ├─ quality: high
  └─ fast_mode: True
Outputs:
  ├─ image: (resized image)
  ├─ width: 1280
  ├─ height: 720
  └─ total_pixels: 921600
```

## Requirements
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- PyTorch (ComfyUI default)

## License
[Add your license here] 