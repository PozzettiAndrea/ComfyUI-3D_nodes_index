# ComfyUI Quick Resolution Selector

A simple custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allows you to quickly select resolution presets for various models (SDXL, Flux, SD1.5, etc.) from a dropdown menu.

## Features

- **Preset Dropdown**: Select from common aspect ratios and resolutions for SDXL, Flux/SD3, SD1.5, and video formats.
- **Round to Multiple**: Automatically rounds the width and height to a specified multiple (default 64). This ensures your latent dimensions are always valid for the model you are using.
- **Customizable**: All presets are stored in a simple `resolutions.json` file that you can edit.
- **Hot Reload (Values)**: Changes to resolution *values* in the JSON file are applied immediately without restarting ComfyUI.

## Installation

1. Navigate to your ComfyUI `custom_nodes` directory via command line:
   ```bash
   cd /path/to/ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/danielwolber-wood/ComfyUI-QuickResolutionSelector.git
   ```
3. Restart ComfyUI.

## Usage

1. Right-click in the ComfyUI graph or double-click to search.
2. Find the node under **Utils** -> **Resolution Quick Select**.
3. Select a preset from the dropdown menu.
4. Connect the `width` and `height` outputs to an **Empty Latent Image** node or any other node that requires resolution inputs.

## Customization

You can add your own presets by editing the `resolutions.json` file located in the node's directory.

```json
{
  "My Custom Preset": [1234, 5678],
  ...
}
```

### Important Note on Updates
- **Adding New Presets**: If you add a new entry (a new name) to the JSON file, you must **restart ComfyUI** for it to appear in the dropdown menu.
- **Editing Values**: If you modify the numbers for an existing preset, the changes will take effect immediately the next time you queue a prompt (no restart required).

## AI Disclosure

The first draft of this README was written by AI, but was manually edited and checked for correctness.