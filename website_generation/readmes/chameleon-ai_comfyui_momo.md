# ComfyUI MoMo

Implementation of [MoMo](https://github.com/JHLew/MoMo) video frame interpolation for ComfyUI. This does simple 2x interpolation.

The original MoMo code was written by [Jaihyun Lew](https://github.com/JHLew). This is a ComfyUI node implementation with minimal changes.

Disentangled Motion Modeling for Video Frame Interpolation, AAAI 2025
![momo cover](https://github.com/JHLew/MoMo/raw/main/figures/cover_figure.png)


## Installation

### ComfUI Manager
- Install [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
- Look up this extension in ComfyUI-Manager or install via URL
  - If you get the error `This action is not allowed with this security level configuration`, you will have to edit the [security policy](https://github.com/Comfy-Org/ComfyUI-Manager#security-policy) to `weak`. The config is located at `user/__manager/config.ini`
- Restart ComfyUI.

### Manual Install
- Clone this repository into the `custom_nodes` directory:
```
cd custom_nodes
git clone https://github.com/chameleon-ai/comfyui_momo.git
```
- Activate the ComfyUI virtual environment and install dependencies
```
source venv/bin/activate
pip install -r custom_nodes/comfyui_momo/requirements.txt
```

## Usage
On first run, the model will be downloaded to `models/diffusers/momo_full.pth`\
You can manually download the model [here](https://huggingface.co/chameleon-ai/comfyui-momo)

The node is located under `image/animation/MoMo Video Frame Interpolation`\
An [example workflow](https://github.com/chameleon-ai/comfyui_momo/blob/main/momo-example-workflow.json) is included.

Dependencies:
```
torch
accelerate
diffusers
einops
```

Tested in python 3.13 on Linux+AMD. The original MoMo implementation was for python 3.10, so it should work for that and everything in between.

