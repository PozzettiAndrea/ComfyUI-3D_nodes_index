# ComfyUI Image Expand Nodes

Custom nodes for ComfyUI to expand images with noise for outpainting or inpainting purposes. This allows for seamless image extension in any direction.

### Basic Expansion

![](https://raw.githubusercontent.com/tuki0918/comfyui-image-expand-nodes/refs/heads/docs/docs/image1.png)

### Expansion with Mask

![](https://raw.githubusercontent.com/tuki0918/comfyui-image-expand-nodes/refs/heads/docs/docs/image3.png)

### Seamless Merging

![](https://raw.githubusercontent.com/tuki0918/comfyui-image-expand-nodes/refs/heads/docs/docs/image2.png)

## Features

- **Expand Image**: Add noise to any side of an image (top, bottom, left, right) to prepare for outpainting.
- **Inside/Outside Modes**: Choose between expanding the canvas (`outside`) or overwriting existing content (`inside`).
- **Merge**: Seamlessly stitch the original image with the newly generated content.

## Nodes

### 1. Image Expand Option
A configuration node to define the expansion strategy.
- **direction**: Choose the direction to expand (`top`, `bottom`, `left`, `right`).
- **mode**:
    - `outside`: Increases the image canvas size.
    - `inside`: Maintains image size but overlays noise on the specified area.

### 2. Image Expand Noiser
Prepares the image for the generation process.
- **Inputs**:
    - `image`: Source image.
    - `options`: Configuration from `Image Expand Option`.
    - `percentage`: The ratio of expansion relative to the image size (default: 0.2).
    - `mask`: (Optional) Mask to merge.
- **Outputs**:
    - `IMAGE`: Image with noise added to the target area.
    - `MASK`: Mask corresponding to the noisy area (useful for inpainting).

### 3. Image Expand Merger
Merges the original image with the generated result.
- **Inputs**:
    - `image1`: The original source image.
    - `image2`: The generated image (output from KSampler/VAE Decode).
    - `mask`: The mask used for generation.
    - `options`: Configuration from `Image Expand Option`.
- **Outputs**:
    - `IMAGE`: The final combined image.

## Installation

1. Navigate to your ComfyUI `custom_nodes` directory.
2. Clone this repository:
   ```bash
   git clone https://github.com/tuki0918/comfyui-image-expand-nodes.git
   ```
3. Restart ComfyUI.


## Related Tools

**[image-noise-expander](https://github.com/tuki0918/image-noise-expander)**

- Expand Image with Noise and Crop + Mask

**[image-overlap-merger](https://github.com/tuki0918/image-overlap-merger)**

- Automatically detect and merge overlapping regions of two images
