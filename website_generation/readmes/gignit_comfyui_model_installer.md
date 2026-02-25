# ComfyUI Model Installer

Automatically installs missing model files from workflow templates with Install/Uninstall buttons and progress tracking.

## Features

- **Workflow-Based Security**: Only allows installation of models defined in workflow templates
- **One-Click Installation**: Install missing models directly from the Missing Models dialog
- **Smart Directory Detection**: Automatically determines correct installation directories
- **Multi-Path Support**: Downloads files to path with most available storage (v1.1.2 - requested by BrknSoul)
- **Enhanced Proxy Support**: Robust proxy detection and timeout handling (v1.1.5)
- **Progress Tracking**: Real-time download progress with speed, ETA, and completion percentage
- **Hugging Face Support**: Seamless authentication for gated models
- **Multiple Sources**: Supports Hugging Face, Civitai, and direct download URLs
- **Safe Installation**: Validates paths and prevents unauthorized downloads

## Installation

### Via ComfyUI-Manager (Recommended)
1. Open ComfyUI-Manager in your ComfyUI interface
2. Search for "Model Installer"
3. Click Install
4. Restart ComfyUI

### Manual Installation
1. Clone this repository to your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/gignit/comfyui_model_installer
   ```
2. Install dependencies:
   ```bash
   pip install -r comfyui_model_installer/requirements.txt
   ```
3. Restart ComfyUI

## Usage

1. Load a workflow that requires missing models
2. Open the Missing Models dialog (appears automatically or via menu)
3. Click the **Install** button next to any missing model

![Missing Models](images/step1-missing-models.png)

4. Watch the progress in the top-right download panel

![Downloading](images/step2-downloading.png)

5. The button changes to **Uninstall** when the model is installed

![Complete](images/step3-complete.png)


### Hugging Face Authentication

For gated models on Hugging Face:
1. Click Install on a gated model
2. Enter your Hugging Face token in the dialog that appears
3. Get your token from: https://huggingface.co/settings/tokens
4. The token is saved for future downloads

## How It Works

The extension automatically determines the correct installation directory by:
1. **Primary Method**: Reading directory info from workflow templates (`"text_encoders / clip_l.safetensors"`)
2. **Fallback Method**: Mapping URL patterns to model directories

### Supported Model Types
- Checkpoints → `models/checkpoints/`
- LoRAs → `models/loras/`
- VAE → `models/vae/`
- ControlNet → `models/controlnet/`
- Text Encoders → `models/text_encoders/`
- CLIP Vision → `models/clip_vision/`
- Upscale Models → `models/upscale_models/`

## Configuration

### Enable/Disable Extension
Use ComfyUI-Manager to enable or disable this extension:
- ComfyUI-Manager → Custom Nodes → Enable/Disable "Model Installer"

**Important**: The directory name must use underscores (`comfyui_model_installer`) not hyphens for Python import compatibility.

### Uninstall Feature
The uninstall feature is disabled by default. To enable it, modify the configuration:

1. Edit `custom_nodes/comfyui_model_installer/config.py`
2. Change `ALLOW_UNINSTALL = False` to `ALLOW_UNINSTALL = True`
3. Restart ComfyUI

When disabled, the client will still be presented with a button that indicates 'uninstall' but clicking this will gracefully fail indicating the feature is disabled.

### Download Configuration (v1.1.4)
Advanced users can customize download behavior by editing `config.py`:

```python
DOWNLOAD_CONFIG = {
    # Timeout settings
    "timeout_connect": 30,    # Connection timeout in seconds
    "timeout_total": None,    # Total timeout (None = unlimited)
    
    # Connection pool settings (aiohttp TCPConnector parameters)
    "limit": 100,             # Max total connections
    "limit_per_host": 30,     # Max connections per host
    "ttl_dns_cache": 10,      # DNS cache TTL in seconds
    "use_dns_cache": True,    # Enable DNS caching
    
    # Download settings
    "chunk_size": 8192,       # Download chunk size in bytes
}
```

**Performance Tuning Examples:**
- **High-performance**: Increase `limit`, `limit_per_host`, and `chunk_size`
- **Corporate/restricted**: Decrease connection limits, shorter DNS cache
- **Memory-constrained**: Reduce `chunk_size` and connection limits

## Troubleshooting

### Install buttons not visible
- Check that the extension is enabled in ComfyUI-Manager
- Hard refresh your browser (Ctrl+F5)
- Check browser console for errors

### Downloads not working
- Verify internet connection
- Check ComfyUI logs for error messages
- For Hugging Face models, ensure you have a valid token

### Connection timeouts or proxy issues (v1.1.4)
- **"Failed to Initiate Download"**: Check proxy settings and network connectivity
- **Corporate networks**: Verify `HTTP_PROXY`, `HTTPS_PROXY`, and `ALL_PROXY` environment variables
- **Slow connections**: Increase `timeout_connect` in `config.py`
- **Check logs**: Look for "Using proxy settings" messages in ComfyUI console

### Permission errors
- Ensure ComfyUI has write permissions to model directories
- Check available disk space

### Performance issues
- **Slow downloads**: Increase `chunk_size` and connection limits in `config.py`
- **Memory usage**: Decrease `chunk_size` and `limit` settings
- **Corporate restrictions**: Reduce `limit_per_host` to be more server-friendly

## Security

- **Workflow Validation**: Only models defined in workflow templates can be installed
- **Zero-Trust Model**: Backend validates all requests against cached workflow index
- **Path Protection**: Prevents directory traversal attacks with safe path joining
- **Secure Authentication**: Hugging Face tokens stored using standard `huggingface_hub` library

## Proxy Support (Enhanced in v1.1.4)

The model installer automatically detects and uses proxy settings from environment variables. This works independently of ComfyUI's proxy configuration and includes robust timeout handling and error feedback.

### Environment Variables
Set these environment variables before starting ComfyUI:

```bash
# For HTTP and HTTPS proxies
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080

# For authenticated proxies
export HTTP_PROXY=http://username:password@proxy.company.com:8080
export HTTPS_PROXY=http://username:password@proxy.company.com:8080

# For SOCKS proxies (supports all protocols)
export ALL_PROXY=socks5://127.0.0.1:7890

# Mixed proxy setup example (supports both cases)
export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890

# Exclude local addresses from proxy
export NO_PROXY=localhost,127.0.0.1,.local

# Then start ComfyUI
python main.py --listen 0.0.0.0 --port 8189
```

### Windows Example
```cmd
set HTTP_PROXY=http://proxy.company.com:8080
set HTTPS_PROXY=http://proxy.company.com:8080
set ALL_PROXY=socks5://127.0.0.1:7890
python main.py --listen 0.0.0.0 --port 8189
```

### Download Behavior (v1.1.4 Improvements)
- **Fast failure detection**: 30 seconds to establish connection (configurable)
- **No download timeout**: Large model files can take hours without interruption
- **Immediate error feedback**: "Failed to Initiate Download" appears instantly on connection issues
- **Smart retry system**: "Retry Install" button for failed downloads with error details
- **Comprehensive proxy support**: HTTP, HTTPS, SOCKS5, and mixed configurations
- **Configurable connection pooling**: Optimized for corporate and high-performance environments

### Button States
- **"Install"** → **"Initiating..."** → **"Downloading..."** (success)
- **"Install"** → **"Initiating..."** → **"Failed to Initiate Download"** (connection timeout/proxy issues)
- **"Downloading..."** → **"Retry Install"** (download failure during progress)

The model installer uses its own HTTP client with configurable settings for optimal performance in any network environment, including corporate proxies and restricted networks.

## License

MIT License - see LICENSE file for details
