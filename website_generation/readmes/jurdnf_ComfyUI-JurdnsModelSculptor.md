# ComfyUI-JurdnsModelSculptor

A collection of ComfyUI nodes that "sculpt" diffusion models by applying gradient-based modifications to different layers and blocks. Transform your models with mathematical curves and shapes to create unique artistic effects, enhance details during upscaling, or experiment with creative model variations.

## What Does It Do?

Instead of traditional model merging that blends two models together, Model Sculptor applies mathematical gradient shapes across the layers of a single model. Think of it like applying a curve or wave pattern to the model's "depth" - making some layers stronger, others weaker, creating peaks and valleys of influence throughout the network. Best used in refinement or upscale stages for effective detailing.

## Use Cases

### 🔍 **Iterative Upscaling & Refining**
Use Model Sculptor in your upscaling workflows to enhance detail recovery. Apply different gradient shapes at different upscale stages to bring out fine details, textures, or specific artistic elements.

### 🎨 **Creative Model Merging Process**
Instead of traditional merging, use Model Sculptor as a preprocessing step before merging, or apply it to merged models to create unique variations that can't be achieved through conventional blending.

### ⚡ **Dynamic Workflow Enhancement**
Integrate into your existing workflows where you want the same base model to behave differently for specific tasks - portraits vs landscapes, detailed vs stylized, etc.

## Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/jurdnf/ComfyUI-JurdnsModelSculptor.git
   ```

Also found in the ComfyUI Manager.

3. Restart ComfyUI

The nodes will appear under **models/advanced** in your node browser.

## Available Nodes

- **Jurdn's Model Sculptor (Flux)** - For Flux.1 models
- **Jurdn's Model Sculptor (SDXL)** - For SDXL models  
- **Jurdn's Model Sculptor (SD3)** - For Stable Diffusion 3 models

Finetuned versions of the above architectures (such as Illustrious, because it is based on SDXL)

## How to Use

1. **Connect your model** from "Load Diffusion Model" directly to a Model Sculptor node
2. **Choose a gradient shape** that defines how the effect varies across layers
3. **Set the strength** (typically 0.05-0.3 for subtle effects, higher for dramatic changes)
4. **Select target blocks** to focus the effect on specific parts of the model
5. **Connect the output** to your sampler as usual

**Important**: Always connect directly from the model loader to avoid cumulative effects.

## Gradient Shapes Explained

Each shape creates a different "curve" of influence across your model's layers:

- **Linear (Ascending/Descending)** - Gradual ramp up or down
- **Ease In/Out (Quadratic)** - Smooth acceleration/deceleration curves  
- **Ease In/Out (Sine)** - Natural, smooth wave-like transitions
- **Spike (Gaussian)** - Sharp peak in the middle layers
- **Dip (Inverse Gaussian)** - Valley in the middle, emphasis on edges
- **Steps** - Discrete level changes across layers
- **Random (Noise)** - Unpredictable variations for experimental effects

## Target Blocks

### Flux Models
- **in_layers** - Input processing layers
- **double_blocks** - Main transformer blocks (0-18)
- **single_blocks** - Secondary transformer blocks (0-37)
- **Double & Single (Synced Shape)** - Apply same gradient to both block types

### SDXL Models  
- **input_blocks** - Downsampling path (0-11)
- **middle_block** - Bottleneck processing
- **output_blocks** - Upsampling path (0-11)
- **time_embed** - Timestep embeddings
- **label_emb** - Class/style embeddings
- **Input & Output (Synced Shape)** - Symmetrical application

### SD3 Models
- **joint_blocks** - Main DiT transformer blocks (0-23)
- **x_embedder** - Image embedding layers
- **y_embedder** - Text embedding layers
- **t_embedder** - Time embedding layers
- **pos_embed** - Positional embeddings
- **final_layer** - Output projection
- **Joint & Final (Synced Shape)** - Focus on core processing


## Tips & Best Practices

- **Start subtle** - Begin with strength values around 0.1 and adjust
- **Experiment with combinations** - Different shapes work better for different content
- **Use in upscaling** - Particularly effective during multi-stage upscaling workflows  
- **Connect directly** - Always connect from "Load Diffusion Model" to avoid stacking effects
- **Try different blocks** - Each block type affects different aspects of generation
