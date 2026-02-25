
# Apply Style Model Adjust for ComfyUI

A custom node that provides enhanced control over style transfer balance when 
using FLUX style models in ComfyUI. This node offers better control over the 
influence of text prompts versus style reference images.

![image](https://github.com/user-attachments/assets/17bbd3a9-3615-41e1-aed6-1ca34db5d36c)

## Features

- Enhanced prompt influence when reducing style strength
- Better balance between style transfer and text prompt conditioning
- Smoother transition between style and prompt dominance 
- Specifically optimized for FLUX style models and image variations

## Installation

1. Navigate to your ComfyUI's `custom_nodes` directory
2. Clone this repository:
```bash
cd custom_nodes
git clone https://github.com/ShmuelRonen/ComfyUI-Apply_Style_Model_Adjust.git
```

Or download and extract the zip file into your `ComfyUI/custom_nodes` folder.

## Usage

The node appears as "Apply Style Model (Adjusted)" under the 
conditioning/style_model category.

### Node Parameters

- **conditioning**: Base conditioning from your text prompt
- **style_model**: Loaded FLUX style model
- **clip_vision_output**: CLIP Vision encoding of reference image
- **strength**: Balance between style and prompt (0.0 - 1.0)
  - Low values (0.0-0.3): Text prompt dominates
  - Medium values (0.4-0.7): Balanced mix
  - High values (0.8-1.0): Style reference dominates

## Difference from Standard Style Model Apply

The standard Style Model Apply node can sometimes:
- Let style overwhelm prompt instructions
- Have abrupt transitions when adjusting strength
- Provide less control over the final result

This adjusted version:
- Maintains better prompt influence
- Provides smoother strength transitions
- Reduces maximum style influence
- Better handles text instructions while maintaining style

### FLUX Model Note

This node is optimized for use with FLUX.1 Redux which:
- Is designed for image variation generation
- Works as an adapter for FLUX.1 base models
- Naturally integrates into complex workflows
- Best used for subtle style adjustments

## Requirements

- ComfyUI (latest version)
- FLUX style models
- Standard ComfyUI dependencies

## Known Limitations

- Primary focus is on FLUX model compatibility
- Very low strength values (<0.2) might affect image quality
- Cannot override FLUX model's inherent limitations:
  - Heavy influence from input image
  - Limited ability to add new elements
  - Focus on variations rather than major changes

## Support

If you encounter issues:
1. Open an issue on GitHub
2. Check existing issues first
3. Provide your:
   - ComfyUI version
   - Workflow setup
   - Error messages if any

## Credits

Based on ComfyUI's original Style Model Apply node, with modifications for 
better control and balance.

## License

MIT License - feel free to use, modify, and distribute.

## Version History

### v1.0
- Initial release
- Improved balance control
- Better prompt influence scaling
```
