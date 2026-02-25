# ComfyUI My Template Nodes

A collection of utility nodes for ComfyUI, focusing on batch processing, stitching, and visualization.

**[中文说明 (Chinese Version)](README_ZH.md)**

## Features

This node pack includes the following functionalities. The input ports for all nodes can be dynamically expanded using the `inputcount` widget.

**Note**: The dynamic input logic is adapted from **[KJNodes](https://github.com/kijai/ComfyUI-KJNodes)**. Special thanks to the author for the implementation.

### 1. Multiple Text Inputs
Connects multiple text strings into a single output string using a custom delimiter.
- Useful for prompt composition or batching text parameters.

![Text Node Example](assets/example1.png)

### 2. Multiple Masks to RGB Image
Converts multiple mask inputs into a single RGB image where each mask is represented by a unique color.
- **Features**: Includes options for binarization (thresholding) and noise removal (removing small isolated pixels) to clean up mask edges before visualization.
- **Output**: Returns the visual image and a string report of the colors used (RGB/Hex).

![Mask to RGB Example](assets/example2.png)

### 3. Multiple Image Stitch
Stitches multiple images (or image batches) into a single large image.
- **Direction**: Supports stitching "right" (horizontal) or "down" (vertical).
- **Resizing**: Automatically handles resizing images to match the base dimension and offers a final output resize option.
- **List Output**: Also returns a flat list of all input images, useful for converting individual inputs into a batch/list for other nodes.

![Image Stitch Example](assets/example3.png)

### 4. Multiple Mask Stitch
Similar to the Image Stitch node but specialized for masks.
- Stitches multiple masks horizontally or vertically.
- Returns both the stitched mask and a list of individual masks.

![Mask Stitch Example](assets/example4.png)

## Usage

1. **Adjust Input Count**: Change the `inputcount` value to the desired number of inputs.
2. **Update Ports**: The node will automatically update (or click "Update inputs" if available in your UI context) to show the new input slots.
3. **Connect**: Link your Strings, Images, or Masks.

## Installation

1. Clone this repository into your `ComfyUI/custom_nodes/` folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt