# va1 — Custom ComfyUI Nodes

A collection of custom ComfyUI nodes for image manipulation, comparison, and creative workflows.

---

## Nodes

### 1. Pad Image by Aspect for Outpaint

A versatile node designed to **expand**, **pad**, and **mask** images to fixed or randomized aspect ratios with precise spatial and scale control — engineered for outpainting, compositional layout, and creative canvas expansion.

#### Key Features

* **Aspect Ratio with Random Option**: Choose from fixed presets (`16:9`, `9:16`, `3:2`, `2:3`, `4:5`, `5:4`, `1:1`) or select **`random`** to pick a new ratio on each run.
* **Scale Percentage**: Shrink the input image **after** canvas sizing. Presets range from **`50%`** to **`100%`**, plus **`random`** for varying scales each execution. When using `1:1`, **100%** is disabled to ensure visible shrinkage.
* **Placement Control**: Full spatial options:
  * **Directional**: `left`, `right`, `up`, `down`
  * **3x3 Grid**: `top-left`, `top-mid`, `top-right`, `mid-left`, `center`, `mid-right`, `bottom-left`, `bottom-mid`, `bottom-right`
  * **Random**: Uniform placement anywhere on the canvas.
  * **Smart Fallbacks**: Directional choices auto-revert to **`center`** if incompatible with the aspect ratio's orientation.
* **Rotation**: Rotate the input image before padding. Options from `0` to `330` degrees in 30-degree steps, or **`random`**.
* **Background Color**: Choose from `white`, `black`, or `grey` for padded areas.
* **Feathered Mask**: Generates a soft-edged mask for the new padded areas to facilitate seamless inpainting/outpainting.

#### Inputs

| Name           | Type                                                                 | Description                                                                                                                    |
| -------------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `image`        | `IMAGE`                                                              | The input image tensor (B x H x W x C).                                                                                       |
| `aspect_ratio` | `"random"`, `"16:9"`, `"9:16"`, `"3:2"`, `"2:3"`, `"4:5"`, `"5:4"`, `"1:1"` | Target aspect ratio for the canvas. Select **`random`** for a fresh ratio each run.                               |
| `placement`    | `"center"`, `"random"`, directional, or 3x3 grid positions          | Spatial placement of the image inside the new canvas.                                                                          |
| `scale_pct`    | `"random"`, `"50"` – `"100"`                                        | Percentage to shrink the original image after canvas sizing. `100` disabled for `1:1`.                                         |
| `rotation`     | `"random"`, `"0"` – `"330"` (30-degree steps)                       | Rotation angle applied to the input image before padding.                                                                      |
| `bg_color`     | `"white"`, `"black"`, `"grey"`                                       | Background color for padded areas.                                                                                             |
| `seed`         | `INT` (default `0`)                                                  | Slider to force node re-execution.                                                                                             |
| `feathering`   | `INT` (0–1024)                                                       | Softness of the mask's edge — higher values produce smoother transitions at the padded border.                                 |

#### Outputs

| Name     | Type     | Description                                                                                     |
| -------- | -------- | ----------------------------------------------------------------------------------------------- |
| `Image`  | `IMAGE`  | The padded (and optionally shrunk/rotated) image tensor.                                        |
| `Mask`   | `MASK`   | Feathered mask where `0` = original content, `>0` = padded regions with smooth blending values. |
| `Params` | `STRING` | Summary of the parameters used (aspect ratio, placement, scale, rotation).                      |

---

### 2. Image Mask Comparer

Compares the masked regions of two images and returns a boolean indicating whether they match above a configurable similarity threshold. Useful for verifying that a specific region (e.g. a logo or label) has been preserved after an AI generation or inpainting step.

#### Key Features

* **Masked Region Comparison**: Compares only the pixels within a mask, ignoring everything outside.
* **Dual Similarity Metric**: Uses a weighted combination of Mean Absolute Error (MAE) similarity and Normalized Cross-Correlation (NCC) for robust matching.
* **Automatic Retry**: When `max_retries` > 0 and the comparison fails, the node will:
  1. **Randomise** the seed of every KSampler/noise node it finds in the prompt.
  2. **Re-queue** the modified prompt via direct queue access (with HTTP POST as fallback).
  3. **Interrupt** the current execution so downstream nodes never see the bad result.
* **Broad Sampler Support**: Recognises seeds from `KSampler`, `KSamplerAdvanced`, `SamplerCustom`, `RandomNoise`, Impact Pack samplers, and any node with a `seed` or `noise_seed` input.

#### Inputs

| Name          | Type    | Description                                                                                     |
| ------------- | ------- | ----------------------------------------------------------------------------------------------- |
| `image_a`     | `IMAGE` | The reference image (original).                                                                 |
| `image_b`     | `IMAGE` | The generated/modified image to compare against.                                                |
| `mask`        | `MASK`  | The mask defining which region to compare. White (1) = region of interest.                      |
| `threshold`   | `FLOAT` | Similarity threshold (0.0–1.0, default 0.90). Values at or above this are considered a match.   |
| `max_retries` | `INT`   | Maximum number of retry attempts (0–50, default 4). Set to 0 to disable automatic retries.      |

#### Outputs

| Name         | Type      | Description                                                           |
| ------------ | --------- | --------------------------------------------------------------------- |
| `is_match`   | `BOOLEAN` | `True` if the masked regions match above the threshold.               |
| `similarity` | `FLOAT`   | The computed similarity score (0.0–1.0).                              |
| `image_out`  | `IMAGE`   | Pass-through of `image_b` for downstream use.                         |

---

## Primary Use Cases

* **Outpainting & Canvas Expansion**: Prepare larger canvases around existing images with precise control.
* **Quality Verification**: Automatically check that inpainting preserved critical regions (logos, text, faces).
* **Automated Retry Loops**: Re-generate until a specific region matches the original, without manual intervention.
* **Batch Processing**: Randomised parameters enable varied compositions across batch jobs.

---

## Installation

**Option 1: ComfyUI Manager**

1. Open **ComfyUI Manager**
2. Click **"Install from URL"**
3. Paste:

   ```text
   https://github.com/vaishnav-vn/va1
   ```

**Option 2: Manual**

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/vaishnav-vn/va1.git
```

Restart ComfyUI.

---

## Node Metadata

| Node                        | Display Name                    | Category        |
| --------------------------- | ------------------------------- | --------------- |
| `RandomAspectRatioMask`     | Pad Image by Aspect for Outpaint | `va1`          |
| `ImageMaskComparer`         | Image Mask Comparer             | `image/compare` |

---
