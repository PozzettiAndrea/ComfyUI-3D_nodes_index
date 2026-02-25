# Comfy Contact Sheet Image Loader

A custom ComfyUI node that displays up to 64 recent images from a folder as numbered thumbnails in a flexible grid contact sheet format, allowing you to easily select and load one of them for post-processing.

## Screenshot

![image](https://github.com/user-attachments/assets/21de481d-236e-4149-8650-948f8e2051b5)

## Features

- **Visual Selection**: Shows up to 64 numbered thumbnails of the most recent images in a folder
- **Flexible Grid Layout**: Choose 1-8 rows (8, 16, 24, 32, 40, 48, 56, or 64 images)
- **Numbered Thumbnails**: Each thumbnail displays a number (1-64) for easy identification and loading via the selector
- **Automatic Sorting**: Images are automatically sorted by modification time (newest first)
- **Smart Refresh**: Updates automatically when connected load_trigger changes
- **Default Output Folder**: Automatically defaults to ComfyUI's output directory, but you can change it
- **Efficient Caching**: Thumbnails are cached for better performance
- **Multiple Formats**: Supports JPG, JPEG, PNG, BMP, TIFF, and WEBP images

## Installation

- **Recommended:** Use ComfyUI Manager's "Install via Git URL" feature and enter:
  ```
  https://github.com/benstaniford/comfy-contact-sheet-image-loader.git
  ```
### Or for manual installation: 

1. Copy this folder to your ComfyUI `custom_nodes` directory
2. Restart ComfyUI
3. Add the "Contact Sheet Image Loader" node to your workflow
4. Attach a load_trigger from some point in your work flow to auto refresh the contact sheet
5. Attach a Preview Image node to view the contact sheet
6. Set the folder path (or accept comfy's output folder as default) and start browsing your images!
7. Connect the output image/mask nodes and use the numbered images on the contact sheet to load and post-process your gens

## Node Parameters

- **folder_path**: Path to folder containing your images (defaults to ComfyUI output folder)
- **load_trigger**: Connect any output here to refresh thumbnails (required)
- **selected_image**: Which image to load (1-64, based on numbered thumbnails)
- **thumbnail_size**: Size of thumbnails in pixels (64-512, default 256)
- **rows**: Number of rows in contact sheet (1-8, determines total images shown)

## Outputs

- **contact_sheet**: Visual contact sheet showing numbered thumbnails in a grid (intended to be used with ComfyUI's **Preview Image** node)
- **image**: The selected image tensor
- **mask**: Corresponding mask (useful for further processing)
- **filename**: Name of the selected file

## Grid Layout Examples

- **1 Row**: 8 images in a single horizontal row
- **2 Rows**: 16 images in a 8×2 grid
- **4 Rows**: 32 images in a 8×4 grid  
- **8 Rows**: 64 images in a 8×8 grid

## Use Cases

- Quickly browse and select from recent AI-generated images, selecting them for post-processing
- Create workflows that process the most recent images
- Review and select from up to 64 recent images at once
