# ComfyUI Diffusers Model Loader

A powerful and extensible custom node for ComfyUI that enables seamless loading of Diffusers-based image generation models. Currently optimized for Qwen (千问) models with plans to support additional model architectures.
[中文介绍](#中文介绍)
## 🌟 Features
WARNNING!!!Extremely consumes VRAM, requiring approximately 40g of VRAM to run the project❗❗❗
Alternatively, you can set the FP8 quantization loading for the model
### Core Capabilities
- **🚀 Full Pipeline Support**: Loads complete Diffusers pipelines including transformer/UNet, text encoder, and VAE components
- **🔧 Flexible Model Architecture**: Supports both Transformer-based (Qwen) and UNet-based diffusion models
- **💾 Advanced Memory Management**: Multiple precision options (FP32, FP16, BF16, FP8) with intelligent device allocation
- **📦 Sharded Model Support**: Handles large models split across multiple files (`.safetensors.index.json`)
- **🎯 Optimized VAE Decoding**: Custom tiled decoding implementation for memory-efficient image generation

### How To Use
##Double click the canva to search'加载千问diffusers模型'node to use,then use the workflow of comfyui ORG


## 📦 Installation

### Method 1: Direct Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-repo/qwen_diffusers_loader.git
```

### Method 2: Manual Installation
1. Download or clone this repository
2. Copy the entire `qwen_diffusers_loader` folder to `ComfyUI/custom_nodes/`
3. Restart ComfyUI
4. Find the node under `loaders` → `Load Diffusers Model (Qwen)`

## 🏗️ Model Structure & Preparation

### Supported Model Directory Structure
```
models/diffusers/your-model-name/
├── model_index.json                    # Pipeline configuration
├── transformer/                        # Diffusion model (Qwen) or unet/ (others)
│   ├── config.json
│   ├── diffusion_pytorch_model.safetensors.index.json
│   ├── diffusion_pytorch_model-00001-of-00009.safetensors
│   └── ...
├── text_encoder/                       # CLIP/T5 text encoder
│   ├── config.json
│   ├── model.safetensors.index.json
│   ├── model-00001-of-00004.safetensors
│   └── ...
├── vae/                                # Variational Autoencoder
│   ├── config.json
│   └── diffusion_pytorch_model.safetensors
├── tokenizer/                          # Text tokenizer
│   ├── tokenizer.json
│   └── tokenizer_config.json
└── scheduler/                          # Noise scheduler
    └── scheduler_config.json
```

### Model Preparation Steps
1. Download your Diffusers model to `ComfyUI/models/diffusers/`
2. Ensure the model follows the standard Diffusers structure
3. Verify `model_index.json` exists and contains valid component mappings

## 🎮 Usage Guide

### Basic Workflow
```
Load Diffusers Model → KSampler → VAE Decode → Save Image
        ↓
CLIP Text Encode (Prompt)
```

### Node Parameters

#### Advanced Options
- **Memory Optimization**: Automatic component unloading when not in use
- **Tiled VAE**: Built-in support for tiled decoding to handle large images
- **Error Recovery**: Automatic fallback to CPU if GPU memory insufficient


### Component Loading System
```python
# Simplified component loading flow
1. Parse model_index.json → identify components
2. Load each component with specified precision
3. Apply memory optimizations
4. Integrate with ComfyUI model management
```


### Upcoming Features
- **🔄 Hot Model Swapping**: Switch models without reloading ComfyUI
- **⚡ Optimized Memory Management**: Advanced VRAM optimization
- **🎨 LoRA Support**: Fine-tuned model loading
- **🔧 Custom Scheduler Support**: Additional noise schedulers
- **📊 Performance Metrics**: Built-in benchmarking tools

## 🐛 Troubleshooting

### Common Issues

#### Model Loading Failures
```bash
# Check model integrity
python -c "import json; print(json.load(open('models/diffusers/your-model/model_index.json')))"

# Verify file permissions
ls -la models/diffusers/your-model/
```



## 🤝 Contributing

### Development Setup
```bash
git clone https://github.com/your-repo/qwen_diffusers_loader.git
cd qwen_diffusers_loader
# Make your changes
# Test with ComfyUI
# Submit pull request
```

### Adding New Model Support
1. Extend the `load_diffusers_model` function
2. Add model-specific component handling
3. Update the README with new model instructions
4. Add test cases

### Code Style
- Follow PEP 8 guidelines
- Add docstrings for new functions
- Include error handling for new features
- Test with multiple model types

## 🙏 Acknowledgments

- ComfyUI team for the excellent framework
- Hugging Face for the Diffusers library
- Qwen team for the innovative model architecture
- Community contributors and testers

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-repo/qwen_diffusers_loader/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-repo/qwen_diffusers_loader/discussions)
- **Documentation**: [Wiki](https://github.com/your-repo/qwen_diffusers_loader/wiki)

---

**Version**: 1.0.0 | **ComfyUI Compatibility**: Latest | **Python**: 3.8+ | **PyTorch**: 1.13+

---

# 中文介绍

警告！！！消耗VRAM，需要大约40g的VRAM来运行项目
你也可以尝试使用fp8量化来加载模型
## 🌟 ComfyUI Diffusers 模型加载器

这是一个为ComfyUI设计的强大且可扩展的自定义节点，能够无缝加载基于Diffusers的图像生成模型。目前已针对千问(Qwen)模型进行优化，并计划支持更多模型架构。

### 🚀 核心功能

#### 主要特性
- **🔥 完整流水线支持**：加载完整的Diffusers流水线，包括transformer/UNet、文本编码器和VAE组件
- **⚙️ 灵活的模型架构**：支持基于Transformer的(千问)和基于UNet的扩散模型
- **💾 高级内存管理**：多种精度选项(FP32、FP16、BF16、FP8)与智能设备分配
- **📦 分片模型支持**：处理拆分为多个文件的大型模型(`.safetensors.index.json`)
- **🎯 优化的VAE解码**：自定义分块解码实现，实现内存高效的图像生成
- **🌐 多语言界面**：原生中文和英文支持

#### 使用方法
##双击画布搜索'加载千问diffusers模型'节点，使用官方工作流

### 📦 安装方法

#### 方法一：Git安装（推荐）
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-repo/qwen_diffusers_loader.git
```

#### 方法二：手动安装
1. 下载或克隆此仓库
2. 将整个`qwen_diffusers_loader`文件夹复制到`ComfyUI/custom_nodes/`
3. 重启ComfyUI
4. 在节点菜单的`loaders` → `Load Diffusers Model (Qwen)`中找到节点

### 🏗️ 模型结构与准备

#### 支持的模型目录结构
```
models/diffusers/你的模型名称/
├── model_index.json                    # 流水线配置文件
├── transformer/                        # 扩散模型(千问)或unet/(其他模型)
│   ├── config.json
│   ├── diffusion_pytorch_model.safetensors.index.json
│   ├── diffusion_pytorch_model-00001-of-00009.safetensors
│   └── ...
├── text_encoder/                       # CLIP/T5文本编码器
│   ├── config.json
│   ├── model.safetensors.index.json
│   ├── model-00001-of-00004.safetensors
│   └── ...
├── vae/                                # 变分自编码器
│   ├── config.json
│   └── diffusion_pytorch_model.safetensors
├── tokenizer/                          # 文本分词器
│   ├── tokenizer.json
│   └── tokenizer_config.json
└── scheduler/                          # 噪声调度器
    └── scheduler_config.json
```

#### 模型准备步骤
1. 将你的Diffusers模型下载到`ComfyUI/models/diffusers/`
2. 确保模型遵循标准的Diffusers结构
3. 验证`model_index.json`存在且包含有效的组件映射

### 🎮 使用指南

#### 基本工作流
```
加载Diffusers模型 → KSampler → VAE解码 → 保存图像
        ↓
CLIP文本编码(提示词)
```

#### 节点参数

##### 模型配置
- **`model_path`**：从下拉菜单选择模型(自动扫描`models/diffusers/`)
- **`weight_dtype`**：选择精度以平衡内存和质量
  - `default`：原始模型精度
  - `fp16`：半精度(推荐8-12GB显存)
  - `bf16`：BFloat16(更好兼容性，12GB+显存)
  - `fp8_e4m3fn`：8位精度(4-8GB显存)
  - `fp8_e4m3fn_fast`：快速8位模式
  - `fp8_e5m2`：替代8位格式
- **`device`**：强制指定设备(留空自动选择)

##### 高级选项
- **内存优化**：不使用时自动卸载组件
- **分块VAE**：内置分块解码支持，处理大图像
- **错误恢复**：GPU内存不足时自动回退到CPU

### 📊 性能建议

| 显存容量 | 推荐设置 | 预期性能 |
|---------|---------|---------|
| 4-6GB | `fp8_e4m3fn_fast` | 良好质量，较慢 |
| 8-12GB | `fp16` | 平衡质量/速度 |
| 16GB+ | `bf16`或`default` | 最佳质量 |
| 仅CPU | `default` + `cpu`设备 | 功能正常但慢 |

### 🔧 技术架构

#### 组件加载系统
```python
# 简化的组件加载流程
1. 解析model_index.json → 识别组件
2. 使用指定精度加载各组件
3. 应用内存优化
4. 与ComfyUI模型管理集成
```

#### VAE解码实现
- **标准解码**：直接张量处理
- **分块解码**：大图像的内存高效处理
  - 1D分块：用于基于序列的处理
  - 2D分块：用于标准图像解码
  - 3D分块：用于视频或批处理
- **DecoderOutput处理**：自动提取样本张量


### 🐛 故障排除


##### 内存问题
- **CUDA内存不足**：降低`weight_dtype`精度或启用CPU模式
- **加载缓慢**：检查磁盘I/O和可用RAM
- **组件错误**：验证所有模型文件已完全下载

##### 性能问题
- **生成缓慢**：检查模型是否在CPU而非GPU上运行
- **显存使用过高**：使用更低精度或启用分块解码
- **兼容性问题**：确保ComfyUI和PyTorch版本是最新的
- **OOM**:采用分块解码以节省显存


#### 添加新模型支持
1. 扩展`load_diffusers_model`函数
2. 添加模型特定的组件处理
3. 更新README中的新模型说明
4. 添加测试用例


### 🙏 致谢

- ComfyUI团队提供的优秀框架
- Hugging Face的Diffusers库
- 千问团队的创新模型架构
- 社区贡献者和测试者

### 📞 支持

- **问题反馈**：[GitHub Issues](https://github.com/your-repo/qwen_diffusers_loader/issues)
- **讨论交流**：[GitHub Discussions](https://github.com/your-repo/qwen_diffusers_loader/discussions)
- **文档说明**：[Wiki](https://github.com/your-repo/qwen_diffusers_loader/wiki)

---

**版本**: 1.0.0 | **ComfyUI兼容性**: 最新版本 | **Python**: 3.8+ | **PyTorch**: 1.13+
