# Save Uncompressed 16 Bit PNG
This is a custom node for the Comfy UI stable diffusion client.

## Description
The `SaveImageARGB16PNG` node provides functionality for saving images as uncompressed PNG files with ARGB16 precision.
This node is particularly useful for workflows that require high-quality image saving with metadata such as prompts and additional PNG info.

## Inputs
- **images**: A tensor of images to be saved. Each image is expected to be in a format compatible with ARGB16.
- **filename_prefix**: A string used as the prefix for the saved filenames. This can include dynamic formatting options.
- **prompt** (optional): Metadata to embed in the PNG file.
- **extra_pnginfo** (optional): Additional metadata to include in the PNG file as key-value pairs.

## Outputs
- Saves images to the Comfy UI output directory with metadata embedded in the PNG files.
- Returns a UI-compatible dictionary containing details about the saved images.

## Getting Started
Import this script into the custom nodes directory of your Comfy UI client.

## Dependencies
- ComfyUI
- Pillow (for PNG processing)

## License
This project is licensed under the MIT License.