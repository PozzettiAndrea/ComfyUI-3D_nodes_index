# ComfyUI Loops

A custom node for ComfyUI that creates looping animations from image sequences.

## Description

The `LoopImageNode` takes a sequence of images and reorders them to create a seamless back-and-forth loop animation. The node works by taking the original sequence, then reversing the middle section (excluding the first and last images), and appending this reversed sequence to the original.

This results in a smooth loop effect where the animation plays forward and then backward without any noticeable hitches.

## Installation

1. Clone this repository into your ComfyUI custom_nodes directory:
   ```
   cd /path/to/ComfyUI/custom_nodes
   git clone https://github.com/yourusername/comfyui_loops.git
   ```

2. Restart ComfyUI

## Usage

1. In ComfyUI, locate the "Loop Image Sequence" node under the "Image Processing" category.
2. Connect a sequence of images to the node's input.
3. The node will output the reordered sequence for looping.

## Features

- Creates smooth looping animations from image sequences
- Handles edge cases with sequences that have fewer than 3 images
- Seamlessly integrates with other ComfyUI nodes

## Example Workflow

A typical workflow would be:
1. Generate or load a sequence of images
2. Pass them through the Loop Image Sequence node
3. Feed the output to animation/video nodes

## Requirements

- ComfyUI
- torch

## License

[MIT License](LICENSE) 