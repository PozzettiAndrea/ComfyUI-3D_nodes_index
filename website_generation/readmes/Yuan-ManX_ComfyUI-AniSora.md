# ComfyUI-AniSora

ComfyUI-AniSora is now available in ComfyUI, [Index-AniSora](https://github.com/bilibili/Index-anisora) is the most powerful open-source animated video generation model. It enables one-click creation of video shots across diverse anime styles including series episodes, Chinese original animations, manga adaptations, VTuber content, anime PVs, mad-style parodies(鬼畜动画), and more!



## Installation

1. Make sure you have ComfyUI installed

2. Clone this repository into your ComfyUI's custom_nodes directory:
```
cd ComfyUI/custom_nodes
git clone https://github.com/Yuan-ManX/ComfyUI-AniSora.git
```

3. Install dependencies:
```
cd ComfyUI-AniSora
pip install -r req-fastvideo.txt
pip install -r requirements.txt
pip install -e .
```


## Model

### Download Pretrained Weights:

Please download AnisoraV2 checkpoints from [Huggingface](https://huggingface.co/IndexTeam/Index-anisora).

```
git lfs install
git clone https://huggingface.co/Wan-AI/Wan2.1-I2V-14B-480P
```

