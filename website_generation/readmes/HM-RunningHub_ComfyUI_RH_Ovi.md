# ComfyUI Ovi Node

A custom node for ComfyUI that integrates Ovi for synchronized video+audio generation from text or image inputs.

## ✨ Features

* 🎬 **Joint Video+Audio Generation**: Generate synchronized video and audio content simultaneously
* 📝 **Text-to-Video+Audio**: Create videos from text prompts with speech and sound effects
* 🖼️ **Image-to-Video+Audio**: Generate videos from image and text inputs
* ⏱️ **5-Second Videos**: 24 FPS, 720×720 area, multiple aspect ratios (9:16, 16:9, 1:1, etc)
* ⚙️ **Memory Optimization**: FP8 precision + CPU offload for 24GB VRAM GPUs
* 🚀 **Flexible Control**: Advanced parameter control for quality fine-tuning

## 🔧 Node List

### Core Nodes
* **RunningHub Ovi Model Loader**: Load and initialize Ovi engine with optimization options
* **RunningHub Ovi Text to Video**: Generate video+audio from text prompts
* **RunningHub Ovi Image to Video**: Generate video+audio from image and text inputs

## 🚀 Quick Installation

### Step 1: Install the Node

```bash
# Navigate to ComfyUI custom_nodes directory
cd ComfyUI/custom_nodes/

# Clone the repository
git clone https://github.com/HM-RunningHub/ComfyUI_RH_Ovi.git

cd ComfyUI_RH_Ovi

# Install dependencies
pip install -r requirements.txt

# Install Flash Attention
pip install flash_attn --no-build-isolation
```

### Step 2: Download Required Models

```bash
# Download models (will download to ComfyUI/models/Ovi by default)
python download_weights.py

# Download fp8 quantized model (for 24GB VRAM mode)
cd ../../models/Ovi
wget -O "model_fp8_e4m3fn.safetensors" \
  "https://huggingface.co/rkfg/Ovi-fp8_quantized/resolve/main/model_fp8_e4m3fn.safetensors"
cd ../../custom_nodes/ComfyUI_RH_Ovi

# Final model structure should look like:
# ComfyUI/models/Ovi/
# ├── MMAudio/
# │   └── ext_weights/
# │       ├── best_netG.pt
# │       └── v1-16.pth
# ├── Ovi/
# │   ├── model.safetensors
# │   └── model_fp8_e4m3fn.safetensors
# └── Wan2.2-TI2V-5B/
#     ├── google/umt5-xxl/
#     ├── models_t5_umt5-xxl-enc-bf16.pth
#     └── Wan2.2_VAE.pth

# Restart ComfyUI
```

## 📖 Usage

### Basic Workflow

```
[RunningHub Ovi Model Loader] → [RunningHub Ovi Text to Video] → [Save/Preview Video]

```
<img width="1159" height="583" alt="image" src="https://github.com/user-attachments/assets/1cc83355-6253-413e-84e4-ba7582dccdf6" />


### Prompt Format

Ovi uses special tags to control speech and audio:

* **Speech**: `<S>Your speech content here<E>` - Text will be converted to speech
* **Audio Description**: `<AUDCAP>Audio description here<ENDAUDCAP>` - Describes audio/sound effects

**Example Prompt**:
```
<S>Hello world!<E> <AUDCAP>Soft piano music playing<ENDAUDCAP>
```

### Generation Types

#### Text-to-Video+Audio
1. Connect `RunningHub Ovi Model Loader` to `RunningHub Ovi Text to Video`
2. Input text prompt with speech and audio tags
3. Set video dimensions, seed, and generation parameters
4. Generate synchronized video+audio

#### Image-to-Video+Audio
1. Load an image using ComfyUI's `Load Image` node
2. Connect image and `ovi_engine` to `RunningHub Ovi Image to Video`
3. Input text prompt with speech and audio tags
4. Generate video+audio based on the image

### Example Prompts

* **Text-to-Video**: See [example_prompts/gpt_examples_t2v.csv](example_prompts/gpt_examples_t2v.csv)
* **Image-to-Video**: See [example_prompts/gpt_examples_i2v.csv](example_prompts/gpt_examples_i2v.csv)

## 🛠️ Technical Requirements

* **GPU**: 24GB+ VRAM (with CPU offload + FP8 optimization)
  * 32GB+ VRAM without optimization
* **RAM**: 32GB+ recommended
* **Storage**: ~30GB for all models
  * Ovi models: ~12GB
  * MMAudio: ~2GB
  * Wan2.2-TI2V-5B: ~13GB
  * FP8 quantized model: ~6GB
* **CUDA**: Required for optimal performance

## ⚠️ Important Notes

* **Model Paths**: Models must be placed in `ComfyUI/models/Ovi/` directory
* **Default Configuration**: Model Loader defaults to CPU offload + FP8 for 24GB VRAM
  * Disable both for 32GB+ VRAM (better quality, faster inference)
* **FP8 Model**: Required for 24GB VRAM mode (slight quality degradation)
* All model files must be downloaded before first use

## 📄 License

This project is based on the original [Ovi](https://github.com/character-ai/Ovi) project.

## 🔗 References

* [Ovi Project Page](https://aaxwaz.github.io/Ovi/)
* [Ovi Paper](https://arxiv.org/abs/2510.01284)
* [Ovi HuggingFace](https://huggingface.co/chetwinlow1/Ovi)
* [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## ⭐ Citation

If you find this project useful, please consider citing the original Ovi paper:

```bibtex
@misc{low2025ovitwinbackbonecrossmodal,
      title={Ovi: Twin Backbone Cross-Modal Fusion for Audio-Video Generation}, 
      author={Chetwin Low and Weimin Wang and Calder Katyal},
      year={2025},
      eprint={2510.01284},
      archivePrefix={arXiv},
      primaryClass={cs.MM},
      url={https://arxiv.org/abs/2510.01284}, 
}
```
