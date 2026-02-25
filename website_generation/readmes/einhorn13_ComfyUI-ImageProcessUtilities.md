# ComfyUI-ImageProcessUtilities

A collection of custom nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) designed to enhance image processing workflows. Especially useful for high-resolution rendering, complex inpainting, tiling, and batch manipulation. This allows you to perform processing that would otherwise exceed your VRAM limits.

---

## Key Features

- **Image Tiling & Untiling**  
  Break large images into overlapping tiles and reassemble them seamlessly without losing data.

- **Coordinate-Based Transforms**  
  Crop and paste image regions using flexible coordinate inputs.

- **Coordinate Utilities**  
  Convert strings to coordinates and manipulate coordinate lists for dynamic workflows.

- **Batch Tools**  
  Reorder or adjust batches of images for animation, video, or layout tasks.

---

## Available Nodes

### Tiling
- `ImageTiler`
- `ImageUntiler`

### Transform
- `CropByCoords`
- `PasteByCoords`
- `ReorderBatch`

### Coordinates
- `StringToIntegers`
- `CombineCoords`
- `SplitCoords`

---

## Installation

1. Navigate to your `ComfyUI/custom_nodes/` directory:
   ```bash
   cd ComfyUI/custom_nodes/

2. Clone this repository: git clone <repository_url>

3. Restart ComfyUI.

Example usecase: High-Resolution Upscaling Workflow

This allows you to upscale images that would otherwise exceed your VRAM limits.
