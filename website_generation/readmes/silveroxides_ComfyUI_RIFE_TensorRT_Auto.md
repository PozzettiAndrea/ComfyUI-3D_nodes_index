<div align="center">

# ComfyUI Rife TensorRT ⚡

[![python](https://img.shields.io/badge/python-3.12-green)](https://www.python.org/downloads/)
[![cuda](https://img.shields.io/badge/cuda-13.0-green)](https://developer.nvidia.com/cuda-13-0-2-download-archive)
[![trt](https://img.shields.io/badge/TRT-10.14.1.48-green)](https://developer.nvidia.com/tensorrt)
[![by-nc-sa/4.0](https://img.shields.io/badge/license-CC--BY--NC--SA--4.0-lightgrey)](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en)

![node](https://github.com/user-attachments/assets/5fd6d529-300c-42a5-b9cf-46e031f0bcb5)


</div>

This project provides a [TensorRT](https://github.com/NVIDIA/TensorRT) implementation of [RIFE](https://github.com/hzwer/ECCV2022-RIFE) for ultra fast frame interpolation inside ComfyUI

This project is licensed under [CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/), everyone is FREE to access, use, modify and redistribute with the same license.

If you like the project, please give me a star! ⭐

---

## ⏱️ Performance

_Note: The following results were benchmarked on FP16 engines inside ComfyUI, using 2000 frames consisting of 2 alternating similar frames, averaged 2-3 times_

| Device | Rife Engine | Resolution| Multiplier | FPS |
| :----: | :-: | :-: | :-: | :-: |
|  H100  | rife49_ensemble_True_scale_1_sim | 512 x 512  | 2 | 45 |
|  H100  | rife49_ensemble_True_scale_1_sim | 512 x 512  | 4 | 57 |
|  H100  | rife49_ensemble_True_scale_1_sim | 1280 x 1280  | 2 | 21 |

## 🚀 Installation

Navigate to the ComfyUI `/custom_nodes` directory

```bash
git clone https://github.com/yuvraj108c/ComfyUI-Rife-Tensorrt
cd ./ComfyUI-Rife-Tensorrt
pip install -r requirements.txt
```

### ⚠️ CUDA Version Selection

This node defaults to **CUDA 13** (RTX 50 series, driver 580+).

**For CUDA 12 (RTX 30/40 series):**
```bash
pip install -r requirements_cu12.txt
```

**For CUDA 13 (Default):**
```bash
pip install -r requirements.txt
```

### 📦 CUDA Toolkit Required

The node automatically detects your CUDA installation via `CUDA_PATH` or `CUDA_HOME` environment variables.

If CUDA is not detected, download from: https://developer.nvidia.com/cuda-13-0-2-download-archive

### 🎯 Resolution Profiles

The node supports resolution profiles to optimize VRAM usage:
- **small**: 480-896px (recommended for most video generation)
- **medium**: 720-1280px (for higher resolution videos)
- **custom**: Connect a "RIFE Custom Resolution Config" node for manual control

The following RIFE models are supported and will be automatically downloaded and built:
   - **rife49_ensemble_True_scale_1_sim** (default) - Latest and most accurate
   - **rife48_ensemble_True_scale_1_sim** - Good balance of speed and quality
   - **rife47_ensemble_True_scale_1_sim** - Fastest option

Models are automatically downloaded from [HuggingFace](https://huggingface.co/yuvraj108c/rife-onnx) and TensorRT engines are built on first use.

## ☀️ Usage

1. **Load Model**: Insert `Right Click -> Add Node -> tensorrt -> Load Rife Tensorrt Model`
   - Choose your preferred RIFE model (rife47, rife48, or rife49)
   - Select precision (fp16 recommended for speed, fp32 for maximum accuracy)
   - Select resolution profile (small, medium, or custom)
   - The model will be automatically downloaded and TensorRT engine built on first use

2. **Process Frames**: Insert `Right Click -> Add Node -> tensorrt -> Rife Tensorrt`
   - Connect the loaded model from step 1
   - Input your video frames
   - Configure interpolation settings (multiplier, CUDA graph, etc.)

## 🤖 Environment tested

- Windows 11, CUDA 13.0, TensorRT 10.14.1.48, Python 3.12, RTX 5070 Ti
- WSL Ubuntu 24.04.03 LTS, CUDA 12.9, TensorRT 10.13.3.9, Python 3.12.11, RTX 5080

## 🚨 Updates

### January 2026
- **CUDA 13 Default**: Updated to CUDA 13.0 and TensorRT 10.14.1.48
- **Auto CUDA Detection**: Automatically finds CUDA toolkit and DLL paths
- **Resolution Profiles**: Added small/medium/custom profiles to reduce VRAM usage

### December 2025
- **Automatic Model Management**: No more manual downloads! Models are automatically downloaded from HuggingFace and TensorRT engines are built on demand
- **Improved Workflow**: New two-node system with `Load Rife Tensorrt Model` + `Rife Tensorrt` for better organization
- **Updated Dependencies**: TensorRT updated to 10.13.3.9 for better performance and compatibility

## 👏 Credits

- https://github.com/styler00dollar/VSGAN-tensorrt-docker
- https://github.com/Fannovel16/ComfyUI-Frame-Interpolation
- https://github.com/hzwer/ECCV2022-RIFE

## License

[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
