# ComfyUI-PixArt_XL

## Support My Work
If you find this project helpful, consider buying me a coffee:

[![Buy Me A Coffee](https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=shmuelronen&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff)](https://buymeacoffee.com/shmuelronen)

A ComfyUI extension that integrates PixArt-Alpha models directly into ComfyUI with advanced memory management.

![image](https://github.com/user-attachments/assets/9b489265-acc3-46e1-b8cb-f2b39017f1b3)


## Features

- Use PixArt-Alpha XL models directly in ComfyUI
- Smart memory management using both GPU and system RAM
- Automatic fallback to lower resolutions with high-quality upscaling
- Support for both DPM-Solver and SA-Solver schedulers
- Full precision processing for maximum stability

## Installation

1. Clone this repository into your ComfyUI custom nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ShmuelRonen/ComfyUI-PixArt_XL.git
```

2. Install dependencies:
```bash
pip install sentencepiece
```

3. Restart ComfyUI

## Usage

After installation, you'll have access to two new nodes:

### PixArtAlpha ModelLoader

Automatic loads a PixArt-Alpha model from Hugging Face.

**Inputs:**
- `base_model_path`: Path to the model (default: "PixArt-alpha/PixArt-XL-2-1024-MS")

**Outputs:**
- `model`: The loaded model

### PixArtAlpha Generation

Generates images using the PixArt-Alpha model.

**Inputs:**
- `model`: The PixArt-Alpha model
- `positive`: Positive prompt
- `negative`: Negative prompt
- `width`, `height`: Image dimensions
- `steps`: Number of sampling steps
- `guidance_scale`: How closely to follow the prompt
- `schedule`: Sampling scheduler
- `seed`: Random seed

**Outputs:**
- `image`: The generated image

## Memory Optimization

This implementation includes several advanced techniques to maximize memory efficiency:
- CPU component offloading
- Attention slicing
- VAE optimization
- Periodic CUDA cache clearing
- Resolution fallback with quality-preserving upscaling

## Acknowledgments

- [PixArt-alpha](https://github.com/PixArt-alpha/PixArt-alpha)
- [Diffusers library](https://github.com/huggingface/diffusers)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
