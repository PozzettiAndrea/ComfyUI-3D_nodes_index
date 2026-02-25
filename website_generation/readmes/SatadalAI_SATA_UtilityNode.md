# SATA Utility Node Suite for ComfyUI

**Author:** Satadal  
**Version:** 1.5.0  
**License:** MIT  
**Repository:** https://github.com/SatadalAI/SATA_UtilityNode

---

## 🚀 Overview

SATA Utility Node Suite is a collection of custom nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) designed to enhance your image processing and workflow experience.  
It includes:

- **Upscale Machine:** High-quality model-based image upscaling with aspect-ratio preserving rescale.
- **Prompt Machine:** Easy prompt selection from a CSV for positive/negative prompt workflows.
- **Touchpad Pan & Zoom:** Seamless navigation for large images in the ComfyUI preview panel.
- **Resolution Machine:** Quick selection of model-specific image resolutions for popular models.
- **Save Image w/Metadata:** saving images with meta data and with different file formats.
- **Prompt Autocomplete:** Text widget with autocompletion, random selection, and preview capabilities.
- **Latent Machine:** Advanced noise generation for creating empty latents initialized with specific noise patterns instead of standard Gaussian noise.
- **Preview Machine:** Privacy-focused image preview node with auto-hide and hover-to-reveal functionality.

---

## 🧩 Node Features

### 🖼️ Upscale Machine

- **Model-based Upscaling:** Uses custom or pre-trained models from the `upscale_models` folder.
- **Aspect Ratio Preserving Rescale:** Output size is always original size × rescale factor.
- **CPU-based Rescaling:** Efficient resizing using OpenCV.
- **Supersampling:** Optional detail preservation for downscaling/fractional resizing.
- **Rounding Modulus:** Ensures output dimensions align with model/UI constraints.

### 💬 Prompt Machine

- **CSV-based Prompt Selection:** Select prompt sets from a CSV file (`prompts.csv`).
- **Positive/Negative Output:** Outputs both positive and negative prompts as strings.
- **Easy Integration:** Designed for use in prompt-driven workflows.

### 🖱️ Touchpad Pan & Zoom

- **Preview Navigation:** Enables smooth pan and zoom for large images in the ComfyUI preview panel.
- **User Experience:** Makes inspecting high-res outputs fast and intuitive.

### 📏 Resolution Machine

- **Model-aware Resolution Selection:** Choose from a list of recommended resolutions for each supported model.
- **Auto-populate Width/Height:** Selecting a resolution automatically fills in the correct width and height.
- **Manual Override:** You can manually set width/height, which clears the preset selection.
- **Supports Many Models:** Includes presets for SD1.5, SDXL, Illustrious XL, Pony XL, Flux.1 Dev, Qwen-Image, Wan2.2-S2V, SD3.5 Large, Lumina-Image 2.0, and more.
- **UI Integration:** Intuitive dropdowns for model and resolution selection in the ComfyUI interface.

---

### 💾 Save Image w/Metadata

- **Single path+filename input:** Provide a single required `path_and_filename` string (examples: `comfy`, `Test/comfy`, `SDXL/Test/comfy`). The last path segment is used as the filename; preceding segments become folders under the ComfyUI output directory.
- **Supported formats:** PNG, JPEG (saved as .jpg), WEBP (choose with the `extension` dropdown).
- **Automatic folder creation:** Any missing folders in the provided path are created automatically.
- **Metadata embedding:** PNG files receive tEXt entries (parameters/prompt). JPEG/WEBP receive EXIF UserComment where possible.
- **Placeholder resolution:** Filenames and paths accept `%...%` placeholders which are resolved from the node's `prompt` dictionary (best-effort). Example: if `prompt` contains `{"title": "MyTitle"}`, using `%title%/img` will save under `MyTitle/img.png`.
- **Collision-safe saving:** If a file already exists the node will append `_0001`, `_0002`, ... to the base filename to avoid overwriting.

### ✍️ Prompt Autocomplete

- **Autocompletion:** Type `#` (configurable) to trigger a popup with suggestions from CSV/JSON files in the `prompt` folder.
- **Random Selection:** Select `🎲 Random` to insert a random item from a category.
- **Preview:** View full text of long snippets before inserting.
- **Global Mode:** Optional setting to enable autocompletion on ALL text widgets in ComfyUI.
- **Custom Data:** Add your own `.csv` or `.json` files to the `prompt` folder to extend the library.

### 🌌 Latent Machine

- **Advanced Noise Generation:** Create empty latents initialized with specific noise patterns instead of standard Gaussian noise.
- **Noise Types:**
    - **Gaussian (White):** Standard noise, good for sharp details.
    - **Pink (1/f):** Balanced noise, great for photorealism and nature.
    - **Brown (1/f²):** Smoother noise, ideal for backgrounds and anime.
    - **Perlin:** Cloud-like structure, perfect for landscapes and fluids.
    - **Plasma:** Very smooth, abstract blobs for sci-fi and alien terrains.
- **Model Support:** Select between **4-channel** (SD1.5, SDXL, etc.) and **16-channel** (Flux, SD3) latents.
- **Reproducibility:** Full seed support for consistent noise generation.

### 👁️ Preview Machine

- **Privacy-Focused Preview:** Image preview node that hides content by default.
- **Hover to Reveal:** Simply hover over the node to temporarily reveal the image.
- **Auto-Hide:** Image automatically hides again when you move the mouse away.
- **Global Hide Mode:** Optional setting to hide ALL preview nodes in the workflow (Settings → SATA Utility: Global Hide Previews).
- **Save Machine Integration:** The Save Machine node also includes a `hide_preview` toggle (default: hidden) with the same hover-to-reveal behavior.


## 📦 Installation

1. Clone or download this repository into your ComfyUI `custom_nodes` directory:

   ```sh
   git clone https://github.com/SatadalAI/SATA_UtilityNode.git
   ```

2. (Optional) Install dependencies if not already present:

   ```sh
   pip install -r requirements.txt
   ```

3. Restart ComfyUI.

---

**Settings:**
- **Trigger Character:** Change the character that opens the popup (default: `#`).
- **Global Mode:** Enable autocompletion for all text widgets in ComfyUI (default: `false`).

## 📝 License

MIT License

---

## 🔗 Links

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)