# Real Noise Pattern Matcher for ComfyUI

Extract authentic noise patterns from real photographs and apply them to AI-generated or composited elements for seamless photorealistic integration.

## Installation

1. Clone or copy this folder to `ComfyUI/custom_nodes/`
2. Restart ComfyUI
3. Nodes will appear under `image/noise` category

## Dependencies

- `torch` (included with ComfyUI)
- `numpy` (standard)
- `scipy` (for gaussian_filter)

Install scipy if needed:
```bash
pip install scipy