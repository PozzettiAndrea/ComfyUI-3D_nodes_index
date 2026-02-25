# ComfyUI-Inspector

A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allows you to inspect any input data. It provides detailed metadata (type, shape, values) and renders a visual preview if the input is an image or video tensor.

## Features

- **Universal Input**: Accepts any connection type (`*`).
- **Detailed Inspection**:
  - **Tensors**: Displays shape, dtype, device, value range (min/max), mean, and standard deviation.
  - **Primitives**: Shows type and value for integers, floats, booleans, and strings.
  - **Collections**: Summarizes Lists and Dictionaries with length/keys and sample content.
- **Visual Preview**:
  - Automatically detects image tensors (`[B, H, W, C]`).
  - Displays a preview image directly on the node.
  - Supports batch images by generating an animated WEBP preview (video).
- **Dynamic Resizing**: The node automatically resizes to fit the text content and preview image.

## Installation

1. Navigate to your ComfyUI `custom_nodes` directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/danielwolber-wood/ComfyUI-Inspector.git
   ```
3. (Optional) Install dependencies if they are missing (most are standard in ComfyUI):
   ```bash
   pip install -r ComfyUI-Inspector/requirements.txt
   ```
4. Restart ComfyUI.

## Usage

1. Open ComfyUI.
2. Double-click to search and add the node **SimpleDisplayNode**.
   - Located under the category `DLWW/Utils`.
3. Connect any output from another node to the `any_input` slot.
4. Queue the prompt.
5. The node will display text details about the data and a visual preview if applicable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
