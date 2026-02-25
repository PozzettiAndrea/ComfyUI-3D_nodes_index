# ComfyUI LoRA Combine Node

A custom ComfyUI node that allows you to combine two LoRAs with adjustable strengths and multiple merging methods.

## Features

- Combine two LoRA files from your ComfyUI loras folder
- Adjust the strength of each LoRA independently (-100.0 to 100.0)
- Choose merge method (linear, weighted average, concatenation) with optional compatibility checks
- Output a merged LoRA_MODEL that can be used with other ComfyUI nodes
- Works with any LoRA format (Stable Diffusion, Qwen, etc.) as long as they have compatible tensor structures

## Installation

1. Download or clone this repository
2. Copy the `Comfyui_LoraCombine` folder to your `ComfyUI/custom_nodes/` directory (or clone the repo directly there)
3. Restart ComfyUI

The node will appear as "Combine LoRAs" in the "loaders" category.

## Usage

1. Add the "Combine LoRAs" node to your workflow
2. Select two LoRA files from your loras folder
3. Set the strength values for each LoRA
4. Connect the output to a node that accepts LORA_MODEL (like Save LoRA Weights to save it, or LoraModelLoader to apply it)

## Node Inputs

- `lora_name1`: First LoRA file
- `strength1`: Strength multiplier for first LoRA (default: 1.0)
- `lora_name2`: Second LoRA file
- `strength2`: Strength multiplier for second LoRA (default: 1.0)

## Node Output

- `LORA_MODEL`: The combined LoRA weights

## Saving Combined LoRAs

To save your combined LoRA:
1. Connect the output to "Save LoRA Weights" node
2. Set a filename prefix (can include subfolders)
3. Optionally set steps for file naming
4. Run the workflow

## How It Works

The node merges LoRA weights by:
- Loading both LoRA safetensors files
- For each tensor key that exists in both LoRAs: `merged[key] = strength1 * lora1[key] + strength2 * lora2[key]`
- For keys that exist in only one LoRA: `merged[key] = strength * lora[key]`
- Outputting the combined weight dictionary

## Requirements

- ComfyUI (with training nodes enabled for saving)
- PyTorch (included with ComfyUI)
- safetensors (only for compatibility checks)

## Credits

- Original concept and initial implementation by Snowshoes311
- Major enhancements to merging methods and compatibility checks by @sweetmax797

## License

MIT License - feel free to use and modify as needed.
