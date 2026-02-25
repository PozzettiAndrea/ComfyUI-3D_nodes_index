# ComfyUI-Sa2VAWrapper

A custom ComfyUI node that implements the ByteDance [Sa2VA](https://huggingface.co/ByteDance/Sa2VA-8B) model, enabling video captioning and segmentation capabilities within ComfyUI.

## Description

This extension integrates [Sa2VA](https://huggingface.co/ByteDance/Sa2VA-8B) into ComfyUI, allowing you to generate detailed descriptions of video frames. Sa2VA-8B is a multimodal model developed by ByteDance that can understand video content and generate natural language descriptions.

WIP:
- [ ] Add a node that can take a gif 
- [ ] Add node that implements segmentation

## Features

- Process sequences of images to generate detailed captions
- Customizable prompting to guide the model's description
- Seamless integration with ComfyUI workflow
- GPU-accelerated inference with Flash Attention support

## Installation

### Prerequisites

- ComfyUI installation

### Method 1: Via ComfyUI Manager

1. Open ComfyUI Manager
2. Search for "Sa2VAWrapper"
3. Click Install

### Method 2: Manual Installation

```
WORKDIR /comfyui/custom_nodes
RUN git clone https://github.com/pablerdo/ComfyUI-Sa2VAWrapper.git --recursive
WORKDIR /comfyui/custom_nodes/ComfyUI-Sa2VAWrapper
RUN git reset --hard (commit hash)
RUN if [ -f requirements.txt ]; then python -m pip install -r requirements.txt; fi
RUN if [ -f install.py ]; then python install.py || echo "install script failed"; fi
```