# ComfyUI Fisheye Transform Nodes

Custom nodes for handling fisheye camera distortion in ComfyUI inpainting workflows.

## Problem Solved

When inpainting fisheye images, generative models produce objects with incorrect perspective because they're trained on rectilinear (flat) images. This node pack provides:

1. **Undistort** fisheye → flat image (before inpainting)
2. **Redistort** flat → fisheye (after inpainting)

## Installation

Copy this folder to your ComfyUI custom_nodes directory:

```
ComfyUI/custom_nodes/ComfyUI-FisheyeTransform/
```

Restart ComfyUI.

## Nodes

### 🐟 Fisheye Undistort

Converts fisheye image to rectilinear. Use **before** inpainting.

**Inputs:**

- `image`: Fisheye IMAGE
- `mask`: Optional MASK (will be transformed too)
- `strength`: Distortion strength (0.0-3.0, default 1.0)
- `zoom`: Output zoom level (0.5-2.0, default 1.0)

**Outputs:**

- `image`: Undistorted IMAGE
- `mask`: Undistorted MASK
- `params`: Parameters for redistortion

### 🐟 Fisheye Redistort

Restores fisheye distortion. Use **after** inpainting.

**Inputs:**

- `image`: Flat IMAGE (inpainted result)
- `params`: FISHEYE_PARAMS from Undistort node
- `mask`: Optional MASK

**Outputs:**

- `image`: Fisheye IMAGE
- `mask`: Fisheye MASK

### 🐟 Fisheye Strength Estimate

Estimates distortion strength from image (heuristic).

## Tips

- Start with `strength=1.0` and adjust based on your camera
- If edges look stretched after undistort, increase `zoom`
- Korean street cameras typically use `strength` around 0.8-1.2
