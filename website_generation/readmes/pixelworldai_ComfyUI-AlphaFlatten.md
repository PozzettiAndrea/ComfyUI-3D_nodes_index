# ComfyUI-AlphaFlatten

A custom node for ComfyUI that flattens a batch of images with alpha channels into a single image, similar to Photoshop's flatten function.

## Description

This node takes a batch of images with alpha channels (RGBA format) and combines them into a single image, respecting the transparency of each layer. It's particularly useful for compositing multiple masked elements (like faces) into a single image.

## Features

- Combines multiple images with alpha channels into a single image
- Supports various background options:
  - Black background
  - White background
  - Transparent background (preserves alpha channel)
  - Custom color background (RGB values)
- Properly handles alpha blending for realistic compositing
- Works with any number of images in a batch

## Installation

1. Clone this repository into your ComfyUI's `custom_nodes` directory:
   ```
   cd ComfyUI/custom_nodes
   git clone https://github.com/yourusername/ComfyUI-FlattenByAlpha.git
   ```
   
2. Restart ComfyUI if it's already running.

## Usage

1. In ComfyUI, find the "Flatten Images By Alpha" node under the "image/processing" category.
2. Connect a batch of RGBA images to the "images" input.
3. Select a background color option:
   - `black`: Use a black background
   - `white`: Use a white background
   - `transparent`: Maintain transparency in the output
   - `custom`: Define a custom RGB color using the color sliders
4. If you selected `custom`, adjust the R, G, and B values to create your desired background color.
5. The node will output a single flattened image.

## Use Cases

This node is particularly useful for:

- Compositing multiple face or object masks into a single image
- Combining multiple transparent layers from image generation
- Creating complex compositions from individually generated elements
- Simulating Photoshop's "flatten layers" functionality within ComfyUI workflows

## Technical Details

The node processes each image in the batch sequentially, blending them together based on their alpha channels. Images later in the batch will appear "on top" of earlier images, similar to how layers work in image editing software.

For transparent backgrounds, the node preserves the alpha channel in the output, allowing for further compositing in downstream nodes.

## Requirements

- ComfyUI
- PyTorch
