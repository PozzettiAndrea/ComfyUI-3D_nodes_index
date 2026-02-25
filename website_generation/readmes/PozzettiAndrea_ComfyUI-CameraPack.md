# ComfyUI-CameraPack

Camera utilities for ComfyUI. Convert between camera formats.

## Nodes

### DA3 to Load3D Camera
Convert DepthAnythingV3 camera parameters to ComfyUI's Load3DCamera format for use with Preview3D.

**Inputs:**
- `extrinsics` (EXTRINSICS) - 4x4 pose matrix from DA3
- `intrinsics` (INTRINSICS) - 3x3 intrinsics matrix from DA3
- `target_distance` (optional) - Distance from camera to target point
- `zoom_scale` (optional) - Scale factor for zoom

**Output:**
- `camera_info` (LOAD3D_CAMERA) - Compatible with Preview3D node

### Create Load3D Camera
Manually create a Load3DCamera from position, target, and zoom values.

**Inputs:**
- `pos_x`, `pos_y`, `pos_z` - Camera position
- `target_x`, `target_y`, `target_z` - Look-at target
- `zoom` - Zoom level
- `camera_type` - "perspective" or "orthographic"

**Output:**
- `camera_info` (LOAD3D_CAMERA)

## Installation

### Via ComfyUI Manager
Search for "CameraPack" in ComfyUI Manager.

### Manual
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/PozzettiAndrea/ComfyUI-CameraPack.git
```

## Usage

Connect DA3 Giant model outputs to the converter:
```
[DA3 Giant] → extrinsics → [DA3 to Load3D Camera] → camera_info → [Preview 3D]
           → intrinsics ↗
```

## License

MIT
