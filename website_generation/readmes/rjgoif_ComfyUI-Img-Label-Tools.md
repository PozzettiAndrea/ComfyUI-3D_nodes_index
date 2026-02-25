# ComfyUI Img Label Tools

Custom nodes for ComfyUI that provide advanced image processing and labeling capabilities for creating organized image arrays and equalizing image dimensions.

## Installation

### Via ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "Img Label Tools"
3. Click Install

### Manual Installation

1. Navigate to your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/rjgoif/ComfyUI-Img-Label-Tools.git
   ```

3. Restart ComfyUI

## Nodes

### Image Equalizer

Equalizes multiple images to matching dimensions by either growing all images to the largest size or shrinking all to the smallest size.

**Category:** Image Label Tools

**Inputs:**
- `images` - List or batch of images to equalize

**Parameters:**
- `size_mode` - Either shrinking all large imgages or growing smaller images up.
- `upscale_method` - Scaling algorithm (`nearest-exact`, `bilinear`, `area`, `bicubic`, `lanczos`)
- `keep_proportion` - How to handle aspect ratios:
  - `pad` - Add padding to maintain aspect ratio (default)
  - `stretch` - Stretch to fill target size
  - `resize` - Scale to fit within target (results may not all be the same size, but will fit in a bounding box)
  - `crop` - Crop to fill target
  - `total_pixels` - Maintain total pixel count (results may not all be the same size, will depend on aspect ratio)
- `pad_color` - Color for padding: black, white, gray, a weighted mean of all colors in the image, or just of the edge of the image. 
- `crop_position` - Position for cropping (`center`, `top`, `bottom`, `left`, `right`)

**Outputs:**
- `images` - Batch or list of equalized images (all same dimensions)

**Use Cases:**
- Prepare images for array display (primary use)
- Prepare images for batch processing without losing data
- Create uniform image sets for training data (one of many nodes that can)

---

### Image Array

Creates organized grids/arrays of images with optional text labels. Images are first equalized in size, then labeled, and finally arranged in customizable layouts.

**Category:** Image Label Tools

**Inputs:**
- `images` - List or batch of images to arrange
- `label_input` (optional) - Dynamic label input (string, number, or list)

**Parameters:**

**Layout & Sizing:**
- `background` - Decides the pad color and text color, and the opposite color will be used for label backgrounds
- `resize` - Either shrinking all large imgages or growing smaller images up. Images have to fit together in the array...
- `size_method` - Resizing approach, as above. Will only come into play if you have different sized inputs. 
- `pad` - Enable/disable uniform sizing (boolean)
- `shape` - Array layout:
  - `horizontal` - Single row
  - `vertical` - Single column
  - `square` - N×M grid closest to square (minimizes blank cells)
  - `smart_square` - Optimizes for 1:1 aspect ratio considering image dimensions
  - `smart_landscape` - Optimizes for 3:2 aspect ratio considering image dimensions
  - `smart_portrait` - Optimizes for 2:3 aspect ratio considering image dimensions

**Labels:**
- `labels` - Multiline text box for labels (one per line, or semicolon-separated)
- `label_end` - If more imaages than labels, what to do? Either start over with repeats or just stop 
- `label_location` - Where to place labels.
- `label_size` - Font size in pixels (8-200, default 32)
- `font` - Font selection from ComfyUI/fonts directory (falls back to Arial)

**Spacing:**
- `spacing` - Pixel border around each image (0-100, default 0), high contrast

**Outputs:**
- `image` - Single combined image containing the complete array

**Label Text Format:**
Labels can be provided in multiple ways:
- **Multi-line labels:** Use `\n` within a label for line breaks in the text
  ```
  Image 1
  Image 2\nLine 2
  Image 3
  ```
  This creates 3 labels, where the second label displays on two lines.
    
- **Semicolon-separated:** `Image 1; Image 2; Image 3`
- **Dynamic input:** Connect string, number, or list output from another node
- **Numbers:** Automatically formatted (decimals truncated to 5 places, trailing zeros removed)

**Note:** Actual newlines (pressing Enter) separate different labels. Use `\n` (backslash-n) for line breaks within a single label.


**Use Cases:**
- Image galleries/comparisons (for Reddit, etc)
- Manual XYZ stuff.

---

### Random Subset
Selects a random subset from newline-delimited text. Supports sampling with/without replacement, optional randomization of output order, and configurable delimiters. Returns the subset as a string list, merged string, and list of indices.

---

## Examples
Eventually...

## Requirements

- ComfyUI (latest version recommended)
- Python 3.8+
- Pillow (PIL)
- PyTorch

## Tips

**Image Equalizer:**
- Use `average_edge` padding for seamless borders that match image content
- Use `grow` + `pad` for lossless size normalization
- Use `shrink` + `crop` to create uniform thumbnails

**Image Array:**
- Enable `pad` to ensure uniform cell sizes in the grid
- Use `smart_square` for photo galleries with mixed portrait/landscape images
- Set `spacing` to 5-10 pixels for clean visual separation
- Place labels on `bottom` or `top` for easier reading
- Use `left_vert` or `right_vert` for space-efficient labeling
- For dynamic labels, connect output from other nodes like counters or text processors

## Font Setup

For custom fonts:
1. Create a `fonts` directory in your ComfyUI installation root
2. Place TrueType (.ttf) font files in this directory
3. Restart ComfyUI - fonts will appear in the dropdown

If no fonts directory exists, the node will fall back to Arial (Windows) or the system default.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Credits

- Image Equalizer inspired by KJNodes by GitHub user kijai
- Labels for Image Array inspired by Mikey Nodes by GitHub user bash-j
- Created for the ComfyUI community

## License

MIT License - see LICENSE file for details

## Support

If you encounter any issues or have suggestions, please open an issue on GitHub:
https://github.com/rjgoif/ComfyUI-Img-Label-Tools/issues
