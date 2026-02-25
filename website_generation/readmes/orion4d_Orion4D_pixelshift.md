# Orion4D Pixel-Shift Nodes for ComfyUI

This custom node pack for ComfyUI provides an advanced image processing workflow to achieve high-quality upscales with an extended dynamic range (HDR), mimicking the flexibility of a camera's RAW file. 
Note: this node will not correct AI image hallucinations, ideally it is used in the last pass from a good quality image (2000/3000px with an X2 or X4 model).

<img width="1643" height="1038" alt="image" src="https://github.com/user-attachments/assets/b878d7de-5472-4710-9145-0186e73f5bb8" />

## Features

*   **Ensemble Super-Resolution (HDR)**: An upscaling node that uses an ensemble (pixel-shift) technique to enhance details, reduce artifacts, and improve sharpness.
*   **32-bit Float HDR Output**: The upscaler generates an unclamped HDR output that preserves all highlight and shadow detail.
*   **Save Image Advanced (16b/32f)**: A robust saving node capable of writing images in standard formats (16-bit PNG/TIFF) and professional HDR formats (32-bit Float TIFF, OpenEXR).
*   **Professional Post-Production Workflow**: The combination of these two nodes allows you to create a "digital master" file, perfect for serious color grading and post-processing.

## Installation

1.  Clone or download this repository into your `ComfyUI/custom_nodes/` directory.
2.  Ensure you have the necessary Python dependencies installed. For the best experience, install the following libraries:
    ```bash
    pip install imageio tifffile opencv-python-headless
    ```
3.  Restart ComfyUI.

## Recommended Workflow

The ideal workflow involves chaining the two nodes to maximize image quality. The `image_float` output is the key to this process.

---

## Node Reference

### 1. Ensemble Super-Resolution (HDR)

This is the core node of the workflow. It upscales an image using an ensemble super-resolution (or *pixel-shift*) technique. The process involves creating multiple variations of the source image, upscaling them individually, and then intelligently merging them to reconstruct finer details, reduce noise, and correct the upscaling model's artifacts.

#### Core Inputs & Outputs

| Name                | Type   | Description                                                                                                                                                                                            |
| ------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **`image`**         | Input  | The low-resolution source image you want to upscale.                                                                                                                                                   |
| **`upscale_model`** | Input  | The upscale model (e.g., ESRGAN, SwinIR) that will be used for **each pass** of the process. The choice of this model is critical and heavily influences the final result's style (see dedicated section below). |
| **`image_float`**   | Output | **(Recommended)** The primary 32-bit float output. Its pixel values are not limited to the 0-1 range, preserving the full dynamic range. This is your "digital RAW master" to be saved as an EXR/TIFF_32F file. |
| **`image_clamped`** | Output | A standardized SDR (Standard Dynamic Range) version, where all values are forced (clamped) to the 0.0-1.0 range. Useful for previews or for compatibility with other nodes that do not support HDR. |
| **`image16`**       | Output | A 16-bit quantized version based on the clamped image. Ready for direct saving as a 16-bit PNG if you don't need HDR flexibility.                                                                     |

---

### Detailed Parameter Table

