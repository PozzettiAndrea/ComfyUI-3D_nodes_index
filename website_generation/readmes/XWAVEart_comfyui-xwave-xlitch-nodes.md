# ComfyUI XWAVE Nodes

A collection of artistic glitch and image manipulation nodes for ComfyUI, featuring advanced noise effects, color manipulations, distortions, and more.

## Installation

### Method 1: ComfyUI Manager (Recommended)
1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
2. Search for "XWAVE" in the manager
3. Install "ComfyUI XWAVE Nodes"
4. Restart ComfyUI

### Method 2: Manual Installation
1. Navigate to your ComfyUI's `custom_nodes` directory:
```bash
cd /path/to/ComfyUI/custom_nodes
```

2. Clone this repository:
```bash
git clone https://github.com/XWAVEart/comfyui-xwave-xlitch-nodes
```

3. Install dependencies:
```bash
cd comfyui-xwave-xlitch-nodes
pip install -r requirements.txt
```

4. Restart ComfyUI

### Method 3: Direct Copy
1. Download this repository as a ZIP file
2. Extract the `comfyui-xwave-xlitch-nodes` folder into your `ComfyUI/custom_nodes` directory
3. Install dependencies:
```bash
cd ComfyUI/custom_nodes/comfyui-xwave-xlitch-nodes
pip install -r requirements.txt
```
4. Restart ComfyUI

## Available Nodes

All nodes can be found under the "XWAVE" category in the node menu.

### 🎨 Color Effects

#### XWAVE Noise Effect
Adds various types of noise to images with extensive customization options.

**Features:**
- 5 noise types: Film Grain, Digital, Colored, Salt & Pepper, Gaussian
- 4 blend modes: Overlay, Add, Multiply, Screen
- 3 patterns: Random, Perlin, Cellular
- Customizable grain size and color variation
- Seed control for reproducible results

**Inputs:**
- `image`: Input image
- `noise_type`: Type of noise effect
- `intensity`: Overall noise strength (0.0-1.0)
- `grain_size`: Size of noise particles (0.5-5.0)
- `color_variation`: Amount of color variation (0.0-1.0)
- `blend_mode`: How to blend noise with the image
- `pattern`: Noise generation pattern
- `noise_color`: Base color for colored noise (hex format)
- `seed`: Random seed (0 for random, 1-4294967295 for specific seed)

#### XWAVE Color Channel Manipulation
Manipulate color channels through swapping, inverting, adjusting, or creating negatives.

**Features:**
- 4 operations: Swap, Invert, Adjust, Negative
- Channel control: Red, Green, Blue, or combinations
- Intensity adjustment for fine control
- Simple yet powerful color effects

**Inputs:**
- `image`: Input image
- `operation`: Type of manipulation (swap, invert, adjust, negative)
- `intensity`: Adjustment factor for operations (0.0-2.0)
- `channels`: Channels to manipulate (e.g., "R", "G", "B", "RG", "RB", "GB")
- `seed`: Random seed (-1 for random, currently unused)

#### XWAVE RGB Channel Shift
Creates chromatic aberration effects by shifting or mirroring RGB channels independently.

**Features:**
- 2 modes: Shift channels spatially or mirror them
- Control which channel stays centered
- Adjustable shift amount
- Horizontal or vertical shifting
- Perfect for glitch aesthetics and retro effects

**Inputs:**
- `image`: Input image
- `mode`: Operation mode (shift or mirror)
- `shift_amount`: Number of pixels to shift (1-100, ignored in mirror mode)
- `direction`: Shift direction (horizontal or vertical)
- `centered_channel`: Which channel remains unchanged (R, G, or B)

#### XWAVE Histogram Glitch
Apply different mathematical transformations to each color channel independently.

**Features:**
- 4 transformation modes per channel: Solarize, Log, Gamma, Normal
- Independent control for R, G, B channels
- Solarization with frequency and phase control
- Gamma correction with adjustable power
- Logarithmic compression for dynamic range control

**Inputs:**
- `image`: Input image
- `r_mode`, `g_mode`, `b_mode`: Transformation mode for each channel
- `r_freq`, `g_freq`, `b_freq`: Solarization frequency (0.1-10.0)
- `r_phase`, `g_phase`, `b_phase`: Solarization phase (0.0-6.28)
- `gamma_val`: Gamma value for gamma transformation (0.1-3.0)

