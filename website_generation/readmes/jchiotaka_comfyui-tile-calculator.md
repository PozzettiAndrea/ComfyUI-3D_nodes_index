# ComfyUI Tile Calculator

A simple ComfyUI custom node that calculates tile dimensions for tiled upscaling workflows.

## What it does

Given an input image, magnification (zoom) factor, and desired number of tiles, this node calculates the optimal tile dimensions using the formula:

```
tile_dimension = ceil((original_dimension × zoom) / tiles_per_dimension)
```

The original image is passed through unchanged, making it easy to integrate into existing workflows.

## Installation

### Option 1: ComfyUI Manager

Search for "Tile Calculator" in the ComfyUI Manager and install.

### Option 2: Git Clone

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/jchiotaka/comfyui-tile-calculator.git
```

### Option 3: Manual

1. Download this repository
2. Extract to `ComfyUI/custom_nodes/comfyui-tile-calculator`
3. Restart ComfyUI

## Usage

Find the node at: **Add Node → image → utils → Tile Calculator**

### Inputs

| Input | Type | Description |
|-------|------|-------------|
| image | IMAGE | The input image |
| tiles_per_width | INT | Number of tiles horizontally (1-16) |
| tiles_per_height | INT | Number of tiles vertically (1-16) |
| zoom | FLOAT | Magnification factor (0.1-8.0) |

### Outputs

| Output | Type | Description |
|--------|------|-------------|
| image | IMAGE | Pass-through of the input image |
| tile_width | INT | Calculated tile width in pixels |
| tile_height | INT | Calculated tile height in pixels |

## Example

For a 1024×768 image with:
- zoom: 2.0
- tiles_per_width: 2
- tiles_per_height: 2

Results:
- tile_width: ceil((1024 × 2) / 2) = 1024
- tile_height: ceil((768 × 2) / 2) = 768

## License

MIT License - see [LICENSE](LICENSE) for details.
