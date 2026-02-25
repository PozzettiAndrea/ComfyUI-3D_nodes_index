[中文](README-CN.md)|[English](README.md)

# ComfyUI Node for parakeet-tdt-0.6b-v2

An accurate and fast automatic speech recognition (ASR) model. Designed for high-quality English transcription, supporting punctuation, capitalization, and accurate timestamp prediction.

![](https://github.com/billwuhao/ComfyUI_parakeet-tdt/blob/main/images/20250520010321.png)

## Usage

- Quickly add captions:
![](https://github.com/billwuhao/ComfyUI_parakeet-tdt/blob/main/images/2025-05-20_10-36-53.png)


## 📣 Updates

[2025-05-20]⚒️: Released v1.0.0.

## Installation

```
cd ComfyUI/custom_nodes
git clone https://github.com/billwuhao/ComfyUI_parakeet-tdt.git
cd ComfyUI_parakeet-tdt
pip install -r requirements.txt

# Linux
pip install nemo_toolkit['asr']

# Windows
git clone https://github.com/NVIDIA/NeMo
cd NeMo
pip install '.[asr]'
```
If an error occurs: `RuntimeError: CUDA error: operation not supported`. Add `--disable-cuda-malloc` to the ComfyUI launch parameters, for example:
```
.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --disable-cuda-malloc
```

## Model Download

- [parakeet-tdt-0.6b-v2.nemo](https://huggingface.co//nvidia/parakeet-tdt-0.6b-v2/blob/main/parakeet-tdt-0.6b-v2.nemo): Download and place it in the `ComfyUI/models/TTS` directory.

## Acknowledgments

[NeMo](https://github.com/NVIDIA/NeMo)
