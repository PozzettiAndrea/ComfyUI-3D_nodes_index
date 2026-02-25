# ComfyUI-HunyuanPortrait

ComfyUI-HunyuanPortrait is now available in ComfyUI, [HunyuanPortrait](https://github.com/Tencent-Hunyuan/HunyuanPortrait) is a diffusion-based condition control method that employs implicit representations for highly controllable and lifelike portrait animation. 


## Installation

1. Make sure you have ComfyUI installed

2. Clone this repository into your ComfyUI's custom_nodes directory:
```
cd ComfyUI/custom_nodes
git clone https://github.com/Yuan-ManX/ComfyUI-HunyuanPortrait.git
```

3. Install dependencies:
```
cd ComfyUI-HunyuanPortrait
pip install torch torchvision torchaudio
pip install -r requirements.txt
```


## Model

### Download pretrained checkpoint

All the weights should be placed under the `ComfyUI/models/HunyuanPortrait/pretrained_weights` direcotry. You can download weights manually as follows:

All models are stored in `pretrained_weights` by default:
```bash
pip install "huggingface_hub[cli]"
cd pretrained_weights
huggingface-cli download --resume-download stabilityai/stable-video-diffusion-img2vid-xt --local-dir . --include "*.json"
wget -c https://huggingface.co/LeonJoe13/Sonic/resolve/main/yoloface_v5m.pt
wget -c https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/resolve/main/vae/diffusion_pytorch_model.fp16.safetensors -P vae
wget -c https://huggingface.co/FoivosPar/Arc2Face/resolve/da2f1e9aa3954dad093213acfc9ae75a68da6ffd/arcface.onnx
huggingface-cli download --resume-download tencent/HunyuanPortrait --local-dir hyportrait
```

And the file structure is as follows:
```bash
.
├── arcface.onnx
├── hyportrait
│   ├── dino.pth
│   ├── expression.pth
│   ├── headpose.pth
│   ├── image_proj.pth
│   ├── motion_proj.pth
│   ├── pose_guider.pth
│   └── unet.pth
├── scheduler
│   └── scheduler_config.json
├── unet
│   └── config.json
├── vae
│   ├── config.json
│   └── diffusion_pytorch_model.fp16.safetensors
└── yoloface_v5m.pt
```


## Requirements

* An NVIDIA 3090 GPU with CUDA support is required. 
  * The model is tested on a single 24G GPU.
 
* Tested operating system: Linux

