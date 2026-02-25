# ComfyUI Conditioning Resizer

A custom node for ComfyUI that allows resizing of conditioning tensors, particularly useful for fixing size mismatches between CLIP Text Encode and CLIP Vision Encode outputs in SD3 workflows.

## Problem This Solves

When using StyleModelApply with CLIP Vision Encode alongside CLIP Text Encode in SD3 workflows, you might encounter size mismatches in the attention bias tensors:

- CLIP Text Encode typically outputs attention bias with dimensions such as (1, 24, 5273, 5273)
- StyleModelApply with CLIP Vision outputs attention bias with different dimensions like (1, 24, 4544, 4544)

This mismatch causes errors when these conditioning tensors need to be combined in nodes like RegionMaskConditioning.

## Features

- Resize conditioning attention bias tensors to match a target size
- Two resize methods:
  - `pad_or_trim`: Simple padding or trimming to target size
  - `interpolate`: Uses bilinear interpolation for resizing
- Adjustable padding value

## Installation

1. Clone this repository into your ComfyUI custom nodes directory:
```bash
cd /path/to/ComfyUI/custom_nodes/
git clone https://github.com/yourusername/comfyui-conditioning-resizer.git
```

2. Restart ComfyUI to load the new node

## Usage

1. Add the "Conditioning Resizer" node to your workflow
2. Connect the output from your StyleModelApply node to the "conditioning" input
3. Set the target_length to match your CLIP Text Encode output (typically 5273 for SD3)
4. Connect the output to nodes like RegionMaskConditioning

## Parameters

- **conditioning**: The conditioning tensor to resize
- **target_length**: The desired sequence length (default: 5273)
- **resize_method**: 
  - `pad_or_trim`: Pads or trims the tensor (faster, simpler)
  - `interpolate`: Uses bilinear interpolation (may preserve more information)
- **pad_value**: Value used for padding (default: 0.0)

## Example Workflow

Insert this node between your StyleModelApply node and any node that expects conditioning with a specific size (like RegionMaskConditioning):

```
StyleModelApply → Conditioning Resizer → RegionMaskConditioning
```

## License

MIT
