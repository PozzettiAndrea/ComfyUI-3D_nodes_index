# ComfyUI Video-As-Prompt Node

A custom node for ComfyUI that integrates Video-As-Prompt for motion-guided video generation from image inputs.

## ✨ Features

* 🎬 **Motion-Guided Generation**: Use reference videos to control motion in generated videos
* 🖼️ **Image-to-Video**: Generate videos from image with reference motion guidance
* ⚙️ **Memory Optimization**: INT8 quantization + CPU offload for efficient inference
* 🚀 **CogVideoX-5B**: Based on powerful CogVideoX-5B model

## 🔧 Node List

* **RunningHub VideoAsPrompt Loader**: Load and initialize Video-As-Prompt pipeline
* **RunningHub VideoAsPrompt Sampler(CogVideoX)**: Generate video from image with reference motion

## 🚀 Quick Installation

### Step 1: Install the Node

```bash
# Navigate to ComfyUI custom_nodes directory
cd ComfyUI/custom_nodes/

# Clone the repository
git clone https://github.com/HM-RunningHub/ComfyUI_RH_VideoAsPrompt.git

cd ComfyUI_RH_VideoAsPrompt

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Download Required Models

Download the CogVideoX-5B model and place it in the following structure:

```
ComfyUI/models/Video-As-Prompt/
└── CogVideoX-5B/
    ├── vae/
    ├── transformer/
    └── ...
```

You can download from [Video-As-Prompt Dataset](https://huggingface.co/datasets/BianYx/VAP-Data) or use the pretrained CogVideoX-5B model.

### Step 3: Restart ComfyUI

## 📖 Usage

### Basic Workflow

```
[Load Image] → [Load Video] → [RunningHub VideoAsPrompt Loader] → [RunningHub VideoAsPrompt Sampler] → [Save Video]
```

### Generation Parameters

* **image**: Input image for video generation
* **ref_video**: Reference video for motion guidance
* **prompt**: Text description for the output video
* **prompt_mot_ref**: Text description for the reference motion
* **height/width**: Output video dimensions (default: 480x720)
* **num_frames**: Number of frames to generate (default: 49)
* **num_inference_steps**: Denoising steps (default: 50)

## 🛠️ Technical Requirements

* **GPU**: 12GB+ VRAM (with INT8 quantization + CPU offload)
* **RAM**: 16GB+ recommended
* **Storage**: ~20GB for CogVideoX-5B model
* **CUDA**: Required for optimal performance

## ⚠️ Important Notes

* **Model Paths**: Models must be placed in `ComfyUI/models/Video-As-Prompt/` directory
* **Memory Optimization**: INT8 quantization and CPU offload are enabled by default for memory efficiency
* All model files must be downloaded before first use

## 🔗 References

* [Video-As-Prompt Project](https://github.com/bytedance/Video-As-Prompt)
* [Video-As-Prompt Dataset](https://huggingface.co/datasets/BianYx/VAP-Data)
* [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## 📄 License

This project is based on the [Video-As-Prompt](https://github.com/bytedance/Video-As-Prompt) project.

## ⭐ Citation

If you find this project useful, please consider citing the original Video-As-Prompt paper.

---

**Developed by [HM-RunningHub](https://github.com/HM-RunningHub)**

