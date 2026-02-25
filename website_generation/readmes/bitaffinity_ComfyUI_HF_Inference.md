# Hugging Face hosted inference nodes for ComfyUI

Unofficial ComfyUI nodes for Hugging Face's inference API

Visit [the official docs](https://huggingface.co/docs/api-inference/detailed_parameters) for an overview of how the HF inference endpoints work

Find models by task on the [official website](https://huggingface.co/tasks)

## Installation

### Clone and install dependencies
```
git clone https://github.com/bitaffinity/ComfyUI_HF_Inference custom_nodes/ComfyUI_HF_Inference
cd custom_nodes/ComfyUI_HF_Inference
pip install -r requirements.txt
```

Export HF_AUTH_TOKEN with one of your [Hugging Face tokens](https://huggingface.co/settings/tokens)

### Run ComfyUI
`HF_AUTH_TOKEN=hf_1111111111111111111111111111111111 python main.py`

## Nodes

> [!WARNING]
> Inference API (serverless) requires a model 10GB or below and fails for random reasons on different models.

### Text

* Feature Extraction
    - [facebook/bart-base](https://huggingface.co/facebook/bart-base)
* Question Answering
    - [deepset/roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2)
* Translation
    - [google-t5/t5-base](https://huggingface.co/google-t5/t5-base)
* Generation
    - [HuggingFaceH4/zephyr-7b-beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta)

### Image

* Classification
    - [google/vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224)
* Object Detection
    - [facebook/detr-resnet-50](https://huggingface.co/facebook/detr-resnet-50)
* Segmentation
    - [facebook/detr-resnet-50-panoptic](https://huggingface.co/facebook/detr-resnet-50-panoptic)
* TextToImage
    - [sd-community/sdxl-flash](https://huggingface.co/sd-community/sdxl-flash)