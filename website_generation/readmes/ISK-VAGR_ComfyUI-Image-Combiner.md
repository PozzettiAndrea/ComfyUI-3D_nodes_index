# ComfyUI Image Combiner

A powerful ComfyUI custom node for combining and stitching multiple images with flexible layouts and advanced spacing options.

## Features

- **Multiple Layout Options**: Horizontal, vertical, and 2x2 grid arrangements
- **Flexible Spacing**: Configurable spacing between images with customizable colors
- **Dimension Preservation**: Option to preserve original image dimensions or normalize sizes
- **Smart Canvas Sizing**: Dynamic canvas creation that adapts to your image content
- **Multiple Input Support**: Combine up to 4 images in a single operation
- **Custom Filename Prefix**: Set your own naming convention for output files

## Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Go to the "Install Custom Nodes" tab
3. Search for "Image Combiner"
4. Click "Install"

### Method 2: Manual Installation
1. Clone this repository to your ComfyUI custom_nodes folder:
   ```bash
   git clone https://github.com/yourusername/ComfyUI-Image-Combiner.git
   ```
2. Restart ComfyUI

## Usage

### Node Inputs

**Required:**
- `image1`: The primary image to combine
- `layout`: Choose from "horizontal", "vertical", or "2x2_grid"
- `spacing`: Spacing between images (0-100 pixels)
- `spacing_color`: Color for spacing areas ("white", "black", "transparent")
- `preserve_dimensions`: Whether to preserve original image sizes ("enabled"/"disabled")
- `grid_mode`: For 2x2 grid, choose "original_size" or "adjusted_size"
- `filename_prefix`: Prefix for the output filename

**Optional:**
- `image2`, `image3`, `image4`: Additional images to combine (up to 4 total)

### Layout Options

1. **Horizontal**: Images are arranged side by side
2. **Vertical**: Images are stacked vertically
3. **2x2 Grid**: Images are arranged in a 2x2 grid pattern

### Spacing Options

- **Spacing**: Control the gap between images (0-100 pixels)
- **Spacing Color**: Choose the color for spacing areas:
  - White: Clean, professional look
  - Black: High contrast separation
  - Transparent: For compositing workflows

### Dimension Handling

- **Preserve Dimensions**: When enabled, maintains original image sizes
- **Grid Mode**: For 2x2 layouts, choose between original sizes or adjusted sizes

## Examples

### Basic Horizontal Stitching
```
Image1 → Image Combiner → Output
Image2 → Image Combiner
```

### 2x2 Grid with Spacing
```
Image1 → Image Combiner → Output
Image2 → Image Combiner
Image3 → Image Combiner
Image4 → Image Combiner
```

## Technical Details

- **Category**: ISK
- **Return Type**: IMAGE
- **Dependencies**: torch, Pillow, numpy
- **ComfyUI Compatibility**: >=1.0.0

## Workflow Integration

This node integrates seamlessly with ComfyUI workflows and can be used in combination with:
- Image generation nodes
- Image processing nodes
- Batch processing workflows
- Animation frame stitching

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/ComfyUI-Image-Combiner/issues) page
2. Create a new issue with detailed information about your problem
3. Include your ComfyUI version and any error messages

## Changelog

### Version 1.0.0
- Initial release
- Support for horizontal, vertical, and 2x2 grid layouts
- Configurable spacing and spacing colors
- Dimension preservation options
- Support for up to 4 images
