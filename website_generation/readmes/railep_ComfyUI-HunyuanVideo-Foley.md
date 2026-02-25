# ComfyUI-HunyuanVideo-Foley

A ComfyUI custom node for generating synchronized audio for videos using the HunyuanVideo-Foley model.

## Features

- Generate realistic sound effects synchronized with video content
- Support for both video file input and frame batch input from other ComfyUI nodes
- Flexible model selection through UI dropdowns
- Audio output for further processing in ComfyUI workflows
- Optional saving of audio and merged video files

---

## Installation

Clone this repository into your ComfyUI `custom_nodes` folder:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/railep/ComfyUI-HunyuanVideo-Foley
cd ComfyUI-HunyuanVideo-Foley
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Model Setup

### Required Models

#### 1. Diffusion Model & VAE
Download from: https://huggingface.co/tencent/HunyuanVideo-Foley

- Place `hunyuanvideo_foley.pth` in `ComfyUI/models/diffusion_models/`
- Place `foley_vae_128d_48k.pth` in `ComfyUI/models/vae/`

#### 2. CLIP Vision Model (SigLIP)
Download from: https://huggingface.co/google/siglip-base-patch16-512

- Create folder `ComfyUI/models/clip_vision/siglip2-base-patch16-512/`
- Download all files (`config.json`, `model.safetensors`, etc.) into this folder

#### 3. CLAP Model
Download from: https://huggingface.co/laion/clap-htsat-unfused

- Create folder `ComfyUI/models/clap/` if it doesn't exist
- Create subfolder `ComfyUI/models/clap/clap-htsat-unfused/`
- Download all model files into this folder

#### 4. Synchformer Model
Download from the HunyuanVideo-Foley repository:

- Place `synchformer_state_dict.pth` in `ComfyUI/syncforner/`

> **Note:** Ensure the folder name matches your local setup.

---

## Directory Structure

After setup, your directory structure should look like:

```
ComfyUI/
├── models/
│   ├── diffusion_models/
│   │   └── hunyuanvideo_foley.pth
│   ├── vae/
│   │   └── foley_vae_128d_48k.pth
│   ├── clip_vision/
│   │   └── siglip2-base-patch16-512/
│   │       ├── config.json
│   │       └── model.safetensors
│   └── clap/
│       └── clap-htsat-unfused/
│           ├── config.json
│           └── pytorch_model.bin
├── syncforner/
│   └── synchformer_state_dict.pth
└── custom_nodes/
    └── ComfyUI-HunyuanVideo-Foley/
```

---

## Usage

**Node:** `Hunyuan Foley: Generate Audio`

### Inputs

- `prompt`: Text description for audio generation
- `config_name`: Configuration file selection
- `diffusion_model`: Select diffusion model from dropdown
- `vae_model`: Select VAE model from dropdown
- `clip_vision_model`: Select CLIP vision model from dropdown
- `clap_model`: Select CLAP model from dropdown
- `guidance_scale`: Control generation quality (default: 4.5)
- `num_inference_steps`: Number of denoising steps (default: 50)
- `save_video`: Save merged video with audio
- `save_audio`: Save generated audio file
- `video_path` *(optional)*: Direct path to video file
- `video` *(optional)*: Frame batch input from other nodes
- `video_fps`: Frames per second for frame batch input
- `output_dir`: Output directory for saved files

### Outputs

- `audio`: Audio tensor for further processing
- `sample_rate`: Audio sample rate (48000 Hz)
- `audio_wav_path`: Path to saved audio file (if saved)
- `merged_video_path`: Path to merged video file (if saved)

---

## Example Workflow

1. Load a video using a **Video Loader** node.
2. Connect the frame output to the video input.
3. Set your audio generation prompt.
4. Configure save options as needed.
5. Run the generation.

Files will be saved as:
- `hunyuan_foley_00001.wav`
- `hunyuan_foley_00001.mp4`

with automatic numbering.

---

## Requirements

- CUDA-capable GPU recommended (8GB+ VRAM)
- Python 3.8+
- PyTorch 2.0+

---

## Troubleshooting

### CLIP Vision Model Loading Error
If you encounter permission errors, ensure the CLIP vision folder contains all necessary files and has proper read permissions.

### FFmpeg Issues
The node requires **FFmpeg** for video processing. Install it if not present:

- **Windows**: https://ffmpeg.org
- **Linux**: `sudo apt install ffmpeg`
- **Mac**: `brew install ffmpeg`

---

## Credits

Based on the HunyuanVideo-Foley model by Tencent.

---

## License

This project follows the licensing terms of the original HunyuanVideo-Foley model. Please refer to the original repository for detailed license information.
