# Woohee HF Loader

Load models directly from Hugging Face Hub in ComfyUI without manual downloads.

## Description

This custom node collection allows you to load various models (upscalers, checkpoints, LoRAs, etc.) directly from Hugging Face repositories into ComfyUI. No need to manually download and place models in your models folder - just provide the repository name and filename!

Currently supports:
- UNET models (Diffusion models, Qwen Image Layered, etc.)
- CLIP models (Text encoders, Qwen 2.5 VL, etc.)
- VAE models (Variational Autoencoders)
- Upscale models (ESRGAN, Real-ESRGAN, etc.)
- GGUF models (Quantized models for efficient inference)

## Features

- Load UNET, CLIP, VAE, upscale, and GGUF models directly from Hugging Face Hub
- Pre-configured defaults for Qwen Image Layered models
- **4-channel RGBA VAE support** with embedded WanVAE implementation
- **ComfyUI v0.3.62+ compatible** - works on older versions without updates
- **Full alpha channel preservation** for Qwen Image Layered layer decomposition
- Automatic model caching to avoid repeated downloads
- Support for both public and private repositories (with API token)
- Compatible with standard ComfyUI model formats
- Works seamlessly with all ComfyUI model nodes

## Installation

### Via ComfyUI Manager

Search for "Woohee HF Loader" in ComfyUI Manager and install.

### Manual Installation

