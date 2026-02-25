# ComfyUI Unusual Tools

A collection of unusual but useful image processing nodes for ComfyUI.

## Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/ComfyUI-Unusual-Tools.git
```

2. Restart ComfyUI

## Nodes

### Auto Image Resize

Resizes an image to fit a target dimension while maintaining aspect ratio. The image is centered in the target dimensions and a feathering mask is created for the edges.

**Inputs:**
- `image`: The input image
- `target_width`: Target width (pixels)
- `target_height`: Target height (pixels)
- `feathering`: Feathering amount for the edges (pixels)

**Outputs:**
- `IMAGE`: The resized image
- `MASK`: A mask for the resized area

### Adjust Crop

Automatically crops an image to remove excess white or transparent areas. Useful for removing unnecessary borders from images.

**Inputs:**
- `image`: The input image
- `threshold`: Brightness threshold for detecting white pixels (0.0-1.0)
- `padding`: Additional padding around the cropped area (pixels)
- `mode`: Crop mode - "white" (remove white areas), "transparent" (remove transparent areas), or "both"

**Outputs:**
- `IMAGE`: The cropped image

### Batch Save Latent & Image

Saves latents and their corresponding images to disk. Supports batch processing and automatically handles single/multiple items.

**Inputs:**
- `latent`: The latent to save
- `image`: The image to save
- `filenames`: List of filenames (one per line) to use for saving
- `save_directory`: Directory to save files (defaults to "latents", which saves to ComfyUI's output/latents folder)

**Outputs:**
- None (files are saved to disk)

### Batch Load Latent & Image

Loads latents and their corresponding images from disk. Supports batch processing by specifying multiple filenames.

**Inputs:**
- `filenames`: List of filenames (one per line) to load
- `load_directory`: Directory to load files from (defaults to "latents", which loads from ComfyUI's output/latents folder)

**Outputs:**
- `LATENT`: The loaded latent(s)
- `IMAGE`: The loaded image(s)

## Memory Management

The Batch Save/Load nodes are designed to help manage VRAM usage in complex workflows. By saving intermediate latents and images to disk, you can free up VRAM and then load them back when needed.

## Troubleshooting

If you encounter issues with saving or loading latents and images:

1. Check the ComfyUI console for detailed error messages
2. Ensure the "latents" directory exists in your ComfyUI output folder
3. Make sure you have write permissions to the output directory
4. Try using absolute paths if relative paths aren't working
5. Verify that the filenames you're trying to load actually exist in the specified directory

## License

MIT 