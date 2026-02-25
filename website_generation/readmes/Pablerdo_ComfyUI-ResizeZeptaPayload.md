# ComfyUI-ResizeZeptaPayload

A custom node extension for ComfyUI that provides utilities for resizing images and trajectory data while maintaining compatibility with Zepta AI tools.

## Features

- **ResizeImageBatch**: Resize a batch of images with various methods and settings
  - Control output dimensions with multiple input options
  - Keep proportions while resizing
  - Make dimensions divisible by a specific value
  - Choose from multiple upscaling methods (nearest-exact, bilinear, area, bicubic, lanczos)
  - Center cropping option

- **ResizeTrajectoryBatch**: Resize trajectory coordinates proportionally to match resized images
  - Automatically scales trajectory points to new dimensions
  - Maintains the relative positioning of trajectory data

## Installation

1. Clone this repository into your ComfyUI custom_nodes directory:
   ```
   cd path/to/ComfyUI/custom_nodes
   git clone https://github.com/yourusername/ComfyUI-ResizeZeptaPayload.git
   ```

2. Restart ComfyUI

## Usage

### ResizeImageBatch

The node can be found in the node menu under the "ResizeZeptaPayload" category.

Input parameters:
- `images`: Batch of images to resize
- `output_width`: Target width (set to 0 to maintain original width)
- `output_height`: Target height (set to 0 to maintain original height)
- `upscale_method`: Interpolation method to use
- `keep_proportion`: Whether to maintain aspect ratio
- `divisible_by`: Make dimensions divisible by this value
- `crop`: Crop method (disabled or center)
- `width_input` (optional): Override output width
- `height_input` (optional): Override output height
- `get_size_from_image` (optional): Get dimensions from this image

### ResizeTrajectoryBatch

Input parameters:
- `input_width`: Original width of the context
- `input_height`: Original height of the context
- `output_width`: Target width
- `output_height`: Target height
- `trajectories`: JSON string containing trajectory data


