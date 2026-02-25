# ComfyUI-JK-ToRetro

Retro graphics converter node for ComfyUI. Converts modern images to authentic retro computing styles (VGA, EGA, CGA, PC-98) with proper color palettes, dithering, and resolution constraints.

## Examples

<table>
  <tr>
    <td align="center">
      <img src="examples/cga_yliluoma.png" alt="CGA with Yliluoma dithering" width="320"/><br/>
      <b>CGA (4 colors)</b><br/>
      Yliluoma ordered dithering
    </td>
    <td align="center">
      <img src="examples/vga_o2x2.png" alt="VGA with Bayer 2x2 dithering" width="320"/><br/>
      <b>VGA (256 colors)</b><br/>
      Bayer 2x2 ordered dithering
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="examples/ega_stucki.png" alt="EGA with Stucki dithering" width="320"/><br/>
      <b>EGA (16 colors)</b><br/>
      Stucki error diffusion
    </td>
    <td align="center">
      <img src="examples/PC-98_flloyd_steinberg.png" alt="PC-98 with Floyd-Steinberg" width="320"/><br/>
      <b>PC-98 (16 colors)</b><br/>
      Floyd-Steinberg error diffusion
    </td>
  </tr>
</table>

## Features

- **Authentic Retro Formats:**
  - **VGA** (640x480, 256 colors)
  - **EGA** (640x350, 16 colors with authentic palette)
  - **CGA Palette 1** (320x200, 4 colors: Black, Cyan, Magenta, White)
  - **CGA Palette 2** (320x200, 4 colors: Black, Green, Red, Yellow)
  - **PC-98** (640x400, 16 colors)

- **Flexible Aspect Ratio Handling:**
  - Fit (maintain aspect ratio, no padding - default)
  - Pad (letterbox/pillarbox with black bars)
  - Crop (fill frame)
  - Stretch (distort to fit)

- **Integer Upscaling:** Scale output 1-10x with nearest-neighbor filtering for crisp pixelated aesthetic

- **Multiple Dithering Algorithms:**
  - **Error Diffusion:** Floyd-Steinberg, Riemersma, or None
  - **Ordered Dithering:** Yliluoma's algorithm (optimized for limited palettes) and Bayer matrix patterns (2x2, 4x4, 8x8, 16x16)

## Installation

### Requirements

- **ImageMagick** must be installed on your system
  - Windows: Download from https://imagemagick.org/script/download.php#windows
  - Linux: `sudo apt install imagemagick` or equivalent
  - macOS: `brew install imagemagick`

### Via ComfyUI Manager (Recommended)
*(When published)*
1. Open ComfyUI Manager
2. Search for "JK-ToRetro"
3. Click Install

### Manual Installation

