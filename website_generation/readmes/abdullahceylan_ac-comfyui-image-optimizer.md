# AC Image Optimizer - ComfyUI Custom Node

A powerful ComfyUI custom node for optimizing and compressing images with support for multiple formats (JPEG, WebP, PNG) and configurable quality settings.

## Features

- ✅ **Multiple Formats**: JPEG, WebP, PNG support
- ✅ **Quality Control**: Adjustable quality from 1-100
- ✅ **Real-time Statistics**: View compression ratios and file sizes
- ✅ **Advanced Mode**: Format comparison and debug output
- ✅ **Batch Processing**: Works with ComfyUI's batch processing
- ✅ **Batch Resizing**: Resize to multiple sizes in one operation
- ✅ **🔥 Dynamic Inputs**: Multi-Input nodes automatically add/remove image inputs
- ✅ **Optimized Performance**: Built on PIL with efficient compression

## Installation

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone or copy this repository:
```bash
git clone https://github.com/abdullahceylan/ac-comfyui-image-optimizer
# or
cp -r ac-image-optimizer ComfyUI/custom_nodes/
```

3. Restart ComfyUI

## Nodes

### 1. AC Image Optimizer (Basic)

Simple image optimization node with essential controls.

**Inputs:**
- `image` (IMAGE): Input image to optimize
- `format` (JPEG/WEBP/PNG): Output image format
- `quality` (1-100): Compression quality (higher = better quality, larger file)
- `optimize` (BOOLEAN): Enable additional optimization passes

**Outputs:**
- `image` (IMAGE): Optimized image
- `stats` (STRING): Compression statistics (format, size, reduction %)

**Example Usage:**
```
Load Image → AC Image Optimizer → Preview Image
```

**⚠️ Important Note:** This node optimizes the image but returns it as a tensor for preview. If you use ComfyUI's standard "Save Image" node, it will save as PNG (ComfyUI's default). **Use "AC Image Optimizer & Save" instead to save in the correct format.**

**Recommended Settings:**
- **For web display**: JPEG, quality 85
- **For high quality**: JPEG, quality 90-95
- **For smallest size**: WebP, quality 75-85
- **For lossless**: PNG (quality ignored)

### 2. AC Image Optimizer & Save ⭐ **RECOMMENDED**

Optimizes AND saves the image directly in the correct format. This solves the issue where ComfyUI's Save Image node always saves as PNG.

**Inputs:**
- `image` (IMAGE): Input image to optimize
- `format` (JPEG/WEBP/PNG): Output format for saved file
- `quality` (1-100): Compression quality
- `filename_prefix` (STRING): Prefix for saved filename (e.g., "optimized")

**Outputs:**
- `image` (IMAGE): Optimized image (for preview)
- `save_info` (STRING): Save confirmation with file location and stats

**Example Usage:**
```
Load Image → AC Image Optimizer & Save → Preview Image
                                        (optional - already saved!)
```

**Benefits:**
- ✅ Saves directly in the format you choose (JPEG/WebP/PNG)
- ✅ Maintains the compression and optimization
- ✅ No need for separate Save Image node
- ✅ Auto-increments filename to avoid overwriting
- ✅ Shows where the file was saved

**Output Location:** `ComfyUI/output/` directory with filenames like `optimized_00001.jpg`

### 3. AC Image Optimizer Advanced

Advanced optimization with format comparison and debug capabilities.

**Inputs:**
- `image` (IMAGE): Input image to optimize
- `primary_format` (JPEG/WEBP/PNG): Primary output format
- `quality` (1-100): Compression quality
- `enable_debug` (BOOLEAN): Save debug comparison images
- `debug_prefix` (STRING, optional): Prefix for debug filenames

**Outputs:**
- `image` (IMAGE): Optimized image in primary format
- `comparison_stats` (STRING): Detailed comparison of JPEG vs WebP

