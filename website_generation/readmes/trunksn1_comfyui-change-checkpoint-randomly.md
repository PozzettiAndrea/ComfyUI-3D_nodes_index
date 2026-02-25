# ComfyUI Checkpoint Rotation Node

A custom node for ComfyUI that enables automatic checkpoint rotation during batch image generation. This allows you to generate images using multiple different model checkpoints in a single workflow, automatically switching between them based on your specified interval.

## Features

- **Automatic Checkpoint Rotation**: Switch between checkpoints every N images
- **Subfolder Selection**: Choose checkpoints from specific subfolders in your models directory
- **Multiple Rotation Modes**:
  - **Sequential**: Cycle through checkpoints in order
  - **Random**: Randomly select checkpoints (with seed for reproducibility)
  - **Shuffle**: Randomize order once, then cycle through
- **Checkpoint Filtering**: Filter checkpoints by name pattern
- **Batch Index Tracking**: Helper nodes to track generation progress
- **Smart Caching**: Efficient checkpoint discovery with caching

## Use Case Example

Generate 20 images with checkpoint changes every 4 images:
- **Batch Count**: 20 images
- **Change Interval**: 4 images
- **Result**: 5 different checkpoints used (changing every 4 images)

## Installation

### Method 1: Git Clone (Recommended)

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/trunksn1/comfyui-change-checkpoint-randomly.git
```

3. Restart ComfyUI

### Method 2: Manual Installation

1. Download this repository as ZIP
2. Extract to `ComfyUI/custom_nodes/comfyui-change-checkpoint-randomly/`
3. Restart ComfyUI

### Verify Installation

After restarting ComfyUI, you should see these new nodes in the node menu:
- `Checkpoint Rotation Loader` (under **loaders**)
- `Batch Index Counter` (under **utils**)
- `Simple Counter` (under **utils**)

Look for the success message in the console:
```
[ComfyUI] Checkpoint Rotation Node loaded successfully!
```

## Node Reference

### 1. Checkpoint Rotation Loader

The main node that loads checkpoints with rotation logic.

**Location**: Add Nodes → loaders → Checkpoint Rotation Loader

**Inputs**:
- **subfolder** (STRING): Path to checkpoint subfolder relative to `models/checkpoints/`
  - Leave empty `""` to use root checkpoints folder
  - Example: `"sd15"`, `"sdxl/anime"`, `"realistic"`
- **change_interval** (INT): Number of images to generate before switching checkpoint
  - Default: `1`
  - Example: `4` means change checkpoint every 4 images
- **batch_index** (INT): Current position in batch generation
  - Connect to `Batch Index Counter` node for automatic tracking
  - Manual: increment this value in your workflow
- **rotation_mode** (COMBO): How to select the next checkpoint
  - `sequential`: Cycle through in alphabetical order
  - `random`: Random selection (seed-based)
  - `shuffle`: Shuffle list once, then cycle
- **seed** (INT): Random seed for `random` and `shuffle` modes
  - Same seed = same checkpoint sequence
  - Different seed = different sequence
- **checkpoint_filter** (STRING, optional): Filter checkpoints by name
  - Example: `"anime"` only loads checkpoints with "anime" in filename
  - Case-insensitive substring match

**Outputs**:
- **model**: Loaded model (connect to KSampler)
- **clip**: CLIP model (connect to CLIP Text Encode)
- **vae**: VAE model (connect to VAE Decode)
- **checkpoint_name**: Name of current checkpoint (for display/logging)
- **info**: Detailed information about current rotation state

### 2. Batch Index Counter

Helper node to automatically track and increment batch index.

**Location**: Add Nodes → utils → Batch Index Counter

**Inputs**:
- **action** (COMBO): What to do with the counter
  - `increment`: Add to counter
  - `set`: Set to specific value
  - `reset`: Reset to 0
- **counter_id** (STRING, optional): Unique identifier for this counter
  - Default: `"default"`
  - Use different IDs for multiple independent counters
- **set_value** (INT): Value to set when action is "set"
- **increment_by** (INT): Amount to increment (default: 1)

**Outputs**:
- **batch_index**: Current counter value (connect to Checkpoint Rotation node)
- **info**: Information string about counter state

### 3. Simple Counter

Basic counter that outputs sequential numbers.

**Location**: Add Nodes → utils → Simple Counter

**Inputs**:
- **start** (INT): Starting value (default: 0)
- **step** (INT): Increment amount (default: 1)

**Outputs**:
- **value**: Current counter value

## Usage Examples

### Example 1: Basic Rotation with Loop

Generate 20 images, changing checkpoint every 4 images:

```
[Batch Index Counter]
  action: increment
  increment_by: 1
  └─→ batch_index

[Checkpoint Rotation Loader]
  subfolder: "sdxl"
  change_interval: 4
  batch_index: (from counter)
  rotation_mode: sequential
  └─→ model, clip, vae

[CLIP Text Encode (Positive)]
  clip: (from rotation loader)
  text: "your prompt"

[CLIP Text Encode (Negative)]
  clip: (from rotation loader)
  text: "negative prompt"

[KSampler]
  model: (from rotation loader)
  batch_size: 1  ← Important: use 1 for rotation to work
  └─→ latent

[VAE Decode]
  vae: (from rotation loader)
  samples: (from sampler)
  └─→ image

[Save Image]
  images: (from decoder)
```

**Workflow Notes**:
- Set KSampler `batch_size: 1` to generate images one at a time
- Wrap the entire workflow in a loop (20 iterations)
- Batch Index Counter automatically increments each iteration
- Checkpoint changes every 4 iterations (4, 8, 12, 16, 20)

### Example 2: Random Rotation with Seed Control

Same setup as Example 1, but with random checkpoint selection:

```
[Checkpoint Rotation Loader]
  subfolder: "realistic"
  change_interval: 5
  rotation_mode: random
  seed: 12345  ← Controls which checkpoints are selected
