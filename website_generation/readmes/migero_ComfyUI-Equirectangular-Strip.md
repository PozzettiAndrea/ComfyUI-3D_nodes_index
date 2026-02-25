# ComfyUI-Equirectangular-Strip

Custom nodes for ComfyUI to convert between equirectangular (360°) images and a strip of 6 cube faces (90° FOV each).

<img width="1248" height="527" alt="Zrzut ekranu 2026-01-13 130835" src="https://github.com/user-attachments/assets/83f917b5-2a74-4c9b-b77a-7afdf21c3e48" />

## Nodes

### 360 → 6×90° Strip
Converts an equirectangular panorama into a horizontal strip of 6 perspective views:
- **Front** (0), **Left** (1), **Back** (2), **Right** (3), **Top** (4), **Bottom** (5)

**Inputs:**
- `image`: Equirectangular image
- `face_size`: Output size for each face (default: 512)
- `order`: Comma-separated face order (default: "0,1,2,3,4,5")
- `flip_sides`: Flip horizontal faces vertically (useful for person detection)

**Outputs:**
- `strip`: Horizontal strip image (width = face_size × 6)
- `order`: Pass-through for wiring to inverse node
- `flip_sides`: Pass-through for wiring to inverse node

### 6×90° Strip → 360
Converts a 6-face strip back to equirectangular projection.

**Inputs:**
- `strip`: The strip image
- `width`, `height`: Output equirectangular dimensions
- `face_size`: Size of each face in the strip
- `order`: Same order used during encoding
- `flip_sides`: Same setting used during encoding

## Installation

Copy this folder to your ComfyUI `custom_nodes` directory.

## Usage

1. Connect an equirectangular image to **360 → 6×90° Strip**
2. Process the strip (e.g., apply effects, run detection)
3. Connect to **6×90° Strip → 360** to reconstruct
4. Wire `order` and `flip_sides` outputs to inputs for correct reconstruction

## License

MIT
