# ComfyUI-DJZ-Offsquare

A ComfyUI custom node that creates optimized image collages from batches of 2-6 images with intelligent layout selection and aspect ratio control.

## Features

- **Multiple Layout Strategies** — 3 layouts per image count (2-6 images)
- **Aspect Ratio Selection** — 1:1, 16:9, 9:16, 3:2, 2:3, 4:3, 3:4
- **Consistent Output Size** — Maintains ~4 megapixels (same as 2048×2048)
- **Smart Image Placement** — First image → top-left, Last image → bottom-right with spill effect
- **Aspect-Ratio Aware** — Matches images to regions for minimal clipping
- **Auto Layout** — Automatically selects best layout based on image dimensions

## Installation

### Option 1: Git Clone (Recommended)

1. Navigate to your ComfyUI custom nodes folder:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/MushroomFleet/ComfyUI-DJZ-Offsquare.git
   ```

3. Restart ComfyUI

### Option 2: Manual Installation

1. Download the repository as a ZIP file
2. Extract to `ComfyUI/custom_nodes/ComfyUI-DJZ-Offsquare/`
3. Restart ComfyUI

The node will appear under: **image/compositing → DJZ Offsquare Collage**

## Inputs

| Input | Type | Description |
|-------|------|-------------|
| `images` | IMAGE | Batch of 2-6 images |
| `aspect_ratio` | Dropdown | Output aspect ratio (default: 1:1) |
| `border_radius` | INT (0-64) | Corner radius for image regions |
| `background_color` | STRING | Hex color for canvas background |

## Outputs

| Output | Type | Description |
|--------|------|-------------|
| `image` | IMAGE | The generated collage |
| `layout_info` | STRING | Layout details (type, dimensions, etc.) |

## Automatic Layout Selection

The node automatically selects the best layout based on your images' aspect ratios. Available layouts per image count:

| Images | Available Layouts |
|--------|-------------------|
| 2 | diagonal, vsplit, hsplit |
| 3 | cascade, l-shape, reverse-l |
| 4 | grid, dominant-three, t-layout |
| 5 | quincunx, asymmetric, l-shape |
| 6 | grid-2x3, grid-3x2, feature-corner |

## Aspect Ratios & Dimensions

All ratios maintain ~4,194,304 total pixels:

| Ratio | Dimensions | Use Case |
|-------|------------|----------|
| 1:1 | 2048 × 2048 | Square |
| 16:9 | 2731 × 1536 | Widescreen |
| 9:16 | 1536 × 2731 | Vertical/Mobile |
| 3:2 | 2509 × 1672 | Classic Photo |
| 2:3 | 1672 × 2509 | Portrait Photo |
| 4:3 | 2365 × 1774 | Standard |
| 3:4 | 1774 × 2365 | Portrait Standard |

## Usage Tips

1. **Image Order Matters** — First image in batch goes to top-left (background), last image goes to bottom-right (foreground with spill)

2. **Batch Creation** — Use a "Batch Images" node to combine individual images before connecting to this node

3. **Chain with Save** — Connect output directly to "Save Image" node for export

## Example Workflow

```
[Load Image 1] ─┐
[Load Image 2] ─┼─► [Batch Images] ─► [DJZ Offsquare] ─► [Save Image]
[Load Image 3] ─┤
[Load Image 4] ─┘
```

## Requirements

- ComfyUI (latest version recommended)
- Python 3.8+
- PIL/Pillow
- PyTorch
- NumPy

## License

MIT License

## Citation

```bibtex
@software{djz_offsquare,
  title = {DJZ-Offsquare: Intelligent Image Collage Component},
  author = {Drift Johnson},
  year = {2025},
  url = {https://github.com/MushroomFleet/ComfyUI-DJZ-Offsquare},
  version = {1.0.0}
}
```

## Support

[![Ko-Fi](https://cdn.ko-fi.com/cdn/kofi3.png?v=3)](https://ko-fi.com/driftjohnson)