1. Navigate to your ComfyUI custom_nodes directory
2. Clone this repository:
   ```bash
   git clone https://github.com/hw5511/woohee_hf_loader.git
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Restart ComfyUI

## Usage

### UNET Model Loader From HF

1. Add "UNET Model Loader From HF" node to your workflow
2. Default values are pre-configured for Qwen Image Layered model:
   - repo_name: `Comfy-Org/Qwen-Image-Layered_ComfyUI`
   - filename: `qwen_image_layered_fp8mixed.safetensors`
   - subfolder: `split_files/diffusion_models`
3. Connect the MODEL output to KSampler or other compatible nodes

### CLIP Model Loader From HF

1. Add "CLIP Model Loader From HF" node to your workflow
2. Default values are pre-configured for Qwen 2.5 VL model:
   - repo_name: `Comfy-Org/Qwen-Image_ComfyUI`
   - filename: `qwen_2.5_vl_7b_fp8_scaled.safetensors`
   - subfolder: `split_files/text_encoders`
   - type: `qwen_image`
3. Connect the CLIP output to CLIPTextEncode nodes

### VAE Model Loader From HF

1. Add "VAE Model Loader From HF" node to your workflow
2. Default values are pre-configured for Qwen Image Layered VAE:
   - repo_name: `Comfy-Org/Qwen-Image-Layered_ComfyUI`
   - filename: `qwen_image_layered_vae.safetensors`
   - subfolder: `split_files/vae`
3. Connect the VAE output to VAEDecode or VAEEncode nodes

**4-Channel RGBA Support:**
- Automatically detects and supports 4-channel RGBA VAE models (Qwen Image Layered)
- Preserves alpha channel for layer decomposition and transparency
- Uses embedded WanVAE implementation for ComfyUI v0.3.62 compatibility
- Automatically falls back to embedded version if ComfyUI's WanVAE is unavailable
- Console output shows: `[VAELoader] Using WanVAE from: Embedded` or `ComfyUI`

### Upscale Model Loader From HF

1. Add "Upscale Model Loader From HF" node to your workflow
2. Enter the Hugging Face repository name (e.g., `Phips/2xNomosUni_span_multijpg`)
3. Enter the model filename (e.g., `2xNomosUni_span_multijpg.pth`)
4. (Optional) Enter subfolder path if the model is in a subdirectory
5. Connect the output to an "Upscale Image (using Model)" node

### GGUF Model Loader From HF

1. Add "GGUF Model Loader From HF" node to your workflow
2. Enter the Hugging Face repository name (e.g., `QuantStack/Qwen-Image-Edit-2509-GGUF`)
3. Enter the GGUF filename (e.g., `Qwen-Image-Edit-2509-Q4_K_M.gguf`)
4. (Optional) Enter subfolder path if needed
5. Connect the MODEL output to compatible ComfyUI nodes

## Inputs

All loaders share the same input structure:
- **repo_name** (STRING): Hugging Face repository name
- **filename** (STRING): Model file name in the repository
- **subfolder** (STRING, optional): Subfolder path within the repository

## Outputs

- **UNET Model Loader**: MODEL output
- **CLIP Model Loader**: CLIP output
- **VAE Model Loader**: VAE output
- **Upscale Model Loader**: UPSCALE_MODEL output
- **GGUF Model Loader**: MODEL output

## Example Workflows

### Qwen Image Layered Workflow
```
UNET Model Loader From HF -> ModelSamplingAuraFlow
CLIP Model Loader From HF -> CLIPTextEncode (Positive/Negative)
VAE Model Loader From HF -> VAEEncode/VAEDecode
Load Image -> KSampler -> VAEDecode -> Save Image
```

### Upscale Workflow
```
Load Image -> Upscale Model Loader From HF -> Upscale Image (using Model) -> Save Image
```

### GGUF Workflow
```
GGUF Model Loader From HF -> [Connect to compatible MODEL input nodes]
```

## Supported Model Formats

- **Upscale Models**: PyTorch models (.pth, .pt), SafeTensors (.safetensors)
- **GGUF Models**: Quantized GGUF files (.gguf)
- Any format supported by ComfyUI's model loaders

## Example Models on Hugging Face

### Qwen Image Layered Models
- **UNET**: `Comfy-Org/Qwen-Image-Layered_ComfyUI` (split_files/diffusion_models/qwen_image_layered_fp8mixed.safetensors)
- **CLIP**: `Comfy-Org/Qwen-Image_ComfyUI` (split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors)
- **VAE**: `Comfy-Org/Qwen-Image-Layered_ComfyUI` (split_files/vae/qwen_image_layered_vae.safetensors)

### Upscale Models
- `Phips/2xNomosUni_span_multijpg` - High-quality 2x upscaler
- `ai-forever/Real-ESRGAN` - Popular Real-ESRGAN models

### GGUF Models
- `QuantStack/Qwen-Image-Edit-2509-GGUF` - Qwen Image Edit model (quantized)
- Search for more GGUF models on Hugging Face Hub!

## Changelog

### 2.2.4
- **Forced embedded WanVAE usage** for guaranteed ComfyUI v0.3.62 compatibility
- Fixed `image_channels` parameter error in older ComfyUI versions
- Bypasses ComfyUI's built-in WanVAE to use embedded implementation
- Resolves "WanVAE.__init__() got an unexpected keyword argument 'image_channels'" error
- Ensures 4-channel RGBA support works on all ComfyUI versions (0.3.62+)

### 2.2.3
- **Critical bug fix**: Fixed 4-channel VAE loading logic
- Standard VAE loader now properly skipped when 4-channel WanVAE is detected
- Resolved shape mismatch errors (`Error(s) in loading state_dict...`)
- Direct WanVAE instantiation now triggered immediately for 4-channel models
- Guaranteed proper RGBA support with alpha channel preservation

### 2.2.2
- **Added 4-channel RGBA VAE support** for Qwen Image Layered models
- **Embedded WanVAE implementation** for ComfyUI v0.3.62+ compatibility
- Automatic fallback mechanism: ComfyUI WanVAE → Embedded WanVAE
- Full alpha channel preservation for layer decomposition functionality
- Compatible with RunDiffusion and other cloud environments running older ComfyUI versions
- Source: Alibaba WanVAE from ComfyUI master branch

### 2.2.1
- Fixed VAE loader to use `comfy.sd.VAE()` for proper model loading
- Fixed CLIP loader to use `comfy.sd.load_clip()` with correct parameters
- Fixed UNET loader to use `comfy.sd.load_unet()` directly
- Resolved "VAEModelWrapper has no attribute encode" error
- All loaders now properly handle HuggingFace model paths

### 2.2.0
- Added UNET Model Loader From HF node with Qwen Image Layered defaults
- Added CLIP Model Loader From HF node with Qwen 2.5 VL defaults
- Added VAE Model Loader From HF node with Qwen Image Layered VAE defaults
- Pre-configured repository paths and filenames for easy Qwen model loading
- Enhanced documentation with Qwen Image Layered workflow examples

### 2.1.0
- Added GGUF Model Loader From HF node
- Support for loading quantized GGUF models from Hugging Face
- Enhanced documentation with GGUF usage examples

### 2.0.0
- Renamed project to "Woohee HF Loader" for broader scope
- Preparing infrastructure for additional model loaders (checkpoints, LoRAs, etc.)
- Maintained backward compatibility with existing workflows

### 1.0.2
- Removed API token requirement (public repositories only)
- Added subfolder support for models in subdirectories
- Improved cache key handling for subfolder paths

### 1.0.1
- Bug fixes and improvements

### 1.0.0
- Initial release
- Support for loading upscale models from Hugging Face Hub
- Automatic model caching

## License

MIT

## Author

woohee5511

## Credits

Inspired by [ComfyUI-HfLoader](https://github.com/olduvai-jp/ComfyUI-HfLoader) by olduvai-jp
