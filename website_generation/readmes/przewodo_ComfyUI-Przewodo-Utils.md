# ComfyUI-Przewodo-Utils

[![GitHub stars](https://img.shields.io/github/stars/przewodo/ComfyUI-Przewodo-Utils)](https://github.com/przewodo/ComfyUI-Przewodo-Utils/stargazers)
[![GitHub license](https://img.shields.io/github/license/przewodo/ComfyUI-Przewodo-Utils)](https://github.com/przewodo/ComfyUI-Przewodo-Utils/blob/main/LICENSE)
[![ComfyUI Registry](https://img.shields.io/badge/ComfyUI-Registry-blue)](https://registry.comfy.org)

A comprehensive collection of utility nodes for ComfyUI designed to simplify complex workflow development without requiring numerous nodes for basic operations. This node pack focuses on providing essential utilities and advanced video generation capabilities, particularly for Wan2.1 models.

## 📋 Table of Contents

- [Installation](#installation)
- [Node Categories](#node-categories)
  - [PrzewodoUtils/Wan - Advanced Video Generation](#przewodoutilswan---advanced-video-generation)
  - [PrzewodoUtils - General Utilities](#przewodoutils---general-utilities)
- [Node Reference](#node-reference)
- [Features](#features)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Installation

### Method 1: ComfyUI Manager (Recommended)
1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
2. Search for "ComfyUI-Przewodo-Utils" in the manager
3. Install directly from the interface

### Method 2: Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/przewodo/ComfyUI-Przewodo-Utils.git
```

### Method 3: ComfyUI Registry
Available on the [ComfyUI Registry](https://registry.comfy.org) for easy installation.

## 📂 Node Categories

### PrzewodoUtils/Wan - Advanced Video Generation

The **PrzewodoUtils/Wan** category contains specialized nodes for advanced video generation, particularly optimized for Wan2.1 models with cutting-edge features and optimizations.

#### 🎬 Core Video Generation

**WanImageToVideoAdvancedSampler**
- **Purpose**: Advanced image-to-video generation with comprehensive quality preservation
- **Key Features**:
  - **Multi-Chunk Generation**: Generate videos longer than model limits by sequencing multiple chunks
  - **Quality Preservation**: Advanced temporal coherence and latent space continuity between chunks
  - **Dual Sampler Support**: High CFG + Low CFG sampling for superior quality
  - **TeaCache Integration**: Accelerated inference with intelligent caching
  - **SageAttention**: Optimized attention computation for memory efficiency
  - **Skip Layer Guidance**: Enhanced generation quality through selective layer processing
  - **TAESD Preview**: Fast latent space previews during generation
  - **Model Support**: GGUF and Diffusion models with multiple weight types
- **Quality Preservation Features**:
  - Temporal overlap frames for smooth transitions
  - Latent space blending between chunks
  - Artifact reduction with gaussian blur
  - Color matching for consistency
  - Multi-frame averaging for continuity
- **Advanced Options**:
  - CausVid LoRA integration
  - Block swap optimization
  - Model shift for stability
  - CFG Zero Star optimization

#### 🔧 Video Processing & Enhancement

**WanVideoEnhanceAVideo**
- **Purpose**: Video enhancement and post-processing
- **Features**: Temporal consistency, quality improvement, artifact reduction

**WanVideoVaeDecode**
- **Purpose**: Specialized VAE decoding for video latents
- **Features**: Optimized for video sequences, memory efficient processing

**WanFirstLastFirstFrameToVideo**
- **Purpose**: Convert start/end frames to video sequences
- **Features**: Intelligent frame interpolation, smooth transitions

#### 🎯 Specialized Selectors & Utilities

**WanModelTypeSelector**
- **Purpose**: Smart model type selection (GGUF vs Diffusion)
- **Features**: Automatic optimization based on model type

**WanVideoGenerationModeSelector**
- **Purpose**: Choose between different video generation modes
- **Options**: Start image, end image, start+end, start+end+start modes

**WanGetMaxImageResolutionByAspectRatio**
- **Purpose**: Calculate optimal resolutions for Wan models
- **Features**: Aspect ratio preservation, model-specific sizing

#### 📊 Advanced Workflow Tools

**WanVideoLoraStack**
- **Purpose**: Manage multiple LoRAs for video generation
- **Features**: Stack management, strength control, selective application

**WanPromptChunkStacker**
- **Purpose**: Advanced prompt management for multi-chunk generation
- **Features**: Chunk-specific prompts, automatic prompt cycling, LoRA integration per chunk

### PrzewodoUtils - General Utilities

The **PrzewodoUtils** category provides essential utility nodes for streamlined workflow development.

#### 🔢 Logic & Comparison

**CompareNumbersToCombo**
- **Purpose**: Compare two numbers and return different strings based on result
- **Comparisons**: ==, !=, <, >, <=, >=
- **Use Cases**: Conditional logic, dynamic prompt selection

**SwapAnyCondition**
- **Purpose**: Conditionally swap any two values
- **Features**: Universal type support, boolean-based switching

**SwapAnyComparison** 
- **Purpose**: Swap values based on comparison results
- **Features**: Numeric comparison with value swapping

**SwapImageComparison**
- **Purpose**: Specialized image swapping based on conditions
- **Features**: Image-specific comparison and swapping

#### 🖼️ Image Processing

**ImageScaleFactor**
- **Purpose**: Calculate scale factors for image resizing
- **Features**: Maintain aspect ratios, precise scaling calculations

**ImageSizer**
- **Purpose**: Advanced image sizing with multiple modes creating empty latent for each type of model
- **Features**: Controls  the aspect ratio of the empty latent to be generated.

**BatchImagesFromPath**
- **Purpose**: Load multiple images from filesystem paths
- **Features**: Pattern matching, recursive directory scanning, batch processing

#### 🔧 Data Management

**AppendToAnyList**
- **Purpose**: Dynamically append items or merge arrays to lists
- **Features**: 
  - Single item appending
  - Array merging
  - List extension
  - Type-agnostic operation

**DebugLatentShapes**
- **Purpose**: Debug and display latent tensor dimensions
- **Features**: Shape analysis, memory usage reporting

#### 🎛️ Control Flow

**IsInputDisabled**
- **Purpose**: Check if workflow inputs are disabled
- **Features**: Conditional execution, input validation

**FloatIfElse**
- **Purpose**: Conditional float value selection
- **Features**: Boolean-based float switching

**HasInputValue**
- **Purpose**: Verify if inputs contain valid values
- **Features**: None checking, input validation

## ✨ Features

### 🎥 Advanced Video Generation
- **Multi-Chunk Support**: Generate videos longer than model limits
- **Quality Preservation**: Maintain consistency across video chunks
- **Temporal Coherence**: Smooth transitions between sequences
- **Model Optimization**: Support for both GGUF and Diffusion models

### ⚡ Performance Optimizations
- **TeaCache**: Intelligent caching for faster inference
- **SageAttention**: Memory-efficient attention computation
- **Block Swap**: Dynamic memory management
- **TAESD Preview**: Fast latent previews

### 🔄 Workflow Efficiency
- **Universal Type Support**: `any_type` compatibility
- **Smart Selectors**: Intelligent model and mode selection
- **Batch Processing**: Efficient multi-item operations
- **Debug Tools**: Built-in debugging and analysis

### 🎯 User-Friendly Design
- **Advanced Tooltips**: Comprehensive parameter descriptions
- **Organized Categories**: Logical node grouping
- **Error Handling**: Robust error reporting and recovery
- **Flexible Configuration**: Extensive customization options

## 📋 Requirements

### Essential Dependencies
- **ComfyUI**: Latest version recommended
- **PyTorch**: GPU support recommended
- **Python**: 3.8+ required

### Required Enhancements
- **TeaCache**: `teacache>=1.7.0` for accelerated inference
- **ComfyUI-KJNodes**: `comfyui-kjnodes>=1.0.0` for enhanced functionality
- **ComfyUI-GGUF**: `comfyui-gguf>=1.0.0` for GGUF model support

## 🎯 Use Cases

### Video Generation Workflows
- **Long-form Video Creation**: Multi-chunk generation for extended sequences
- **Image-to-Video Conversion**: Transform static images into dynamic videos
- **Quality-Focused Generation**: Maintain consistency across long sequences

### Utility Workflows
- **Conditional Logic**: Dynamic workflow behavior based on comparisons
- **Batch Processing**: Handle multiple images or data efficiently
- **Data Management**: Organize and manipulate workflow data

### Advanced Workflows
- **Model Optimization**: Leverage different model types efficiently
- **Memory Management**: Handle large-scale generations with optimization
- **Debug & Analysis**: Troubleshoot and optimize workflow performance

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Links

- **Repository**: [GitHub](https://github.com/przewodo/ComfyUI-Przewodo-Utils)
- **ComfyUI Registry**: [Registry Page](https://registry.comfy.org)
- **Issues**: [Bug Reports & Feature Requests](https://github.com/przewodo/ComfyUI-Przewodo-Utils/issues)
- **Discussions**: [Community Discussions](https://github.com/przewodo/ComfyUI-Przewodo-Utils/discussions)

## 🙏 Acknowledgments

- ComfyUI team for the excellent framework
- Community contributors for feedback and testing
- Wan2.1 model developers for advanced video generation capabilities

---

*Made with ❤️ for the ComfyUI community*