**Debug Output:**
When `enable_debug` is enabled, saves comparison images to:
```
ComfyUI/output/ac_image_optimizer_debug/
  ├── {prefix}_1_original.png
  ├── {prefix}_2_compressed.jpg
  └── {prefix}_3_compressed.webp
```

**Example Usage:**
```
Load Image → AC Image Optimizer Advanced → Preview Image
                                          └→ Save Image
```

### 4. AC Image Optimizer (Multi-Input) ⭐ **NEW** 🔥 **DYNAMIC**

Optimize multiple separate images with individual connections. Perfect when you want to connect multiple different image nodes directly.

**Inputs:**
- `image1` (IMAGE, required): First image
- `image2+` (IMAGE, optional): Additional images (dynamically added)
- `format` (JPEG/WEBP/PNG): Output format
- `quality` (1-100): Compression quality

**Outputs:**
- `images` (IMAGE): Batch of all optimized images
- `stats` (STRING): Combined statistics for all images

**Key Features:** 
- Each image has its own input port
- **✨ Dynamic Input Addition**: Automatically adds new input when all are connected
- **🏷️ Smart Labels**: Shows connected node name (e.g., `📎 Load Image`)
- **🧹 Auto Cleanup**: Removes empty trailing inputs (keeps at least 1)
- **🖱️ Manual Control**: Right-click for "Add Image Input" and "Cleanup Empty Inputs"
- Connect as many images as you need without limitation!

**Example Usage:**
```
Load Image 1 ──┐
Load Image 2 ──┼──> AC Image Optimizer (Multi-Input) ──> Preview Image
Load Image 3 ──┘         format: JPEG
                         quality: 85
```

---

### 5. AC Image Optimizer & Save (Multi-Input) ⭐ **NEW** 🔥 **DYNAMIC**

Like the Multi-Input optimizer, but saves directly to disk in the correct format.

**Inputs:**
- `image1` (IMAGE, required): First image
- `image2+` (IMAGE, optional): Additional images (dynamically added)
- `format` (JPEG/WEBP/PNG): Output format for saved files
- `quality` (1-100): Compression quality
- `filename_prefix` (STRING): Prefix for saved filenames

**Outputs:**
- `stats` (STRING): Combined save confirmation and statistics

**Dynamic Features:** 
- **✨ Auto-adds inputs** when all are connected
- **🏷️ Smart labels** show connected node names (📎 icon)
- **🧹 Auto-removes** empty trailing inputs
- **🖱️ Right-click menu** for manual control
- No limit on number of images!

**Example Usage:**
```
Generated Image 1 ──┐
Generated Image 2 ──┼──> AC Image Optimizer & Save (Multi-Input)
Generated Image 3 ──┘         format: WEBP
                              quality: 85
                              prefix: "generation"
```

**Output:** Saves as `generation_00001.webp`, `generation_00002.webp`, etc.

---

### 6. AC Image Batch Resizer ⭐ **NEW**

Batch resize a single image to multiple sizes in one operation. Perfect for generating responsive image sets or multiple resolution variants.

**Inputs:**
- `image` (IMAGE): Input image to resize
- `sizes` (STRING, multiline): Multiple sizes, one per line
  - Format: `WIDTHxHEIGHT` (e.g., "1920x1080")
  - Format: `WIDTH,HEIGHT` (e.g., "1920,1080")
  - Format: `WIDTH` only (e.g., "1920") - maintains aspect ratio
  - Comments: Lines starting with `#` are ignored
- `resize_mode`: How to handle aspect ratio
  - `stretch`: Stretch to exact size (may distort)
  - `fit`: Fit inside size maintaining aspect ratio (recommended)
  - `fill`: Fill size maintaining aspect ratio (crop if needed)
  - `pad`: Fit and pad to exact size with color
- `resampling`: Quality filter
  - `lanczos`: Highest quality (default)
  - `bicubic`: High quality, faster
  - `bilinear`: Good quality, fast
  - `nearest`: Fastest, lowest quality
