# ComfyUI-MouseCoords

Display real-time mouse coordinates in graph space for ComfyUI workflows.

## Features

- Real-time display of mouse position in graph coordinates
- Always visible in top-right corner of canvas
- No configuration needed

## Installation

### Via ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "MouseCoords"
3. Click Install
4. Restart ComfyUI

### Manual Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/Malkalypse/ComfyUI-MouseCoords.git
   ```

3. Restart ComfyUI

## Usage

Once installed, the mouse coordinates will automatically appear in the top-right corner of your canvas. The coordinates are displayed in graph space (not screen space), which is useful for:

- Positioning nodes precisely
- Debugging node layouts
- Measuring distances between elements
- Creating extensions that need coordinate information

## How It Works

This extension is intentionally minimal:
- Pure JavaScript, no Python dependencies
- Uses ComfyUI's built-in coordinate conversion
- Automatically loads a small CSS file for styling
- No API calls or backend processing

## Project Structure

```
ComfyUI-MouseCoords/
├── __init__.py           # Extension registration (v1.0.0)
├── README.md             # This file
├── LICENSE               # Unlicense (public domain)
├── pyproject.toml        # Project metadata
└── web/
    ├── mouse_coords.js   # Main extension logic
    └── styles.css        # Display styling
```

## Version

Current version: **1.0.0**

This extension is feature-complete and stable. Future versions will only be released if ComfyUI API changes require updates.

## License

This is free and unencumbered software released into the public domain. See [LICENSE](LICENSE) for details.

## Contributing

This is a simple, feature-complete extension. However, if you find bugs or have suggestions, feel free to open an issue or pull request.