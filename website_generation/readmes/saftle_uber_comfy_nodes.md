# Uber Comfy Nodes - Misc ComfyUI Nodes


Handy "scratch-itch" nodes I've built while working in ComfyUI.
Install the repo via **Comfy Manager** (recommended), then restart ComfyUI. All nodes appear under **Uber Comfy**.


---


## Node list


| # | Display name | What it does | Typical use-case |
|---|--------------|--------------|------------------|
| 1 | **ControlNet Selector** | Dropdown of every ControlNet file; *does not* load the model. | Pick once, pass name downstream. |
| 2 | **Load Optional ControlNet Model** | Core loader fork with an extra **None** option so a workflow can disable ControlNet on the fly. | On/off toggles without duplicate graphs. |
| 3 | **Diffusers Selector** | Dropdown of every Diffusers-format model folder; zero weight loading. | Feed the chosen path to custom loaders or merge nodes. |
| 4 | **Save Image JPG No Meta** | Saves JPG (set quality) **without** PNG metadata chunks. | Produce lightweight web images. |
| 5 | **Multi Input Variable Rewrite** | Up to 26 optional inputs (`{a}`…`{z}`) replace placeholders inside a template string. | Dynamic prompts, filename templating. |
| 6 | **Text Regex Operations** | Chain up to 20 regex find/replace operations, each with its own pattern, replacement, and multiline flag. | Complex multi-step text processing and caption cleanup. |
| 7 | **Video Segment Calculator** | Given clip duration, FPS & index, returns frame count, skip offset, precise start/end times (optional overlap). | Slice long videos into equal segments. |
| 8 | **Model Similarity Node** | Compares two Stable-Diffusion models (tested SD1.x and SDXL so far) **MODEL** sockets. Calculates cosine similarity across every self-attention layer in input, middle and output blocks. | Detect fine-tunes, merges, or genuine scratch-trained checkpoints. |
| 9 | **Model Weight Dumper** | Dumps all weight keys from a **MODEL** socket with optional shape/dtype info and prefix filtering. | Inspect model architecture, debug custom loaders, compare layer structures. |
| 10 | **Runware Resolution Calculator** | Analyzes input image (with optional mask) and selects optimal resolution from model-specific presets using aspect ratio matching and area utilization scoring. | Auto-select best generation resolution for Nano Banana 2 and similar models. |
| 11 | **Adaptive Image Scaler** | Intelligent scaling with automatic ML upscaler engagement (>1.08× scale), progressive tile reduction on OOM, and synchronized alpha channel processing. | High-quality upscaling with fallback safety and dimension alignment. |


---


## Example – Model Similarity Node


```
[Checkpoint Loader] ─► base_model
[Checkpoint Loader] ─► target_model
                    ╰─► Model Similarity Node
```


Possible outputs:


```
Similarity:  0-5 %   → truly independent training
Similarity: 60-90 %  → fine-tune / weight-merge
Similarity: 95 %+    → almost identical weights
```


---


## Examples for Selected Nodes


### Text Regex Operations
```
Input text: "
*Start* of line and some extra text $5.99."


num_operations: 3
Pattern 1: "^\*"          → Replacement 1: "-"            (convert bullet * at line start to dash -)
Pattern 2: "\*(.*?)\*"  → Replacement 2: ""            (remove asterisks around words)
Pattern 3: "\$(.+)"       → Replacement 3: "Price: \1"      (label prices starting with $)


use_multiline_1: true
use_multiline_2: false
use_multiline_3: false


Output: "-Start of line and some extra text Price: 5.99."
```


### Multi Input Variable Rewrite
```
Input text: "Create {a} image of {b} in {c} style"
Input a: "a beautiful"
Input b: "mountains" 
Input c: "anime"
Output: "Create a beautiful image of mountains in anime style"
```


### Video Segment Calculator
```
Duration: 45.0 seconds, FPS: 30.0, Index: 2
Output: frame_load_cap=1350, skip_first_frames=2700, start_time=90.0, end_time=135.0
(Use this to split a 2-minute video into 45-second chunks and process second 90-135 separately)
```


### Load Optional ControlNet Model
```
Set ControlNet name to "None" to disable ControlNet loading in workflows without rebuilding.
```


### Save Image JPG No Meta
```
Saves all images in the batch as JPG files with the specified quality without writing any metadata
```


### Model Weight Dumper
```
[Checkpoint Loader] ─► MODEL ─► Model Weight Dumper

show_shapes: true
filter_prefix: "model.diffusion_model.input_blocks"

Output: Text list of all matching weight keys with shapes and dtypes
Example output line: "model.diffusion_model.input_blocks.0.0.weight → (320, 4, 3, 3) (torch.float16)"
```


### Runware Resolution Calculator
```
Input: Full image (1920×1080), cropped image, mask highlighting subject area (400×600px ROI)
model_preset: "Nano Banana 2"

Process:
- Analyzes ROI aspect ratio (2:3 portrait)
- Tests fitting strategies (width-anchor, height-anchor, proportional)
- Scores resolutions by expansion efficiency and scale match

Output: width=896, height=1200 (optimal 2:3 portrait from preset)
Console: "✓ Selected: 896×1200 (expansion: 2.15x)"
```


### Adaptive Image Scaler
```
Scenario 1: Small upscale (1024×1024 → 1152×1152, scale 1.125x)
interpolation: "lanczos"
upscale_model: (connected)
dimension_alignment: 64

Process: Engages ML upscaler (>1.08× threshold), tiles at 512px, adjusts to 1152×1152 (64px aligned)
Output: High-quality ML-upscaled image with alpha channel preserved via bicubic interpolation


Scenario 2: Large downscale (4096×4096 → 1024×1024, scale 0.25x)
interpolation: "area"
upscale_model: None

Process: Uses direct "area" interpolation (best for downscaling), bypasses ML model
Output: Clean downscaled image with all 4 channels preserved
```


---


*Open an issue or PR if you spot a missing utility—this repo will keep growing as new workflow gaps appear.*
