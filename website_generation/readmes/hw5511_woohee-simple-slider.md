# Woohee Simple Slider

A simple ComfyUI custom node that provides a slider with **-1 to 1 range** support. Unlike the original SimpleMathSlider which only supports 0 to 1, this slider allows negative values.

## Features

- **Negative Value Support**: Default range from -1.0 to 1.0
- **Customizable Range**: Adjust min and max values to any range
- **Rounding Control**: Specify decimal precision (0-10 decimal places)
- **Dual Output**: Returns both FLOAT and INT values
- **Slider UI**: Clean slider interface for easy value adjustment

## Why This Node?

The original ComfyUI Essentials' SimpleMathSlider has a limitation - the slider UI component only works with values from 0 to 1. This makes it impossible to directly use negative values with the slider.

**Woohee Simple Slider** solves this by:
1. Using a -1 to 1 slider range by default
2. Mapping the slider value to your custom min/max range
3. Supporting full negative value ranges

## Installation

### Via ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "Woohee Simple Slider"
3. Click Install

### Manual Installation

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/hw5511/woohee-simple-slider.git
# No additional dependencies needed - restart ComfyUI
```

## Usage

### Basic Usage

1. Add the node: Search "Woohee Simple Slider" in ComfyUI
2. Adjust the slider: Drag the slider or enter a value (-1.0 to 1.0)
3. Connect outputs: Use FLOAT or INT output as needed

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| **value** | FLOAT (slider) | 0.0 | Main slider value (-1.0 to 1.0) |
| **min** | FLOAT | -1.0 | Minimum output value |
| **max** | FLOAT | 1.0 | Maximum output value |
| **rounding** | INT | 0 | Decimal places (0 = no rounding) |

### Outputs

- **FLOAT**: Calculated float value
- **INT**: Integer version of the value

## Examples

### Example 1: Basic -1 to 1 Slider
```
value: 0.5 (slider)
min: -1.0
max: 1.0
rounding: 2

Output FLOAT: 0.0
Output INT: 0
```

### Example 2: Custom Range (0 to 100)
```
value: 0.75 (slider)
min: 0.0
max: 100.0
rounding: 0

Output FLOAT: 87.5
Output INT: 87
```

### Example 3: Negative Range (-50 to -10)
```
value: -0.5 (slider)
min: -50.0
max: -10.0
rounding: 1

Output FLOAT: -30.0
Output INT: -30
```

### Example 4: High Precision
```
value: 0.333 (slider)
min: 0.0
max: 1.0
rounding: 5

Output FLOAT: 0.66650
Output INT: 0
```

## How It Works

The node uses a simple linear interpolation formula:

```
output = min + slider_value * (max - min)
```

This allows the slider (which ranges from -1 to 1) to be mapped to any custom range you specify.

## Comparison with SimpleMathSlider

| Feature | SimpleMathSlider | Woohee Simple Slider |
|---------|------------------|---------------------|
| Slider Range | 0.0 to 1.0 | -1.0 to 1.0 |
| Negative Values | Limited | Full support |
| Custom Range | Yes | Yes |
| Rounding | Yes | Yes |
| Dependencies | ComfyUI Essentials | None |

## Technical Details

- **Python Version**: 3.9+
- **Dependencies**: None (uses only ComfyUI built-in functionality)
- **Category**: woohee/utilities
- **License**: MIT

## Credits

Inspired by [ComfyUI Essentials](https://github.com/cubiq/ComfyUI_essentials) SimpleMathSlider node.

## Support

- **Issues**: [GitHub Issues](https://github.com/hw5511/woohee-simple-slider/issues)
- **Repository**: [GitHub](https://github.com/hw5511/woohee-simple-slider)

## License

MIT License - see LICENSE file for details.
