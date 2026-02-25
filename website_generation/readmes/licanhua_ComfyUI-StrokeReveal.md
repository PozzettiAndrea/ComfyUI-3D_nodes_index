# ComfyUI-StrokeReveal

A ComfyUI custom node that creates an animated stroke reveal effect, where a brush/pen follows a mask edge to reveal an image underneath.

![Demo](assets/demo.gif)

## Example Workflow

The example workflow is available in the ComfyUI template browser under **Workflow → Browse Templates → ComfyUI-StrokeReveal**.

You can also find it directly at [example_workflows/StrokeReveal.json](example_workflows/StrokeReveal.json).

## Features

- Reveals a static image through an animated pen stroke effect
- Pen tip follows the mask edge during animation
- Supports 8 different drawing directions
- Feathered edge blending for smooth transitions
- Customizable number of frames and pen scale

## Installation

1. Clone or download this repository into your `ComfyUI/custom_nodes/` folder
2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Restart ComfyUI

## Node: Stroke Reveal Animation

### Inputs

| Input | Type | Description |
|-------|------|-------------|
| **static_image** | IMAGE | The image to be revealed |
| **mask** | MASK | The mask area defining where the reveal happens |
| **background_image** | IMAGE | The background shown before reveal |
| **pen_tip** | IMAGE | PNG image of the pen tip (with transparency) |
| **num_frames** | INT | Number of frames in the animation (2-500, default: 30) |
| **draw_direction** | ENUM | Direction of the reveal animation |
| **feather_radius** | INT | Blur radius for edge feathering (0-100, default: 10) |
| **pen_scale** | FLOAT | Scale factor for the pen tip (0.1-5.0, default: 1.0) |

### Draw Directions

- `left_to_right` (default)
- `right_to_left`
- `top_to_bottom`
- `bottom_to_top`
- `top_left_to_bottom_right`
- `top_right_to_bottom_left`
- `bottom_left_to_top_right`
- `bottom_right_to_top_left`

### Output

| Output | Type | Description |
|--------|------|-------------|
| **images** | IMAGE | Batch of frames showing the reveal animation |

## How It Works

1. At the beginning, the mask area is filled with the background image with a feathered edge
2. As the animation progresses, the pen tip moves along the mask edge
3. The area behind the pen tip is progressively revealed with the static image
4. The final frame shows the complete static image

## Example Workflow

1. Load your static image
2. Create or load a mask defining the reveal area
3. Load a background image
4. Load a pen tip PNG with transparency
5. Connect all inputs to the Stroke Reveal Animation node
6. Set desired number of frames and direction
7. Connect output to a video/GIF encoder or preview

## License

MIT License
