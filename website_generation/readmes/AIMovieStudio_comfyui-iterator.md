# ComfyUI Iterator Nodes

A set of custom nodes for ComfyUI that allows you to iterate over files in a directory. This is useful for batch processing images or text files.

## Features

-   **Iterator List Files**: Scans a directory for files matching specific extensions and outputs them as a list.
-   **Iterator Load Image**: Loads an image from a file path.
-   **Iterator Load String**: Loads text content from a file path.

## Installation

1.  Navigate to your ComfyUI `custom_nodes` directory.
2.  Clone this repository:
    ```bash
    git clone https://github.com/AIMovieStudio/comfyui-iterator.git
    ```
3.  Restart ComfyUI.

## Usage Guide

The core concept is to use **Iterator List Files** to generate a list of file paths, and then feed that list into **Iterator Load Image** or **Iterator Load String**.

### Batch Processing Images

1.  Add **Iterator List Files** node.
2.  Set the `directory` to your image folder.
3.  Set `extension` to `png, jpg` (or whatever you need).
4.  Add **Iterator Load Image** node.
5.  Connect `file_paths` from **Iterator List Files** to `file_path` on **Iterator Load Image**.
6.  ComfyUI will automatically execute the **Iterator Load Image** node (and any subsequent nodes) for each file in the list.

### Batch Processing Text

1.  Add **Iterator List Files** node.
2.  Set `directory` to your text folder.
3.  Set `extension` to `txt`.
4.  Add **Iterator Load String** node.
5.  Connect `file_paths` to `file_path`.

## Nodes

### Iterator List Files
-   **Inputs**:
    -   `directory`: Path to the directory.
    -   `extension`: File extensions to filter (e.g., "png, jpg").
    -   `limit`: Max files to process (0 for all).
-   **Output**: List of file paths.

### Iterator Load Image
-   **Inputs**:
    -   `file_path`: Path to an image file.
-   **Output**: Image tensor and filename.

### Iterator Load String
-   **Inputs**:
    -   `file_path`: Path to a text file.
-   **Output**: String content and filename.

## License

GPL-3.0 license