- `pad_color` (optional): Color for pad mode
  - Named colors: "black", "white", "gray", "red", "green", "blue"
  - Hex colors: "#RRGGBB" (e.g., "#FF0000")

**Outputs:**
- `images` (IMAGE): Batch of all resized images (padded to largest dimensions)
- `info` (STRING): Summary of resizing operation

**Note:** Since ComfyUI requires all images in a batch to have the same dimensions, smaller images are automatically padded with black to match the largest image dimensions.

**Example Size Input:**
```
1920x1080
1280x720
800x600
640,480
# This is a comment
1024
```

**Example Usage:**
```
Load Image → AC Image Batch Resizer → Preview Image (shows all sizes)
                                     └→ Save Images (saves batch)
                                     └→ AC Image Optimizer & Save (optimize each)
```

**Use Cases:**
- 📱 Generate responsive image sets for web
- 🖼️ Create multiple resolution variants for different displays
- 📐 Batch resize for social media (Instagram, Twitter, etc.)
- 🎨 Create thumbnails and previews in one step

**Benefits:**
- ✅ One image → Multiple sizes in single operation
- ✅ Flexible size format support
- ✅ Multiple resize modes for different needs
- ✅ High-quality resampling filters
- ✅ Returns batch for further processing

## 🔥 Dynamic Input Feature

The Multi-Input nodes now feature **automatic dynamic input management**!

### How It Works

#### Automatic Behavior
1. **Auto-Add**: When all image inputs are connected, a new empty input automatically appears
2. **Smart Labels**: Input labels update to show connected node names (e.g., `image1` → `📎 Load Image`)
3. **Auto-Restore**: Labels revert to original names when disconnected
4. **Auto-Remove**: Empty trailing inputs are automatically cleaned up (always keeps at least 1 empty)
5. **No Limits**: Connect as many images as you need - inputs grow automatically

#### Manual Control
Right-click on any Multi-Input node to access:
- **Add Image Input**: Manually add a new input slot
- **Cleanup Empty Inputs**: Manually remove empty trailing inputs

### Why This Matters

**Before** (Fixed Inputs):
- Limited to 5 images maximum
- Cluttered with unused input slots (showing image1-5 always)
- Had to know how many images you'd need in advance

