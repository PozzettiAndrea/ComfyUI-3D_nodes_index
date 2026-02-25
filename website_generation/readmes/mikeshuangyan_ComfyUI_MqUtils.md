# ComfyUI MqUtils

A collection of utility nodes for ComfyUI that provide essential helper functions for workflow automation.

## Features

This extension provides the following utility nodes:

### 🔤 MQ Text Splitter
Splits text into a list based on a delimiter with advanced control options.
- **Inputs:**
  - `text`: The input text to split
  - `delimiter`: The character(s) to split by (supports escape sequences like `\n`)
  - `start_index`: Starting position in the result list
  - `skip_every`: Skip N items between selections
  - `max_count`: Maximum number of items to return
- **Outputs:**
  - `STRING LIST`: Array of split text items
  - `LENGTH`: Number of items in the result

### 🔀 MQ Int Switch
Conditional integer value selector based on a boolean condition.
- **Inputs:**
  - `if_true`: Value to return when condition is true
  - `if_false`: Value to return when condition is false
  - `condition`: Boolean condition to evaluate
- **Output:** Selected integer value

### 🔢 MQ Int To String
Converts integer values to string format.
- **Input:** Integer value (supports large numbers from -1e9 to 1e9)
- **Output:** String representation of the integer

### 🖥️ MQ Check FP4 Support
Checks if your GPU supports FP4 (4-bit floating point) operations.
- **Output:** Boolean indicating FP4 support (requires GPU compute capability > 9.0)

## Installation

### Via ComfyUI Manager (Recommended)
1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager)
2. Search for "ComfyUI MqUtils" in the Manager
3. Click Install
4. Restart ComfyUI

### Manual Installation
1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/mikeshuangyan/ComfyUI_MqUtils.git
   ```
3. Restart ComfyUI

## Usage Examples

### Text Processing
Use **MQ Text Splitter** to process comma-separated prompts or split multi-line text:
- Split tags: `"landscape, sunset, mountains"` → `["landscape", "sunset", "mountains"]`
- Process every other item with `skip_every: 1`
- Limit results with `max_count`

### Conditional Logic
Use **MQ Int Switch** for dynamic workflow control:
- Switch between different seed values based on conditions
- Toggle between quality levels
- Implement if-then logic in your workflows

### Type Conversion
Use **MQ Int To String** when you need to:
- Display numeric values in text widgets
- Concatenate numbers with strings
- Format numeric outputs

## Development

To set up the development environment:

```bash
cd ComfyUI_MqUtils
pip install -e .[dev]
pre-commit install
```

This will install the package in editable mode and set up pre-commit hooks for code quality checks.

### Code Quality
The project uses:
- **Ruff** for linting and formatting
- **Pre-commit** hooks to ensure code quality
- GitHub Actions for continuous integration

## Contributing

Contributions are welcome! Please ensure your code passes all linting checks:

```bash
ruff check .
ruff format .
```

## License

This project is licensed under the GNU General Public License v3. See the [LICENSE](LICENSE) file for details.

## Support

- Report issues on [GitHub Issues](https://github.com/mikeshuangyan/ComfyUI_MqUtils/issues)
- For questions, join the [ComfyUI Discord](https://discord.com/invite/comfyorg)