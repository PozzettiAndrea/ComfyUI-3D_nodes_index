# ComfyUI-HMT-Suite

Custom nodes suite for ComfyUI with advanced model downloading capabilities.

## Features

### 1. Model Downloader Node
Download models from various sources directly within ComfyUI:
- ✅ **Direct file URLs** - Download any file from direct links
- ✅ **GitHub support** - Download files or entire repositories from GitHub
- ✅ **Progress tracking** - Real-time download progress for API integration
- ✅ **Cross-platform** - Works on both Windows and Linux
- ✅ **Smart file handling** - Auto-detect filenames, resume downloads, overwrite control

### 2. Custom Node Installer
Install ComfyUI custom nodes from GitHub repositories:
- ✅ **One-click installation** - Install any custom node from GitHub URL
- ✅ **Automatic dependency installation** - Installs requirements.txt automatically
- ✅ **Smart detection** - Auto-detects node name from repository URL
- ✅ **Progress tracking** - Real-time installation progress
- ✅ **Cross-platform** - Works on both Windows and Linux

### 3. ComfyUI Restart Node
Safely restart ComfyUI server from within workflows:
- ✅ **Safe restart** - Preserves all command-line arguments
- ✅ **Configurable delay** - Set delay before restart (0-10 seconds)
- ✅ **Confirmation required** - Prevents accidental restarts
- ✅ **Auto-detection** - Automatically detects Python executable and arguments
- ✅ **Cross-platform** - Works on Windows, Linux, and macOS



## Installation

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/tuyenhm68/ComfyUI-HMT-Suite.git
```

3. Install dependencies:
```bash
cd ComfyUI-HMT-Suite
pip install -r requirements.txt
```

4. Restart ComfyUI

## Usage

### Model Downloader Node

The Model Downloader node appears in the node menu under **HMT Suite > Utils > Model Downloader**.

#### Parameters:

- **download_type**: Choose between `file` or `github`
  - `file`: Direct file download from any URL
  - `github`: Download from GitHub (files or repositories)

- **url**: The source URL
  - For files: Direct download link
  - For GitHub: Repository URL, file URL, or release URL

- **destination_folder**: Folder name relative to `ComfyUI/models/`
  - Examples: `checkpoints`, `loras`, `vae`, `unet`, etc.
  - The folder will be created automatically if it doesn't exist

- **filename**: (Optional) Custom filename
  - Leave empty to auto-detect from URL
  - Specify a name to override

- **overwrite**: Whether to overwrite existing files
  - `false`: Skip download if file exists
  - `true`: Download and replace existing file

**File/Folder Existence Check:**
- The node automatically checks if the target file or folder already exists
- If `overwrite=false` and file/folder exists:
  - **For files**: Shows existing file size and skips download
  - **For repositories**: Checks for extracted folder and skips if found
  - Returns success with `skipped=true` flag
- If `overwrite=true` and file exists:
  - Shows warning and proceeds with download
  - Replaces the existing file

- **extract_repo**: (Optional, GitHub only) Extract repository ZIP
  - `true`: Download and extract repository
  - `false`: Keep as ZIP file

#### Outputs:

- **status**: `success` or `error`
- **file_path**: Full path to downloaded file
- **message**: Status message with details
- **progress_percentage**: Download progress (0-100%)

The progress percentage is updated in real-time during download and is also logged to the console every 10%.

### Example Workflows

#### 1. Download a checkpoint from direct URL
```
download_type: file
url: https://example.com/model.safetensors
destination_folder: checkpoints
filename: (leave empty for auto-detect)
overwrite: false
```

#### 2. Download from GitHub release
```
download_type: github
url: https://github.com/user/repo/releases/download/v1.0/model.safetensors
destination_folder: loras
filename: my_lora.safetensors
overwrite: false
```

#### 3. Download a file from GitHub repository
```
download_type: github
url: https://github.com/user/repo/blob/main/models/model.pt
destination_folder: custom
filename: (leave empty)
overwrite: false
```

#### 4. Clone entire GitHub repository
```
download_type: github
url: https://github.com/user/repo
destination_folder: repositories
extract_repo: true
overwrite: true
```

### Custom Node Installer

The Custom Node Installer node appears in the node menu under **HMT Suite > Utils > Custom Node Installer (HMT)**.

#### Parameters:

- **github_url**: GitHub repository URL or ZIP file URL
  - **GitHub repository**: `https://github.com/city96/ComfyUI-GGUF`
  - **ZIP file**: `https://cdn.comfy.org/city96/ComfyUI-GGUF/1.1.10/node.zip`
  - Automatically detects URL type and uses appropriate installation method


