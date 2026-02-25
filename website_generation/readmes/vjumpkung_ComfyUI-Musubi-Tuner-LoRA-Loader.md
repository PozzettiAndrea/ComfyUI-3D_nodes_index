# ComfyUI Musubi-Tuner LoRA Loader

A ComfyUI custom node that enables direct loading of musubi-tuner based LoRAs without manual format conversion. The conversion happens automatically in-memory during node execution.

## Features

- **On-the-fly Conversion**: Automatically converts musubi-tuner LoRA format to ComfyUI-compatible diffusers format
- **No File Creation**: All conversion happens in-memory, no temporary files needed
- **Multi-Format Support**:
  - **Qwen-Image** LoRAs
  - **Z-Image Turbo** LoRAs
  - **Hunyuan Video 1.5** LoRAs
  - **FLUX** LoRAs
  - **Wan2.1** LoRAs
- **ComfyUI v3 Schema**: Uses the latest ComfyUI extension API

## Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/vjumpkung/ComfyUI-Musubi-Tuner-LoRA-Loader.git
   ```

3. Restart ComfyUI or reload custom nodes

## Usage

1. Find the node in ComfyUI under the name **"musubi-tuner LoRA Loader"**
2. Connect a MODEL input
3. Select your musubi-tuner format LoRA from the dropdown
4. Adjust the strength_model parameter (default: 1.0, range: -100.0 to 100.0)
5. Connect the MODEL output to your workflow

## How It Works

The node converts musubi-tuner LoRA format to diffusers-compatible format using a comprehensive mapping system:

### 1. Format Detection and Module Name Mapping
The conversion automatically detects the LoRA format based on key patterns:
- **Qwen-Image**: Uses predefined key mappings for transformer blocks
- **Z-Image**: Detects `.attention.to.` and `.feed.forward.` patterns
- **Hunyuan Video/FLUX**: Detects `double.blocks.` and `single.blocks.` patterns
- **Wan2.1**: Detects `.cross.attn.` and `.self.attn.` patterns

### 2. Key Transformation
Converts musubi-tuner naming conventions to diffusers format:
- Replaces underscores with dots for module hierarchy
- Applies format-specific fixes (e.g., `to.q` → `to_q`, `img.` → `img_`)
- Maps to diffusers structure: `lora_down` → `lora_A.weight`, `lora_up` → `lora_B.weight`

### 3. Alpha Scaling
Applies LoRA alpha scaling to weights:
- Scales both down and up weights by `sqrt(alpha / dim)`
- Ensures proper weight magnitude for model integration

## Technical Details

- **API Version**: Built with ComfyUI v3 Schema API (`comfy_api.latest`)
- **Base Class**: Implements `io.ComfyNode` with `define_schema()` and `execute()` methods
- **Extension System**: Uses `ComfyExtension` and `comfy_entrypoint()` for registration
- **Optimization**: Returns original model immediately if `strength_model == 0`
- **Dependencies**: `torch`, `tqdm`, `comfy.sd`, `comfy.utils`, `folder_paths`

## Credits

Conversion logic adapted from [musubi-tuner by kohya-ss](https://github.com/kohya-ss/musubi-tuner/blob/main/src/musubi_tuner/convert_lora.py)

## License

This project is provided as-is for use with ComfyUI.
