# SSpack for ComfyUI 🦅SS

Compact, UI-friendly nodes for ComfyUI. Everything ships with the `🦅SS` prefix so you can spot the pack at a glance, and the selectors come with thumbnail helpers for faster browsing.

## Highlights
- LoRA and checkpoint selectors with preview thumbnails (tree/grid/list) plus stack/apply helpers for random or indexed picks.
- Text utilities: prompt filtering/clean-up and weighted text formatting; JSON picker to pull a prompt from a list.
- Image helpers: SDXL/SD1.5/FLUX auto-resize, last-saved-image loader, and an overlay annotator for quick labels.
- Lightweight cache cleaner script for ComfyUI (optional).
- Pure Python/JS—drop it in and restart ComfyUI.

## Installation (quick)
1) Drop this folder into `ComfyUI/custom_nodes/SSpack_ComfyUI`.
2) Make sure Python deps are available (most are bundled with ComfyUI):
   ```
   pip install opencv-python pillow requests
   ```
3) Restart ComfyUI. The JS helpers (`betterLoras.js`, `betterCheckpoints.js`) auto-load.

### Quick start workflow
1) Add **🦅SS Checkpoint Selector** (3/6/12) and pick models; thumbnails appear on right-click.  
2) Add **🦅SS Checkpoint Loader** and feed it the selector’s stack to load a model.  
3) For LoRAs: use **🦅SS LoRA Selector** → **🦅SS Random LoRA Applier** → **🦅SS LoRA Stack Applier** into your model/clip.  
4) Clean prompts with **🦅SS Filter** and weight text with **🦅SS Text Weight**.  
5) For images: run **🦅SS SDXL Auto-Resize** before your pipeline, and use **🦅SS Last Saved Image** to pull the newest output; annotate with **🦅SS Image Annotator** if needed.

## Nodes
- **🦅SS Checkpoint Selector (3/6/12) & Loader** (`ss_checkpoint_loader.py`)  
  Build a checkpoint stack (with thumbnails) and load by index or randomly.
- **🦅SS LoRA Selector / Random Applier / Stack Applier** (`ss_lora_stack.py`)  
  Preview LoRAs, gather trigger words from metadata/CivitAI, stack them, and apply with random or fixed strengths.
- **🦅SS SDXL Auto-Resize** (`ss_sdxl_auto_resize.py`)  
  Snap images to SD1.5/SDXL/FLUX-friendly sizes with crop/pad/letterbox options.
- **🦅SS Image Annotator** (`ss_image_node_annotator.py`)  
  Overlay text labels on images, optionally compositing another layer.
- **🦅SS Last Saved Image** (`ss_last_saved_image.py`)  
  Load the newest (or Nth newest) file from an output folder (supports subfolders and filters).
- **🦅SS Filter** (`ss_filter.py`)  
  Clean and slice prompts: tokenization, NG word removal/erasure, case conversion, de-duplication.
- **🦅SS Text Weight** (`ss_text_weight.py`)  
  Wrap text with weighted brackets; optional prefix/suffix; skip when weight is 1.0.
- **🦅SS JSON Output** (`ss_json_output.py`)  
  Pick one prompt from a JSON array (index, sequential, or seeded random).

## Web UI extras
- **betterLoras.js** and **betterCheckpoints.js** add previews to the right-click menus (list/tree/grid view).  
  Previews are pulled from files that match the model name (`.preview.png/.jpg/.jpeg` or the base image).
- **loraInfo.js** adds a “View info…” menu item for LoRAs (uses ComfyUI-Custom-Scripts dialog if present).

## Tips & notes
- LoRA tag fetching uses CivitAI’s hash API (`utils.py`); allow network access for auto trigger words.
- `opencv-python` is required for the auto-resize node; install it if ComfyUI was built without OpenCV.
- Previews load from files next to your models (`name.preview.png/jpg/jpeg` or the base image).
- The cache cleaner (`clear_comfyui_cache.py`) is optional; run it from inside your ComfyUI folder if UI widgets act up.
- All nodes live under `🦅SS/*` categories in the node browser.

## Quick validation
To sanity-check the Python modules:
```
python -m py_compile ss_*.py
```
If you hit issues or want another node prefixed with 🦅SS, open an issue/PR.
