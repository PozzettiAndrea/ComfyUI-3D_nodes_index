# ComfyUI-Prepack

**Version: 1.7.0**

A comprehensive workflow optimization toolkit for ComfyUI, providing essential nodes for model management, sampling control, and workflow enhancement with professional-grade reliability.

## 🚀 Features

### Model Management
- **💀Prepack Model DualCLIP** - Load models with dual CLIP encoders
- **💀Prepack Model SingleCLIP** - Load models with single CLIP encoder
- **💀Prepack Loras** - Apply up to 3 LoRA adapters with text document integration
- **💀Prepack Loras and MSSD3** - LoRA management with MSSD3 support

### Sampling Control
- **💀Prepack Ksampler** - Enhanced KSampler with optimized parameters
- **💀Prepack Ksampler Advanced** - Advanced sampling control with additional options
- **💀Prepack Seed** - Smart seed management with random generation and history tracking

### Workflow Management
- **💀Prepack SetPipe** - Set and store workflow pipeline states (now includes LoRA path support)
- **💀Prepack GetPipe** - Retrieve and use stored pipeline states (now includes LoRA path output)

### Logic Operations
- **💀Prepack Logic Int** - Integer logic operations and comparisons
- **💀Prepack Logic String** - String logic operations and manipulations

### Integer Operations
- **💀Prepack Int Combine** - Combine up to 4 integers into a string with selectable separator
- **💀Prepack Int Split** - Split a string into up to 4 integers using selectable separator

### Math Operations
- **💀Prepack Calculator** - Evaluate mathematical expressions with variables a, b, c, d. Supports custom formulas like `(a*c)+d/2`. Outputs both integer and float results

### Type Conversion
- **💀Prepack Number Type Converter** - Convert between string, int, and float types. Accepts any of these types and outputs all three simultaneously

### File Management
- **💀Save By File Name** - Smart file saving with format preservation and custom naming. Supports images (WebP, JPEG, PNG, GIF), videos (MP4, AVI), and text files with automatic format detection

### Workflow Tools
- **💀Export Workflow as PNG** - Export complete workflow as PNG image with embedded workflow data or image only. Accessible via right-click canvas menu

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "Prepack"
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation
1. Navigate to your ComfyUI custom_nodes directory:
   ```
   cd ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```
   git clone https://github.com/S4MUEL-404/ComfyUI-Prepack.git
   ```
3. Install dependencies (minimal requirements):
   ```
   pip install -r ComfyUI-Prepack/requirements.txt
   ```
4. Restart ComfyUI

## 🔧 Dependencies

This package has minimal dependencies and uses built-in ComfyUI functionality:
- **PyTorch** - Core tensor operations (usually already available)
- **NumPy** - Numerical computations (usually already available)

All dependencies are typically already available in standard ComfyUI installations.

## 📖 Usage

1. **Find Nodes**: All Prepack nodes are prefixed with 💀 in the ComfyUI node browser
2. **Categories**: Look under "💀Prepack" category
3. **Professional Quality**: All nodes include comprehensive error handling
4. **Smart Features**: Advanced UI controls with JavaScript extensions

### Quick Start Example
1. Add any Prepack node to your workflow
2. Configure node parameters
3. Connect to your existing workflow
4. Execute workflow with enhanced control

## 🎯 Key Features

- ✅ **Workflow Optimization** - Streamlined model and sampling management
- ✅ **Smart UI Controls** - Enhanced interfaces with JavaScript extensions
- ✅ **LoRA Integration** - Advanced LoRA management with text document support
- ✅ **Pipeline Management** - Store and retrieve workflow states efficiently
- ✅ **Seed Management** - Smart seed control with history tracking
- ✅ **Logic Operations** - Comprehensive logic and comparison tools
- ✅ **File Management** - Smart file saving with format preservation and custom naming
- ✅ **Workflow Export** - Export workflow as PNG with embedded data support

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or report issues.

## 📜 License

This project is open source. Please respect the licensing terms.

---

**Author:** S4MUEL  
**Website:** [s4muel.com](https://s4muel.com)  
**GitHub:** [https://github.com/S4MUEL-404/ComfyUI-Prepack](https://github.com/S4MUEL-404/ComfyUI-Prepack)  
**Version:** 1.7.0
