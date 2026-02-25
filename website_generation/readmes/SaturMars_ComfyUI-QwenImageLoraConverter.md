# ComfyUI Qwen LoRA Converter Node

[🇨🇳 中文版本](README.zh.md) | [🇺🇸 English](README.md)

This is a ComfyUI custom node used to convert Qwen-Image LoRA files trained on the ModelScope platform to a format that ComfyUI can recognize.

## Usage

1. Copy this folder to the `custom_nodes` directory of ComfyUI
2. Restart ComfyUI
3. Find the "Qwen-Image Lora Converter" node in the node list
4. Select the LoRA file to convert from the dropdown
5. Run the workflow, and the node will automatically complete the conversion and save it

The converted file will be saved in the original LoRA directory with the filename format: `original_filename_converted.safetensors`. Press R key or F5 to refresh ComfyUI to see the LoRA.

## License

This project is open source and available under the MIT License.
