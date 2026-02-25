# ComfyUI IC-Custom Node

A custom node for ComfyUI that integrates IC-Custom model for high-quality image customization and generation.

## ✨ Features

- 🎨 **High-Quality Image Generation**: Powered by FLUX.1-Fill-dev and IC-Custom models
- 🖼️ **Image Customization**: Generate customized images based on reference images
- 🎯 **Flexible Generation Modes**: Support for position-free and position-precise generation
- ⚙️ **Advanced Controls**: Configurable guidance scale, inference steps, and seed control
- 🚀 **Optimized Performance**: Model quantization and offloading for better memory efficiency

## 📦 Installation

### Step 1: Install the Node

```bash
# Navigate to ComfyUI custom_nodes directory
cd ComfyUI/custom_nodes

# Clone the repository
git clone https://github.com/HM-RunningHub/ComfyUI_RH_ICCustom

# Install dependencies
cd ComfyUI_RH_ICCustom
pip install -r requirements.txt
```

### Step 2: Download Required Models

Create the following directory structure in your ComfyUI models folder:

#### Main Models

**FLUX.1-Fill-dev Model:**
- Download: [FLUX.1-Fill-dev](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev/tree/main)
- Files: `ae.safetensors`, `flux1-fill-dev.safetensors`
- Location: `ComfyUI/models/black-forest-labs/FLUX.1-Fill-dev/`

**IC-Custom Model:**
- Download: [IC-Custom](https://huggingface.co/TencentARC/IC-Custom/tree/main)
- Files: All files from the repository
- Location: `ComfyUI/models/IC-Custom/`

**FLUX Redux Model:**
- Download: [FLUX.1-Redux-dev](https://huggingface.co/black-forest-labs/FLUX.1-Redux-dev/tree/main)
- File: `flux1-redux-dev.safetensors`
- Location: `ComfyUI/models/IC-Custom/`

#### CLIP Models

**SigLIP Model:**
- Download: [siglip-so400m-patch14-384](https://huggingface.co/google/siglip-so400m-patch14-384/tree/main)
- Files: All files from the repository
- Location: `ComfyUI/models/clip/siglip-so400m-patch14-384/`

**XFlux Text Encoders:**
- Download: [xflux_text_encoders](https://huggingface.co/XLabs-AI/xflux_text_encoders/tree/main)
- Files: All files from the repository
- Location: `ComfyUI/models/clip/xflux_text_encoders/`

#### CLIP Vision Models

**CLIP ViT Large:**
- Download: [clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14/tree/main)
- Files: All files from the repository
- Location: `ComfyUI/models/clip_vision/clip-vit-large-patch14/`

**SigCLIP Vision:**
- Download: [sigclip_vision_patch14_384](https://huggingface.co/funnewsr/sigclip_vision_patch14_384/tree/main)
- File: `sigclip_vision_patch14_384.safetensors`
- Location: `ComfyUI/models/clip_vision/`

## 🚀 Usage

### Basic Workflow

1. **Add Model Loader**: Add "RunningHub ICCustom Loader" node to your workflow
2. **Add Sampler**: Add "RunningHub ICCustom Sampler" node and connect the pipeline output
3. **Configure Inputs**:
   - Connect reference image
   - Set prompt text
   - Configure generation parameters
   - Optionally add target image and mask for precise control

### Example Workflow

```
[Reference Image] → [ICCustom Loader] → [ICCustom Sampler] → [Save Image]
                                    ↓
                               [Prompt Input]
```

### Generation Modes

- **Position-Free**: Generate without target constraints (no mask required)
- **Position-Precise**: Generate with specific target positioning (requires mask)

## ⚙️ Parameters

- **Prompt**: Text description for the generated content
- **Guidance**: Controls adherence to prompt (default: 40.0)
- **True GS**: Additional guidance parameter (default: 3.0)
- **Steps**: Number of inference steps (default: 25)
- **Seed**: Random seed for reproducible results

## 🔧 Requirements

- **GPU Memory**: 16GB+ VRAM recommended
- **System RAM**: 32GB+ recommended
- **Storage**: ~100B for all models
- **Dependencies**: PyTorch, Diffusers, Transformers

## 📄 License

This project is licensed under the Apache 2.0 License.

## 🔗 References

- [IC-Custom](https://github.com/TencentARC/IC-Custom)
- [FLUX Models](https://huggingface.co/black-forest-labs)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## 🙏 Acknowledgments

Special thanks to **AIwood爱屋研究室** ([Bilibili](https://space.bilibili.com/503934057)) for helping with Windows environment testing and contributing to the installation documentation.
<img width="1464" height="1140" alt="image" src="https://github.com/user-attachments/assets/f77bf3e1-ece3-4c70-9bbe-2e77044cfa1e" />
<img width="1706" height="1119" alt="image" src="https://github.com/user-attachments/assets/71cd94aa-7f45-4fc3-a06d-37105cf7daae" />

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.
