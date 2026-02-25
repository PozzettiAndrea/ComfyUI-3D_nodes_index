<h1 align="center">
    ComfyUI-Flow-Assistor
    <br>
    <sub><sup><i>Essential utility nodes for ComfyUI</i></sup></sub>
</h1>

<p align="center">
  <img width="100%" alt="image" src="https://github.com/user-attachments/assets/c9306ce8-96b0-4535-91f7-144f2ac27840" />
</p>

<br>

# Get Started

## Install

1. Install the great [ComfyUI](https://github.com/comfyanonymous/ComfyUI).
2. Clone this repo into `custom_nodes`:
    ```bash
    cd ComfyUI/custom_nodes
    git clone https://github.com/Merserk/ComfyUI-Flow-Assistor.git
    ```
3. Start up ComfyUI.

<br>

## 🛠️ The Nodes

### 1. 📝 Prompt Queue
**Iterate through prompt lines one by one.**

Instead of randomizing a list, this node strictly follows the order of your text. It is perfect for testing specific prompt variations or storytelling sequences.

> **How it works:**  
> Paste a multi-line list of prompts. Every time you queue a generation, the node outputs the *next* line in the list.

<details>
<summary><b>🔻 Click for Parameters & Features</b></summary>

| Parameter | Description |
| :--- | :--- |
| **Prompts** | The multi-line text input. |
| **On End** | Behavior when the list finishes: `empty` (stop outputting), `repeat_last` (keep sending the last line), or `loop` (start over). |
| **Reset Trigger** | Change this integer value to force the queue back to line 1. |
| **Strip / Skip** | Automatically cleans up whitespace and ignores empty lines. |

</details>

---

### 2. 📂 Prompt Queue (From Folder)
**Batch processing made simple.**

Stop copying and pasting. Point this node to a folder on your computer, and it will read text files (`.txt`, `.json`, etc.) one by one.

> **Use Case:**  
> Great for processing wildcards, long metadata files, or batch-generating images based on a library of text descriptions stored locally.

<details>
<summary><b>🔻 Click for Parameters & Features</b></summary>

| Parameter | Description |
| :--- | :--- |
| **Folder Path** | The absolute path to your directory (e.g., `C:/Prompts`). |
| **Extensions** | Comma-separated list of file types to read (default: `txt, json`). |
| **On End** | `empty` (returns empty string), `loop` (starts at first file), `hold_last` (repeats last file). |
| **Outputs** | Returns both the **content** of the file and the **filename**. |

</details>

---

### 3. 🎥 Camera Angle Control
**Professional camera descriptions without the hassle.**

Generating specific camera angles in Stable Diffusion can be hit-or-miss. This node constructs precise camera prompts based on rotation, height, depth, and focal length.

**Three Output Modes:**
1. **Natural:** "camera rotated slightly to the right, camera raised high angle..."
2. **Technical:** "rotation 45.0°, vertical up 30.0..."
3. **Keywords:** "right side view, high angle, close-up..."

<details>
<summary><b>🔻 Click for Parameters & Features</b></summary>

*   **Rotation:** Pan the camera around the subject (Front → Side → Rear).
*   **Vertical:** Move the camera up or down (Bird's Eye → Eye Level → Worm's Eye).
*   **Depth:** Push in or pull out (Macro → Close-up → Wide Shot).
*   **Focal Length:** Simulate lens compression (24mm Wide Angle to 600mm Super Telephoto).
*   **Prefix/Suffix:** Add extra framing text easily.

</details>

---

### 4. 📐 Resolution Selector (Groups)
**Standardized resolutions with aspect ratios.**

Stop guessing pixel dimensions. This node groups resolutions by Megapixel count (0.25MP to 4MP) and provides standard aspect ratios (1:1, 16:9, 4:3, 21:9, etc.).

> **Logic:**  
> Select a resolution from the dropdown, then **Enable** the switch for that group. The switches are mutually exclusive—enabling one automatically disables the others, ensuring only one resolution group is active at a time.

<details>
<summary><b>🔻 Click for Available Resolutions</b></summary>

*   **0.25MP:** SD 1.5 style small generations.
*   **0.6MP:** Intermediate sizes.
*   **1MP (Default):** Standard SDXL / SD 1.5 Hi-Res.
*   **2MP - 4MP:** High-resolution upscaling targets.
*   **Aspect Ratios:** Covers 1:1, 4:3, 3:4, 3:2, 2:3, 16:9, 9:16, 21:9, 9:21.

</details>

---

### 5. 🖼️ Image Resolution Fit
**Resize images while keeping aspect ratio.**

Allows you to resize an input image to a specific Megapixel target (e.g., 1MP, 2MP) without distorting it. The node automatically calculates the correct width and height to preserve the original shape and rounds dimensions to multiples of 8.

> **Use Case:**  
> Perfect for Image-to-Image workflows where you want to upscale or downscale a source image to a standard generation size (like 1024x1024 total pixels) but don't want to crop or stretch it.

<details>
<summary><b>🔻 Click for Parameters & Features</b></summary>

| Parameter | Description |
| :--- | :--- |
| **Resolution Select** | Choose the target Megapixel count (0.25MP to 4MP). |
| **Logic** | Calculates `sqrt(target_pixels / current_pixels)` to scale both dimensions equally. |
| **Outputs** | Returns the resized **Image**, a matching empty **Latent**, and the new **Width/Height**. |

</details>

---

### 6. 📏 Image Resolution Extractor
**Get dimensions without resizing.**

A utility node that passes an image through unchanged but extracts its width and height. It also creates a matching empty latent.

> **Use Case:**
> Use this when you want to use an uploaded image as a reference (e.g., for ControlNet) and need an empty latent that matches its exact dimensions.

<details>
<summary><b>🔻 Click for Parameters & Features</b></summary>

| Parameter | Description |
| :--- | :--- |
| **Image** | The input image. |
| **Outputs** | Returns `Width`, `Height`, a matching `Latent`, and the original `Image`. |

</details>

---

### 7. 📏 Image Latent Resolution Extractor
**Get pixel dimensions from a Latent.**

Standard Stable Diffusion latents are compressed (1/8th scale). This node reads the latent dimensions and multiplies them by 8 to give you the effective pixel width and height.

> **Use Case:**
> Useful when you have a latent and need to know its target pixel size for downstream resizing or conditionings, without decoding it first.

---

### 8. ✖️ Multiplication (Dual & Latent)
**Mathematical scaling for custom upscaling.**

Takes two integer inputs (like Width and Height) and an optional Latent, and multiplies them by a float factor.

> **Use Case:**  
> Use this for "1.5x Upscales" or "2x Hires Fix". Connect your base width/height, set the multiplier to `1.5`, and feed the output into your latent upscaler or resize node.

<details>
<summary><b>🔻 Click for Parameters & Features</b></summary>

| Parameter | Description |
| :--- | :--- |
| **Multiplier** | The scaling factor (e.g., `1.5` or `2.0`). |
| **Inputs** | Accepts two Integers (`value_1`, `value_2`) and a `Latent`. |
| **Outputs** | Returns the multiplied integers and the bilinearly interpolated latent. |

</details>

---

### 9. 🧹 VRAM/RAM Cleaner
**Manage your resources mid-workflow.**

A "Pass-through" node that can connect to **any** input (Model, VAE, Image, etc.). It passes the data through unchanged but triggers a garbage collection and VRAM flush event when executed.

> **Modes:**  
> 1. **Current:** Unloads the specific model passing through the node.  
> 2. **Others:** Unloads everything else, keeping only the passing model in VRAM.  
> 3. **All:** Unloads everything to system RAM (clean slate).

---

### 10. 🎮 Flow Control (Sidecar Bypass)
**Toggle nodes On/Off remotely.**

A control panel that connects to up to 4 other nodes. This acts as a "Sidecar" — it does not sit in the flow of data, but rather controls the logic of the connected nodes.

> **How it works:**
> 1. Connect a node (e.g., a KSampler or ControlNet) to an `input` slot.
> 2. Toggle the switch on this node.
> 3. **Off (BYPASS):** Forces the connected node into Bypass mode (purple).
> 4. **Active:** Forces the connected node into Always/Normal mode.

---

### 11. 🔀 Any Passthrough
**Universal rerouting tools.**

Use these to clean up "spaghetti" wires or create fallback logic. These nodes accept **any** connection type (Model, Image, String, Latent, etc.).

*   **Any Passthrough (6 → 1):** Takes up to 6 inputs. Outputs the **first** one that is not null. Great for fallback defaults.
*   **Any Passthrough (1 → 6):** Takes 1 input and duplicates it to 6 outputs. Great for organizing wires from a single source.

---

### 12. ⏱️ Add Delay
**Pause execution for debugging.**

A simple node that connects to any data type, waits for a specified number of seconds, and then passes the data through unchanged. Useful for timing API calls or debugging complex flows.

---

### 13. 🐞 Debug Data (Any Input)
**Inspect your data connections.**

Not sure what shape a tensor is? Want to check the exact resolution of a latent? Connect **ANY** output to this node. It analyzes the data and displays a summary directly on the node.

> **Features:**
> *   **Images:** Displays Resolution, Aspect Ratio, Batch Size, and Channels.
> *   **Latents:** Displays Latent Shape and equivalent Pixel Resolution (8x).
> *   **General:** Displays Type, Tensor Shape, Dtype, and Device.
> *   **On-Graph Display:** Shows the data in a read-only "Matrix green" text box directly on the node itself.

---

### 14. 📺 Show Text
**Display text directly on the graph.**

Connect any string output (like the `Prompt Queue` or `Camera Angle Control`) to this node. It will display the text content inside a widget box on the node itself. Useful for verifying what is actually being sent to your CLIP encoder.

---

### 15. 🎨 CLIP Text Encode (Prompt Enrichment)
**Standard conditioning with built-in style power.**

Why copy-paste "masterpiece, best quality, 4k..." every time? This node acts exactly like the standard CLIP Text Encode but includes a dropdown with **20 curated style presets**.

> **Use Case:**
> Quickly test how your prompt looks in "Anime Style" vs "Photographic" without rewriting your text, or use utility presets like "White Background" for assets.

<details>
<summary><b>🔻 Click for Parameters & Features</b></summary>

| Parameter | Description |
| :--- | :--- |
| **Text** | Your main prompt input. |
| **Preset** | Choose from 20 styles including: *Cinematic, Digital Art, Dark Fantasy, 3D Render, Crisp/Sharp Focus, Huge Scene, White Background, etc.* |
| **Behavior** | Appends the specific style keywords to the end of your prompt and generates the Conditioning. |

</details>

---

### 16. 🖱️ Visual Marquee (Interactive)
**Pause, Select, and Refine.**

A Human-in-the-Loop tool that pauses your workflow and opens a popup editor over your generated image. You can draw a crop box to select a specific area, then resume the workflow to process just that area.

> **How it works:**
> 1. The node generates a preview and pauses the execution.
> 2. A popup appears in your browser. Draw a selection box.
> 3. Click **Confirm**. The workflow resumes, outputting the cropped image, a mask, and tile coordinates.

<details>
<summary><b>🔻 Click for Parameters & Features</b></summary>

| Parameter | Description |
| :--- | :--- |
| **Max Resolution** | If `Original Size` is disabled, the crop will be upscaled/downscaled so the longest side matches this value. |
| **Original Size** | **True:** Returns the exact pixels you selected. **False:** Resizes the selection to `Max Resolution`. |
| **Outputs** | `cropped_image`, `mask`, and `tile_data` (required for merging back later). |

</details>

---

### 17. 🧩 Tile Compositor (Merge)
**Seamlessly paste refined details back.**

The partner node to **Visual Marquee**. After you have processed/upscaled/inpainted your cropped area, this node puts it back into the original full-size image at the exact correct coordinates.

> **Features:**
> *   **Auto-Scaling:** Automatically handles size differences if you upscaled the crop in the middle of the workflow.
> *   **Feathering:** Blends the edges of the pasted tile to prevent visible seams.

---

### 18. 💎 Detail Enhancer
**Inject texture and crispness.**

A specialized node that manipulates the noise schedule (Sigmas) to force the model to generate more high-frequency detail. It works by "slowing down" the sampling process during the critical detail-formation phase and artificially inflating noise values.

> **Variants:**
> *   **Detail Enhancer (Sampler):** Wraps a sampler node.
> *   **Detail Enhancer (Sigmas):** Modifies the Sigmas connection directly.

<details>
<summary><b>🔻 Click for Parameters & Features</b></summary>

| Parameter | Description |
| :--- | :--- |
| **Enhance Factor** | Time Dilation. Slows down sampling in the active zone (e.g., `2.0` = 2x steps in zone). Adds structural detail. |
| **Texture Boost** | Sigma Inflation. Increases noise values (e.g., `0.5`). Adds sharp, gritty texture. |
| **Start / End %** | The range of the generation where the effect applies (Default `0.1` to `0.8`). |

</details>

---

### 19. ☁️ LoRA Online
**Use LoRAs directly from URLs.**

Skip the manual download process. Paste a link from Civitai, Tensor.art, or HuggingFace, and this node will download the LoRA, load it into your model, and optionally delete it after generation to save disk space.

> **Smart Integration:**
> You don't need to hunt for the direct file link. Just paste the **Civitai Model Page URL** (e.g., `https://civitai.com/models/12345/...`), and the node will automatically query the API to find the correct download file.

<details>
<summary><b>🔻 Click for Parameters & Features</b></summary>

| Parameter | Description |
| :--- | :--- |
| **URL** | The link to the LoRA (Direct link or Civitai Model Page). |
| **Strength** | Standard LoRA strength control. |
| **Save to Disk** | **True:** Keeps the file forever. **False:** Downloads, generates, then **deletes** the file to free up space. |
| **Open Folder** | A button to instantly open the download directory (`models/loras/Flow-Assistor-LoRA`) in your OS file explorer. |

</details>

<br>

## 🚀 Workflow Examples

### The "Storyteller" Batch
1. Create a text file with 10 different scenes describing a story.
2. Use **Prompt Queue** to paste them in.
3. Connect output to your CLIP Text Encode.
4. Set "Batch Count" in ComfyUI to 10.
5. Hit Queue. You get 10 images, one for each scene, in order.

### The "Cinematographer"
1. Connect **Camera Angle Control** to a text concatenator or CLIP Encode.
2. Set Output Format to `Natural`.
3. Set Focal Length to `85mm` (Portrait) and Depth to `Close-up`.
4. Resulting Prompt: *"85.0mm portrait lens with compression, camera very close, close-up"* appended to your main prompt.

### The "Smart Upscaler"
1. Connect your base `Width` and `Height` to **Multiplication (Dual)**.
2. Set Multiplier to `1.5`.
3. Connect the output `Result 1` and `Result 2` to a "Latent Upscale" node.
4. This dynamically calculates a 1.5x resolution regardless of your starting aspect ratio.

### The "Instant Style Switcher"
1. Use **CLIP Text Encode (Prompt Enrichment)** instead of the standard node.
2. Write a simple prompt: *"A cat sitting on a wall"*.
3. Select Preset: **Cyberpunk**.
4. Result: It generates *"A cat sitting on a wall, cyberpunk, neon lights, synthwave, futuristic..."*.
5. Switch Preset to **Line Art** or **White Background** to instantly change the vibe.

### The "Interactive Zoom & Enhance"
1. Feed an image into **Visual Marquee**.
2. Run flow. It pauses. Select a face or detail. Click Confirm.
3. Feed `cropped_image` into a KSampler (Img2Img) or UltimateSDUpscale to add detail.
4. Feed the Result, the Original Image, and the `tile_data` into **Tile Compositor**.
5. Result: The original image with a high-res, refined detail pasted back in seamlessly.

### The "Debugger"
1. Not sure if your latent is the right size?
2. Connect your Latent to the **Debug Data** node.
3. It instantly shows: `Latent Size: 128x128` and `Pixel Res: 1024x1024` right on the graph.

<br>

## 🤝 Contributing

If you have ideas for new flow-assisting nodes or improvements to existing ones, feel free to open an issue or submit a pull request!

## 📄 License
AGPL-3.0 License. Feel free to use this in any project, personal or commercial.