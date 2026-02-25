# Woohee NanoBanano Gemini 2.5

Updated version of ComfyUI-NanoBanano with Gemini 2.5 Flash Image support.

## About This Version

This is an updated fork of the original [ComfyUI-NanoBanano](https://github.com/ShmuelRonen/ComfyUI-NanoBanano) by ShmuelRonen.

The original repository uses `gemini-2.0-flash-exp-image-generation` model, but this version has been updated to use the latest `gemini-2.5-flash-image` model for improved image generation capabilities.

### Changes from Original

- Updated model from `gemini-2.0-flash-exp-image-generation` to `gemini-2.5-flash-image`
- Added ComfyUI Registry support with pyproject.toml
- Maintained all original functionality and features

## Features

- Multi-Modal Operations: Generate, edit, style transfer, and object insertion
- Up to 5 Reference Images: Support for complex multi-image operations
- Character Consistency: Maintain identity across edits and generations
- Batch Processing: Generate up to 4 images per request
- Quality Control: Temperature and quality settings
- Aspect Ratio Support: Multiple format options (1:1, 16:9, 9:16, 4:3, 3:4)
- Cost Tracking: Built-in cost estimation (approximately 0.039 USD per image)

## Requirements

- ComfyUI
- Paid Google Gemini API Key (Free tier does not support image generation)
- Python packages (installed automatically):
  - google-generativeai >= 0.8.0
  - torch >= 1.11.0
  - pillow >= 8.3.0
  - numpy >= 1.21.0
  - requests >= 2.25.0

## Installation

### Via ComfyUI Manager

Search for "Woohee NanoBanano Gemini 2.5" in ComfyUI Manager and install.

### Manual Installation

\`\`\`bash
cd ComfyUI/custom_nodes/
git clone https://github.com/woohee5511/woohee-nanobanano-gemini25.git
cd woohee-nanobanano-gemini25
pip install -r requirements.txt
\`\`\`

## API Key Setup

### 1. Get Your API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in and enable billing (paid tier required)
3. Generate API key (starts with AIza...)

### 2. Configure the Key

Environment Variable (Recommended):
\`\`\`bash
export GEMINI_API_KEY="your_api_key_here"
\`\`\`

Or enter directly in the node's api_key field.

## Usage

1. Find the Node: Search "Nano Banana" in ComfyUI
2. Select Operation:
   - Generate: Create new images from text
   - Edit: Modify existing images
   - Style Transfer: Apply styles from references
   - Object Insertion: Add elements to scenes

3. Key Parameters:
   - prompt: Describe what you want
   - reference_image_1-5: Upload reference images
   - temperature: Creativity (0.0-1.0)
   - batch_count: Images per run (1-4)
   - aspect_ratio: Only affects generation, not editing

## Examples

### Basic Generation
\`\`\`
Operation: generate
Prompt: "A dragon flying over a cyberpunk city at sunset"
Aspect Ratio: 16:9
\`\`\`

### Image Editing
\`\`\`
Operation: edit
Reference Image: [Your photo]
Prompt: "Add falling snow and winter atmosphere"
\`\`\`

### Style Transfer
\`\`\`
Operation: style_transfer
Reference Image 1: [Content]
Reference Image 2: [Style reference]
Prompt: "Apply watercolor painting style"
\`\`\`

## Important Limitations

- Output Resolution: API limits to approximately 1024px max dimension
- Cost: Approximately 0.039 USD per image generated
- API Access: Requires paid Gemini subscription
- Rate Limits: Vary by subscription tier

## Troubleshooting

"API key not valid"
- Ensure billing is enabled in Google Cloud Console
- Free tier cannot access image generation models

"No images found in response"
- Try more explicit prompts: "Generate an image of..."
- Check API rate limits and billing status

Module errors:
\`\`\`bash
pip install google-generativeai pillow torch numpy requests
\`\`\`

## Cost Information

- Per Image: Approximately 0.039 USD
- Batch of 4: Approximately 0.156 USD
- Node displays cost estimates automatically

## Credits

Original Code: [ComfyUI-NanoBanano](https://github.com/ShmuelRonen/ComfyUI-NanoBanano) by ShmuelRonen

Updated for Gemini 2.5 by woohee5511

## License

MIT License - see LICENSE file for details.

## Support

- Issues: [GitHub Issues](https://github.com/woohee5511/woohee-nanobanano-gemini25/issues)
- Original Repository: [ComfyUI-NanoBanano](https://github.com/ShmuelRonen/ComfyUI-NanoBanano)
- ComfyUI Community: Discord channel

Note: Unofficial implementation. Google and Gemini are trademarks of Google LLC.
