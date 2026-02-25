# ComfyUI Wrapper nodes for STAR Video Super-Resolution

A ComfyUI custom node wrapper for [STAR (Spatial-Temporal Augmentation with Text-to-Video Models for Real-World Video Super-Resolution)](https://github.com/NJU-PCALab/STAR), enabling high-quality video upscaling with AI-powered super-resolution.

## Overview

This node provides an easy-to-use interface for the STAR video super-resolution model within ComfyUI. STAR can upscale low-resolution videos by 2x-4x while preserving and enhancing details, with specialized models for light and heavy degradation scenarios.

## Features

- **Two Degradation Models**: Choose between Light and Heavy degradation models optimized for different video quality levels
- **Flexible Upscaling**: Use target Resolution for upscaling.
- **Text Prompting**: Guide the enhancement with text descriptions
- **Advanced Sampling**: Multiple samplers (heun, dpmpp_2m_sde) and solver modes
- **Automatic Model Download**: Models are automatically downloaded from Hugging Face Hub on first use
- **ComfyUI Integration**: Seamless integration with ComfyUI workflows

## Installation


1. Install xformers before installing this custom nodes please check xformers version which match with currnet pytorch at https://github.com/facebookresearch/xformers/releases .

2. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

3. Clone this repository:
```bash
git clone https://github.com/vjumpkung/ComfyUI-STARWrapper.git
```

4. Install dependencies:
```bash
cd ComfyUI-STARWrapper
pip install -r requirements.txt
```

5. Restart ComfyUI

## Alternative Install

1. Search in ComfyUI-Manager name `ComfyUI-STARWrapper` then click install.

## Usage

1. In ComfyUI, find the node under **video/upscaling** → **STAR Video Super Resolution**
2. Connect your video frames (as IMAGE tensors) to the input
3. Configure the parameters:
   - **Model**: Choose "Light Degradation" or "Heavy Degradation"
   - **Prompt**: Describe the desired output (e.g., "a high quality video")
   - **Resolution**: Target Resolution (720p, 1080p, 2160p, ...)
   - **Steps**: Number of denoising steps (15-50 recommended)
   - **CFG**: Guidance scale (7.5 default)
   - **Sampler**: Choose sampling method
   - **Max Chunk Length**: For long videos, process in chunks (32 default)
4. The node outputs upscaled video frames

## Parameters

| Parameter     | Description                   | Default           | Range             |
| ------------- | ----------------------------- | ----------------- | ----------------- |
| model         | Degradation type              | Light Degradation | Light/Heavy       |
| prompt        | Text guidance for enhancement | "a good video"    | -                 |
| resolution    | Target Resolution             | 720               | 16-16384          |
| max_chunk_len | Maximum frames per chunk      | 32                | 1-128             |
| cfg           | Guidance scale                | 7.5               | 0.0-20.0          |
| sampler       | Sampling method               | dpmpp_2m_sde      | heun/dpmpp_2m_sde |
| solver_mode   | Solver speed                  | fast              | fast/normal       |
| steps         | Denoising steps               | 15                | 1-100             |
| seed          | Random seed                   | 42                | 0-2^64            |

## Requirements

- Python 3.8+
- PyTorch with CUDA support
- xformers (CUDA13 is not working)
- ComfyUI
- See [requirements.txt](requirements.txt) for full dependencies

## Models

Models are automatically downloaded from the [SherryX/STAR](https://huggingface.co/SherryX/STAR) Hugging Face repository:
- **Light Degradation**: `I2VGen-XL-based/light_deg.pt`
- **Heavy Degradation**: `I2VGen-XL-based/heavy_deg.pt`

Downloaded models are cached in `./models/STAR/` directory.

## Credits

This is a ComfyUI wrapper for the original STAR project:

**STAR (Spatial-Temporal Augmentation with Text-to-Video Models for Real-World Video Super-Resolution)**
- Original Repository: https://github.com/NJU-PCALab/STAR
- Developed by: NJU-PCALab (Nanjing University)
- Paper: [STAR (Spatial-Temporal Augmentation with Text-to-Video Models for Real-World Video Super-Resolution)](https://arxiv.org/pdf/2501.02976)

Please cite the original work if you use this in research:
```bibtex
@misc{xie2025starspatialtemporalaugmentationtexttovideo,
      title={STAR: Spatial-Temporal Augmentation with Text-to-Video Models for Real-World Video Super-Resolution}, 
      author={Rui Xie and Yinhong Liu and Penghao Zhou and Chen Zhao and Jun Zhou and Kai Zhang and Zhenyu Zhang and Jian Yang and Zhenheng Yang and Ying Tai},
      year={2025},
      eprint={2501.02976},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2501.02976}, 
}
```

### Third-Party Components

This wrapper also uses:
- Color correction adapted from [sd-webui-stablesr](https://github.com/pkuliyi2015/sd-webui-stablesr) by Li Yi
- Stable Video Diffusion VAE from [Stability AI](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid)
- OpenCLIP text encoder

## License

This wrapper follows the license of the original STAR project. Please refer to the [original repository](https://github.com/NJU-PCALab/STAR) for licensing details.

## Troubleshooting

### CUDA Out of Memory
- Reduce `max_chunk_len` to process fewer frames at once
- Lower the target resolution.
- Process shorter video segments

### Model Download Issues
- Ensure you have internet connection for first-time model download
- Check Hugging Face Hub accessibility
- Models are ~2-3GB each, ensure sufficient disk space

### Color Artifacts
- The node automatically applies AdaIN color correction
- Try adjusting the prompt for better color guidance
- Experiment with different CFG values

## Contributing

Contributions are welcome! Please ensure:
- Code follows the existing style (uses ruff for formatting)
- Test with both degradation models
- Update documentation for new features

## Support

For issues related to:
- **This ComfyUI wrapper**: Open an issue in this repository
- **The STAR model itself**: Refer to the [original STAR repository](https://github.com/NJU-PCALab/STAR)
