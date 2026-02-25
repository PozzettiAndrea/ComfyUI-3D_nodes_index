# ComfyUI USO Node

A custom node for ComfyUI that integrates USO (Unified Style and Subject-Driven Generation) for high-quality image generation with style and subject control.

## ✨ Features

- 🎨 **Unified Style & Subject Generation**: Powered by USO model based on FLUX architecture
- 🎯 **Style-Driven Generation**: Generate images with specific artistic styles
- 👤 **Subject-Driven Generation**: Maintain subject consistency across generations
- 🔄 **Multi-Style Support**: Combine multiple styles in a single generation
- ⚙️ **Memory Optimization**: FP8 precision support for consumer-grade GPUs (~16GB VRAM)
- 🚀 **Flexible Control**: Advanced parameter control for fine-tuning results

## 🔧 Node List

### Core Nodes
- **RH_USO_Loader**: Load and initialize USO models with optimization options
- **RH_USO_Generator**: Generate images with style and subject control

## 🚀 Quick Installation

### Step 1: Install the Node
```bash
# Navigate to ComfyUI custom_nodes directory
cd ComfyUI/custom_nodes

# Clone the repository
git clone https://github.com/HM-RunningHub/ComfyUI_RH_USO

# Install dependencies
cd ComfyUI_RH_USO
pip install -r requirements.txt
```

### Step 2: Download Required Models
```bash
# Download FLUX.1-dev model (Required base model)
huggingface-cli download black-forest-labs/FLUX.1-dev flux1-dev.safetensors --local-dir models/diffusers/FLUX.1-dev
huggingface-cli download black-forest-labs/FLUX.1-dev ae.safetensors --local-dir models/diffusers/FLUX.1-dev

# Download USO model
huggingface-cli download bytedance-research/USO --local-dir models/uso

# Download SigLIP model
huggingface-cli download google/siglip-so400m-patch14-384 --local-dir models/clip/siglip-so400m-patch14-384

# Final model structure should look like:
models/
├── diffusers/
│   └── FLUX.1-dev/
│       ├── flux1-dev.safetensors
│       └── ae.safetensors
│       └── ....
├── uso/
│   ├── assets/
│   │   └── uso.webp
│   ├── config.json
│   ├── download_repo_enhanced.py
│   ├── README.md
│   └── uso_flux_v1.0/
│       ├── dit_lora.safetensors
│       └── projector.safetensors
└── clip/
    └── siglip-so400m-patch14-384/
    
# Restart ComfyUI
```

## 📖 Usage

### Basic Workflow
```
[RH_USO_Loader] → [RH_USO_Generator] → [Save Image]
```

### Generation Types

#### Style-Driven Generation
- Load style reference images
- Input text prompt describing the content
- Generate images in the specified style

#### Subject-Driven Generation  
- Load subject reference image
- Input text prompt with scene description
- Generate images maintaining subject identity

#### Style + Subject Generation
- Load both style and subject reference images
- Combine style transfer with subject consistency
- Generate images with unified style and preserved subjects

## 🛠️ Technical Requirements

- **GPU**: 16GB+ VRAM (with FP8 optimization)
- **RAM**: 32GB+ recommended
- **Storage**: ~35GB for all models
  - FLUX.1-dev: ~24GB (flux1-dev.safetensors + ae.safetensors)
  - USO models: ~6GB
  - SigLIP: ~1.5GB
- **CUDA**: Required for optimal performance

## ⚠️ Important Notes

- **Model Paths**: Models must be placed in specific directories:
  - FLUX.1-dev → `models/diffusers/FLUX.1-dev/`
  - USO models → `models/uso/`
  - SigLIP → `models/clip/siglip-so400m-patch14-384/`
- FP8 mode recommended for consumer GPUs (reduces VRAM usage)
- All model files must be downloaded before first use

## 📄 License

This project is licensed under Apache 2.0 License.

## 🔗 References

- [USO Project Page](https://bytedance.github.io/USO/)
- [USO Paper](https://arxiv.org/abs/2508.18966)
- [USO HuggingFace](https://huggingface.co/bytedance-research/USO)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## 🔗 Example
<img width="1788" height="866" alt="image" src="https://github.com/user-attachments/assets/3b462f37-b874-45c8-9f30-9c7d0d963d81" />
<img width="1833" height="821" alt="image" src="https://github.com/user-attachments/assets/54ab0142-ba49-45a4-8e57-32404904ce20" />
<img width="1837" height="836" alt="image" src="https://github.com/user-attachments/assets/1a4120f4-2258-4216-b7f8-f4a6a8a36169" />


## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## ⭐ Citation

If you find this project useful, please consider citing the original USO paper:

```bibtex
@article{wu2025uso,
    title={USO: Unified Style and Subject-Driven Generation via Disentangled and Reward Learning},
    author={Shaojin Wu and Mengqi Huang and Yufeng Cheng and Wenxu Wu and Jiahe Tian and Yiming Luo and Fei Ding and Qian He},
    year={2025},
    eprint={2508.18966},
    archivePrefix={arXiv},
    primaryClass={cs.CV},
}
```
