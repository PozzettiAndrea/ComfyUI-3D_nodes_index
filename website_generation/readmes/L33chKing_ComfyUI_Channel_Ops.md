![preview](./preview.gif)

# ComfyUI Channel Ops (live-preview)

Comfyui custom nodes that modifies image channels with various per-channel operations across RGB, HSV, and Oklab color-space,  aswell separate image blending node with live-previews


Note: Destination parameter has no effect on any operations other than Overwrites


## Channel Ops



| Operation | Amount | Notes |
|-----------|--------|-------|
| Invert | – | Flip selected channel(s); Hue wraps. |
| Overwrite | – | Copy Source into Destination (cross-space allowed). |
| Overwrite from Image | – | Same as Overwrite but Source comes from 2nd image if connected. |
| Set | x/255 | Set Source to Amount. |
| Add | x/255 | Add Amount to Source. |
| Subtract | x/255 | Subtract Amount from Source. |
| Multiply | raw | Multiply Source by Amount (2 → 2×; 255 → 255×). |
| Divide | raw | Divide Source by Amount (2 → ÷2). |
| Clamp Min | x/255 | Clamp Source ≥ Amount. |
| Clamp Max | x/255 | Clamp Source ≤ Amount. |
| Truncate | 1−x/255 | Snap to step size. |
| Contrast | 1−x/255 | Piecewise contrast around 0.5 (Oklab a/b normalized). |


| Source | Type | Notes |
|--------|------|-------|
| RGB | group | Applies to R,G,B together. |
| R / G / B | single | One RGB component. |
| HSV | group | Operates in HSV; Hue wraps on arithmetic. |
| H / S / V | single | One HSV component. |
| Oklab | group | L,a,b in perceptual space; a/b normalized to ±0.4 for some ops. |

| Destination | Type | Behavior |
|-------------|------|----------|
| R / G / B / H / S / V | single | Write scalar Source value into that component. |
| RGB / HSV / Oklab | group | If Source group matches, copy full vector; else map scalar (HSV: h wraps; Oklab: L=scalar, a/b from normalized scalar). |

Notes
- “Overwrite from Image” uses the second image when connected; size and batch auto-align.

---

## Layer Blending

Modes (sRGB per-channel)

| Mode | Behavior |
|------|----------|
| Normal | B |
| Multiply | A·B |
| Screen | 1 − (1−A)(1−B) |
| Overlay | A≤0.5: 2AB; else: 1−2(1−A)(1−B) |
| Soft Light | (1−2B)A² + 2BA |
| Hard Light | Overlay with B driving |
| Darken / Lighten | min(A,B) / max(A,B) |
| Color Dodge / Burn | A/(1−B) · clamp; 1−(1−A)/B |
| Linear Dodge (Add) / Linear Burn | A+B; A+B−1 |
| Vivid Light | B<0.5: Color Burn(A,2B); else: Color Dodge(A,2B−1) |
| Linear Light | A + 2B − 1 |
| Pin Light | B<0.5: min(A,2B); else: max(A,2B−1) |
| Difference / Exclusion | |A−B|; A+B−2AB |
| Add / Subtract / Divide | A+B; A−B; A/B |
| Hard Mix | threshold(A+B) |
| Darker Color / Lighter Color | Choose pixel by total brightness (sum RGB) |

Compositing & alignment

| Aspect | Rule |
|--------|------|
| Opacity | Out = A·(1−α) + Blend(A,B)·α |
| Resize | Foreground bilinearly resized to background H×W |
| Batch | Align to min(B) |
| Clamp | Final result clamped to [0,1] |

---


## License
MIT
