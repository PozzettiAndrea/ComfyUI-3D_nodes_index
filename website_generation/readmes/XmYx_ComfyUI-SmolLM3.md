# 🪄 ComfyUI-SmolLM3 ✨

![SmolLM3 Banner](https://img.shields.io/badge/SmolLM3-ComfyUI-purple?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTggMEw5LjA5IDQuNjNMMTQgNS4yNEwxMSA4LjE3TDExLjY4IDEzTDggMTAuNjNMNC4zMiAxM0w1IDguMTdMMiA1LjI0TDYuOTEgNC42M0w4IDBaIiBmaWxsPSIjRkZGIi8+Cjwvc3ZnPg==)
![License](https://img.shields.io/github/license/XmYx/ComfyUI-SmolLM3?style=flat-square&color=blue)
![Stars](https://img.shields.io/github/stars/XmYx/ComfyUI-SmolLM3?style=flat-square&color=yellow)

> *"Small models, big dreams, infinite possibilities"* 🌟

Welcome to **ComfyUI-SmolLM3**, where we bring the magic of Hugging Face's SmolLM3 language models into your ComfyUI workflow! Whether you're crafting stories, generating ideas, or building AI-powered creativity tools, this node pack makes it delightfully simple.

Created with 💜 by [XmYx](https://github.com/XmYx) - bringing a touch of magic to the AI animation and VFX community!

## ✨ Features

- 🎯 **Simple & Intuitive** - Just load and generate! No complex setups required
- 🚀 **Dual Model Support** - Choose between base and instruct models
- 🎨 **Flexible Generation** - From simple completions to full chat conversations
- ⚡ **Optimized Performance** - Support for fp16, fp32, and bf16 precision
- 🎲 **Reproducible Results** - Seed support for consistent outputs
- 🌈 **ComfyUI Native** - Seamlessly integrates with your existing workflows

## 🎬 What's Inside

### 🔮 Three Magical Nodes

1. **SmolLM3 Model Loader** - Your gateway to loading the models
2. **SmolLM3 Sampler (Chat)** - Full-featured chat generation with all the bells and whistles
3. **SmolLM3 Simple Generate** - Quick and easy text completion

## 🚀 Installation

1. Navigate to your ComfyUI custom nodes folder:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/XmYx/ComfyUI-SmolLM3.git
   ```

3. Install the required dependencies:
   ```bash
   cd ComfyUI-SmolLM3
   pip install -r requirements.txt
   ```

4. Restart ComfyUI and let the magic begin! ✨

## 📖 Usage

### Basic Workflow

1. Add a **SmolLM3 Model Loader** node
2. Select your preferred model:
   - `HuggingFaceTB/SmolLM3-3B-Base` - For general text generation
   - `HuggingFaceTB/SmolLM3-3B` - For chat and instruction following
3. Connect to either:
   - **SmolLM3 Sampler** for chat-style interactions
   - **SmolLM3 Simple Generate** for basic completions
4. Set your prompt and parameters
5. Generate! 🎉

### 🎯 Pro Tips

- 🌡️ Use **temperature = 0.6** and **top_p = 0.95** for best results (as recommended by the SmolLM3 team)
- 🎲 Set a **seed** for reproducible outputs
- 💬 Enable **chat template** for conversational AI
- 🖥️ Choose **CPU** mode if you're running on limited GPU memory

## 🌟 Example Prompts

```
"Give me a brief explanation of gravity in simple terms."
"Write a haiku about artificial intelligence."
"What are three creative uses for a paperclip?"
"Continue this story: Once upon a time in a digital realm..."
```

## 🤝 Contributing

Found a bug? Have an idea? Want to add more sparkle? ✨

Contributions are warmly welcomed! Feel free to:
- 🐛 Report issues
- 💡 Suggest features
- 🔧 Submit pull requests
- ⭐ Star the repo if you find it useful!

## 🎨 About the Creator

This node pack is crafted with love by [XmYx (Miklos Nagy)](https://github.com/XmYx), a human, artist and ML enthusiast who believes in making AI tools accessible and fun for creators. Check out my other projects:

- 🎬 [Deforum ComfyUI Nodes](https://github.com/XmYx/deforum-comfy-nodes)
- 🎯 [magixworld](http://magixworld.com)

## 📜 License

This project is licensed under the MIT License - because sharing is caring! 💝

## 🙏 Acknowledgments

- The amazing [Hugging Face](https://huggingface.co/) team for SmolLM3
- The [ComfyUI](https://github.com/comfyanonymous/ComfyUI) community for the incredible platform
- You, for being part of this creative journey! 🌟

---

<p align="center">
  Made with 💜 and a sprinkle of ✨ by the AI creative community
</p>

<p align="center">
  <i>"In a world of large models, sometimes the smallest ones cast the biggest spells"</i> 🪄
</p>
