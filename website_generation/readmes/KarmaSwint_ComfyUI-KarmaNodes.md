# ComfyUI-KarmaNodes

Advanced KSampler node and professional post-processing tools for ComfyUI with multi-cycle sampling, progressive upscaling, and cinematic enhancement capabilities.

## Overview

ComfyUI-KarmaNodes provides a comprehensive suite of nodes for advanced image generation and post-processing:

- **Karma KSampler Cycle**: Specialized KSampler that performs multiple sampling cycles with progressive upscaling between cycles, enabling high-quality, high-resolution image generation with better detail preservation
- **Karma Film Grain**: Professional film grain simulation for authentic analog film texture and cinematic aesthetics
- **Karma Kolors**: Advanced color grading and correction tools for professional-grade color enhancement

## Features

### 🔄 Multi-Cycle Sampling
- **Progressive Upscaling**: Automatically upscales images between sampling cycles
- **Configurable Cycles**: Support for 2-12 sampling cycles
- **Dynamic Parameters**: Adjust sampling parameters between cycles

### 🎯 Advanced Sampling Control
- **Dual Model Support**: Switch between primary and secondary models at specified cycles
- **Additive Conditioning**: Blend additional positive/negative conditioning with strength scaling
- **Dynamic Denoise**: Configurable denoise strength scaling with minimum threshold protection
- **Steps Scaling**: Flexible steps adjustment with increment/decrement modes and threshold control
- **Threshold Management**: Auto-calculated or manual threshold settings for precise control

### 🔧 Upscaling Options
- **Basic Upscaling**: High-quality image rescaling with multiple resampling methods
- **Model-Based Upscaling**: Use dedicated upscale models for enhanced quality
- **Gradual Upscaling**: Multi-step upscaling for smoother transitions
- **Configurable Resampling**: Separate methods for image and latent space upscaling
- **VAE Compatibility**: Ensures dimensions are VAE-compatible (divisible by 8)

### ✨ Post-Processing
- **Sharpening Filter**: Optional unsharp mask filter between cycles
- **Film Grain Effects**: Realistic analog film grain simulation
- **Color Grading**: Professional color correction and enhancement
- **Tiled VAE Support**: Handle large images with tiled VAE processing
- **Memory Management**: Automatic device management for optimal performance

## Installation

### Method 1: ComfyUI Manager (Recommended)
1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
2. Search for "KarmaNodes" in the manager
3. Install and restart ComfyUI