**Now** (Dynamic Inputs):
- ✅ Starts with just ONE input (image1)
- ✅ Unlimited images (automatically adds more as you connect)
- ✅ Clean, minimal interface (only shows what you're using)
- ✅ Clear labels showing source nodes (📎 icon)
- ✅ Automatically adapts to your needs
- ✅ No manual input management required

See [DYNAMIC_INPUTS.md](DYNAMIC_INPUTS.md) for detailed documentation.

---

## Node Selection Guide

### When to Use Which Node?

**For Single Image Optimization:**
- Use **AC Image Optimizer** (basic) - Simple, clean interface

**For Multiple Images from ONE Source (Batch):**
- Use **AC Image Optimizer & Preview** - When you have a batch tensor (e.g., from Batch Resizer)
- Use **AC Image Optimizer & Save** - To save batch directly

**For Multiple Images from DIFFERENT Sources:**
- Use **AC Image Optimizer (Multi-Input)** - Connect up to 5 separate image nodes
- Use **AC Image Optimizer & Save (Multi-Input)** - Connect and save up to 5 separate images

**For Resizing to Multiple Sizes:**
- Use **AC Image Batch Resizer** - One image → multiple sizes

**Quick Reference:**
```
Scenario 1: Connect multiple separate image nodes
  → Use Multi-Input variants (image1, image2, image3 ports)

Scenario 2: Process a batch tensor (already combined)
  → Use regular variants (images port)

Scenario 3: Need to combine images first
  → Use ComfyUI's Batch node → Regular variants
```

## Quality Presets

| Preset | Quality | Use Case |
|--------|---------|----------|
| **High** | 95 | Maximum quality, larger files |
| **Good** | 85 | **Recommended** - Best balance |
| **Medium** | 75 | Good quality, smaller files |
| **Low** | 60 | Maximum compression |

## Format Comparison

| Format | Pros | Cons | Best For |
|--------|------|------|----------|
| **JPEG** | Universal support, good compression | Lossy, no transparency | Photos, general images |
| **WebP** | Better compression than JPEG | Limited older browser support | Web display, modern apps |
| **PNG** | Lossless, transparency support | Larger file sizes | Graphics, logos, masks |

## Typical Compression Results

### Example 1: Generated Image (1024x1024)
- **Original PNG**: 2.3 MB
- **JPEG (q=85)**: 83 KB (96% reduction)
- **WebP (q=85)**: 52 KB (98% reduction)

### Example 2: High Resolution Photo (2048x2048)
- **Original PNG**: 8.5 MB
- **JPEG (q=90)**: 420 KB (95% reduction)
- **WebP (q=90)**: 285 KB (97% reduction)

## Workflow Examples

### Basic Workflow
```
┌─────────────┐     ┌───────────────────┐     ┌────────────┐
│ Load Image  │────▶│ AC Image Optimizer│────▶│ Save Image │
└─────────────┘     │  format: JPEG     │     └────────────┘
                    │  quality: 85      │
                    └───────────────────┘
```

### Advanced Workflow with Comparison
```
┌─────────────┐     ┌─────────────────────────┐     ┌────────────────┐
│ Load Image  │────▶│ AC Image Optimizer Adv  │────▶│ Preview Image  │
└─────────────┘     │  primary: JPEG          │     └────────────────┘
                    │  quality: 85            │             │
                    │  debug: True            │             ▼
                    └─────────────────────────┘     ┌────────────────┐
                              │                     │ Display Stats  │
                              └────────────────────▶└────────────────┘
```

### Batch Processing
```
┌─────────────┐     ┌───────────────────┐     ┌───────────────┐     ┌────────────┐
│ Load Images │────▶│ AC Image Optimizer│────▶│ Batch Process │────▶│ Save Batch │
│   (Batch)   │     │  format: WEBP     │     └───────────────┘     └────────────┘
└─────────────┘     │  quality: 80      │
                    └───────────────────┘
```

### Batch Resizing to Multiple Sizes
```
┌─────────────┐     ┌──────────────────────┐     ┌────────────────┐
│ Load Image  │────▶│ AC Image Batch       │────▶│ Preview Batch  │
└─────────────┘     │   Resizer            │     └────────────────┘
                    │  sizes:              │             │
                    │   1920x1080          │             ▼
                    │   1280x720           │     ┌────────────────┐
                    │   800x600            │────▶│ AC Image       │
                    │  mode: fit           │     │ Optimizer Save │
                    │  resampling: lanczos │     └────────────────┘
                    └──────────────────────┘
```

## Integration with Other Nodes

### Example: Optimize After Upscaling
```
Load Image → Upscaler → AC Image Optimizer → Save Image
                        (JPEG, q=90)
```

### Example: Optimize Before API Send
```
Load Image → AC Image Optimizer → Base64 Encode → API Call
             (JPEG, q=85)
```

### Example: Compare Formats
```
Load Image → AC Image Optimizer Advanced → Preview Stats
             (enable_debug: True)
             
Check: ComfyUI/output/ac_image_optimizer_debug/
```

### Example: Generate Responsive Image Set
```
Load Image → AC Image Batch Resizer → For Each → AC Image Optimizer & Save
             sizes: 1920x1080             (loop)   (JPEG, q=85)
                    1280x720
                    800x600
                    640x480
```

## Technical Details

### Image Processing Pipeline

1. **Input**: ComfyUI image tensor (B, H, W, C) in [0, 1] range
2. **Convert**: Tensor → PIL Image
3. **Optimize**: PIL Image → Compressed buffer (using utils/image_optimization.py)
4. **Convert Back**: Compressed buffer → PIL Image → Tensor
5. **Output**: Optimized tensor + statistics

### Supported Color Modes
- RGB (most common)
- RGBA (converted to RGB for JPEG)
- Grayscale (preserved)

### Dependencies
- Python 3.8+
- PyTorch
- Pillow (PIL)
- NumPy

## Troubleshooting

### Issue: Saved image is still PNG/large file size ⚠️

**Problem**: Using "AC Image Optimizer" with ComfyUI's "Save Image" node saves as PNG.

**Why**: ComfyUI's Save Image node always saves tensors as PNG by default, losing your optimization.

**Solution**: Use **"AC Image Optimizer & Save"** node instead! This saves directly in your chosen format.

```
❌ Bad:  Load Image → AC Image Optimizer → Save Image (saves as PNG!)
✅ Good: Load Image → AC Image Optimizer & Save (saves as JPEG/WebP!)
```

### Issue: Node not appearing in ComfyUI
**Solution**: 
1. Check that the folder is in `ComfyUI/custom_nodes/`
2. Restart ComfyUI completely
3. Check console for any error messages

### Issue: "Module not found" error
**Solution**: Ensure all dependencies are installed:
```bash
pip install torch pillow numpy
```

### Issue: Images appear corrupted
**Solution**: 
1. Try increasing quality to 90+
2. Check input image is valid
3. Try different format (PNG for lossless)

### Issue: Debug files not saving
**Solution**:
1. Ensure `enable_debug` is True
2. Check write permissions in ComfyUI/output/
3. Verify the output directory exists

## Performance Tips

1. **Use JPEG for photos**: Better compression than PNG
2. **Use WebP for smallest files**: Up to 30% smaller than JPEG
3. **Quality 85 is optimal**: Good balance of quality and size
4. **Enable optimize**: Minimal speed impact, better compression
5. **Use PNG only when needed**: For transparency or lossless

## Development

### Project Structure
```
ac-image-optimizer/
├── __init__.py                               # Main node definitions
├── web/                                       # JavaScript extensions
│   ├── ac_image_optimizer_multi_extension.js # Multi-Input dynamic behavior
│   └── ac_image_optimizer_multi_input_extension.js # Multi-Input Save dynamic behavior
├── utils/
│   ├── __init__.py
│   ├── image_optimization.py                 # Core optimization utilities
│   └── IMAGE_OPTIMIZATION_USAGE.md
├── DYNAMIC_INPUTS.md                         # Dynamic input documentation
└── README.md                                  # This file
```

### Extending the Node

To add custom functionality, extend the base classes:

```python
from . import ACImageOptimizer

class MyCustomOptimizer(ACImageOptimizer):
    @classmethod
    def INPUT_TYPES(cls):
        inputs = super().INPUT_TYPES()
        inputs["required"]["my_param"] = ("INT", {"default": 10})
        return inputs
    
    def optimize_image(self, image, format, quality, optimize, my_param):
        # Your custom logic
        return super().optimize_image(image, format, quality, optimize)
```
## License

MIT License - see [LICENSE](LICENSE) file for details

Copyright (c) 2025 Abdullah Ceylan

## Support

For issues, questions, or contributions:
- GitHub Issues: [Add your repo link]
- Email: [Add your email]

## Changelog

### v1.1.0 (Dynamic Inputs Update)
- 🔥 **NEW**: Dynamic image input management for Multi-Input nodes
- ✨ Auto-add inputs when all are connected
- 🏷️ **NEW**: Smart labels showing connected node names (📎 icon)
- 🔄 Labels automatically revert when disconnected
- 🧹 Auto-cleanup empty trailing inputs
- 🖱️ Manual control via context menu
- 📚 Updated Python backend to support unlimited dynamic inputs
- 📖 Added DYNAMIC_INPUTS.md documentation

### v1.0.0 (Initial Release)
- Basic image optimization node
- Advanced node with format comparison
- Support for JPEG, WebP, PNG
- Configurable quality settings
- Debug output mode
- Compression statistics
- Multi-Input nodes for multiple separate images
- Batch Resizer node for generating multiple sizes

