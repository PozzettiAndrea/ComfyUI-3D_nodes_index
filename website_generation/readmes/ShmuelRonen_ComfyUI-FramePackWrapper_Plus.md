# ComfyUI-FramePackWrapper_Plus

An improved wrapper for the FramePack project that allows the creation of videos of any length based on reference images and LoRAs with F1 sampler.

## Features

- **F1 Sampler Support**: Uses the improved F1 video generation method for higher quality and better temporal coherence
- **LoRA Integration**: Full support for HunyuanVideo LoRAs with proper weight handling and fusion options
- **Timestamped Prompts**: Create dynamic videos with changing prompts at specific timestamps
- **Flexible Input Options**: Works with both reference images and empty latents for complete creative control
- **Resolution Control**: Automatic bucket finding for optimal video dimensions
- **Blend Control**: Smooth transitions between different prompts at timestamps

## Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ShmuelRonen/ComfyUI-FramePackWrapper_Plus
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Download the necessary model files and place them in your models folder:
- FramePackI2V_HY: [HuggingFace Link](https://huggingface.co/lllyasviel/FramePackI2V_HY)
- FramePack_F1_I2V_HY: [HuggingFace Link](https://huggingface.co/lllyasviel/FramePack_F1_I2V_HY_20250503)

## Model Files

### Main Model Options
- [FramePackI2V_HY_fp8_e4m3fn.safetensors](https://huggingface.co/Kijai/HunyuanVideo_comfy/blob/main/FramePackI2V_HY_fp8_e4m3fn.safetensors) - Optimized fp8 version (smaller file size)
- [FramePackI2V_HY_bf16.safetensors](https://huggingface.co/Kijai/HunyuanVideo_comfy/blob/main/FramePackI2V_HY_bf16.safetensors) - BF16 version (better quality)

### Required Components
- **CLIP Vision**: [sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384/tree/main)
- **Text Encoder and VAE**: [HunyuanVideo_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/tree/main/split_files)

## Usage

### Basic Workflow

1. Load the HunyuanVideo model with your preferred settings
2. (Optional) Add LoRAs with the FramePackLoraSelect node
3. Prepare your input image or empty latent
4. Set up CLIP Vision encoding for image embeddings
5. Create timestamped prompts with FramePackTimestampedTextEncode
6. Generate your video with FramePackSampler (F1)

### Example Workflow

![image](https://github.com/user-attachments/assets/e7ba12b5-41ef-484b-a796-801b701628a5)

### Timestamped Prompts

Use the following format for timestamped prompts:
```
[0s: A beautiful landscape, mountains in the background]
[5s-10s: Camera pans to reveal a lake, reflections of clouds]
[10s: A boat appears on the horizon, sailing slowly]
```

- `[Xs: prompt]`: Starts at X seconds and continues until the next timestamp
- `[Xs-Ys: prompt]`: Active from X seconds to Y seconds

### LoRA Usage

1. Place your HunyuanVideo LoRAs in the `ComfyUI/models/loras` folder
2. Use the FramePackLoraSelect node to add them to your workflow
3. Adjust strength as desired (typically 0.5-1.2)
4. Set fuse_lora to false for flexibility or true for performance

## Node Reference

### FramePackSampler (F1)
The main generation node using the F1 sampling technique.

**Inputs:**
- `model`: The loaded FramePack model
- `positive_timed_data`: Timestamped positive prompts
- `negative`: Negative prompt conditioning
- `start_latent`: Initial latent for generation
- `start_image_embeds`: CLIP Vision embeddings for start image
- `end_latent`: (Optional) End latent for transitions
- `end_image_embeds`: (Optional) CLIP Vision embeddings for end image
- `initial_samples`: (Optional) For video-to-video generation
- Various sampling parameters (steps, CFG, guidance scale, etc.)

### FramePackTimestampedTextEncode
Encodes text prompts with timestamps for timed conditioning.

**Inputs:**
- `clip`: CLIP text model
- `text`: Text prompt with timestamps
- `negative_text`: Negative prompt
- `total_second_length`: Video duration in seconds
- `latent_window_size`: Processing window size
- `prompt_blend_sections`: Number of sections to blend prompts

### FramePackLoraSelect
Selects and configures LoRA models.

**Inputs:**
- `lora`: LoRA model selection
- `strength`: LoRA strength (0.0-2.0)
- `fuse_lora`: Whether to fuse the LoRA weights into the base model
- `prev_lora`: (Optional) For chaining multiple LoRAs

### LoadFramePackModel / DownloadAndLoadFramePackModel
Loads the FramePack model with various precision options.

## Advanced Tips

1. **Resolution Control**: Use the FramePackFindNearestBucket node to optimize dimensions
2. **Memory Management**: Adjust gpu_memory_preservation for large models
3. **Blending Prompts**: Set prompt_blend_sections > 0 for smooth transitions
4. **Multiple LoRAs**: Chain several LoRAs together for combined effects
5. **Empty Latents**: Use an Empty Latent Image node when starting from scratch

## Troubleshooting

- **CUDA Out of Memory**: Reduce resolution, decrease latent_window_size, or increase gpu_memory_preservation
- **LoRA Loading Issues**: Ensure LoRAs are in the correct format (safetensors)
- **Video Artifacts**: Try increasing steps or adjusting CFG/guidance_scale

## Acknowledgements

- Based on the original [ComfyUI-FramePackWrapper](https://github.com/kijai/ComfyUI-FramePackWrapper) by kijai
- Uses models from [FramePack](https://github.com/lllyasviel/Fooocus-FramePack) by lllyasviel
- Special thanks to the ComfyUI and Stable Diffusion communities

## License

[MIT License](LICENSE)

## Credits

This project is an extension of the original [ComfyUI-FramePackWrapper](https://github.com/kijai/ComfyUI-FramePackWrapper) created by kijai. The original wrapper provided the foundation for working with FramePack models in ComfyUI.

ComfyUI-FramePackWrapper_Plus builds upon that foundation by adding support for:
- F1 sampler for improved temporal coherence
- LoRA integration for customized generation
- Timestamped prompts for dynamic video creation
- Additional workflow improvements and optimizations

Special thanks to kijai for the original implementation that made this extension possible.
