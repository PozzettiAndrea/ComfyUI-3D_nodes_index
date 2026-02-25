# ComfyUI Save Prompt and Output
[![Sponsor](https://img.shields.io/badge/Sponsor-t22m003-red)](https://github.com/sponsors/t22m003)

This custom node and hook for ComfyUI automatically saves all intermediate outputs (images and metadata) for every executed node in your workflow.

## Features

- **Automatic Hook**: No need to place special nodes. Just running your workflow captures everything.
- **Workflow Logging**: Saves the full workflow and parameters used for generation.
- **Intermediate Output**: Captures outputs from executed nodes, including images and non-image data (serialized).
- **Organized Storage**: Creates a unique folder for each execution (Queue) based on the Prompt ID.
  - Path: `ComfyUI/output/hooked_outputs/<prompt_id>/`

## Installation

1. Clone this repository into your `ComfyUI/custom_nodes/` directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone git@github.com:t22m003/ComfyUI_SavePromptAndOutput.git
   ```

2. Restart ComfyUI.

## Usage

Just run your workflows as usual.
Check the `ComfyUI/output/hooked_outputs/` directory for results.

## Configuration

Currently, the save path is hardcoded to `ComfyUI/output/hooked_outputs`.
You can modify `hooks.py` if you need to change the location.