### Method 2: Manual Installation
1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/karmaswint/ComfyUI-KarmaNodes.git
   ```

3. Install dependencies:
   ```bash
   cd ComfyUI-KarmaNodes
   pip install -r requirements.txt
   ```

4. Restart ComfyUI

## Usage

### Basic Workflow

1. **Add the Node**: Search for "Karma KSampler Cycle" in the node browser
2. **Connect Inputs**: 
   - Connect your model, VAE, and conditioning inputs
   - Provide an initial latent image
3. **Configure Parameters**:
   - Set the number of cycles (2-12)
   - Configure upscale factor and method
   - Adjust denoise strengths
4. **Run**: Execute the workflow

### Key Parameters

#### Core Sampling
- **Steps**: Number of sampling steps per cycle
- **Total Cycles**: Number of upscaling/sampling cycles (2-12)
- **Starting Denoise**: Denoise strength for the first cycle (0.0-1.0)
- **Cycle Denoise**: Denoise strength for subsequent cycles (0.0-1.0)

#### Denoise Scaling
- **Enable Denoise Scaling**: Automatically adjust denoise strength between cycles
- **Denoise Min Threshold**: Minimum denoise value to prevent going too low (0.01-1.0)

#### Steps Scaling
- **Enable Steps Scaling**: Automatically adjust sampling steps between cycles
- **Steps Scaling Value**: Amount to adjust steps by each cycle (1-50)
- **Steps Adjustment Mode**: 
  - `decrement`: Reduce steps each cycle (for refinement)
  - `increment`: Increase steps each cycle (for more detail)
- **Steps Threshold Mode**:
  - `auto`: Automatically calculate threshold based on initial steps
  - `manual`: Use a fixed threshold value
- **Steps Manual Threshold**: Fixed threshold when using manual mode (1-200)

#### Upscaling
- **Upscale Factor**: Total upscaling factor to achieve
- **Upscale Method**: 
  - `basic`: High-quality image rescaling
  - `model`: Use dedicated upscale model (requires upscale_model input)
- **Scale Sampling**: Resampling method for image upscaling (bilinear, bicubic, nearest, lanczos)
- **Latent Upscale Method**: Resampling method for latent space upscaling (bilinear, bicubic, nearest, lanczos)
- **Enable Gradual Upscaling**: Use multiple intermediate upscaling steps for smoother transitions
- **Gradual Upscale Steps**: Number of intermediate steps when gradual upscaling is enabled (1-10)

#### Advanced Features
- **Secondary Model**: Optional model to switch to at specified cycle
- **Secondary Model Start Cycle**: Cycle number to switch to secondary model (1-12)
- **Additive Conditioning**: Additional positive/negative prompts with strength control
- **Sharpening**: Apply unsharp mask filter between cycles

### Example Workflow

```
[Model] → [Karma KSampler Cycle] → [VAE Decode] → [Save Image]
[VAE] ↗                        ↘ [VAE]
[Positive Conditioning] ↗
[Negative Conditioning] ↗
[Empty Latent] ↗
```

## Advanced Usage

### Dual Model Workflow
Use different models for different phases of generation:
1. Connect primary model for initial cycles
2. Connect secondary model (optional)
3. Set "Secondary Model Start Cycle" to switch models mid-process

### Additive Conditioning
Enhance your prompts with additional conditioning:
1. Connect main positive/negative conditioning
2. Connect additive positive/negative conditioning (optional)
3. Adjust strength values and scaling options

### High-Resolution Generation
For very high-resolution outputs:
1. Start with lower resolution latent
2. Set higher upscale factor (2.0-4.0)
3. Use more cycles (4-8) for gradual upscaling
4. Enable tiled VAE for memory efficiency

### Steps Scaling Strategies

#### Decrement Mode (Refinement Strategy)
Best for progressive refinement with fewer steps in later cycles:
- **Use Case**: When you want detailed initial generation, then refinement
- **Configuration**: 
  - Steps Adjustment Mode: `decrement`
  - Steps Scaling Value: 3-8 (moderate reduction)
  - Threshold Mode: `auto` (prevents going too low)
- **Example**: 20 → 15 → 10 → 5 steps across 4 cycles

#### Increment Mode (Detail Enhancement Strategy)
Best for progressive detail enhancement with more steps in later cycles:
- **Use Case**: When you want quick initial generation, then detailed refinement
- **Configuration**:
  - Steps Adjustment Mode: `increment`
  - Steps Scaling Value: 5-10 (moderate increase)
  - Threshold Mode: `manual` with reasonable cap (e.g., 50)
- **Example**: 10 → 15 → 20 → 25 steps across 4 cycles

### Gradual Upscaling
For smoother upscaling transitions:
1. Enable "Gradual Upscaling"
2. Set "Gradual Upscale Steps" to 3-5
3. Use with higher upscale factors (3.0+) for best results

## Post-Processing Nodes

ComfyUI-KarmaNodes includes specialized post-processing nodes for enhancing your generated images with professional-grade effects and color corrections.

### 🎬 Karma Film Grain

Add authentic analog film grain texture to your images for a cinematic, vintage aesthetic.

#### Features
- **Realistic Multi-Layer Grain**: Combines multiple noise layers for authentic film texture
- **Luminance-Based Intensity**: More grain in darker areas, mimicking real film behavior
- **Configurable Parameters**: Adjustable grain strength and particle size
- **Reproducible Results**: Seed-based grain patterns for consistent outputs
- **Fallback Support**: Works even without scipy dependency

#### Parameters
- **Strength** (0.01-1.0): Intensity of the film grain effect
- **Grain Size** (0.1-5.0): Size/scale of grain particles
- **Seed** (0-2³¹-1): Random seed for reproducible grain patterns

#### Usage Tips
- **Subtle Effects**: Use strength values 0.05-0.15 for realistic film look
- **Vintage Style**: Higher strength (0.2-0.4) with larger grain size (2.0-3.0)
- **Fine Detail**: Smaller grain size (0.5-1.0) for high-resolution images
- **Consistency**: Use the same seed across similar images for matching grain patterns

### 🎨 Karma Kolors

Professional color grading and correction tools for precise image enhancement.

#### Features
- **White Balance Correction**: Temperature-based color correction (2000K-10000K)
- **Brightness Control**: Precise brightness adjustments (-20% to +20%)
- **Contrast Enhancement**: Professional contrast control with fine increments
- **Saturation Adjustment**: Color intensity control for vibrant or muted looks
- **Optimal Processing Order**: Adjustments applied in the correct sequence for best results

#### Parameters
- **White Balance**: Temperature in Kelvin (2000K-10000K) or "auto"
  - **2000K-3000K**: Warm, candlelight tones
  - **3000K-4000K**: Warm white, tungsten lighting
  - **5000K-6500K**: Daylight, neutral white
  - **6500K-10000K**: Cool, blue-tinted lighting
- **Brightness** (-20% to +20%): Overall image brightness in 0.5% increments
- **Contrast** (-20% to +20%): Contrast adjustment in 0.5% increments
- **Saturation** (-20% to +20%): Color intensity in 0.5% increments

#### Usage Tips
- **Natural Corrections**: Start with small adjustments (±2-5%)
- **Creative Looks**: Combine temperature shifts with saturation changes
- **Portrait Enhancement**: Slight brightness (+2-5%) and contrast (+3-8%)
- **Landscape Vibrancy**: Increase saturation (+5-10%) with slight contrast boost
- **Vintage Look**: Warm temperature (3000K-4000K) with reduced saturation (-5-10%)

### Post-Processing Workflow Examples

#### Basic Enhancement Chain
```
[Generated Image] → [Karma Kolors] → [Karma Film Grain] → [Save Image]
```

#### Professional Color Grading
```
[Generated Image] → [Karma Kolors] → [Additional Processing] → [Final Output]
                     ↓
                   White Balance: 5500K
                   Brightness: +3.0%
                   Contrast: +5.0%
                   Saturation: +2.0%