- **platform**: Target platform
  - `auto`: Automatically detect platform (default)
  - `windows`: Force Windows installation (uses .bat scripts)
  - `linux`: Force Linux installation (uses .sh scripts)

#### Outputs:

- **status**: `success` or `error`
- **installation_path**: Full path to installed custom node
- **message**: Status message with installation details

#### Installation Process:

**For GitHub Repository:**
1. **Clone Repository**: Git clones the repository to `ComfyUI/custom_nodes/`
   - Git automatically uses the repository name as the folder name
2. **Run Setup Scripts**: Automatically runs platform-specific scripts if found
3. **Auto-Install Dependencies**: If `requirements.txt` exists, automatically installs
4. **Completion**: Shows success message and reminds to restart ComfyUI

**For ZIP File:**
1. **Download**: Downloads the ZIP file from the provided URL
2. **Extract**: Extracts the ZIP file to `ComfyUI/custom_nodes/[node_name]`
   - Node name is extracted from the URL path (e.g., `ComfyUI-GGUF`)
3. **Run Setup Scripts**: Automatically runs platform-specific scripts if found
4. **Auto-Install Dependencies**: If `requirements.txt` exists, automatically installs
5. **Completion**: Shows success message and reminds to restart ComfyUI

#### Example Usage:

**Install ComfyUI-GGUF custom node:**
```
github_url: https://github.com/city96/ComfyUI-GGUF
platform: auto
```
Result: Installed to `ComfyUI/custom_nodes/ComfyUI-GGUF`

**Install from ZIP file:**
```
github_url: https://cdn.comfy.org/city96/ComfyUI-GGUF/1.1.10/node.zip
platform: auto
```
Result: Downloaded, extracted to `ComfyUI/custom_nodes/ComfyUI-GGUF`

**Install on Linux:**
```
github_url: https://github.com/username/awesome-node
platform: linux
```
Result: Installed to `ComfyUI/custom_nodes/awesome-node`

**Install on Windows:**
```
github_url: https://github.com/username/some-node
platform: windows
```
Result: Installed to `ComfyUI/custom_nodes/some-node`

#### Important Notes:

- ⚠️ **Restart Required**: You must restart ComfyUI after installing a custom node
- ⚠️ **Git Required**: Git must be installed and available in your system PATH
- ⚠️ **Auto Setup Scripts**: The node automatically runs `install.bat` or `setup.bat` if found
- ⚠️ **Auto Dependencies**: The node automatically installs requirements.txt if it exists
- ⚠️ **Python Path**: The node automatically detects Python from:
  - `ComfyUI/python_embeded/python.exe` (Windows portable)
  - `ComfyUI/python_embedded/python.exe` (alternative spelling)
  - System Python (fallback)
- ⚠️ **Existing Nodes**: If a node with the same name exists, installation will be skipped

### ComfyUI Restart Node

The ComfyUI Restart node appears in the node menu under **HMT Suite > Utils > ComfyUI Restart**.

#### Parameters:

- **restart_delay**: Delay in seconds before restarting (0-10)
  - `0`: Immediate restart
  - `2`: Default, recommended for safe restart
  - `10`: Maximum delay

- **confirm_restart**: Confirmation flag to actually perform restart
  - `false`: Shows restart info but doesn't restart (safe mode)
  - `true`: Actually restarts the server
  - ⚠️ **Must be true to restart!**

- **show_info**: (Optional) Show detailed restart information
  - `true`: Shows Python path, arguments, working directory
  - `false`: Minimal logging

#### Outputs:

- **status**: `success`, `cancelled`, or `error`
- **message**: Status message with details
- **restart_command**: Full command used to restart ComfyUI

#### How It Works:

