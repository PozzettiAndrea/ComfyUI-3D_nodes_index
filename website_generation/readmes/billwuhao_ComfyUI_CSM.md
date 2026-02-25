[中文](README-CN.md)|[English](README.md)

# ComfyUI Node for CSM

CSM（Conversational Speech Model）, Clone voice, multi person conversation. Temporarily supports two person conversations.

## 📣 Update

[2025-05-29]⚒️: Re implement the core dialogue function.

[2025-03-18]⚒️: v1.0.0. 

## Preview

- The prompt and text format must be as follows:
```
[S1] Hi, how are you.
[S2] Fine, thank you, and you?
[S1] I'm fine, too.
[S2] What are you planning to do?
```

- Clone voice conversation and save speaker:
![](https://github.com/billwuhao/ComfyUI_CSM/blob/master/images/2025-03-18_15-38-45.png)

- Load saved speakers:
![](https://github.com/billwuhao/ComfyUI_CSM/blob/master/images/2025-03-18_19-01-15.png)


## Installation

```
cd ComfyUI/custom_nodes
git clone https://github.com/billwuhao/ComfyUI_CSM.git
cd ComfyUI_CSM
pip install -r requirements.txt

# python_embeded
./python_embeded/python.exe -m pip install -r requirements.txt
```

## Model Download

- [csm-1b](https://huggingface.co/sesame/csm-1b/tree/main): Download `config.json` and `model.safetensors` and place them in the `ComfyUI/models/TTS/csm-1b` directory.

- [moshiko-pytorch-bf16](https://huggingface.co/kyutai/moshiko-pytorch-bf16/tree/main): Download `tokenizer-e351c8d8-checkpoint125.safetensors` and place it in the `ComfyUI/models/TTS/moshiko-pytorch-bf16` directory.

- [Llama-3.2-1B](https://huggingface.co/meta-llama/Llama-3.2-1B/tree/main): Download everything except the `original` directory and place it in the `ComfyUI\models\LLM\Llama-3.2-1B` directory.

## Acknowledgements

[csm](https://github.com/SesameAILabs/csm)

Thanks to the SesameAILabs team for their excellent work 👍.
