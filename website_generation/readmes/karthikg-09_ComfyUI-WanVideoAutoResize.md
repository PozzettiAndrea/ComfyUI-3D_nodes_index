# ComfyUI WanVideo Auto Resize

A high-performance ComfyUI custom node for intelligent image resizing with industry-standard presets and smart orientation detection. Optimized for video workflows and batch processing.

## Features

- **Industry Standard Presets**: 480p, 576p, 720p, 1080p resolutions
- **Smart Orientation Detection**: Automatic portrait/landscape/square detection with improved ranges
- **Multiple Resize Modes**: Keep Proportion, Pad, Crop, Stretch
- **Quality Options**: Multiple interpolation methods for different use cases
- **GPU Accelerated**: CUDA optimized with automatic mixed precision
- **Flexible Padding**: Black, White, Gray, or Blur edge options

## Installation

1. Clone into your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/your-username/ComfyUI-WanVideoAutoResize
   ```

2. Restart ComfyUI

## Usage

### Input Parameters

- **Preset Resolution**: Choose from standard resolutions or Custom
- **Resize Mode**: How to handle aspect ratio differences
- **Orientation Priority**: Auto-detect or force specific orientation
- **Interpolation**: Choose quality vs speed
  - `Bilinear`: Good balance of speed and quality (default)
  - `Bicubic`: Higher quality, slower processing
  - `Nearest`: Maximum speed, good for pixel art
  - `Lanczos`: High-quality downscaling

### Outputs

- **image**: Processed image tensor
- **width/height**: Final dimensions
- **orientation**: Detected orientation
- **aspect_ratio**: Final aspect ratio
- **resize_info**: Processing details

## Orientation Detection

Improved range detection handles near-square images better:
- **Square**: Aspect ratio 0.85-1.18 (e.g., 410×390 = 1.05)
- **Landscape**: Aspect ratio > 1.18
- **Portrait**: Aspect ratio < 0.85

## Performance

- **GPU Optimization**: Automatic CUDA acceleration when available
- **Memory Efficient**: Smart memory management for large images
- **Fast Interpolation**: Nearest neighbor for maximum speed
- **Quality Interpolation**: Bicubic and Lanczos for best results

## Example Workflows

### Fast Video Processing
```
Preset: 720p
Mode: Keep Proportion
Interpolation: Nearest
Orientation: Auto Detect
```

### High-Quality Output
```
Preset: 1080p
Mode: Pad
Interpolation: Bicubic
Orientation: Auto Detect
```

## License

MIT License - see LICENSE file for details.