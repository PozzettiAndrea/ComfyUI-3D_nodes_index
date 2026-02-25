# Seb Nodes for ComfyUI

A powerful suite of utility nodes for ComfyUI by Seb (cyberhirsch), designed to streamline your creative process from initial setup to final output. This collection features four essential nodes: **Aspect Ratio** for perfect image sizing, **Unified Prompter** for modular prompt building, **Switch Mask** for dynamic mask selection, and **Save Image** for advanced file organization.

---

## 📋 Table of Contents

- [🚀 Installation](#-installation)
- [📦 The Nodes](#-the-nodes)
  - [1. Aspect Ratio (Seb)](#1-aspect-ratio-seb)
  - [2. Unified Prompter (Seb)](#2-unified-prompter-seb)
  - [3. Switch Mask (Seb)](#3-switch-mask-seb)
  - [4. Save Image (Seb)](#4-save-image-seb)
- [📄 License](#-license)

---

## 🚀 Installation

### Recommended: Using ComfyUI-Manager

1.  Install the [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager) if you haven't already.
2.  In your ComfyUI interface, click the **Manager** button.
3.  Click **Install Custom Nodes**.
4.  Search for `Seb`.
5.  Click the **Install** button next to the package.
6.  **Restart ComfyUI** completely.

### Manual Installation

1.  Navigate to your ComfyUI installation directory.
2.  Enter the `custom_nodes` subfolder (e.g., `ComfyUI/custom_nodes/`).
3.  Open a terminal or command prompt in this directory.
4.  Clone the repository:
    ```bash
    git clone https://github.com/cyberhirsch/seb_nodes.git
    ```
5.  **Restart ComfyUI** completely.

---

## 📦 The Nodes

This collection is designed to work together seamlessly, solving common workflow challenges with elegant and powerful solutions.

### 1. Aspect Ratio (Seb)
**(Category: `utils/aspect_ratio`)**

Stop guessing image dimensions. This node intelligently calculates `width` and `height` for you, ensuring your generations are perfectly sized and compatible with your models.

<img src="screenshots/Aspect%20Ratio.png" alt="Screenshot of the Aspect Ratio (Seb) node" width="427">

#### Key Features
*   **Preset Library**: A logically sorted list of common aspect ratios, from tall portrait (`9:16`) to cinematic widescreen (`21:9`).
*   **Intelligent Sizing Modes**:
    *   **Megapixels**: Set a target image complexity (e.g., `1.0` for a ~1MP image) and let the node handle the math across different shapes.
    *   **Fixed Side**: Lock in a specific width or height, and the node calculates the other dimension to match your chosen ratio.
*   **Dynamic UI**: The interface smartly hides irrelevant options, reducing clutter.
*   **Model-Safe Output**: A `multiple_of` setting ensures your final dimensions are divisible by a required number (e.g., 8) to prevent model errors.

> **Pro-Tip:** Use the **Megapixels** mode when experimenting with different aspect ratios. It keeps your VRAM usage and generation time consistent, allowing for a fair comparison between compositions.

### 2. Unified Prompter (Seb)
**(Category: `utils/prompting`)**

Build complex, high-quality prompts with an organized, modular system. This node replaces dozens of text boxes with a clean, dropdown-based interface powered by a simple, external JSON file.

<img src="screenshots/Unified%20Prompter.png" alt="Screenshot of the Unified Prompter (Seb) node" width="591">

#### Key Features
*   **External JSON Stylesheet**: All dropdown options are loaded from `unified_prompter_styles.json`. Add, edit, and share entire prompt libraries without touching any code.
*   **Categorized Modifiers**: Organize prompt fragments into logical groups like `technique`, `composition`, `lighting`, and `artist`.
*   **Creative Roulette**: Every positive prompt category includes a **"Random"** option. Let the node surprise you with new style combinations to break creative blocks.
*   **Multi-Layered Negatives**: Stack up to three negative prompt presets (e.g., a base negative, a model-specific one, and an aesthetic filter) for fine-tuned control.
*   **Transparent Output**: Outputs the final text prompts as strings, so you can preview exactly what's being sent to the sampler.

> **Pro-Tip:** Create different style files for different themes (e.g., `scifi_styles.json`, `fantasy_styles.json`). Before starting ComfyUI, just rename the one you want to use to `unified_prompter_styles.json`.

### 3. Switch Mask (Seb)
**(Category: `mask/util/Seb`)**

Automate your masking process for any image shape. This node receives an image and selects the most appropriate mask from a set of eight aspect-ratio-specific inputs.

<img src="screenshots/Switch%20Mask.png" alt="Screenshot of the Switch Mask (Seb) node" width="301">

#### Key Features
*   **Dynamic Mask Selection**: Automatically detects the incoming image's aspect ratio and outputs the mask from the corresponding input slot.
*   **Failsafe Design**: If no mask is connected to the best-matching input, the node outputs nothing, preventing errors in your workflow.
*   **Clear Feedback**: Outputs a text label of the detected aspect ratio (e.g., "16:9") for easy verification.

> **Example Workflow:** Combine this with a 'Vignette' or 'Blur' node. Create masks for 16:9, 1:1, and 9:16, and connect them to the respective inputs. This node will now automatically apply the correct vignette to any image, making your post-processing workflow universal.

### 4. Save Image (Seb)
**(Category: `image/save`)**

Take full control of your file organization and naming. This node is a super-powered replacement for the default save functionality.

<img src="screenshots/Save%20Image.png" alt="Screenshot of the Save Image (Seb) node" width="498">

#### Key Features
*   **Granular File Naming**: Construct filenames with a core component, a separator, an optional timestamp, and an automatic batch counter.
*   **Dynamic Folder Sorting**: Use date and time patterns (e.g., `%date:yyyy-MM-dd%`) to automatically sort your images into a clean folder structure.
*   **Instant Access Button**: Includes an **"Open Last Output Folder"** button directly on the node to immediately navigate to where your files were saved.
*   **Metadata Control**: Choose whether to embed the full ComfyUI workflow into the saved PNG file.

> **Pro-Tip:** The `filename_core` input can be connected to the output of other nodes. For example, connect the `seed` number from a "Primitive" node to include the seed directly in every filename.

---

## 📄 License

This project is licensed under the **MIT License**.
