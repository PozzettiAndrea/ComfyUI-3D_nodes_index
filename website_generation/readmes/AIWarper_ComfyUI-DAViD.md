# ComfyUI-DAViD

Custom nodes for [DAViD (Data-efficient and Accurate Vision Models from Synthetic Data)](https://microsoft.github.io/DAViD) models in ComfyUI. These nodes enable depth estimation, surface normal estimation, and soft foreground segmentation for human-centric images.

PLEASE NOTE: AS CONFIRMED BY THE RESEARCH TEAM THIS WAS NOT TRAINED TO BE TEMPORALLY STABLE ACROSS VIDEO FRAMES.

## 🌟 Features

- **Multi-Task Processing**: Get depth, normal, and foreground masks in a single node
- **High Quality**: State-of-the-art results for human subjects
- **GPU Accelerated**: Full ONNX Runtime GPU support
- **Batch Processing**: Process multiple images efficiently
- **Flexible Outputs**: Choose between raw outputs or visualization-ready formats

## 📦 Installation

### Method 1: ComfyUI Manager (NOT ADDED YET - USE METHOD 2 FOR NOW)

1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager) if you haven't already
2. Search for "DAViD" in the ComfyUI Manager
3. Click Install

### Method 2: Manual Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ComfyUI-DAViD.git
   ```

3. Install dependencies (BEFORE DOING THIS TRY LAUNCHING COMFY AND SEEING WHICH DEPENDENCIES YOU ARE MISSING FROM THE TERMINAL OUTPUT. INSTALL ONLY THE ONES REQUIRED):
   ```bash
   cd ComfyUI-DAViD
   pip install -r requirements.txt
   ```

## 📥 Model Download

The DAViD models need to be downloaded separately:

1. Create the models directory:
   ```bash
   mkdir -p ComfyUI-DAViD/models/david
   ```

2. Download the multi-task model:
   ```bash
   # Multi-task model (recommended - all three tasks in one model)
   wget https://facesyntheticspubwedata.z6.web.core.windows.net/iccv-2025/models/multi-task-model-vitl16_384.onnx -O ComfyUI-DAViD/models/david/multitask-vitl16_384.onnx
   ```

3. (Optional) Download individual task models:
   ```bash
   # Depth estimation models
   wget https://facesyntheticspubwedata.z6.web.core.windows.net/iccv-2025/models/depth-model-vitb16_384.onnx -O ComfyUI-DAViD/models/david/depth-vitb16_384.onnx
   wget https://facesyntheticspubwedata.z6.web.core.windows.net/iccv-2025/models/depth-model-vitl16_384.onnx -O ComfyUI-DAViD/models/david/depth-vitl16_384.onnx
   
   # Surface normal models
   wget https://facesyntheticspubwedata.z6.web.core.windows.net/iccv-2025/models/normal-model-vitb16_384.onnx -O ComfyUI-DAViD/models/david/normal-vitb16_384.onnx
   wget https://facesyntheticspubwedata.z6.web.core.windows.net/iccv-2025/models/normal-model-vitl16_384.onnx -O ComfyUI-DAViD/models/david/normal-vitl16_384.onnx
   
   # Foreground segmentation models  
   wget https://facesyntheticspubwedata.z6.web.core.windows.net/iccv-2025/models/foreground-segmentation-model-vitb16_384.onnx -O ComfyUI-DAViD/models/david/foreground-vitb16_384.onnx
   wget https://facesyntheticspubwedata.z6.web.core.windows.net/iccv-2025/models/foreground-segmentation-model-vitl16_384.onnx -O ComfyUI-DAViD/models/david/foreground-vitl16_384.onnx
   ```

## 🚀 Usage

### DAViD Multi-Task Node

The main node that performs all three tasks in a single inference:

**Inputs:**
- `image`: Input image (RGB)
- `model_name`: Model to use (default: multitask-vitl16_384.onnx)
- `inverse_depth`: Invert depth values (closer = higher)
- `binarize_foreground`: Convert soft mask to binary
- `foreground_threshold`: Threshold for binarization (0.0-1.0)

**Outputs:**
- `depth_map`: Colored depth visualization (TURBO colormap)
- `normal_map`: Surface normal map (RGB visualization)
- `foreground_rgb`: Foreground mask as RGB image
- `foreground_mask`: Raw foreground mask (single channel)

### Example Workflows

#### Basic Human Processing
```
Load Image → DAViD Multi-Task → Save Image (depth)
                              → Save Image (normal)
                              → Save Image (foreground)
```

#### Background Replacement
```
Load Image → DAViD Multi-Task → 
                ↓ (foreground_mask)
            → Image Composite (with new background) → Save Image
```

#### Depth-based Effects
```
Load Image → DAViD Multi-Task →
                ↓ (depth_map)
            → Depth Blur → Save Image
```

## 🎯 Use Cases

- **Portrait Enhancement**: Extract clean foreground masks for background replacement
- **3D Effects**: Use depth maps for bokeh, fog, or depth-of-field effects
- **Relighting**: Apply new lighting using surface normals
- **Virtual Production**: Green screen alternative using AI segmentation
- **AR/VR**: Depth and normal data for 3D reconstruction
- **Style Transfer**: Use masks to apply effects selectively

## 🛠️ Troubleshooting

### ONNX Runtime Issues
If you encounter ONNX Runtime errors:
```bash
pip uninstall onnxruntime onnxruntime-gpu
pip install onnxruntime-gpu==1.16.3
```

### CUDA/GPU Issues
Ensure CUDA is properly installed and matches your PyTorch version:
```python
import torch
print(torch.cuda.is_available())  # Should return True
```

### Model Not Found
Ensure models are in the correct directory:
```
ComfyUI-DAViD/models/david/multitask-vitl16_384.onnx
```

## 🙏 Acknowledgments

- Original DAViD paper and models by Microsoft Research
- ComfyUI framework by comfyanonymous

## 📄 License

This custom node implementation is licensed under MIT License.
The DAViD models are licensed under their respective licenses (see original repository).

## 🔗 Links

- [DAViD Paper](https://arxiv.org/abs/2507.15365)
- [DAViD Project Page](https://microsoft.github.io/DAViD)
- [Original Repository](https://github.com/microsoft/DAViD)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)

## 📝 Citation

If you use these nodes in your research, please cite:
```bibtex
@misc{saleh2025david,
    title={{DAViD}: Data-efficient and Accurate Vision Models from Synthetic Data},
    author={Fatemeh Saleh and others},
    year={2025},
    eprint={2507.15365},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
}
``` 