# ComfyUI-AutoModelDownloader

A pretty straightforward rebranding of [ComfyUI-RunpodDirect](https://github.com/MadiatorLabs/ComfyUI-RunpodDirect) with the Runpod bits removed in order to make the addon ideally suited for "offline" use.  

## Features

- **Direct Downloads**: Download models directly to your ComfyUI instance.
- **Background Downloads**: Downloads happen in the background with progress tracking.
- **Multi-Connection Support**: Accelerated downloads using multiple connections.
- **Cross-Platform**: Works on Linux, Windows, and macOS.
- **Secure**: Validates filenames and paths to prevent security issues.
- **Privacy Focused**: No external tracking or analytics.

## Usage

### Via Missing Models Dialog

1. Load a workflow that references missing models.
2. When the "Missing Models" dialog appears, you'll see:
   - **Download All Models** button (downloads all models sequentially)
   - Individual buttons for each model:
     - **Download** (browser download)
     - **Copy URL** (copy model URL)
     - **Download to Comfy** (NEW - downloads directly to the appropriate Comfy directory)

3. **Option A: Download All Models**
   - Click "Download All Models" button.
   - Watch the progress area showing:
     - Current file being downloaded.
     - Overall progress.
     - Download speed and file size.
     - Pause/Resume/Cancel controls.

4. **Option B: Download Individual Model**
   - Click "Download to Comfy" button for a specific model.
   - Button shows status with icons (spinner → checkmark/error).
   - Download happens in the background.

## Installation

### ComfyUI Manager (Recommended)
1. Search for "ComfyUI-AutoModelDownloader" in ComfyUI Manager.
2. Install the node.
3. Restart ComfyUI.

### Manual Installation
1. Navigate to your ComfyUI `custom_nodes` directory.
2. Clone this repository:
   ```bash
   git clone https://github.com/FNGarvin/ComfyUI-AutoModelDownloader.git
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Restart ComfyUI.

## License

GNU General Public License v3.0 - See [LICENSE](LICENSE) for details.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue.

## Credits

Since this is basically a Rebranded ComfyUI-RunpodDirect, all credit goes to MadiatorLabs.