| Parameter | Technical Description | Impact & Recommended Usage |
| :--- | :--- | :--- |
| **`use_flip`** | **Boolean.** If `true`, each pass has a chance of being flipped horizontally and/or vertically before upscaling, and then flipped back. | **Impact:** Reduces directional or grid-like artifacts that some models can create. It's a form of "Data Augmentation" that forces the model to be more consistent.<br>**Recommendation:** **Leave `true`**. It's an almost "free" improvement to the result's robustness. |
| **`use_translate`** | **Boolean.** If `true`, applies a random sub-pixel shift on the X and Y axes before each pass. This is the core of the "pixel-shift" technique. | **Impact:** Provides the model with slightly different information in each pass, allowing it to "guess" details located *between* the source image's pixels. This is key for reconstructing fine textures.<br>**Recommendation:** **Leave `true`**. Without this, the node just averages N identical upscales. |
| **`randomize_each_run`** | **Boolean.** If `true`, the internal seed used for generating variations is re-randomized on every run, even if the main `seed` parameter is fixed. | **Impact:** Controls reproducibility.<br>- `false` (default): The result is **identical** every time for a given `seed`.<br>- `true`: The result is **different** every time you queue the prompt, even with the same `seed`.<br>**Recommendation:** **Leave `false`** for precision work, comparisons, or debugging. Switch to `true` only if you want to quickly generate multiple variations without manually changing the seed. |
| **`passes`** | **Integer.** Defines the total number of image variations to be generated, upscaled, and merged. | **Impact:** This is the main driver of quality and computation time. <br>- **More passes** = better noise reduction, more effective artifact correction, more stable details. <br>- **Fewer passes** = faster. <br>**Recommendation:** **6-12 passes** is an excellent quality/speed trade-off. Below 4, the benefits are minor. Above 16, gains are marginal while render time increases significantly. |
| **`translate_pixels`** | **Float.** The **maximum** distance (in source image pixels) for the random shift. A shift of `[-val, +val]` is applied to both X and Y. | **Impact:** Controls the magnitude of the variations. <br>- **Too low (< 0.5):** Variations are too similar; detail gain is minimal. <br>- **Too high (> 3.0):** Can cause realignment issues at the image borders. <br>**Recommendation:** A value between **0.75 and 1.5** is a great starting point. `1.1` is an excellent default. |
| **`interpolation`** | **List.** The mathematical algorithm used for resampling during sub-pixel translations. | **Impact:** <br>- **`BILINEAR`:** Fast and soft. Produces smooth transitions without artifacts. An excellent default choice. <br>- **`BICUBIC`:** Sharper, better at preserving high frequencies. However, it can introduce slight "ringing" artifacts around sharp edges. <br>- **`NEAREST`:** Very fast but low quality (aliasing). Only use for pixel art. <br>**Recommendation:** **Start with `BILINEAR`**. If you need maximum sharpness and your image doesn't have hard edges, try `BICUBIC`. |
| **`fusion_mode`** | **List.** The method used to combine the N upscaled and realigned passes. | **Impact:** <br>- **`MEAN`:** Averages each pixel. Extremely effective at eliminating **random noise** (grain). Tends to slightly soften the image. <br>- **`MEDIAN`:** Takes the median value for each pixel. Very robust at removing **outlier artifacts** (e.g., a single black pixel in a white area). <br>- **`MIX`:** A weighted blend of both methods. <br>**Recommendation:** **`MIX` is the most versatile and often the best choice**. |
| **`mix_weight`** | **Float (0.0 to 1.0).** Used only with `fusion_mode: MIX`. Controls the blend weight. `0.0` = 100% MEAN, `1.0` = 100% MEDIAN. | **Impact:** Allows you to fine-tune the benefits of both fusion modes. <br>**Recommendation:** A value around **0.5** is a great starting point. Increase towards `0.7` if you have stubborn artifacts; decrease towards `0.3` if you want to prioritize noise reduction. |
| **`use_unsharp`** | **Boolean.** If `true`, applies an Unsharp Mask to the final image **after** all passes have been merged. | **Impact:** Merging (especially with `MEAN`) can slightly soften the result. This option restores sharpness and clarity. Crucially, this unsharp mask is **unclamped**, meaning it can push highlights above 1.0, creating beautiful specular details perfect for the HDR workflow. <br>**Recommendation:** **Leave `true`** for a more professional and punchy final render. |
| **`unsharp_amount`** | **Float.** The strength of the sharpening effect. Higher values create stronger local contrast along edges. | **Impact:** <br>- **Low (0.1-0.3):** Adds subtle clarity. <br>- **Medium (0.4-0.7):** Clearly visible sharpness. <br>- **High (>0.8):** Risk of halos and an over-sharpened look. <br>**Recommendation:** Start with a moderate value like **0.25 or 0.3**. Adjust based on your upscale model's softness and the number of passes. |
| **`seed`** | **Integer.** The initial seed for the random number generator that controls flips and translations. | **Impact:** Ensures **reproducibility**. With the same seed and parameters, the variations will be identical on every run (if `randomize_each_run` is `false`). <br>**Recommendation:** Use a fixed seed when tweaking other parameters to reliably compare results. |

