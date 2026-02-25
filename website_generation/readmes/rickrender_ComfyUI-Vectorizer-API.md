# ComfyUI Vectorizer.ai API Node Pack

This repository contains a pack of useful nodes for ComfyUI designed to simplify a professional vector-based image processing pipeline. Convert raster images to clean, scalable vectors using the [Vectorizer.AI API](https://vectorizer.ai/), and then remove the background with a background removal node for compositing and further creative work. There are options to scale the vector graphic to a user defined value, this can allow for higher resolution raster graphics without quality loss.

![workflow](https://github.com/rickrender/ComfyUI-Vectorizer-API/blob/main/examples/workflow.png)
---

## ✨ Core Features

- **High-Quality Vectorization**: Integrates with the powerful Vectorizer.AI API to convert PNGs into clean, editable SVGs.
- **Infinite Scalability**: Includes a `scaled_png` option to render the resulting SVG at any resolution (e.g., 4x, 8x) for crisp, high-resolution raster images without quality loss.
- **Background Removal Nodes**: Node options for two different methods that detect and remove a solid color background from a raster image or the largest shape from a returned SVG file.
- **Mask Output for Advanced Workflows**: The background remover provides a perfect black and white silhouette mask, ideal for inpainting, compositing, sticker effects, and driving ControlNets.
- **Secure & Convenient**: Supports API key management via an optional `config.json` file, so you don't have to enter your credentials in the workflow.

---

## 📦 Nodes Included

### 1. Vectorizer.ai API

This node is the bridge to the Vectorizer.AI service. It takes an image and sends it for vectorization.

- **Inputs**: `image`, API credentials, `output_format` (`svg`, `png`, `scaled_png`), `mode` (`production` or `test`), and other vectorization parameters.
- **Output**: Returns the original or processed `IMAGE` back into the workflow.
- **Functionality**: Saves the final vector (`.svg`) or raster (`.png`) file to your ComfyUI `output` directory, respecting your `filename_prefix` and numbering.

### 2. Background Remover (Shape)

A node to remove the single largest shape from the background of the returned SVG file with an option to save the edited SVG or pass through an RGBA PNG.

### 3. Background Remover (Color) [WIP]

A fast chroma keyer designed for images with a solid color background.

- **Inputs**: `image`, `threshold` (to control the edge softness/fuzziness).
- **Outputs**: `image_rgba` (the subject on a transparent background) and `mask` (the black and white silhouette).
- **Functionality**: Detects the background color by analyzing the image borders.

---

## ⚙️ Installation

Automatic Install: Search for `Vectorizer API` in ComfyUI Manager and click `Install`.

Manual Install:
Activate your `venv` then proceed by following these instructions:

1.  **Clone the Repository**

    Navigate to your ComfyUI `custom_nodes` directory and clone this repository:
    ```bash
    cd ComfyUI/custom_nodes/
    git clone https://github.com/rickrender/ComfyUI-Vectorizer-API.git
    ```

2.  **Install Python Dependencies**

    Install the required Python packages using the included `requirements.txt` file.
    ```bash
    cd ComfyUI-Vectorizer-API
    pip install -r requirements.txt
    ```

3.  **Install System Dependencies (for CairoSVG)**

    The `scaled_png` feature relies on the Cairo graphics library. You must install it on your system.

    - **For Debian/Ubuntu:**
      ```bash
      sudo apt-get update && sudo apt-get install libcairo2-dev pkg-config
      ```
    - For other operating systems, please consult their package manager to install the "Cairo" library.

4.  **Set Up API Credentials (Recommended)**

    Create an account at [vectorizer.ai](https://vectorizer.ai/) and get your keys from [your account page](https://vectorizer.ai/account). For convenience, create a file named `config.json` inside the `ComfyUI-Vectorizer-Pack` folder. Add your API keys to this file:
    ```json
    {
      "api_id": "YOUR_REAL_API_ID",
      "api_secret": "YOUR_REAL_API_SECRET"
    }
    ```
    The node will automatically use these credentials if the fields in the UI are left blank. You can also enter them in the UI if you wish instead.

5.  **Restart ComfyUI**

    Completely restart your ComfyUI instance. The new nodes will appear in the "Conversion" category.

---

## Dependencies

- **Python**: `requests`, `lxml`, `CairoSVG`
- **System**: `libcairo2` or equivalent

## License

This project is licensed under the MIT License.

## Acknowledgements

This node pack utilizes the powerful [Vectorizer.AI](https://vectorizer.ai/) service.
