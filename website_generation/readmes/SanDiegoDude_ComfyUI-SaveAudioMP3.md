# Save Audio MP3 for ComfyUI

A custom node for ComfyUI to save audio as MP3 files.

![image](https://github.com/user-attachments/assets/edc13e00-3bfd-4560-bba4-843ab3f5a145)


## What It Does

*   Saves audio from an upstream node into an MP3 file.
*   Lets you choose the MP3 bitrate (defaults to 320k).
*   You can set a `filename_prefix` (e.g., `audio_outputs/my_project/`) to organize your files.
*   An optional `song_name` input will be added to your filename (spaces are turned into underscores).

## Installation

**1. Using ComfyUI Manager (Recommended):**

*   In ComfyUI, open the Manager.
*   Click "Install Custom Nodes".
*   Search for this node (e.g., "SaveAudioMP3" or by its repository name).
*   Click "Install" and restart ComfyUI.

**2. Manual Installation (Git Clone):**

*   Go to your `ComfyUI/custom_nodes/` directory in a terminal.
*   Run:
    ```bash
    git clone https://github.com/your_username/ComfyUI-SaveAudioMP3.git 
    ```
    *(Make sure to use your actual repository URL here.)*
*   Restart ComfyUI.

## Dependencies

You'll need to install these manually for the node to work:

*   **`pydub` (Python library):**
    Open your terminal (and activate your ComfyUI Python environment if you use one) and run:
    ```bash
    pip install pydub
    ```

*   **`ffmpeg` (System utility):**
    `pydub` needs `ffmpeg` to do its work.
    *   **Windows:** Download from [ffmpeg.org](https://ffmpeg.org/download.html). Extract it, and add the `bin` folder inside to your system's PATH.
    *   **macOS:** `brew install ffmpeg`
    *   **Linux:** `sudo apt update && sudo apt install ffmpeg` (or your distro's equivalent).
    Make sure you can run `ffmpeg -version` in your terminal.


