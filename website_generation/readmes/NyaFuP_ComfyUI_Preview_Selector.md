# NF Preview Selector

A floating dialog-based image preview and selection system for ComfyUI.

日本語版READMEは[こちら](README-ja.md)です。

## Intended Use
1. Generate images in a batch.
2. Select your favorite results.
3. Process them with Hires fixes or other enhancements.

## Features

- **Floating Dialog Interface**: Non-intrusive dialog window
- **Drag & Drop Positioning**: Move the review window anywhere on screen
- **Multi-Selection**: Click images to select/deselect multiple images
- **Timeout Support**: Configurable timeout with visual countdown
- **Multiple Modes**: Review mode, pass-through, take first/last
- **Latent Support**: Optional latent passthrough for efficiency
- **Memory**: Window position and settings are remembered

## New Features in v1.2.5
- **Double-Click Image Expansion**: Full-screen image viewing with advanced zoom and pan capabilities
---

## Usage

1. Add the "NF Preview Selector" node to your workflow
2. Connect image input (and optionally latent input)
3. Choose a mode:
   - **review_and_select**: Opens floating dialog for manual selection
   - **pass_through**: Passes all images without review
   - **take_first**: Automatically selects first image
   - **take_last**: Automatically selects last image
4. Set timeout value (10-300 seconds)

  <img width="284" height="517" alt="Main node" src="https://github.com/user-attachments/assets/0509c1d4-bb15-4f46-b924-383fd63981cb" />

## Dialog Interface

When in review mode, a floating dialog will appear showing:
- Grid of images to review
- Click images to select/deselect (green number mark indicates selection)
- Selection counter
- Countdown timer
- Confirm/Cancel buttons
- Pin button to keep the floating dialog open(v1.2.0)

  <img width="316" height="528" alt="Dialog Interface" src="https://github.com/user-attachments/assets/e2bc576e-5e66-4735-beb0-2742a8a0d419" />

## Settings

Access via ComfyUI Settings menu:
- **Dialog maximum width**: Determines the maximum width of the dialog in pixels. (Max 1800px)
- **Remember window position**: Saves dialog position between uses

<img width="544" height="121" alt="Settings" src="https://github.com/user-attachments/assets/105277be-b16d-4d66-b683-9617f097a201" />

## Outputs

- **selected_images**: IMAGE batch of selected images
- **selected_latents**: LATENT batch of corresponding latents (if input provided)
- **selection_indices**: STRING of selected indices (e.g., "0,2,4")

## Installation

1. It can be installed from ComfyUI Manager. Or git clone this repo.
2. Restart ComfyUI
3. The "NF Preview Selector" node will appear in the "image/review" category

## Known Issues
- When this custom node is waiting for user input, the previewed image will not be saved if you select "Cancel" or if it times out. Currently, implementing a fix for this is beyond my abilities, so it will remain as is until I can get some hints on how to improve it.

## Please Note

- I created this custom node because I needed it for my own use. I am a beginner at coding and developed it with the assistance of Claude Code. Therefore, I am unable to provide detailed support even if there are issues with this custom node.

## Credits

This custom node was implemented with reference to [cg-image-filter](https://github.com/chrisgoringe/cg-image-filter).
