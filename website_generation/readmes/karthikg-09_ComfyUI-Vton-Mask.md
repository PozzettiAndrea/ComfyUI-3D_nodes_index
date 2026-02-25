# ComfyUI-Vton-Mask

A lightweight ComfyUI custom node for generating high-quality masks and pose detection for virtual try-on applications. This node extracts only the essential masking functionality from FitDiT without requiring heavy diffusion models.

## Features

- **Lightweight**: Only ~500MB vs 8-10GB for full models
- **Automatic Setup**: Models download automatically on first use
- **CPU Friendly**: Runs efficiently on CPU, no GPU required
- **High Quality**: Identical masking quality to full FitDiT
- **Simple Workflow**: Easy 2-node setup
- **Zero Configuration**: No manual model downloads needed

## Installation

1. Clone or download this repository
2. Place the `ComfyUI-Vton-Mask` folder in your `ComfyUI/custom_nodes/` directory
3. Restart ComfyUI
4. Models will download automatically on first use

### Git Installation
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/your-repo/ComfyUI-Vton-Mask.git
```

## Automatic Model Download

Models automatically download from [kg-09/kg-vton-mask](https://huggingface.co/kg-09/kg-vton-mask) on first use:

- **Download Size**: ~500MB
- **Location**: `ComfyUI/models/ComfyUI-Vton-Mask/`
- **One-Time Setup**: Models are cached locally after first download

## Usage

### Basic Workflow
```
LoadImage → ComfyUIVtonMaskLoader → ComfyUIVtonMaskGenerator → PreviewImage
```

### Nodes

**ComfyUIVtonMaskLoader**
- Loads masking models (auto-downloads if needed)
- Output: `COMFYUI_VTON_MASK_MODEL`

**ComfyUIVtonMaskGenerator**
- Inputs: mask_model, vton_image, category, offset parameters
- Outputs: masked_image, mask, pose_image
- Categories: Upper-body, Lower-body, Dresses

### Example Workflow
Load the included `comfyui_vton_mask_workflow.json` in ComfyUI.

## Parameters

- **category**: Upper-body, Lower-body, or Dresses
- **offset_top/bottom/left/right**: Fine-tune mask boundaries (-200 to +200)

## Technical Details

### Models Used
- DWpose Detection: Human pose keypoint detection
- Human Parsing: Semantic segmentation (ATR + LIP models)

### Memory Usage
| Component | ComfyUI-Vton-Mask | Full FitDiT |
|-----------|-------------------|-------------|
| Models | ~500MB | ~8-10GB |
| GPU Memory | 0-2GB | 8-12GB |
| Loading Time | ~10s | ~60s |

## Requirements

```
torch>=1.9.0
torchvision>=0.10.0
numpy>=1.21.0
opencv-python>=4.5.0
scikit-image>=0.18.0
onnxruntime>=1.8.0
transformers>=4.20.0
huggingface_hub>=0.16.0
```

## Troubleshooting

1. **Slow first download**: Models are ~500MB, check internet connection
2. **Download failed**: Manually download from https://huggingface.co/kg-09/kg-vton-mask
3. **Model not found**: Restart ComfyUI and verify files in `ComfyUI/models/ComfyUI-Vton-Mask/`
4. **Import errors**: Install requirements with `pip install -r requirements.txt`

## License

This project is based on FitDiT and follows the same licensing terms.

## Acknowledgments

This project is built upon the excellent work of:

- **FitDiT**: [BoyuanJiang/FitDiT](https://github.com/BoyuanJiang/FitDiT) - Original implementation of the virtual try-on pipeline
- **FitDiT Paper**: "FitDiT: Fit Diffusion Model for Virtual Try-On" - The foundational research that made this work possible
- **ComfyUI Community**: For providing the framework and ecosystem

We extend our gratitude to the original authors for their innovative work in virtual try-on technology. This lightweight masking node aims to make their research more accessible for specific use cases.

## Citation

If you use this work, please cite the original FitDiT paper:
```
@article{fitdit2024,
  title={FitDiT: Fit Diffusion Model for Virtual Try-On},
  author={[Original Authors]},
  journal={[Journal/Conference]},
  year={2024}
}
``` 