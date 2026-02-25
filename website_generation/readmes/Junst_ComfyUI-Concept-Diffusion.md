# ComfyUI-Concept-Diffusion
# 💥💥💥Fixing Now!!!💥💥💥
ComfyUI custom node implementation of ConceptAttention: Diffusion Transformers Learn Highly Interpretable Features.

This node allows you to generate high-quality saliency maps that precisely locate textual concepts within images using diffusion transformer attention layers.

## Features

- **ConceptAttention Node**: Extract concept embeddings from diffusion transformer attention layers
- **Saliency Map Generation**: Generate precise saliency maps for textual concepts
- **Zero-shot Segmentation**: Perform zero-shot semantic segmentation using concept attention
- **Multi-concept Support**: Handle multiple concepts simultaneously
- **Video Support**: Works with video generation models (CogVideoX)
- **Visualization Tools**: Overlay attention maps on original images
- **Flexible Thresholding**: Multiple threshold methods for saliency maps

## Installation

1. Clone this repository to your ComfyUI custom_nodes folder:
   ```bash
   git clone https://github.com/Junst/ComfyUI-Concept-Diffusion.git
   cd ComfyUI-Concept-Diffusion
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Restart ComfyUI

## Nodes

### ConceptAttentionNode
Main node for generating concept attention maps from diffusion models.

**Inputs:**
- `model`: Diffusion model (MODEL)
- `clip`: CLIP text encoder (CLIP)
- `image`: Input image (IMAGE)
- `concepts`: Comma-separated list of concepts (STRING)
- `num_inference_steps`: Number of inference steps (INT)
- `seed`: Random seed (INT, optional)

**Outputs:**
- `concept_maps`: Generated concept attention maps (CONCEPT_MAPS)
- `visualized_image`: Visualization of all concept maps (IMAGE)

### ConceptSaliencyMapNode
Extract individual concept saliency maps and convert to masks.

**Inputs:**
- `concept_maps`: Concept attention maps (CONCEPT_MAPS)
- `concept_name`: Name of concept to extract (STRING)
- `threshold`: Threshold for mask generation (FLOAT)

**Outputs:**
- `mask`: Binary mask for the concept (MASK)
- `saliency_image`: Saliency map visualization (IMAGE)

### ConceptSegmentationNode
Perform zero-shot semantic segmentation using concept attention.

**Inputs:**
- `concept_maps`: Concept attention maps (CONCEPT_MAPS)
- `image`: Original image (IMAGE)
- `concepts`: List of concepts for segmentation (STRING)

**Outputs:**
- `segmentation_mask`: Segmentation mask (MASK)
- `segmented_image`: Colored segmentation result (IMAGE)

### ConceptAttentionVisualizerNode
Visualize concept attention maps overlaid on the original image.

**Inputs:**
- `concept_maps`: Concept attention maps (CONCEPT_MAPS)
- `image`: Original image (IMAGE)
- `overlay_alpha`: Transparency of overlay (FLOAT)

**Outputs:**
- `visualized_image`: Image with attention overlay (IMAGE)

## Usage Example

1. Load an image using `LoadImage` node
2. Load a diffusion model (Flux, SD3, etc.) using `CheckpointLoaderSimple`
3. Connect the model, CLIP, and image to `ConceptAttentionNode`
4. Specify concepts like "person, car, tree, sky, building"
5. Use `ConceptSaliencyMapNode` to extract specific concept maps
6. Use `ConceptSegmentationNode` for zero-shot segmentation
7. Use `ConceptAttentionVisualizerNode` for visualization
8. Save results using `SaveImage` nodes

## Example Workflow

See `example_workflow.json` for a complete ComfyUI workflow example.

## Testing

Run the test script to verify the nodes work correctly:

```bash
python test_nodes.py
```

## Technical Details

This implementation is based on the ConceptAttention paper which shows that:

1. Multi-modal diffusion transformers (DiTs) have rich representations
2. Linear projections in the attention output space produce sharper saliency maps
3. Concept embeddings can be extracted without additional training
4. The method works for both image and video generation models

## Supported Models

- Flux (Flux1-dev, Flux1-schnell)
- Stable Diffusion 3/3.5
- CogVideoX (for video)
- Other DiT-based diffusion models

## Based on

[ConceptAttention: Diffusion Transformers Learn Highly Interpretable Features](https://arxiv.org/pdf/2502.04320)

## License

MIT License
