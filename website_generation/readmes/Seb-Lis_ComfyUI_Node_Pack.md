# Custom Nodes for ComfyUI

A collection of utility nodes for image processing, workflow management, and generation metadata tracking.

## Installation

1. Navigate to your ComfyUI `custom_nodes` directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. Clone this repository (or copy the folder `seb-nodes-comfyui`):
   ```bash
   git clone https://github.com/yourusername/seb-nodes-comfyui.git
   ```
3. Restart ComfyUI.
### 1. KSampler Bridge to Text (SEB)
**Category:** `sampling/control`

Master Controller for KSampler. Captures parameters and start time, formats them for text overlay.

*   **Inputs:**
    *   `latent`: The latent image.
    *   `seed`: Random seed.
    *   `steps`: Number of steps.
    *   `cfg`: Classifier Free Guidance scale.
    *   `sampler_name`: Sampler selection.
    *   `scheduler`: Scheduler selection.
*   **Outputs:**
    *   `text_overlay`: Formatted string with generation info.
    *   `latent`, `seed`, `steps`, `cfg`, `sampler_name`, `scheduler`: Passthrough values.
    *   `start_time`: Timestamp for generation time calculation.
*   **How to Connect:**
    *   Connect the outputs of this node (Seed, Steps, etc.) to your actual **KSampler** node.
    *   Connect `text_overlay` and `start_time` to the **Generation Time** node (optional).

### 2. Generation Time (SEB)
**Category:** `sampling/control`

Calculates the total generation time and appends it to your text overlay.

*   **Inputs:**
    *   `image`: The generated image (from VAE Decode).
    *   `text`: The `text_overlay` output from the **KSampler Bridge** node.
    *   `start_time`: The `start_time` output from the **KSampler Bridge** node.
*   **Outputs:**
    *   `image`: Passthrough of the input image.
    *   `text`: Updated text string including "Time: X.XXs".
*   **How to Connect:** Place this after your VAE Decode. Connect the image and the data from the Bridge node.

### 3. Text Label (SEB)
Adds customizable text labels to images with transparent backgrounds and alignment options.

*   **Inputs:**
    *   `image`: The input image(s).
    *   `text`: The text to display (multiline supported).
    *   `font_family`: Font selection (includes custom fonts like Funnel Sans, Google Sans Code).
    *   `font_size`: Size of the text.
    *   `text_align`: Horizontal alignment (left, center, right).
    *   `placement`: Position of the label (top_left, center, etc.).
    *   `edge_offset`: Distance from the edge.
    *   `color_scheme`: Preset colors (white_on_black, black_on_white).
    *   `padding`: Padding around the text.
    *   `corner_radius`: Radius of the background box corners.
    *   `stroke_width`: Width of the text stroke/outline.
    *   `background_opacity`: Opacity of the background box (0-255).
*   **Outputs:**
    *   `image`: The image with the text label applied.

### 4. Image Grid (SEB)
Arranges multiple image batches into a customizable grid layout.

*   **Inputs:**
    *   `columns`: Number of columns in the grid.
    *   `padding`: Padding between images in pixels.
    *   `image_1`...`image_6`: Optional image inputs.
*   **Outputs:**
    *   `image`: A single grid image containing all inputs.
*   **Usage:** Useful for comparing results or creating contact sheets.

---

## Example Workflow

1.  **KSampler Bridge** -> (Pass parameters) -> **KSampler** -> **VAE Decode** -> **Generation Time** (Input Image).
2.  **KSampler Bridge** -> (Pass `text_overlay` + `start_time`) -> **Generation Time**.
3.  **Generation Time** -> (Pass `image` + `text`) -> **Text Label**.
4.  **Text Label** -> **Save Image**.
