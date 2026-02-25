# ComfyUI Model Quantizer

A comprehensive custom node pack for ComfyUI that provides advanced tools for quantizing model weights to lower precision formats like FP16, BF16, and true FP8 types, with specialized support for ControlNet models.


![image](https://github.com/user-attachments/assets/070b741d-e682-4e08-a4b4-5be8b2abd64f)


## Overview

This node pack provides powerful quantization tools directly within ComfyUI, including:

### Standard Quantization Nodes
1.  **Model To State Dict**: Extracts the state dictionary from a model object and attempts to normalize keys.
2.  **Quantize Model to FP8 Format**: Converts model weights directly to `float8_e4m3fn` or `float8_e5m2` format (requires CUDA).
3.  **Quantize Model Scaled**: Applies simulated FP8 scaling (per-tensor or per-channel) and then casts the model to `float16`, `bfloat16`, or keeps the original format.
4.  **Save As SafeTensor**: Saves the processed state dictionary to a `.safetensors` file at a specified path.

### NEW: ControlNet FP8 Quantization Nodes
5.  **ControlNet FP8 Quantizer**: Advanced FP8 quantization specifically designed for ControlNet models with precision-aware quantization, tensor calibration, and ComfyUI folder integration.
6.  **ControlNet Metadata Viewer**: Analyzes and displays ControlNet model metadata, tensor information, and structure for debugging and optimization.

### NEW: GGUF Model Quantization
7.  **GGUF Quantizer 👾**: Advanced GGUF quantization wrapper around @city96 GGUF tools, optimized for diffusion models including WAN, HunyuanVid, and FLUX. Supports multiple quantization levels (F16, Q4_K_M, Q5_0, Q8_0, etc.) with automatic architecture detection and 5D tensor handling.

## Installation

1.  Clone or download this repository into your ComfyUI's `custom_nodes` directory.
    * Example using git:
        ```bash
        cd ComfyUI/custom_nodes
        git clone [https://github.com/YourUsername/YourRepoName.git](https://github.com/YourUsername/YourRepoName.git) ComfyUI-ModelQuantizer
        # Replace with your actual repo URL and desired folder name
        ```
    * Alternatively, download the ZIP and extract it into `ComfyUI/custom_nodes/ComfyUI-ModelQuantizer`.

2.  Install dependencies:
    ```bash
    cd ComfyUI/custom_nodes/ComfyUI-ModelQuantizer
    pip install -r requirements.txt
    ```

3.  **For ControlNet quantization**, ensure your ControlNet models are in the correct folder:
    ```
    ComfyUI/models/controlnet/
    ├── control_v11p_sd15_canny.safetensors
    ├── control_v11p_sd15_openpose.safetensors
    └── ...
    ```

4.  Restart ComfyUI.

## Usage

### Model To State Dict
* **Category:** `Model Quantization/Utils`
* **Function:** Extracts state dict from a MODEL object, stripping common prefixes.
* **Inputs**:
    * `model`: The input `MODEL` object.
* **Outputs**:
    * `model_state_dict`: The extracted state dictionary.

### Quantize Model to FP8 Format
* **Category:** `Model Quantization/FP8 Direct`
* **Function:** Converts model weights directly to a specific FP8 format. Requires CUDA.
* **Inputs**:
    * `model_state_dict`: The state dictionary to quantize.
    * `fp8_format`: The target FP8 format (`float8_e5m2` or `float8_e4m3fn`).
* **Outputs**:
    * `quantized_model_state_dict`: The state dictionary with FP8 tensors.

### Quantize Model Scaled
* **Category:** `Model Quantization`
* **Function:** Applies simulated FP8 value scaling and then casts to FP16, BF16, or keeps the original dtype. Useful for size reduction with good compatibility.
* **Inputs**:
    * `model_state_dict`: The state dictionary to quantize.
    * `scaling_strategy`: How to simulate scaling (`per_tensor` or `per_channel`).
    * `processing_device`: Where to perform calculations (`Auto`, `CPU`, `GPU`).
    * `output_dtype`: Final data type (`Original`, `float16`, `bfloat16`). Defaults to `float16`.
* **Outputs**:
    * `quantized_model_state_dict`: The processed state dictionary.

### Save As SafeTensor
* **Category:** `Model Quantization/Save`
* **Function:** Saves the processed state dictionary to a `.safetensors` file.
* **Inputs**:
    * `quantized_model_state_dict`: The state dictionary to save.
    * `absolute_save_path`: The full path (including filename) where the model will be saved.
* **Outputs**: None (Output node).

### ControlNet FP8 Quantizer
* **Category:** `Model Quantization/ControlNet`
* **Function:** Advanced FP8 quantization specifically designed for ControlNet models with precision-aware quantization and tensor calibration.
* **Inputs**:
    * `controlnet_model`: Dropdown selection of ControlNet models from `models/controlnet/` folder
    * `fp8_format`: FP8 format (`float8_e4m3fn` recommended, or `float8_e5m2`)
    * `quantization_strategy`: `per_tensor` (faster) or `per_channel` (better quality)
    * `activation_clipping`: Enable percentile-based outlier handling (recommended)
    * `custom_output_name`: Optional custom filename for output
    * `calibration_samples`: Number of samples for tensor calibration (10-1000, default: 100)
    * `preserve_metadata`: Preserve original metadata in output file
* **Outputs**:
    * `status`: Operation status and result message
    * `metadata_info`: JSON-formatted metadata information
    * `quantization_stats`: Detailed compression statistics and ratios

### ControlNet Metadata Viewer
* **Category:** `Model Quantization/ControlNet`
* **Function:** Analyzes and displays ControlNet model metadata, tensor information, and structure.
* **Inputs**:
    * `controlnet_model`: Dropdown selection of ControlNet models from `models/controlnet/` folder
* **Outputs**:
    * `metadata`: JSON-formatted original metadata
    * `tensor_info`: Detailed tensor information including shapes, dtypes, and sizes
    * `model_analysis`: Model structure analysis including layer types and statistics

### GGUF Quantizer 👾
* **Category:** `Model Quantization/GGUF`
* **Function:** Advanced GGUF quantization wrapper around City96's GGUF tools for diffusion models. Supports automatic architecture detection and multiple quantization formats.
* **Inputs**:
    * `model`: Input MODEL object (UNET/diffusion model)
    * `quantization_type`: Target quantization format (`F16`, `Q4_K_M`, `Q5_0`, `Q8_0`, `ALL`, etc.)
    * `output_path_template`: Output path template (relative or absolute)
    * `is_absolute_path`: Toggle between relative (ComfyUI output) and absolute path modes
    * `setup_environment`: Run llama.cpp setup if needed
    * `verbose_logging`: Enable detailed debug logging
* **Outputs**:
    * `status_message`: Operation status and detailed progress information
    * `output_gguf_path_or_dir`: Path to generated GGUF file(s)

**Supported Models:**
- ✅ **WAN** (Weights Are Not) - Video generation models
- ✅ **HunyuanVid** - Hunyuan video diffusion models
- ✅ **FLUX** - FLUX diffusion models with proper tensor handling
- 🚧 **LTX** - Coming soon
- 🚧 **HiDream** - Coming soon

## Example Workflows

### Standard Model Quantization
1.  Load a model using a standard loader (e.g., `Load Checkpoint`).
2.  Connect the `MODEL` output to the `Model To State Dict` node.
3.  Connect the `model_state_dict` output from `Model To State Dict` to `Quantize Model Scaled`.
4.  In `Quantize Model Scaled`, select your desired `scaling_strategy` and set `output_dtype` to `float16` (for size reduction).
5.  Connect the `quantized_model_state_dict` output from `Quantize Model Scaled` to the `Save Model as SafeTensor` node.
6.  Specify the `absolute_save_path` in the `Save Model as SafeTensor` node.
7.  Queue the prompt.
8.  Restart ComfyUI or refresh loaders to find the saved model.

### ControlNet FP8 Quantization
1.  Add `ControlNet FP8 Quantizer` node to your workflow.
2.  Select your ControlNet model from the dropdown (automatically populated from `models/controlnet/`).
3.  Configure settings:
    * **FP8 Format**: `float8_e4m3fn` (recommended for most cases)
    * **Strategy**: `per_channel` (better quality) or `per_tensor` (faster)
    * **Activation Clipping**: `True` (recommended for better quality)
4.  Execute the workflow - quantized model automatically saved to `models/controlnet/quantized/`.
5.  Use `ControlNet Metadata Viewer` to analyze original vs quantized models.

### Batch ControlNet Processing
1.  Add multiple `ControlNet FP8 Quantizer` nodes.
2.  Select different ControlNet models in each node.
3.  Use consistent settings across all nodes.
4.  Execute to process multiple models simultaneously.

### GGUF Model Quantization
1.  Load your diffusion model using standard ComfyUI loaders.
2.  Add `GGUF Quantizer 👾` node to your workflow.
3.  Connect the `MODEL` output to the GGUF quantizer input.
4.  Configure settings:
    * **Quantization Type**: `Q4_K_M` (recommended balance), `Q8_0` (higher quality), or `ALL` (generate multiple formats)
    * **Output Path**: Specify where to save (e.g., `models/unet/quantized/`)
    * **Verbose Logging**: Enable for detailed progress information
5.  Execute workflow - quantized GGUF files will be saved to specified location.
6.  Use quantized models with ComfyUI-GGUF loader nodes.

**Note**: GGUF quantization requires significant RAM (96GB+) and processing time varies by model size.

## Features

### Advanced ControlNet Quantization
- **Precision-aware quantization** with tensor calibration and percentile-based scaling
- **Two FP8 formats**: `float8_e4m3fn` (recommended) and `float8_e5m2`
- **Quantization strategies**: per-tensor (faster) and per-channel (better quality)
- **Automatic ComfyUI integration** with dropdown model selection
- **Smart output management** - quantized models saved to `models/controlnet/quantized/`
- **Comprehensive analysis** with metadata viewer and detailed statistics
- **Fallback logic** for compatibility across different PyTorch versions

### Technical Capabilities
- **~50% size reduction** with maintained quality
- **Advanced tensor calibration** using statistical analysis
- **Activation clipping** with outlier handling
- **Metadata preservation** with quantization information
- **Error handling** with graceful fallbacks
- **Progress tracking** and detailed logging

### ComfyUI Integration
- **Automatic model detection** from `models/controlnet/` folder
- **Dropdown selection** - no manual path entry needed
- **Auto-generated filenames** with format and strategy information
- **Organized output** in dedicated quantized subfolder
- **Seamless workflow integration** with existing ControlNet nodes

## Requirements

### Core Dependencies
* PyTorch 2.0+ (for FP8 support, usually included with ComfyUI)
* `safetensors` >= 0.3.1
* `tqdm` >= 4.65.0

### Additional Dependencies (for ControlNet nodes)
* `tensorflow` >= 2.13.0 (optional, for advanced optimization)
* `tensorflow-model-optimization` >= 0.7.0 (optional)

### Hardware
* CUDA-enabled GPU recommended for FP8 operations
* CPU fallback available for compatibility

### GGUF Quantization Requirements
* **Minimum 96GB RAM** - Required for processing large diffusion models
* **Decent GPU** - For model loading and processing (VRAM requirements vary by model size)
* **Storage Space** - GGUF files can be large during processing (temporary files cleaned up automatically)
* **Python 3.8+** with PyTorch 2.0+

## Troubleshooting

### ControlNet Nodes Not Appearing
1. Ensure all dependencies are installed: `pip install -r requirements.txt`
2. Check that ControlNet models are in `ComfyUI/models/controlnet/` folder
3. Restart ComfyUI completely
4. Check console for import errors

### "No models found" in Dropdown
1. Place ControlNet models in `ComfyUI/models/controlnet/` folder
2. Supported formats: `.safetensors`, `.pth`
3. Check file permissions
4. Use manual path input as fallback if needed

### Quantization Errors
- **"quantile() input tensor must be either float or double dtype"**: Fixed in latest version
- **CUDA out of memory**: Use CPU processing or reduce batch size
- **FP8 not supported**: Upgrade PyTorch to 2.0+ or use CPU fallback

### Performance Tips
- **For best quality**: Use `per_channel` + `activation_clipping` + `float8_e4m3fn`
- **For speed**: Use `per_tensor` + reduce `calibration_samples`
- **Memory issues**: Process models one at a time

## Workflow Examples

Pre-made workflow JSON files are available in the `examples/` folder:
- `workflow_controlnet_fp8_quantization.json` - Basic ControlNet quantization
- `workflow_advanced_controlnet_quantization.json` - Advanced with verification
- `workflow_integrated_quantization.json` - Integration with existing nodes
- `workflow_batch_controlnet_quantization.json` - Batch processing multiple models

## Development Roadmap & TODO

### Completed Features ✅
#### Standard Quantization
- [x] **FP16 Quantization** - Standard half-precision quantization
- [x] **BF16 Quantization** - Brain floating-point 16-bit format
- [x] **FP8 Direct Quantization** - True FP8 formats (float8_e4m3fn, float8_e5m2)
- [x] **FP8 Scaled Quantization** - Simulated FP8 with scaling strategies
- [x] **Per-Tensor & Per-Channel Scaling** - Multiple quantization strategies
- [x] **State Dict Extraction** - Model to state dictionary conversion
- [x] **SafeTensors Export** - Reliable model saving format

#### ControlNet FP8 Integration
- [x] **ControlNet FP8 Quantizer** - Specialized FP8 quantization for ControlNet models
- [x] **Precision-Aware Quantization** - Advanced tensor calibration and scaling

#### GGUF Quantization
- [x] **WAN Model Support** - Complete with 5D tensor handling
- [x] **HunyuanVid Model Support** - Architecture detection and conversion
- [x] **FLUX Model Support** - Proper tensor prefix handling and quantization
- [x] **Automatic Architecture Detection** - Smart model type detection
- [x] **5D Tensor Handling** - Special handling for complex tensor shapes
- [x] **Path Management** - Robust absolute/relative path handling
- [x] **Multiple GGUF Formats** - F16, Q4_K_M, Q5_0, Q8_0, and more

### Upcoming Features 🚧
- [ ] **LTX Model Support** - Integration planned for next release
- [ ] **HiDream Model Support** - Integration planned for next release
- [ ] **DFloat11 Quantization** - Ultra-low precision format coming soon
- [ ] **Memory Optimization** - Reduce RAM requirements where possible
- [ ] **Batch Processing** - Support for multiple models in single operation

### Known Issues
- [ ] **High RAM Requirements** - Currently requires 96GB+ RAM for large models
- [ ] **Processing Time** - Large models can take significant time to process
- [ ] **Temporary File Cleanup** - Ensure all temporary files are properly cleaned up

## Acknowledgments

This project wraps and extends [City96's GGUF tools](https://github.com/city96/ComfyUI-GGUF) for diffusion model quantization. Special thanks to the City96 team for this excellent GGUF implementation and the broader ComfyUI community for their contributions.

## License

MIT (Or your chosen license)
