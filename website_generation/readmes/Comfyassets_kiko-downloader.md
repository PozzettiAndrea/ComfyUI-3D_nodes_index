# Kiko Downloader

A ComfyUI custom node for downloading models, LoRAs, upscalers, and more from CivitAI, HuggingFace, and other sources. If you are logged into these pages in a browser it will work without an API token, if you are using runpod or another means you can provide your API token. 

## Features

- **CivitAI Support**: Download models directly from CivitAI model pages or API URLs
- **HuggingFace Support**: Download from HuggingFace repositories (supports blob and resolve URLs)
- **Custom URLs**: Download from any direct download URL
- **Progress Tracking**: Real-time download progress with speed indicator
- **Auto-Detection**: Automatically detects the download source from the URL
- **Skip Existing**: Optionally skip download if file already exists
- **API Token Support**: Authenticate with CivitAI or HuggingFace for gated models
- **Interrupt Handling**: Safely handles user cancellation and cleans up partial downloads

## Installation

### Via ComfyUI Manager (Recommended)

Search for "Kiko Downloader" in ComfyUI Manager and install.

### Manual Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/kiko-downloader.git
   ```

3. Restart ComfyUI

## Usage

The node appears under **🫶 ComfyAssets / 🛠️ Utils** category in ComfyUI.

### Inputs

| Input | Type | Description |
|-------|------|-------------|
| `url` | STRING | URL to download from (CivitAI, HuggingFace, or direct link) |
| `save_path` | STRING | Directory path to save the downloaded file (relative to ComfyUI) |
| `filename` | STRING (optional) | Custom filename (leave empty for auto-detection) |
| `api_token` | STRING (optional) | API token for CivitAI or HuggingFace authentication |
| `force_download` | BOOLEAN | Force re-download even if file exists |

### Example URLs

**CivitAI:**
- Model page: `https://civitai.com/models/12345`
- Specific version: `https://civitai.com/models/12345?modelVersionId=67890`
- Direct API: `https://civitai.com/api/download/models/67890`

**HuggingFace:**
- Blob URL: `https://huggingface.co/username/repo/blob/main/model.safetensors`
- Resolve URL: `https://huggingface.co/username/repo/resolve/main/model.safetensors`

**Custom:**
- Any direct download URL: `https://example.com/files/model.safetensors`

### Common Save Paths

| Model Type | Save Path |
|------------|-----------|
| Checkpoints | `models/checkpoints` |
| LoRAs | `models/loras` |
| VAE | `models/vae` |
| Upscalers | `models/upscale_models` |
| ControlNet | `models/controlnet` |
| Embeddings | `models/embeddings` |

## API Tokens

### CivitAI Token

1. Go to [CivitAI Account Settings](https://civitai.com/user/account)
2. Navigate to "API Keys"
3. Create a new API key
4. Copy the key and paste it in the `api_token` input

### HuggingFace Token

1. Go to [HuggingFace Settings](https://huggingface.co/settings/tokens)
2. Create a new access token with "Read" permissions
3. Copy the token and paste it in the `api_token` input

## Project Structure

```
kiko-downloader/
├── __init__.py              # ComfyUI entry point
├── kiko_downloader/         # Main package
│   ├── __init__.py          # Package exports
│   ├── node.py              # ComfyUI node implementation
│   ├── base.py              # Base downloader class
│   ├── civitai.py           # CivitAI downloader
│   ├── huggingface.py       # HuggingFace downloader
│   ├── custom.py            # Custom URL downloader
│   └── detector.py          # URL type detection
├── pyproject.toml           # Project configuration
├── requirements.txt         # Dependencies (none required)
├── LICENSE                  # MIT License
└── README.md                # This file
```

## Development

### Requirements

- Python 3.10+
- No external dependencies (uses only Python standard library)

### Code Quality

```bash
# Format code
black .

# Lint
flake8 .

# Type check
mypy .
```

## License

MIT License - see [LICENSE](LICENSE) for details.
