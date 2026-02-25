# ComfyUI AIO Core

Custom node for ComfyUI that collects key workflow settings in one place and exposes them as individual outputs.

## Included Node

- `AIO Core Settings`

## Inputs

- `checkpoint` (dropdown, includes `(none)`)
- `lora` (dropdown, includes `(none)`)
- `positive_prompt` (multiline text)
- `negative_prompt` (multiline text)
- `sampler` (dropdown, includes `(none)`)
- `scheduler` (dropdown, includes `(none)`)
- `steps` (integer)
- `cfg` (float)
- `filename` (single-line text, optional override)

## Outputs

- `checkpoint` (string, flexible socket type for COMBO compatibility)
- `lora` (string, flexible socket type for COMBO compatibility)
- `positive_prompt` (string)
- `negative_prompt` (string)
- `sampler` (string, flexible socket type for COMBO compatibility)
- `scheduler` (string, flexible socket type for COMBO compatibility)
- `steps` (int)
- `cfg` (float)
- `filename` (string)

## Optional Behavior

- Dropdown value `(none)` is emitted as empty string `""`.
- If `filename` is empty, an automatic value is generated as:
  - `<checkpoint>_<lora>_<sampler>_`
- The `filename` field is auto-filled from `checkpoint`, `lora`, and `sampler`.
- The auto-filled value updates immediately when `checkpoint`, `lora`, or `sampler` changes.
- If you edit `filename` manually, that manual value is kept.
- Clearing `filename` re-enables auto-generated naming.
- Only the file name (no folders) is used for checkpoint and lora in the generated filename.
- File extensions are removed from checkpoint and lora names in the generated filename.
- If checkpoint, lora, and sampler are all empty, filename falls back to:
  - `ComfyUI_`

## Install

Place this folder inside:

- `ComfyUI/custom_nodes/ComfyUI_AIOcore`

Then restart ComfyUI.
