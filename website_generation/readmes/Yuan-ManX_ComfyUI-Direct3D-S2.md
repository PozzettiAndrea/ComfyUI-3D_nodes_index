# ComfyUI-Direct3D-S2

ComfyUI-Direct3D‑S2 is now available in ComfyUI, [Direct3D‑S2](https://github.com/DreamTechAI/Direct3D-S2) - Gigascale 3D Generation Made Easy with Spatial Sparse Attention. Direct3D‑S2 is a scalable 3D generation framework based on sparse volumes that achieves superior output quality with dramatically reduced training costs.



## Installation

1. Make sure you have ComfyUI installed

2. Clone this repository into your ComfyUI's custom_nodes directory:
```
cd ComfyUI/custom_nodes
git clone https://github.com/Yuan-ManX/ComfyUI-Direct3D-S2.git
```

3. Install dependencies:
```
cd ComfyUI-Direct3D-S2

# Make sure the PyTorch CUDA version matches your installed CUDA Toolkit.
pip install torch==2.5.1 torchvision==0.20.1 --index-url https://download.pytorch.org/whl/cu121

# Torchsparse
git clone https://github.com/mit-han-lab/torchsparse
cd torchsparse && python -m pip install .

# Install dependencies
pip install -r requirements.txt
pip install -e .
```


## Model


### Download Pretrained Models


Direct3D-S2 Pretrained [Models](https://huggingface.co/wushuang98/Direct3D-S2)

