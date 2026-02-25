# ComfyUI PadToEight Node

This is a custom node for ComfyUI that pads images to multiples of eight dimensions.

## Installation

1. Clone the repository into your ComfyUI custom_nodes directory:
```bash
git clone https://github.com/umiyuki/comfyui-pad-to-eight.git
```

2. Install dependencies:
```bash
cd ComfyUI/custom_nodes/ComfyUI-PadToEight
pip install -r requirements.txt
```

For portable ComfyUI versions:
```bash
python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-PadToEight\requirements.txt
```

## Usage

1. Load the node in ComfyUI
2. Connect your image to the PadToEight node
3. The node will:
   - Resize the image to 1024px height while maintaining aspect ratio
   - Pad the width to the nearest multiple of 8 pixels
   - Return the processed image along with its final dimensions

### Input/Output
- **Input**: 
  - `image`: Any RGB image tensor
- **Output**:
  - `image`: Processed image tensor
  - `width`: Final image width (multiple of 8)
  - `height`: Final image height (1024px)

### Example Workflow
```json
{
  "nodes": [
    {
      "type": "PadToEight",
      "inputs": {
        "image": "<your_image>"
      }
    }
  ]
}
```

## Features

- Supports both RGB and RGBA images
- Preserves aspect ratio while padding
- Configurable padding color

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
