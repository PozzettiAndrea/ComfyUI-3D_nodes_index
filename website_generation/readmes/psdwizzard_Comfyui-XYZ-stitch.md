# ComfyUI XYZ Grid

Create A1111-style XYZ plot grids in ComfyUI! Test multiple parameters and compare results in organized, labeled comparison grids.

![License](https://img.shields.io/badge/license-MIT-green)
![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom%20Node-orange)

## Features

- 🎨 **A1111 Style Layout** - Classic Automatic1111 XYZ plot layout with labeled blocks
- 🔄 **Automatic Collection** - Automatically collects images across multiple runs
- 📊 **2D & 3D Grids** - Support for X×Y grids and X×Y×Z combinations
- 🏷️ **Clear Labels** - Large, readable labels for all axes
- 🎯 **Easy to Use** - Simple node-based workflow with automatic management
- 🔢 **Type Conversion** - Built-in string-to-number conversion for parameters

## What is an XYZ Grid?

An XYZ grid lets you test multiple combinations of parameters and see all results in one organized comparison image. Perfect for:

- Testing different prompts with various CFG scales
- Comparing samplers across step counts
- Finding optimal parameter combinations
- A/B testing models or styles
- Parameter sweeps for quality optimization

## Installation

### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "XYZ Grid" or "XYZ Stitch"
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation

1. Navigate to your ComfyUI custom_nodes folder:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/psdwizzard/Comfyui-XYZ-stitch.git
   ```

3. Restart ComfyUI

4. Nodes will appear under the "XYZ Grid" category

## Quick Start

### Basic 2D Grid (X × Y)

1. **Add XYZ Grid Input** node
   - X values: `red car, blue car, green car` (prompts)
   - Y values: `10, 20, 30` (steps)
   - Z values: (leave empty)
   - Index: Start at 0

2. **Add XYZ String to Number** node
   - Connect Grid Input `y_value` → `text`
   - Connect `int_value` → your sampler's steps parameter

3. **Add XYZ Auto Collector** node
   - Connect Grid Input `total_combinations` → Auto Collector `total_combinations`
   - Connect your generated image → Auto Collector `images`

4. **Add XYZ Grid Stitch** node
   - Connect Auto Collector `images` → Stitch `images`
   - Connect Auto Collector `is_complete` → Stitch `is_complete` (IMPORTANT!)
   - Set X labels: `red car, blue car, green car`
   - Set Y labels: `10, 20, 30`
   - Choose layout style: `A1111 Style (X blocks)`

5. **Generate all combinations:**
   - Queue with index 0, then 1, then 2, ... up to 8
   - On the last run, your grid automatically appears!

**Result:** One 3×3 grid showing all combinations of prompts and steps

### 3D Grid (X × Y × Z) - A1111 Style

Perfect for testing 3 parameters at once!

1. **Configure axes:**
   - X values: `red, blue` (prompts)
   - Y values: `10, 20` (steps)
   - Z values: `5.0, 7.0` (CFG scale)

2. **Connect parameters:**
   - X → prompts
   - Y → String to Number (INT) → steps
   - Z → String to Number (FLOAT) → CFG

3. **Run 8 times** (2×2×2 combinations)

**Result:** Two blocks (one for red, one for blue), each showing a 2×2 grid of steps vs CFG!

## Nodes Overview

### XYZ Grid Input
Generates parameter combinations one at a time. Increment the index for each run to get the next combination.

**Inputs:**
- `x_values`: Comma-separated values (e.g., "red, blue, green")
- `y_values`: Comma-separated values (e.g., "10, 20, 30")
- `z_values`: Comma-separated values (optional, leave empty for 2D)
- `index`: Current combination index (0 to total-1)

**Outputs:**
- `x_value`, `y_value`, `z_value`: Current values as strings
- `total_combinations`: Total number of combinations
- Indices for grid positioning

### XYZ String to Number
Converts string values to integers or floats for numeric parameters.

**Use for:** Steps, CFG scale, denoise strength, etc.

### XYZ Auto Collector
Automatically collects images across multiple runs and outputs them all when complete.

**Key feature:** No manual mode switching! Detects when all images are collected and automatically outputs to the grid.

**Inputs:**
- `images`: Generated images
- `total_combinations`: Connect from Grid Input
- `collection_id`: Unique ID for this collection

**Outputs:**
- `images`: Collected images (all at once when complete)
- `is_complete`: Boolean indicating completion

### XYZ Grid Stitch
Creates the final labeled comparison grid.

**Layout Styles:**
- **A1111 Style (X blocks)**: Each X value gets its own block with Y×Z grid inside
- **Z Horizontal**: Z values create separate grids side-by-side

**Inputs:**
- `images`: All generated images
- `is_complete`: Must connect from Auto Collector!
- Labels for X, Y, Z axes
- `label_height`: Space for top labels (default: 120px)
- `label_width`: Space for left labels (default: 150px)
- `layout_style`: Choose your preferred layout

## Example Workflows

### Prompt Testing
Test different prompts with various CFG scales:
```
X: "realistic photo", "oil painting", "anime style"
Y: 6.0, 7.5, 9.0  (CFG)
Z: (empty)
= 3×3 grid
```

### Parameter Optimization
Find optimal steps and CFG:
```
X: 15, 20, 25, 30  (steps)
Y: 6.0, 7.0, 8.0, 9.0, 10.0  (CFG)
Z: (empty)
= 4×5 grid (20 combinations)
```

### Sampler Comparison
Compare samplers at different step counts:
```
X: "euler", "dpm++", "ddim"
Y: 10, 20, 30  (steps)
Z: 7.0, 9.0  (CFG)
= 3 blocks, each with 3×2 grid
```

## Documentation

Detailed guides are included in the package:

- **[EASY_GUIDE.md](EASY_GUIDE.md)** - Simple step-by-step tutorial
- **[A1111_STYLE_GUIDE.md](A1111_STYLE_GUIDE.md)** - A1111 layout explained
- **[AXIS_GUIDE.md](AXIS_GUIDE.md)** - Understanding X, Y, Z axes
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Quick reference with diagrams

## Tips & Tricks

### 1. The is_complete Connection is Critical!
Always connect Auto Collector's `is_complete` output to Stitch's `is_complete` input. This prevents the grid from being created on every run.

### 2. Start Small
Begin with 2×2 or 3×3 grids to test your workflow before running large parameter sweeps.

### 3. Use Descriptive Labels
Your labels appear on the grid, so make them clear and concise.

### 4. String vs Number Parameters
- Text/prompts → Connect x_value directly
- Numbers (steps, CFG) → Use String to Number node first

### 5. Organizing Complex Grids
For 3+ parameters, use A1111 style with:
- X = What you want to compare (prompts, models)
- Y = First numeric parameter (steps, denoise)
- Z = Second numeric parameter (CFG, strength)

### 6. Collection ID
Use different `collection_id` values to run multiple grids simultaneously without mixing them up.

### 7. Adjust Label Sizes
If labels are cut off or too small:
- Increase `label_height` for top labels
- Increase `label_width` for side labels
- Increase `gap_size` for more spacing

## Troubleshooting

### "Skipping - waiting for all images to be collected"
✅ This is normal during collection! The grid only creates on the final run.

### Getting the same image 9 times
❌ You're not changing the index! Manually increment from 0 to 8.

### Images are different sizes in the grid
❌ Ensure your workflow outputs consistent image dimensions.

### Labels are cut off
❌ Increase `label_width` or `label_height` in the Stitch node.

### Save Image node saves tiny images between runs
❌ Make sure you connected `is_complete` from Auto Collector to Stitch!

### "Collected 10/9 images"
❌ You ran too many times. Set Auto Collector's `reset` to True and start over.

## Advanced Features

### Manual Collection (Advanced Users)
For fine control, use **XYZ Image Collector (Manual)** with mode switching.

### Batch Processing
Use **XYZ Grid Input (Batch)** for workflows that support list/batch processing.

### Iterator
Use **XYZ Grid Iterator** for advanced automatic index tracking (limited use cases).

## Requirements

- ComfyUI (any recent version)
- No additional dependencies (uses standard Python libraries)

## Comparison to A1111

| Feature | A1111 XYZ Plot | ComfyUI XYZ Grid |
|---------|---------------|------------------|
| Layout | Automatic grid | A1111 style + more |
| Execution | Fully automatic | Manual queuing (more control) |
| Integration | Built-in | Custom node |
| Flexibility | Fixed workflow | Full node workflow |
| 3D Grids | Side-by-side | Multiple layouts |

## Contributing

Found a bug? Have a feature request?

1. Check existing issues
2. Open a new issue with details
3. Pull requests welcome!

## License

MIT License - See [LICENSE](LICENSE) file for details

## Credits

Created by [@psdwizzard](https://github.com/psdwizzard)

Inspired by Automatic1111's XYZ Plot functionality.

## Support

- 🐛 **Issues:** [GitHub Issues](https://github.com/psdwizzard/Comfyui-XYZ-stitch/issues)
- 💬 **Discussions:** [GitHub Discussions](https://github.com/psdwizzard/Comfyui-XYZ-stitch/discussions)

## Changelog

### v1.0.0 (Initial Release)
- XYZ Grid Input with manual index control
- XYZ Auto Collector for automatic image collection
- XYZ Grid Stitch with two layout styles
- String to Number converter
- A1111-style grid layout
- Comprehensive documentation

---

**Enjoy creating your XYZ grids!** 🎨📊

If you find this useful, consider starring the repo ⭐
