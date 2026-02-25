# ComfyUI Random Number Generator

A simple and efficient custom node for ComfyUI that generates random numbers between two user-selectable values. Perfect for seed variation, parameter randomization, and workflow experimentation.

## Features

- 🎲 Generate random integers and floats simultaneously
- 🔄 Seed control for reproducible results
- 📊 User-selectable min/max range with decimal support
- ⚡ Lightweight - uses only Python standard library
- 🎯 Appears in Logic/Math category for easy access

## Installation

### Via ComfyUI Manager (Recommended)

1. Open ComfyUI Manager in your ComfyUI interface
2. Search for "Random Number"
3. Click Install
4. Restart ComfyUI

### Manual Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/warfy5/ComfyUI-RandomNumbers.git
   ```

3. Restart ComfyUI

## Usage

### Finding the Node

- **Method 1**: Double-click on the canvas and search for "Random Number"
- **Method 2**: Right-click → **Logic** → **Math** → **Random Number**

### Node Inputs

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| `min_value` | FLOAT | 0.0 | Minimum value (inclusive) |
| `max_value` | FLOAT | 999999.0 | Maximum value (inclusive) |
| `seed` | INT | 0 | Random seed for reproducibility |

### Node Outputs

| Output | Type | Description |
|--------|------|-------------|
| `int` | INT | Integer random value |
| `float` | FLOAT | Float random value |

### Example Use Cases

**1. Random Seed Generation**
- Set min=0, max=9999999
- Use the `int` output to feed into KSampler seed inputs
- Change the node's seed parameter to get different random seeds

**2. Parameter Variation**
- Set min=0.5, max=1.5 for denoise strength variation
- Set min=5.0, max=15.0 for CFG scale randomization
- Use the `float` output for continuous parameters

**3. Reproducible Randomness**
- Set a specific seed value (e.g., 42)
- Same seed always produces the same random number
- Perfect for reproducible workflows and testing

## How It Works

The node uses Python's built-in `random` module with seed control:

1. If `min_value > max_value`, they are automatically swapped
2. The seed is set for reproducible randomization
3. A float value is generated using `random.uniform()`
4. An integer value is created by converting the float
5. Both values are output simultaneously

## Requirements

- ComfyUI
- Python 3.8 or higher
- No additional dependencies required


## Troubleshooting

**Node doesn't appear in menu:**
1. Check that the folder is in `ComfyUI/custom_nodes/`
2. Verify the folder name is `ComfyUI-RandomNumber`
3. Restart ComfyUI completely
4. Check console for any Python errors

**Getting the same number every time:**
- This is expected behavior when using the same seed
- Change the `seed` parameter to get different results
- The seed parameter is what makes results reproducible

## Version History

### v1.0.0 (2025-01-XX)
- Initial release
- Basic random number generation with int/float outputs
- Seed control for reproducibility
- Min/max range selection

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

Do whatever you want with it licence. Thanks for checking though. 

## Credits

Created for the ComfyUI community.

## Support

If you encounter any issues or have suggestions:
- Open an issue on [GitHub](https://github.com/warfy5/ComfyUI-RandomNumbers/issues)
- Check existing issues for solutions

---
