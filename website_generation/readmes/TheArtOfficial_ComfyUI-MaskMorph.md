# Directional Mask Expand (ComfyUI custom node)

Expands a mask along a specified direction, measured clockwise in degrees:

- `0` = up, `90` = right, `180` = down, `270` = left.
- `pixels` controls how many pixels to extend along that vector.
- If `pixels` is `0`, the mask is returned unchanged.

Separate node for pinch/widen:
- **Mask Pinch/Widen**: keeps the outer silhouette fixed and adjusts inner gaps by operating inside the mask’s bounding box using directional morphology on the inverted mask.  
  - `vertical_pinch` / `vertical_widen`: operate horizontally on the gap between left/right sides.  
  - `horizontal_pinch` / `horizontal_widen`: operate vertically on the gap between top/bottom.  
  - `taper_amount` = pixel amount for the operation; `0` disables the effect.

## Installation

1) Place this folder inside `ComfyUI/custom_nodes/` (already done here).
2) Install any extra deps if you add them to `requirements.txt` (none needed by default).
3) Restart or reload ComfyUI custom nodes.

## Usage

- Add **Directional Mask Expand** from the `mask` category.
  - Inputs: `mask`, `angle_deg` (float), `pixels` (int).
  - Output: expanded `MASK`.
- Add **Mask Pinch/Widen** from the `mask` category.
  - Inputs: `mask`, `taper_amount` (int), pinch/widen toggles.
  - Output: reshaped `MASK`.

## Notes

- The node includes `IS_CHANGED` so it won't re-run when inputs are unchanged.