---

### A Note on Choosing an Upscale Model (`upscale_model`)

The `EnsembleSuperRes` node simply orchestrates the model you provide. The final character of your image depends heavily on this choice. Here are a few model families and their characteristics:

1.  **ESRGAN (and its derivatives: `4x-UltraSharp`, `Remacri`, `BSRGAN`, etc.)**
    *   **Style:** Very sharp, detailed, sometimes to the point of "hallucinating" textures. They are trained to produce visually pleasing and impactful images.
    *   **Best for:** Photographs, realistic renders, any art where you want maximum sharpness.
    *   **With this node:** The ensemble merging process helps to **tame** the aggressive nature of ESRGAN models. Inconsistent "hallucinated" textures are averaged out, resulting in a high level of detail that feels more natural.

2.  **SwinIR (and its derivatives)**
    *   **Style:** Softer and more "photographic" than ESRGAN. They excel at image restoration (noise, JPEG artifacts) and produce a very clean, natural result without adding artificial details.
    *   **Best for:** Upscaling noisy images, faces, or whenever you need a result that is faithful to the original.
    *   **With this node:** A very powerful combination. SwinIR's cleanliness combined with the pixel-shift detail reconstruction yields an extremely clean, detailed, and natural final image. The unsharp mask is often a welcome addition to add back some punch.

3.  **Specialized Models (Anime, Manga, etc.)**
    *   **Style:** Designed specifically to preserve sharp lines, flat color areas, and the distinct style of illustrations.
    *   **Best for:** 2D art, illustrations, anime.
    *   **With this node:** The technique also works very well here. It can help make lines even cleaner and eliminate compression or scaling artifacts that can appear on flat color areas.

**Conclusion:** Don't hesitate to experiment! The combination of **(Upscale Model + Ensemble Parameters)** is your new creative palette for finishing your images.

### 2. Save Image Advanced (16b/32f)

This node is designed to save the image resulting from the HDR workflow, letting you choose the most suitable file format for your needs.

#### Parameters

| Parameter | Description | Recommendation |
| :--- | :--- | :--- |
| **`images`** | The image to be saved. Connect the `image_float` output from the previous node here. | |
| **`format`** | The output file format. This is the most important setting. <br> - **`PNG` / `TIFF`**: 16-bit integer formats. Excellent quality, but HDR data (>1.0) will be clipped (blown-out highlights). Perfect for direct sharing or final delivery. <br> - **`TIFF_32F` / `EXR`**: 32-bit float (HDR) formats. **Recommended.** They preserve all the nuances of the `image_float` output for post-production. | **Use `EXR`** for the best compatibility with VFX and color grading software. |
| **`compression`** | Compression level for formats that support it (like PNG). `0` = none, `9` = maximum. | `6` is a good compromise between file size and saving speed. |
| **`force_opaque_alpha`** | For 16-bit integer formats, this forces the alpha channel to be 100% opaque. This prevents display issues (like black thumbnails) in Windows. | Leave on `true`. |
| **`drop_alpha_on_cv2`** | If OpenCV is used as a fallback to save a PNG, this option drops the alpha channel to prevent potential errors. | Leave on `true`. |

---
<div align="center">

<h3>🌟 <strong>Show Your Support</strong></h3>
<p>If this project helped you, please consider giving it a ⭐ on GitHub!</p>
<p><strong>Made with ❤️ for the ComfyUI community</strong></p>
<p><strong>by Orion4D</strong></p>
<a href="https://ko-fi.com/orion4d">
<img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Buy Me A Coffee" height="41" width="174">
</a>

</div>
