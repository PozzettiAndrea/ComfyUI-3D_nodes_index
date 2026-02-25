# 🎨 ComfyUI-ForgeAPI for InstantID workflow

![ComfyUI](https://img.shields.io/badge/ComfyUI-Extension-blue?style=flat-square) ![SDXL](https://img.shields.io/badge/Model-SDXL-orange?style=flat-square) ![Status](https://img.shields.io/badge/Status-Active-green?style=flat-square)

**A ComfyUI node for controlling a local Forge UI / Automatic1111 WebUI via API.**

This node bridges the gap between ComfyUI's workflow flexibility and Forge UI's superior implementation of specific ControlNet models. It is designed specifically for an **InstantID + Canny ControlNet** workflow on SDXL, allowing you to leverage Forge's robust rendering backend directly from your ComfyUI canvas.

### 🚀 Why use this?
While ComfyUI is a powerful platform, Forge UI often delivers superior results for **InstantID**. This node allows you to:
* Use Forge UI as a rendering engine for ComfyUI.
* Achieve high-quality results in **under 8 steps** (using `dmd2_sdxl_4step_lora_fp16`).
* Seamlessly map InstantID keypoints and Canny edges.

---

## ✨ Key Features

* **SDXL & InstantID Optimized:** Pre-configured for high-performance face reference workflows.

* **Flexible LoRA Support:** Defaults to 4-step LoRAs but supports full customization via dropdowns.

---

## 🛠️ Requirements

### 1. Local Forge UI Instance
You must have a local instance of Forge UI (or Automatic1111) running.
* **Default URL:** `http://127.0.0.1:7860`
* **Flag:** You must launch Forge with the API enabled:
    
    python launch.py --api
    

### 2. Required Models
Place the following models in your Forge UI `models/ControlNet/` directory:

| Model Type | Filename | Description |
| :--- | :--- | :--- |
| **IP-Adapter** | `ip-adapter_instant_id_sdxl.safetensors` | The InstantID adapter. |
| **ControlNet** | `control_instant_id_sdxl.safetensors` | Handles InstantID keypoints. |
| **ControlNet** | `diffusers_xl_canny_full.safetensors` | Handles Canny edge detection. |

> **⚠️ Note:** This node connects to your *external* Forge UI instance. These models must be installed in **Forge**, not just ComfyUI.

---

## ⚡ Quick Start Guide

1.  **Launch Forge UI:**
    Run your local Forge instance with the API flag.
    ```bash
    python launch.py --api
    ```
2.  **Start ComfyUI:**
    Open ComfyUI and load your workflow.
3.  **Add the Node:**
    Search for and add the **Local Forge UI Controller** node.
4.  **Configure:**
    * Select your models from the dropdowns (these are auto-detected from your running Forge instance).
    * Load your `instantid_image` (Face Reference) and `canny_image` (Edge Reference).
5.  **Run:**
    Connect your output and queue the prompt.

---

## 🎛️ Node Parameters

### Required Settings

| Parameter | Description |
| :--- | :--- |
| **`forge_url`** | The API URL for Forge (Default: `http://127.0.0.1:7860`). |
| **`instantid_model`** | Select the IP-Adapter model (e.g., `ip-adapter_instant_id_sdxl`). |
| **`instantid_keypoints_model`** | Select the Keypoints model. |
| **`canny_model`** | Select the Canny ControlNet model. |
| **`prompt`** / **`negative`** | Your text prompts for generation. |
| **`steps`** | Recommended: **8-12**. (8 for speed, 12 for quality). |
| **`lora_tag`** | The LoRA used for acceleration (e.g., `dmd2_sdxl_4step`). |

### Optional Inputs

* **`instantid_image`**: The reference image for facial identity.
* **`canny_image`**: The reference image for composition.
* **`weights`**: Fine-tune the influence of InstantID or Canny (`0.0` to `2.0`).

---

## ❓ Troubleshooting

**Failed to Connect?**
* Ensure Forge UI is running.
* Verify you started Forge with `--api`.
* Check that `forge_url` matches your local address.

**No Images Returned?**
* Verify that all required `.safetensors` are inside the Forge `models/ControlNet/` folder.
* Ensure the models appear in the dropdown lists.

**Dropdowns showing defaults/empty?**
* **Restart Order:** You must start Forge UI *before* starting ComfyUI (or reload the ComfyUI browser tab) so the node can fetch the model list.