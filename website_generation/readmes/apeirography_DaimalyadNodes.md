# DaimalyadNodes

A ComfyUI custom nodes package providing **Model Downloader** and **API-Friendly Wildcard Processor** utilities.

## Features

### 🚀 Model Downloader (`DaimalyadModelDownloader`)
- **Workflow-based model downloading** - Download models directly from your ComfyUI workflows
- **Smart path handling** - Automatically organizes downloads into proper ComfyUI model directories
- **SHA-256 verification** - Optional integrity checking for downloaded files
- **Retry logic** - Robust network error handling with exponential backoff
- **Progress tracking** - Real-time download progress with speed estimates
- **Safe file operations** - Atomic file replacement to prevent corruption

### 🎲 API-Friendly Wildcard Processor (`DaimalyadWildcardProcessor`)
- **Advanced wildcard resolution** - Supports nested `{option1|option2|option3}` syntax
- **Escape sequences** - Use `\{`, `\|`, `\}` for literal characters
- **Always fresh randomization** - Uses nanosecond timestamp for non-reproducible results
- **Simple interface** - Single text input, no complex controls
- **API integration** - Designed for programmatic use in automated workflows
- **API workflow execution** - Works seamlessly with ComfyUI API calls, unlike most other wildcard processors
- **Performance optimized** - Efficient parsing with guaranteed fresh execution

## Installation

### Via ComfyUI Manager (Recommended)
1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
2. Go to **Manager** → **Install Custom Nodes**
3. Search for `daimalyadnodes`
4. Click **Install**

### Manual Installation
1. Clone this repository to your `ComfyUI/custom_nodes/` directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/daimalyad/DaimalyadNodes.git
   ```
2. Restart ComfyUI

## Usage

### Model Downloader

**Inputs:**
- `url` (required): HTTP(S) URL to download from
- `subfolder` (required): Target subfolder under `/models` (e.g., "checkpoints", "loras", "controlnet")
- `filename` (optional): Custom filename (defaults to URL basename)
- `overwrite` (optional): Whether to overwrite existing files (default: True)
- `sha256` (optional): SHA-256 hash for integrity verification
- `timeout_s` (optional): Network timeout in seconds (default: 120)
- `retries` (optional): Number of retry attempts (default: 3)
- `user_agent` (optional): Custom HTTP User-Agent header

**Output:**
- `path`: Absolute path to the downloaded file

**Example:**
```
URL: https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned.safetensors
Subfolder: checkpoints
Filename: stable-diffusion-v1-5.safetensors
SHA-256: 6ce9ef5449e8abcb9bafd9a5d10aa7f9653e3a9f3c77a2e7d8f1e9a2b3c4d5e6f
```

### Wildcard Processor

**Inputs:**
- `text` (required): Text containing wildcards like `{a beautiful|an amazing} {landscape|portrait}`

**Output:**
- `text`: Resolved text with wildcards replaced

**Examples:**
```
Input: "A {beautiful|stunning} {landscape|portrait} of a {cat|dog}"
Output: "A beautiful landscape of a cat" (or any combination, always fresh)

Input: "Create a \{literal\} {option1|option2}"
Output: "Create a {literal} option1" (escaped braces preserved, always fresh)
```

**Key Features:**
- **Always fresh results** - Each execution produces different output
- **Non-reproducible** - Same input never gives same output twice
- **Nanosecond precision** - Uses `time.time_ns()` for maximum randomization
- **No caching** - Guaranteed fresh execution every time

**API Workflow Compatibility:**
Unlike most other wildcard processors, this node works seamlessly with ComfyUI's API workflow execution system. When you execute workflows via API calls, the wildcard processor will:
- **Always execute** - No caching issues that plague other processors
- **Provide fresh randomization** - Each API call gets unique wildcard resolution
- **Maintain consistency** - Same API workflow always produces fresh results
- **Integrate seamlessly** - Works exactly the same in API and manual execution

This makes it ideal for automated workflows, batch processing, and server-side applications where you need reliable, fresh wildcard resolution.

## Node Categories

- **Model Downloader**: `utils`
- **Wildcard Processor**: `Text/Wildcards`

## Requirements

- **Python**: 3.8+
- **ComfyUI**: Latest version
- **Dependencies**: None (uses only Python standard library)

## Development

### Project Structure
```
DaimalyadNodes/
├── __init__.py                  # Node exports
├── daimalyad_model_downloader.py
├── daimalyad_wildcard_processor.py
├── requirements.txt             # Dependencies
├── pyproject.toml              # Package metadata
├── LICENSE                     # MIT License
└── README.md                   # This file
```

### Building
This package is designed to work directly as a ComfyUI custom node. No build step required.

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/daimalyad/DaimalyadNodes/issues)
- **Discord**: Join the ComfyUI community for general support

## Changelog

### v0.1.0
- Initial release
- Model Downloader with SHA-256 verification
- API-Friendly Wildcard Processor with guaranteed fresh randomization
- ComfyUI Manager integration ready

---

**Made with ❤️ by [@daimalyad](https://github.com/daimalyad)**
