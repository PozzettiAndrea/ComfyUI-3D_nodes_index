# 📐 Empty Latent Advanced

An advanced Empty Latent image generator for ComfyUI with visual aspect ratio presets and a smart, foldable UI. 

You can find it in right-click - Add Node - Latent - 📐 Empty Latent Advanced

<p align="center">
  <img src="./assets/preview.png" width="300" />
</p>

## Features

*   **Visual Presets:** Easy-to-read icons for aspect ratios (Portrait ▯, Square □, Landscape ▭).
*   **Ratio Lock:** When enabled in Override mode, changing Width calculates Height automatically based on the selected preset's ratio.
*   **Smart UI:** Automatically hides advanced settings when using presets to keep your workflow clean.
*   **Override Mode:** Allows custom dimensions with an optional Aspect Ratio Lock.
*   **Zero-Lag:** Optimized for performance, no unnecessary GPU formatting.

## Installation

### via ComfyUI Manager (Recommended)
1.  Search for `Empty Latent Advanced` in ComfyUI Manager.
2.  Install and Restart ComfyUI.

### Manual Installation
1.  Navigate to your ComfyUI `custom_nodes` folder.
2.  Clone this repository:
    ```bash
    git clone https://github.com/ameyukisora/ComfyUI-Empty-Latent-Advanced.git
    ```
3.  Restart ComfyUI.

## Usage

*   **Mode - Use Preset:** Select a resolution from the list. 
*   **Mode - Override:** Unlocks Width, Height, and Ratio Lock settings. 

## Credits

Created by ameyukisora.