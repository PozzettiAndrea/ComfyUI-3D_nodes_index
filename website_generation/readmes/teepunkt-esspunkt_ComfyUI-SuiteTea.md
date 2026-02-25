# ComfyUI-SuiteTea
<p align="left">
  <img src="assets/SuiteTea.png" alt="SuiteTea Logo" width="400">
</p>

Some good ComfyUI nodes for bad reasons.

## Install
- **ComfyUI Manager → Install from URL** →  
  https://github.com/teepunkt-esspunkt/ComfyUI-SuiteTea.git
- Or manually:  
  git clone https://github.com/teepunkt-esspunkt/ComfyUI-SuiteTea.git  
  into your `ComfyUI/custom_nodes/` folder.

---

## Nodes

### Tea: Save & Reload Image (category: SuiteTea / IO)

A utility node to save VRAM on older GPUs.
Many workflows pass images directly from one model to another → this can cause out-of-memory (OOM) errors on the first run.
This node saves the image to disk and reloads it, forcing upstream tensors to unload.

- Works as both a detacher and a normal image loader.
- Has a file picker with preview (like the stock Load Image node).
- Cleaner defaults: Teafault.png, output/temp, output/saved.

**Inputs**
- `image_in` (optional IMAGE tensor) → triggers save→reload.
- `image`(picker) → choose/upload an image with preview.
- `temp_folder` (default `output/temp`)  
- `filename` (default `Teafault.png`)  
- `also_save_perm` (BOOLEAN, default `false`)  
- `perm_folder` (default `output/saved`)  

**Output**
- `reloaded_image` (BHWC float, shape 1×H×W×3)

**Usage**
- To break tensor lineage:
  Model Output → Tea: Save & Reload Image V2 → Next Node

- To just load a file:
  leave image_in unconnected and pick a file.

---

### Tea: CheckpointLoader (category: SuiteTea / Loaders)

This Node is created to help run a python script run the same workflow with different models
A string-based checkpoint loader to work with external Python batch scripts.
Lets you loop the same workflow across multiple models without clicking through the dropdown.

**Inputs**
- `ckpt_path` (STRING, full path to .safetensors or .ckpt)  

**Usage** (model loop workflow)
1. Create a suiteTea_local.json in suitetea/scripts/ with your private model folder path: 
```{ "MODELS_DIR": "C:/your/full/path/to/checkpoints" }```
2. Run discover_models_flat.py → generates models_list.txt.
3. Build a workflow modelloop.json using Tea: CheckpointLoader instead of the dropdown loader.
4. Run run_all_models.py → will iterate through all models in models_list.txt using the same workflow.

---

### Tea: Load Fram from Vid As Img (category: SuiteTea / IO)

Extract a single frame from any video and output it as an IMAGE tensor.
Useful for extending clips from the last frame, grabbing a reference still, or snapshotting a timestamp—while keeping VRAM usage low. Optionally saves the frame as a PNG to reuse in later chains.

**Inputs**
- `video`(picker) → choose a video
- `mode`(`first` | `last` | `index` | `time`)
- `video_path`(STRING, optional override; if set, this path is used instead of the picker)
- `frame_index`(INT, used when `mode=index`)
- `time_Sec`(FLOAT, used when `mode=time`)
- `max_side`(INT, 0 = no resize; otherwise downscales keeping aspect, e.g. 1024)
- `save_png`(STRING, if empty, auto-names to `output/tea_frames/<video>_<tag>.png`)
- `overwrite`(BOOLEAN)

**Outputs**
- `image`(BHCW float, shape 1xHxWx3)
- `saved_path`(STRING; empty if `save_png=false`)
- `picked_index`(INT; returns the frame index in `index`mode, otherwise `-1`)

**Usage**
- Extend a clip from its last frame:
  `Tea: Load Frame From Vid As Img (mode=last)` → (optional) VAE Encode → your i2v/video pipeline
- Grab a specific moment:
  `mode=time`, set `time_sec=2.5` to pick the frame at 2.5s
  or` mode=index`, set `frame_index=123`
- Persist the still:
  Toggle `save_png=true` (and/or set `save_path`) to store a reusable PNG and break tensor lineage.

**Notes**
- Prefers ffmpeg (fast, robust). If ffmpeg isn’t on PATH, it falls back to OpenCV if installed.
- Works with common formats (mp4, mov, webm, mkv, …) as supported by ffmpeg.
- The node returns a CPU tensor; VRAM is only touched when you feed it into a VAE/model.
- If both `video` and` video_path` are provided, `video_path` takes precedence.

## Scripts

Located in suitetea/scripts/ — helper utilities for batch workflows:

- ```discover_models_flat.py```:
  Scans your private models folder (from suiteTea_local.json) and writes models_list.txt.
Run this whenever you add/remove checkpoints.

- ```run_all_models.py```
  Reads models_list.txt and your exported workflow (modelloop.json).
  Runs the workflow once for each model, saving results into a timestamped folder with the model name as filename prefix.

---

*(More nodes will be added here as SuiteTea grows.)*

## License
MIT
