# ComfyUI-LTXVGuideRebase

Small ComfyUI addon that provides **segment-safe** utilities for Comfy-Org LTX video nodes.

## Node: `LTXV Rebase Guides (segment-safe)`

Rewrites the LTX guide metadata stored in conditioning under `keyframe_idxs`, to make it easier
to experiment with FLF-style **chained segments** while still reusing earlier guide state.

### Inputs

- **positive / negative**: conditioning inputs that may contain `keyframe_idxs`
- **segment_start_frame**: the start frame (in the *original/global* timeline) that this segment begins at
- **segment_length_frames**:
  - `> 0`: enables filtering guides to the window `[segment_start_frame, segment_start_frame + segment_length_frames)`
  - `-1`: disables filtering; only rebasing (or clearing) is applied
- **mode**:
  - `rebase_and_drop_outside` (default)
  - `drop_outside`
  - `rebase_only`
  - `clear_all`

### Output

Returns the updated `positive` and `negative` conditionings.

## Install into ComfyUI

Copy or symlink this folder into:

`ComfyUI/custom_nodes/ComfyUI-LTXVGuideRebase`

Then restart ComfyUI.

