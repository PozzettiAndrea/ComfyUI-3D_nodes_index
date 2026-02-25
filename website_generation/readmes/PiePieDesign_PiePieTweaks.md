# PiePieTweaks

Custom nodes for ComfyUI by PiePieDesign

## Nodes

### PiePie - Preview Image

A preview node that gives you control over when images get saved.

**The Problem It Solves:**
- Combines behavior of Preview Image and Save Image core nodes
- Allows for ad-hoc saving to follow the Save Image prefix formats
- Key use case: you have a lot of runs with mixed quality results. You only want to save the good ones and not the bad ones. -> Use "Manual Save" mode
- Key use case: you want to save all the runs just like the Save Image node. -> Use "Always Save" mode

**How It Works:**

Two modes to choose from:

1. **Always save mode** - Works exactly like Save Image
   - Every generation automatically saves to your output folder

2. **Manual save mode** - Only saves when you click the button
   - Generates and shows preview
   - Nothing gets saved until you click "💾 Manual Save"
   - Bad generations? Just re-generate
   - Good generation? Click save and it goes to your output folder with the same prefix you would have had with the Save Image node

---

### PiePie - Resolution Picker

Quick way to pick optimal resolutions for different model types.

**The Problem It Solves:**
- No more guessing which resolution works best for your model
- No more manually typing in width/height values
- Extensable with the js/resolutions.js file

**How It Works:**

1. Choose your model type (Flux, SDXL, SD1.5, Pony, etc.)
2. Choose orientation (Portrait, Landscape, Square)
3. Pick from the filtered list of optimal resolutions
4. Or select CUSTOM and enter whatever dimensions you want

The dropdown dynamically updates based on your selections, showing only relevant resolutions.

---

### PiePie - Resolution from Megapixels

Find the closest suggested resolution to your target megapixel count.

**The Problem It Solves:**
- You know you want "around 1.5 megapixels" but don't want to calculate dimensions
- Key use case: you're iterating fast and want consistent megapixel counts without manually picking resolutions
- Optional use case: you want to stay under a certain megapixel limit for VRAM reasons

**How It Works:**

1. Set your target megapixels (e.g., 1.5)
2. Choose model type and orientation filters (or leave as ALL)
3. Toggle "do not exceed" if you want to enforce a hard limit
4. Node outputs the closest matching width, height, and actual megapixels

---

### PiePie - Text Concatenate

Simple text concatenation with a separator.

**The Problem It Solves:**
- Joining multiple text inputs without messy workarounds
- Key use case: combining prompts, filenames, or tags from different sources

**How It Works:**

Takes multiple text inputs and joins them with your chosen separator (space, comma, newline, etc.).
Allows for manual entry or inputs.

---

### PiePie - Lucidflux

Image restoration and enhancement using the LucidFlux model with Flux diffusion.


**Notes:**

1. **Dimension workaround** - dimensions are automatically adjusted to SwinIR requirements. There might be a better way of handling that but this avoids a lot of issues.
2. **Use embeddings or conditioning** - precomputed prompt embeddings or live CLIP conditioning. I suggest using the embeddings and ensure "use_embeddings" is TRUE. IF using CLIP then set that to false.
3. **Accelerator** - FLUX Turbo is in example workflow, optional. Use 4-8 steps instead if using.
4. **Prepreocess** - OPTIONAL - Suggest using HYPIR (see workflow example with preprocessing) as preprocessor for most general use cases. This requires ComfyUI-HYPIR custom node download.

The node handles model caching, memory management, and optional model offloading for VRAM efficiency.

**Required Models and Download Links:**

| Model | Location | Download Link | Notes |
|-------|----------|---------------|-------|
| **LucidFlux Checkpoint** | `ComfyUI/models/LucidFlux/` | [lucidflux.pth (3.39 GB)](https://huggingface.co/W2GenAI/LucidFlux/blob/main/lucidflux.pth) | Main restoration model |
| **SwinIR Prior** | `ComfyUI/models/LucidFlux/` | [Download from LucidFlux repo](https://github.com/W2GenAI-Lab/LucidFlux) | Use `tools.download_weights` script |
| **Prompt Embeddings** (Optional) | `ComfyUI/models/LucidFlux/` | [prompt_embeddings.pt (8.39 MB)](https://huggingface.co/W2GenAI/LucidFlux/blob/main/prompt_embeddings.pt) | Pre-computed embeddings |
| **Flux Model** (Recommended) | `ComfyUI/models/unet/` | [flux1-dev-fp8.safetensors (17.2 GB)](https://huggingface.co/Comfy-Org/flux1-dev/blob/main/flux1-dev-fp8.safetensors) | FP8 quantized for lower VRAM usage. Alternative: [Kijai/flux-fp8](https://huggingface.co/Kijai/flux-fp8) |
| **VAE** | `ComfyUI/models/vae/` | [ae.safetensors](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/ae.safetensors) | Flux VAE |
| **CLIP Vision** (Recommended) | `ComfyUI/models/clip_vision/` | [siglip2-so400m-patch16-512](https://huggingface.co/google/siglip2-so400m-patch16-512) | Google SigLIP 2 model (4.55 GB) |


## Installation

### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI
2. Click the "Manager" button
3. Click "Install Custom Nodes"
4. Search for "PiePieTweaks"
5. Click Install
6. Restart ComfyUI

### Method 2: Manual Install

Clone this repository into ComfyUI/custom_nodes

## Contributing

Found a bug? Have a feature idea? Open an issue!

Pull requests welcome. Please keep it simple and well-commented.

## License

MIT License

## Credits

Made by PiePieDesign