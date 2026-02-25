[English](README.md) | [简体中文](README_zh_CN.md)
# ComfyUI Hunyuan3D-1-wrapper

**ComfyUI Hunyuan3D-1-wrapper** is a custom node that allows you to run [Tencent/Hunyuan3D-1](https://github.com/Tencent/Hunyuan3D-1) in ComfyUI as a wrapper.
![img_1.png](img_1.png)
**!!To avoid breaking your existing environment, it is strongly recommended to use a fresh ComfyUI installation for this node**

# Setup
Please note that this plugin currently doesn't have an easy way to install in ComfyUI. I'll provide several scenarios for reference.

Additionally, the following environments are all based on Windows 10 + CUDA 12.4 + Python 3.12.

## Scenario 1: ComfyUI Bundle(Python 3.12) + 3D Pack
If you downloaded ComfyUI from the ComfyUI Release page (current latest version 0.2.7, bundled with Python 3.12) and have successfully installed 3D Pack, congratulations, you dont need this repo, 3d-pack has its implement already.

## Scenario 2: ComfyUI Bundle(Python 3.12)
If you downloaded ComfyUI from the ComfyUI Release page (current latest version 0.2.7, bundled with Python 3.12) but haven't installed 3D Pack, you'll need some additional steps to package related dependencies.

It should be noted that if you plan to use ComfyUI's built-in Python, **texture mapping** and **gif output** will not be available in this node.

### Package and Install Pytorch3D
Pytorch3D is a major challenge during installation, whether for 3D Pack or this node. Reference steps:
1. Install C++ build tools locally, and check the following during installation: ![img.png](img.png)
2. Create a Python 3.12 environment using conda:  
`conda create -n comfy-hunyuan3d-py312-build python=3.12`
3. Activate conda environment:  
`conda activate comfy-hunyuan3d-py312-build`
4. Install torch:  
`pip install torch==2.5.1 --index-url https://download.pytorch.org/whl/cu124`
5. Package pytorch3d wheel:  
`pip wheel git+https://github.com/facebookresearch/pytorch3d`
If everything goes smoothly, you'll see the pytorch3d wheel file in your current directory
6. Install pytorch3d wheel using comfyui's bundled python:  
`{comfyUI_python_embeded}\python -m pip install pytorch3d-0.7.8-cp312-cp312-win_amd64.whl`

### Install Open3D
Currently, Open3D hasn't released packages for Python 3.12, but you can download the Python 3.12 dev version from their github:
1. Download the wheel for py3.12+win:  
`https://github.com/isl-org/Open3D/releases/tag/main-devel`
2. Install local Open3D wheel using comfyui's bundled python:  
`{comfyUI_python_embeded}\python -m pip install open3d-0.18.0+fcc396e-cp312-cp312-win_amd64.whl`

### Install Hunyuan3D-1 Node Dependencies
1. `git clone` this repository in ComfyUI's custom nodes folder
2. `{comfyUI_python_embeded}\python -m pip install -r requirements.txt`
3. `{comfyUI_python_embeded}\python -m pip install git+https://github.com/NVlabs/nvdiffrast`
4. `{comfyUI_python_embeded}\python -m pip install Ninja`

Again, reminder that in this scenario, **texture mapping** and **gif output** are not available.

## Scenario 3: Using ComfyUI in Conda Environment (Recommended)
From my personal perspective, this is my most recommended approach, as texture mapping and gif output can be used in this environment. Specific steps:
1. Install C++ build tools locally, and check the following during installation: ![img.png](img.png)
2. Create a Python 3.12 environment for ComfyUI using Conda:  
`conda create -n hunyuan3d-comfyui-py312 python=3.12`
3. Activate the environment:  
`conda activate hunyuan3d-comfyui-py312`
4. Install torch and torchvision:  
`pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124`
5. Go to ComfyUI's own directory (containing requirements.txt), install ComfyUI's dependencies:  
`pip install -r .\requirements.txt`
6. `pip install git+https://github.com/facebookresearch/pytorch3d`
7. `pip install git+https://github.com/NVlabs/nvdiffrast`
8. Download Open3D wheel for py3.12+win:  
**https://github.com/isl-org/Open3D/releases/tag/main-devel**
9. `pip install open3d-0.18.0+fcc396e-cp312-cp312-win_amd64.whl`
10. `git clone` this repository in ComfyUI's custom nodes folder
11. Install this repository's dependencies:  
`pip install -r requirements.txt`
12. `pip install Ninja`

Run the following command in ComfyUI's root directory to start:
`python -s main.py --windows-standalone-build`

## Other Launcher Scenarios (aki, StabilityMatrix, etc.)
I apologize, but I personally don't have the habit of using these launchers. Since different launchers bind to different environments, due to time constraints, I haven't done any testing on them. However, theoretically, they should all work - please research on your own.

# Download Checkpoints
Regardless of which scenario you use, after installing the above dependencies, we still need to manually download related checkpoints. Specific steps:
1. Install **huggingface-cli** using system environment or Conda python:  
`pip install "huggingface_hub[cli]"`  
Ensure the command **huggingface-cli** is available.
2. create weights and weights/hunyuanDiT folder.
3. Run in this node's directory:  
`huggingface-cli download tencent/Hunyuan3D-1 --local-dir ./weights`  
and  
`huggingface-cli download Tencent-Hunyuan/HunyuanDiT-v1.1-Diffusers-Distilled --local-dir ./weights/hunyuanDiT`
4. or if you prefer to run hunyuanDit natively in ComfyUI, download the checkpoint from [here](https://huggingface.co/comfyanonymous/hunyuan_dit_comfyui/blob/main/hunyuan_dit_1.2.safetensors), put it into your **ComfyUI/models/checkpoints** folder.

# Runtime
1. Output path is at **ComfyUI/output/Unique3D/Hunyuan3D-1/**

# Workflow
Here I provide three workflows:
- Text to 3D - native [example-text2mesh-native](workflow/example-text2mesh-native.json)
for this workflow:
1. make sure download hunyuanDit checkpoint and put it into checkpoints folder.
2. keep the negative prompt
3. keep the last three prompts **,白色背景,3D风格,最佳质量** and add your own prompts before them, for example：**a lovely rabbit eating carrots, 白色背景,3D风格,最佳质量**
- Text to 3D [example-text2mesh](workflow/example-text2mesh.json)
- Image to 3D [example-image2mesh](workflow/example-image2mesh.json)

Please understand the node usage in conjunction with the workflows.

# Known issue
Sometimes, ComfyUI will throw the error of **torch.OutOfMemoryError: Allocation on device** randomly while generating mesh.![img_2.png](img_2.png) 
However, if I run it again several times, then it could generate successfully. You can fix the seed to save time.

## Credit
- [Tencent/Hunyuan3D-1](https://github.com/Tencent/Hunyuan3D-1) - A Unified Framework for Text-to-3D and Image-to-3D Generation
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - A powerful and modular stable diffusion GUI.
- [ComfyUI-3D-Pack](https://github.com/MrForExample/ComfyUI-3D-Pack) - An extensive node suite that enables ComfyUI to process 3D inputs (Mesh & UV Texture, etc) using cutting edge algorithms (3DGS, NeRF, etc.)

## My extensions for ComfyUI
- [ComfyUI-Unique3D](https://github.com/jtydhr88/ComfyUI-Unique3D) - ComfyUI Unique3D is custom nodes that running Unique3D into ComfyUI
- [ComfyUI-LayerDivider](https://github.com/jtydhr88/ComfyUI-LayerDivider) - ComfyUI LayerDivider is custom nodes that generating layered psd files inside ComfyUI
- [ComfyUI-InstantMesh](https://github.com/jtydhr88/ComfyUI-InstantMesh) - ComfyUI InstantMesh is custom nodes that running InstantMesh into ComfyUI
- [ComfyUI-ImageMagick](https://github.com/jtydhr88/ComfyUI-ImageMagick) - This extension implements custom nodes that integreated ImageMagick into ComfyUI
- [ComfyUI-Workflow-Encrypt](https://github.com/jtydhr88/ComfyUI-Workflow-Encrypt) - Encrypt your comfyui workflow with key

## My extensions for stable diffusion webui
- [3D Model/pose loader](https://github.com/jtydhr88/sd-3dmodel-loader) A custom extension for AUTOMATIC1111/stable-diffusion-webui that allows you to load your local 3D model/animation inside webui, or edit pose as well, then send screenshot to txt2img or img2img as your ControlNet's reference image.
- [Canvas Editor](https://github.com/jtydhr88/sd-canvas-editor) A custom extension for AUTOMATIC1111/stable-diffusion-webui that integrated a full capability canvas editor which you can use layer, text, image, elements and so on, then send to ControlNet, basing on Polotno.
- [StableStudio Adapter](https://github.com/jtydhr88/sd-webui-StableStudio) A custom extension for AUTOMATIC1111/stable-diffusion-webui to extend rest APIs to do some local operations, using in StableStudio.
- [Txt/Img to 3D Model](https://github.com/jtydhr88/sd-webui-txt-img-to-3d-model) A custom extension for sd-webui that allow you to generate 3D model from txt or image, basing on OpenAI Shap-E.
- [3D Editor](https://github.com/jtydhr88/sd-webui-3d-editor) A custom extension for sd-webui that with 3D modeling features (add/edit basic elements, load your custom model, modify scene and so on), then send screenshot to txt2img or img2img as your ControlNet's reference image, basing on ThreeJS editor.
