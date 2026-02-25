# ComfyUI-PromptsO

**Version: 1.1.1**

A comprehensive AI API integration and prompt processing toolkit for ComfyUI, providing powerful text and image generation capabilities with advanced prompt manipulation tools.

## 📝 Update Log

### Version 1.1.1
- **Bug Fix**: Fixed **💀Prompts Split** node newline delimiter not working correctly
  - Resolved issue where selecting "Newline" as delimiter failed to split text by line breaks
  - Text can now be properly split using newline characters

## 🚀 Features

### AI API Integration
- **💀Image with Gemini** - Generate images using Google Gemini API with your own API key
- **💀Image with Grok** - Generate images using Grok AI API with your own API key
- **💀Text with Deepseek** - Generate text using Deepseek AI API with your own API key
- **💀Text with Gemini** - Generate text using Google Gemini API with your own API key
- **💀Text with OpenAI** - Generate text using OpenAI GPT API with your own API key
- **💀Text with Grok** - Generate text using Grok AI API with your own API key

### Prompt Processing Tools
- **💀Prompts Combine** - Merge multiple prompts with customizable separators
- **💀Prompts Input** - Advanced prompt input with multiline support
- **💀Prompts Split** - Split prompts by delimiters into separate outputs
- **💀Prompts Replace** - Replace text patterns using regex or simple text matching
- **💀Prompts from Janus Pro** - Extract and process prompts from Janus Pro model

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "PromptsO" or "S4MUEL"
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation
1. Navigate to your ComfyUI custom_nodes directory:
   ```
   cd ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```
   git clone https://github.com/S4MUEL-404/ComfyUI-PromptsO.git
   ```
3. Install dependencies:
   ```
   pip install -r ComfyUI-PromptsO/requirements.txt
   ```
4. Restart ComfyUI

## 🔧 Dependencies

The plugin automatically manages its dependencies:
- **Pillow** (PIL) - Image processing
- **NumPy** - Numerical operations
- **Requests** - API communications
- **Torch** - Deep learning operations
- **Transformers** - AI model handling
- **Additional AI libraries** - Advanced API integrations

## 📖 Usage

### AI API Nodes

#### Image Generation:
1. **Find Nodes**: All nodes are prefixed with 💀 in the ComfyUI node browser
2. **Categories**: Look under "💀S4PromptsO" category
3. **API Keys**: Enter your own API keys for full control and privacy
4. **Configuration**: Each node provides specific parameters for optimal results

#### Text Generation:
1. Add any text generation node to your workflow
2. Enter your API key and prompt
3. Configure parameters like temperature, max tokens, etc.
4. Execute workflow to generate text

### Prompt Processing Nodes

#### Combining Prompts:
- Use **💀Prompts Combine** to merge multiple prompt inputs
- Customize separators and formatting
- Perfect for complex multi-part prompts

#### Splitting Prompts:
- Use **💀Prompts Split** to divide prompts by delimiters
- Useful for batch processing or multi-output workflows
- Supports custom delimiter patterns

#### Text Replacement:
- Use **💀Prompts Replace** for pattern matching and replacement
- Supports both regex and simple text matching
- Essential for dynamic prompt modification

## 🎯 Key Features

- ✅ **Multiple AI APIs** - Support for major AI providers with your own keys
- ✅ **Privacy Focused** - No data stored, direct API communication
- ✅ **Advanced Prompting** - Comprehensive prompt manipulation tools
- ✅ **Production Quality** - Enterprise-grade error handling and logging
- ✅ **Flexible Integration** - Compatible with existing ComfyUI workflows
- ✅ **Cost Control** - Use your own API keys for transparent billing

## 📁 Project Structure

```
ComfyUI-PromptsO/
├── py/                 # Core node implementations
│   ├── imageGemini.py  # Gemini image generation
│   ├── imageGrok.py    # Grok image generation
│   ├── textDeepseek.py # Deepseek text generation
│   ├── textGemini.py   # Gemini text generation
│   ├── textOpenAI.py   # OpenAI text generation
│   ├── textGrok.py     # Grok text generation
│   ├── promptsCombine.py    # Prompt combination
│   ├── promptsInput.py      # Advanced prompt input
│   ├── promptsSplit.py      # Prompt splitting
│   ├── promptsReplace.py    # Text replacement
│   └── promptsFromJanusPro.py # Janus Pro integration
├── cache/              # API response cache
├── summary_md/         # Development documentation
├── __init__.py         # Plugin initialization
├── s4_logger.py        # Logging system
└── requirements.txt    # Python dependencies
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or report issues.

## 📜 License

This project is open source. Please respect the licensing terms.

---

**Author:** S4MUEL  
**Website:** [s4muel.com](https://s4muel.com)  
**GitHub:** [https://github.com/S4MUEL-404/ComfyUI-PromptsO](https://github.com/S4MUEL-404/ComfyUI-PromptsO)
