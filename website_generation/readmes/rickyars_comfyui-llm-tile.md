# Tiled Image Generator for ComfyUI

A ComfyUI node that generates tiled image compositions with overlapping regions. This approach creates coherent compositions by using the edges of each tile as seeds for neighboring tiles, resulting in seamless transitions.

## Features

- Generate multi-tile image compositions with proper overlapping and seeding
- Configure grid dimensions, tile sizes, and overlap percentages
- Feathering options for smooth transitions between tiles
- Create seamless tiled images in X or Y
- Template generator for easier prompt creation

## Installation

1. Clone this repository into your ComfyUI custom_nodes folder:
   ```
   cd ComfyUI/custom_nodes
   git clone https://github.com/rickyars/comfyui-llm-tile.git
   ```

2. Restart ComfyUI or reload the UI

## Usage

The node system includes two main components:

1. **Tile Prompt Template**: Generates a template JSON structure that you can customize with individual tile prompts.
2. **Tiled Image Generator**: The main node that generates the complete tiled composition.

### Workflow:

1. Use the Tile Prompt Template node to generate an initial JSON template
2. Customize the prompts for each tile as needed
3. Connect the JSON output to the Tiled Image Generator node
4. Configure your desired grid and tile settings
5. Run the workflow to generate your tiled composition

## Example

This node was inspired by the "Tiled LLM composition" technique where an LLM (like Claude) is asked to think of a pleasing overall composition and then describe what should go in each tile.

## Parameters

- **grid_width/height**: Number of tiles in each dimension
- **tile_width/height**: Size of each generated tile in pixels
- **overlap_percent**: How much tiles should overlap (0.0-0.5, recommended: 0.15-0.25)
- **blend_sigma**: Controls the Gaussian blend smoothness (0.1-1.0):
  - Lower values (0.1-0.3): Sharper transitions
  - Medium values (0.4-0.6): Balanced blending for most content
  - Higher values (0.7-1.0): Very gradual transitions for difficult content
- **base_seed**: Starting seed for the generation sequence
- **seamlessX/seamlessY**: Make image edges seamless tiles in X or Y (Minimum of 2 tiles)
  
## License

MIT License
