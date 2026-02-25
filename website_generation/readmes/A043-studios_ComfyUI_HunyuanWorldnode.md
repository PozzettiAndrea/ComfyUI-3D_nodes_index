# ComfyUI HunyuanWorld - Complete 3D Generation Suite

[![CI](https://github.com/A043-studios/ComfyUI_HunyuanWorldnode/workflows/CI/badge.svg)](https://github.com/A043-studios/ComfyUI_HunyuanWorldnode/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-green.svg)](https://github.com/comfyanonymous/ComfyUI)

A comprehensive ComfyUI custom node package that provides multiple approaches to 3D generation using Hunyuan3D models. This package offers both simplified interfaces and advanced workflows for creating 3D models from images.

## 🌟 Features

### Four Different Approaches:

1. **🔥 Real Hunyuan3D Pipeline Implementation** - Direct integration with official Hunyuan3D library
2. **🎯 Simplified Wrapper** - Easy-to-use interface wrapping existing ComfyUI nodes
3. **⚙️ Native ComfyUI Workflow** - Using built-in ComfyUI Hunyuan3D nodes directly
4. **🔀 Hybrid Approach** - Combines custom functionality with existing infrastructure

## 📦 Installation

### 🚀 Quick Install from GitHub (Recommended)

#### Method 1: ComfyUI Manager (Easiest)
1. Open ComfyUI Manager
2. Search for "HunyuanWorld"
3. Click Install
4. Restart ComfyUI

#### Method 2: Git Clone
```bash
# Navigate to ComfyUI custom_nodes directory
cd ComfyUI/custom_nodes

# Clone the repository
git clone https://github.com/A043-studios/ComfyUI_HunyuanWorldnode.git

# Navigate to the cloned directory
cd ComfyUI_HunyuanWorldnode

# Run the installation script
python install.py

# Or install manually
pip install -r requirements.txt
```

#### Method 3: Direct Download
1. Download the [latest release](https://github.com/A043-studios/ComfyUI_HunyuanWorldnode/releases)
2. Extract to `ComfyUI/custom_nodes/ComfyUI_HunyuanWorldnode`
3. Run `python install.py` or `pip install -r requirements.txt`
4. Restart ComfyUI

### 🔧 Manual Installation

#### Core Dependencies
```bash
pip install torch>=2.0.0 transformers>=4.30.0 diffusers>=0.21.0
pip install trimesh>=3.15.0 numpy>=1.21.0 Pillow>=9.0.0
```

#### Optional Dependencies
```bash
# For enhanced functionality
pip install accelerate>=0.20.0 opencv-python>=4.5.0
pip install fastapi>=0.68.0 uvicorn>=0.15.0 gradio>=3.0.0
```

#### Hunyuan3D from Source (Latest Features)
```bash
git clone https://github.com/tencent/hunyuan3d-2.git
cd hunyuan3d-2
pip install -e .
```

### 🐳 Docker Installation (Coming Soon)
```bash
# Pull the Docker image
docker pull a043studios/comfyui-hunyuanworld:latest

# Run with GPU support
docker run --gpus all -p 8188:8188 a043studios/comfyui-hunyuanworld:latest
```

## 🚀 Quick Start

### Method 1: Using Real Hunyuan3D Pipeline (Recommended)

```python
# 1. Load the model
model_loader = HunyuanWorldModelLoader()
pipeline = model_loader.load_model(
    model_name="tencent/Hunyuan3D-2mini",  # Faster, less VRAM
    precision="fp16",
    enable_texture=True,
    low_vram_mode=True
)

# 2. Generate 3D from image
generator = HunyuanWorldImageTo3D()
mesh_path, info, preview = generator.generate_3d(
    pipeline=pipeline,
    image=your_image,
    apply_texture=True,
    save_mesh=True,
    filename_prefix="my_3d_model"
)
```

### Method 2: Simplified Wrapper

```python
# One-click 3D generation
simple_wrapper = HunyuanWorldSimplifiedWrapper()
result_info, preview = simple_wrapper.simple_generate(
    image=your_image,
    model_variant="mini",  # or "standard", "multiview"
    resolution=1024,
    enable_texture=True,
    filename_prefix="simple_3d"
)
```

## 📋 Node Reference

### 🔥 Real Implementation Nodes

#### HunyuanWorldModelLoader
**Purpose**: Load Hunyuan3D models with proper memory management

**Inputs**:
- `model_name`: Choose from "tencent/Hunyuan3D-2", "tencent/Hunyuan3D-2mini", "tencent/Hunyuan3D-2mv"
- `precision`: "fp16" (recommended) or "fp32"
- `enable_texture`: Enable texture synthesis pipeline
- `low_vram_mode`: Optimize for low VRAM systems

**Outputs**:
- `pipeline`: Loaded Hunyuan3D pipeline ready for generation

#### HunyuanWorldImageTo3D
**Purpose**: Generate 3D meshes from input images

**Inputs**:
- `pipeline`: Output from HunyuanWorldModelLoader
- `image`: Input image (ComfyUI IMAGE format)
- `apply_texture`: Whether to apply texture to the mesh
- `save_mesh`: Save mesh as GLB file
- `filename_prefix`: Prefix for saved files
- `seed` (optional): Random seed for reproducible results

**Outputs**:
- `mesh_path`: Path to saved GLB file
- `info`: Generation information
- `preview_image`: Rendered preview of the 3D mesh

### 🎯 Simplified Nodes

#### HunyuanWorldSimplifiedWrapper
**Purpose**: One-click 3D generation for beginners

**Inputs**:
- `image`: Input image
- `model_variant`: "standard", "mini", or "multiview"
- `resolution`: Output resolution (512-2048)
- `enable_texture`: Apply texture
- `filename_prefix`: File naming prefix

**Outputs**:
- `result_info`: Generation status and information
- `preview`: Preview image of the result

### 🔀 Hybrid Nodes

#### HunyuanWorldHybridNode
**Purpose**: Flexible generation with multiple backend options

**Inputs**:
- `mode`: "direct_pipeline" or "comfyui_workflow"
- `image`: Input image
- `model_name`: Hunyuan3D model to use
- `use_texture`: Enable texture synthesis
- `filename_prefix`: File naming
- `existing_latent` (optional): Use existing latent from ComfyUI workflow
- `existing_conditioning` (optional): Use existing conditioning

**Outputs**:
- `mesh_path`: Path to generated mesh
- `preview`: Preview image
- `method_info`: Information about the method used

## 🔧 Using Native ComfyUI Hunyuan3D Nodes

ComfyUI already includes powerful Hunyuan3D nodes. Here's how to use them:

### Basic Workflow:

1. **EmptyLatentHunyuan3Dv2** - Create latent space
   ```
   resolution: 3072 (or 1536 for faster generation)
   batch_size: 1
   ```

2. **CLIPVisionLoader** + **CLIPVisionEncode** - Process input image
   ```
   Load CLIP vision model → Encode your image
   ```

3. **Hunyuan3Dv2Conditioning** - Create conditioning
   ```
   Connect CLIP vision output → Get positive/negative conditioning
   ```

4. **Load Hunyuan3D Model** + **KSampler** - Generate
   ```
   Load model → Sample with conditioning → Get latent output
   ```

5. **VAEDecodeHunyuan3D** - Decode to voxels
   ```
   latent → voxels (with octree_resolution: 256)
   ```

6. **VoxelToMesh** - Convert to mesh
   ```
   voxels → mesh (with threshold: 0.5)
   ```

7. **SaveGLB** - Save final result
   ```
   mesh → GLB file
   ```

### Advanced Multi-View Workflow:

Use **Hunyuan3Dv2ConditioningMultiView** for better results:
```
front_image → CLIP encode → front conditioning
left_image → CLIP encode → left conditioning
back_image → CLIP encode → back conditioning
right_image → CLIP encode → right conditioning
→ Combine in MultiView node → Enhanced conditioning
```

## 🎛️ Model Variants

### tencent/Hunyuan3D-2
- **Best quality** but requires more VRAM
- Recommended for: High-quality final outputs
- VRAM requirement: ~8GB+

### tencent/Hunyuan3D-2mini
- **Balanced** quality and speed
- Recommended for: Most users, development, testing
- VRAM requirement: ~4GB+

### tencent/Hunyuan3D-2mv
- **Multi-view** optimized
- Recommended for: When you have multiple view images
- VRAM requirement: ~6GB+

## 💡 Tips and Best Practices

### For Best Results:
1. **Use high-quality input images** (512x512 or higher)
2. **Clear subject isolation** - objects with clean backgrounds work better
3. **Good lighting** - avoid harsh shadows or overexposure
4. **Single objects** - works better than complex scenes

### Performance Optimization:
1. **Use fp16 precision** for 2x speed improvement
2. **Enable low_vram_mode** if you have limited GPU memory
3. **Start with mini model** for testing, upgrade to full model for final output
4. **Use smaller resolutions** (1536 instead of 3072) for faster iteration

### Troubleshooting:
- **Out of memory**: Enable low_vram_mode, use fp16, or use mini model
- **Poor quality**: Try full model, higher resolution, or better input image
- **Import errors**: Install requirements with `pip install -r requirements.txt`

## 🔄 Workflow Examples

### Example 1: Quick 3D Generation
```
LoadImage → HunyuanWorldModelLoader → HunyuanWorldImageTo3D → Preview3D
```

### Example 2: Advanced Pipeline
```
LoadImage → CLIPVisionEncode → Hunyuan3Dv2Conditioning →
EmptyLatentHunyuan3Dv2 → KSampler → VAEDecodeHunyuan3D →
VoxelToMesh → SaveGLB
```

### Example 3: Hybrid Approach
```
LoadImage → HunyuanWorldHybridNode (mode: direct_pipeline) → Preview
```

## 🆚 Comparison: Custom vs Built-in Nodes

| Feature | Custom Nodes | Built-in ComfyUI Nodes |
|---------|--------------|-------------------------|
| **Ease of use** | ⭐⭐⭐⭐⭐ Simple | ⭐⭐⭐ Complex workflow |
| **Flexibility** | ⭐⭐⭐ Good | ⭐⭐⭐⭐⭐ Maximum |
| **Performance** | ⭐⭐⭐⭐ Direct | ⭐⭐⭐⭐⭐ Optimized |
| **Memory usage** | ⭐⭐⭐ Standard | ⭐⭐⭐⭐⭐ Efficient |
| **Customization** | ⭐⭐⭐ Limited | ⭐⭐⭐⭐⭐ Full control |

**Recommendation**:
- **Beginners**: Use custom simplified wrapper
- **Advanced users**: Use built-in ComfyUI workflow
- **Developers**: Use hybrid approach for maximum flexibility

## 🐛 Troubleshooting

### Common Issues:

1. **"Hunyuan3D libraries not available"**
   ```bash
   pip install -r requirements.txt
   ```

2. **CUDA out of memory**
   ```python
   # Use these settings:
   low_vram_mode=True
   precision="fp16"
   model_name="tencent/Hunyuan3D-2mini"
   ```

3. **Slow generation**
   ```python
   # Optimize with:
   resolution=1536  # instead of 3072
   model_variant="mini"
   ```

4. **Poor mesh quality**
   ```python
   # Try:
   model_name="tencent/Hunyuan3D-2"  # full model
   resolution=3072
   apply_texture=True
   ```

## 📚 Additional Resources

- [Hunyuan3D Official Repository](https://github.com/tencent/hunyuan3d-2)
- [ComfyUI Documentation](https://docs.comfy.org/)
- [3D Model Formats Guide](https://en.wikipedia.org/wiki/GLB)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## 📄 License

This project follows the same license as the original Hunyuan3D project. Please refer to the official repository for license details.

---

**Made with ❤️ for the ComfyUI community**