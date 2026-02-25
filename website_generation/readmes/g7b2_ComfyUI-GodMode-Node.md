# 👑 ComfyUI God Mode Node (All-In-One)

A powerful, single-node workflow solution for ComfyUI. It aims to replicate the **Stable Diffusion WebUI (A1111)** experience within a single custom node.

**Zero Spaghetti Wiring! Just Focus on Creation.**

## ✨ Features

*   **All-in-One**: Checkpoint + VAE + CLIP Skip + Prompt + Sampler + Save Image.
*   **5-Slot LoRA Stack**: Mix up to 5 LoRAs with independent strength control.
*   **ControlNet Integrated**: Built-in ControlNet support (Model + Strength + Start/End).
*   **Smart Mode Switching**: Automatically switches between **Text-to-Image** and **Image-to-Image** based on input connection.
*   **Hires. Fix**: Built-in Latent Upscale + Second Pass Sampling (High-Res generation).
*   **Post Upscale**: Support for model-based image upscaling (e.g., 4x-UltraSharp).
*   **Metadata Support**: Generated images contain full workflow metadata. Drag and drop them back to ComfyUI to restore settings!

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)
1.  Open ComfyUI Manager.
2.  Click "Install via Git URL".
3.  Paste this repository's URL: `https://github.com/g7b2/ComfyUI-GodMode-Node`
4.  Click Install and Restart ComfyUI.

### Method 2: Manual
1.  Navigate to your `ComfyUI/custom_nodes/` folder.
2.  Clone this repository:
    ```bash
    git clone https://github.com/g7b2/ComfyUI-GodMode-Node.git
    ```
3.  Restart ComfyUI.

## 🛠️ Usage

1.  **Right Click** -> `Custom OneClick` -> `👑 God Mode (Metadata Fixed)`.
2.  **T2I**: Just enter prompt and click Queue.
3.  **I2I**: Connect an image to `input_image_i2i`.
4.  **ControlNet**: Connect an image to `input_image_cn` and select a model.

## 📄 License
MIT License