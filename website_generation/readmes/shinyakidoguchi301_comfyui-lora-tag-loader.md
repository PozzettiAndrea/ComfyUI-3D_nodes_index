## 📄 `README.md`

# LoRA Tag Loader for ComfyUI

This custom node allows you to select a LoRA file from the `models/loras` directory (including subfolders), automatically load training tags from metadata or Eagle MEMO, set strength, and optionally display a preview image.

## Features

- Dropdown selection of LoRA files from `models/loras` (recursive)
- Automatic tag loading from `.safetensors` metadata (`ss_tag_frequency`)
- Optional tag loading from Eagle MEMO with multiple tag packages
- Editable tag textbox
- Strength slider
- Output:
  - `model`, `clip`
  - Formatted text: `<lora:filename:strength>\nTags`
  - Preview image (if `preview.png` exists in the same folder)

## Installation

1. Clone or copy this folder into your `ComfyUI/custom_nodes/` directory:

```bash
git clone https://github.com/yourname/comfyui-lora-tag-loader.git
```

2. Install dependencies:

```bash
pip install safetensors pillow
```

3. Restart ComfyUI.

## Notes

- Eagle MEMO parsing is simulated. Replace with actual API integration for production use.
- Tag packages must be listed in MEMO using the format:
  ```
  Tags:
    - default: anime, 1girl, solo
    - action: anime, 1girl, dynamic pose
  ```
