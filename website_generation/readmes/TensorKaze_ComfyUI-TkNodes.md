# ComfyUI-TkNodes

A collection of custom nodes for ComfyUI by TensorKaze, designed to enhance workflows with advanced sampling, latent manipulation, image processing, and model loading. Includes nodes optimized for Flux.1 as well as general-purpose utilities for ComfyUI.
These nodes aim to streamline complex workflows, offering quality-of-life improvements for both Flux-based and general diffusion tasks. This is a work in progress, with node descriptions available in the ComfyUI interface (click the ? icon on each node for details).
Installation
Clone this repository into the custom_nodes folder of ComfyUI:
bash

cd ComfyUI/custom_nodes
git clone https://github.com/TensorKaze/ComfyUI-TkNodes

Install dependencies:
bash

cd ComfyUI-TkNodes
pip install -r requirements.txt

If you're using the portable version of ComfyUI, run:
bash

ComfyUI_windows_portable/python_embeded/python.exe -m pip install -r ComfyUI/custom_nodes/ComfyUI-TkNodes/requirements.txt

Note: Ensure you have a PyTorch version compatible with your hardware. For example:
bash

pip install torch --index-url https://download.pytorch.org/whl/cu121  # For CUDA 12.1
pip install torch  # For CPU

Recommended: PyTorch 2.0.0 or higher for Flux.1 nodes.

Restart ComfyUI to load the nodes.

Requirements
ComfyUI updated to the latest version (recommended: as of May 24, 2025).

Flux.1 model (Dev or Schnell) for Flux-specific nodes (FluxAdvancedSampler, FluxLatentSampler).

Minimum VRAM: 6 GB (for Flux GGUF) or 8-12 GB (for Flux.1 Dev/Schnell).

Optional: Upscale models for LoadModelAndUpscaleImage (available via ComfyUI's model downloader or Hugging Face).

Nodes
FluxAdvancedSampler
Advanced sampling for Flux.1 with customizable guidance, denoising, and scheduler settings.
Inputs: Model, conditioning, sampler name, noise seed, steps, denoise, scheduler, guidance, latent image, VAE.

Output: Decoded image.

Category: sampling/flux

Use case: Generate high-quality images with precise control over Flux sampling parameters.

FluxLatentSampler
Generates empty latents for Flux.1 with adjustable shift parameters.
Inputs: Model, width, height, batch size, max shift, base shift.

Outputs: Modified model and latent.

Category: advanced/model

Use case: Create latents for Flux workflows with custom resolutions and sampling adjustments.

LoadImageAndScaleToTotalPixels
Loads an image from the input directory and scales it to a specified total pixel count (in megapixels).
Inputs: Image file, upscale method, target megapixels.

Outputs: Scaled image and mask (from alpha channel, if present).

Category: image

Use case: Preprocess images to desired resolutions for diffusion or other workflows.

LoadModelAndUpscaleImage
Loads an upscale model and applies it to enhance the resolution of an input image.
Inputs: Image, upscale model name.

Output: Upscaled image.

Category: image/upscaling

Use case: Improve image quality using pretrained upscale models.

MultiLatentSelector
Selects one of up to four input latents based on a selector, simplifying dynamic workflows.
Inputs: Up to four latents, selector.

Output: Selected latent.

Category: utilities/latent

Use case: Switch between latents without complex rerouting in workflows.

MultiModelLoader
Loads a diffusion model, dual CLIP models, VAE, and optionally applies a LoRA with customizable strengths.
Inputs: UNET name, weight dtype, CLIP names (two), CLIP type, VAE name, LoRA name, model/CLIP strengths, bypass LoRA option, CLIP device.

Outputs: Diffusion model, CLIP, VAE.

Category: loaders

Use case: Efficiently load and configure models for diffusion workflows, with LoRA support.

Known Limitations
Flux-specific nodes (FluxAdvancedSampler, FluxLatentSampler) require Flux.1 models, which may need 6-12 GB of VRAM depending on the model.

LoadModelAndUpscaleImage requires compatible upscale models, downloadable separately.

Ensure PyTorch is installed with the correct CUDA version for GPU users to avoid compatibility issues.

Some nodes may not work with outdated ComfyUI versions or incompatible model types.

Heavy workflows (e.g., large batches or high-resolution images) may require significant computational resources.

Support
For issues or feature requests, open an issue on this repository: GitHub Issues.

Check the ? icon on each node in ComfyUI for detailed descriptions.

Join the ComfyUI community on Reddit or Discord for additional support.
