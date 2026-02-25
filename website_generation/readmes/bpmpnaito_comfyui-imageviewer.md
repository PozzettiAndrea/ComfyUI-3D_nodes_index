# ComfyUI Image Viewer

Image viewer node that displays preview of images directly in the node.

## Installation

1. Copy this folder to `ComfyUI/custom_nodes/comfyui-imageviewer`
2. Restart ComfyUI

## Usage

1. Add the "Image Viewer" node from the image category
2. Connect any IMAGE output to the Image Viewer input
3. Run the workflow - the image preview will appear in the node

## Features

- Shows image preview directly in the node
- Supports multiple images
- Displays image count
- Works as pass-through (outputs the same images it receives)

## Files

- `nodes.py` - Python node with preview functionality
- `web/imageviewer.js` - JavaScript for in-node preview display
- `__init__.py` - ComfyUI registration