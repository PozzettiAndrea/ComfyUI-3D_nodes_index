# ComfyUI-CharaConsistent

Training-free CharaConsist algorithm implementation for ComfyUI - Generate consistent subjects across multiple generations with enhanced mask generation and multi-model support.

## License

MIT License

Copyright (c) 2025 ZHOU He
Email: he.zhou@unity.cn

Repository: https://github.com/thatname/Comfyui_CharaConsist
## Credits & References

This is a ComfyUI implementation of the CharaConsist algorithm originally developed by Murray-Wang et al.

- **Original Research**: [CharaConsist: Fine-Grained Consistent Character Generation](https://arxiv.org/abs/2507.11533) (ICCV 2025)
- **Original Implementation**: [Murray-Wang/CharaConsist](https://github.com/Murray-Wang/CharaConsist)
- **Project Page**: [https://murray-wang.github.io/CharaConsist/](https://murray-wang.github.io/CharaConsist/)

This ComfyUI implementation includes significant enhancements and improvements over the original algorithm.

## Overview

ComfyUI-CharaConsistent implements the training-free CharaConsist algorithm within ComfyUI, enabling generation of consistent subjects across multiple images. Unlike the original implementation which primarily supported FLUX models, this version extends compatibility to multiple state-of-the-art text-to-image models while introducing improvements to mask generation and workflow integration.

## Key Improvements Over Original

### Enhanced Mask Generation
- **Original Issue**: The original mask generation was not perfect, especially for Chroma models
- **Solution**: Support for external GroundingDinoSAM for more accurate mask extraction
- **Flexibility**: Users can choose between original or improved mask generation methods

### Expanded Model Support
- **Original**: Primarily FLUX models only
- **This Implementation**: 
  - FLUX models
  - Chroma models (optimal performance)
  - Qwen-Image models
  - Chroma1-Radiance T2I models

### Multi-Subject Support
- Supports simultaneous processing of multiple subjects in a single workflow
- Each subject gets independent attention caching and mask processing

### ComfyUI Integration
- Native ComfyUI node implementation
- Seamless workflow integration with other ComfyUI custom nodes
- Visual workflow examples provided

## Features

- ✅ **Training-free consistency** - No fine-tuning required
- ✅ **Multi-subject support** - Generate consistent multiple characters/objects
- ✅ **Enhanced mask generation** - GroundingDinoSAM integration for better results
- ✅ **Broad model compatibility** - Works with FLUX, Chroma, Qwen-Image, Chroma1-Radiance
- ✅ **Optimal for Chroma** - Best performance with Chroma models
- ✅ **Attention caching** - Efficient memory management for subject consistency
- ✅ **Cross-similarity matching** - Advanced subject matching algorithms
- ✅ **Visual workflow examples** - Ready-to-use JSON workflows

## Installation

1. Navigate to your ComfyUI `custom_nodes` directory
2. Clone or copy this repository:
   ```bash
   git clone https://github.com/thatname/Comfyui_CharaConsist.git
   ```
3. Restart ComfyUI
4. The nodes will appear in the `chara_consist` category

## Supported Models

| Model | Compatibility | Performance Notes |
|--------|---------------|------------------|
| **Chroma Models** | ✅ Excellent | **Best performance** - Recommended |
| **FLUX Models** | ✅ Good | Compatible, original algorithm focus |
| **Qwen-Image** | ✅ Good | Full support with example workflow |
| **Chroma1-Radiance** | ✅ Good | Compatible with T2I workflows |

### Model-Specific Notes
- **Chroma Models**: Optimal performance, enhanced mask generation recommended
- **FLUX Models**: Good compatibility, original mask generation works adequately
- **Qwen-Image**: Full support, see example workflow for best practices

## Mask Generation Options

### Option 1: Enhanced Mask Generation (Recommended)
- **Method**: External GroundingDinoSAM
- **Benefits**: 
  - Superior mask accuracy
  - Better edge detection
  - Improved results for Chroma models
- **Requirements**: GroundingDinoSAM custom node
- **Example Workflow**: See JSON examples for implementation

### Option 2: Original Mask Generation
- **Method**: Built-in algorithm
- **Benefits**: 
  - No additional dependencies
  - Faster processing
  - Works well with FLUX models
- **Limitations**: 
  - Less accurate for Chroma models
  - May have edge detection issues

## Example Workflows

### Chroma Workflow
- **File**: `chroma_chara_consist.json`
- **Model**: Chroma1-HD
- **Features**: 
  - Enhanced mask generation with GroundingDinoSAM
  - Multi-step generation pipeline
  - Optimal settings for Chroma models

### Qwen-Image Workflow
- **File**: `qwen_chara_consist.json`
- **Model**: Qwen-Image
- **Features**:
  - LoRA integration
  - CFG normalization
  - Optimized for Qwen architecture

## Node Documentation

This implementation includes 9 custom nodes:

### Core Nodes
1. **ExtractAttn** - Extracts attention data from model layers for subject analysis
2. **GenConsistent** - Generates consistent images using cached attention data
3. **GetCrossSim** - Computes cross-similarity between subject and target attention
4. **BatchedMaskedReferenceGen** - Applies masked attention for consistent generation

### Mask Processing Nodes
5. **MasksToPatches** - Converts pixel masks to patch-level masks for attention
6. **MaskToPatchMask** - Converts masks to patch format with configurable parameters
7. **PreviewSubjectMask** - Preview extracted subject masks

### Conditioning Nodes
8. **ReferenceConditionCombine** - Combines reference and target conditioning
9. **ConditioningMatchMask** - Matches reference conditions to target prompts

## Memory Requirements

**⚠️ Important RAM Considerations**

- **Per Subject**: 10s of gigabytes of System RAM required
- **Attention Caching**: Each subject needs separate attention cache
- **Multi-Subject**: Memory usage scales linearly with number of subjects
- **Recommendations**:
  - Minimum 32GB RAM for single subject
  - 64GB+ RAM recommended for multiple subjects
  - Monitor RAM usage during generation

### Optimization Tips
- Clear attention cache between sessions
- Use appropriate batch sizes
- Consider system RAM when planning multi-subject workflows

## Performance Tips

### Best Practices
1. **Model Selection**: Use Chroma models for best results
2. **Mask Generation**: Prefer GroundingDinoSAM for Chroma models
3. **Memory Management**: Monitor RAM usage closely
4. **Workflow Optimization**: Use provided example workflows as templates

### Troubleshooting
- **High RAM Usage**: Reduce batch size or number of subjects
- **Poor Mask Quality**: Switch to GroundingDinoSAM mask generation
- **Model Compatibility**: Ensure you're using supported model versions
- **Performance Issues**: Check system RAM availability

## Academic Citation

If you use CharaConsist in your research, please cite the original paper:

```bibtex
@inproceedings{CharaConsist,
  title={{CharaConsist}: Fine-Grained Consistent Character Generation},
  author={Wang, Mengyu and Ding, Henghui and Peng, Jianing and Zhao, Yao and Chen, Yunpeng and Wei, Yunchao},
  booktitle={ICCV},
  year={2025}
}
```

## Contributing

Contributions are welcome! Please feel free to submit issues and enhancement requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
