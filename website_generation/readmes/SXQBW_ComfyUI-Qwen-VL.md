<div align="center">

# ComfyUI-Qwen-VL 🐼
<p align="center">
        <a href="README_zh.md">中文</a> &nbsp｜ &nbsp English
</p>

**Where Figma meets VSCode: Artistic vision meets engineering precision —— a romantic manifesto from designers to the code world.**  
✨ A ComfyUI extension for Qwen2.5-VL series large language models, supporting multimodal capabilities such as text generation, image understanding, and video analysis. ✨
  
[![Star History](https://img.shields.io/github/stars/SXQBW/ComfyUI-Qwen-VL?style=for-the-badge&logo=starship&color=FE428E&labelColor=0D1117)](https://github.com/SXQBW/ComfyUI-Qwen-VL/stargazers)
[![Model Download](https://img.shields.io/badge/Model_Download-6DB33F?style=for-the-badge&logo=ipfs&logoColor=white)](https://huggingface.co/Qwen)
</div>
<div align="center">
  <img src="pic/screenshot-20250523-180706.png" width="90%">
</div>

---

### 🌟 Features

- Supports Qwen2-VL, Qwen2.5-VL and other series models
- Provides various functional nodes for text generation, image understanding, video analysis, etc.
- Supports model quantization configuration to optimize memory usage
- Offers an intuitive user interface for easy parameter adjustment

### 🚀 Installation

1. Navigate to the `custom_nodes` directory of ComfyUI
2. Clone this repository:
   ```bash
   git clone https://github.com/SXQBW/ComfyUI-Qwen-VL.git
   ```
3. Install dependencies:
   ```bash
   cd ComfyUI-Qwen-VL
   pip install -r requirements.txt
   ```
4. Restart ComfyUI

### 📖 Usage

1. In the ComfyUI interface, locate the Qwen-VL related nodes
2. Select the model and quantization method you want to use
3. Configure generation parameters such as temperature and maximum tokens
4. Connect input (text, image, or video) and output nodes
5. Run the workflow

### 📦 Supported Models

The following models are currently supported:

- Qwen/Qwen2.5-VL-3B-Instruct
- Qwen/Qwen2.5-VL-3B-Instruct-AWQ
- Qwen/Qwen2.5-VL-7B-Instruct
- Qwen/Qwen2.5-VL-7B-Instruct-AWQ
- Qwen/Qwen2.5-VL-32B-Instruct
- Qwen/Qwen2.5-VL-32B-Instruct-AWQ
- Qwen/Qwen2.5-VL-72B-Instruct
- Qwen/Qwen2.5-VL-72B-Instruct-AWQ
- Qwen/Qwen2-VL-2B
- Qwen/Qwen2-VL-2B-Instruct
- Qwen/Qwen2-VL-7B-Instruct
- Qwen/Qwen2-VL-72B-Instruct
- Qwen/Qwen2-VL-2B-Instruct-AWQ
- Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int4
- Qwen/Qwen2-VL-2B-Instruct-GPTQ-Int8
- Qwen/Qwen2-VL-7B-Instruct-AWQ
- Qwen/Qwen2-VL-7B-Instruct-GPTQ-Int4
- Qwen/Qwen2-VL-7B-Instruct-GPTQ-Int8
- Qwen/Qwen2-VL-72B-Instruct-AWQ
- Qwen/Qwen2-VL-72B-Instruct-GPTQ-Int4
- Qwen/Qwen2-VL-72B-Instruct-GPTQ-Int8
- huihui-ai/Qwen2.5-VL-7B-Instruct-abliterated

### Quantization Options

- 🚫 None (Original Precision): Use original precision
- 👍 4-bit (VRAM-friendly): Use 4-bit quantization to save VRAM
- ⚖️ 8-bit (Balanced Precision): Use 8-bit quantization for balanced precision and performance

### 👀 Example Workflows

Here's a simple example workflow for image understanding:
![alt text](pic/screenshot-20250523-180706.png)

![alt text](pic/screenshot-20250506-055913.png)

![alt text](pic/screenshot-20250506-065011.png)

### 📖 FAQ

#### Model Loading Issues

If you encounter errors loading the model, ensure:

1. The model file path is correct
2. You have sufficient GPU memory (Choose an appropriate model based on your VRAM size. Don't jump straight to the 72B model – brute force won't work here, it'll just crash your VRAM)
3. All necessary dependencies are installed

#### About Quantization

When using pre-quantized models (e.g., AWQ versions), you may see the following warning: "Model Qwen2.5-VL-3B-Instruct-AWQ is already quantized, user quantization settings will be ignored." This is normal, and the plugin will automatically use the model's pre-quantized version.

### 🤝 Contributing

Contributions, issues, and feature requests are welcome!

### 🙏 Acknowledgments

Special thanks to the Qwen team for developing these powerful models, and to the ComfyUI community for their support!

**The star you're about to click ✨**  
Is not just a gesture of approval, but a cosmic explosion where design thinking meets the code universe. When an artist's aesthetic obsession collides with a programmer's geek spirit – this might just be the most romantic chemical reaction on GitHub.

[Click to Star and Witness the Cross-Disciplinary Revolution](https://github.com/SXQBW/ComfyUI-Qwen-VL)
