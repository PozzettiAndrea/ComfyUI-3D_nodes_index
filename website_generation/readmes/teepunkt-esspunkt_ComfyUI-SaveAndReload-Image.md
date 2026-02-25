# Save & Reload Image – ComfyUI node

A simple utility node for creating a VRAM boundary.  
Because some workflows pass images directly from one model to another, I often ran into OOM errors.  
This node saves the incoming IMAGE to disk and reloads it immediately, forcing upstream tensors to unload.

Use it between heavy preprocessors and samplers to avoid first-run OOM.

## Install
- ComfyUI Manager → **Install from URL** → paste this repo URL  
- or `git clone https://github.com/teepunkt-esspunkt/ComfyUI-SaveAndReload-Image.git` into `ComfyUI/custom_nodes/`

## Node
**Save & Reload Image** (category: IO)  
- Inputs:  
  - `image`  
  - `temp_folder` (default `output/temp`)  
  - `filename` (`bgstrip.png`)  
  - `also_save_perm` (checkbox)  
  - `perm_folder` (default `output/saved`)  
- Output:  
  - `reloaded_image` (BHWC float, shape 1×H×W×3)

## Usage
Use this node in between heavy preprocessors (like background removal) and samplers.  
It forces a disk round-trip so the preprocessor frees VRAM before the sampler starts.
