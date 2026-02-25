# ComfyUI Coherent Video Sampler Node (V0.3)

A custom node for ComfyUI that enables coherent video generation while maintaining efficient memory usage, specifically optimized for heavy models like Flux.

![image](https://github.com/user-attachments/assets/a690a69b-675c-4658-a1be-761017b0fabb)

## Features

- 🎥 Frame-by-frame video processing with motion preservation
- 🧠 Efficient memory management for heavy models
- 🔄 Progressive denoising with coherence maintenance
- 💫 Dynamic quality control and motion guidance
- 🎨 Style preservation across frames
- 🛠️ Advanced adjustment controls for fine-tuning

## Installation

Install from ComfyUI manager

or

Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes
```

Clone this repository:
```bash
git clone https://github.com/ShmuelRonen/ComfyUI-CohernetVideoSampler.git
```

Restart ComfyUI

## Usage

#### For Deforum-like results please use 'shuttle-3-diffusion-fp8.safetensors' 4 steps flux model

The node appears in the node menu as "Cohernet Video Sampler". 

### Core Parameters Guide

The sampler now includes four key adjustment parameters that work together to control different aspects of video generation:

1. **denoise** (0.0-1.0):
   - Primary denoising control for the sampling process
   - Controls overall deviation from input
   - Lower values (0.3-0.5): Subtle changes, closer to input
   - Higher values (0.7-0.9): More dramatic transformations
   - Recommended: 0.6 for balanced results

2. **motion_strength** (0.0-1.0):
   - Controls motion intensity between frames
   - Affects transition smoothness
   - Lower values (0.3-0.4): More static, stable output
   - Higher values (0.7-0.8): Pronounced motion, dynamic transitions
   - Recommended: 0.5 for natural movement

3. **consistency_strength** (0.0-1.0):
   - Maintains visual consistency across frames
   - Controls style preservation
   - Lower values (0.7-0.8): More variation allowed
   - Higher values (0.9-1.0): Strict consistency enforcement
   - Recommended: 0.9 for coherent results

4. **denoise_strength** (0.0-1.0):
   - Secondary denoising for artifact reduction
   - Fine-tunes final output quality
   - Lower values (0.5-0.7): Preserve more details
   - Higher values (0.8-0.9): Smoother, cleaner output
   - Recommended: 0.8 for balanced detail preservation

### Parameter Combinations for Different Effects

#### High Quality Stable Video
```
denoise: 0.6
motion_strength: 0.5
consistency_strength: 0.9
denoise_strength: 0.8
```

#### Dynamic Movement Priority
```
denoise: 0.5
motion_strength: 0.7
consistency_strength: 0.8
denoise_strength: 0.7
```

#### Maximum Detail Preservation
```
denoise: 0.4
motion_strength: 0.4
consistency_strength: 0.85
denoise_strength: 0.6
```

### Other Inputs
- `model`: Your diffusion model (tested extensively with Flux)
- `positive`: Positive prompt conditioning
- `negative`: Negative prompt conditioning
- `video_latents`: Input video in latent space (from VAE Encode)
- `seed`: Generation seed
- `steps`: Number of sampling steps
- `cfg`: Classifier free guidance scale
- `sampler_name`: Choice of sampler
- `scheduler`: Choice of scheduler

### Memory Management
The node implements several memory optimization techniques:
- Progressive batch processing
- Automatic VRAM cleanup
- Dynamic batch size adjustment
- Efficient latent space operations

This allows it to work smoothly even with memory-intensive models like Flux without OOM errors.

## Memory Usage Examples

When using with Flux model:
- 20 frame video @ 512x512: ~8GB VRAM
- 40 frame video @ 512x512: ~10GB VRAM
- Processing happens in windows of frames to maintain stable memory usage

## Optimization Tips

1. **For Smoother Videos:**
   - Increase consistency_strength
   - Decrease motion_strength slightly
   - Keep denoise moderate
   - Maintain high denoise_strength

2. **For More Dynamic Videos:**
   - Increase motion_strength
   - Decrease consistency_strength slightly
   - Lower denoise_strength for detail
   - Adjust denoise based on desired change level

3. **For Maximum Quality:**
   - Balance all parameters
   - Use higher consistency_strength
   - Moderate motion_strength
   - Higher denoise_strength

## Known Limitations

- Very long videos might need to be processed in segments
- Extreme motion can affect coherence
- High denoise values might reduce motion preservation
- Parameter interactions can be complex

## Future Plans

- Additional motion control parameters
- Custom denoising patterns
- Advanced style preservation options
- Multi-model support optimization
- Parameter presets for common use cases

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT License](LICENSE)

## Acknowledgments

- ComfyUI team for the amazing framework
- Flux model team for the inspiration in handling heavy models
