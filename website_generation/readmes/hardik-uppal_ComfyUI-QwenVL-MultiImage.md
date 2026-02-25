# ComfyUI-QwenVL-MultiImage 🧪

A powerful ComfyUI custom node that integrates Qwen2.5-VL and Qwen3-VL vision-language models with **multi-image support**. Process multiple images simultaneously with advanced AI capabilities for image understanding, comparison, and analysis.

## ✨ Features

- 🖼️ **Multi-Image Support**: Process multiple images in a single inference
- 🤖 **Latest Models**: Support for Qwen2.5-VL and Qwen3-VL series
- 💾 **Flexible Quantization**: 4-bit, 8-bit, and FP16 options for different VRAM requirements
- ⚡ **Model Caching**: Keep models loaded in VRAM for faster subsequent runs
- 🎛️ **Two Node Variants**: Standard and Advanced nodes for different use cases
- 🔧 **Full Parameter Control**: Temperature, top_p, top_k, beam search, and more (Advanced node)
- 🎯 **GPU Optimized**: Flash Attention 2 support and efficient memory management

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "QwenVL Multi-Image"
3. Click Install

### Method 2: Manual Installation

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/YOUR_USERNAME/ComfyUI-QwenVL-MultiImage.git
```

3. Install dependencies:
```bash
cd ComfyUI-QwenVL-MultiImage
pip install -r requirements.txt
```

4. Restart ComfyUI

## 🎯 Supported Models

### Qwen3-VL Series (Latest)

| Model | Size | HuggingFace Link |
|-------|------|------------------|
| Qwen3-VL-4B-Instruct | 4B | [Download](https://huggingface.co/Qwen/Qwen3-VL-4B-Instruct) |
| Qwen3-VL-8B-Instruct | 8B | [Download](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct) |
| Qwen3-VL-32B-Instruct | 32B | [Download](https://huggingface.co/Qwen/Qwen3-VL-32B-Instruct) |
| Qwen3-VL-8B-Thinking | 8B | [Download](https://huggingface.co/Qwen/Qwen3-VL-8B-Thinking) |
| Qwen3-VL-32B-Thinking | 32B | [Download](https://huggingface.co/Qwen/Qwen3-VL-32B-Thinking) |
| Qwen3-VL-8B-Instruct-FP8 | 8B | [Download](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct-FP8) |
| Qwen3-VL-32B-Instruct-FP8 | 32B | [Download](https://huggingface.co/Qwen/Qwen3-VL-32B-Instruct-FP8) |

### Qwen2.5-VL Series

| Model | Size | HuggingFace Link |
|-------|------|------------------|
| Qwen2.5-VL-2B-Instruct | 2B | [Download](https://huggingface.co/Qwen/Qwen2.5-VL-2B-Instruct) |
| Qwen2.5-VL-3B-Instruct | 3B | [Download](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) |
| Qwen2.5-VL-7B-Instruct | 7B | [Download](https://huggingface.co/Qwen/Qwen2.5-VL-7B-Instruct) |
| Qwen2.5-VL-72B-Instruct | 72B | [Download](https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct) |

Models will be automatically downloaded from HuggingFace on first use.

## 📖 Usage

### Basic Usage (Standard Node)

1. Add the **"🧪 QwenVL Multi-Image"** node from the `🧪AILab/QwenVL` category
2. Connect one or more image sources to the node:
   - `images`: Main image input (can be a batch)
   - `images_batch_2`: Optional second batch
   - `images_batch_3`: Optional third batch
3. Select your desired model from the dropdown
4. Write your prompts:
   - `system_prompt`: System instructions for the AI
   - `user_prompt`: Your question or task
5. Configure quantization and other settings
6. Run the workflow

### Advanced Usage (Advanced Node)

Use the **"🧪 QwenVL Multi-Image (Advanced)"** node for fine-grained control:

- `temperature`: Controls randomness (0.1-2.0)
- `top_p`: Nucleus sampling threshold (0.0-1.0)
- `top_k`: Top-k sampling (1-100)
- `num_beams`: Beam search width (1-10)
- `repetition_penalty`: Penalize repeated tokens (1.0-2.0)
- `device`: Force specific device (auto/cuda/cpu)

## ⚙️ Parameters

### Common Parameters

| Parameter | Description | Default | Range |
|-----------|-------------|---------|-------|
| **images** | Main image input (supports batches) | Required | - |
| **model_name** | Qwen-VL model to use | Qwen3-VL-4B-Instruct | See model list |
| **system_prompt** | System instructions | "You are a helpful assistant." | Any text |
| **user_prompt** | Your question/task | "Describe these images..." | Any text |
| **quantization** | Memory optimization mode | 8-bit (Balanced) | FP16/8-bit/4-bit |
| **max_tokens** | Maximum output length | 1024 | 64-4096 |
| **keep_model_loaded** | Cache model in VRAM | True | True/False |
| **seed** | Random seed | 1 | 1 - 2^32-1 |

### Advanced Parameters (Advanced Node Only)

| Parameter | Description | Default | Range |
|-----------|-------------|---------|-------|
| **temperature** | Sampling randomness | 0.7 | 0.1-2.0 |
| **top_p** | Nucleus sampling | 0.9 | 0.0-1.0 |
| **top_k** | Top-k sampling | 50 | 1-100 |
| **repetition_penalty** | Penalize repeats | 1.1 | 1.0-2.0 |
| **num_beams** | Beam search width | 1 | 1-10 |
| **device** | Device selection | auto | auto/cuda/cpu |

## 💡 Quantization Guide

| Mode | Precision | VRAM Usage | Speed | Quality | Recommended For |
|------|-----------|------------|-------|---------|-----------------|
| None (FP16) | 16-bit | High | Fastest | Best | 16GB+ VRAM |
| 8-bit (Balanced) | 8-bit | Medium | Fast | Very Good | 8GB+ VRAM |
| 4-bit (VRAM-friendly) | 4-bit | Low | Slower | Good | <8GB VRAM |

**Note**: FP8 models (pre-quantized) automatically use optimized precision and ignore the quantization setting.

## 🎨 Example Use Cases

### 1. Multi-Image Comparison
Compare multiple product photos, analyze differences, or identify similarities.

**Prompt**: "Compare these images and describe the key differences between them."

### 2. Sequential Analysis
Analyze a sequence of images showing a process or timeline.

**Prompt**: "Describe the progression shown across these images."

### 3. Multi-View Understanding
Process multiple angles or views of the same object.

**Prompt**: "Based on these different views, provide a comprehensive description of the object."

### 4. Batch Description
Generate captions or descriptions for multiple images simultaneously.

**Prompt**: "Provide a detailed caption for each image."

## 🔧 Troubleshooting

### Out of Memory Errors

1. Switch to a smaller model (e.g., 2B or 3B)
2. Enable more aggressive quantization (4-bit)
3. Reduce `max_tokens`
4. Process fewer images at once
5. Set `keep_model_loaded` to False

### Slow Performance

1. Use FP8 models on supported hardware (RTX 40 series)
2. Enable `keep_model_loaded` for repeated inference
3. Use FP16 quantization on high-VRAM systems
4. Ensure CUDA is properly installed

### Model Download Issues

Models are downloaded from HuggingFace on first use. If you encounter issues:

1. Check your internet connection
2. Verify HuggingFace is accessible
3. Manually download models to your HuggingFace cache directory
4. Check available disk space (models can be 2-150GB)

### Import Errors

If you get import errors after installation:

```bash
cd ComfyUI/custom_nodes/ComfyUI-QwenVL-MultiImage
pip install -r requirements.txt --upgrade
```

## 🎯 Tips & Best Practices

### Model Selection
- **For most users**: Start with `Qwen3-VL-4B-Instruct` (balanced performance)
- **Low VRAM (<8GB)**: Use `Qwen2.5-VL-2B-Instruct` with 4-bit quantization
- **Best quality**: Use `Qwen3-VL-32B-Instruct` with FP16 (requires 24GB+ VRAM)
- **RTX 40 series**: Use FP8 variants for optimal speed

### Memory Management
- Enable `keep_model_loaded` if running multiple inferences
- Disable it if you need to switch between different models
- Use 8-bit quantization as a good balance between quality and VRAM

### Prompt Engineering
- Be specific about what you want from multiple images
- Use system prompts to set the context and behavior
- For comparisons, explicitly ask to compare or contrast
- Number your images in the prompt if order matters

### Performance
- First load is always slower (downloading/caching)
- Subsequent runs with cached models are much faster
- Batch multiple images when possible instead of separate inferences

## 🛠️ Development

### Requirements

- Python 3.8+
- PyTorch 2.0+
- CUDA 11.8+ (for GPU acceleration)
- 8GB+ VRAM recommended (4GB minimum with quantization)

### Building from Source

```bash
git clone https://github.com/YOUR_USERNAME/ComfyUI-QwenVL-MultiImage.git
cd ComfyUI-QwenVL-MultiImage
pip install -r requirements.txt
```

## 🙏 Credits

- **Qwen Team** (Alibaba Cloud): For developing the Qwen-VL models
- **ComfyUI**: For the excellent node-based interface
- **1038lab/ComfyUI-QwenVL**: For the original QwenVL node implementation that inspired this project

## 📜 License

This project is licensed under the GPL-3.0 License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📮 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Search existing [Issues](https://github.com/YOUR_USERNAME/ComfyUI-QwenVL-MultiImage/issues)
3. Open a new issue with detailed information

## ⭐ Star History

If you find this project useful, please consider giving it a star!

---

**Note**: Replace `YOUR_USERNAME` with your actual GitHub username before publishing.

