# ComfyUI-Dia

Make Dia avialbe in ComfyUI.

A TTS model capable of generating ultra-realistic dialogue in one pass.

[Dia](https://github.com/nari-labs/dia) is a 1.6B parameter text to speech model created by Nari Labs. Dia directly generates highly realistic dialogue from a transcript. You can condition the output on audio, enabling emotion and tone control. The model can also produce nonverbal communications like laughter, coughing, clearing throat, etc.



## Installation

1. Make sure you have ComfyUI installed

2. Clone this repository into your ComfyUI's custom_nodes directory:
```
cd ComfyUI/custom_nodes
git clone https://github.com/Yuan-ManX/ComfyUI-Dia.git
```

3. Install dependencies:
```
cd ComfyUI-Dia
pip install -r requirements.txt
```


## Model

Pretrained model checkpoints - The model weights are hosted on [Hugging Face](https://huggingface.co/nari-labs/Dia-1.6B). The model only supports English generation at the moment.

