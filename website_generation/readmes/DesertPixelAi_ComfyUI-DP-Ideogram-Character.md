# ComfyUI DP Ideogram Character Node

A custom ComfyUI node for generating consistent character images using Ideogram API v3's character reference feature. Part of the Desert Pixel (DP) node collection.

<img width="1254" height="580" alt="dxrthgft" src="https://github.com/user-attachments/assets/421e13e8-97a6-4b3b-ad17-a1b81c3dbd65" />

## 🌟 Features

- 🎨 **Character Consistency**: Generate multiple images with the same character
- 🖼️ **Character Reference**: Use any portrait/face image as reference
- 📐 **Flexible Aspect Ratios**: 15+ preset dimensions for any use case
- 🎨 **Five Style Types**: Auto, General, Realistic, Design, Fiction
- 🚀 **Three Speed Modes**: Turbo, Default, and Quality
- 🎲 **Seed Control**: Reproducible results with seed management
- ✨ **Magic Prompt**: AI-enhanced prompt generation
- 📦 **Batch Generation**: Generate 1-4 images at once

## 📋 Requirements

- ComfyUI (latest version)
- Python 3.8+
- Ideogram API key

## 🔧 Installation

### Method 1: Git Clone

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/DesertPixelAI/ComfyUI-DP-Ideogram-Character
   cd ComfyUI-DP-Ideogram-Character
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Restart ComfyUI

### Method 2: Manual Installation

1. Download the repository as ZIP
2. Extract to `ComfyUI/custom_nodes/ComfyUI-DP-Ideogram-Character`
3. Install dependencies: `pip install -r requirements.txt`
4. Restart ComfyUI

## 🔑 Getting an API Key

1. Visit [Ideogram Developer Portal](https://developer.ideogram.ai)
2. Sign up or log in to your account
3. Navigate to API section
4. Create a new API key
5. Copy the key (it will only be shown once)

## 📖 Usage

### Basic Workflow

1. Add the **"DP Ideogram Character"** node to your workflow
2. Connect an image source to the `character_image` input:
   - Load Image node
   - VAE Decode output
   - Any node outputting IMAGE type
3. Enter your API key
4. Write a descriptive prompt
5. Configure settings (aspect ratio, speed, etc.)
6. Click "Queue Prompt" to generate

### Node Inputs

#### Required Inputs
- **API Key**: Your Ideogram API key (keep it secret!)
- **Prompt**: Detailed description of the scene/pose
- **Character Image**: Reference image (portrait/headshot works best)
- **Aspect Ratio**: Output dimensions (15+ presets: 1:1, 16:9, 9:16, etc.)
- **Style Type**: Visual style (Auto, General, Realistic, Design, Fiction)
- **Image Count**: Number of images to generate (1-4)
- **Render Speed**: Quality/speed trade-off

#### Optional Inputs
- **Seed**: For reproducible results (-1 for random)
- **Magic Prompt**: AI enhancement (AUTO/ON/OFF)

### Node Outputs
- **images**: Generated images as tensor batch
- **info**: Generation details (seed, image count, dimensions)

## 💡 Tips for Best Results

### Character Reference Image
- Use clear, well-lit portraits
- Face should be clearly visible
- Slight angle often works better than straight-on
- Avoid heavily cropped or obscured faces

## 🔧 Troubleshooting

### Node Not Appearing in ComfyUI

If the "DP Ideogram Character" node doesn't appear in your ComfyUI node menu:

1. **Check dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify file structure**:
   ```
   ComfyUI-DP-Ideogram-Character/
   ├── __init__.py
   ├── nodes/
   │   ├── __init__.py
   │   └── ideogram_character.py
   ├── utils/
   │   ├── __init__.py
   │   ├── image_utils.py
   │   └── api_client.py
   ├── requirements.txt
   └── README.md
   ```

3. **Restart ComfyUI completely**

### Common Error Messages

- **"Invalid API key"**: Check your API key at https://developer.ideogram.ai
- **"No images returned"**: Check your API quota/credits
- **"Image too large"**: The reference image exceeds 10MB limit
- **"Import error"**: Check ComfyUI console for detailed error messages

### Getting Help

1. Check ComfyUI console for error messages
2. Verify your API key has sufficient credits
3. Ensure all dependencies are installed correctly
- Resolution: at least 512x512px recommended

### Prompts
- Be descriptive about pose, setting, and action
- Include details about clothing and environment
- Specify camera angles and lighting
- The AI will preserve facial features from reference

## 💰 Pricing

Prices per image with character reference:
- **Turbo**: $0.04 (fastest, lower quality)
- **Default**: $0.07 (balanced)
- **Quality**: $0.10 (slowest, best quality)

## ⚠️ API Limitations

When using character reference with Ideogram API:
- Custom color palettes are not supported
- Style reference images cannot be combined with character reference
- Character masks are not supported in Generate mode (use Edit mode for selective editing)
- Image URLs from Ideogram expire after a limited time (download to keep)

## 🗂️ Project Structure

```
ComfyUI-DP-Ideogram-Character/
├── __init__.py              # Main package file
├── nodes/                   # Node implementations
│   ├── __init__.py
│   └── ideogram_character.py
├── utils/                   # Utility functions
│   ├── __init__.py
│   ├── image_utils.py      # Image processing
│   └── api_client.py        # API communication
├── requirements.txt         # Python dependencies
└── README.md               # Documentation
```

## 🐛 Troubleshooting

### Common Issues

1. **"Invalid API key"**
   - Check your API key is correct
   - Ensure no extra spaces or characters
   - Verify API key is active on Ideogram dashboard

2. **"No images returned"**
   - Check your API quota/credits
   - Verify internet connection
   - Try reducing image count or quality

3. **"Image too large"**
   - Node automatically resizes, but very large images may fail
   - Try using smaller reference images
   - Recommended max: 2048x2048px

4. **Connection errors**
   - Check firewall/proxy settings
   - Verify Ideogram API is accessible
   - Try increasing timeout in advanced settings

### Debug Mode

Enable logging to see detailed information:
```python
import logging
logging.basicConfig(level=logging.INFO)
```

## 📄 License

MIT License - see LICENSE file for details

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 🙏 Credits

- Ideogram for their amazing API
- ComfyUI community for the framework
- Contributors and testers

## 📞 Support

- **Issues**: Open an issue on GitHub
- **Discussions**: Use GitHub Discussions for questions
- **API Support**: Contact Ideogram support for API issues

## 🔄 Version History

### v1.0.1 (Current Release)
- Fixed character mask input (removed - not needed for Generate API)
- Character reference support with Ideogram API v3
- 15 preset aspect ratios for flexible output sizes
- 5 style types: Auto, General, Realistic, Design, Fiction
- 3 render speeds: Turbo, Default, Quality
- Batch generation (1-4 images)
- Comprehensive security features
- Production-ready with error handling

## 🔗 Links

- [Ideogram Website](https://ideogram.ai)
- [Ideogram API Documentation](https://developer.ideogram.ai)
- [ComfyUI GitHub](https://github.com/comfyanonymous/ComfyUI)
- [Report Issues](https://github.com/DesertPixelAI/ComfyUI-DP-Ideogram-Character/issues)

---


Made with ❤️ for the ComfyUI community



