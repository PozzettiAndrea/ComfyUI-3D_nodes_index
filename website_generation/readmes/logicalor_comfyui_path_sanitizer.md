# ComfyUI Path Sanitizer

A ComfyUI custom node that sanitizes strings for use as filesystem paths (directories or filenames).

## Features

- **Removes/replaces invalid characters** - Characters like `< > : " / \ | ? *` and control characters
- **Handles Windows reserved names** - `CON`, `PRN`, `AUX`, `NUL`, `COM1-9`, `LPT1-9`
- **Unicode normalization** - Converts unicode to a standard form (NFKC)
- **Strips trailing periods/spaces** - Windows doesn't allow these at the end of filenames
- **Preserves file extensions** - When truncating, tries to keep the extension intact

## Installation

### Via ComfyUI Manager

Search for "Path Sanitizer" in ComfyUI Manager and click Install.

### Manual Installation

1. Navigate to your ComfyUI `custom_nodes` directory
2. Clone this repository:
   ```bash
   git clone https://github.com/logicalor/comfyui_path_sanitizer.git
   ```
3. Restart ComfyUI

## Usage

The node appears under the **utils/string** category in the node menu.

### Inputs

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| `input_string` | STRING | "" | The string to sanitize |
| `replacement_char` | STRING | "_" | Character to replace invalid characters with |
| `max_length` | INT | 255 | Maximum length of the output string |
| `lowercase` | BOOLEAN | False | Convert the result to lowercase |
| `strip_spaces` | BOOLEAN | False | Remove all spaces from the result |
| `collapse_replacement` | BOOLEAN | True | Collapse consecutive replacement characters into one |

### Output

| Output | Type | Description |
|--------|------|-------------|
| `sanitized_path` | STRING | A clean string safe for filesystem use |

## Examples

| Input | Output |
|-------|--------|
| `my:file<name>.txt` | `my_file_name.txt` |
| `CON` | `_CON` |
| `hello   world` | `hello   world` |
| `hello   world` (strip_spaces=True) | `helloworld` |
| `My///Path` | `My_Path` |
| `trailing...` | `trailing` |

## License

MIT License
