# ComfyUI-NanoBanano

A ComfyUI custom node for Google's **Gemini 2.5 Flash Image** (aka "Nano Banana") model - the state-of-the-art image generation and editing AI.

## Features

- **Multi-Modal Operations**: Generate, edit, style transfer, and object insertion
- **Up to 5 Reference Images**: Support for complex multi-image operations  
- **Character Consistency**: Maintain identity across edits and generations
- **Batch Processing**: Generate up to 4 images per request
- **Quality Control**: Temperature and quality settings
- **Aspect Ratio Support**: Multiple format options (1:1, 16:9, 9:16, 4:3, 3:4)
- **Cost Tracking**: Built-in cost estimation (~$0.039 per image)

## Requirements

- ComfyUI
- **Paid Google Gemini API Key** (Free tier does not support image generation)
- Python packages (installed automatically):
  - `google-generativeai`
  - `torch`
  - `pillow`
  - `numpy`
  - `requests`

## Installation

### Method 1: Git Clone (Recommended)

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/ShmuelRonen/ComfyUI-NanoBanano.git
cd ComfyUI-NanoBanano
pip install -r requirements.txt
```

## API Key Setup

### 1. Get Your API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in and **enable billing** (paid tier required)
3. Generate API key (starts with `AIza...`)

### 2. Configure the Key

**Environment Variable (Recommended):**
```bash
export GEMINI_API_KEY="your_api_key_here"
```

**Or enter directly in the node's api_key field**

## Usage

1. **Find the Node**: Search "Nano Banana" in ComfyUI
2. **Select Operation**:
   - **Generate**: Create new images from text
   - **Edit**: Modify existing images 
   - **Style Transfer**: Apply styles from references
   - **Object Insertion**: Add elements to scenes

3. **Key Parameters**:
   - `prompt`: Describe what you want
   - `reference_image_1-5`: Upload reference images
   - `temperature`: Creativity (0.0-1.0)
   - `batch_count`: Images per run (1-4)
   - `aspect_ratio`: Only affects generation, not editing

## Examples

### Basic Generation
```
Operation: generate
Prompt: "A dragon flying over a cyberpunk city at sunset"
Aspect Ratio: 16:9
```

### Image Editing
```
Operation: edit  
Reference Image: [Your photo]
Prompt: "Add falling snow and winter atmosphere"
```

### Style Transfer
```
Operation: style_transfer
Reference Image 1: [Content]
Reference Image 2: [Style reference]
Prompt: "Apply watercolor painting style"
```

## Important Limitations

- **Output Resolution**: API limits to ~1024px max dimension
- **Cost**: ~$0.039 per image generated
- **API Access**: Requires paid Gemini subscription
- **Rate Limits**: Vary by subscription tier

## Troubleshooting

**"API key not valid"**
- Ensure billing is enabled in Google Cloud Console
- Free tier cannot access image generation models

**"No images found in response"**
- Try more explicit prompts: "Generate an image of..."
- Check API rate limits and billing status

**Module errors**
```bash
pip install google-generativeai pillow torch numpy requests
```

## Cost Information

- **Per Image**: ~$0.039 USD
- **Batch of 4**: ~$0.156 USD  
- Node displays cost estimates automatically

## Contributing

1. Fork this repository
2. Create feature branch (`git checkout -b feature/name`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push branch (`git push origin feature/name`)
5. Open Pull Request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Support

- **Issues**: [GitHub Issues](https://github.com/ShmuelRonen/ComfyUI-NanoBanano/issues)
- **ComfyUI Community**: Discord #custom-nodes channel

---

**Note**: Unofficial implementation. Google and Gemini are trademarks of Google LLC. Repository Structure

