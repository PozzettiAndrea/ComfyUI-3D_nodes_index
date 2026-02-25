# ShinChven's Custom Nodes Package

This project contains custom nodes for ComfyUI, developed by ShinChven. The nodes in this package extend the functionality of ComfyUI by providing additional features and utilities.

## Installation

To install this package into your ComfyUI setup, follow these steps:

1. Navigate to the `custom_nodes` directory inside your ComfyUI installation:
    ```sh
    cd /path/to/ComfyUI/custom_nodes
    ```

2. Clone this repository into the `custom_nodes` directory:
    ```sh
    git clone https://github.com/ShinChven/sc-comfy-nodes.git
    ```

3. Restart ComfyUI to load the new nodes.

## Usage

After installation, the custom nodes will be available in ComfyUI. You can use them just like any other nodes in the interface.

## Nodes Included

### Rescaler Node

The Rescaler node allows you to resize images while ensuring the dimensions are divisible by a specified factor. This is useful for maintaining compatibility with certain image processing algorithms.

#### Input Types

- `width`: The original width of the image.
- `height`: The original height of the image.
- `limit`: The maximum dimension (either width or height) after resizing.

#### Return Types

- `new width`: The new width of the image, adjusted to be divisible by the specified factor.
- `new height`: The new height of the image, adjusted to be divisible by the specified factor.
- `original width`: The original width of the image.
- `original height`: The original height of the image.
- `limit`: The limit used for resizing.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
