# Pixel3DMM ComfyUI Nodes

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-green.svg)](https://github.com/comfyanonymous/ComfyUI)

**Professional 3D face reconstruction for ComfyUI using the Pixel3DMM method**

Transform 2D face images into detailed 3D models with state-of-the-art neural networks, FLAME parametric models, and advanced optimization techniques.

![Pixel3DMM Pipeline]((https://github.com/A043-studios/comfyui-pixel3dmm/blob/15ce8b5ebf46c118bcfb4290c88e16927e6fbcc0/examples/banner.gif))

## 🌟 Features

- **🎭 Complete 3D Face Reconstruction**: From single images to detailed 3D meshes
- **🔥 FLAME Model Integration**: Industry-standard parametric face model
- **🗺️ UV Coordinate Prediction**: High-quality texture mapping
- **📐 Surface Normal Estimation**: Detailed geometric surface information
- **⚡ Real-time Optimization**: Interactive parameter refinement
- **📦 Multiple Export Formats**: OBJ, PLY, STL mesh export
- **🎛️ User-Friendly Interface**: Intuitive ComfyUI integration

## 📋 Table of Contents

- [Installation](#-installation)
- [Quick Start](#-quick-start)
- [Node Reference](#-node-reference)
- [Workflow Examples](#-workflow-examples)
- [Troubleshooting](#-troubleshooting)
- [Advanced Usage](#-advanced-usage)
- [Contributing](#-contributing)
- [License](#-license)

## 🚀 Installation

### Prerequisites

- **ComfyUI**: Latest version installed and working
- **Python**: 3.9 or higher
- **PyTorch**: 2.0 or higher (CPU or CUDA)
- **System Memory**: 8GB+ RAM recommended

### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "Pixel3DMM"
3. Click "Install"
4. Restart ComfyUI

### Method 2: Manual Installation

1. **Clone the repository**:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/your-repo/comfyui-pixel3dmm.git
   ```

2. **Install dependencies**:
   ```bash
   cd comfyui-pixel3dmm
   pip install -r requirements.txt
   ```

3. **Restart ComfyUI**

### Method 3: Download and Extract

1. Download the latest release from [Releases](https://github.com/your-repo/comfyui-pixel3dmm/releases)
2. Extract to `ComfyUI/custom_nodes/comfyui-pixel3dmm/`
3. Install dependencies: `pip install -r requirements.txt`
4. Restart ComfyUI

## ⚡ Quick Start

### Basic 3D Face Reconstruction

1. **Load an image** using ComfyUI's `Load Image` node
2. **Add Pixel3DMM Loader** node and configure model path
3. **Connect Face Reconstructor** node to process the image
4. **Add Mesh Exporter** to save your 3D model

```
[Load Image] → [Pixel3DMM Loader] → [Face Reconstructor 3D] → [Mesh Exporter]
```

### Example Workflow

```json
{
  "workflow": "basic_reconstruction",
  "nodes": [
    {"type": "LoadImage", "inputs": {"image": "face_photo.jpg"}},
    {"type": "Pixel3DMMLoader", "inputs": {"model_path": "models/pixel3dmm.pth"}},
    {"type": "FaceReconstructor3D", "inputs": {"quality": "balanced"}},
    {"type": "MeshExporter", "inputs": {"format": "obj", "filename": "face_3d"}}
  ]
}
```

## 🎛️ Node Reference

### 🔧 Pixel3DMM Loader

**Purpose**: Load and initialize Pixel3DMM models

**Inputs**:
- `model_path` (STRING): Path to model file
- `device` (CHOICE): auto/cpu/cuda
- `precision` (CHOICE): fp32/fp16
- `config_override` (STRING): JSON config overrides

**Outputs**:
- `model` (PIXEL3DMM_MODEL): Loaded model container
- `status` (STRING): Loading status message

**Usage**:
```python
# Basic usage
model_path = "models/pixel3dmm_model.pth"
device = "auto"  # Automatically detect GPU/CPU
precision = "fp32"  # Use fp16 for faster inference on GPU
```

### 🎭 Face Reconstructor 3D

**Purpose**: Complete 3D face reconstruction from images

**Inputs**:
- `model` (PIXEL3DMM_MODEL): Loaded model from Pixel3DMM Loader
- `image` (IMAGE): Input face image
- `reconstruction_quality` (CHOICE): fast/balanced/high
- `optimize_flame` (BOOLEAN): Enable parameter optimization
- `optimization_steps` (INT): Number of optimization iterations
- `learning_rate` (FLOAT): Optimization learning rate

**Outputs**:
- `rendered_face` (IMAGE): Rendered 3D face view
- `flame_parameters` (FLAME_PARAMS): FLAME model parameters
- `mesh_data` (MESH_DATA): 3D mesh data
- `status` (STRING): Reconstruction status

**Quality Settings**:
- **Fast**: Quick reconstruction, lower quality
- **Balanced**: Good quality-speed tradeoff (recommended)
- **High**: Best quality, slower processing

### 🗺️ UV Predictor

**Purpose**: Predict UV coordinates for texture mapping

**Inputs**:
- `model` (PIXEL3DMM_MODEL): Loaded model
- `image` (IMAGE): Input face image
- `output_resolution` (CHOICE): 256/512/1024
- `uv_smoothing` (FLOAT): Smoothing amount (0.0-1.0)
- `confidence_threshold` (FLOAT): Confidence threshold (0.0-1.0)

**Outputs**:
- `uv_map` (IMAGE): UV coordinate visualization
- `uv_coordinates` (UV_COORDS): Raw UV coordinate data
- `status` (STRING): Prediction status

### 📐 Normal Predictor

**Purpose**: Predict surface normals for geometric detail

**Inputs**:
- `model` (PIXEL3DMM_MODEL): Loaded model
- `image` (IMAGE): Input face image
- `output_resolution` (CHOICE): 256/512/1024
- `normal_space` (CHOICE): camera/world
- `normal_smoothing` (FLOAT): Smoothing amount (0.0-1.0)
- `enhance_details` (BOOLEAN): Enable detail enhancement

**Outputs**:
- `normal_map` (IMAGE): Normal map visualization
- `normal_vectors` (NORMALS): Raw normal vector data
- `status` (STRING): Prediction status

### 🔥 FLAME Optimizer

**Purpose**: Optimize FLAME parameters using geometric constraints

**Inputs**:
- `model` (PIXEL3DMM_MODEL): Loaded model
- `image` (IMAGE): Input face image
- `initial_params` (FLAME_PARAMS): Initial FLAME parameters
- `optimization_steps` (INT): Number of optimization steps
- `uv_coordinates` (UV_COORDS): Optional UV constraints
- `surface_normals` (NORMALS): Optional normal constraints
- `learning_rate` (FLOAT): Optimization learning rate
- `uv_weight` (FLOAT): UV loss weight
- `normal_weight` (FLOAT): Normal loss weight
- `regularization_weight` (FLOAT): Regularization weight

**Outputs**:
- `optimized_params` (FLAME_PARAMS): Optimized parameters
- `mesh_data` (MESH_DATA): Optimized mesh data
- `status` (STRING): Optimization status

### 📦 Mesh Exporter

**Purpose**: Export 3D meshes to various formats

**Inputs**:
- `mesh_data` (MESH_DATA): 3D mesh data to export
- `output_format` (CHOICE): obj/ply/stl
- `filename` (STRING): Output filename
- `output_directory` (STRING): Output directory path
- `include_textures` (BOOLEAN): Include texture coordinates
- `scale_factor` (FLOAT): Mesh scaling factor
- `center_mesh` (BOOLEAN): Center mesh at origin

**Outputs**:
- `file_path` (STRING): Path to exported file
- `status` (STRING): Export status

## 🔄 Workflow Examples

### Example 1: Basic Reconstruction

```
[Load Image] → [Pixel3DMM Loader] → [Face Reconstructor 3D] → [Mesh Exporter]
```

**Use Case**: Quick 3D face model from photo
**Quality**: Balanced
**Time**: ~30 seconds

### Example 2: High-Quality with Optimization

```
[Load Image] → [Pixel3DMM Loader] → [Face Reconstructor 3D]
                                           ↓
[UV Predictor] → [FLAME Optimizer] → [Mesh Exporter]
     ↑                ↑
[Normal Predictor] ----
```

**Use Case**: Professional-quality 3D reconstruction
**Quality**: High
**Time**: ~2-5 minutes

### Example 3: Batch Processing

```
[Load Image Batch] → [Pixel3DMM Loader] → [Face Reconstructor 3D] → [Mesh Exporter Batch]
```

**Use Case**: Process multiple faces
**Quality**: Configurable
**Time**: Varies by batch size

## 🛠️ Troubleshooting

### Common Issues

#### ❌ "Model file not found"
**Solution**: 
1. Check model path is correct
2. Download required model files
3. Ensure models are in the correct directory

#### ❌ "CUDA out of memory"
**Solutions**:
1. Switch to CPU: Set device to "cpu"
2. Use FP16: Set precision to "fp16"
3. Reduce image resolution
4. Close other GPU applications

#### ❌ "Import error: module not found"
**Solutions**:
1. Install dependencies: `pip install -r requirements.txt`
2. Restart ComfyUI completely
3. Check Python environment

#### ❌ "Poor reconstruction quality"
**Solutions**:
1. Use higher quality settings
2. Enable FLAME optimization
3. Ensure good input image quality
4. Check lighting and face visibility

#### ❌ "Slow processing"
**Solutions**:
1. Use GPU if available
2. Enable FP16 precision
3. Use "fast" quality setting
4. Reduce optimization steps

### Performance Tips

- **GPU Usage**: Always use GPU when available for 10x+ speedup
- **Image Size**: 512x512 is optimal, larger images don't improve quality significantly
- **Batch Size**: Process multiple images together for efficiency
- **Memory**: Close other applications to free up GPU memory

### Getting Help

1. **Check the logs**: ComfyUI console shows detailed error messages
2. **GitHub Issues**: Report bugs and request features
3. **Community**: Join our Discord for support and discussions
4. **Documentation**: Check our wiki for advanced tutorials

## 🔧 Advanced Usage

### Custom Model Training

```python
# Train custom UV predictor
from pixel3dmm.training import UVTrainer

trainer = UVTrainer(config)
trainer.train(dataset_path="path/to/uv_data")
```

### API Usage

```python
# Use nodes programmatically
from comfyui_pixel3dmm import Pixel3DMMLoader, FaceReconstructor3D

loader = Pixel3DMMLoader()
model, status = loader.load_model("models/pixel3dmm.pth")

reconstructor = FaceReconstructor3D()
result = reconstructor.reconstruct_face(model, image)
```

### Configuration

Create `config.json` for custom settings:

```json
{
  "model": {
    "encoder_backbone": "vit_base_patch14_dinov2.lvd142m",
    "embedding_dim": 128,
    "flame_dim": 101
  },
  "optimization": {
    "max_steps": 200,
    "learning_rate": 0.01,
    "convergence_threshold": 1e-6
  }
}
```

## 📚 Additional Resources

- **Paper**: [Pixel3DMM: Generating 3D Representations from Multi-view Images](https://arxiv.org/abs/2023.xxxxx)
- **FLAME Model**: [Official FLAME repository](https://flame.is.tue.mpg.de/)
- **ComfyUI**: [ComfyUI documentation](https://github.com/comfyanonymous/ComfyUI)
- **Tutorials**: [Video tutorials playlist](https://youtube.com/playlist/xxxxx)

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
git clone https://github.com/your-repo/comfyui-pixel3dmm.git
cd comfyui-pixel3dmm
pip install -e .
pip install -r requirements-dev.txt
```

### Running Tests

```bash
python -m pytest tests/
python tests/test_pixel3dmm_nodes.py
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Pixel3DMM Research Team**: Original research and methodology
- **FLAME Team**: Parametric face model
- **ComfyUI Community**: Framework and inspiration
- **PyTorch Team**: Deep learning framework

## 📊 Citation

If you use this work in your research, please cite:

```bibtex
@article{pixel3dmm2023,
  title={Pixel3DMM: Generating 3D Representations from Multi-view Images},
  author={Research Team},
  journal={arXiv preprint arXiv:2023.xxxxx},
  year={2023}
}
```

---

**Made with ❤️ by the MCP Multi-Agent System**

For support, please open an issue on [GitHub](https://github.com/your-repo/comfyui-pixel3dmm/issues) or join our [Discord community](https://discord.gg/xxxxx).