#### XWAVE Color Shift Expansion

Apply color shift expansion effects with customizable patterns and themes. This node expands colored shapes from various points in the image, creating unique and artistic color effects.

### Features
- Multiple expansion types (square, circle, diamond)
- Customizable color themes (full-spectrum, warm, cool, pastel)
- Various pattern types for point placement (random, grid, edges)
- Saturation and value boosting
- Distance-based color influence with decay control
- Reproducible results with seed control

### Inputs
- `image`: Input image to process
- `num_points`: Number of expansion points (1-50)
- `shift_amount`: Amount of color shifting (1-20)
- `expansion_type`: Shape of expansion ('square', 'circle', 'diamond')
- `mode`: Mode of color application ('xtreme', 'subtle', 'mono')
- `saturation_boost`: Amount to boost saturation (0.0-1.0)
- `value_boost`: Amount to boost brightness (0.0-1.0)
- `pattern_type`: Pattern of color point placement ('random', 'grid', 'edges')
- `color_theme`: Color theme to use ('full-spectrum', 'warm', 'cool', 'pastel')
- `decay_factor`: How quickly effect fades with distance (0.0-1.0)
- `seed`: Seed for random number generation

### Tips
- Use 'grid' pattern type for more structured effects
- Try 'edges' pattern type for frame-like effects
- Adjust decay_factor to control how quickly colors blend
- Use different color themes for different moods
- Higher shift_amount values create more dramatic effects
- Combine with other color nodes for unique results

#### XWAVE Posterize
Reduce the number of colors in an image with optional dithering.

**Features:**
- Adjustable color levels (2-256)
- Multiple dithering methods
- Support for different color spaces
- Creates retro and artistic effects

**Inputs:**
- `image`: Input image
- `levels`: Number of color levels per channel (2-256)
- `dither`: Dithering method:
  - `none`: No dithering
  - `floyd-steinberg`: Classic error diffusion
  - `atkinson`: Sharp, high-contrast dithering
  - `ordered`: Bayer pattern dithering
- `color_space`: Color space for posterization:
  - `rgb`: Standard RGB color space
  - `hsv`: Hue-Saturation-Value space
  - `lab`: Perceptually uniform LAB space

**Tips:**
- **Levels**: Lower values create more dramatic effects
  - 2-4: Extreme posterization
  - 8-16: Classic retro look
  - 32-64: Subtle color reduction
- **Dithering**:
  - `floyd-steinberg`: Best for smooth gradients
  - `atkinson`: Good for high contrast images
  - `ordered`: Creates regular patterns
- **Color Spaces**:
  - `rgb`: Standard color reduction
  - `hsv`: Better for artistic effects
  - `lab`: More perceptually accurate

#### XWAVE Curved Hue Shift
Apply non-linear hue transformations to images using various curve types.

**Features:**
- 4 curve types: Sine, Cosine, Tangent, Exponential
- Adjustable intensity and frequency
- Phase control for precise timing
- Option to preserve original luminance
- Creates unique color effects

**Inputs:**
- `image`: Input image
- `curve_type`: Type of curve to use:
  - `sine`: Smooth, wave-like hue shifts
  - `cosine`: Similar to sine but phase-shifted
  - `tangent`: Sharp, dramatic hue changes
  - `exponential`: Progressive hue transformations
- `intensity`: Strength of the hue shift (0.0-1.0)
- `frequency`: Frequency of the curve (0.1-10.0)
- `phase`: Phase offset of the curve (0.0-6.28)
- `preserve_luminance`: Whether to maintain original brightness

**Tips:**
- **Curve Types**:
  - `sine`: Best for smooth, natural-looking shifts
  - `cosine`: Good for complementary color effects
  - `tangent`: Creates dramatic, high-contrast changes
  - `exponential`: Useful for progressive color transformations
- **Intensity**:
  - Low (0.1-0.3): Subtle color variations
  - Medium (0.4-0.6): Noticeable hue shifts
  - High (0.7-1.0): Dramatic color changes
