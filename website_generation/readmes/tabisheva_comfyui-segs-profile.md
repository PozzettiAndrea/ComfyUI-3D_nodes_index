# comfyui-segs-profile

A tiny ComfyUI custom node that detects whether a face is in profile using SEGS eye detections.

It expects a single `SEGS` input that may contain segments labeled `left_eye` and `right_eye`
(as produced by many SEGS/Impact pipelines). It picks the largest segment for each eye,
computes the area ratio, and returns a boolean `is_profile`.

If one of the eyes is missing, the node returns `is_profile = True` and `eye_ratio = 0.0`.

## Node

**Name in ComfyUI:** `SEGS Is Profile (eye_ratio)`

### Inputs
- `segs` (SEGS): should contain segments with labels `left_eye` and `right_eye` (if detected)
- `threshold` (FLOAT): default `2.0`  
  `is_profile = eye_ratio > threshold`

### Outputs
- `is_profile` (BOOLEAN)
- `eye_ratio` (FLOAT)
- `debug` (STRING) – convenient for previewing values

### Algorithm
1. Extract segments list from `SEGS`
2. Pick the largest `left_eye` and `right_eye` by bbox area
3. Compute `area = (x2-x1) * (y2-y1)`
4. If one eye is missing: `is_profile=True`, `eye_ratio=0.0`
5. Else: `eye_ratio = max(area_left, area_right) / (min(area_left, area_right) + eps)`
6. Compare with `threshold`

## Installation

### Option A: as a git subfolder (recommended)
Clone into ComfyUI custom_nodes:

```bash
cd /path/to/ComfyUI/custom_nodes
git clone https://github.com/tabisheva/comfyui-segs-profile.git

