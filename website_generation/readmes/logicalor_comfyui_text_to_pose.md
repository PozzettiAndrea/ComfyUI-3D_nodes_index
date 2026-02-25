# ComfyUI Text-to-Pose Nodes

Generate human poses from text descriptions using the T2P Transformer model, then use them to guide image generation with ControlNet.

Based on the paper ["From Text to Pose to Image: Improving Diffusion Model Control and Quality"](https://arxiv.org/abs/2411.12872) (NeurIPS 2024 Workshop).

## Features

- **Text to Pose Generation**: Convert natural language descriptions into DWPose format poses
- **Multi-Person Support**: Generate up to 5 people in a single image
- **Batch Generation**: Create multiple pose variations from a single prompt
- **ControlNet Compatible**: Output works with any OpenPose ControlNet model
- **Raw Keypoints Output**: Access pose keypoints for advanced workflows

## Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Click "Install Custom Nodes"
3. Search for "Text-to-Pose" 
4. Click Install
5. Restart ComfyUI

The install script will automatically clone the required `text-to-pose` library.

### Method 2: Manual Installation

```bash
# Navigate to ComfyUI custom_nodes folder
cd ComfyUI/custom_nodes

# Clone this repository
git clone https://github.com/YOUR_USERNAME/comfyui-text-to-pose
cd comfyui-text-to-pose

# Run the install script (clones t2p library automatically)
python install.py

# Or manually:
# git clone https://github.com/clement-bonnet/text-to-pose t2p_repo
# ln -s t2p_repo/t2p t2p

# Install dependencies
pip install -r requirements.txt

# Restart ComfyUI
```

### Method 3: ComfyUI Registry (comfy-cli)

```bash
# Install comfy-cli if not already installed
pip install comfy-cli

# Install the node pack
comfy node registry-install comfyui-text-to-pose
```

## Nodes

### T2P Model Loader
Loads the Text-to-Pose transformer model from HuggingFace. Models are stored locally in ComfyUI's `models/t2p/` directory.

| Input | Type | Description |
|-------|------|-------------|
| model_name | dropdown | Model to load (default: t2p-transformer-v0) |
| device | dropdown | Device to load model on (auto/cuda/cpu) |
| force_cpu | boolean | Force CPU mode (slower but more compatible) |

| Output | Type | Description |
|--------|------|-------------|
| t2p_model | T2P_MODEL | Loaded model for use with generator nodes |

### Text to Pose
Generates a pose image from a text prompt. The number of people is automatically determined from the prompt (up to 5).

| Input | Type | Description |
|-------|------|-------------|
| t2p_model | T2P_MODEL | Model from T2P Model Loader |
| prompt | string | Text description of desired pose |
| width | int | Output image width (256-2048) |
| height | int | Output image height (256-2048) |
| seed | int | Random seed for reproducibility |
| bbox_temperature | float | Bounding box sampling temperature (0.01-2.0) |
| pose_temperature | float | Pose sampling temperature (0.01-2.0) |

| Output | Type | Description |
|--------|------|-------------|
| pose_image | IMAGE | Rendered pose visualization |
| pose_keypoints | POSE_KEYPOINTS | Raw keypoints data |

### Text to Pose (Batch)
Generates multiple pose variations from a single prompt. Useful for exploring different interpretations of the same description.

| Input | Type | Description |
|-------|------|-------------|
| t2p_model | T2P_MODEL | Model from T2P Model Loader |
| prompt | string | Text description of desired pose |
| width | int | Output image width (256-2048) |
| height | int | Output image height (256-2048) |
| batch_size | int | Number of variations to generate (1-16) |
| seed | int | Random seed for reproducibility |
| bbox_temperature | float | Bounding box sampling temperature (0.01-2.0) |
| pose_temperature | float | Pose sampling temperature (0.01-2.0) |

| Output | Type | Description |
|--------|------|-------------|
| pose_images | IMAGE | Batch of pose images |

## Example Workflows

### Basic Text to Pose
```
[T2P Model Loader] → [Text to Pose] → [Preview Image]
```

### Pose-Controlled Image Generation with ControlNet (Works with SD 1.5 and SDXL)

The pose image from Text to Pose is compatible with any OpenPose ControlNet model. This is the **recommended approach** for most users:

```
┌─────────────────────┐     ┌──────────────────────────┐
│  Load Checkpoint    │     │  Load ControlNet Model   │
│  (SD 1.5 or SDXL)   │     │  (OpenPose ControlNet)   │
└────────┬────────────┘     └────────────┬─────────────┘
         │                               │
         ▼                               ▼
┌─────────────────────┐     ┌──────────────────────────┐
│   T2P Model Loader  │     │                          │
└────────┬────────────┘     │                          │
         │                  │                          │
         ▼                  │                          │
┌─────────────────────┐     │    Apply ControlNet      │
│    Text to Pose     │────▶│                          │
│ "a dancer jumping"  │     │    strength: 0.8         │
└─────────────────────┘     └────────────┬─────────────┘
                                         │
         ┌───────────────────────────────┘
         ▼
┌─────────────────────┐
│      KSampler       │◄── positive/negative CONDITIONING
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│     VAE Decode      │
└────────┬────────────┘
         │
         ▼
    [Output Image]
```

**Recommended ControlNet Models:**
- **SD 1.5:** `control_v11p_sd15_openpose` 
- **SDXL:** `controlnet-openpose-sdxl-1.0`

**Node Connections:**
1. `Text to Pose` → `pose_image` output connects to `Apply ControlNet` → `image` input
2. `Load ControlNet Model` → connects to `Apply ControlNet` → `control_net` input  
3. `Apply ControlNet` → `CONDITIONING` outputs connect to `KSampler`

## Example Prompts

- "a person standing with arms raised above their head"
- "two people dancing together"
- "a woman sitting cross-legged on the floor"
- "a man running to the left"
- "a person doing a yoga tree pose"
- "three friends taking a group photo"

## Tips

### Temperature Settings
- **Lower temperature (0.05-0.1)**: More deterministic, consistent poses
- **Higher temperature (0.3-0.5)**: More variety, useful for batch generation
- **Very high temperature (>1.0)**: May produce unusual/unrealistic poses

### Multi-Person Scenes
- The model automatically determines the number of people from your prompt
- Supports up to 5 people per image
- Use descriptive prompts like "two people dancing" or "a group of friends"
- Works best with prompts that clearly describe multiple people

### Integration with Existing Workflows
- The pose image output is compatible with any ControlNet/OpenPose workflow
- POSE_KEYPOINTS output can be converted to other formats if needed

## Requirements

- Python 3.9+
- PyTorch 2.0+
- transformers
- huggingface_hub
- Pillow
- numpy

## Model Information

| Model | HuggingFace ID | Size |
|-------|----------------|------|
| T2P Transformer | clement-bonnet/t2p-transformer-v0 | ~150MB |

Models are automatically downloaded from HuggingFace on first use and cached locally in `ComfyUI/models/t2p/`.

## Credits

- Original paper and code: [clement-bonnet/text-to-pose](https://github.com/clement-bonnet/text-to-pose)
- Paper: "From Text to Pose to Image: Improving Diffusion Model Control and Quality"
- Authors: Clément Bonnet et al. (NeurIPS 2024 Workshop on Compositional Learning)

## License

This ComfyUI integration follows the license of the original text-to-pose repository.
