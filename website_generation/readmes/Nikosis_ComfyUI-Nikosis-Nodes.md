# ComfyUI-Nikosis-Nodes

A collection of custom nodes for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) designed to enhance your workflow with utilities for aspect ratio generation,
multi-style prompt selection, and text concatenation.

## Installation

### **Recommended**
* Install via [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager).

### **Manual**
* Navigate to `ComfyUI/custom_nodes` in your terminal (cmd).
* Clone the repository under the `custom_nodes` directory using the following command:
  ```
  git clone https://github.com/Nikosis/ComfyUI-Nikosis-Nodes comfyui-nikosis-nodes
  cd comfyui-nikosis-nodes
  ```
* Install dependencies in your Python environment.
    * For Windows Portable, run the following command inside `ComfyUI\custom_nodes\comfyui-nikosis-nodes`:
        ```
        ..\..\..\python_embeded\python.exe -m pip install -r requirements.txt
        ```
    * If using venv or conda, activate your Python environment first, then run:
        ```
        pip install -r requirements.txt
* Restart ComfyUI


# Nodes Overview

## 🖌️ Aspect Ratio (nikosis)

**File:** `nodes/aspect_ratio_nikosis.py`  
**Category:** Nikosis/Utilities  

### Description
Generates an empty latent tensor for SDXL (4 channels) or SD3/Flux (16 channels) with customizable aspect ratios and dimensions.

### Inputs
- **model_type**: Choose between SDXL (4 channels) or SD3/Flux (16 channels).
- **aspect_ratio**: Select from presets (e.g., `1:1` square `1024x1024`, `16:9` landscape `1344x768`) or custom.
- **width/height**: Custom dimensions (`64–16384`, step `8`) when using custom.
- **swap_dimensions**: Toggle to flip width and height (`Off/On`).
- **batch_size**: Number of latents to generate (`1–64`).

### Outputs
- **empty_latent**: A LATENT tensor (`batch_size x channels x height//8 x width//8`).
- **width/height**: Final dimensions as integers.

### Features
- Automatically rounds dimensions to multiples of `8`.
- Supports preset aspect ratios or custom sizes with dimension swapping.

### Example Usage
Select `SDXL`, `4:3` landscape `1152x896`, and `batch_size=2` to generate two empty latents at `1152x896` for SDXL workflows.

---

## 🖌️ Prompt Multiple Style Selector (nikosis)

**File:** `nodes/prompt_multiple_styles_selector_nikosis.py`  
**Category:** Nikosis/Text  

### Description
Combines up to four styles from a `styles.json` file into positive and negative prompts, with dropdown selection.

### Inputs
- **style1/style2/style3/style4**: Choose styles from `styles.json` (defaults to `No Style`).

### Outputs
- **positive_prompt**: Comma-separated positive prompts from selected styles.
- **negative_prompt**: Comma-separated negative prompts from selected styles.

### Configuration
- Requires a `styles.json` file in `config/` (e.g., `comfyui-nikosis-nodes/config/styles.json`).

#### Example `styles.json`
```json
{
  "Vivid": {"prompt": "bright colors, high detail", "negative_prompt": "dull, blurry"},
  "Minimal": {"prompt": "simple, clean", "negative_prompt": "cluttered"},
  
}
```
```json
{
      "||| PHOTOGRAPHY": {
        "prompt": "photography, capturing moments, storytelling, creative composition",
        "negative_prompt": "bad anatomy, comics, cropped, cross-eyed, worst quality, low quality, painting, 3D render, drawing,"
      },
}
```
- Creates `config/` directory if missing.

### Example Usage
Select `Vivid` and `Minimal` to get:
- **Positive**: `bright colors, high detail, simple, clean`
- **Negative**: `dull, blurry, cluttered`

---

## 🖌️ Text Concatenate (nikosis)

**File:** `nodes/text_concatenate_nikosis.py`  
**Category:** Nikosis/Text  

### Description
Concatenates multiple text inputs with a customizable delimiter and optional whitespace cleaning.

### Inputs
- **text_a/text_b**: Required text inputs (must be connected).
- **delimiter**: String to join texts (default: `", "`; supports `\n` for newlines).
- **clean_whitespace**: Toggle to strip extra whitespace (`true/false`).
- **text_c/text_d**: Optional additional texts.

### Outputs
- **STRING**: Concatenated result.

### Features
- Strips whitespace if `clean_whitespace` is `true`.
- Ignores empty inputs.

### Example Usage
**Inputs:**  
- `text_a="hello"`  
- `text_b="world"`  
- `delimiter=" , "`  
- `clean_whitespace="true"`  

**Output:**  
`hello , world`

---

## Usage Notes
- **Dependencies**: Works with ComfyUI’s standard setup—no extra installs needed.
- **Path**: Place in `ComfyUI/custom_nodes/comfyui-nikosis-nodes/`.
- **Testing**: Ensure your `styles.json` is correctly formatted for the style selector node.

---

## Contributing
- Feel free to submit pull requests or issues on GitHub.
- Suggestions for new nodes or improvements are welcome!

---

## License
MIT License (see `LICENSE` file).





