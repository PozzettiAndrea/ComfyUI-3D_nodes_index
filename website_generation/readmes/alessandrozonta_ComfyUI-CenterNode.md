# Bounding Box Crop Node for ComfyUI

This repository contains a custom node for ComfyUI. The node, called "Bounding Box Crop", is designed to compute the top-left coordinates of a cropped bounding box based on input coordinates and dimensions of the final cropped image. It does so computing the center of the cropping area and then computing where the top-left coordinates would be.

## Features

- Computes the top-left coordinates of a cropped bounding box.
- Takes input for the left, top, right, and bottom coordinates of the bounding box, as well as the desired width and height of the cropped area.
- Suitable for integration into ComfyUI workflows.

## Example

![Example Workflow](example/workflow.png)

You can use `example/workflow.json` to run the custom node. It requires also [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)

## Installation

To use the Bounding Box Crop node in your ComfyUI workflow, follow these steps:

1. Clone this repository to the `custom_node` folder of your ConfyUI installation:

   ```
   git clone https://github.com/alessandrozonta/ComfyUI-CenterNode.git
   ```

## Contributions

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to [open an issue](https://github.com/alessandrozonta/ComfyUI-CenterNode/issues) or [submit a pull request](https://github.com/alessandrozonta/ComfyUI-CenterNode/pulls).

## License

This project is licensed under the [GPL-3.0 license](LICENSE).