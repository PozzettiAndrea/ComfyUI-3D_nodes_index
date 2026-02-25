# DuoUmiWild - ComfyUI Wildcard Node

A powerful custom node for ComfyUI that supports wildcards from `.txt` files, advanced YAML-based selections with tags, `{}` randomization, and prefix/suffix injection.

## Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```
   cd ComfyUI/custom_nodes/
   ```

2. Clone or copy this repository:
   ```
   git clone https://github.com/yourusername/DuoUmiWild.git
   ```

3. Restart ComfyUI

The node will appear under the **DuoUmiWild** category in the node menu.

## Usage

### Basic Wildcard Syntax

Use `__filename__` in your prompt to randomly select a line from `wildcards/filename.txt`:

```
a photo of __subject__, __style__
```

This will:
- Read a random line from `wildcards/subject.txt`
- Read a random line from `wildcards/style.txt`
- Replace the wildcards with the selected values

### Range Selection Syntax

Select multiple random items from a wildcard file:

- `__2$$colors__` - Select exactly 2 random colors
- `__1-3$$animals__` - Select between 1 and 3 random animals
- `__-5$$tags__` - Select up to 5 random tags
- `__2-$$items__` - Select at least 2 random items

Examples:
```
__3$$artist__ style painting
__1-2$$mood__, __2-4$$colors__
```

### Creating Wildcard Files

1. Create a `wildcards` folder in the DuoUmiWild directory (it's created automatically on first run)

2. Create `.txt` files with one option per line:

**wildcards/subject.txt:**
```
beautiful woman
handsome man
cute cat
majestic dragon
```

**wildcards/style.txt:**
```
photorealistic
anime style
oil painting
watercolor
digital art
```

3. Use comments to document your wildcards (lines starting with `#` are ignored):

```
# Portrait subjects
beautiful woman
handsome man
# Fantasy subjects
elf warrior
dwarf blacksmith
```

### Using the Seed Parameter

The seed parameter ensures reproducible results:
- Same seed = same random selections
- Different seed = different random selections
- Connect to your KSampler's seed for consistent generations

### Nested Folder Support

Organize wildcards in subfolders for better organization:

```
wildcards/
├── characters/
│   ├── heroes.txt
│   └── villains.txt
└── environments/
    ├── indoor.txt
    └── outdoor.txt
```

Use with folder path:
```
__characters/heroes__ fighting __characters/villains__ in __environments/indoor__
```

Or just use the filename (ignores folder structure):
```
__heroes__ vs __villains__
```

### Recursive/Nested Wildcards

Wildcard files can contain other wildcards that will be expanded:

**wildcards/combo.txt:**
```
__subject__ in __style__
__quality__ portrait
```

Using `__combo__` will expand the wildcards inside!

### YAML Wildcards

DuoUmiWild supports advanced YAML-based wildcards with tag selection and prefix/suffix injection.

**Tag-Based Selection:**
```
<[Pose]>              # Select any entry tagged "Pose"
<[Hat][Fancy]>        # Select entries with BOTH "Hat" AND "Fancy" tags
<[Hat|Headband]>      # Select entries with "Hat" OR "Headband" tag
```

**Curly Brace Randomization:**
```
{option1|option2|option3}        # Randomly pick one
{2$$a|b|c|d}                     # Pick exactly 2
{1-3$$red|blue|green}            # Pick 1 to 3
```

**Combined Example:**
```
girl, {a|b|c|d|e}-size, <[Pose]>, wearing {<[Hat]>|<[Headband]>}
```

See **[YAML_GUIDE.md](YAML_GUIDE.md)** for complete YAML documentation!

### Curly Brace Randomization

Use `{}` with `|` pipes to randomly select options:

```
{happy|sad|neutral} expression
{0-1$$dark skinned female}
wearing {red|blue|green} dress
```

## Nodes Included

### 1. Wildcard Prompt Node

The main wildcard processing node.

**Inputs:**
- **text**: Your prompt with wildcards in `__filename__` format, YAML tags `<[Tag]>`, and `{}` randomization
- **seed**: Random seed for reproducible wildcard selection (0 to max int)
- **autorefresh**:
  - **No** (default): Cache wildcard files for faster processing
  - **Yes**: Reload files each time (slower, but see edits immediately)

