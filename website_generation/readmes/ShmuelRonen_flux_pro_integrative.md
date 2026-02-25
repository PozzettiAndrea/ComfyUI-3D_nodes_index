# ComfyUI Flux Pro Integrative - Enhanced Flux API Node

## Support My Work
If you find this project helpful, consider buying me a coffee:

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=shmuelronen&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/shmuelronen)

A completely rewritten and enhanced custom node for ComfyUI that integrates with [Black Forest Labs](https://blackforestlabs.ai/) FLUX API, providing seamless access to FLUX's image generation and finetuning capabilities with improved reliability and user experience.

<img width="1295" height="826" alt="image" src="https://github.com/user-attachments/assets/a5d41d30-da67-426f-93f3-ee5ac18b1d94" />



## ✨ What's New in v2.0

**Complete Rewrite with Modern Architecture:**
- 🏗️ **Modular Design**: Separated concerns with dedicated classes for configuration, API handling, and node logic
- 🛡️ **Robust Error Handling**: Custom exception handling with detailed error messages and graceful fallbacks
- 🔧 **Smart Configuration**: Automatically searches multiple locations for config files with clear setup instructions
- 📝 **Enhanced Logging**: Detailed console output for better debugging and monitoring
- 🎨 **Better UX**: Improved tooltips, organized parameters, and clearer status information
- 🚀 **Modern ComfyUI**: Full compatibility with latest ComfyUI versions using modern node patterns

## 🌟 Features

**Core Image Generation:**
- Support for FLUX 1.1 Pro regular and Ultra modes
- Optional Raw mode for more natural-looking images
- Multiple aspect ratios (21:9, 16:9, 4:3, 1:1, 3:4, 9:16, 9:21)
- Configurable safety tolerance (0-6 scale)
- Support for both JPEG and PNG output formats
- Seed support for reproducible results

**Advanced Finetuning System:**
- Complete finetuning workflow integration
- Model customization with multiple training modes
- Training mode selection (character/product/style/general)
- Inference with adjustable strength control
- Support for both full and LoRA finetuning
- Comprehensive parameter control

**Reliability & Usability:**
- Intelligent retry logic with exponential backoff
- Graceful error handling with informative messages
- Automatic config file discovery
- Session-based HTTP requests for better performance
- Detailed progress reporting and status updates

## 📋 Requirements

- ComfyUI (latest version recommended)
- Black Forest Labs API key
- Python packages (auto-installed with ComfyUI):
  - requests
  - Pillow (PIL)
  - numpy
  - torch

## 🚀 Installation

1. **Create the node directory:**
   ```
   ComfyUI/custom_nodes/flux_pro_integrative/
   ```

2. **Download the files:**
   - `__init__.py`
   - `flux_pro_integrative.py`
   - `config.ini` (template)

3. **Set up your API key:**
   
   Create or edit `config.ini` in the node directory:
   ```ini
   [API]
   X_KEY=your_actual_api_key_here
   ```

4. **Restart ComfyUI**

The node will automatically appear as "🎨 Flux Pro Integrative" in the **BFL/Flux Pro** category.

## 🔑 Getting Your API Key

1. **Create Account**: Visit [Black Forest Labs API Portal](https://api.us1.bfl.ai/auth/login)
2. **Generate Key**: Access your dashboard and create a new API key
3. **Add to Config**: Copy the key to your `config.ini` file

**Useful Links:**
- Main Website: [Black Forest Labs](https://blackforestlabs.ai/)
- API Documentation: [BFL API Docs](https://docs.bfl.ai/)

## 💰 Pricing (Current Rates)

### Image Generation
- **FLUX 1.1 Pro Ultra**: $0.06 per image - Best for photo-realistic images at 2K+ resolution
- **FLUX 1.1 Pro Ultra Finetuned**: $0.07 per image - Using your custom models
- **FLUX 1.1 Pro**: $0.04 per image - Efficient for large-scale generation
- **FLUX.1 Pro**: $0.05 per image - Original pro model
- **FLUX.1 Dev**: $0.025 per image - Distilled model for development

### Finetuning Training
- **Short** ($2): < 150 steps - Quick exploration and testing
- **Medium** ($4): 150-500 steps - Standard use cases
- **Long** ($6): > 500 steps - Complex tasks requiring precision

## 🎛️ Node Interface

### Core Parameters

**Mode Selection:**
- `generate`: Create new images from prompts
- `finetune`: Train custom models on your data
- `inference`: Generate images using trained models

**Generation Settings:**
- `prompt`: Text description of desired image (supports multiline)
- `ultra_mode`: Enable Ultra mode for higher quality (default: True)
- `aspect_ratio`: Choose from 7 ratios (default: 16:9)
- `safety_tolerance`: Content filter strength 0-6 (default: 6)
- `output_format`: PNG or JPEG output
- `raw`: Skip safety filters for natural results (Ultra only)
- `seed`: Set specific seed for reproducibility (-1 for random)

### Finetuning Parameters

**Training Setup:**
- `finetune_zip`: Path to training data ZIP file
- `finetune_comment`: Description of your model (required)
- `trigger_word`: Word to activate your concept (default: "TOK")
- `finetune_mode`: Training type (character/product/style/general)

**Advanced Training:**
- `iterations`: Training steps (100-2000, default: 300)
- `learning_rate`: Training rate (default: 0.00001)
- `captioning`: Auto-generate image descriptions (default: True)
- `priority`: Training priority (speed/quality)
- `finetune_type`: Full model or LoRA training
- `lora_rank`: LoRA complexity (8-128, default: 32)

**Inference Settings:**
- `finetune_id`: ID of your trained model
- `finetune_strength`: Effect intensity (0.1-2.0, default: 1.2)

## 📖 Usage Guide

### Basic Image Generation

1. Add "🎨 Flux Pro Integrative" node to workflow
2. Set mode to "generate"
3. Enter your prompt
4. Configure settings (aspect ratio, safety, etc.)
5. Connect to Preview Image node

**Example prompt:**
```
A majestic mountain landscape at sunset, golden hour lighting, 
photorealistic, highly detailed, dramatic clouds
```

### Training Custom Models

**Step 1: Prepare Training Data**
- Collect 5-20 high-quality images (JPG, PNG, WebP)
- Optionally add `.txt` files with descriptions
- Create ZIP file with all training data

**Step 2: Start Training**
- Set mode to "finetune"
- Provide ZIP file path
- Set descriptive comment
- Choose appropriate finetune_mode:
  - `character`: For people, fictional characters
  - `product`: For objects, items, brands
  - `style`: For artistic styles, aesthetics
  - `general`: For concepts, scenes, general use

**Step 3: Monitor Training**
- Node returns finetune ID
- Training happens on BFL servers
- Check status via API portal

### Using Trained Models

1. Set mode to "inference"
2. Enter your finetune_id
3. Include trigger_word in prompt
4. Adjust finetune_strength as needed

**Example inference prompt:**
```
TOK character wearing a red dress in a garden, 
professional photography, portrait
```

## 🎯 Best Practices

### Finetuning Success Tips

**Image Quality:**
- Use high-resolution, clear images (1024px+ recommended)
- Ensure consistent lighting and quality
- Avoid blurry or heavily compressed images

**Training Data:**
- For characters: Single person per image, various poses/angles
- For products: Different angles, lighting conditions
- For styles: Consistent artistic elements across images

**Parameter Tuning:**
- Start with default settings
- Increase iterations for complex concepts (500-1000)
- Adjust finetune_strength during inference:
  - 0.8-1.0: Subtle influence
  - 1.2-1.5: Strong effect (default range)
  - 1.6-2.0: Very strong (may cause artifacts)

### Generation Optimization

**Prompt Engineering:**
- Be specific and descriptive
- Include style keywords (photorealistic, artistic, etc.)
- Mention lighting, composition, quality descriptors

**Technical Settings:**
- Use Raw mode for photorealistic content
- Higher safety_tolerance for creative freedom
- PNG for detailed images, JPEG for photography

## 🔧 Troubleshooting

### Common Issues

**"Node not properly initialized"**
- Check if `config.ini` exists in node directory
- Verify API key format: `X_KEY=your_key` under `[API]` section
- Ensure no extra spaces around the API key

**"Config file not found"**
The node searches these locations:
1. `ComfyUI/custom_nodes/flux_pro_integrative/config.ini`
2. `ComfyUI/config.ini`
3. Current working directory

**API Errors**
- `HTTP 401`: Invalid or expired API key
- `HTTP 429`: Rate limiting (wait and retry)
- `HTTP 500`: Server error (retry later)

**Network Issues**
- Check internet connection
- Verify firewall/proxy settings
- Try again after a few minutes

### Error Recovery

The node includes comprehensive error handling:
- Returns blank image with error message on failure
- Automatic retry logic for transient errors
- Detailed console logging for debugging
- Graceful degradation when services unavailable

## 🏗️ Technical Architecture

### Class Structure

- **`ConfigManager`**: Handles configuration loading and validation
- **`FluxAPIClient`**: Manages all API interactions with robust error handling
- **`FluxProIntegrative`**: Main ComfyUI node class with user interface
- **`FluxAPIError`**: Custom exception for API-related errors

### Key Improvements

- **Session Management**: Reuses HTTP connections for better performance
- **Smart Retries**: Exponential backoff for failed requests
- **Type Safety**: Full type hints for better code reliability
- **Modular Design**: Easy to extend and maintain

## 🤝 Contributing

Contributions are welcome! Please feel free to submit:
- Bug reports with detailed reproduction steps
- Feature requests with use case descriptions
- Code improvements via pull requests
- Documentation enhancements

## 📝 Changelog

### v2.0.0 (Current)
- Complete architectural rewrite with modular design
- **NEW**: GUI API key input field for easy configuration
- **NEW**: Hybrid API key support (GUI overrides config file)
- Enhanced error handling and user experience
- Modern ComfyUI compatibility
- Improved configuration management with flexible options
- Better logging and debugging tools
- More robust network error handling

### v1.0.0 (Legacy)
- Initial release with basic API integration

## 🙏 Acknowledgements

- **Black Forest Labs** for their powerful FLUX API
- **ComfyUI Community** for the excellent node framework
- **Contributors** who help improve this project

---

**Note**: This node requires an active Black Forest Labs API subscription. Please review their pricing and terms of service before use.
