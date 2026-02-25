# Pixel Sorting

ASDF-style pixel sorting implementation in Python with extended features. Based on [Kim Asendorf's original Processing sketch](https://github.com/kimasendorf/ASDFPixelSort) from 2010, with additional modes inspired by [satyarth/pixelsort](https://github.com/satyarth/pixelsort).

## What is Pixel Sorting?

Pixel sorting is a glitch art technique that rearranges pixels in an image based on certain criteria (brightness, hue, saturation, etc.) within defined intervals. This creates distinctive visual effects ranging from subtle distortions to dramatic abstract transformations.

## Installation

### As a CLI tool

This project uses `uv` for dependency management. Dependencies will be installed automatically when you run the script.

### As a library

Install using pip:

```bash
pip install git+https://github.com/rockerBOO/pixel-sorting.git
```

Or with uv:

```bash
uv pip install git+https://github.com/rockerBOO/pixel-sorting.git
```

### For ComfyUI

Clone directly into your ComfyUI custom_nodes directory:

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/rockerBOO/pixel-sorting.git
cd pixel-sorting
pip install -e .
```

The nodes will be automatically available after restarting ComfyUI.

**See [COMFYUI_SETUP.md](COMFYUI_SETUP.md) for detailed ComfyUI installation and usage instructions.**

## Quick Start

### Command Line

```bash
# Analyze an image to find good thresholds
uv run python main.py your_image.jpg --analyze

# Sort with ASDF bright mode
uv run python main.py your_image.jpg --interval bright

# Sort with random intervals and hue sorting
uv run python main.py your_image.jpg --interval random --sort hue
```

### As a Library

```python
from PIL import Image
from pixelsort import pixelsort, analyze

# Load an image
img = Image.open("photo.jpg")

# Analyze to get suggested thresholds
stats = analyze(img)
print(f"Suggested bright threshold: {stats['suggestions']['bright']['subtle']}")

# Apply pixel sorting
result = pixelsort(
    img,
    interval='bright',
    sorting='hue',
    bright_value=stats['suggestions']['bright']['subtle']
)

# Save result
result.save("sorted.png")
```

See [example_library.py](example_library.py) for more usage examples.

## Usage

### Basic Command Structure

```bash
uv run python main.py INPUT [OPTIONS]
```

### Image Analysis

Before sorting, analyze your image to find optimal thresholds:

```bash
uv run python main.py input.jpg --analyze
```

This displays:
- Brightness statistics (min, max, mean, median, percentiles)
- Pixel value statistics
- Suggested thresholds for each interval mode (subtle, moderate, aggressive)

### Interval Modes

The `--interval` (or `-i`) flag controls WHERE pixels are sorted:

#### ASDF-style Threshold Modes

- **bright** - Sort pixels with brightness ≥ threshold (default: 127)
  ```bash
  uv run python main.py input.jpg --interval bright --bright-value 100
  ```

- **dark** - Sort pixels with brightness ≤ threshold (default: 223)
  ```bash
  uv run python main.py input.jpg --interval dark --dark-value 50
  ```

- **white** - Sort pixels with value ≥ threshold (default: -12345678)
  ```bash
  uv run python main.py input.jpg --interval white --white-value -10000000
  ```

- **black** - Sort pixels with value ≤ threshold (default: -3456789)
  ```bash
  uv run python main.py input.jpg --interval black --black-value -5000000
  ```

#### Extended Interval Modes

- **threshold** - Sort pixels between lower and upper brightness thresholds
  ```bash
  uv run python main.py input.jpg --interval threshold --lower-threshold 0.3 --upper-threshold 0.7
  ```

- **random** - Randomly generated intervals
  ```bash
  uv run python main.py input.jpg --interval random --char-length 100
  ```

- **waves** - Wave-like intervals of nearly uniform width
  ```bash
  uv run python main.py input.jpg --interval waves --char-length 75
  ```

- **edges** - Intervals defined by edge detection
  ```bash
  uv run python main.py input.jpg --interval edges --lower-threshold 0.2
  ```

- **none** - Sort entire rows (no interval boundaries)
  ```bash
  uv run python main.py input.jpg --interval none
  ```

### Sorting Functions

The `--sort` (or `-s`) flag controls HOW pixels are sorted within intervals:

- **value** - ASDF-style pixel integer value (default)
- **lightness** - Sort by brightness/lightness (HLS)
- **hue** - Sort by hue (creates rainbow effects)
- **saturation** - Sort by color saturation
- **intensity** - Sort by sum of RGB values
- **minimum** - Sort by minimum RGB channel value

```bash
# Sort bright intervals by hue
uv run python main.py input.jpg --interval bright --sort hue

# Sort dark intervals by saturation
uv run python main.py input.jpg --interval dark --dark-value 60 --sort saturation
```

### Additional Parameters

#### Angle Rotation

Sort at an angle (in degrees):

```bash
# Sort at 45 degrees
uv run python main.py input.jpg --interval bright --angle 45

# Sort at 90 degrees (vertical sorting)
uv run python main.py input.jpg --interval bright --angle 90
```

#### Randomness

Randomly skip sorting some intervals (0-100%):

```bash
# Skip 30% of intervals randomly
uv run python main.py input.jpg --interval bright --randomness 30
```

#### Multiple Passes

Apply sorting multiple times for stronger effects:

```bash
# Two passes
uv run python main.py input.jpg --interval bright --loops 2
```

#### Character Length

Control interval width for random and waves modes:

```bash
uv run python main.py input.jpg --interval random --char-length 150
```

#### Output Path

Specify output file:

```bash
uv run python main.py input.jpg --interval bright --output result.png
```

If not specified, output defaults to `input_INTERVAL_SORT.png`

## Examples

### Classic ASDF Effects

```bash
# Bright mode with default settings
uv run python main.py photo.jpg --interval bright

# Dark mode with custom threshold (use --analyze first to find good values)
uv run python main.py photo.jpg --interval dark --dark-value 50

# Two-pass sorting (sort vertically then horizontally like original ASDF)
uv run python main.py photo.jpg --interval bright --angle 90 --output temp.png
uv run python main.py temp.png --interval bright --output final.png
```

### Creative Effects

```bash
# Rainbow sorting (hue-based)
uv run python main.py photo.jpg --interval bright --sort hue

# Random glitch with saturation sorting
uv run python main.py photo.jpg --interval random --char-length 80 --sort saturation

# Edge-detected intervals with lightness sorting
uv run python main.py photo.jpg --interval edges --lower-threshold 0.3 --sort lightness

# Diagonal sorting
uv run python main.py photo.jpg --interval bright --angle 45

# Chaotic random with high randomness
uv run python main.py photo.jpg --interval random --randomness 50 --char-length 100
```

### Combining Multiple Options

```bash
# Complex example: diagonal bright intervals, sorted by hue, with 20% randomness
uv run python main.py photo.jpg --interval bright --bright-value 100 --sort hue --angle 45 --randomness 20

# Aggressive dark sorting with multiple passes
uv run python main.py photo.jpg --interval dark --dark-value 75 --loops 3
```

## Complete Options Reference

```
positional arguments:
  input                 Input image path

optional arguments:
  -h, --help            Show help message
  --analyze             Analyze image and suggest thresholds (does not sort)

interval options:
  -i, --interval {threshold,bright,dark,white,black,random,waves,edges,none}
                        Interval function (default: bright)

sorting options:
  -s, --sort {lightness,hue,saturation,intensity,minimum,value}
                        Sorting function (default: value)

output options:
  -o, --output OUTPUT   Output image path

parameters:
  -a, --angle ANGLE     Angle in degrees (default: 0)
  -r, --randomness PCT  Randomness percentage 0-100 (default: 0)
  -c, --char-length N   Characteristic length for random/waves (default: 50)
  -l, --loops N         Number of sorting passes (default: 1)

threshold values:
  --lower-threshold FLOAT   Lower threshold 0-1 for threshold mode (default: 0.25)
  --upper-threshold FLOAT   Upper threshold 0-1 for threshold mode (default: 0.8)
  --white-value INT         White threshold for white mode (default: -12345678)
  --black-value INT         Black threshold for black mode (default: -3456789)
  --bright-value INT        Brightness threshold for bright mode (default: 127)
  --dark-value INT          Darkness threshold for dark mode (default: 223)
```

## Tips & Tricks

1. **Always analyze first** - Run `--analyze` to find good thresholds for your specific image
2. **Start subtle** - Use the "subtle" suggested values from analysis for gentle effects
3. **Dark/bright defaults are often wrong** - The ASDF defaults (127, 223) work poorly on most images. Use --analyze to find better values.
4. **Experiment with sorting functions** - Try different combinations of interval modes and sorting functions
5. **Angle 90 = vertical sorting** - Use `--angle 90` then `--angle 0` for the classic ASDF two-pass effect
6. **Randomness adds variation** - Small randomness values (10-30%) can make effects more interesting

## Recommended Threshold Ranges

Based on typical images:

- **bright-value**: 75-150 (sorts top 10-50% brightest pixels)
- **dark-value**: 30-80 (sorts bottom 10-40% darkest pixels)
- **lower-threshold**: 0.2-0.4 (for threshold mode)
- **upper-threshold**: 0.6-0.9 (for threshold mode)

## How It Works

1. **Interval Generation** - The interval function divides each row into segments (intervals) that will or won't be sorted
2. **Pixel Sorting** - Pixels within each interval are sorted according to the sorting function
3. **Randomness** - Some intervals are randomly skipped (left unsorted) based on the randomness percentage
4. **Rotation** - The image can be rotated before/after sorting for diagonal effects
5. **Multiple Passes** - The process can be repeated multiple times for stronger effects

## Library API

### pixelsort()

Main function to sort pixels in an image.

```python
pixelsort(
    image: Image.Image,
    interval: str | Callable = 'bright',
    sorting: str | Callable = 'value',
    angle: float = 0,
    randomness: float = 0,
    char_length: int = 50,
    loops: int = 1,
    lower_threshold: float = 0.25,
    upper_threshold: float = 0.8,
    white_value: int = -12345678,
    black_value: int = -3456789,
    bright_value: int = 127,
    dark_value: int = 223,
) -> Image.Image
```

**Parameters:**
- `image` - PIL Image to sort (will be converted to RGBA)
- `interval` - Interval function name or callable
  - Options: `'threshold'`, `'bright'`, `'dark'`, `'white'`, `'black'`, `'random'`, `'waves'`, `'edges'`, `'none'`
- `sorting` - Sorting function name or callable
  - Options: `'lightness'`, `'hue'`, `'saturation'`, `'intensity'`, `'minimum'`, `'value'`
- `angle` - Rotation angle in degrees (default: 0)
- `randomness` - Percentage of intervals to skip (0-100, default: 0)
- `char_length` - Characteristic length for random/waves modes (default: 50)
- `loops` - Number of sorting passes (default: 1)
- `lower_threshold` - Lower threshold for threshold mode (0-1, default: 0.25)
- `upper_threshold` - Upper threshold for threshold mode (0-1, default: 0.8)
- `white_value` - Threshold for white mode (default: -12345678)
- `black_value` - Threshold for black mode (default: -3456789)
- `bright_value` - Threshold for bright mode (0-255, default: 127)
- `dark_value` - Threshold for dark mode (0-255, default: 223)

**Returns:** PIL Image with sorted pixels

### analyze()

Analyze image brightness distribution and suggest thresholds.

```python
analyze(image: Image.Image) -> dict
```

**Parameters:**
- `image` - PIL Image to analyze

**Returns:** Dictionary containing:
- `brightness_stats` - min, max, mean, median, percentiles
- `pixel_int_stats` - min, max, median, percentiles
- `suggestions` - recommended thresholds for each mode
  - `bright`, `dark`, `white`, `black` - each with `subtle`, `moderate`, `aggressive` values

**Example:**

```python
from PIL import Image
from pixelsort import pixelsort, analyze

img = Image.open("photo.jpg")

# Get suggested thresholds
stats = analyze(img)
bright_threshold = stats['suggestions']['bright']['subtle']

# Apply sorting
result = pixelsort(
    img,
    interval='bright',
    sorting='hue',
    bright_value=bright_threshold,
    randomness=10
)

result.save("output.png")
```

### ComfyUI Integration

This package works out-of-the-box as a ComfyUI custom node.

**Included nodes:**
- `PixelSorting` - Main sorting node with all parameters exposed (found under `image/effects`)
- `PixelSortAnalyze` - Analyze images and output suggested thresholds (found under `image/analysis`)

**Quick setup:**
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/rockerBOO/pixel-sorting.git
cd pixel-sorting
pip install -e .
# Restart ComfyUI
```

**Features:**
- Proper tensor conversion between ComfyUI and PIL formats
- Batch processing support
- All interval and sorting modes available
- Direct output of analyzed threshold values to other nodes

For detailed ComfyUI usage, workflows, and troubleshooting, see **[COMFYUI_SETUP.md](COMFYUI_SETUP.md)**.

## Credits

- Original ASDF Pixel Sort: [Kim Asendorf](https://github.com/kimasendorf/ASDFPixelSort) (2010)
- Python implementation inspiration: [satyarth/pixelsort](https://github.com/satyarth/pixelsort)
