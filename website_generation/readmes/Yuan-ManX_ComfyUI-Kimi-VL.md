# ComfyUI-Kimi-VL

Make Kimi-VL avialbe in ComfyUI.

[Kimi-VL](https://github.com/MoonshotAI/Kimi-VL): Mixture-of-Experts Vision-Language Model for Multimodal Reasoning, Long-Context Understanding, and Strong Agent Capabilities.


## Installation

1. Make sure you have ComfyUI installed

2. Clone this repository into your ComfyUI's custom_nodes directory:
```
cd ComfyUI/custom_nodes
git clone https://github.com/Yuan-ManX/ComfyUI-Kimi-VL.git
```

3. Install dependencies:
```
cd ComfyUI-Kimi-VL
pip install -r requirements.txt
```


## Model

🤗 For general multimodal perception and understanding, OCR, long video and long document, video perception, and agent uses, we recommend `Kimi-VL-A3B-Instruct` for efficient inference; for advanced text and multimodal reasoning (e.g. math), please consider using `Kimi-VL-A3B-Thinking`.

<div align="center">

| **Model** | **#Total Params** | **#Activated Params** | **Context Length** | **Download Link** |
| :------------: | :------------: | :------------: | :------------: | :------------: |
| Kimi-VL-A3B-Instruct | 16B | 3B | 128K   | [🤗 Hugging Face](https://huggingface.co/moonshotai/Kimi-VL-A3B-Instruct)   |
| Kimi-VL-A3B-Thinking  | 16B | 3B |  128K   | [🤗 Hugging Face](https://huggingface.co/moonshotai/Kimi-VL-A3B-Thinking)   |

</div>

> [!Note]
> Recommended parameter settings:
> - For **Thinking models**, it is recommended to use `Temperature = 0.6`. 
> - For **Instruct models**, it is recommended to use `Temperature = 0.2`. 
