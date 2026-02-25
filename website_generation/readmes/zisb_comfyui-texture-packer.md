# ComfyUI Texture Packer - Alpha Edge Solidify

A ComfyUI custom node that converts RGBA-style assets into fully solid RGB textures by bleeding edge colours outward from the alpha mask.

Intended for **foliage, grass, decals, and cutout assets** to prevent edge halos and mipmap bleeding in game engines.

<img width="1304" height="607" alt="{1CF15327-E180-45AA-BC6A-25EF5AE841F2}" src="https://github.com/user-attachments/assets/26cbed17-2afb-4453-91b3-4f3b92ca2f9a" />


## The Problem

When working with alpha-cutout textures in game engines, the RGB data in transparent areas can cause visible artifacts:
- **Edge halos** - light or dark fringes around cutout edges
- **Mipmap bleeding** - colours from transparent regions bleeding into visible areas at lower mip levels
- **Atlas artifacts** - neighbouring textures contaminating edges in texture atlases

Artists typically solve this with a "solidify" or "alpha bleed" pass in tools like Photoshop, Substance Painter, or TexturePacker.

This node brings that workflow into ComfyUI.

## Installation

1. Clone or download this repository
2. Place the folder in your `ComfyUI/custom_nodes/` directory
3. Restart ComfyUI

```
ComfyUI/
└── custom_nodes/
    └── comfyui-texture-packer/
        ├── __init__.py
        ├── nodes.py
        └── README.md
```

## Usage

1. Load your RGBA texture using **Load Image**
2. Connect the `IMAGE` output to the node's image input
3. Connect the `MASK` output to the node's mask input
4. Run the workflow
5. Save the resulting solid RGB texture

> **Note:** ComfyUI auto-inverts masks from Load Image. You may need to use an **Invert Mask** node before connecting to this node.

## Node: Alpha Edge Solidify -> RGB

### Inputs

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| `image` | IMAGE | - | RGB input from Load Image |
| `mask` | MASK | - | Alpha mask from Load Image |
| `bleed_pixels` | INT | 64 | How many pixels to bleed outward (1-256) |
| `mask_threshold` | FLOAT | 0.5 | Threshold for what counts as "inside" the mask (0-1) |
| `kernel_size` | INT | 3 | Dilation kernel size: 3, 5, or 7 |
| `mode` | ENUM | basic | `basic` for speed, `smooth` for quality |

### Output

| Output | Type | Description |
|--------|------|-------------|
| `image` | IMAGE | Fully solid RGB texture (no alpha) |

### Modes

- **basic** - Fast iterative dilation using uniform neighbor averaging. Good for most use cases.
- **smooth** - Distance-weighted averaging for smoother colour gradients. Better for large bleed distances.

## Use Cases

- Game engine assets (Unity, Unreal, Godot, etc.)
- Foliage and vegetation textures
- Decals and stickers
- UI elements with alpha cutouts
- Texture atlas preparation
- Any mip-mapped alpha-tested materials

## Requirements

- ComfyUI
- PyTorch (included with ComfyUI)

No additional dependencies required.

## License

MIT

---

*This project was built with [Claude Code](https://claude.ai/code).*
