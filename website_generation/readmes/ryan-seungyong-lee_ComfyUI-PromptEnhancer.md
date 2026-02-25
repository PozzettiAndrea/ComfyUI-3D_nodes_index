# ComfyUI-PromptEnhancer

ComfyUI custom nodes for **Hunyuan PromptEnhancer** - Enhance your text-to-image prompts and image editing instructions with AI-powered prompt rewriting.

<p align="center">
  <img src="assets/teaser.png" alt="ComfyUI PromptEnhancer Teaser" width="800">
</p>

<p align="center">
  <a href="https://github.com/Hunyuan-PromptEnhancer/PromptEnhancer"><img src="https://img.shields.io/badge/Original%20Repo-PromptEnhancer-blue?logo=github" alt="Original Repo"></a>
  <a href="https://www.arxiv.org/abs/2509.04545"><img src="https://img.shields.io/badge/Paper-arXiv:2509.04545-red?logo=arxiv" alt="arXiv"></a>
  <a href="https://huggingface.co/tencent/HunyuanImage-2.1/tree/main/reprompt"><img src="https://img.shields.io/badge/Model-PromptEnhancer_7B-blue?logo=huggingface" alt="HuggingFace Model"></a>
</p>

## 🌟 Features

- **🎨 Text-to-Image Prompt Enhancement**: Transform simple prompts into detailed, well-structured descriptions
- **🖼️ Image-to-Image Editing Enhancement**: Enhance editing instructions while preserving non-edited regions
- **🤖 Automatic Model Download**: Models are automatically downloaded from HuggingFace when first used
- **🌐 Multi-language Support**: Works with both Chinese and English prompts

## 📦 Installation

### ⚠️ Important: Install flash-attn (Required for Image-to-Image)

> **Note**: This is not required for Text-to-Image Prompt Enhancement (7B).

The **Image-to-Image Prompt Enhancer** node requires `flash-attn`. Install it first:

```bash
pip install flash-attn --no-build-isolation
```


---

### Method 1: ComfyUI Manager (Recommended)

1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
2. In ComfyUI, go to `Manager` → `Install Custom Nodes`
3. Search for "PromptEnhancer"
4. Click `Install` and restart ComfyUI

### Method 2: Git Clone

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/ryan-seungyong-lee/ComfyUI-PromptEnhancer.git
cd ComfyUI-PromptEnhancer
pip install -r requirements.txt
```

### Method 3: Manual Installation

1. Download this repository as ZIP
2. Extract to `ComfyUI/custom_nodes/ComfyUI-PromptEnhancer/`
3. Install dependencies:
```bash
cd ComfyUI/custom_nodes/ComfyUI-PromptEnhancer
pip install -r requirements.txt
```

## 🚀 Quick Start

### Available Nodes

#### 1. **Prompt Enhancer (Text-to-Image)**
Enhances text prompts for better image generation results.

**Inputs:**
- `prompt`: Your original prompt (text)
- `model_name`: Choose between "promptenhancer-7b" (default, faster) or "promptenhancer-32b" (higher quality)
- `temperature`: Sampling temperature (0 = deterministic, higher = more creative)
- `top_p`: Nucleus sampling parameter
- `max_new_tokens`: Maximum length of enhanced prompt
- `system_prompt` (optional): Custom system prompt for specialized use cases

**Output:**
- `enhanced_prompt`: Enhanced, detailed prompt ready for image generation

#### 2. **Prompt Enhancer (Image-to-Image)**
Enhances image editing instructions based on visual context.

**Inputs:**
- `image`: Input image to edit
- `edit_instruction`: Your editing instruction (text)
- `temperature`: Sampling temperature
- `top_p`: Nucleus sampling parameter
- `max_new_tokens`: Maximum length of enhanced instruction
- `system_prompt` (optional): Custom system prompt

**Output:**
- `enhanced_prompt`: Enhanced editing instruction preserving non-edited regions


## 📥 Model Downloads

Models are automatically downloaded on first use and cached in `ComfyUI/models/prompt_enhancer/`.

| Model | Size | Quality | Download Time* | Best For |
|-------|------|---------|---------------|----------|
| **promptenhancer-7b** | ~13GB | High | ~15 min | Most users, balanced performance |
| **promptenhancer-32b** | ~64GB | Highest | ~60 min | Maximum quality, requires 32GB+ VRAM |
| **promptenhancer-img2img** | ~30GB | High | ~30 min | Image editing tasks |

*Approximate times on a 100Mbps connection

### Manual Download (Optional)

If you prefer to download models manually:

```bash
# For Text-to-Image (7B model)
huggingface-cli download tencent/HunyuanImage-2.1 --include "reprompt/*" --local-dir ComfyUI/models/prompt_enhancer/promptenhancer-7b

# For Text-to-Image (32B model)
huggingface-cli download PromptEnhancer/PromptEnhancer-32B --local-dir ComfyUI/models/prompt_enhancer/promptenhancer-32b

