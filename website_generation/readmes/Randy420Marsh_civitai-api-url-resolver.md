# Civitai URL Resolver for ComfyUI

A ComfyUI custom node that converts Civitai share/model page URLs into direct download URLs, making it easier to integrate Civitai models into your workflows.

## What It Does

This node solves a common problem: Civitai share links and model page URLs can't be used directly for downloading. This node automatically resolves them to direct download URLs that can be used with download nodes or external tools.

**Input:** `https://civitai.com/models/123456?modelVersionId=789`  
**Output:** `https://civitai.com/api/download/models/789`

## Why Use This Node?

### The Problem
- Civitai share URLs are designed for browsing, not downloading
- Model page URLs don't point directly to the file
- Manually finding download links is tedious and breaks workflow automation
- Some models require API authentication to access

### The Solution
This node:
- ✅ Automatically extracts model/version IDs from URLs
- ✅ Queries Civitai's API to get the correct download URL
- ✅ Handles authentication securely using API tokens
- ✅ Works with share links, model pages, and direct download URLs
- ✅ Integrates seamlessly into ComfyUI workflows

## Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "Civitai URL Resolver"
3. Click Install

### Method 2: Manual Installation
1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/Randy420Marsh/civitai-api-url-resolver.git
   ```

3. Restart ComfyUI

## Configuration

### Setting Up Your Civitai API Token (Optional but Recommended)

Some Civitai models require authentication. To enable full functionality:

1. **Get your Civitai API token:**
   - Go to https://civitai.com/user/account
   - Navigate to API Keys section
   - Generate a new API key
   - Copy the token (it should be 32 characters long)

2. **Configure the node:**
   - Navigate to `ComfyUI/custom_nodes/civitai-api-url-resolver/`
   - Copy `.config.example` to `.config`:
     ```bash
     cp .config.example .config
     ```
   - Edit `.config` and replace `YOUR_TOKEN_HERE` with your actual token:
     ```ini
     [API]
     civitai_token = your_actual_32_character_token_here
     ```

3. **Secure your config file (Linux/Mac):**
   ```bash
   chmod 600 .config
   ```

**Important:** The `.config` file is ignored by git and stays on your local machine. Your token is never exposed in URLs, workflows, or generated images.

## Usage

### In ComfyUI

1. Add the node to your workflow:
   - Right-click → Add Node → utils/url → Civitai Share → Direct URL

2. Paste any Civitai URL into the input:
   - Share links: `https://civitai.com/models/123456?modelVersionId=789`
   - Model pages: `https://civitai.com/models/123456`
   - Already direct URLs: `https://civitai.com/api/download/models/789`

3. The node outputs a direct download URL that you can use with:
   - Download nodes
   - External download managers
   - Automation scripts
   - Any tool that needs a direct file URL

### Example Workflow

```
[Civitai Share → Direct URL] → [Download Model Node] → [Load Checkpoint]
```

## Security

This node is designed with security as a priority:

- ✅ **API tokens stay local** - stored in `.config` file on your machine only
- ✅ **Tokens never exposed** - used only in HTTP headers, never in URLs or outputs
- ✅ **Git-safe** - `.config` is in `.gitignore` and won't be committed
- ✅ **No data collection** - no telemetry, no external logging
- ✅ **Open source** - audit the code yourself

## Supported URL Formats

The node handles these Civitai URL types:

- ✅ Share links with modelVersionId: `/models/12345?modelVersionId=67890`
- ✅ Model page URLs: `/models/12345`
- ✅ Direct download URLs: `/api/download/models/67890` (passes through)
- ✅ Full URLs with domain: `https://civitai.com/models/...`
- ✅ Relative URLs: `/models/...`

Non-Civitai URLs are returned unchanged.

## Troubleshooting

### "The node returns the same URL I put in"
- Check if you need authentication for that model
- Verify your `.config` file exists and has a valid token
- Ensure the token is valid 32 characters with no spaces

### "Downloads fail with 401/403 errors"
- The model requires authentication
- Add your Civitai API token to `.config` (see Configuration section)

### "Node not appearing in ComfyUI"
- Restart ComfyUI completely
- Check `ComfyUI/custom_nodes/` contains this folder
- Look for errors in the ComfyUI console

## Requirements

- ComfyUI (any recent version)
- Python 3.8+
- No additional dependencies (uses Python standard library only)

## API Rate Limits

The node respects Civitai's API rate limits. For heavy usage, ensure you're using an API token to get higher rate limits.

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

[MIT]

## Credits

Created for the ComfyUI community to simplify Civitai model integration.

## Support

- **Issues:** [GitHub Issues](https://github.com/Randy420Marsh/civitai-api-url-resolver/issues)
- **Discussions:** [GitHub Discussions](https://github.com/Randy420Marsh/civitai-api-url-resolver/discussions)
- **Civitai API Docs:** https://github.com/civitai/civitai/wiki/REST-API-Reference

---


**Note:** This is an unofficial tool and is not affiliated with or endorsed by Civitai.
