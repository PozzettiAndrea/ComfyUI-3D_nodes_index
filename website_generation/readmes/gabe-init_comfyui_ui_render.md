# ComfyUI HTML Renderer Node

A custom node for ComfyUI that renders HTML content directly within the node interface, enabling rich text display, formatted output, and interactive content visualization.

## Features

- Render HTML content inside ComfyUI nodes
- Support for CSS styling
- JavaScript execution capability
- Live updates when connected to dynamic HTML sources
- Isolated iframe rendering for security
- Responsive sizing within node boundaries

## Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yourusername/comfyui_ui_render
```

2. Restart ComfyUI (no additional dependencies required)

## Usage

The HTML Renderer node accepts HTML content as input and displays it within an embedded iframe in the node interface.

### Basic Example

1. Add an "HTML Renderer" node to your workflow
2. Connect any node that outputs HTML strings
3. The HTML content will be rendered inside the node

### Input

- **html**: HTML string input (must be connected from another node)

### Use Cases

1. **Rich Text Display**: Show formatted text, tables, or styled content
2. **Data Visualization**: Render charts or graphs generated as HTML
3. **Progress Indicators**: Display custom progress bars or status updates
4. **Debug Output**: Show formatted debug information
5. **Interactive Forms**: Create simple interactive elements

## Example HTML Content

```html
<div style="padding: 10px; font-family: Arial;">
    <h3>Results</h3>
    <p>Processing complete!</p>
    <ul>
        <li>Items processed: 100</li>
        <li>Success rate: 95%</li>
    </ul>
</div>
```

## Advanced Features

### CSS Support

Include CSS directly in your HTML:
```html
<style>
    .status { 
        color: green; 
        font-weight: bold; 
    }
</style>
<div class="status">Ready</div>
```

### JavaScript Support

The iframe supports JavaScript execution:
```html
<script>
    document.body.style.backgroundColor = '#f0f0f0';
</script>
```

## Security Notes

- Content is rendered in an isolated iframe
- No access to parent ComfyUI interface
- Scripts run in a sandboxed environment

## Limitations

- Height is determined by content (no fixed height)
- Some advanced JavaScript features may be restricted
- External resource loading depends on CORS policies

## Technical Details

The node uses ComfyUI's DOM widget system to embed an iframe that updates whenever new HTML content is received. The implementation includes:

- Frontend JavaScript extension for DOM manipulation
- Backend Python node for HTML input handling
- Automatic iframe updates on execution

## Troubleshooting

- **Content not showing**: Ensure HTML input is properly connected
- **Styling issues**: Check for CSS conflicts or missing styles
- **JavaScript errors**: Open browser console for debugging

## Requirements

- ComfyUI (no additional Python packages needed)
- Modern web browser with iframe support

## License

MIT License

Copyright (c) 2024 

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.