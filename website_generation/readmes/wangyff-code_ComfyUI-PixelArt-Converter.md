
# ComfyUI PixelArt Converter

A ComfyUI custom node that converts images into Pixel Art using ONNX models.
Ported from [Original Project Name/Link] to ComfyUI.

## Features
- Converts any image to pixel art style.
- Supports 128x and 256x internal resolutions.
- Adjustable temperature, noise, and seed for variation.
- Runs fast using ONNX Runtime.

## Installation

1. Clone this repository into your `ComfyUI/custom_nodes/` folder:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/wangyff-code/ComfyUI-PixelArt-Converter.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Search for the node **"Pixel Art Converter (ONNX)"**.
2. Connect an image input.
3. Adjust `resolution` (128 or 256) for detail level.
4. **Tips**: 
   - `Resolution`: 128 is more abstract, 256 is more detailed.
   - `Temperature`: Controls color/style randomness.
   - `Noise`: Adds texture variations.

## Workflow Example
![Workflow Screenshot](workflow_screenshot.png) 