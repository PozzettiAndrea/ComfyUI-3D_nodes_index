# Pixstri ComfyUI Comics

Pixstri is a custom plugin for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) designed to generate comic pages. It provides a hierarchical node system that allows you to create comic layouts with rows and frames, making it easy to design and preview comic pages within your ComfyUI workflows.

## Features

- **Hierarchical Comic Layout System**:
  - **Page Node**: The top-level container for your comic page
    - Accepts multiple Row nodes as input
    - Provides image preview of the entire page layout
  - **Row Node**: Organizes frames horizontally in a row
    - Accepts multiple Frame nodes as input
    - Provides image preview of the row layout
  - **Frame Node**: Individual comic panels
    - Accepts images as input
    - Provides image preview of the frame

## Installation

### Option 1: Install via ComfyUI Manager (Recommended)

If you have [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager) installed:

1. Open ComfyUI
2. Go to the "Manager" tab
3. Search for "Pixstri"
4. Click "Install"

### Option 2: Manual Installation

1. Clone this repository into your ComfyUI custom_nodes directory:
   ```bash
   cd /path/to/ComfyUI/custom_nodes
   git clone https://github.com/yourusername/pixstri.git
   ```

2. Restart ComfyUI

## Usage

### Creating a Comic Page

1. **Start with Frame Nodes**:
   - Add Frame nodes to your workflow
   - Connect images to each Frame node
   - Adjust frame properties as needed

2. **Create Rows with Row Nodes**:
   - Add Row nodes to your workflow
   - Connect Frame nodes to each Row node
   - Arrange frames horizontally within each row

3. **Assemble the Page**:
   - Add a Page node to your workflow
   - Connect Row nodes to the Page node
   - The complete comic page will be output

Each node provides an image preview of its current state, allowing you to see how individual frames, rows, and the final page will look.

## Examples

### Basic Comic Page Layout

![Example Comic Workflow](https://via.placeholder.com/800x400?text=Comic+Page+Example+(Replace+with+actual+screenshot))

## Requirements

- ComfyUI
- PyTorch
- NumPy
- Pillow (PIL)

## License

MIT

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

