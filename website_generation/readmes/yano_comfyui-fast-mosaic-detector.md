# ComfyUI Fast Mosaic Detector

📘 **English** | 📗 [日本語](README.ja.md)

High-precision & high-speed mosaic detection node for **ComfyUI**, featuring three modes (FAST / ACCURATE / HYBRID) and adaptive ROI refinement.  
The HYBRID mode delivers near-ACCURATE precision at a fraction of the cost (7× faster).

---

## 🔍 Overview

This node detects mosaic (pixel-block censorship / block-pattern noise) from images or video frames.  
It outputs:

- A **binary mask** (0 or 255)
- Estimated **mosaic block size**

The detector combines:

- **B-mode (FAST)** — lightweight, CUDA batch-optimized
- **D-mode (ACCURATE)** — full histogram + gradient + grid-structure analysis  
- **HYBRID mode** — FAST → ROI extraction → ACCURATE refinement

HYBRID mode typically achieves:

✅ ~85–95% of ACCURATE precision  
✅ ~7× faster than ACCURATE  
✅ Robust for video sequences

---

## Workflow Screenshot
![Workflow Screenshot](assets/examples/ScreenShot.jpg)

## Input Video

https://github.com/user-attachments/assets/17b95590-77cc-435e-8df1-6cf04604c46b

[example_input.mp4](assets/examples/example_input.mp4)

## Output Video (Image&Mask Blend)

https://github.com/user-attachments/assets/28731ee8-8a11-4971-af86-5be63b44a870

[example_output.mp4](assets/examples/example_output.mp4)

---

## Example Workflow

See the example_workflow folder.

---

# ✅ Features

### **FAST Mode**
- ~4 sec for 840[frames]x640x480[pixels] @RTX3090 (210fps)
- May over-detect  
- Best for quick estimation

### **ACCURATE Mode**
- ~420 sec for 840[frames]x640x480[pixels] @RTX3090 (0.5fps)
- Best precision  
- Full-frame exhaustive scan

### **HYBRID Mode (Recommended)**
- ~40–60 sec for 840[frames]x640x480[pixels] @RTX3090 (14-21fps)
- Near-accurate quality  
- Smart ROI refinement  
- Recommended for most use cases

---

# ✅ Inputs & Parameters

Below is the detailed explanation for every parameter in the node.

---

## 🖼 Image
image: IMAGE

Accepts single images or multi-frame batches.

---

# 🎛 ACCURATE Mode (D-mode) Parameters

### ✅ Skin Mask (HSV-based)
| Parameter | Description |
|----------|-------------|
| `hsv_skin_h_low` | Minimum hue for skin detection |
| `hsv_skin_h_high` | Maximum hue |
| `hsv_skin_s_threshold` | Minimum saturation |

Helps detect mosaics primarily appearing on skin regions.

---

### ✅ Gradient Detection
| Parameter | Description |
|----------|-------------|
| `gradient_threshold` | Threshold for edge gradient magnitude |
| `ratio_threshold` | Gradient ratio threshold (block pattern strength) |
| `gradient_band_height` | Height of sampling windows |
| `gradient_band_half_width` | Half-width of sampling windows |

Controls how the algorithm identifies block-like structure.

---

### ✅ Histogram / Grid Structure
| Parameter | Description |
|----------|-------------|
| `histogram_threshold` | Required peak ratio of histogram bin |
| `mosaic_length_min` | Minimum block size |
| `mosaic_length_max` | Maximum block size |
| `intersection_margin` | Allowed misalignment |

---

# 🚀 Execution Mode
### `mode: FAST | ACCURATE | HYBRID`

- **FAST** → Quick, lower precision  
- **ACCURATE** → Highest precision  
- **HYBRID** → Recommended balance  

---

# ⚙ Backend Selection
### `processing_backend: AUTO | CPU | TORCH`
- AUTO → intelligently selects optimal mode  
- CPU → forces CPU  
- TORCH → forces PyTorch/CUDA  

---

# 🔧 System Parameters

### `max_workers`
CPU thread count for accurate mode.

Suggested: equal to physical CPU cores.

---

# 🟦 HYBRID Mode Parameters

### **`fast_recall_boost`**  
Boost recall of FAST detector (0.1–2.0).  
Higher → more ROIs but may include noise.

### **`roi_margin_px`**  
Expand ROIs (recommended: 24px)

### **`refine_logic`**
| Option | Meaning |
|--------|---------|
| `replace` | Replace FAST masks with refined results |
| `union` | Merge masks |
| `intersect` | Keep only overlapping |

Default: `replace`

### **ROI-related parameters**

| Parameter | Description |
|----------|-------------|
| `refine_frame_stride` | Interval of refinement |
| `roi_merge_dilate_px` | Unifies ROIs |
| `roi_max_count` | ROI count limit |
| `min_mask_pixels` | Minimum mask size |
| `frame_cover_threshold` | Frame considered over-detected if exceeding ratio |

---

# 🟩 Adaptive ROI Downscaling

Automatically downscale large ROIs to accelerate refinement.

| Parameter | Description |
|----------|-------------|
| `adaptive_roi_area_ratio` | Shrink ROI when > this % of frame |
| `adaptive_roi_min_side` | Small ROIs never downscale |
| `roi_downscale_large` | Downscale rate (0.4–1.0) |

---

# 🟨 Aspect Ratio Filters

| Parameter | Description                                           |
|----------|-------------------------------------------------------|
| `roi_aspect_ratio_max` | Ignore overly elongated ROIs (recommended range: 3-5) |
| `roi_min_short_side` | Ignore too-small ROIs                                 |

Useful for rejecting window frames, bars, non-mosaic patterns.

---
[manifest.json](manifest.json)
# ✅ Output

- `mask` — 0/255 binary mosaic mask  
- `size` — detected mosaic block size

Fully batch-compatible with ComfyUI's image sequences.

---

# ✅ Recommended Presets

### **Best Practical**
mode = HYBRID  
roi_downscale_large = 0.75  
roi_aspect_ratio_max = 3.0  
fast_recall_boost = 0.9

### **Highest Precision**
mode = ACCURATE

### **Fast Preview**
mode = FAST

---

# ✅ Notes

- Smaller mosaics require `roi_downscale_large = 1.0`
- For anime/non-skin content → expand HSV ranges
- If HYBRID misses regions → increase `fast_recall_boost`

- This node is fully compatible with ComfyUI-VideoHelperSuite for loading video frames and saving processed video outputs. If you plan to use this node with video workflows, installing VideoHelperSuite is strongly recommended.

- When processing Full HD video, we recommend downsizing the image to 0.5 to 0.75 times its original size, as this allows for sufficiently accurate estimation at a faster speed. Since the estimable mosaic size is approximately 4 to 30 pixels, we recommend resizing the image so that the mosaic fits within this size range.

---

# ✅ License
MIT

# ✅ Author
Takahiro Yano  
ComfyUI Fast Mosaic Detector