- **Frequency**:
  - Low (0.1-1.0): Gradual color transitions
  - Medium (1.0-3.0): Balanced color shifts
  - High (3.0-10.0): Rapid color variations
- **Phase**:
  - Adjust to fine-tune the timing of color changes
  - Full rotation (0-6.28) shifts the entire color cycle
- **Preserve Luminance**:
  - `true`: Maintains original brightness while changing colors
  - `false`: Allows brightness to vary with color changes

#### XWAVE Color Filter
Apply color filters with various blend modes and filter types.

**Features:**
- 3 filter types: Solid color, gradient, and custom gradient image
- 12 blend modes for creative effects
- Adjustable opacity
- Support for custom gradient images
- Horizontal and vertical gradient directions

**Inputs:**
- `image`: Input image
- `filter_type`: Type of filter to apply:
  - `solid`: Single color filter
  - `gradient`: Two-color gradient filter
  - `custom`: Custom gradient image filter
- `color`: Start color for solid filter or gradient (hex format)
- `end_color`: End color for gradient (hex format)
- `gradient_direction`: Direction of gradient:
  - `horizontal`: Left to right
  - `vertical`: Top to bottom
- `custom_gradient`: Custom gradient image (for 'custom' filter type)
- `blend_mode`: How to blend the filter with the image:
  - `normal`: Standard overlay
  - `multiply`: Darkens the image
  - `screen`: Lightens the image
  - `overlay`: Combines multiply and screen
  - `soft_light`: Subtle light/dark effect
  - `hard_light`: Strong light/dark effect
  - `color_dodge`: Brightens the image
  - `color_burn`: Darkens the image
  - `linear_dodge`: Adds colors
  - `linear_burn`: Subtracts colors
  - `vivid_light`: Combines color dodge and burn
- `opacity`: Filter strength (0.0-1.0)

**Tips:**
- **Filter Types**:
  - `solid`: Best for color grading and tinting
  - `gradient`: Great for creative color transitions
  - `custom`: Use your own gradient images for unique effects
- **Blend Modes**:
  - `multiply`/`screen`: Classic darken/lighten effects
  - `overlay`/`soft_light`: Subtle color adjustments
  - `color_dodge`/`burn`: Dramatic color effects
  - `vivid_light`: High-contrast color manipulation
- **Opacity**:
  - Lower values (0.1-0.3): Subtle color adjustments
  - Medium values (0.4-0.7): Noticeable color effects
  - Higher values (0.8-1.0): Strong color transformations
- **Custom Gradients**:
  - Use smooth gradients for best results
  - Gradient will be automatically resized to match input image
  - Supports any RGB image as a gradient source

### 🎭 Pixelation Effects

#### XWAVE Pixelate
Applies traditional pixelation with attribute-based color selection.

**Features:**
- Customizable pixel block dimensions
- Multiple attribute modes for pixel selection
- Preserves important visual characteristics based on chosen attribute

**Inputs:**
- `image`: Input image
- `pixel_width`: Width of each pixelated block (1-256)
- `pixel_height`: Height of each pixelated block (1-256)
- `attribute`: Attribute to use for pixel grouping:
  - `color`: Most common color in each block
  - `brightness`: Average brightness-based selection
  - `hue`: Hue-based pixel selection
  - `saturation`: Saturation-based selection
  - `luminance`: Luminance-based selection

## Usage Example

1. Add an image loader node
2. Find "XWAVE Noise Effect" under "XWAVE/Color" category
3. Connect image output to noise effect input
4. Adjust parameters to taste
5. Connect to preview or save node

## Workflow Examples

Example workflows can be found in the `examples/` directory.

## Tips for Best Results

### Noise Effect Tips:
- **Film Grain**: Use low intensity (0.1-0.3) for realistic film look
- **Digital Noise**: Works well with higher intensities
- **Pattern Selection**:
  - `random`: Classic noise
  - `perlin`: Organic, cloud-like patterns
  - `cellular`: Unique structured patterns
- **Blend Modes**:
  - `overlay`: Preserves image details
  - `add`: Brightens the image
  - `multiply`: Creates texture effects
  - `screen`: Lighter, ethereal effect

