# ComfyUI Burve Tools

A collection of custom nodes for ComfyUI, focusing on integration with Google's Gemini AI models for image generation and more.

## Nodes

### 1. Burve Google Image Gen
This is the main node for generating images using Google's Gemini models.

*   **Functionality**: Generates images based on text prompts, with support for system instructions and reference images.
*   **Inputs**:
    *   `prompt`: The description of the image you want to generate.
    *   `model`: Select between `gemini-3-pro-image-preview` and `gemini-2.5-flash-image`.
    *   `resolution`: Output resolution (1K, 2K, 4K).
    *   `aspect_ratio`: Desired aspect ratio (e.g., 1:1, 16:9, 9:16).
    *   `seed`: Seed for reproducibility.
    *   `enable_google_search`: If enabled, allows the model to use Google Search grounding (if supported by the model/API).
    *   `system_instructions` (Optional): Advanced instructions to guide the model's behavior.
    *   `reference_images` (Optional): A list of images to use as context/reference for the generation. Use the **Burve Image Ref Pack** node to create this list.
*   **Outputs**:
    *   `image`: The generated image(s).
    *   `thinking_process`: The text output from the model, which may include reasoning or descriptions.
    *   `system_messages`: Error messages or status updates (e.g., if the API key is missing).

### 2. Burve Image Ref Pack
A utility node to bundle multiple images into a single list for the generator node.

*   **Functionality**: Accepts up to 14 individual image inputs and packages them into a format compatible with the `reference_images` input of the **Burve Google Image Gen** node.
*   **Inputs**: `image1` through `image14` (optional).
*   **Outputs**: `images` (A list of images).

### 3. Burve Debug Gemini Key
A helper node to verify your API key configuration.

*   **Functionality**: Checks if the `GEMINI_API_KEY` environment variable is correctly set and visible to ComfyUI. It displays the status and a masked version of the key.
*   **Outputs**: `info` (Status message).

### 4. Burve System Instructions
Selects pre-defined system instructions from a dropdown menu.

*   **Functionality**: Loads system instructions from a JSON file (which auto-updates from GitHub) and outputs the selected instruction text.
*   **Inputs**:
    *   `instruction_name`: Select a system instruction preset.
*   **Outputs**:
    *   `instruction`: The full text of the selected system instruction.

### 5. Burve Variable Injector
Defines variables for use in dynamic prompts.

*   **Functionality**: A utility node to create a dictionary of variable values. Accepts up to 14 string inputs.
*   **Inputs**:
    *   `V1` through `V14` (Optional): String values for variables.
*   **Outputs**:
    *   `variables`: A dictionary of the provided variables.

### 6. Burve Prompt Database
Loads prompts from a database and injects variables.

*   **Functionality**: Selects a prompt from a JSON database (auto-updating) and replaces placeholders (e.g., `[[name:default]]`) with values from the **Burve Variable Injector**.
*   **Inputs**:
    *   `prompt_name`: Select a prompt from the database.
    *   `variables` (Optional): A dictionary of variables from the **Burve Variable Injector** node.
*   **Outputs**:
    *   `compiled_prompt`: The prompt with variables injected.
    *   `raw_prompt`: The original prompt with placeholders.
    *   `title`: The title of the selected prompt.


### 7. Burve Blind Grid Splitter
Splits an image into a grid of tiles without content analysis.

*   **Functionality**: Slices an input image into a specified number of rows and columns. Useful for processing large images in chunks.
*   **Inputs**:
    *   `image`: The input image to split.
    *   `rows`: Number of horizontal slices (default: 2).
    *   `cols`: Number of vertical slices (default: 2).
    *   `center_crop`: If enabled, centers the grid on the image if dimensions aren't perfectly divisible, otherwise starts from top-left.
*   **Outputs**:
    *   `tiles`: A batch of images containing the resulting grid tiles.

## Installation

1.  Clone this repository into your ComfyUI `custom_nodes` directory:
    ```bash
    cd ComfyUI/custom_nodes
    git clone https://github.com/Burve/ComfyUI_Burve_Tools.git
    ```
2.  Install the required dependencies:
    ```bash
    cd ComfyUI_Burve_Tools
    pip install -r requirements.txt
    ```
    (Note: You may need to use the `pip` associated with your ComfyUI python environment, e.g., `python_embeded/python.exe -m pip install ...` if using the portable version).

## Google API Key Setup

This project requires a Google Gemini API key. You must set it as an environment variable named `GEMINI_API_KEY`.

### How to get an API Key
1.  Go to [Google AI Studio](https://aistudio.google.com/).
2.  Create a new API key.

### Setting the Environment Variable

**Windows (PowerShell):**
Run the following command in PowerShell:
```powershell
setx GEMINI_API_KEY "YOUR_REAL_KEY_HERE"
```
*After running this, you must close and restart your terminal and ComfyUI for the change to take effect.*

**macOS / Linux:**
Add the export command to your shell configuration file (e.g., `~/.bashrc` or `~/.zshrc`):
```bash
export GEMINI_API_KEY="YOUR_REAL_KEY_HERE"
```
Then run `source ~/.bashrc` (or `.zshrc`) and restart ComfyUI.

### Troubleshooting
If the **Burve Google Image Gen** node reports that the API key is missing, use the **Burve Debug Gemini Key** node to inspect what ComfyUI is seeing. If it shows "GEMINI_API_KEY is NOT set", double-check your environment variable setup and ensure you have restarted the application.
