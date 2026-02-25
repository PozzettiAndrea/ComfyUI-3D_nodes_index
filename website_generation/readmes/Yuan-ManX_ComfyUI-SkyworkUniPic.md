# ComfyUI-SkyworkUniPic

ComfyUI-SkyworkUniPic is now available in ComfyUI, [Skywork-UniPic](https://github.com/SkyworkAI/UniPic) is a unified autoregressive multimodal model with 1.5 billion parameters that natively integrates image understanding, text-to-image generation, and image editing capabilities within a single architecture.


## Installation

1. Make sure you have ComfyUI installed

2. Clone this repository into your ComfyUI's custom_nodes directory:
```
cd ComfyUI/custom_nodes
git clone https://github.com/Yuan-ManX/ComfyUI-SkyworkUniPic.git
```

3. Install dependencies:
```
cd ComfyUI-SkyworkUniPic
pip install -r requirements.txt
```

## Model

### Download Pretrained Models

Download the model checkpoints from [[🤗 SkyworkUniPic](https://huggingface.co/Skywork/Skywork-UniPic-1.5B)],
It is recommended to use the following command to download the checkpoints

```bash
# pip install -U "huggingface_hub[cli]"
huggingface-cli download Skywork/Skywork-UniPic-1.5B  --local-dir checkpoint --repo-type model
```
