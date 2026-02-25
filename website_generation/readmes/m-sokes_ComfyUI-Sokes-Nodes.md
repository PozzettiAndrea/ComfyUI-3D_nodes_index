ComfyUI Sokes Nodes 🦬
=======
A small node suite for ComfyUI featuring the following nodes:

| Node | Description |
| --- | --- |
| **Current Date & Time** | Add the current date and or time to the filename with custom formatting. E.g. YYYY-MM-DD<br /><h6>Tip: Also supports python formated date & time properties</h6> |
| **Empty Latent Selector (9 Inputs)** | Useful for generating a random latent dimentions based on a fixed set |
| **Get Files in Folder with Extension** | Gets a list of files with a specific extension from a given folder |
| **Hex to Color Name** | Convert hex to descriptive color names for image-generation prompts |
| **Load Random Image** | Load a random image(s) and output optional alpha channel and reference image path(s)<br /><h6>Tip: You can use wildcards "*" and or "\|"'s in the folder path input</h6> |
| **Random Number** | A user friendly random number generator that supports int, float, and bool |
| **Replace Text with RegEx** | Useful for using RegEx for text replacement |
| **Runpod Serverless** | Call a Runpod serverless endpoint (text or image+text). Outputs: response_text, full_response, status, execution_time.<br /><h6>Tip: Set RUNPOD_API_KEY env var</h6> |
| **Street View Loader** | Loads Google Street View images based on address or lat/lon. Outputs an image.<br /><h6>Tip: Set GOOGLE_STREET_VIEW_API_KEY env var</h6> |


---

### Instalation

To install nodes follow these steps:

**Via ComfyUI Manager**
1. Open ComfyUI Manager
2. Open Custom Nodes Manager
3. Search for ```ComfyUI Sokes Nodes```
4. Click Install


**Manually**
1. Open a terminal or a command line interface.
2. Navigate to the ComfyUI/custom_nodes/ directory.
3. Run the following command: ```git clone https://github.com/m-sokes/ComfyUI-Sokes-Nodes.git```
4. Activate your environment (assuming there is one)
5. ```pip install -r requirements.txt```
6. Restart ComfyUI.

---

### What is ComfyUI?

[ComfyUI](https://github.com/comfyanonymous/ComfyUI) is a node based interface and backend for all things AI related, including image, video, audio, and text generation.

*Recommended ComfyUI extension: [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)*

---

### Runpod Serverless node

- **Requirements**: Set environment variable `RUNPOD_API_KEY`.
- Note: For vision models, connect an `IMAGE` input; for text-only, leave it unconnected.

### Street View Loader node

- **Requirements**: Set environment variable `GOOGLE_STREET_VIEW_API_KEY`.

---

### Why a bison 🦬 emoji?

There's no offical musk ox emoji...I'll reached out to the Unicode Consortium.

---

### Future Node Concepts
- [ ] Prompt Styler node with custom categories based on json file(s)
- [ ] Palette-to-Prompt Builder

### Get Files in Folder By Extension Node

- **Inputs**: `folder_path` (string), `file_extension` (string).
- **Outputs**: `file_list` (list of strings).
- **Note**: The `file_extension` input can be provided with or without a leading dot (e.g., "mp3" or ".mp3"). The output list of files will be sorted alphabetically.

### Hex to Color Name Node

- **Inputs**: `hex_color` (string, comma-separated hex codes), `use_css_name` (boolean).
