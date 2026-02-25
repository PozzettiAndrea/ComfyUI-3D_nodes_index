# ComfyUI-Muyan-TTS

Make Muyan-TTS avialbe in ComfyUI.

[Muyan-TTS](https://github.com/MYZY-AI/Muyan-TTS) is a trainable TTS model designed for podcast applications within a $50,000 budget, which is pre-trained on over 100,000 hours of podcast audio data, enabling zero-shot TTS synthesis with high-quality voice generation. Furthermore, Muyan-TTS supports speaker adaptation with dozens of minutes of target speech, making it highly customizable for individual voices.


## Installation

1. Make sure you have ComfyUI installed

2. Clone this repository into your ComfyUI's custom_nodes directory:
```
cd ComfyUI/custom_nodes
git clone https://github.com/Yuan-ManX/ComfyUI-Muyan-TTS.git
```

3. Install dependencies:
```
cd ComfyUI-Muyan-TTS
pip install -r requirements.txt
```


## Model

### Model Download 

| Models   | Links   |
|-------|-------|
| Muyan-TTS   | [huggingface](https://huggingface.co/MYZY-AI/Muyan-TTS) \| [modelscope](https://modelscope.cn/models/MYZY-AI/Muyan-TTS)   |
| Muyan-TTS-SFT   | [huggingface](https://huggingface.co/MYZY-AI/Muyan-TTS-SFT) \| [modelscope](https://modelscope.cn/models/MYZY-AI/Muyan-TTS-SFT)   |

Additionally, you need to download the weights of [chinese-hubert-base](https://huggingface.co/TencentGameMate/chinese-hubert-base).

