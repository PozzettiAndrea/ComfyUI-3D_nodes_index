# ComfyUI Multi-Replace

[![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom%20Node-blue)](https://github.com/comfyanonymous/ComfyUI)

A ComfyUI custom node package for creating and applying multiple find/replace pairs to text.

## Features

- **Find/Replace Pairs Node**: Create an arbitrary number of find/replace pairs
  - Starts with one pair, click "➕ Add Pair" button to add more (up to 80 pairs)
  - Right-click menu also provides Add/Remove pair options
  - Each pair has a text field with an input connector (connected inputs override widget values)
  - Outputs: pairs object, JSON, and CSV formats

- **Text Replacer Node**: Apply find/replace pairs to text
  - Accepts pairs from the FindReplacePairs node
  - Supports regular expressions
  - Case-sensitive/insensitive matching
  - Replace all or first occurrence only
  - Outputs: modified text, pairs (for chaining), changes log, and replacement count

## Installation

1. Clone or copy this folder to your ComfyUI `custom_nodes` directory:
   ```
   cd ComfyUI/custom_nodes
   git clone <repo-url> comfyui-multi-replace
   ```

2. Restart ComfyUI

## Usage

### Basic Usage

1. Add a **Find/Replace Pairs** node
2. Enter your find pattern and replacement in the first pair
3. Click **➕ Add Pair** to add more pairs as needed
4. Connect the `pairs` output to a **Text Replacer** node
5. Enter or connect your input text
6. Get the modified text from the `result` output

### Connecting Dynamic Values

Each pair has both a text field for direct entry and an input connector on the left side. When a connector is linked, it overrides the widget value.

### Chaining Replacers

The Text Replacer node passes through the pairs object, allowing you to chain multiple replacers or use the same pairs set multiple times.

### Output Formats

**Find/Replace Pairs outputs:**
- `pairs` - Internal pairs object for use with TextReplacer
- `json` - JSON array of pairs: `[{"find": "...", "replace": "...", "index": 1}, ...]`
- `csv` - CSV format: `find,replace` per line

**Text Replacer outputs:**
- `result` - The text after all replacements
- `pairs` - The pairs object (for chaining)
- `changes_log` - Human-readable log of changes made
- `replacement_count` - Total number of replacements performed

## Node Reference

### Find/Replace Pairs

| Input | Type | Description |
|-------|------|-------------|
| `find_N` | STRING | Find pattern for pair N (text field + input connector) |
| `replace_N` | STRING | Replacement for pair N (text field + input connector) |

**Buttons:**
- **➕ Add Pair** - Add a new find/replace pair
- **➖ Remove Last Pair** - Remove the last pair (disabled when only 1 pair exists)

### Text Replacer

| Input | Type | Description |
|-------|------|-------------|
| `pairs` | FR_PAIRS | Pairs from FindReplacePairs node |
| `input_text` | STRING | Text to perform replacements on |
| `use_regex` | BOOLEAN | Treat patterns as regex |
| `case_sensitive` | BOOLEAN | Case-sensitive matching |
| `replace_all` | BOOLEAN | Replace all vs first occurrence |

## License

MIT License

## Credits

Created for use with [ComfyUI](https://github.com/comfyanonymous/ComfyUI).
