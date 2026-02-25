# EternalKernel PyTorch Nodes

[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0+-red.svg)](https://pytorch.org/)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)

A comprehensive collection of PyTorch nodes for ComfyUI, enabling advanced machine learning workflows with neural network training, inference, and data manipulation capabilities.

## 🌟 Features

### 🧠 Neural Network Components
- **Layer Nodes**: Linear, Convolutional, BatchNorm, Dropout, Transformer layers
- **Activation Functions**: ReLU, Sigmoid, Tanh, Softmax, and more
- **Model Building**: Sequential model construction and layer extraction
- **Architecture Tools**: Reshape, flatten, and tensor manipulation utilities

### 🚀 Training & Inference
- **Model Training**: Full training loops with loss computation and optimization
- **Grid Search**: Automated hyperparameter optimization
- **Inference**: Efficient model inference with GPU acceleration
- **Model Management**: Save/load PyTorch models with metadata

### 📊 Data Handling
- **Dataset Tools**: Download popular datasets (MNIST, CIFAR, etc.)
- **Data Processing**: Split, shuffle, and batch your datasets
- **Tensor Operations**: Slice, reshape, type conversion, and device management
- **ComfyUI Integration**: Convert between ComfyUI images and PyTorch tensors

### 🔧 Advanced Features
- **GPU Support**: Automatic CUDA acceleration when available
- **Model Modification**: Extract layers, freeze/unfreeze parameters
- **Visualization**: Plot training metrics and data distributions
- **Flexible I/O**: Support for various data formats and tensor types

## 📦 Installation

### Quick Start
1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes
```

2. Clone this repository:
```bash
git clone https://github.com/TashaSkyUp/EternalKernelPyTorchNodes.git
```

3. Install dependencies:
```bash
cd EternalKernelPyTorchNodes
pip install -r requirements.txt
```

4. Restart ComfyUI and the nodes will appear under the **ETK/pytorch** category.

### Requirements
- **Python**: 3.8 or higher
- **PyTorch**: 2.0+ (with CUDA support recommended)
- **ComfyUI**: Latest version
- **Dependencies**: See `requirements.txt` for full list

## 🎯 Node Categories

### Dataset & Data Processing
- `PyTorchDatasetDownloader` - Download popular ML datasets
- `DatasetSplitter` - Split datasets into train/test/validation
- `TensorsToDataset` - Create datasets from tensor collections
- `DatasetToDataloader` - Generate DataLoaders with batching

### Neural Network Layers
- `AddLinearLayerNode` - Fully connected layers
- `AddConvLayer` - Convolutional layers with customizable parameters
- `AddBatchNormLayer` - Batch normalization for stable training
- `AddDropoutLayer` - Regularization through dropout
- `AddTransformerLayer` - Modern attention-based layers
- `AddReshapeLayer` - Dynamic tensor reshaping

### Model Operations
- `SequentialModelProvider` - Build sequential neural networks
- `PyTorchInferenceNode` - Run inference on trained models
- `TrainModel` - Complete training loops with optimization
- `GridSearchTraining` - Automated hyperparameter tuning
- `SaveModel` / `LoadModel` - Model persistence with metadata

### Tensor Utilities
- `FlattenTensor` - Flatten multi-dimensional tensors
- `ReshapeTensor` - Reshape tensors to desired dimensions
- `SliceTensor` - Extract tensor slices and subsets
- `ChangeTensorType` - Convert between tensor data types
- `PyTorchToDevice` - Move tensors between CPU/GPU
- `RandomTensor` - Generate random tensors for testing

### Advanced Tools
- `ExtractLayersAsModel` - Extract sublayers as standalone models
- `AddModelAsLayer` - Embed existing models as layers
- `SetModelTrainable` - Freeze/unfreeze model parameters
- `FuncModifyModel` - Apply custom functions to models
- `PlotSeriesString` - Visualize training metrics

## 🚀 Usage Examples

### Basic Neural Network Training
Create and train a neural network with just a few nodes:

1. **Download Dataset** → **Split Data** → **Build Model** → **Train** → **Save**

### Grid Search Optimization
Automatically find the best hyperparameters for your model with the GridSearchTraining node.

### ComfyUI Integration
Seamlessly convert between ComfyUI images and PyTorch tensors for ML processing in your workflows.

## 🧪 Testing

Run the comprehensive test suite:
```bash
cd EternalKernelPyTorchNodes
python -m pytest tests/ -v
```

Tests cover all node functionality, model training/inference, tensor operations, and GPU/CPU compatibility.

## 🤝 Contributing

Contributions welcome! Please:
- Report bugs or issues
- Suggest new features  
- Submit pull requests
- Improve documentation

## 📋 Compatibility

- **ComfyUI**: All recent versions
- **OS**: Windows, macOS, Linux
- **Hardware**: CPU and CUDA GPUs
- **PyTorch**: 2.0+ (optimized for latest)

## 📄 License

GNU Affero General Public License v3.0 - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built for the [ComfyUI](https://github.com/comfyanonymous/ComfyUI) community, powered by [PyTorch](https://pytorch.org/).

---

**Made with ❤️ for the ComfyUI and PyTorch communities**

For support: [GitHub Issues](https://github.com/TashaSkyUp/EternalKernelPyTorchNodes/issues)
