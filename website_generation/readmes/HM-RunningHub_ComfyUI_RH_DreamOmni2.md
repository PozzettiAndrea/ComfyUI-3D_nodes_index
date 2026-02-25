# ComfyUI DreamOmni2 Node

A custom node for ComfyUI that integrates DreamOmni2 for image generation and editing with multi-modal understanding.

## ✨ Features

* 🎨 **Image Generation**: Create images from 1-3 reference images with VLM-guided prompts
* ✏️ **Image Editing**: Edit source images using reference images and natural language instructions
* 🧠 **VLM Integration**: Qwen2.5-VL model for intelligent prompt understanding
* 💾 **Memory Optimized**: INT8 quantization + CPU offload for efficient inference
* ⚡ **FLUX-based**: Built on FLUX.1-Kontext-dev architecture

## 🔧 Node List

### Core Nodes

* **RunningHub DreamOmni2 Gen Pipeline**: Load generation pipeline with LoRA weights
* **RunningHub DreamOmni2 Edit Pipeline**: Load editing pipeline with LoRA weights
* **RunningHub DreamOmni2 Generator**: Generate images from reference images and prompts
* **RunningHub DreamOmni2 Editor**: Edit images using source and reference images

## 🚀 Quick Installation

### Step 1: Install the Node

```bash
# Navigate to ComfyUI custom_nodes directory
cd ComfyUI/custom_nodes/

# Clone the repository
git clone https://github.com/HM-RunningHub/ComfyUI_RH_DreamOmni2.git
cd ComfyUI_RH_DreamOmni2

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Download Required Models

Download and place models in the following structure:

```
ComfyUI/models/
├── flux/
│   └── FLUX.1-Kontext-dev/
│       ├── transformer/
│       ├── vae/
│       ├── text_encoder/
│       └── text_encoder_2/
└── DreamOmni2/
    ├── gen_lora/
    │   └── pytorch_lora_weights.safetensors
    ├── edit_lora/
    │   └── pytorch_lora_weights.safetensors
    └── vlm-model/
        ├── config.json
        ├── model.safetensors
        └── ...
```

**Model Downloads**:
* FLUX.1-Kontext-dev: [black-forest-labs/FLUX.1-Kontext-dev](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev)
* DreamOmni2 Models: [xiabs/DreamOmni2](https://huggingface.co/xiabs/DreamOmni2)

**Quick Download**:
```bash
# Download DreamOmni2 models (gen_lora, edit_lora, vlm-model)
huggingface-cli download --resume-download --local-dir-use-symlinks False \
    xiabs/DreamOmni2 --local-dir ComfyUI/models/DreamOmni2

# Download FLUX.1-Kontext-dev
huggingface-cli download --resume-download --local-dir-use-symlinks False \
    black-forest-labs/FLUX.1-Kontext-dev --local-dir ComfyUI/models/flux/FLUX.1-Kontext-dev
```

Restart ComfyUI after installation.

## 📖 Usage

### Image Generation Workflow

```
[RunningHub DreamOmni2 Gen Pipeline] → [RunningHub DreamOmni2 Generator] → [Save/Preview Image]
                                              ↑
                                    [Load Image (Ref 1-3)]
```

**Generator Parameters**:
* `ref_image`: Primary reference image (required)
* `ref_image_2`, `ref_image_3`: Additional reference images (optional)
* `prompt`: Natural language instruction describing the desired output
* `width`, `height`: Output image dimensions (default: 1024×1024)
* `num_inference_steps`: Denoising steps (default: 30)
* `guidance_scale`: CFG scale (default: 3.5)
* `seed`: Random seed for reproducibility

### Image Editing Workflow

```
[RunningHub DreamOmni2 Edit Pipeline] → [RunningHub DreamOmni2 Editor] → [Save/Preview Image]
                                              ↑
                                    [Load Image (Source + Ref)]
```

**Editor Parameters**:
* `src_image`: Source image to edit (required)
* `ref_image`: Reference image for style/content (required)
* `prompt`: Natural language editing instruction
* `num_inference_steps`: Denoising steps (default: 30)
* `guidance_scale`: CFG scale (default: 3.5)
* `seed`: Random seed for reproducibility

### Example Prompts

**Generation**:
* "Create an anime-style portrait with blue hair and golden eyes"
* "Generate a cyberpunk cityscape at night with neon lights"

**Editing**:
* "Change the hair color to red while keeping the face"
* "Add sunglasses and a leather jacket to the person"

## 🛠️ Technical Requirements

* **GPU**: 18GB+ VRAM
* **RAM**: 64GB+ recommended
* **CUDA**: Required for optimal performance

## ⚠️ Important Notes

* **Model Paths**: Models must be placed in `ComfyUI/models/` directory
* **CPU Offload**: Automatically enabled for memory optimization
* **INT8 Quantization**: Applied to transformer for 12GB VRAM support
* **VLM Processing**: The VLM model automatically enhances your prompt before generation
* All model files must be downloaded before first use

## 📄 License

This project is licensed under the Apache License 2.0.

## 🔗 References

* [DreamOmni2 Official Repository](https://github.com/dvlab-research/DreamOmni2)
* [DreamOmni2 Models](https://huggingface.co/xiabs/DreamOmni2)
* [FLUX.1-Kontext-dev](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev)
* [Qwen2.5-VL](https://huggingface.co/Qwen)
* [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## 🙏 Credits

Developed by [@HM-RunningHub](https://github.com/HM-RunningHub)

Based on the original [DreamOmni2](https://github.com/dvlab-research/DreamOmni2) project by dvlab-research.

## ⭐ Citation

If you find this project useful, please consider citing the original DreamOmni2 paper:

```bibtex
@article{dreamomni2,
  title={DreamOmni2: Multimodal Instruction-based Editing and Generation},
  author={Xia, Bin and others},
  journal={arXiv preprint},
  year={2025}
}
```

## About

ComfyUI custom nodes for DreamOmni2 image generation and editing

### License

Apache-2.0 license

