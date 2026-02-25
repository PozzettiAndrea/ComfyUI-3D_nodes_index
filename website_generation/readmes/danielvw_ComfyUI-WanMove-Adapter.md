# ComfyUI-WanMove-Adapter

**JSON → WanMove TRACKS Node for ComfyUI**

This custom node allows you to convert trajectories from JSON files directly into WanMove TRACKS. It supports:

- Any number of tracks
- Flexible frame length (`num_frames`)
- Normalized (0-1) or pixel coordinates (`normalized`)
- Automatic visibility tensors

---

## Installation

1. Copy the node to `custom_nodes/ComfyUI-WanMove-Adapter/coords_to_tracks.py`  
2. Restart ComfyUI  
3. The node will appear under `WanMove/Adapters`

---

## Usage

```python
from coords_to_tracks import CoordsToWanTracks

node = CoordsToWanTracks()
tracks = node.convert(coords=json_string, width=720, height=720, num_frames=81, normalized=False)
