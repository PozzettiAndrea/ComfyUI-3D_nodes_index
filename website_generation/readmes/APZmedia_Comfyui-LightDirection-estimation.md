# NormalMapLightEstimator

A ComfyUI custom node for estimating light direction and quality from normal maps using luma masking. The system analyzes surface normals to infer lighting information for downstream tasks like adaptive relighting, directional masking, or stylized effects.

## Features

- **Categorical Directional Outputs**: X direction (left/central/right), Y direction (top/central/bottom)
- **Hard/Soft Classification**: Continuous index from 0.0 (hard) to 1.0 (soft)
- **Curves Strategy**: Advanced luma processing with multiple curve types
- **User-Controllable Thresholds**: Fine-tune detection sensitivity
- **Debug Visualization**: Visual feedback for analysis results
- **Confidence Scoring**: Reliability indicators for all outputs

## Installation

1. Copy this folder to your ComfyUI `custom_nodes` directory:
   ```
   ComfyUI/custom_nodes/NormalMapLightEstimator/
   ```

2. Restart ComfyUI

3. Dependencies will install automatically. If installation fails, see troubleshooting.

## Usage

### Basic Setup

1. Connect a normal map to the `normal_map` input
2. Connect a luma/lighting image to the `luma_image` input
3. Adjust the `luma_threshold` to control which areas are considered lit
4. Run the workflow to get directional and quality outputs

### Inputs

| Name | Type | Description | Default |
|------|------|-------------|---------|
| `normal_map` | IMAGE | RGB normal map in tangent space (0–255) | - |
| `luma_image` | IMAGE | Grayscale or RGB image to extract luminance | - |
| `luma_threshold` | FLOAT | Threshold to mask out non-lit areas | 0.5 |
| `curve_type` | COMBO | Luma processing curve | s_curve |
| `x_threshold` | FLOAT | Sensitivity for left/right detection | 0.1 |
| `y_threshold` | FLOAT | Sensitivity for top/bottom detection | 0.1 |
| `central_threshold` | FLOAT | Threshold for central lighting detection | 0.3 |
| `hard_light_threshold` | FLOAT | Below this = hard light | 0.15 |
| `soft_light_threshold` | FLOAT | Above this = soft light | 0.35 |
| `use_weighted` | BOOLEAN | Use weighted averaging | False |
| `custom_curve_points` | STRING | Custom curve points (optional) | - |

### Outputs

| Name | Type | Description |
|------|------|-------------|
| `x_direction` | STRING | "left", "central", "right" |
| `y_direction` | STRING | "top", "central", "bottom" |
| `combined_direction` | STRING | "top-left", "top-central", etc. |
| `hard_soft_index` | FLOAT | 0.0 (hard) to 1.0 (soft) |
| `x_confidence` | FLOAT | Confidence in X direction classification |
| `y_confidence` | FLOAT | Confidence in Y direction classification |
| `overall_confidence` | FLOAT | Combined confidence score |
| `spread_value` | FLOAT | Raw numerical spread value |
| `debug_mask` | IMAGE | Binary mask showing which normals were used |
| `directional_viz` | IMAGE | Color-coded visualization of results |

## Algorithm

### Core Concept
The system analyzes surface normals to infer lighting information:
1. **Normal Map (RGB)** → Surface orientation (XYZ)
2. **Luma Mask** → Which areas are actually lit
3. **Filtered Normals** → Only consider lit surface orientations
4. **Statistical Analysis** → Infer light direction and quality

### Key Insight
Lit surface normals point **TOWARD** the light source. By averaging these directions, we get the light direction.

### Processing Pipeline
1. **Normal Processing**: Convert RGB to XYZ, apply axis inversions
2. **Luma Masking**: Extract luminance, apply threshold with curves
3. **Directional Analysis**: Quadrant-based normal distribution analysis
4. **Quality Classification**: Spread analysis for hard/soft determination

## Curve Types

### Linear
Simple threshold-like behavior for basic masking.

### S-curve
Enhance mid-tones, compress highlights/shadows. Good for balanced lighting.

### Exponential
Emphasize bright areas. Useful for high-contrast scenes.

### Logarithmic
Compress highlights, expand shadows. Good for low-light scenarios.

### Custom
User-defined curve points for advanced control.

## Threshold Controls

### Directional Thresholds
- **X Threshold**: Controls left/right detection sensitivity
- **Y Threshold**: Controls top/bottom detection sensitivity
- **Central Threshold**: Detects central lighting patterns

### Quality Thresholds
- **Hard Light Threshold**: Below this = hard light (index 0.0)
- **Soft Light Threshold**: Above this = soft light (index 1.0)
- **Between**: Linear interpolation from 0.0 to 1.0

## Usage Examples

### Basic Directional Detection
```
X Threshold: 0.1 (sensitive to left/right)
Y Threshold: 0.1 (sensitive to top/bottom)
Central Threshold: 0.3 (detect central lighting)
```

### Hard Light Detection
```
Hard Threshold: 0.1 (very sensitive)
Soft Threshold: 0.2 (narrow range)
Result: Index 0.0-0.5 range
```

### Soft Light Detection
```
Hard Threshold: 0.2 (less sensitive)
Soft Threshold: 0.5 (wider range)
Result: Index 0.5-1.0 range
```

## Visualization System

### Debug Mask
- **White pixels**: Lit areas used in analysis
- **Black pixels**: Masked out areas

### Directional Visualization
- **Red Channel**: X direction (left=255, central=192, right=128)
- **Green Channel**: Y direction (top=255, central=192, bottom=128)
- **Blue Channel**: Hard/soft index (hard=255, soft=128)
- **Confidence**: Applied as transparency effect

## Troubleshooting

### Common Issues

**"No light direction detected"**
- Check if luma threshold is too high
- Verify normal map has proper lighting information
- Try adjusting directional thresholds

**"Incorrect direction classification"**
- Try inverting X or Y axes for different normal conventions
- Adjust central threshold for omnidirectional lighting
- Check confidence scores for reliability

**"Poor quality classification"**
- Adjust hard/soft thresholds based on your use case
- Try different curve types for luma processing
- Use weighted averaging for more accurate results

### Manual Installation

If auto-installation fails:

```bash
cd ComfyUI/custom_nodes/NormalMapLightEstimator/
pip install -r requirements.txt
```

## Technical Details

### Dependencies
- torch>=1.9.0
- numpy>=1.21.0
- Pillow>=8.0.0
- scipy>=1.7.0

### Performance
- Optimized for ComfyUI tensor operations
- Batch processing support
- Memory-efficient covariance calculations
- GPU acceleration where possible

### Edge Cases Handled
- No lit areas: Returns default central direction
- Single normal: Uses that direction
- Collinear normals: Handles degenerate cases gracefully
- Low confidence: Provides reliability indicators

## License

MIT License - see LICENSE for details.

## Changelog

### v1.0.0
- Initial release with categorical directional outputs
- Hard/soft classification with continuous index
- Curves strategy for luma processing
- User-controllable thresholds
- Debug visualization system
- Confidence scoring system

---

For support, open an issue on GitHub.