# For Image-to-Image
huggingface-cli download PromptEnhancer/PromptEnhancer-Img2img-Edit --local-dir ComfyUI/models/prompt_enhancer/promptenhancer-img2img
```

## 🎯 Usage Examples

### Example Workflow

Check out the example workflow to get started quickly:

<p align="center">
  <img src="workflow_examples/hunyuan_prompt_enhancer_t2i.png" alt="Text-to-Image Workflow Example" width="800">
</p>

**How to use:**
1. Download the workflow image above
2. Open ComfyUI
3. Drag and drop the image into the ComfyUI canvas
4. The workflow will be automatically loaded with all nodes configured

### Example 1: Basic Text Prompt Enhancement

**Input:**
```
"a cat"
```

**Enhanced Output:**
```
"A photorealistic portrait of a domestic cat with soft fur, sitting elegantly on a wooden surface. 
The cat has bright, alert eyes and pointed ears, with whiskers clearly visible. The composition 
focuses on the feline subject with natural lighting creating subtle shadows. The background is 
gently blurred to emphasize the cat. High-quality digital photography style."
```

### Example 2: Gaming Scene Enhancement

**Input (Chinese):**
```
"第三人称视角，赛车在城市赛道上飞驰"
```

**Enhanced Output:**
```
"第三人称视角游戏画面，一辆流线型赛车正在繁华的城市赛道上高速飞驰。左上角显示小地图，
标注当前位置和赛道布局，地图下方实时显示当前排名。右下角的仪表盘清晰展示速度表，
指针指向高速区域。赛道两旁是现代化的城市建筑群，具有动态模糊效果增强速度感。
画面采用动态追踪镜头，呈现竞速游戏的紧张氛围和高画质视觉效果。"
```

### Example 3: Image Editing Enhancement

**Input Image:** [Image with watermark]
**Instruction:**
```
"去除图片中的水印"
```

**Enhanced Output:**
```
"保持画面中的主体内容、构图和色调完全不变，仅将图片底部的文字水印或logo标识完整移除。
使用智能修复技术填补去除水印后的区域，确保过渡自然无痕迹。其余所有元素包括前景、
背景、光影效果、人物或物体的位置、大小、颜色均保持原样。"
```

## ⚙️ Advanced Configuration

### Custom System Prompts

You can provide custom system prompts for specialized use cases:

**For Anime Style:**
```python
system_prompt = """你是一位专注于动漫风格图像提示词的专家。
请将用户输入改写为适合动漫风格图像生成的提示词，
注重角色特征、动漫画风特点和典型的视觉元素。"""
```

**For Photography:**
```python
system_prompt = """You are an expert in photography prompt writing.
Rewrite the user's input into a detailed photography prompt,
including camera settings, lighting, composition, and style."""
```

### Parameter Tuning Guide

- **temperature = 0**: Deterministic output (recommended for consistency)
- **temperature = 0.7**: Balanced creativity and consistency (recommended default)
- **temperature = 1.0+**: More creative variations (may lose some intent)

- **top_p = 0.9**: Standard nucleus sampling (recommended)
- **top_p = 1.0**: Consider all tokens (more diverse but less focused)

- **max_new_tokens**: 
  - 256-512: Short, concise enhancements
  - 512-1024: Standard detailed descriptions (recommended)
  - 1024-2048: Very detailed, structured prompts

## 🔧 Troubleshooting

### Issue: Model download fails

**Solution:**
- Check your internet connection
- Check HuggingFace Authentication (`hf auth login` or `huggingface-cli login`)
- Ensure you have enough disk space (7B model needs ~15GB free)
- Try manual download using `huggingface-cli` (see Manual Download section)

### Issue: Out of memory error

**Solution:**
- Use the 7B model instead of 32B
- Close other applications to free up VRAM
- If using CPU, reduce `max_new_tokens` parameter

### Issue: Node doesn't appear in ComfyUI

**Solution:**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Restart ComfyUI completely
- Check the console for error messages

### Issue: Slow inference

**Solution:**
- First run is slower due to model loading (subsequent runs use cached model)
- Use the 7B model for faster inference
- Reduce `max_new_tokens` if you don't need very long prompts
- Ensure you have adequate VRAM (recommended 8GB+ for 7B model)

## 📊 System Requirements

### Minimum Requirements (7B Model)
- **GPU**: 8GB VRAM (NVIDIA GPU with CUDA support)
- **RAM**: 16GB system RAM
- **Storage**: 20GB free space
- **OS**: Windows 10/11, Linux, macOS (with Metal support)

### Recommended Requirements (7B Model)
- **GPU**: 12GB+ VRAM (RTX 3060 12GB or better)
- **RAM**: 32GB system RAM
- **Storage**: SSD with 30GB+ free space

### For 32B Model
- **GPU**: 32GB+ VRAM (A100, H100, or multiple GPUs)
- **RAM**: 64GB+ system RAM
- **Storage**: 80GB+ free space

## 📚 Additional Resources

- [Original Paper](https://www.arxiv.org/abs/2509.04545)
- [Original Repository](https://github.com/Hunyuan-PromptEnhancer/PromptEnhancer)
- [HuggingFace Models](https://huggingface.co/tencent/HunyuanImage-2.1)
- [ComfyUI Documentation](https://github.com/comfyanonymous/ComfyUI)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the Tencent Hunyuan Community License Agreement - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgements

- [Hunyuan-PromptEnhancer Team](https://github.com/Hunyuan-PromptEnhancer/PromptEnhancer) for the original implementation
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) for the amazing node-based interface
- [HuggingFace](https://huggingface.co) for model hosting

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/ryan-seungyong-lee/ComfyUI-PromptEnhancer/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ryan-seungyong-lee/ComfyUI-PromptEnhancer/discussions)
- **Original Project**: hunyuan_opensource@tencent.com

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ryan-seungyong-lee/ComfyUI-PromptEnhancer&type=Date)](https://www.star-history.com/#ryan-seungyong-lee/ComfyUI-PromptEnhancer&Date)

---

Made with ❤️ for the ComfyUI community
