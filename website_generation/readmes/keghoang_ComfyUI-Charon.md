# ComfyUI-Charon

Custom ComfyUI nodes for CHARON auto-alignment and DA3 camera export.

## Contents
- `__init__.py`: node registrations.
- `nodes/auto_align.py`: `CHARON_3D_Auto_Align` (mesh alignment with optional symmetry + ground snap). Returns both the file path and a transform JSON, and publishes the mesh in `ui.meshes` so it shows in Comfy history.
- `nodes/charon_camera.py`: `CHARON_Camera_From_DA3` (converts DA3 intrinsics/extrinsics to a Nuke Camera3 snippet, with optional transform application).

## Installation
1. Copy this repo folder into your `ComfyUI/custom_nodes/` directory (you can name it `ComfyUI_CHARON` if you want to match the internal label).
2. Install deps in your ComfyUI Python environment:
   ```bash
   pip install -r requirements.txt
   ```
   (Only `trimesh` is required; NumPy is bundled with ComfyUI.)
3. Restart ComfyUI.

## Usage
### CHARON_3D_Auto_Align
- Inputs: `mesh_path`, `symmetry`, `ground_snap`, `filename_prefix` (default `charon_mesh`), `save_transform_json`.
- Outputs:
  - `aligned_mesh_file`: path to the saved aligned mesh in ComfyUI’s output dir.
  - `transform_json`: JSON with `rotation` (3x3) and `translation` (xyz).
- The node also advertises the mesh in the `ui.meshes` block so it appears in history/downloads.

### CHARON_Camera_From_DA3
- Inputs: DA3 `extrinsics_json`, `intrinsics_json`, `batch_index`, `image_width`/`image_height`, `sensor_width_mm`, optional `transform_json` from the align node, optional Nuke export toggle/prefix.
- Outputs: `nukecam_file` (if enabled) and `nukecam_text` (Camera3 snippet with additive Euler/translation).

Place the two nodes in a Comfy graph, feed a mesh into `CHARON_3D_Auto_Align`, and optionally feed its `transform_json` into `CHARON_Camera_From_DA3` to move the DA3 camera to match the aligned mesh.***
