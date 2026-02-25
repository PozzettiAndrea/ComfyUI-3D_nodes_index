# ComfyUI-Regex-Runner

A ComfyUI custom node plugin that allows you to run regular expression operations directly in ComfyUI workflows.

[中文文档](README_CN.md)

> This custom node is powered by [ltdrdata](https://github.com/ltdrdata) and developed by [Cursor](https://cursor.sh/)

## Features

- Execute regex matching and replacement in ComfyUI
- Support all standard Python regular expression syntax
- Easy text input and output handling
- Fully integrated into ComfyUI workflows

## Installation

1. Navigate to your ComfyUI custom nodes directory:

```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:

```bash
git clone https://github.com/ltdrdata/ComfyUI-Regex-Runner
```

## Usage

### Available Nodes

The plugin provides the following nodes:

- **Regex Match**: Performs regular expression matching operations
- **Regex Replace**: Performs regular expression replacement operations

### Node Parameters

#### Regex Match Node
- `text`: Input text to match
- `pattern`: Regular expression pattern
- `flags`: Regex flags (optional)
- Output: List of matched texts

#### Regex Replace Node
- `text`: Input text to process
- `pattern`: Regular expression pattern
- `replacement`: Replacement text
- `flags`: Regex flags (optional)
- Output: Replaced text

### Examples

1. **Extract Numbers**
```python
Input text: "Image size is 512x512"
Pattern: "\d+"
Output: ["512", "512"]
```

2. **Replace Text**
```python
Input text: "prompt: a cat"
Pattern: "^prompt: "
Replacement: "negative prompt: "
Output: "negative prompt: a cat"
```

## Common Issues

1. **Regex Not Matching?**
   - Check if the regex syntax is correct
   - Verify if you need to use raw strings (r"pattern")
   - Ensure special characters are properly escaped

2. **How to Use Regex Flags?**
   - Supports standard Python regex flags
   - Examples: `re.IGNORECASE`, `re.MULTILINE`, etc.



## License

MIT License

## Support

If you encounter any issues or have suggestions for improvements:

1. Submit an issue on GitHub
2. Provide detailed problem description and steps to reproduce
3. Include relevant error messages and logs
