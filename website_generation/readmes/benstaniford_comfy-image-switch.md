# ComfyUI Image Switch Node

An image source switch node for ComfyUI that allows you to select one image from up to 8 input image sources.

## Features

- **Multiple Image Inputs**: Supports up to 8 optional image inputs
- **Dynamic Selection**: Use an integer input (1-8) to select which image to output
- **Fallback Behavior**: If the selected image slot is empty, automatically falls back to the first available image
- **Default Output**: Creates a black 512x512 image if no images are connected

## Installation

### Method 1: Manual Installation
1. Clone or download this repository
2. Copy the entire folder to your ComfyUI custom nodes directory:
   ```
   ComfyUI/custom_nodes/comfy-image-switch/
   ```
3. Restart ComfyUI

### Method 2: Git Clone
Navigate to your ComfyUI custom nodes directory and run:
```bash
git clone https://github.com/yourusername/comfy-image-switch.git
```

## Usage

1. Add the "Image Switch" node to your ComfyUI workflow
2. Connect up to 8 image sources to the optional image inputs (`image_1` through `image_8`)
3. Set the `select` parameter to choose which image to output (1-8)
4. The selected image will be output from the node

## Node Details

- **Category**: `image/switch`
- **Inputs**:
  - `select` (required): Integer from 1-8 to select which image to output
  - `image_1` through `image_8` (optional): Image inputs
- **Outputs**:
  - `image`: The selected image

## Examples

### Basic Usage
1. Connect multiple image sources (Load Image nodes, generators, etc.) to the image inputs
2. Use the select parameter to switch between them
3. Connect the output to other nodes in your workflow

### Dynamic Switching
You can connect the `select` input to other nodes that generate integers to dynamically switch between images during batch processing.

## Requirements

- ComfyUI
- PyTorch
- Python 3.8+

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