```

#### Cinematic Film Look
```
[Generated Image] → [Karma Kolors] → [Karma Film Grain] → [Save Image]
                     ↓                ↓
                   Warm tone (3200K)   Strength: 0.12
                   Contrast: +8%       Grain Size: 1.5
                   Saturation: -3%     Seed: 42
```

## Requirements

- **Python**: 3.9+
- **PyTorch**: 2.0.0+
- **Pillow**: 9.0.0+
- **NumPy**: 1.21.0+
- **scikit-image**: 0.19.0+
- **ComfyUI**: Latest version

### Optional Dependencies
- **scipy**: 1.9.0+ (recommended for enhanced film grain quality)
- **colorsys**: Built-in Python module (used for color space conversions)

## Performance Tips

1. **Memory Management**: Enable tiled VAE for large images
2. **Cycle Count**: More cycles = better quality but longer processing time
3. **Upscale Factor**: Higher factors require more VRAM
4. **Model Selection**: Use appropriate models for your target resolution

## Troubleshooting

### Common Issues

**Out of Memory Errors**:
- Enable tiled VAE processing
- Reduce upscale factor or number of cycles
- Use smaller initial latent size
- Disable gradual upscaling to reduce intermediate steps

**Poor Quality Results**:
- Increase number of cycles
- Adjust denoise strengths and enable denoise scaling
- Try different upscaling methods
- Enable sharpening filter
- Use steps scaling with increment mode for more detail in later cycles
- Enable gradual upscaling for smoother transitions

**Slow Performance**:
- Reduce number of cycles
- Use basic upscaling instead of model-based
- Use steps scaling with decrement mode to reduce steps in later cycles
- Disable gradual upscaling
- Use auto threshold mode for steps scaling

**Steps Scaling Issues**:
- **Steps going too low**: Use manual threshold mode with appropriate minimum
- **Steps going too high**: Use manual threshold mode with reasonable maximum
- **Inconsistent results**: Try auto threshold mode for balanced scaling

**Post-Processing Issues**:
- **Film grain too strong**: Reduce strength value (try 0.05-0.10 for subtle effects)
- **Grain pattern inconsistent**: Use the same seed value across related images
- **Color corrections too harsh**: Use smaller adjustment increments (±1-3%)
- **White balance not working**: Ensure temperature value is within 2000K-10000K range
- **Scipy warning for film grain**: Install scipy for better grain quality: `pip install scipy`

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built for the [ComfyUI](https://github.com/comfyanonymous/ComfyUI) ecosystem
- Inspired by progressive sampling techniques in diffusion models
- Thanks to the ComfyUI community for feedback and testing

## Support

- **Issues**: [GitHub Issues](https://github.com/karmaswint/ComfyUI-KarmaNodes/issues)
- **Discussions**: [GitHub Discussions](https://github.com/karmaswint/ComfyUI-KarmaNodes/discussions)
- **Email**: karma@karmaviz.biz

## ☕ Support Development

If you find ComfyUI-KarmaNodes useful and want to support future development, consider buying me a coffee! Your support helps maintain and improve these tools, develop new features, and keep everything free and open-source.

**[☕ Buy me a coffee](https://coff.ee/karmaviz)**

Every contribution, no matter how small, is greatly appreciated and directly contributes to:
- 🚀 New node development and features
- 🐛 Bug fixes and performance improvements  
- 📚 Better documentation and tutorials
- 🔧 Ongoing maintenance and support

Thank you for being part of the ComfyUI-KarmaNodes community! 🙏

---

**Note**: This node is designed for advanced users familiar with ComfyUI workflows. Basic knowledge of diffusion model sampling is recommended.