### Color Channel Manipulation Tips:
- **Swap**: Create interesting color shifts by swapping channels
  - `RG`: Swap red and green for surreal landscapes
  - `RB`: Swap red and blue for dramatic effects
  - `GB`: Swap green and blue for unique tones
- **Invert**: Invert individual channels for artistic effects
  - Inverting single channels creates unique color palettes
- **Adjust**: Fine-tune channel intensity
  - Values < 1.0 reduce channel intensity
  - Values > 1.0 boost channel intensity
- **Negative**: Creates a full color negative effect

### RGB Channel Shift Tips:
- **Shift Mode**: Creates chromatic aberration effects
  - Small shifts (5-15): Subtle color fringing
  - Medium shifts (20-40): Noticeable channel separation
  - Large shifts (50+): Extreme glitch effects
- **Mirror Mode**: Creates symmetrical channel effects
  - Each non-centered channel is mirrored differently
  - Creates unique artistic distortions
- **Centered Channel**: Choose which color dominates
  - `R`: Red stays centered, green/blue shift
  - `G`: Green stays centered, red/blue shift  
  - `B`: Blue stays centered, red/green shift
- **Direction**: Changes the axis of the effect
  - `horizontal`: Left/right shifts or mirroring
  - `vertical`: Up/down shifts or mirroring

### Histogram Glitch Tips:
- **Solarize**: Creates wave-like transformations
  - Low frequency (0.1-2.0): Smooth transitions
  - High frequency (5.0-10.0): Rapid inversions
  - Phase shifts the wave pattern
- **Log Transform**: Compresses bright areas
  - Useful for high dynamic range images
  - Creates film-like tonal curves
- **Gamma Transform**: Power-based adjustments
  - < 1.0: Brightens mid-tones
  - > 1.0: Darkens mid-tones
  - 1.0: No change
- **Mix and Match**: Try different modes on each channel
  - Solarize red, log green, gamma blue for unique effects
  - Use normal mode to keep a channel unchanged

## Coming Soon

- **Color Manipulation**: Channel swapping, histogram effects, color filters
- **Pixel Sorting**: Advanced sorting algorithms with multiple modes
- **Distortion Effects**: Wave, ripple, and displacement effects
- **Glitch Effects**: Databending, bit manipulation, corruption effects
- **Pattern Generation**: Voronoi, concentric shapes, masked merges
- **And many more!**

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- ComfyUI community for the amazing platform
- Inspired by classic glitch art techniques and modern digital art

## Support

For questions, issues, or feature requests:
- Open an issue on [GitHub](https://github.com/XWAVEart/comfyui-xwave-xlitch-nodes)

## XWAVE Chromatic Aberration

Apply advanced chromatic aberration effects to your images with precise control over color channel separation and patterns.

**Features:**
- Four aberration patterns: Radial, Linear, Barrel, and Custom
- Independent control of red and blue channel displacement
- Adjustable center point and falloff types
- Edge enhancement and color boosting options
- Random seed for pattern variations

**Inputs:**
- `image`: Input image to process
- `intensity`: Overall aberration intensity (0.0-50.0)
- `pattern`: Aberration pattern type (radial, linear, barrel, custom)
- `red_shift_x`: Red channel X displacement (-20.0 to 20.0)
- `red_shift_y`: Red channel Y displacement (-20.0 to 20.0)
- `blue_shift_x`: Blue channel X displacement (-20.0 to 20.0)
- `blue_shift_y`: Blue channel Y displacement (-20.0 to 20.0)
- `center_x`: Aberration center X position (0.0-1.0)
- `center_y`: Aberration center Y position (0.0-1.0)
- `falloff`: Distance falloff type (linear, quadratic, cubic)
- `edge_enhancement`: Edge contrast enhancement (0.0-1.0)
- `color_boost`: Color saturation boost (0.5-2.0)
- `seed`: Random seed for pattern variations

**Tips:**
- Use radial pattern for realistic lens-like effects
- Linear pattern works well for directional color separation
- Barrel pattern creates a curved distortion effect
- Custom pattern allows manual control of channel displacement
- Adjust falloff type to control how the effect diminishes with distance
- Use edge enhancement to make the effect more pronounced
- Color boost can help maintain vibrancy when using strong effects

---

Made with ❤️ by XWAVE 