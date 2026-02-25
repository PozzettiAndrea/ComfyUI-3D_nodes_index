# ComfyUI Google AI Studio Integration

A comprehensive ComfyUI plugin that integrates Google AI Studio's powerful AI models for content generation, image creation, video planning, and advanced prompt optimization.

## 🌟 Features

### 🤖 AI-Powered Content Generation
- **Image Generation**: Create detailed image descriptions using Gemini models
- **Video Planning**: Generate comprehensive video storyboards and scene breakdowns
- **Prompt Optimization**: Advanced prompt enhancement using AI-powered analysis

### 🔧 Technical Capabilities
- **Multiple Models**: Support for Gemini 2.5 Flash, Pro, and 1.5 models
- **Async Processing**: Non-blocking operations for better performance
- **Rate Limiting**: Built-in API rate limit management
- **Error Handling**: Comprehensive error recovery and reporting

### 🎨 Available Nodes

#### Image Generation Nodes
- **🤖 Google AI Image Generator**: Basic image description generation
- **🎨 Google AI Text to Image**: Enhanced text-to-image with style controls

#### Video Generation Nodes
- **🎬 Google AI Video Generator**: Video description and planning
- **📋 Google AI Video Storyboard**: Detailed storyboard creation with scene breakdowns

#### Prompt Tools
- **✨ Prompt Optimizer**: AI-powered prompt enhancement and optimization
- **🔍 Prompt Analyzer**: Detailed prompt structure analysis and scoring

## 🚀 Installation

### Method 1: Automatic Installation
1. Clone or download this repository to your ComfyUI `custom_nodes` directory
2. Run the installation script:
```bash
cd ComfyUI/custom_nodes/ComfyUI-GoogleAIStudio
python install.py
```

### Method 2: Manual Installation
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your API key (see Setup section below)
3. Restart ComfyUI

## ⚙️ Setup

### 1. Get Google AI Studio API Key
1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a new API key
3. Copy the generated key

### 2. Configure API Key

**Option A: Environment Variable (Recommended)**
```bash
# Linux/Mac
export GOOGLE_API_KEY='your-api-key-here'

# Windows
set GOOGLE_API_KEY=your-api-key-here
```

**Option B: Direct Input**
- Use the `api_key` input field in each node

### 3. Restart ComfyUI
After installation and configuration, restart ComfyUI to load the new nodes.

## 📖 Usage Guide

### Basic Workflow

1. **Add a Google AI node** to your workflow
2. **Set your prompt** in the text field
3. **Choose a model**:
   - `gemini-2.5-flash`: Fast, efficient for most tasks
   - `gemini-2.5-pro`: Higher quality for complex creative tasks
   - `gemini-1.5-flash`: Legacy model, faster inference
4. **Adjust parameters** like temperature, max tokens
5. **Execute** the workflow

### Prompt Optimization Workflow

1. Add **Prompt Analyzer** to analyze your current prompt
2. Use **Prompt Optimizer** to enhance the prompt
3. Connect optimized prompt to generation nodes
4. Compare results and iterate

### Video Storyboard Workflow

1. Use **Google AI Video Storyboard** for initial concept
2. Connect to **Google AI Video Generator** for detailed descriptions
3. Export results for further processing

## 🎛️ Node Parameters

### Common Parameters
- **prompt**: Main text input for generation
- **model**: Choose from available Gemini models
- **temperature**: Controls creativity (0.0-1.0)
- **max_tokens**: Maximum response length
- **api_key**: Optional API key override

### Image Generation Specific
- **style**: Artistic style (photorealistic, artistic, cinematic, etc.)
- **quality**: Output quality level
- **aspect_ratio**: Image aspect ratio
- **negative_prompt**: Elements to avoid

### Video Generation Specific
- **duration**: Video length in seconds
- **fps**: Target frame rate
- **resolution**: Output resolution (720p, 1080p, 4K)
- **style**: Video style (cinematic, documentary, artistic)

### Prompt Optimization Specific
- **enhancement_type**: Type of enhancement (general, photography, artistic, etc.)
- **target_model**: Model to optimize for
- **iterations**: Number of optimization rounds

## 🔧 Advanced Configuration

### Rate Limiting
The plugin automatically handles API rate limits:
- **Free Tier**: 15 RPM (Requests Per Minute)
- **Paid Tier**: Higher limits based on billing tier

### Model Selection Guide
- **Gemini 2.5 Flash**: Best for general use, fast responses
- **Gemini 2.5 Pro**: Best for complex creative tasks, higher quality
- **Gemini 1.5 Flash**: Legacy option, good for simple tasks

### Error Handling
The plugin includes comprehensive error handling:
- API key validation
- Network error recovery
- Rate limit management
- Graceful degradation

## 🛠️ Troubleshooting

### Common Issues

**"API key required" error**
- Ensure GOOGLE_API_KEY environment variable is set
- Or provide api_key in node inputs
- Restart ComfyUI after setting environment variable

**"Rate limited" error**
- Wait for the rate limit period to reset
- Consider upgrading to paid API tier
- Use lower frequency for batch operations

**Import errors**
- Run `pip install -r requirements.txt`
- Ensure all dependencies are installed
- Check Python environment compatibility

**Nodes not appearing**
- Restart ComfyUI completely
- Check console for error messages
- Verify plugin is in correct custom_nodes directory

### Debug Mode
Enable debug logging by setting:
```python
logging.basicConfig(level=logging.DEBUG)
```

## 📝 API Usage and Costs

### Token Usage
- **Text Generation**: ~4 characters per token
- **Image Descriptions**: 100-2000 tokens typically
- **Video Storyboards**: 1000-4000 tokens typically

### Cost Optimization Tips
1. Use specific, concise prompts
2. Choose appropriate model for task complexity
3. Monitor token usage in generation info
4. Use caching for repeated operations

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Test thoroughly
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google AI Studio for providing the API
- ComfyUI community for the excellent platform
- All contributors and testers

## 🔗 Links

- [Google AI Studio](https://aistudio.google.com/)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [Plugin Documentation](https://github.com/your-repo/docs)

---

**Made with ❤️ by 浮浮酱 ฅ'ω'ฅ**

*Professional engineering meets feline charm!*# -ComfyUI-GoogleAIStudio
