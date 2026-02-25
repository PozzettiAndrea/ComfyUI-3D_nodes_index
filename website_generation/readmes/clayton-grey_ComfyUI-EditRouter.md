# ComfyUI - Edit Router Custom Node

This custom node detects the **first edit** in a batch of frames and splits the batch into:

- **before_edit**: frames before the cut
- **after_edit**: frames after the cut

If there is **no edit**, the node passes **all frames** through `before_edit` and returns an **empty** `after_edit`.

This is intended for **video frame batches** where you want to route “pre-edit” frames and “post-edit” frames into different branches of a workflow. This is useful if you want to apply VFI within a workflow, as hard edits recieve undesirable transition frames.

---

## Node

### **Edit Router**
Category: `video/analysis`

**Inputs**
- `images` (`IMAGE`): A batch of frames (`[B,H,W,C]`).
- `threshold` (`FLOAT`, default `0.06`): Sensitivity for detecting an edit.
- `stable_frames` (`INT`, default `3`): Number of consecutive “stable” frames required to consider the transition finished (used to trim short fades/dissolves).

**Outputs**
- `before_edit` (`IMAGE`): Frames before the detected edit.
- `after_edit` (`IMAGE`): Frames after the edit (fade frames removed).

---

## How it works (high level)

1. Converts frames to **luma** (brightness) and downsamples for more stable scoring.
2. Computes a per-frame **difference score** between consecutive frames.
3. Finds the first frame where the score exceeds `threshold` (the edit boundary).
4. If the edit looks like a short transition (fade/dissolve), it trims frames until the signal returns to “normal motion” for `stable_frames` frames.
5. Returns the split batches.

---

## Tuning guide

### If it **misses edits**
- Lower `threshold` (try `0.04` → `0.05`).

### If it triggers on **normal motion / camera movement**
- Raise `threshold` (try `0.08` → `0.12`).

### If it leaves a couple blended frames from a **short fade**
- Increase `stable_frames` (try `4` to `6`).

### If it trims too aggressively (removes real post-cut frames)
- Decrease `stable_frames` (try `1` to `2`).

---

## Notes / limitations

- Detects **only the first** edit in the batch.
- Best for **hard cuts** and short fades. Long, slow transitions may be treated as “always transitioning” depending on content.
- Designed around an assumed frame rate of **16 fps** (if you changed the implementation to hardcode fps).

---

## Install / usage

1. Place this custom node in:
   `ComfyUI/custom_nodes/ComfyUI-EditRouter/`
2. Restart ComfyUI.
3. Search for **“Edit Router”** in the node menu.
4. Feed an `IMAGE` batch (e.g. from a video loader) into the node.
5. Route `before_edit` and `after_edit` to separate branches.

---

## Troubleshooting

**The node doesn’t show up:**
- Confirm the file has `NODE_CLASS_MAPPINGS` and `NODE_DISPLAY_NAME_MAPPINGS`.
- Confirm the folder is under `custom_nodes/` and ComfyUI was restarted.

**after_edit is empty but I expected frames:**
- If the detected edit occurs near the end of the batch, there may not be many “after” frames.
- Try lowering `stable_frames` or raising `threshold`.
- (If you still hit this) add temporary debug prints for `start`, `end`, and `b`.

---
