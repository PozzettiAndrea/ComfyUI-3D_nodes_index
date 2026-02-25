# 🍌 ComfyUI-BananaForge

> **Gemini-Powered Image Generation for ComfyUI**  
> Text-to-Image, Image-to-Image, and Batch Processing

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- 🎨 **Text → Image**: Generate images from text prompts
- 🖼️ **Image → Image**: Edit, transform, and style transfer
- 📦 **Batch Processing**: Multiple prompts → multiple images
- ⏱️ **Rate Limit Handling**: Built-in wait timers
- 🔑 **Flexible API Config**: Direct key or .env file

---

## 📥 Installation

### ComfyUI Manager (Recommended)
Search for **"BananaForge"** in ComfyUI Manager and install.

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/peter119lee/ComfyUI-BananaForge.git
pip install -r ComfyUI-BananaForge/requirements.txt
```

Restart ComfyUI after installation.

---

## 🚀 Quick Start

1. **Get an API Key** from [Google AI Studio](https://aistudio.google.com/apikey)
2. Find nodes under **"Banana Forge"** category in ComfyUI
3. Paste your API key
4. Enter a prompt and run!

---

## 📋 Nodes Overview

### 🍌 BananaForge Text → Image

**Purpose**: Generate NEW images from text descriptions.

| Input | Description |
|-------|-------------|
| `api_key` | Your Gemini API key |
| `model_name` | Default: `gemini-3-pro-image-preview` |
| `prompt` | Text description of desired image |
| `aspect_ratio` | 1:1, 16:9, 9:16, 4:3, 3:4 |
| `image_size` | default, 2K, 4K |
| `wait_seconds` | Delay before API call (rate limit protection) |

**Output**: Single image

---

### 🖼️ BananaForge Image → Image

**Purpose**: Edit or transform existing images.

| Input | Description |
|-------|-------------|
| `image_1` | Primary input image (required) |
| `image_2` to `image_6` | Additional reference images (optional) |
| `prompt` | Editing instructions |
| `match_input_aspect` | Auto-match output to input image ratio |

**Output**: Edited image

**Use Cases**:
- Style transfer
- Image editing
- Character consistency (multiple refs)
- Image fusion

---

### 🍌 BananaForge Batch

**Purpose**: Generate multiple images from multiple prompts.

| Input | Description |
|-------|-------------|
| `prompts` | One prompt per line (multi-line text) |
| `reference_image` | Optional: for batch i2i mode |
| `wait_between` | Seconds between API calls (default: 2s) |

**Output**: 
- `IMAGES`: Batch tensor (all generated images)
- `COUNT`: Number of successful generations

**Example Prompts**:
```
A girl sitting on a chair
A girl eating an apple
A girl standing by the window
```
→ Generates **3 separate images**

---

## ⚙️ Configuration

### Option 1: Direct API Key
Paste your key directly in the `api_key` field.

### Option 2: Environment File (.env)
```bash
cp .env.example .env
```

Edit `.env`:
```
API_KEY=your_api_key_here
API_URL=https://generativelanguage.googleapis.com/v1beta
```

Set `use_env_file` to `yes` in the node.

---

## 🎯 Supported Models

| Model | Max Images | Sizes | Notes |
|-------|------------|-------|-------|
| `gemini-2.5-flash-image` | 3 | default | Fast, free tier friendly |
| `gemini-3-pro-image-preview` | 14 | 2K, 4K | Best quality, supports larger sizes |

---

## 💡 Tips

### Avoid Rate Limits
- Use `wait_seconds` (single nodes) or `wait_between` (batch)
- Recommended: 2-5 seconds between calls

### Better Results
- Be specific in prompts
- For i2i: describe desired changes clearly
- For batch: each line is separate, be complete in each

### Third-Party APIs
Works with OpenAI-compatible APIs. Just change `api_url` to your provider.

---

## 🐛 Troubleshooting

| Error | Solution |
|-------|----------|
| "API key cannot be empty" | Add your key or check .env file |
| "Content blocked" | Modify prompt (safety filters) |
| Rate limit errors | Increase `wait_seconds` |
| No image in response | Check model name and API compatibility |

---

## 📝 License

MIT License

---

## 🙏 Credits

- Built for [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- Powered by [Google Gemini API](https://ai.google.dev/)
