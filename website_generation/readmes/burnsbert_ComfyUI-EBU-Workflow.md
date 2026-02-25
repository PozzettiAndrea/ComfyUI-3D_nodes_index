# ComfyUI-EBU-Workflow

A collection of custom ComfyUI nodes to improve your workflow, including nodes to assist in upscaling and file naming.

## Features

- **Smart Resolution Scaling:**  
  Easily upscale or downscale images based on aspect ratio presets.

- **Tile Sizing:**  
  A partner node for Ultimate SD Upscale, automatically compute tile sizes appropriate for landscape or profile images with padding support.

- **Aspect Ratio Detection:**  
  Detect the closest standard aspect ratio of an input image with adjustable tolerance.

- **Unique Filename Generator:**  
  Generate timestamped filenames that change every run for saving unique filenames.

## Installation

1. **Copy/pull Files:**  
   Get `ComfyUI-EBU-ScalingTools` into your `ComfyUI/custom_nodes/` folder.

2. **Dependencies:**  
   - Python 3.11+  
   - ComfyUI (latest recommended)

3. **Restart ComfyUI:**  
   Restart ComfyUI after copying to load the new nodes.

---

## Nodes

### EBU Scaling Resolution

Resolution picker handily sorted by aspect ratio with build in upscaled dimensions based on the upscale_by multiplier
**Inputs:**
- `active_aspect_ratio` (CHOICE): Select from predefined aspect ratios or "Other" for custom dimensions
- `other_width`, `other_height` (INT): Custom dimensions used when "Other" is selected
- `[Aspect Ratio]` (CHOICE): Resolution presets for the selected ratio
- `mode` (CHOICE): “Landscape” or “Profile” mode to swap width/height accordingly
- `upscale_by` (FLOAT): Scaling factor for resolution upscaling (default 1.5)

**Returns:**
- `width` (INT): Original width  
- `height` (INT): Original height  
- `upscaled_width` (INT): Scaled width  
- `upscaled_height` (INT): Scaled height  
- `upscale_by` (FLOAT): Scaling factor used  
- `upscaled_resolution_string` (STRING): Upscaled resolution as a string (e.g., "2048x1152")

---

### EBU Scaling Tile

Use this with the excellent Ultimate SD Upscale custom node. Determines tile sizes based on input dimensions and orientation.

**Inputs:**
- `upscaled_image_width`, `upscaled_image_height` (INT): Image dimensions
- `profile_width_div_by`, `profile_height_div_by` (FLOAT): Divisors for portrait mode tiling
- `landscape_width_div_by`, `landscape_height_div_by` (FLOAT): Divisors for landscape mode tiling
- `tile_width_padding`, `tile_height_padding` (INT): Additional padding added to each tile, useful due to gaps created by rounding

**Returns:**
- `tile_width` (INT): Calculated tile width, send to Ultimate SD Upscale  
- `tile_height` (INT): Calculated tile height, send to Ultimate SD Upscale

---

### EBU Get Image Aspect Ratio

Analyzes an image to determine its closest standard aspect ratio.

**Inputs:**
- `image` (IMAGE): The image to evaluate

**Returns:**
- `aspect_ratio` (STRING): Detected ratio label (e.g., “4:3”) or “Unknown” if not within tolerance

**Supported Ratios:**
Includes common portrait and landscape ratios like `1:1`, `4:3`, `16:9`, `3:2`, `9:16`, and more. Tolerance threshold is 8%.

---

### EBU Unique File Name

Generates a unique filename by appending a timestamp to a base string using a join string.

**Inputs:**
- `str` (STRING): Base string (e.g., “image”)  
- `join_str` (STRING): Separator (e.g., “_” or “-”)  
- `seed` (INT): Dummy input to force rerun (timestamp changes regardless)

**Returns:**
- `unique_filename` (STRING): Generated string (e.g., “image-2025_06_07_19_45_22”)

---

## Requirements

- Python 3.11 or newer  
- ComfyUI

## License

This project is licensed under the MIT License.

## Acknowledgments

- Thanks to the ComfyUI team and community for making powerful workflows accessible.