The node automatically detects and preserves:
- Python executable path (e.g., `H:\ComfyUI\python_embeded\python.exe`)
- All command-line arguments (e.g., `--windows-standalone-build`, `--port 8188`, `--enable-cors-header`, `--disable-auto-launch`)
- Current working directory

When restart is confirmed, it:
1. Flushes all output buffers
2. Waits for specified delay
3. Replaces current process with new one
4. Preserves all original arguments

#### Example Usage:

**Basic restart:**
```
restart_delay: 2
confirm_restart: true
show_info: true
```
Result: ComfyUI restarts after 2 seconds with all arguments preserved

**Quick restart:**
```
restart_delay: 0
confirm_restart: true
show_info: false
```
Result: Immediate restart with minimal logging

**Check restart command (safe mode):**
```
restart_delay: 2
confirm_restart: false
show_info: true
```
Result: Shows restart info without actually restarting

**Auto-restart after installing custom node:**
```
[Custom Node Installer] -> [ComfyUI Restart]
confirm_restart: true
```
Result: Automatically restarts after installing a custom node

#### Important Notes:

- ⚠️ **Confirmation Required**: Must set `confirm_restart: true` to actually restart
- ⚠️ **Connection Loss**: WebSocket connections will be temporarily lost
- ⚠️ **Unsaved Work**: Save workflows before restarting
- ⚠️ **Running Workflows**: Any in-progress generations will be cancelled
- ✅ **Safe**: All command-line arguments are automatically preserved
- ✅ **Useful After**: Installing custom nodes, updating configurations, clearing memory

For detailed documentation, see [docs/COMFYUI_RESTART.md](docs/COMFYUI_RESTART.md)




## API Integration

The Model Downloader provides progress tracking for API integration.

### Access Download Progress

```python
from custom_nodes.ComfyUI_HMT_Suite.nodes.model_downloader import ModelDownloaderNode

# Get progress for specific download
progress = ModelDownloaderNode.get_download_progress(download_id)
print(progress)
# Output: {
#     "status": "downloading",
#     "percentage": 45,
#     "downloaded": 450000000,
#     "total_size": 1000000000,
#     "filename": "model.safetensors",
#     "destination": "/path/to/ComfyUI/models/checkpoints/model.safetensors"
# }

# Get all active downloads
all_downloads = ModelDownloaderNode.get_all_downloads()
```

### Progress Status Values

- `pending`: Download queued but not started
- `downloading`: Download in progress
- `extracting`: Extracting repository (GitHub only)
- `completed`: Download finished successfully
- `error`: Download failed

### Progress Dictionary Structure

```python
{
    "status": str,           # Current status
    "percentage": int,       # Download percentage (0-100)
    "downloaded": int,       # Bytes downloaded
    "total_size": int,       # Total file size in bytes
    "filename": str,         # File name
    "destination": str,      # Full destination path
    "error_message": str     # Error message (if status is "error")
}
```

## Supported GitHub URL Formats

- Repository: `https://github.com/user/repo`
- File in repo: `https://github.com/user/repo/blob/main/path/to/file`
- Raw file: `https://raw.githubusercontent.com/user/repo/main/path/to/file`
- Release asset: `https://github.com/user/repo/releases/download/tag/file`

## Requirements

- Python 3.8+
- requests
- ComfyUI

## Troubleshooting

### Download fails with network error
- Check your internet connection
- Verify the URL is accessible
- Some servers may block automated downloads

### File not found after download
- Check the `destination_folder` parameter
- Verify you have write permissions
- Look in `ComfyUI/models/[destination_folder]/`

### GitHub download fails
- Ensure the URL is a valid GitHub URL
- For private repositories, you may need authentication (not currently supported)
- Check if the repository/file exists

## Cross-Platform Notes

This node is designed to work on both Windows and Linux:
- Uses `pathlib.Path` for cross-platform path handling
- Automatically creates directories with proper permissions
- Handles different line endings and file systems

## Future Features

- [ ] Hugging Face model downloads
- [ ] Download queue management
- [ ] Bandwidth limiting
- [ ] Checksum verification
- [ ] Authentication support for private repositories
- [ ] Pause/resume downloads
- [ ] Multiple simultaneous downloads

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