```

**Result**: Different seed values produce different checkpoint sequences, but the same seed always produces the same sequence.

### Example 3: Using Subfolder Filters

Load only specific checkpoint types:

```
[Checkpoint Rotation Loader]
  subfolder: "sdxl"
  checkpoint_filter: "turbo"  ← Only loads checkpoints with "turbo" in name
  change_interval: 2
  rotation_mode: sequential
```

### Example 4: Multiple Independent Counters

Use different counters for different purposes:

```
[Batch Index Counter A]
  counter_id: "main"
  action: increment
  └─→ for main checkpoint rotation

[Batch Index Counter B]
  counter_id: "secondary"
  action: increment
  increment_by: 2
  └─→ for different rotation speed
```

## Workflow Setup Guide

### Step-by-Step: Creating a Rotation Workflow

1. **Add Batch Index Counter**:
   - Right-click → Add Node → utils → Batch Index Counter
   - Set `action` to "increment"

2. **Add Checkpoint Rotation Loader**:
   - Right-click → Add Node → loaders → Checkpoint Rotation Loader
   - Connect `batch_index` output from counter to `batch_index` input
   - Set `subfolder` to your checkpoint folder (or leave empty for root)
   - Set `change_interval` to desired number (e.g., 4 for every 4 images)
   - Choose `rotation_mode` (sequential recommended for first try)

3. **Connect to Your Workflow**:
   - Connect `model` output to KSampler
   - Connect `clip` output to CLIP Text Encode nodes
   - Connect `vae` output to VAE Decode

4. **Set Up Loop** (Important!):
   - Use ComfyUI's loop nodes or queue multiple prompts
   - Set KSampler `batch_size: 1` (critical for rotation)
   - Loop for total number of images you want

5. **Run Workflow**:
   - Execute the workflow
   - Checkpoint will automatically rotate based on your settings
   - Watch console for rotation messages

## Troubleshooting

### No Checkpoints Found

**Problem**: Error message "No checkpoints found in: [folder]"

**Solutions**:
- Verify the subfolder path is correct relative to `models/checkpoints/`
- Check that checkpoint files exist in the folder (`.safetensors`, `.ckpt`, `.pt`, `.pth`)
- Leave `subfolder` empty to use root checkpoints folder
- Check console for exact error message

### Checkpoint Not Changing

**Problem**: Same checkpoint used for all images

**Solutions**:
- Verify `batch_index` is incrementing (check counter output)
- Set KSampler `batch_size: 1` (batches of images use same checkpoint)
- Ensure `change_interval` is less than total images
- Check that multiple checkpoints exist in selected folder

### Path/Import Errors

**Problem**: Module import errors on startup

**Solutions**:
- Ensure all files are in correct locations
- Restart ComfyUI completely
- Check Python path has no special characters
- Verify file permissions are correct

### Model Loading Errors

**Problem**: "Failed to load checkpoint" errors

**Solutions**:
- Verify checkpoint files are not corrupted
- Ensure sufficient disk space
- Check that checkpoint is compatible with ComfyUI
- Try loading checkpoint manually with default loader first

## Folder Structure

```
comfyui-change-checkpoint-randomly/
├── __init__.py              # Main node registration
├── nodes/
│   ├── __init__.py
│   ├── checkpoint_rotation.py   # Main rotation logic
│   └── batch_counter.py         # Counter helpers
├── utils/
│   ├── __init__.py
│   ├── checkpoint_utils.py      # Checkpoint operations
│   └── path_utils.py            # Path handling
├── examples/
│   └── example_workflow.json    # Example workflow
├── README.md                    # This file
└── IMPLEMENTATION_PLAN.md       # Development plan
```

## Technical Details

### How Rotation Works

The node calculates which checkpoint to use based on:

```python
rotation_index = (batch_index // change_interval) % num_checkpoints
```

**Example**:
- 5 checkpoints available: `[A, B, C, D, E]`
- `change_interval = 4`
- Batch indices 0-3: checkpoint A
- Batch indices 4-7: checkpoint B
- Batch indices 8-11: checkpoint C
- And so on...

### Supported File Types

- `.safetensors` (recommended)
- `.ckpt`
- `.pt`
- `.pth`

### Performance Notes

- **Caching**: Checkpoint lists are cached per subfolder for performance
- **Memory**: Only one checkpoint loaded at a time
- **Scanning**: Recursive folder scanning may be slow with many files

## Roadmap / Future Features

- [ ] Visual checkpoint selector UI
- [ ] Checkpoint preview thumbnails
- [ ] Weighted rotation (use some checkpoints more than others)
- [ ] Conditional rotation based on quality metrics
- [ ] Multi-folder support
- [ ] Checkpoint metadata display
- [ ] Generation history tracking
- [ ] Integration with ComfyUI Manager

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Support

- **Issues**: Report bugs on [GitHub Issues](https://github.com/trunksn1/comfyui-change-checkpoint-randomly/issues)
- **Discussions**: Ask questions in GitHub Discussions
- **ComfyUI Discord**: Get help from the community

## License

MIT License - See LICENSE file for details

## Credits

- **Author**: Claude AI Assistant
- **Version**: 1.0.0
- **Created**: 2025-11-05

## Changelog

### Version 1.0.0 (2025-11-05)
- Initial release
- Checkpoint rotation with multiple modes
- Batch index tracking
- Subfolder and filter support
- Comprehensive documentation

---

**Note**: This node requires a workflow setup that generates images iteratively (one at a time or in small batches). Using large batch sizes in KSampler will use the same checkpoint for the entire batch. Use loops or queue multiple prompts for best results.