**Outputs:**
- **processed_text**: Your prompt with all wildcards replaced with random selections
- **UI Display**: The node displays the processed text as copyable string in the UI

### 2. Latent Ratio Selector Node

Creates empty latent images with predefined aspect ratios.

**Inputs:**
- **ratio_selected**: Choose from portrait, landscape, square, or cinematic ratios
- **batch_size**: Number of latent images (1-64)
- **randomize**:
  - **No**: Use the manually selected ratio
  - **Yes**: Randomly select a ratio (ignores ratio_selected)
- **randomize_from**: When randomize is Yes, select from:
  - **All**: Any ratio
  - **Portrait Only**: Only portrait ratios (2:3, 3:4, 4:5, 9:16)
  - **Landscape Only**: Only landscape ratios (16:9, 21:9, etc.)
  - **Square Only**: 1:1 ratio
- **seed**: Seed for random ratio selection

**Outputs:**
- **latent**: Empty latent tensor
- **ratio_used**: String describing which ratio was used
- **width**: Image width in pixels
- **height**: Image height in pixels

**Available Ratios:**
- Portrait: 2:3 (832x1248), 3:4 (880x1176), 4:5 (912x1144), 9:16 (768x1360)
- Square: 1:1 (1024x1024)
- Landscape: 4:3 (1176x880), 16:9 (1360x768), 21:9 (1536x640), and more
- Cinematic: IMAX (1.43:1), Cinemascope (2.35:1), Anamorphic (2.39:1)
- Special: Golden Ratio (1.618:1)

## Examples

### Simple Example
**Input:**
```
a __quality__ photo of a __subject__
```

**Wildcard files:**
- `wildcards/quality.txt`: high-quality, stunning, professional
- `wildcards/subject.txt`: cat, dog, bird

**Possible outputs:**
- "a stunning photo of a cat"
- "a professional photo of a bird"
- "a high-quality photo of a dog"

### Advanced Example
**Input:**
```
__1-2$$mood__ portrait of __subject__, __2-3$$style__, __lighting__
```

**Possible output:**
```
dramatic, moody portrait of elegant woman, oil painting, renaissance style, soft lighting
```

## Features

- ✅ Random line selection from .txt files
- ✅ Range-based selection (select multiple items)
- ✅ Seeded randomization for reproducibility
- ✅ Comment support in wildcard files (lines starting with #)
- ✅ Inline comment removal
- ✅ Recursive/nested wildcard support (wildcards within wildcards)
- ✅ Nested folder organization for wildcard files
- ✅ **YAML support with tag-based selection** `<[Tag]>`
- ✅ **YAML Prefix/Suffix random injection**
- ✅ **Curly brace randomization** `{option1|option2}`
- ✅ **Combined syntax support** - Mix wildcards, YAML, and `{}`
- ✅ **Latent ratio selector** with randomization
- ✅ **17 preset aspect ratios** (portrait, landscape, cinematic)
- ✅ Text preview as copyable string in the UI
- ✅ File caching with optional auto-refresh
- ✅ Automatic comma formatting
- ✅ Clean output (removes extra commas and whitespace)

## File Structure

```
DuoUmiWild/
├── __init__.py          # Node registration
├── wildcard_node.py     # Main node implementation
├── README.md            # This file
└── wildcards/           # Your wildcard .txt files
    ├── subject.txt
    ├── style.txt
    ├── colors.txt
    └── ...
```

## Tips

1. **Organize your wildcards**: Create separate files for different categories (subjects, styles, colors, moods, etc.)

2. **Use descriptive filenames**: Name files clearly so you can easily remember them in prompts

3. **Comment your files**: Add comments to organize and document your wildcard collections

4. **Test with different seeds**: Try different seed values to explore various combinations

5. **Combine with other nodes**: Connect the output to any node that accepts text/string input

## Troubleshooting

**Wildcard not found:**
- Check that the file exists in the `wildcards/` directory
- Ensure the filename matches exactly (case-sensitive on some systems)
- Verify the file has a `.txt` extension

**No output / empty result:**
- Check that your wildcard files aren't empty
- Ensure lines aren't all comments
- Look at the console for error messages

**Same result every time:**
- Verify you're changing the seed value
- Or connect to a random seed generator node

## License

MIT License - Feel free to use and modify as needed.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues on GitHub.

## Credits

Inspired by the original UmiAI wildcard system for Stable Diffusion WebUI.
