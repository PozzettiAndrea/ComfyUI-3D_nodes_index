![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)
![Made for ComfyUI](https://img.shields.io/badge/Made%20for-ComfyUI-blueviolet)

This is a custom node for ComfyUI designed to remove JPEG compression artifacts, digital noise, and blur from images. It is powered by a **NAFNet-based UNet** model that efficiently restores image quality.

---

# About V2
The project has been updated to **Version 2**. 
- **New Core:** The architecture has been upgraded from a standard ResNet-UNet to a **NAFNet** design.
- **Better Data:** Trained on ~40k high-quality anime images (Danbooru2024).
- **Smarter Training:** Now handles slight blur and uses Perceptual Loss (VGG) to keep textures sharp.

> **Which version to use?** V2 usually gives sharper, cleaner outputs, but it also learned to leave images untouched when they already look clean. If you feel it is too conservative on a specific picture, try V1 (best_ema_15E) and pick the result you prefer.

> **Force processing:** If V2 skips a frame because it thinks it is clean, enable `force_process` and increase `force_noise_std` (default now 0.02; 0.05 works for most stubborn cases). This adds tiny noise so the model always runs; final output is still blended with the original.
---

# Examples

<img width="790" height="234" alt="1_Ready" src="https://github.com/user-attachments/assets/20aeb426-5b85-496a-af39-46bdff7192bc" />
<img width="2702" height="1211" alt="2_Ready" src="https://github.com/user-attachments/assets/a114186f-cd50-431b-9d7c-f0ccd62fec37" />
<img width="2412" height="965" alt="3_Ready" src="https://github.com/user-attachments/assets/01c17f89-3fff-49aa-8b76-016b9f3de9fe" />


---

## 🚀 Installation

The installation consists of two steps: installing the node itself and downloading the model weights.

### Step 1: Install the Node

1.  Open a terminal or command prompt.
2.  Navigate to your ComfyUI `custom_nodes` directory.
    ```bash
    # Example for Windows
    cd D:\ComfyUI\custom_nodes\
    
    # Example for Linux
    cd ~/ComfyUI/custom_nodes/
    ```

3.  Clone this repository into the `custom_nodes` folder:
    ```bash
    git clone https://github.com/SnJake/SnJake_JPG_Artifacts_Noise_Cleaner.git
    ```

4.  **Install Dependencies**: Now, you need to install the required Python packages. The command depends on which version of ComfyUI you are using.

    *   **For standard ComfyUI installations (with venv):**
        1.  Make sure your ComfyUI virtual environment (`venv`) is activated.
        2.  Navigate into the new node directory and install the requirements:
            ```bash
            cd SnJake_JPG_Artifacts_Noise_Cleaner
            pip install -r requirements.txt
            ```

    *   **For Portable ComfyUI installations:**
        1.  Navigate back to the **root** of your portable ComfyUI directory (e.g., `D:\ComfyUI_windows_portable`).
        2.  Run the following command to use the embedded Python to install the requirements. *Do not activate any venv.*
            ```bash
            python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\SnJake_JPG_Artifacts_Noise_Cleaner\requirements.txt
            ```

### Step 2: Install the Model Weights (Or you can skip this step, the node will download the model weights itself after starting the Queue)

1.  Navigate to your `ComfyUI/models/` directory.
2.  Create a folder named `artifacts_remover` inside it, if it doesn't already exist.
3.  Download the v1 or v2 model weights file (`.pt` or `.safetensors`) from the **[Hugging Face page](https://huggingface.co/SnJake/JPG_Noise_Remover)**.
4.  Place the downloaded weights file into the `ComfyUI/models/artifacts_remover/` directory.

### Step 3: Restart

Restart ComfyUI completely. The new node will be available in the "Add Node" menu.

---

## ✨ Usage

The node can be found in the "Add Node" menu under **`😎 SnJake/JPG & Noise Remover`**.

### Inputs

*   **`image`**: The source image to be processed.
*   **`weights_name`**: A dropdown list to select the model weights file from the `models/artifacts_remover` folder.
*   **`weights_path`**: (Optional) A direct path to the weights file if it is located elsewhere.
*   **`base_ch`**: The number of base channels in the model. **This must match the model it was trained with (default is 64)**.
*   **`tile`**: The tile size for processing large images. This helps prevent VRAM shortages. A value of `0` disables tiling. Recommended value: `256-512`.
*   **`overlap`**: The overlap area between tiles for smoother blending. Recommended value: `64-128`.
*   **`edge_aware_window`**: Use a smart blending window that avoids darkening the edges of the image where there are no adjacent tiles. It is recommended to keep this enabled (`True`).
*   **`blend`**: A factor to blend the result with the original image (from 0.0 to 1.0). Small values (e.g., `0.1`-`0.2`) can help restore very fine details if the model has over-smoothed them. `0.0` means the effect is fully applied.
*   **`amp_dtype`**: The precision for computations (for CUDA). `auto` is the optimal choice.
*   **`device`**: The device for computations (`auto`, `cuda`, `cpu`).

### Outputs

*   **`image`**: The image after artifact and noise removal.

---

Training code is included in /training_code for reference, but the main purpose of this repo is the ComfyUI node and pre-trained weights.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/SnJake/JPG-Artifacts-Noise-Cleaner/blob/main/LICENSE.md) file for details.
