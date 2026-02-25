# ComfyUI-Mosaic

ComfyUI custom nodes for mosaic detection and creation.

![ComfyUI-Mosaic](https://github.com/user-attachments/assets/6067a240-0961-4905-b5f3-23824a389e1d)

## Features

- **Mosaic Detection**: Detect mosaic patterns in images using computer vision
- **Mosaic Creation**: Create various mosaic effects (squares, circles, hexagons, gradients)
- **Pattern Types**: Multiple mosaic patterns with customizable parameters
- **Mask Support**: Apply effects to specific areas using masks

## Installation

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes
```

2. Clone this repository:
```bash
git clone https://github.com/1038lab/ComfyUI-Mosaic.git
```

3. Install dependencies:
```bash
cd ComfyUI-Mosaic
pip install -r requirements.txt
```

4. Restart ComfyUI

## Nodes

### MosaicCreator

Create mosaic effects on images.

**Parameters:**
- `image`: Input image
- `mosaic_type`: Pattern type (pixelation, blur, block_average, squares, circles, hexagons, gradient_horizontal, gradient_vertical)
- `block_size`: Mosaic block size (2-100)
- `intensity`: Effect intensity (0.0-1.0)
- `mask`: Optional mask for selective application

**Outputs:**
- `image`: Processed image
- `processing_mask`: Applied mask

### MosaicDetector

Detect mosaic patterns in images.

**Parameters:**
- `image`: Input image
- `top_n`: Number of top detections (1-20)
- `mask_expand`: Mask expansion size (0-64)
- `mask_blur`: Mask edge blur (0-64)
- `invert_mask`: Invert final mask
- `overlay_color`: Visualization color
- `overlay_opacity`: Overlay transparency (0.0-1.0)

**Outputs:**
- `image`: Original image
- `mask_overlay`: Visualization overlay
- `mask`: Detection mask

## Usage

1. Add nodes to your ComfyUI workflow
2. Connect image inputs
3. Adjust parameters as needed
4. Process images

## Requirements

- ComfyUI
- Python 3.8+
- PyTorch ≥1.9.0
- OpenCV ≥4.5.0
- Pillow ≥8.0.0
- NumPy ≥1.21.0

## License

GPLv3 License - see LICENSE file for details.
