<p align="center">
  <img src="images/icon.png" alt="Node Preview" width="300">
</p>

<p align="center">
  <img src="images/01.png" width="45%" alt="16:9 Baseline">
  <img src="images/02.png" width="45%" alt="4:3 Baseline">
  <img src="images/04.png" width="45%" alt="1:1 Baseline">
  <img src="images/08.png" width="45%" alt="follow input">
  <br>
  <em>Qwen Official Qwen Training Aspect Ratio Buckets (16:9 vs 4:3 vs 1:1 vs original input)</em>
</p>

# ComfyUI-Qwen-Canvas

A precision canvas and latent generator designed specifically for **Qwen Image Edit** workflows. It ensures your inputs perfectly align with the high-performance training buckets used by Alibaba's Qwen team.


## 🌟 Why ComfyUI-Qwen-Canvas?

Most models are sensitive to input resolutions. Using standard 512x512 or 1024x1024 latents often results in "composition drift" or "hallucinations" because the model was never trained on those shapes. 

This node acts as a **Hardware-Software Bridge**:
1.  **Official Training Buckets**: Automatically snaps to the exact resolutions Qwen was trained on (up to ~1.7M pixels).
2.  **Visual Proxy**: Real-time dashed-line feedback on the node itself to show the target aspect ratio before you even press "Queue".
3.  **Smart Fitting**: Intelligently fits your reference images into the "Golden Standard" frames using three professional scaling strategies.

---

## 🚀 Features

### 1. Official Resolution Presets
The node enforces the specific resolutions used in Qwen's final training stage to maximize inference quality:

| Aspect Ratio | Target Resolution | Total Pixels |
| :--- | :--- | :--- |
| **1:1** (Square) | $1328 \times 1328$ | ~1.76 M |
| **4:3** (SD) | $1472 \times 1104$ | ~1.62 M |
| **3:4** (Portrait) | $1104 \times 1472$ | ~1.62 M |
| **3:2** (Full Frame) | $1584 \times 1056$ | ~1.67 M |
| **2:3** (Sketch) | $1056 \times 1584$ | ~1.67 M |
| **16:9** (Widescreen) | $1664 \times 928$ | ~1.54 M |
| **9:16** (Vertical) | $928 \times 1664$ | ~1.54 M |

### 2. Intelligent Scaling Strategies (Plus Version)
When providing an input image, choose how it adapts to the Qwen canvas:
* **Crop**: Fills the canvas and cuts off edges (Best for maintaining subject scale).
* **Pad**: Fits the whole image inside the canvas with black bars (Best for keeping the whole composition).
* **Stretch**: Forces the image to match the ratio (Best for precise pixel alignment).

### 3. Real-time Node Canvas
The node's UI dynamically updates:
* **Dashed Outline**: Shows the aspect ratio visually on the node body.
* **Live Preview**: If `vae_encode` is enabled, a low-res thumbnail of the processed result appears directly on the node for instant verification.

---

## 🛠 Node Types

### QwenCanvas (Basic)
* **Purpose**: A fast, lightweight "Empty Latent" generator.
* **Usage**: Select your ratio and link it to your sampler.

### QwenCanvasPlus (Advanced)
* **Purpose**: The ultimate image-to-image / editing pre-processor.
* **Inputs**: Accepts optional `pixels` and `VAE`.
* **Modes**: 
    * **Original (Follow Input)**: Automatically calculates the best "1K-limited" resolution based on your input's unique shape, while remaining VAE-compatible (multiples of 8).

---

## 📦 Installation

1.  **ComfyUI Manager**: Search for `ComfyUI-Qwen-Canvas` and click **Install**.
2.  **Manual**:
    ```bash
    cd ComfyUI/custom_nodes
    git clone [https://github.com/liewcc/ComfyUI-Qwen-Canvas.git](https://github.com/liewcc/ComfyUI-Qwen-Canvas.git)
    ```

## 💡 Pro Tip
When using **Qwen Image Edit** workflows, always use the **Plus** node with `scaling_strategy` set to **Pad**. This ensures the model sees your entire original image within its optimal "vision window," preventing the loss of important details at the edges.

---

## 🔌 Wiring Guide (How to Connect)

### 1. QwenCanvas (Basic Mode)

Best for **Text-to-Image** generation where you need a specific Qwen-optimized empty frame.

* **LATENT Output**  Connect to **KSampler** (samples input).
* **width/height Output**  Connect to any resolution-aware nodes or use as a reference for conditioning.

---

### 2. QwenCanvasPlus (Advanced/Img2Img Mode)

Best for **Image Editing** or **Inpainting** workflows where you have a reference image.

#### Scenario A: The Calibration Workflow (Recommended)

Use this when you want to "force" your input image into a Qwen-standard training bucket.

1. **pixels Input**: Connect your **Load Image** node here.
2. **vae Input**: Connect your **VAE** (from your Checkpoint Loader).
3. **vae_encode**: Set to **"Enabled"**.
4. **LATENT Output**: Connect to **KSampler**'s `latent_image`.
5. **PREVIEW_IMAGE Output**: Use this for a **Preview Image** node to see how the node cropped/padded your original photo.

#### Scenario B: The "Smart Latent" Workflow

Use this when you don't need to encode the image yet, but want the Latent space to match your input's aspect ratio.

1. **pixels Input**: Connect your **Load Image** node.
2. **aspect_ratio**: Set to **"Original (Follow Input)"**.
3. **vae_encode**: Set to **"Disabled"**.

* *The node will now output an empty latent that perfectly matches the aspect ratio of your input image (downscaled to ~1M pixels).*

---

## 💡 Important Logic Notes

* **1K Resolution Limit**: The "Plus" node automatically applies a 1-Megapixel limit (approx.  total area) to follow Qwen's vision encoder constraints, while ensuring dimensions are multiples of 8 for VAE compatibility.
* **Visual Feedback**:
* **Dashed Box**: Represents the target aspect ratio you selected.
* **Solid Image**: Appears inside the node only when `vae_encode` is "Enabled" and an image is processed.


* **Execution Signal**: The Plus node is marked as an `OUTPUT_NODE`, meaning it will update the UI even if its outputs aren't connected to a "Save Image" node.
