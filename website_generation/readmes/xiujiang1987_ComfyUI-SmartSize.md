# ComfyUI-SmartSize

A simple but essential custom node for ComfyUI that automatically detects image dimensions and snaps them to the nearest multiple of 16. This is critical for **Flux** and **SDXL** workflows to prevent `EinopsError` (shape mismatch) and ensure high-quality generation.

## Features
- **Auto-Detection**: Reads the width and height of any input image.
- **Safe Snapping**: Automatically adjusts dimensions to be multiples of 16 (e.g., 1000 -> 992).
- **Workflow Simplification**: No more manual width/height entry in KSampler or EmptyLatent nodes.

## Installation

### Method 1: Manual
1. Clone this repository into your `ComfyUI/custom_nodes/` folder:
   ```bash
   git clone https://github.com/xiujiang1987/ComfyUI-SmartSize.git
   ```
2. Restart ComfyUI.

### Method 2: ComfyUI Manager
(Coming soon)

## Usage
1. Add the node **"Smart Image Size (Flux/SDXL)"**.
2. Connect your **Load Image** node to the input.
3. Connect the `width` and `height` outputs to your **Empty Latent**, **ModelSamplingFlux**, or **ImageScale** nodes.
   - *Note: You may need to convert the target node's widgets to inputs first (Right-click node -> Convert Widget to Input).*

## License
MIT
