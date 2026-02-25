# ColorMatrixGPU Node for ComfyUI

## Overview
This node applies a custom 4x4 color matrix to an image using GPU acceleration via PyTorch.

## Installation
1. Ensure PyTorch with CUDA support is installed:
```
pip install torch torchvision
```
2. Place `colormatrix_gpu_node.py` in your `custom_nodes` folder of ComfyUI.

## Usage
- Add the node `ColorMatrixGPU` in ComfyUI.
- Provide an image input.
- Input a 4x4 color matrix in comma-separated format (16 float values).

## Example Matrix
`1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1`

## License
MIT License
