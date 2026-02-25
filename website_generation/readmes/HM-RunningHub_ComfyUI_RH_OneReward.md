# ComfyUI OneReward Node

A custom node for ComfyUI that integrates OneReward model for high-quality image inpainting, outpainting, and object removal.

## ✨ Features

- 🎨 **Intelligent Image Inpainting**: Powered by OneReward model based on FLUX architecture
- 🖼️ **Image Restoration**: Smart fill of blank areas with prompt-guided content
- 🧽 **Object Removal**: Automatically remove unwanted elements from images
- 🔄 **CFG Support**: Built-in Classifier-Free Guidance for enhanced generation quality
- ⚙️ **Memory Optimization**: Quantization and CPU offload support for consumer-grade GPUs (~16GB VRAM)
- 🚀 **Flexible Control**: True CFG parameter control for fine-tuning results

## 🔧 Node List

### Core Nodes
- **RH_OneReward_Loader**: Load and initialize OneReward models with optimization options
- **RH_OneReward_Sampler**: Prompt-guided image inpainting and restoration generator
- **RH_OneReward_Eraser**: Intelligent object removal tool

## 🚀 Quick Installation

### Step 1: Install the Node
```bash
# Navigate to ComfyUI custom_nodes directory
cd ComfyUI/custom_nodes

# Clone the repository
git clone https://github.com/HM-RunningHub/ComfyUI_RH_OneReward

# Install dependencies
cd ComfyUI_RH_OneReward
pip install -r requirements.txt
```

### Step 2: Download Required Models
```bash
# Download FLUX.1-Fill-dev model (Required base model)
huggingface-cli download black-forest-labs/FLUX.1-Fill-dev --local-dir models/black-forest-labs/FLUX.1-Fill-dev

# Download OneReward models
# Download standard OneReward model
huggingface-cli download black-forest-labs/flux.1-fill-dev-OneReward-transformer --local-dir models/OneReward/flux.1-fill-dev-OneReward-transformer

# Download dynamic OneReward model (optional)
huggingface-cli download black-forest-labs/flux.1-fill-dev-OneRewardDynamic-transformer --local-dir models/OneReward/flux.1-fill-dev-OneRewardDynamic-transformer

# Final model structure should look like:
models/
├── black-forest-labs/
│   └── FLUX.1-Fill-dev/
│       ├── text_encoder/
│       ├── text_encoder_2/
│       ├── tokenizer/
│       ├── tokenizer_2/
│       ├── transformer/
│       ├── vae/
│       └── scheduler/
└── OneReward/
    ├── flux.1-fill-dev-OneReward-transformer/
    └── flux.1-fill-dev-OneRewardDynamic-transformer/
    
# Restart ComfyUI
```

## 📖 Usage

### Basic Workflow
```
[RH_OneReward_Loader] → [RH_OneReward_Sampler] → [Save Image]
```

### Generation Types

#### Image Inpainting
- Load image that needs filling
- Provide mask layer marking areas to be filled
- Input text prompt describing the fill content
- Generate intelligently filled images

#### Image Restoration  
- Load damaged or incomplete images
- Use mask to mark areas needing repair
- Input prompt describing restoration content
- Generate naturally restored images

#### Object Removal
- Use RH_OneReward_Eraser node
- Load image containing unwanted elements
- Provide mask marking areas to remove
- Automatically remove and fill background

## 🛠️ Technical Requirements

- **GPU**: 16GB+ VRAM (with quantization optimization)
- **RAM**: 32GB+ recommended
- **Storage**: ~30GB for all models
  - FLUX.1-Fill-dev: ~24GB
  - OneReward models: ~6GB
- **CUDA**: Required for optimal performance

## ⚠️ Important Notes

- **Model Paths**: Models must be placed in specific directories:
  - FLUX.1-Fill-dev → `models/black-forest-labs/FLUX.1-Fill-dev/`
  - OneReward models → `models/OneReward/`
- Low-memory GPUs automatically enable quantization and CPU offload optimization
- All model files must be downloaded before first use
- Supports true_cfg parameter for quality control

## 📄 License

This project is licensed under Apache 2.0 License.

## 🔗 References

- [OneReward Project Page](https://github.com/bytedance/OneReward)
- [FLUX.1-Fill Model](https://huggingface.co/black-forest-labs/FLUX.1-Fill-dev)
- [OneReward HuggingFace](https://huggingface.co/black-forest-labs/flux.1-fill-dev-OneReward-transformer)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## ⭐ Citation

If you find this project useful, please consider citing the related papers:

```bibtex
@article{onereward2024,
    title={OneReward: Unified Image Inpainting and Outpainting},
    author={OneReward Team},
    year={2024},
    journal={arXiv preprint},
}
```