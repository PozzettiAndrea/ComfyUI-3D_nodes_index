# ComfyUI Random Image Loader

![comfyui-random-image-loader](https://github.com/thezveroboy/comfyui-random-image-loader/blob/main/image.jpg)

A custom node for ComfyUI that loads a random image from a specified folder and outputs it in the standard ComfyUI `IMAGE` format, along with a `MASK` and the image path as `STRING`. Images are loaded in their original dimensions.

## Features
- Loads images in popular formats: `.jpg`, `.jpeg`, `.png`, `.gif`, `.webp`
- Preserves original image dimensions
- Optional subfolder inclusion
- Outputs:
  - `image`: Tensor of the loaded image
  - `mask`: Alpha channel mask (if present)
  - `image_path`: Path to the selected image

## Installation
1. Clone this repository into your ComfyUI `custom_nodes` folder:
   ```bash
   git clone https://github.com/yourusername/comfyui-random-image-loader.git
   cd comfyui-random-image-loader
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Restart ComfyUI

## Usage
Add the "Load Random Image" node from the zverovboy category in ComfyUI.
Set the folder path to your image directory.
Optionally enable include_subfolders.

## Project Structure
__init__.py: Required for ComfyUI to recognize the custom node module.
nodes.py: Contains the node implementation.
requirements.txt: Lists dependencies.

## Requirements
Python 3.8+
PyTorch
Pillow
NumPy
