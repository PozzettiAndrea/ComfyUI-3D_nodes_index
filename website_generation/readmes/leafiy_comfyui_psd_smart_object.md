# ComfyUI PSD Smart Object Nodes

Custom ComfyUI nodes that understand Photoshop mockup files. Drop a PSD/PSB
into `ComfyUI/input`, feed any image (from the usual `Load Image` node or by
providing a path on disk), and the node will automatically project that image
onto every smart-object layer you select. Perspective, rotation, and scale
follow the transform data stored inside the PSD smart object, so the result
matches what you would get when replacing the layer inside Photoshop.

## Features
- **PSD Smart Object Inspector** – Lists each smart-object layer (name, id,
  bounding box, transform box). Use it to confirm the layer names you want to
  target.
- **PSD Mockup Embedder** – Uploads PSD/PSB files directly from the node,
  reuses the PSD’s original clipping stack (shadows, highlights, rounded
  corners, etc.), projects your image into the smart objects, resizes the result
  to any width (default 800 px), and emits the composited tensor plus an
  auto-saved PNG.
- Works with PSD/PSB files, multiple smart objects, and either ComfyUI `IMAGE`
  tensors or file paths.

## Installation
1. Copy this folder into `ComfyUI/custom_nodes/comfyui_psd_smart_object`.
2. (Optional) install the lightweight dependencies inside your ComfyUI
   environment:
   ```bash
   pip install -r requirements.txt
   ```
3. Restart ComfyUI so it can discover the new nodes.

## Usage
1. Place PSD/PSB mockups under `ComfyUI/input/psd` (or pass an absolute path).
2. On **PSD Mockup Embedder**, click “choose PSD to upload” (or drag a PSD onto
   the node). The bundled frontend script uploads the file into `ComfyUI/input`
   and fills the `psd_file` field automatically.
3. Load your artwork with any stock `Load Image` (or `Upload Image`) node and
   connect its `IMAGE` output to the embedder. Leave `smart_object_names`
   empty to target the first smart object automatically, or pass a
   comma-separated list to specify others.
4. Adjust `output_width` if you need a specific export size (set to `0` to keep
   the PSD’s native resolution), then trigger the workflow. The node outputs:
   - `mockup_image`: an `IMAGE` tensor that you can preview or post-process.
   - `debug_info`: JSON describing the layers that were replaced.
   - `png_path`: the auto-saved PNG under `ComfyUI/output`, so you no longer
     need an extra `Save Image` node to receive a PNG file.

### Notes & Limitations
- The result is flattened, so advanced Photoshop blend modes (e.g., highlight
  or shadow layers that sit on top of the smart object) are baked into the
  background. Complex lighting stacks may still need Photoshop for final
  touch-ups.
- Smart objects without transform metadata fall back to their axis-aligned
  bounding boxes.
- Perspective warping depends on OpenCV. If ComfyUI logs an import error,
  install `opencv-python-headless` in the same environment.

## Requirements
See `requirements.txt`. ComfyUI already brings Torch and Pillow, so the
additional runtime dependencies are:
- `psd-tools` – parses PSD/PSB files and exposes smart-object metadata
- `opencv-python-headless` – handles the perspective warp
- `numpy` – tensor and array glue code

## Development
The nodes live in `psd_mockup_node.py`. Run
`PYTHONPYCACHEPREFIX=/tmp/pycache python -m py_compile psd_mockup_node.py`
before shipping changes to make sure there are no syntax issues.
