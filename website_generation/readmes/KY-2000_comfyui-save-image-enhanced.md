# Save Image Enhanced Node for ComfyUI

A powerful and user-friendly custom node for ComfyUI, designed to provide enhanced control over image saving. Inspired by the flexibility found in projects like [WAS Node Suite](https://github.com/WASasquatch/was-node-suite-comfyui) and the innovation of [Divergent Nodes](https://github.com/thedivergentai/divergent_nodes), this node offers advanced filename handling and output options.

## Features

*   **Flexible Filename Prefixes:** Use dynamic placeholders like `%date:yyyy-MM-dd%`, `%width%`, `%height%`, and even values from other connected nodes (e.g., `%Empty Latent Image.width%`) directly in your filename prefix. Supports `%batch_num%` for batch processing.
*   **Custom Output Folders:** Save images to a subfolder within ComfyUI's main output directory or specify an absolute path anywhere on your system.
*   **Smart Counter Suffix:** Automatically append an incrementing numerical suffix (e.g., `_00001_`) to prevent overwriting existing files. The padding (number of digits) of this counter is now fully customizable (from 1 to 9 digits).
*   **Intelligent Filename Increment (New!):** A unique `allow_overwrite` toggle allows you to automatically increment the *entire* `filename_prefix` if a file with that name exists. For example, if `000.png` exists, the next run will save as `001.png`, `002.png`, and so on, without needing to change node inputs. This works for any prefix ending in a number.
*   **Caption Saving:** Optionally save a text caption alongside each image, using a configurable file extension (default `.txt`).
*   **PNG Metadata Support:** Embed workflow metadata (prompt, extra PNG info) directly into the saved PNG files, just like the standard Save Image node.
*   **Robust Error Handling:** Includes filename sanitization to prevent OS errors and UTF-8 encoding for captions and metadata.

## Installation

1.  Navigate to your ComfyUI installation directory.
2.  Go to the `custom_nodes` folder.
3.  Clone this repository:
    ```bash
    git clone https://github.com/KY-2000/comfyui-save-image-enhanced.git
    ```
4.  Restart ComfyUI.

## Usage Tutorial

### 1. Add the Node

*   In the ComfyUI node browser, search for `Save Image Enhanced (DN)`.
*   Drag and drop the node into your workflow.

### 2. Connect Your Image

*   Connect the output of an image-generating node (like `KSampler`, `VAEDecode`, etc.) to the `images` input of this node.

### 3. Configure the Node Parameters

*   **`filename_prefix` (STRING):**
    *   This is the base name for your saved files.
    *   **Dynamic Placeholders:**
        *   `%date:yyyy-MM-dd%`: Inserts the current date (e.g., `2024-06-18`).
        *   `%date:yyyyMMdd_HHmmss%`: Inserts a detailed timestamp (e.g., `20240618_143022`).
        *   `%width%` / `%height%`: Inserts the width/height of the image.
        *   `%batch_num%`: Inserts the index of the image within the current batch (0-padded to 5 digits by default logic, but see `add_counter_suffix`).
        *   `%NodeID.InputName%`: Inserts the value of an input from another node in your workflow (e.g., `%6.width%` to get the width from node 6).
    *   **Example Prefixes:**
        *   `my_project_%date:yyyy-MM-dd%`: Saves as `my_project_2024-06-18.png`.
        *   `character_%width%x%height%_%date:yyyyMMdd_HHmmss%`: Saves as `character_512x768_20240618_143022.png`.
        *   `000`: A simple prefix to be used with the `allow_overwrite` feature (see below).

*   **`output_folder` (STRING):**
    *   Specifies where to save the images.
    *   **Relative Path:** If not an absolute path, it's treated as a subfolder of ComfyUI's main `output` directory.
        *   Example: `my_images` saves to `ComfyUI/output/my_images/`.
    *   **Absolute Path:** Save anywhere on your system.
        *   Example (Linux/macOS): `/Users/YourName/MyArtwork/`
        *   Example (Windows): `C:\\Users\\YourName\\MyArtwork\\`
    *   **Empty String (`""`):** Saves directly to ComfyUI's main `output` directory.

*   **`add_counter_suffix` (BOOLEAN):**
    *   **`True` (Default):** Appends a counter to the filename to prevent overwrites. The counter value is determined by ComfyUI's standard logic, which looks for an existing counter at the *end* of the `filename_prefix`.
        *   **Example:** If `filename_prefix` is `image` and `image.png` doesn't exist, it saves as `image.png`. If `image.png` exists, it saves as `image_00001.png`. If `image_00001.png` exists, it saves as `image_00002.png`.
        *   **Important:** If your `filename_prefix` *ends* with a number (e.g., `image_000`), that number is treated as the starting counter. So if `image_000.png` doesn't exist, it will save as `image_001.png`.
    *   **`False`:** Does not add a counter suffix. If a file with the exact name exists, it will be overwritten (unless `allow_overwrite=False`).

*   **`counter_padding` (INT):**
    *   Controls the number of digits (1-9) used for the counter suffix added by `add_counter_suffix`.
    *   **Default:** `5` (produces `_00001_`, `_00002_`, etc.).
    *   **Example (`counter_padding=3`):** Produces `_001_`, `_002_`, etc.
    *   **Example (`counter_padding=6`):** Produces `_000001_`, `_000002_`, etc.

*   **`allow_overwrite` (BOOLEAN):**
    *   **`False` (Default):** Enables the *Intelligent Filename Increment* feature.
        *   Instead of just adding a counter suffix, this feature automatically increments the *entire* `filename_prefix` if a file with that name already exists.
        *   It works by checking if the file constructed from `filename_prefix` exists. If it does, it tries to find the next available number by parsing the end of the `filename_prefix`.
        *   **How to Use:** Set your `filename_prefix` to a simple incrementing pattern like `000`, `img001`, or `MyArt_10`. Set `add_counter_suffix=False`. Each time you run the node with the *exact same inputs*, it will save `000.png`, then `001.png`, then `002.png`, etc. You don't need to manually change the prefix or toggle `add_counter_suffix` to make it increment. This is particularly useful for sequential generation workflows.
        *   **Note:** For this feature, `add_counter_suffix` should typically be `False` to avoid conflicting counter logic.
    *   **`True`:** Disables the *Intelligent Filename Increment*. The node behaves like a standard ComfyUI Save Image node with the added `counter_padding` option.

*   **`caption` (STRING - Optional Input):**
    *   Connect a text string here to save it as a separate caption file.
    *   Useful for saving prompts or descriptions alongside images.

*   **`caption_file_extension` (STRING - Optional):**
    *   Sets the file extension for the caption file.
    *   **Default:** `.txt`

### 4. Run Your Workflow

*   Queue and run your workflow.
*   The node will save your images according to the configured settings.

## Example Workflows

### Basic Save with Date
1.  Use `filename_prefix`: `MyArt_%date:yyyy-MM-dd%_%batch_num%`
2.  Use `output_folder`: `generated_images`
3.  This saves files like `ComfyUI/output/generated_images/MyArt_2024-06-18_00001.png`.

### Sequential Naming with Intelligent Increment
1.  Use `filename_prefix`: `000`
2.  Use `output_folder`: `sequential_runs`
3.  Set `add_counter_suffix`: `False`
4.  Set `allow_overwrite`: `False`
5.  Run the workflow multiple times. Files will be saved as `ComfyUI/output/sequential_runs/000.png`, `001.png`, `002.png`, etc.

### Custom Counter Padding
1.  Use `filename_prefix`: `test_image`
2.  Set `add_counter_suffix`: `True`
3.  Set `counter_padding`: `3`
4.  Files will be saved as `test_image_001.png`, `test_image_002.png`, etc.

## Acknowledgements

This node takes inspiration from the excellent work done by the creators of [WAS Node Suite](https://github.com/WASasquatch/was-node-suite-comfyui) and [Divergent Nodes](https://github.com/thedivergentai/divergent_nodes). Their contributions to the ComfyUI community have been invaluable.