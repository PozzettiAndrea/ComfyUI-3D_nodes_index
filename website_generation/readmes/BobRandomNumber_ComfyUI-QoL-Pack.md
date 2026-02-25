# ComfyUI Quality of Life Pack

Some optimized enhancements originally from [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts) by `pythongosssss`. This pack aims to incorporate updated enhancments without adding unnecessary features.

---

## Features

This package provides two key quality-of-life improvements:

### 1. Collapsible Nested Menus

Tired of scrolling through endless lists of checkpoints, LoRAs, or VAEs? This feature automatically organizes your model dropdowns into a clean, collapsible tree structure based on your folder layout.

-   Organizes long lists into a nested, foldable hierarchy.
-   Supports subfolder navigation directly in the menu.
-   Makes finding the right model quick and easy, especially for large collections.

### 2. Save Workflow as PNG

Adds a simple, one-click option to the canvas context menu to save your entire workflow as a single PNG image. The workflow data is embedded directly into the PNG file, making it easy to share, store, and reload your work.

-   Adds a `Save Workflow as PNG` option to the right-click menu on the canvas.
-   Embeds the full graph and node data into the image file.
-   Drag-and-drop the saved PNG back onto your ComfyUI canvas to instantly load the workflow.

## Screenshots

**Nested Menus in Action:**


https://github.com/user-attachments/assets/7929050c-b845-411d-a5a9-f029957cfe99



**Save Workflow Option:**

<img width="295" height="250" alt="menu" src="https://github.com/user-attachments/assets/6b9dbba7-0328-46e4-9382-76708b4c08e7" />

## Installation

1.  Navigate to your ComfyUI `custom_nodes` directory.

    ```bash
    cd ComfyUI/custom_nodes/
    ```
3.  Clone this repository into the `custom_nodes` folder.

    ```bash
    git clone https://github.com/BobRandomNumber/ComfyUI-QoL-Pack.git
    ```
5.  Restart ComfyUI.

## ⚠️ Important: Conflicts

This package contains modified versions of scripts found in `ComfyUI-Custom-Scripts` by `pythongosssss`.

**You should not have this pack and the original `ComfyUI-Custom-Scripts` installed at the same time**, as they may conflict and cause issues with your menus.

Please choose one pack or the other. This `QoL-Pack` was created to provide a stable, minimal alternative.

## Credits and Attribution

This package is based on work done by the original author. The features included here are based on a slimmed-down, refactored version of, scripts from the following repository:

-   **Original Project:** [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts)
-   **Original Author:** `pythongosssss`

Specifically, this pack modifies and builds upon:
-   `betterCombos.js`
-   `workflowImage.js`

Full credit goes to `pythongosssss` for creating these excellent utilities for the ComfyUI community.
