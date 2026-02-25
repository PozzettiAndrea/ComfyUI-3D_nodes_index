# ComfyUI_RH_mammothmoda

ComfyUI custom nodes for MammothModa2 text-to-image generation.

## Features

- **Text-to-Image Generation**: High-quality image synthesis using MammothModa2
- **Optimized Performance**: INT8 quantization support for efficient inference
- **Flash Attention**: Enhanced speed with flash_attention_2

## Installation

### Via ComfyUI Manager (Recommended)
Search for "RunningHub Mammothmoda" in ComfyUI Manager and install.

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/HM-RunningHub/ComfyUI_RH_mammothmoda.git
cd ComfyUI_RH_mammothmoda
pip install -r requirements.txt
```

## Model Download

Download the MammothModa2-Preview model from [🤗 HuggingFace](https://huggingface.co/bytedance-research/MammothModa2-Preview) and place it in:
```
ComfyUI/models/MammothModa2-Preview/
```

## Usage

1. **Load Model**: Use "RunningHub Mammothmoda Loader" node
2. **Generate Image**: Connect to "RunningHub Mammothmoda T2I Sampler" node
3. **Configure**: Set prompt, size (width/height), steps, and guidance scales
4. **Run**: Execute workflow to generate images

## Nodes

- **RunningHub Mammothmoda Loader**: Loads the MammothModa2 model
- **RunningHub Mammothmoda T2I Sampler**: Generates images from text prompts

## Requirements

- CUDA-capable GPU (24GB VRAM recommended)
- PyTorch with CUDA support
- flash-attn package

## Acknowledgement

This project is based on [MammothModa2](https://huggingface.co/bytedance-research/MammothModa2-Preview) by ByteDance Research. We are grateful to the MammothModa team for their excellent work.

- **Original Project**: [MammothModa2](https://github.com/bytedance/mammothmoda)
- **Model**: [MammothModa2-Preview](https://huggingface.co/bytedance-research/MammothModa2-Preview)
- **License**: [Apache-2.0](https://opensource.org/licenses/Apache-2.0)

## Citation

```bibtex
@misc{mammothmoda2025,
    title = {MammothModa2: Jointly Optimized Autoregressive-Diffusion Models for Unified Multimodal Understanding and Generation},
    author = {MammothModa Team},
    year = {2025},
    url = {https://github.com/bytedance/mammothmoda}
}
```

## License

Apache-2.0

