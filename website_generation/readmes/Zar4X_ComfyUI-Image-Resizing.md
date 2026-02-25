# ComfyUI Image Resizing
*Precision dimension control nodes for aspect ratio adjustments and resizing workflows*

## Core Features

### 📐 Analysis & Calculation
- `image_aspect_ratio_extractor` - Extract aspect ratios with constraints (0.25-4.0 range)
- `image_resolution_extractor` - Extract specific dimensions (width, height, shortest/longest side)
- `calculate_aspect_ratio_extension` - Compute pixel extensions for target aspect ratios

### 🔧 Resizing & Cropping
- `smart_image_resize` - Intelligent resizing with min/max constraints, model-based upscaling, reference ratio matching, and standard ratio padding
- `resize_to_multiple` - Resize images to multiples of specified numbers (stretch/crop)
- `image_crop_by_percentage` - Precision cropping with percentage/pixel controls
- `mask_crop_by_percentage` - Synchronized mask cropping with detection modes
- `extend_canvas_by_percentage` - Expand canvas with color fill and feathering

## Key Features
- **Mathematical Precision** - Pixel-perfect calculations with rounding control
- **Dual Measurement Modes** - Seamless percentage ↔ pixel conversion
- **Non-Destructive Workflow** - All operations preserve source data
- **Advanced Detection** - Mask-based cropping with multiple detection algorithms

## Installation

1. Clone to your ComfyUI `custom_nodes` directory:
   ```
   ComfyUI/custom_nodes/image-resizing/
   ```

2. Restart ComfyUI

## Nodes Overview

### Analysis Nodes
- **Aspect Ratio Extractor**: Extracts ratios with constraints, supports rounding to common ratios
- **Resolution Extractor**: Extracts width, height, shortest, or longest side dimensions
- **Aspect Ratio Extension**: Calculates pixel extensions needed for target aspect ratios

### Processing Nodes
- **Smart Image Resize**: Intelligent image resizing with min/max resolution constraints, reference ratio matching, model-based or basic upscaling, and standard ratio padding
- **Resize to Multiple**: Resizes images to multiples of specified numbers (32, 64, etc.)
- **Image Crop by Percentage**: Precision cropping with 9 position options and offset controls
- **Mask Crop by Percentage**: Advanced mask-based cropping with detection algorithms
- **Extend Canvas by Percentage**: Expands canvas with color fill, feathering, and mask support

## Typical Use Cases
- Adapting assets for specific aspect ratios
- Matching images to reference aspect ratios without cropping
- Creating social media templates
- Matching AI model input requirements
- Batch canvas extensions and cropping

## Requirements
- ComfyUI
- Standard ComfyUI dependencies

## License
This project is provided as-is for the ComfyUI community.
