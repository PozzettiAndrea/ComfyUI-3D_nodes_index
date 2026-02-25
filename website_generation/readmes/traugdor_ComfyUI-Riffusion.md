# ComfyUI-Riffusion

A ComfyUI extension for Riffusion audio generation. Requires installation of 3rd-party software FFmpeg.

## Installation

1. Clone this repository into your `ComfyUI/custom_nodes` directory:
```git clone https://github.com/traugdor/ComfyUI-Riffusion.git```
OR
Install via Comfy Registry: https://registry.comfy.org/publishers/traugdor/nodes/riffusion

2. Download and install FFMPEG by following these instructions:

### Windows users

1. **Download FFmpeg:**
    * Go to the [official FFmpeg download page](https://ffmpeg.org/download.html).
    * Click on the "Windows" logo and select a build (usually, the "gpl" builds are recommended). You may find builds hosted by third-party sites like Gyan.dev or BtbN.
2. **Extract the Files:**
    * Once downloaded, extract the contents of the ZIP file to a location on your computer (e.g., C:\ffmpeg).
3. **Add FFmpeg to System PATH:**
    * Right-click on "This PC" or "Computer" on your desktop or in File Explorer and select "Properties."
    * Click on "Advanced system settings" on the left side.
    * In the System Properties window, click on the "Environment Variables" button.
    * In the Environment Variables window, find and select the "Path" variable in the "System variables" section, then click "Edit."
    * Click "New" and add the path to the bin directory of the extracted FFmpeg folder (e.g., C:\ffmpeg\bin).
    * Click "OK" to close all dialog boxes.
4. **Verify Installation:**
    * Open Command Prompt (press Win + R, type cmd, and hit Enter).
    * Type the following command and press Enter:
    ```bash
    ffmpeg -version
    ```
    * If FFmpeg is correctly installed, you will see version information and other details. You may need to close and reopen your Command Prompt/Powershell/Terminal window to get the latest environment variables.
5. **Restart ComfyUI**

### Linux users

1. **Open Terminal**
2. **Install FFmpeg** using your package manager
    * Debian/Ubuntu-based:
        ```bash
        sudo apt update
        sudo apt install ffmpeg
        ```
    * Fedora:
        ```bash
        sudo dnf install ffmpeg 
        ```
    * Arch:
        ```bash
        sudo pacman -S ffmpeg
        ```
3. **Verify installation**
    * After installation is complete, you can verify that FFmpeg is installed correctly by running:
        ```bash
        ffmpeg -version
        ```
    * If FFmpeg is installed, you will see version information and other details about the installation.

4. **Restart ComfyUI**

## Usage

The extension adds a new node "Riffusion" under the audio category.

## TODO
- Add support for multiple images (as input) to generate a single audio file for longer audio lengths
- Add support for multiple images to generate multiple audio files
- Add FFmpeg installer for Windows/Linux? Current method is to warn user and disable audio formats that require FFmpeg