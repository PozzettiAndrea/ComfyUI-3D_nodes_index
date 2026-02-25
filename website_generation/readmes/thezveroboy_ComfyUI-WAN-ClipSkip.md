# ComfyUI-CLIPSkip

A custom node for ComfyUI that adds CLIP skip functionality to vanilla WAN workflow using CLIP. This node allows you to skip a specified number of layers in a CLIP model, which can adjust the style or quality of image embeddings in generation pipelines.

![comfy-csm](https://github.com/thezveroboy/ComfyUI-WAN-ClipSkip/picture.jpg)

## Installation

### Via Git (Recommended)
1. Open a terminal in your ComfyUI `custom_nodes` directory:

cd ComfyUI/custom_nodes

2. Clone this repository:

git clone https://github.com/yourusername/ComfyUI-CLIPSkip.git

3. Restart ComfyUI. The node will be automatically loaded.

4. Ensure you have the required WAN CLIP model (e.g., umt5_xxl_fp8_e4m3fn_scaled.safetensors) in ComfyUI/models/text_encoders/.

### Manual Installation
1. Download this repository as a ZIP file.
2. Extract it into the `ComfyUI/custom_nodes` directory.
3. Rename the folder to `ComfyUI-CLIPSkip` if needed.
4. Restart ComfyUI.

## Dependencies
- ComfyUI (latest version recommended)
- PyTorch (installed with ComfyUI)

No additional dependencies are required.

## Usage
1. Load a CLIP Vision model using `CLIPVisionLoader` or any other node that outputs `CLIP_VISION`.
2. Connect the `clip_vision` output to the `clip` input of `CLIPSkip`.
3. Set the `skip_layers` parameter (e.g., 1 to skip the last layer, 0 to disable skipping).
4. Connect the output `clip` to any node that accepts `CLIP_VISION` (e.g., `CLIPVisionEncode`).

### Example Workflow

CLIPVisionLoader -> CLIPSkip -> CLIPVisionEncode -> (further pipeline)

### Supported Models
- umt5_xxl_fp8_e4m3fn_scaled.safetensors (24 layers).

## Notes
- Designed for WAN-type CLIP models in ComfyUI.
- Requires ComfyUI with FP8 support for optimal performance.

## License
MIT License (see `LICENSE` file for details).

## Contributing
Feel free to submit issues or pull requests on GitHub!
