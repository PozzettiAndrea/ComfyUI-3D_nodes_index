# [中文版说明](README_CN.md).
# ComfyUI_RH_OminiControl

**ComfyUI_RH_OminiControl** is a ComfyUI plugin based on [OminiControl](https://github.com/Yuanshi9815/OminiControl) By splitting the pipeline load, the plugin efficiently runs on NVIDIA RTX 4090 GPUs. Additionally, the spatial and fill functionalities are generated using the schnell model, reducing the number of sampling steps and improving overall efficiency.

## Features
- **Optimized Performance:**：Utilizes the RTX 4090's computational power through pipeline splitting.
- **Efficient Generation:**：Uses the schnell model to generate spatial and fill, reducing sampling steps and enhancing generation efficiency.
- **Easy Installation:**：Relies on commonly used ComfyUI libraries, typically requiring no additional installation.
- **Flexible Configuration:**：Supports custom model paths for easier management and updates.


## Installation Guide

### Prerequisites

- **ComfyUI**：Ensure that ComfyUI is installed and configured. [ComfyUI](https://github.com/comfyanonymous/ComfyUI).
- **Python**：No additional libraries are usually required, but it is recommended to install diffusers version 0.31.0 to support FluxPipeline.
  
## Download
Clone the plugin repository into custom_nodes:
```
git clone https://github.com/HM-RunningHub/ComfyUI_RH_OminiControl.git
```


## Model Directory Structure:
```
/models/flux
tree
.
├── FLUX.1-schnell
│   ├── ae.safetensors
│   ├── model_index.json
│   ├── README.md
│   ├── scheduler
│   │   └── scheduler_config.json
│   ├── schnell_grid.jpeg
│   ├── text_encoder
│   │   ├── config.json
│   │   └── model.safetensors
│   ├── text_encoder_2
│   │   ├── config.json
│   │   ├── model-00001-of-00002.safetensors
│   │   ├── model-00002-of-00002.safetensors
│   │   └── model.safetensors.index.json
│   ├── tokenizer
│   │   ├── merges.txt
│   │   ├── special_tokens_map.json
│   │   ├── tokenizer_config.json
│   │   └── vocab.json
│   ├── tokenizer_2
│   │   ├── special_tokens_map.json
│   │   ├── spiece.model
│   │   ├── tokenizer_config.json
│   │   └── tokenizer.json
│   ├── transformer
│   │   ├── config.json
│   │   ├── diffusion_pytorch_model-00001-of-00003.safetensors
│   │   ├── diffusion_pytorch_model-00002-of-00003.safetensors
│   │   ├── diffusion_pytorch_model-00003-of-00003.safetensors
│   │   └── diffusion_pytorch_model.safetensors.index.json
│   └── vae
│       ├── config.json
│       └── diffusion_pytorch_model.safetensors
└── OminiControl
    ├── depth-anything-small-hf
    │   ├── config.json
    │   ├── model.safetensors
    │   ├── preprocessor_config.json
    │   └── README.md
    ├── experimental
    │   ├── canny.safetensors
    │   ├── coloring.safetensors
    │   ├── deblurring.safetensors
    │   ├── depth.safetensors
    │   ├── fill.safetensors
    │   └── subject.safetensors
    ├── omini
    │   ├── subject_1024_beta.safetensors
    │   └── subject_512.safetensors
    └── README.md

12 directories, 39 files
```
### Download and place the following models according to the directory structure above:
```
Flux model in diffusers format, download here: https://huggingface.co/black-forest-labs/FLUX.1-schnell
depth-anything-small-hf/ (for depth recognition, download here: https://huggingface.co/LiheYoung/depth-anything-small-hf/tree/main)
experimental/ (download here: https://huggingface.co/Yuanshi/OminiControl/tree/main/experimental)
omini/ (download here: https://huggingface.co/Yuanshi/OminiControl/tree/main/omini)
```
### Example Run Demo
One-click cloud run: [https://www.runninghub.ai/post/1865085524393500674]( https://www.runninghub.ai/post/1865085524393500674).
![image](https://github.com/user-attachments/assets/cc60cbc0-3c44-4da0-8e96-c2f5f89122be)


### Acknowledgments
Thanks to Yuanshi9815 and the OminiControl project for providing the foundational support.
