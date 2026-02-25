# Image Resizing Nodes - ComfyUI Custom Nodes

Two powerful ComfyUI custom nodes for intelligent image resizing while maintaining aspect ratio. Perfect for handling images of any size with precision and control.

## Nodes Included

### 1. **Aspect Ratio Resizer**
Precise control over image dimensions with flexible width/height constraints.

### 2. **Auto Megapixel Reducer**
Automatically reduces high-resolution images to a target megapixel count.

## Features

### **Aspect Ratio Resizer**
- **Flexible Constraints**: Enable/disable width or height constraints independently
- **Single Dimension Resizing**: Use only width OR only height to calculate the other dimension
- **Smart Scaling**: Only resizes when necessary based on your specified constraints
- **Multiple Resize Modes**: Choose between downscale only, upscale only, or both

### **Auto Megapixel Reducer**
- **Automatic Detection**: Detects high-resolution images (4K, 8K, etc.)
- **Megapixel Targeting**: Reduces to specific megapixel count (e.g., 2MP, 5MP)
- **Safe Mode**: Only reduces size, never upscales small images
- **Perfect for Large Images**: Handles any resolution while maintaining aspect ratio

### **Both Nodes**
- **Aspect Ratio Preservation**: Always maintains the original aspect ratio
- **Various Interpolation Methods**: Support for different interpolation algorithms
- **Batch Processing**: Handles multiple images in a single operation
- **Real-time Feedback**: Shows detailed resize information in the console

## Installation

1. Copy this entire folder to your ComfyUI `custom_nodes` directory:
   ```
   ComfyUI/custom_nodes/aspect-ratio-resizer/
   ```

2. Restart ComfyUI

3. Both nodes will appear in the "image/resize" category when you right-click to add a new node

## Usage

### Aspect Ratio Resizer - Inputs

- **images**: Input image(s) to resize
- **enable_width**: Enable/disable width constraint (default: True)
- **max_width**: Maximum allowed width (default: 1024, range: 64-8192)
- **enable_height**: Enable/disable height constraint (default: True)
- **max_height**: Maximum allowed height (default: 1024, range: 64-8192)
- **resize_mode**:
  - `downscale_only`: Only resize if image is larger than max dimensions
  - `upscale_only`: Only resize if image is smaller than max dimensions
  - `both`: Resize to fit max dimensions regardless of original size
- **interpolation**: Interpolation method for resizing
  - `bilinear`: Good balance of quality and speed (default)
  - `bicubic`: Higher quality, slower
  - `nearest`: Fastest, pixelated look
  - `linear`, `trilinear`, `area`: Other options for specific use cases

### Auto Megapixel Reducer - Inputs

- **images**: Input image(s) to resize
- **max_megapixels**: Target maximum megapixels (default: 2.1, range: 0.1-50.0)
- **only_reduce**: Enable/disable upscaling protection (default: True)
  - `True`: Only reduce size, never upscale (safe mode)
  - `False`: Allow upscaling if image is below target megapixels
- **interpolation**: Interpolation method for resizing (same options as above)

### Outputs

- **resized_images**: The resized image(s) maintaining aspect ratio

## How It Works

1. **Calculates Scale Factor**: Determines the scaling needed to fit within max dimensions
2. **Preserves Aspect Ratio**: Uses the smaller of width_scale or height_scale to maintain proportions
3. **Applies Resize Mode**: Only resizes based on your selected mode
4. **Ensures Even Dimensions**: Rounds to even numbers for better compatibility
5. **Provides Feedback**: Shows original and new dimensions in the console

## Examples

### Example 1: Width-Only Constraint
- Input: 1920x1080 image
- Enable Width: True, Max Width: 1024
- Enable Height: False
- Mode: downscale_only
- Result: 1024x576 (maintains 16:9 aspect ratio, height calculated automatically)

### Example 2: Height-Only Constraint
- Input: 1920x1080 image
- Enable Width: False
- Enable Height: True, Max Height: 1024
- Mode: downscale_only
- Result: 1820x1024 (maintains 16:9 aspect ratio, width calculated automatically)

### Example 3: Both Constraints (Traditional Mode)
- Input: 2048x1536 image
- Enable Width: True, Max Width: 1024
- Enable Height: True, Max Height: 1024
- Mode: downscale_only
- Result: 1024x768 (maintains 4:3 aspect ratio, uses most restrictive constraint)

### Example 4: No Constraints
- Input: Any image
- Enable Width: False, Enable Height: False
- Result: Unchanged (no resizing performed)

## Auto Megapixel Reducer Examples

### Example 1: 4K to 2MP
- Input: 3840x2160 image (8.3MP)
- Max Megapixels: 2.0
- Result: 1884x1060 (2.0MP, maintains 16:9 aspect ratio)

### Example 2: 8K to 2MP
- Input: 7680x4320 image (33.2MP)
- Max Megapixels: 2.0
- Result: 1884x1060 (2.0MP, maintains 16:9 aspect ratio)

### Example 3: Small Image (Safe Mode)
- Input: 1024x768 image (0.8MP)
- Max Megapixels: 2.0, Only Reduce: True
- Result: 1024x768 (unchanged, already below target)

### Example 4: Portrait 4K
- Input: 2160x3840 image (8.3MP, portrait)
- Max Megapixels: 2.0
- Result: 1060x1884 (2.0MP, maintains aspect ratio)

## Technical Details

- Uses PyTorch's `F.interpolate` for high-quality resizing
- Handles batch processing efficiently
- Maintains ComfyUI's image tensor format [B, H, W, C]
- Provides detailed logging for debugging

## Troubleshooting

- **Node doesn't appear**: Make sure you've restarted ComfyUI after installation
- **Images look distorted**: Check that aspect ratio is being maintained (should never happen with this node)
- **Performance issues**: Try using 'nearest' interpolation for faster processing
- **Dimension errors**: Ensure max_width and max_height are reasonable values (64-8192)

## License

This custom node is provided as-is for educational and practical use in ComfyUI workflows.
