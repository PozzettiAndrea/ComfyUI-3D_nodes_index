# ComfyUI-PS_Flatten_Image

A ComfyUI custom node that simulates Photoshop's "Flatten Image" functionality.

## Support My Work
If you find this project helpful, consider buying me a coffee:

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=shmuelronen&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/shmuelronen)

## Description

This node allows you to flatten multiple image layers into a single image, similar to Photoshop's "Flatten Image" command. It takes a batch of images as input and outputs a single flattened image.

## Installation

1. Clone this repository to your ComfyUI custom nodes directory:
```bash
cd /path/to/ComfyUI/custom_nodes/
git clone https://github.com/ShmuelRonen/ComfyUI-PS_Flatten_Image.git
```

2. Restart ComfyUI

## Usage

After installation, you'll find a new node called "Flatten Image" under the "PS Operations" category in the node menu.

To use it:
1. Connect multiple images to the "images" input
2. The node will flatten these images into a single output image

## Example

![image](https://github.com/user-attachments/assets/2db65a28-6824-4c52-9013-b8721796923b)


## Notes

- The node processes images in order, with the first image in the batch at the bottom and the last image on top
- Currently, the node simply takes the topmost layer as the final result
- If only one image is provided, it passes through unchanged

## License

[MIT License](LICENSE)
