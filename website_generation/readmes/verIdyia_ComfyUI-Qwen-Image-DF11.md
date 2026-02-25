# ComfyUI Qwen-Image DFloat11 Nodes

ComfyUI custom nodes for the DFloat11 compressed Qwen-Image model. This package provides efficient image generation with reduced memory usage through DFloat11 compression technology.

## Features

- **DFloat11 Qwen-Image Loader**: Load the compressed Qwen-Image model with CPU offloading options
- **Qwen-Image Text Encode**: Process text prompts with language-specific magic prompts
- **Qwen-Image Sampler**: Generate images with full control over parameters
- **Qwen-Image Decode**: Save generated images to output directory
- **Qwen-Image Aspect Ratio**: Quick aspect ratio selection for common formats
- **Qwen-Image Preset Sampler**: Fast generation with preset configurations

## Installation

### 1. Install Custom Nodes
Clone this repository into your ComfyUI custom_nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/verIdyia/ComfyUI-Qwen-Image-DF11.git
```

Install dependencies:
```bash
cd ComfyUI-Qwen-Image-DF11
pip install -r requirements.txt
```

### 2. Download Models
Download the complete Qwen-Image model structure with DFloat11 compressed transformer:

**Required Model Structure:**
```
ComfyUI/models/diffusion_models/
└── Qwen-Image/
    ├── model_index.json              # From Qwen/Qwen-Image
    ├── transformer/
    │   ├── config.json               # From Qwen/Qwen-Image
    │   └── diffusion_pytorch_model.safetensors  # From DFloat11/Qwen-Image-DF11
    ├── text_encoder/
    │   ├── config.json               # From Qwen/Qwen-Image
    │   ├── model.safetensors         # From Qwen/Qwen-Image
    │   └── ...
    ├── vae/
    │   ├── config.json               # From Qwen/Qwen-Image
    │   ├── diffusion_pytorch_model.safetensors  # From Qwen/Qwen-Image
    │   └── ...
    ├── tokenizer/
    │   ├── tokenizer_config.json     # From Qwen/Qwen-Image
    │   ├── tokenizer.json            # From Qwen/Qwen-Image
    │   └── ...
    └── scheduler/
        └── scheduler_config.json     # From Qwen/Qwen-Image
```

**Installation Steps:**

1. **Download base model structure:**
```bash
cd ComfyUI/models/diffusion_models
git lfs clone https://huggingface.co/Qwen/Qwen-Image
```

2. **Replace transformer with DFloat11 compressed version:**
```bash
cd Qwen-Image/transformer
# Backup original transformer (optional)
mv diffusion_pytorch_model.safetensors diffusion_pytorch_model.safetensors.backup
# Download DFloat11 compressed transformer
wget https://huggingface.co/DFloat11/Qwen-Image-DF11/resolve/main/diffusion_pytorch_model.safetensors
```

**OR using Hugging Face Hub:**
```python
from huggingface_hub import hf_hub_download
hf_hub_download("DFloat11/Qwen-Image-DF11", "diffusion_pytorch_model.safetensors", 
                local_dir="ComfyUI/models/diffusion_models/Qwen-Image/transformer")
```

**Memory Benefits:**
- Original transformer: ~41GB
- DFloat11 compressed: ~28GB (32% size reduction)
- Other components remain unchanged for compatibility

### 3. Restart ComfyUI
Restart ComfyUI to load the new nodes.

## Memory Requirements

- **Without CPU Offloading**: 32GB VRAM required
- **With CPU Offloading**: 16GB VRAM required
- Model Size: 28.42 GB (32% smaller than original BFloat16)

## Usage

See the included example workflow JSON file for a complete setup example.

## Model Information

This package uses the DFloat11 compressed version of Qwen-Image:
- Model: `DFloat11/Qwen-Image-DF11`
- Original: `Qwen/Qwen-Image`
- Compression: Lossless 32% size reduction
- Performance: Bit-identical outputs to original model

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

The underlying Qwen-Image model is also licensed under Apache 2.0. Please refer to the original model's license terms:
- [Qwen-Image](https://huggingface.co/Qwen/Qwen-Image) - Apache 2.0
- [DFloat11/Qwen-Image-DF11](https://huggingface.co/DFloat11/Qwen-Image-DF11) - Please check the model's license on Hugging Face