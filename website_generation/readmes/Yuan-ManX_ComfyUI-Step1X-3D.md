# ComfyUI-Step1X-3D

ComfyUI-Step1X-3D is now available in ComfyUI, delivering high-fidelity 3D asset generation with consistent geometry-texture alignment. It supports multi-style outputs: cartoon, sketch, and photorealistic.

[Step1X-3D](https://github.com/stepfun-ai/Step1X-3D): Towards High-Fidelity and Controllable Generation of Textured 3D Assets.


## Installation

1. Make sure you have ComfyUI installed

2. Clone this repository into your ComfyUI's custom_nodes directory:
```
cd ComfyUI/custom_nodes
git clone https://github.com/Yuan-ManX/ComfyUI-Step1X-3D.git
```

3. Install dependencies:
```
cd ComfyUI-Step1X-3D

pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu124
pip install -r requirements.txt
pip install torch-cluster -f https://data.pyg.org/whl/torch-2.5.1+cu124.html

cd step1x3d_texture/custom_rasterizer
python setup.py install
cd ../differentiable_renderer
python setup.py install
```


## Model

### Models Downloading

| Model                       | Download link                   | Size       | Update date |                                                                                     
|-----------------------------|-------------------------------|------------|------|
| Step1X-3D-geometry| 🤗 [Huggingface](https://huggingface.co/stepfun-ai/Step1X-3D/tree/main/Step1X-3D-Geometry-1300m)    | 1.3B | 2025-05-13  | 
| Step1X-3D-geometry-label  | 🤗 [Huggingface](https://huggingface.co/stepfun-ai/Step1X-3D/tree/main/Step1X-3D-Geometry-Label-1300m) | 1.3B | 2025-05-13|
| Step1X-3D Texture       | 🤗 [Huggingface](https://huggingface.co/stepfun-ai/Step1X-3D/tree/main/Step1X-3D-Texture)    | 3.5B |2025-05-13|
|Models in ModelScope |🤗 [ModelScope](https://www.modelscope.cn/models/stepfun-ai/Step1X-3D) | 6.1B | 2025-05-14|

### Open filtered high quaily datasets 

| Data source                       | Download link                   | Size       | Update date |                                                                                    
|-----------------------------|-------------------------------|------------|------|
| Objaverse| 🤖[Huggingface](https://huggingface.co/datasets/stepfun-ai/Step1X-3D-obj-data/blob/main/objaverse_320k.json)    | 320K |2025-05-13|
| Objaverse-XL  | 🤖[Huggingface](https://huggingface.co/datasets/stepfun-ai/Step1X-3D-obj-data/blob/main/objaverse_xl_github_url_480k.json) | 480K |2025-05-13|
| Assets for texture synthesis | 🤖[Huggingface](https://huggingface.co/datasets/stepfun-ai/Step1X-3D-obj-data/blob/main/objaverse_texture_30k.json) | 30K |2025-05-13|
| Assets in ModelScope| 🤖[ModelScope](https://www.modelscope.cn/datasets/stepfun-ai/Step1X-3D-obj-data) | 830K |2025-05-14|

Given the above high quality 3D assets, you can follow methods from [Dora](https://github.com/Seed3D/Dora/tree/main) to preprocess data for VAE and 3D DiT training, and from [MV-Adapter](https://github.com/huanngzh/MV-Adapter) for ig2mv training.

