# ComfyUI Random Wildcard Loader

A powerful ComfyUI custom node for dynamically loading and combining wildcard prompts. Perfect for generating diverse, randomized prompts for image generation workflows.

## Features

- **Random Wildcard Selection** - Automatically selects random lines from wildcard text files
- **Inline Wildcard Expansion** - Use `__wildcard__` syntax directly in your prompts
- **Mad Libs Style `$prompt`** - Insert random wildcard content anywhere with the `$prompt` keyword
- **Subfolder Filtering** - Target specific wildcard folders for more controlled randomization
- **Prefix & Suffix Support** - Wrap your output with custom text (e.g., LoRA triggers)
- **Same File Mode** - Force all random selections from a single wildcard file
- **Nested Folder Control** - Choose between all levels or top-level only scanning
- **Seed Control** - Reproducible results with seed-based randomization

<p align="center">
  <img src="images/RandomWildcard.png" alt="Node Screenshot" width="600">
</p>

## Installation

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/BWDrum/ComfyUI-RandomWildcardLoader.git
```
Restart ComfyUI after installation.

### ComfyUI Manager
Search for "Random Wildcard Loader" in ComfyUI Manager.

## Nodes Included

| Node | Description |
|------|-------------|
| **Random Wildcard Loader** | Basic version with core functionality |
| **Random Wildcard Loader (Advanced)** | Full-featured version with prefix/suffix, subfolder filtering, and more |

## Usage

### Basic Setup
1. Create a `wildcards` folder in your ComfyUI root directory
2. Add `.txt` files with one prompt per line
3. Add the node to your workflow

### Wildcard Syntax

#### `__wildcard__` - Specific Wildcard
Reference a specific wildcard file by name:
```
A beautiful __colors__ sunset over __landscapes__
```
This expands `__colors__` with a random line from `colors.txt` and `__landscapes__` from `landscapes.txt`.

#### `$prompt` - Random Wildcard (Mad Libs Style)
Insert random content from any available wildcard:
```
The artist created a $prompt using $prompt techniques
```
Each `$prompt` is replaced with random content from a randomly selected wildcard file.

#### Nested Folders
Access wildcards in subfolders:
```
A __styles/artistic__ painting of __subjects/animals__
```

### Advanced Node Options

| Option | Description |
|--------|-------------|
| **num_files** | Number of random wildcard files to load |
| **seed** | Random seed for reproducible results |
| **separator** | Text between combined wildcards (default: `, `) |
| **subfolder** | Limit selection to a specific subfolder |
| **prefix** | Text added before the output (with automatic space) |
| **suffix** | Text added after the output (with automatic comma) |
| **include_nested** | `All Levels` or `Top Level Only` folder scanning |
| **same_file** | `Different Files` or `Same File` for multi-selection |

### Prefix & Suffix Example
Perfect for LoRA triggers:
- Prefix: `<lora:MyLora:0.8>`
- Suffix: `masterpiece, best quality`

Output: `<lora:MyLora:0.8> cyberpunk city, neon lights, masterpiece, best quality`

## Folder Structure Example

```
ComfyUI/
├── wildcards/
│   ├── colors.txt
│   ├── styles.txt
│   ├── subjects/
│   │   ├── animals.txt
│   │   └── people.txt
│   └── artistic/
│       ├── movements.txt
│       └── techniques.txt
└── custom_nodes/
    └── ComfyUI-RandomWildcardLoader/
```

## Wildcard File Format

Simple text files with one option per line:

**colors.txt**
```
vibrant red
deep blue
golden yellow
emerald green
soft pink
```

**styles.txt**
```
photorealistic
oil painting
watercolor
digital art
anime style
```

## Output Display

The node displays:
- **Loaded Contents** - The final combined output text
- **Loaded Wildcards** - Which wildcards were used (e.g., `styles/__artistic__`, `__colors__`)

## Requirements

- ComfyUI (latest version recommended)
- No additional dependencies required

## License

MIT License - Feel free to use, modify, and distribute.

## Contributing

Pull requests and issues are welcome! Feel free to suggest new features or report bugs.

---

Made with care for the ComfyUI community
