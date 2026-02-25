# ComfyUI-GROUT

Custom ComfyUI nodes for **GROUT** (Geometric Reasoning Over Unstructured Tessellations) - a deep learning model for detecting and segmenting grout lines in mosaic images.

![Preview](Workflows/preview.png)

## Nodes

### GROUT Segmentation
Main segmentation node that processes mosaic images.

**Inputs:**
- `image`: Input mosaic image
- `device`: Select CUDA or CPU for inference
- `threshold`: Initial threshold for binary mask (0.0 - 1.0)
- `model_path` (optional): Custom path to model weights. Leave empty to auto-download from HuggingFace.

**Outputs:**
- `probability_heatmap`: Grayscale probability map (0-1 range)
- `binary_mask`: Thresholded binary mask as image
- `mask`: ComfyUI MASK format for compositing

### GROUT Threshold
Post-processing node to adjust threshold without re-running inference.

**Inputs:**
- `probability_heatmap`: Output from GROUT Segmentation node
- `threshold`: Threshold value (0.0 - 1.0)

**Outputs:**
- `binary_mask`: Thresholded binary mask as image
- `mask`: ComfyUI MASK format

### GROUT Heatmap Colorize
Visualization node to apply colormap to probability heatmap.

**Inputs:**
- `probability_heatmap`: Output from GROUT Segmentation node
- `colormap`: Select from magma, viridis, plasma, inferno, hot, jet

**Outputs:**
- `colored_heatmap`: Colorized visualization

## Installation

### Option 1: ComfyUI Manager
Search for "GROUT" in ComfyUI Manager and install.

### Option 2: Manual Installation
1. Navigate to your ComfyUI custom nodes folder:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/advancedtech-sk/ComfyUI-GROUT.git
   ```

3. Install dependencies:
   ```bash
   cd ComfyUI-GROUT
   pip install -r requirements.txt
   ```

   **For standalone Windows version** (portable/embedded Python):
   ```bash
   cd ComfyUI-GROUT
   ..\..\..\python_embeded\python.exe -m pip install -r requirements.txt
   ```

4. Restart ComfyUI

## Model Download

The model will be automatically downloaded from HuggingFace on first use. It will be saved to:
```
ComfyUI/models/grout/grout_b3_zeroshot_v1.pth
```

Alternatively, you can manually download from:
- [HuggingFace Model](https://huggingface.co/advancedtech-sk/GROUT)

## Example Workflow

```
[Load Image] -> [GROUT Segmentation] -> [probability_heatmap] -> [GROUT Threshold] -> [binary_mask]
                         |
                         +-> [GROUT Heatmap Colorize] -> [Preview Image]
```

**Workflow Tips:**
1. Use **GROUT Segmentation** to run inference once
2. Connect the `probability_heatmap` output to **GROUT Threshold**
3. Adjust the threshold slider in GROUT Threshold to tune the mask without re-running the model
4. Use **GROUT Heatmap Colorize** for visualization with different colormaps

## Links

- [GROUT Paper (Zenodo)](https://zenodo.org/records/18187265)
- [GROUT Model (HuggingFace)](https://huggingface.co/advancedtech-sk/GROUT)
- [GROUT Demo (HuggingFace Spaces)](https://huggingface.co/spaces/advancedtech-sk/GROUT)
- [GROUT GitHub](https://github.com/advancedtech-sk/GROUT)

## License

MIT License

## Author

Radoslav Lovecky, Institute of Advanced Technologies, Slovakia
