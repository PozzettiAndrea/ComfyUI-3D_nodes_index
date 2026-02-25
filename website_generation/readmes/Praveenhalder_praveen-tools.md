# Praveen's ComfyUI Custom Nodes

A collection of utility nodes for ComfyUI focused on image manipulation, tiling, batch processing, and workflow optimization.

## Features

### 📦 Image List Operations
- **Split Image List (3-Way)** - Split image batches into three separate lists with customizable ratios
- **Merge Image Lists (3-Way)** - Combine three image lists with configurable merge order
- **Select Last Image** - Extract the last image from a batch
- **Skip First Image** - Remove the first image from a batch

### 🎨 Image Adjustments
- **Brightness/Contrast/Saturation/RGB** - Comprehensive color and tone adjustments with per-channel RGB gain control
- **Diagonal Text Watermark** - Add customizable diagonal text watermarks to images

### 🔲 Tiling & Upscaling
- **Image Tile Split** - Divide images into overlapping tiles for processing large images
- **Image Tile Merge** - Reconstruct images from tiles with smart blending
- **Overlapping Image List Splitter** - Automatically split image batches with overlap
- **Overlapping Image List Merger** - Merge overlapping images with seamless blending

### 🛠️ Utilities
- **Image Dimensions (Multiple of 16)** - Set dimensions constrained to multiples of 16
- **Resolution Wan** - Quick resolution presets for common aspect ratios
- **RGB Channel Merger** - Combine separate R, G, B channels into a single image
- **Black Image Generator** - Create blank black images with specified dimensions
- **Load Image (with filename)** - Load images and output the filename
- **Extract Filename** - Extract filename without extension from file paths
- **Tile Info Display** - Debug utility to display tiling information

## Installation

### Method 1: Clone the Repository

Navigate to your ComfyUI custom nodes folder and clone this repository:

```bash
git clone https://github.com/Praveenhalder/praveen-tools.git
```

### Method 2: Manual Installation

1. Download the `Praveen_tools.py` file
2. Place it in your `ComfyUI/custom_nodes/` directory
3. Restart ComfyUI

## Requirements

- ComfyUI
- PyTorch
- PIL (Pillow)
- NumPy

All dependencies are typically included with a standard ComfyUI installation.

## Node Documentation

### Image List Operations

#### Split Image List (3-Way)
Splits a batch of images into three separate lists based on customizable ratios.

**Inputs:**
- `images` (IMAGE) - Input image batch
- `split_ratio_1` (FLOAT) - Ratio for first split (default: 0.33)
- `split_ratio_2` (FLOAT) - Ratio for second split (default: 0.33)

**Outputs:**
- `images_1`, `images_2`, `images_3` - Three separate image batches

#### Merge Image Lists (3-Way)
Combines three image lists into a single batch.

**Inputs:**
- `images_1`, `images_2`, `images_3` (IMAGE) - Three input image batches
- `merge_order` - Order to merge: "1-2-3", "1-3-2", "2-1-3", etc.

**Outputs:**
- `merged_images` - Combined image batch

### Image Adjustments

#### Brightness/Contrast/Saturation/RGB
Comprehensive image adjustment with individual channel control.

**Inputs:**
- `image` (IMAGE) - Input image
- `brightness` (FLOAT) - 0.0 to 2.0 (default: 1.0)
- `contrast` (FLOAT) - 0.0 to 2.0 (default: 1.0)
- `saturation` (FLOAT) - 0.0 to 2.0 (default: 1.0)
- `red_gain`, `green_gain`, `blue_gain` (FLOAT) - 0.0 to 2.0 (default: 1.0)

**Outputs:**
- Adjusted image

#### Diagonal Text Watermark
Adds customizable diagonal text watermarks across images.

**Inputs:**
- `image` (IMAGE) - Input image
- `text` (STRING) - Watermark text
- `font_size` (INT) - Text size (default: 120)
- `opacity` (FLOAT) - 0.0 to 1.0 (default: 0.2)
- `color` - Text color selection
- `angle` (FLOAT) - Rotation angle in degrees
- `spacing` (INT) - Space between repetitions
- `x_offset`, `y_offset` (INT) - Position offset

### Tiling & Upscaling

#### Image Tile Split
Divides large images into overlapping tiles for processing.

**Inputs:**
- `image` (IMAGE) - Input image
- `tile_size` (INT) - Size of each tile
- `overlap_percent` (FLOAT) - Overlap between tiles (0-50%)

**Outputs:**
- `tiles` (IMAGE) - Batch of tiles
- `tile_info` (TILE_INFO) - Metadata for reconstruction

#### Image Tile Merge
Reconstructs original image from processed tiles with smart blending.

**Inputs:**
- `tiles` (IMAGE) - Processed tiles
- `tile_info` (TILE_INFO) - Metadata from split operation
- `crop_percent` (FLOAT) - Amount of overlap to crop (0-100%)
- `fade_percent` (FLOAT) - Blending zone size (0-100%)
- `blend_mode` - "linear", "cosine", or "sigmoid"

**Outputs:**
- Reconstructed image

### Utilities

#### Image Dimensions (Multiple of 16)
Outputs width and height constrained to multiples of 16, useful for stable diffusion models.

**Inputs:**
- `width` (INT) - Width in pixels (step: 16)
- `height` (INT) - Height in pixels (step: 16)

**Outputs:**
- `width`, `height` (INT)

#### Resolution Wan
Quick access to common aspect ratios and resolutions.

**Inputs:**
- `aspect_ratio` - Predefined ratios (1:1, 16:9, 9:16, etc.)
- `megapixels` (FLOAT) - Target megapixels (default: 1.0)

**Outputs:**
- `width`, `height` (INT)

## Use Cases

### High-Resolution Image Processing
Use the tile split/merge nodes to process images larger than your GPU memory allows:

1. **Image Tile Split** - Break into manageable tiles
2. Process tiles (upscale, denoise, etc.)
3. **Image Tile Merge** - Seamlessly reconstruct

### Batch Processing Workflows
Split batches for different processing paths, then merge:

1. **Split Image List** - Separate into thirds
2. Apply different effects to each third
3. **Merge Image Lists** - Recombine in desired order

### Color Grading
Use the **Brightness/Contrast/Saturation/RGB** node for precise color correction with individual RGB channel control.

### Watermarking
Add professional diagonal watermarks with the **Diagonal Text Watermark** node.

## Tips & Best Practices

- **Tiling**: Use 20-30% overlap for seamless blending
- **Blending**: Cosine mode provides the smoothest transitions
- **Performance**: Larger tiles = fewer tiles but more VRAM per tile
- **Crop**: Start with 50% crop and adjust if you see seams

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

GPL-3.0 License

## Credits

Created by Praveen

## Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions

## Changelog

### Version 1.0
- Initial release with 18 custom nodes
- Image list operations
- Tiling and merging capabilities
- Color adjustment tools
- Utility nodes for workflow optimization

---

**Note**: This is a custom node collection for ComfyUI. Make sure you have ComfyUI installed and running before using these nodes.
