# ComfyUI Outline Alpha Snap

A ComfyUI custom node that adds an outside-only outline around the opaque region of an image while cleaning up semi‑transparent edge pixels and removing stray islands (keeps the largest connected component only).

## Node
- Name: `Outline Alpha Snap`
- Category: `Image/Outline`
- Inputs:
  - `image` (IMAGE)
  - `width` (INT): outline width in pixels (outside-only). `0` disables outline.
  - `color` (STRING): HTML hex color `#RRGGBB` or `#RRGGBBAA`
- Output:
  - `IMAGE`

## Notes
- Preserves transparency, but clamps alpha to the cleaned mask (largest component only).
- Semi‑transparent pixels adjacent to solid pixels are dropped (edge snap behavior).
- RGB inputs are treated as fully opaque.

## Install
Place this folder in `custom_nodes/` and restart ComfyUI.

## Example
- `width`: `1`
- `color`: `#222222`