1. Navigate to your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/Nakamura2828/ComfyUI-JK-ToRetro.git
   ```

3. Install dependencies:
   ```bash
   cd ComfyUI-JK-ToRetro
   pip install -r requirements.txt
   ```

4. Restart ComfyUI

## Usage

### Image to Retro Node

Located in the **JK-ToRetro** category.

**Inputs:**
- `image_in` (IMAGE): Input image to convert
- `output_type` (dropdown): Target retro format
  - VGA
  - EGA
  - CGA (Cyan/Magenta/White)
  - CGA (Green/Red/Yellow)
  - PC-98
- `aspect_mode` (dropdown): How to handle aspect ratio
  - Fit (default) - Maintain aspect ratio, no padding
  - Pad - Letterbox with black bars
  - Crop - Fill frame by cropping
  - Stretch - Distort to fit
- `dither_method` (dropdown): Dithering algorithm
  - **Error Diffusion:** Floyd-Steinberg (default), Riemersma, None
  - **Ordered Dithering:** Yliluoma (optimized for CGA/EGA), Bayer 2x2, Bayer 4x4, Bayer 8x8, Bayer 16x16
- `scale_multiplier` (INT slider, 1-10): Integer upscaling factor

**Outputs:**
- `image_out` (IMAGE): Converted retro-style image

### Example Workflow

1. Load image (Load Image node)
2. Connect to "Image to Retro" node
3. Select desired retro format (e.g., "CGA (Cyan/Magenta/White)")
4. Choose aspect mode (Fit for content-only, Pad for letterboxing, Crop to fill, or Stretch to distort)
5. Select dithering method (Floyd-Steinberg for smooth gradients, Ordered patterns for retro texture)
6. Set scale multiplier (2x or 3x recommended for visibility)
7. Preview or save output

## Technical Details

### Retro Format Specifications

| Format | Output Resolution | Aspect Ratio | Colors | Notes |
|--------|------------------|--------------|--------|-------|
| VGA | 640x480 | 4:3 | 256 | Standard VGA mode 13h |
| EGA | 640x480 | 4:3 | 16 | Authentic IBM EGA palette |
| CGA (P1) | 320x240 | 4:3 | 4 | Cyan/Magenta/White palette |
| CGA (P2) | 320x240 | 4:3 | 4 | Green/Red/Yellow palette |
| PC-98 | 640x480 | 4:3 | 16 | NEC PC-9800 series |

**Note:** All formats output at 4:3 aspect ratio with square pixels for clean display on modern monitors. The horizontal resolution matches the authentic retro format limits to maintain the characteristic low-resolution aesthetic.

### Color Palettes

**EGA 16-Color Palette:**
Black, Blue, Green, Cyan, Red, Magenta, Brown, Light Gray, Dark Gray, Light Blue, Light Green, Light Cyan, Light Red, Light Magenta, Yellow, White

**CGA Palette 1:**
Black, Cyan, Magenta, White

**CGA Palette 2:**
Black, Green, Red, Yellow

### Image Processing Pipeline

1. Input ComfyUI tensor converted to Wand Image object
2. Content dimensions calculated based on aspect mode (Fit/Pad maintain aspect, Crop/Stretch fill target)
3. Image resized to content dimensions with Lanczos filter for smooth downscaling
4. Color reduction with palette mapping or quantization:
   - **Error diffusion** (Floyd-Steinberg/Riemersma/Jarvis-Judice-Ninke/Stucki/Burkes/Sierra variants/Atkinson/None): Applied via ImageMagick or hitherdither
   - **Ordered dithering** (Yliluoma/Cluster-dot/Bayer): Image converted to PIL, palette extracted (if adaptive), dithering applied via hitherdither, converted back to Wand
5. Black padding added if Pad mode selected (Fit mode outputs content-only)
6. Optional integer upscaling with nearest-neighbor filter
7. Converted back to ComfyUI tensor

This simplified pipeline eliminates moire artifacts while maintaining crisp pixels and the characteristic retro aesthetic through limited horizontal resolution and color palettes.

### Dithering Methods

**Error Diffusion Methods:**
- **Floyd-Steinberg** (default): Smooth gradients with diagonal patterns, best for photorealistic images
- **Riemersma**: Hilbert curve dithering, creates unique serpentine patterns
- **None**: No dithering at all - plain quantization/palette mapping with visible color banding and posterization

**Ordered Dithering:**
- **Yliluoma**: Optimized for limited palettes (CGA/EGA), distributes colors more evenly, creates hand-dithered aesthetic
- **Bayer 2x2**: Smallest dithering pattern, coarse but fast
- **Bayer 4x4**: Medium pattern size, good balance
- **Bayer 8x8**: Fine dithering pattern, smooth gradients
- **Bayer 16x16**: Very fine pattern, smoothest but most subtle

**Implementation Details:**
- **Fixed palettes** (CGA, EGA): Dithering applied with exact palette colors via hitherdither library
- **Adaptive palettes** (VGA, PC-98): Image quantized to extract palette, then dithering applied with extracted colors
- **Yliluoma** uses a sophisticated algorithm designed specifically for small palettes, better color distribution than Bayer for 4-16 color palettes
- **Cluster-dot** creates halftone-style patterns reminiscent of print media
- **Bayer** matrix creates the characteristic retro "checkerboard" or "crosshatch" patterns, uses tuned thresholds [64, 64, 64] for better color balance
- **Error diffusion** methods spread quantization error to neighboring pixels for smooth gradients

## Dependencies

- Python 3.10+
- PyTorch (provided by ComfyUI)
- Wand (Python ImageMagick binding)
- ImageMagick (system library)
- Pillow (PIL)
- NumPy
- hitherdither (for ordered dithering with custom palettes)

See `requirements.txt` for complete list.

## Roadmap

### Current Features (v0.3.1)
- ✓ VGA, EGA, CGA (both palettes), PC-98 support
- ✓ 4:3 aspect ratio output with square pixels
- ✓ Fit/Pad/Crop/Stretch aspect ratio modes (Fit default - content-only, no padding)
- ✓ Optimized processing: padding applied after dithering (saves computation)
- ✓ Integer upscaling (1-10x)
- ✓ Comprehensive dithering algorithms:
  - ✓ Error diffusion: Floyd-Steinberg, Riemersma, Jarvis-Judice-Ninke, Stucki, Burkes, Sierra-3, Sierra-2, Sierra-2-4A, Atkinson, None
  - ✓ Ordered dithering: Yliluoma (optimized for limited palettes), Cluster-dot, Bayer matrix (2x2, 4x4, 8x8, 16x16)

### Future Enhancements
- [ ] Additional retro formats (Commodore 64, Amiga, ZX Spectrum, Apple II, etc.)
- [ ] Custom palette support
- [ ] Scanline effects
- [ ] CRT simulation (phosphor glow, screen curvature, bloom)

## License

MIT License

## Author

John Knox (Nakamura2828)

## Contributing

Issues and pull requests welcome!

## Support

If you find this node useful, please star the repository on GitHub!

## Changelog

### v0.3.1 (2026-01-19)
- **Optimization:** Padding now applied after dithering (not before) to avoid wasting computation on black bars
- **New aspect mode:** Added "Fit" mode (now default) - maintains aspect ratio without padding, outputs content-only
- Aspect modes: Fit (content-only, default), Pad (letterbox), Crop (fill), Stretch (distort)

### v0.3.0 (2026-01-19)
- **Major change:** Simplified to 4:3 output with square pixels, eliminating moire artifacts from PAR correction
- Output resolutions: CGA 320x240, EGA 640x480, VGA 640x480, PC-98 640x480
- Added 7 additional error diffusion methods via hitherdither: Jarvis-Judice-Ninke, Stucki, Burkes, Sierra-3, Sierra-2, Sierra-2-4A, Atkinson
- Added Cluster-dot ordered dithering
- Cleaner output suitable for modern displays while maintaining retro aesthetic through limited resolution and color palettes

### v0.2.2 (2026-01-19)
- Added Yliluoma's ordered dithering algorithm (optimized for limited palettes like CGA/EGA)
- Improved Bayer dithering with tuned thresholds [64, 64, 64] for better color distribution
- Yliluoma creates more even color distribution and hand-dithered aesthetic compared to Bayer

### v0.2.1 (2026-01-19)
- Fixed ordered dithering to work correctly with custom palettes
- Replaced ImageMagick's `ordered_dither` with hitherdither library (Bayer matrix)
- Ordered dithering now properly respects palette colors (CGA, EGA, VGA, PC-98)
- Adaptive palette extraction for VGA/PC-98 ordered dithering
- Simplified dithering options: Bayer 2x2, 4x4, 8x8, 16x16

### v0.2.0 (2026-01-19)
- Added multiple dithering algorithms:
  - Error diffusion methods: Floyd-Steinberg, Riemersma, None
  - Ordered dithering: 19 threshold map patterns (dispersed, halftone, circles)
- User-friendly dithering method names with plain English descriptions

### v0.1.0 (2026-01-19)
- Added automatic pixel aspect ratio correction for authentic 4:3 display
- Images now display with correct proportions as they would on original CRT monitors
- Pre-distortion and post-distortion ensure proper handling of non-square pixels

### v0.0.1 (2026-01-19)
- Initial release
- Support for VGA, EGA, CGA (2 palettes), PC-98
- Pad/Crop/Stretch aspect ratio modes
- Integer upscaling with nearest-neighbor
- Floyd-Steinberg dithering
