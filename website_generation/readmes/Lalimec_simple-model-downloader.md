# ComfyUI Simple Model Downloader

A simple and efficient model downloader extension for ComfyUI that allows downloading models with progress tracking and folder management.

![image](https://github.com/user-attachments/assets/f3bb0a2e-6966-4c5b-8e6d-e0585e09f4b5)

## Features

- 📥 Download models directly from URLs
- 📊 Real-time progress tracking with speed and size information
- 📁 Folder management (create new folders, organize models)
- 💾 Persistent last used folder selection
- ⚠️ File existence checks and overwrite confirmation
- 🎨 ComfyUI-styled interface

## Supported File Types

The following model file extensions are supported:
- `.safetensors`
- `.pt`
- `.ckpt`
- `.bin`

## Installation

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/Lalimec/simple-model-downloader
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Restart ComfyUI

## Usage

1. Click the "⬇️ Basic Downloader" button in the ComfyUI menu
2. Enter the model URL and desired name
3. Select or create a destination folder
4. Click Download and monitor the progress

## Features in Detail

### Model Download
- Progress bar showing download progress
- Download speed and file size information
- Success/error notifications
- Automatic file extension validation

### Folder Management
- Create new folders for organization
- Nested folder support
- Last used folder memory
- Visual folder hierarchy in dropdown

### Safety Features
- File existence checks
- Overwrite confirmation
- Safe filename generation
- Error handling and cleanup

## Requirements

- Python >= 3.8
- ComfyUI
- `aiohttp` >= 3.8.0
- `wget` command-line tool

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
