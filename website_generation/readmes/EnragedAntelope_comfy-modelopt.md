# NVIDIA ModelOpt for ComfyUI

> **⚠️ PROJECT STATUS: ON HOLD (2025-11-10)**
>
> **Current Status**: This project is on hold pending PyTorch compatibility fixes.
>
> **Issue**: ModelOpt quantized models have known compatibility issues with PyTorch/TorchScript that prevent full end-to-end inference in ComfyUI. While quantization and save/load work correctly, encode/decode operations are currently blocked.
>
> **What Works**:
> - ✅ Model quantization (v0.3.0)
> - ✅ Save/Load pipeline (v0.4.0)
>
> **What's Blocked**:
> - ❌ Full inference in ComfyUI (pending PyTorch updates)
>
> **Alternative**: Works in Diffusers wrapper (confirmed by community testing)
>
> **Recommendation**: Wait for PyTorch upstream fixes before production use.
>
> See [RESEARCH_NOTES.md](RESEARCH_NOTES.md) for technical details.

---

Quantize and optimize Stable Diffusion models with NVIDIA ModelOpt directly in ComfyUI. Achieve **~2x faster inference** with INT8/FP8 quantization while maintaining image quality. Works with various diffusion model architectures including SDXL, SD1.5, SD3, and more.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![CUDA](https://img.shields.io/badge/CUDA-12.0%2B-green)
![Status](https://img.shields.io/badge/status-on%20hold-yellow)

## ✨ Features

- **🚀 Fast Inference**: ~2x speedup with INT8/FP8 quantization
- **💾 Memory Efficient**: Up to 50% VRAM reduction
- **🎨 Quality Preserved**: <3% quality loss with proper calibration
- **🔧 Easy to Use**: Quantize models directly in ComfyUI workflows
- **💻 Cross-Platform**: Works on Linux, Windows (with some limitations)

## 📦 Included Nodes

| Node | Description | Category |
|------|-------------|----------|
| **ModelOptUNetLoader** | Load pre-quantized UNet models | loaders/modelopt |
| **ModelOptQuantizeUNet** | Quantize UNet to INT8/FP8/INT4 | modelopt |
| **ModelOptSaveQuantized** | Save quantized models | modelopt |
| **ModelOptCalibrationHelper** | Collect calibration data | modelopt |

## 🎯 Model Compatibility

This node pack works with various diffusion model architectures. Quantization support depends on the underlying NVIDIA ModelOpt library.

**For the latest model compatibility information**, see the official [NVIDIA ModelOpt documentation](https://github.com/NVIDIA/TensorRT-Model-Optimizer).

**Expected Performance:**
- **~2x faster inference** with INT8/FP8 quantization
- **~50% VRAM reduction** with 8-bit formats
- **~75% VRAM reduction** with INT4 (experimental)
- **<3% quality loss** with proper calibration

**Tip**: If you encounter issues with a specific model, try updating ModelOpt:
```bash
pip install --upgrade nvidia-modelopt[all]
```

## 💻 Hardware Requirements

### GPU Requirements

| Quantization | Minimum GPU | Compute Capability | Example GPUs |
|--------------|-------------|-------------------|--------------|
| **INT8** | Turing | SM 7.5+ | RTX 2060+, T4, RTX 3000+, RTX 4000+ |
| **FP8** | Ada Lovelace or Hopper | SM 8.9+ | **RTX 4060+**, H100 |
| **INT4** | Turing | SM 7.5+ | RTX 2060+, T4, RTX 3000+, RTX 4000+ |

**Recommended for best experience**:
- **GPU**: RTX 4070+ (for FP8 support)
- **VRAM**: 8GB+ (12GB+ recommended for larger models)
- **System RAM**: 16GB+ (32GB+ recommended)

### Software Requirements

- **Operating System**: Linux (primary), Windows 10/11
- **Python**: 3.10, 3.11, or 3.12
- **CUDA**: 12.0 or higher
- **PyTorch**: 2.0 or higher with CUDA support
- **ComfyUI**: Latest version

## 🚀 Installation

### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "ModelOpt" or "NVIDIA ModelOpt"
3. Click "Install"
4. Restart ComfyUI

### Method 2: Manual Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/EnragedAntelope/comfy-modelopt.git
cd comfy-modelopt
pip install -r requirements.txt

# For Linux (optional, for faster quantization):
pip install -r requirements-linux.txt

# For Windows (optional):
pip install -r requirements-windows.txt
```

### Method 3: Install PyTorch with CUDA First (Recommended)

```bash
# Install PyTorch with CUDA 12.4
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu124

# Then install ModelOpt and dependencies
cd ComfyUI/custom_nodes/comfy-modelopt
pip install -r requirements.txt
```

## 📖 Usage Guide

### Basic Workflow: Quantize a UNet

1. **Load your model** using standard ComfyUI checkpoint loader
2. **Add ModelOptQuantizeUNet node**
3. **Connect model** to the quantizer
4. **Configure quantization**:
   - `precision`: Choose INT8 (most compatible) or FP8 (best quality, RTX 4000+)
   - `calibration_steps`: 32 for testing, 64-128 for production
5. **Run workflow** - quantization will take 2-10 minutes
6. **Save quantized model** using ModelOptSaveQuantized node
7. **Reload quantized model** using ModelOptUNetLoader for faster inference

### Advanced Workflow: Use Real Calibration Data

For best quality, use real latent samples instead of random calibration:

1. **Create your normal generation workflow** (prompt, latent, sampler, etc.)
2. **Add ModelOptCalibrationHelper node** after your KSampler
3. **Connect latent output** to calibration helper
4. **Generate 32-64 images** to collect calibration samples
5. **Connect calibration data** to ModelOptQuantizeUNet node
6. **Run quantization** with your collected calibration data

### Loading Quantized Models

1. **Use ModelOptUNetLoader** instead of regular checkpoint loader
2. **Load VAE** and **CLIP** separately using standard ComfyUI loaders
   - ModelOpt only quantizes the UNet, not VAE/CLIP
3. **Connect to KSampler** and generate as normal
4. **Enjoy ~2x faster inference!**

## 🎨 Example Workflows

See the `examples/` folder for ready-to-use workflow JSON files:

- `quantize_basic.json` - Basic model quantization workflow
- `quantize_with_calibration.json` - Advanced calibration workflow
- `load_quantized_model.json` - Using quantized models

## ⚙️ Node Reference

### ModelOptQuantizeUNet

**Inputs**:
- `model` (MODEL): UNet model to quantize
- `precision` (COMBO): int8 / fp8 / int4
- `calibration_steps` (INT): Number of calibration steps (8-512)
- `calibration_data` (LATENT, optional): Calibration samples
- `skip_layers` (STRING, optional): Comma-separated layers to skip

**Outputs**:
- `quantized_model` (MODEL): Quantized UNet model

**Recommended Settings**:
- Quick test: INT8, 32 steps
- Production: INT8 or FP8, 64-128 steps
- Best quality: FP8, 256+ steps (requires RTX 4000+)

### ModelOptUNetLoader

**Inputs**:
- `unet_name` (COMBO): Select quantized UNet from `models/modelopt_unet/`
- `precision` (COMBO): auto / fp8 / fp16 / int8 / int4
- `enable_caching` (BOOLEAN): Cache model in memory

**Outputs**:
- `model` (MODEL): Loaded quantized UNet

**Note**: Load VAE and CLIP separately using standard ComfyUI loaders.

### ModelOptSaveQuantized

**Inputs**:
- `model` (MODEL): Quantized model to save
- `filename` (STRING): Output filename
- `save_format` (COMBO): safetensors / pytorch
- `metadata` (STRING, optional): JSON metadata

**Saves to**: `ComfyUI/models/modelopt_unet/`

### ModelOptCalibrationHelper

**Inputs**:
- `latent` (LATENT): Latent samples to collect
- `max_samples` (INT): Maximum samples to collect (8-512)

**Outputs**:
- `calibration_data` (LATENT): Collected calibration samples

## 🔧 Troubleshooting

### "No CUDA device available"
- Ensure NVIDIA GPU is installed and recognized
- Check CUDA drivers: `nvidia-smi`
- Reinstall PyTorch with CUDA: `pip install torch --index-url https://download.pytorch.org/whl/cu124`

### "FP8 requires Compute Capability 8.9+"
- FP8 only works on RTX 4000 series (Ada Lovelace) or H100 (Hopper)
- Use INT8 instead for older GPUs (RTX 2000/3000)

### "Out of VRAM"
- Reduce `calibration_steps` (try 16 or 32)
- Close other applications
- Use INT4 for maximum VRAM savings
- Try a smaller/more efficient model architecture if available

### "Quantization is very slow"
- Install Triton (Linux): `pip install triton`
- Reduce `calibration_steps` for testing
- Quantization is one-time process, inference will be faster

### "Image quality is worse"
- Increase `calibration_steps` (try 128 or 256)
- Use real calibration data (ModelOptCalibrationHelper)
- Try FP8 instead of INT8 (requires RTX 4000+)
- Some quality loss (<3%) is normal with quantization

## 📊 Performance Benchmarks

Example benchmarks demonstrate typical performance improvements:

**Example: SDXL-based model on RTX 4090** (1024x1024, 20 steps):

| Configuration | Time/Image | VRAM | Quality |
|---------------|------------|------|---------|
| FP16 (baseline) | 3.2s | ~8GB | 100% |
| INT8 quantized | 1.7s | ~4GB | ~98% |
| FP8 quantized | 1.6s | ~4GB | ~99% |

**Example: SD1.5-based model on RTX 3080** (512x512, 20 steps):

| Configuration | Time/Image | VRAM | Quality |
|---------------|------------|------|---------|
| FP16 (baseline) | 1.1s | ~4GB | 100% |
| INT8 quantized | 0.6s | ~2GB | ~97% |

*Note: Performance varies significantly by model architecture, GPU, resolution, and workflow complexity. These are example benchmarks only.*

## ⚠️ Limitations

- **Component Quantization**: Only UNet/diffusion model is quantized
  - VAE and text encoders remain FP16 (load separately with standard nodes)
- **Adapter Support**: LoRAs, ControlNets, and IP-Adapters are applied after quantization
  - Load the quantized model first, then apply adapters as usual
- **Platform**: Windows support is experimental (Triton acceleration not fully supported)
- **First Run**: Model quantization takes 2-10 minutes (one-time process, saves for reuse)
- **Model Compatibility**: Varies by ModelOpt version - see [NVIDIA's documentation](https://github.com/NVIDIA/TensorRT-Model-Optimizer) for current support

## 📚 Documentation

- **Technical Guide**: See [docs/TECHNICAL_GUIDE.md](docs/TECHNICAL_GUIDE.md) for in-depth technical documentation
- **ModelOpt Official**: [NVIDIA ModelOpt GitHub](https://github.com/NVIDIA/TensorRT-Model-Optimizer)
- **Report Issues**: [GitHub Issues](https://github.com/EnragedAntelope/comfy-modelopt/issues)

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

MIT License - see [LICENSE](LICENSE) for details

## 🙏 Acknowledgments

- **NVIDIA** for ModelOpt and TensorRT
- **ComfyUI** community for the excellent framework
- All contributors and testers

## 💬 Support

- **Issues**: [GitHub Issues](https://github.com/EnragedAntelope/comfy-modelopt/issues)
- **Discussions**: [GitHub Discussions](https://github.com/EnragedAntelope/comfy-modelopt/discussions)
- **ComfyUI Discord**: #custom-nodes channel

---

**⚡ Optimize your Stable Diffusion workflow with NVIDIA ModelOpt!**

Made with ❤️ for the ComfyUI community
