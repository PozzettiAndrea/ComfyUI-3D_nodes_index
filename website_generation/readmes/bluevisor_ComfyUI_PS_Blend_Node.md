# ComfyUI PS Blend Node

This repository contains a simple custom node for ComfyUI that implements familiar PS-style blend modes using PyTorch. The `PSBlendNode` allows you to blend two images together using a variety of blending modes and an opacity parameter.

## Features

- Supports multiple blend modes including Normal, Darken, Multiply, Color Burn, Linear Burn, Lighten, Screen, Color Dodge, Linear Dodge, Overlay, Soft Light, Hard Light, Difference, Exclusion, Subtract, Divide, Hue, Saturation, Color, and Luminosity.
- Blends images with an adjustable opacity setting.

- (current version does not support alpha / transparency)

## Installation

To install this node, clone the repository into the `custom_nodes` directory of your ComfyUI installation:

```bash
cd path/to/ComfyUI/custom_nodes
git clone https://github.com/bluevisor/ComfyUI_PS_Blend_Node.git PSBlendNode
```
## Usage
- To use the PSBlendNode, follow these steps:
1. Load two images into your ComfyUI workflow, make sure they are the same size, resize or crop if necessary.
2. Connect the images to the PSBlendNode input.
3. Select a blend mode.
4. Blend away.
