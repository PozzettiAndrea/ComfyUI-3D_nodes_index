# WarpPipe - ComfyUI Custom Nodes

<p align="center">
  <img src="banner.png" alt="WarpPipe Banner">
</p>

WarpPipe is a set of custom nodes for ComfyUI that provides a data bundling and transfer system. It allows you to package multiple data types (models, conditioning, images, parameters, etc.) into a single "warp" object that can be passed between nodes and unpacked later in your workflow -- like a Super Mario warp pipe for your data.

## Why WarpPipe?

If you've ever built a complex ComfyUI workflow, you know the pain: dozens of connections criss-crossing your canvas, making it impossible to read or maintain. WarpPipe solves this by letting you **bundle everything into a single wire**.

- **Clean workflows**: Replace 20+ tangled connections with one clean Warp-to-Unwarp link. Your workflow becomes readable at a glance.
- **Fast model switching**: Set up multiple Warp nodes -- one per model/style -- each with its own settings (steps, CFG, scheduler, sampler, resolution). Switch between them instantly by connecting a different Warp to your Unwarp.
- **Flexible and modular**: Build reusable workflow sections that accept and return warp bundles. Change one part without touching the rest.
- **No data loss**: Every standard ComfyUI type is supported -- models, CLIP, VAE, conditioning, images, latents, prompts, and all sampling parameters travel together.

## Features

- **Warp Node**: Bundles multiple ComfyUI data types into a single transferable object
- **Unwarp Node**: Unpacks the bundled data back into individual outputs
- **Warp Provider**: Generates latents and parameters with 30+ resolution presets
- **FD Scheduler Adapter**: Converts KSampler schedulers to FaceDetailer-compatible schedulers
- **Dead End Node**: Accepts any input type but produces no output -- perfect for debugging
- **Chain-able**: Warp nodes can copy and extend data from other warp nodes
- **Scheduler Compatibility**: Automatic coercion of exotic schedulers to safe values

## Installation

### Method 1: Comfy Registry (Recommended)

```bash
comfy node install warppipe
```

### Method 2: ComfyUI Manager

1. Open ComfyUI Manager
2. Search for "WarpPipe"
3. Click Install

### Method 3: Manual (git clone)

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/gregory-richard/ComfyUI-WarpPipe.git
```

Restart ComfyUI after installation.

## Nodes

### Warp Node

**Category**: `Custom/WarpPipe Nodes` | **Display Name**: Warp Bundle

Bundles multiple data types into a single "warp" object.

**Inputs** (all optional):

- `warp`: Copy data from an existing warp object (WARPPIPE type)
- `model_1`, `model_2`: MODEL objects (e.g. checkpoints, LoRA-modified models)
- `clip`: CLIP encoder
- `clip_vision`: CLIP_VISION encoder
- `vae`: VAE model
- `conditioning_positive`, `conditioning_negative`: CONDITIONING inputs
- `image`: IMAGE batch
- `mask`: MASK input
- `latent`: LATENT data
- `prompt_positive`, `prompt_negative`: Text prompts (STRING)
- `batch_size`, `seed`, `steps_1`, `steps_2`, `steps_3`, `width`, `height`: Integer parameters
- `cfg`: CFG scale (FLOAT)
- `sampler_name`: Sampler selection (matches KSampler)
- `scheduler`: Scheduler selection (matches KSampler)

**Output**:

- `warp`: Bundled data object (WARPPIPE type)

### Unwarp Node

**Category**: `Custom/WarpPipe Nodes` | **Display Name**: Unwarp Bundle

Unpacks a warp object back into individual data types.

**Input**:

- `warp`: The warp object to unpack (WARPPIPE type) -- optional, returns None values if not connected

**Outputs** (in order):

- `model_1`, `model_2`: MODEL objects
- `image`: IMAGE
- `mask`: MASK
- `clip`: CLIP
- `clip_vision`: CLIP_VISION
- `vae`: VAE
- `conditioning_positive`, `conditioning_negative`: CONDITIONING
- `latent`: LATENT
- `prompt_positive`, `prompt_negative`: STRING
- `batch_size`, `seed`, `steps_1`, `steps_2`, `steps_3`: INT
- `cfg`: FLOAT
- `sampler_name`: Sampler enum
- `scheduler`: Scheduler enum
- `width`, `height`: INT

### Warp Provider Node

**Category**: `Custom/WarpPipe Nodes` | **Display Name**: Warp Provider

Generates latents and parameters with convenient preset dimensions. Features 30+ resolution presets covering all major aspect ratios (9:16, 3:4, 2:3, 4:5, 1:1, 5:4, 3:2, 4:3, 16:9), each labeled with use case, aspect ratio, resolution, and megapixel count.

**Inputs** (all optional):

- `batch_size`: Number of images (default: 1, range: 1-64)
- `seed`: Random seed (default: 0)
- `steps_1`: Primary sampling steps (default: 20, range: 1-200)
- `steps_2`, `steps_3`: Additional step counts for multi-pass workflows (default: 0)
- `cfg`: CFG scale (default: 7.0, range: 0.0-50.0)
- `sampler_name`: Sampler to use (default: "euler")
- `scheduler`: Scheduler to use (default: "normal")
- `size_preset`: Resolution preset dropdown (30+ options, default: Square SDXL native 1024x1024)
- `custom_width`, `custom_height`: Custom dimensions when "Custom" preset is selected (step: 8)

**Outputs**:

- `latent`: Generated empty latent at selected resolution
- `batch_size`, `seed`, `steps_1`, `steps_2`, `steps_3`, `width`, `height`: INT
- `cfg`: FLOAT
- `sampler_name`: Sampler enum
- `scheduler`: Scheduler enum

### FD Scheduler Adapter Node

**Category**: `Custom/WarpPipe Nodes` | **Display Name**: FD Scheduler Adapter

Converts KSampler schedulers to FaceDetailer-compatible schedulers. Exotic schedulers (AYS SDXL, GITS, OSS variants, etc.) are automatically mapped to their closest compatible equivalent.

**Input**:

- `scheduler`: KSampler scheduler type (required)

**Output**:

- `scheduler`: FaceDetailer-compatible scheduler

### Dead End Node

**Category**: `Custom/WarpPipe Nodes` | **Display Name**: Dead End

A true dead end node that accepts any input type but produces no output. Does not trigger execution.

**Input**:

- `input`: Any data type (wildcard) -- optional

**Output**: None

**Use Cases**:

- **Debugging**: Temporarily disconnect a workflow branch without deleting nodes
- **Workflow organization**: Cleanly terminate unused output paths
- **Testing**: Isolate parts of complex workflows during development

## Usage Examples

### Basic Usage

1. Add a **Warp** node to your workflow
2. Connect your models, conditioning, and other data to the Warp node inputs
3. Connect the Warp output to an **Unwarp** node
4. Use the Unwarp outputs in the rest of your workflow

### Using Warp Provider

1. Add a **Warp Provider** node to generate latents and parameters
2. Choose from 30+ presets organized by aspect ratio, or use custom sizes
3. Connect the outputs directly to your sampling nodes or bundle them with a **Warp** node

### Chaining Warps

```
[Model] --> [Warp A] --> [Some Processing] --> [Warp B] --> [Unwarp] --> [KSampler]
                ^                                  ^
          [Additional Data]                  [More Data]
```

Warp B copies all data from Warp A and adds additional data, creating a cumulative bundle.

### FaceDetailer Compatibility

```
[KSampler Scheduler] --> [FD Scheduler Adapter] --> [FaceDetailer Node]
```

### Debugging with Dead End

```
[Model] --> [KSampler] --> [Dead End]
                       \-> [VAE Decode] --> [Save Image]
```

Use the Dead End node to temporarily disable a branch while keeping the rest active.

### Example Workflow

Here's a real workflow using WarpPipe with multiple model configurations:

<p align="center">
  <img src="examples/workflow_example.png" alt="WarpPipe Example Workflow" width="800">
</p>

Download the [example workflow JSON](examples/workflow_example.json) and drag it into ComfyUI to try it out.

## Technical Details

- **Data Types**: Custom `WARPPIPE` type for bundled data transfer between Warp and Unwarp nodes
- **Data Storage**: Global storage with unique UUIDs per warp instance, thread-safe with locking
- **Memory Management**: Automatic time-based cleanup (1-hour expiry) with a 256-entry hard cap
- **Scheduler Compatibility**: Automatic coercion of exotic schedulers to safe, compatible values
- **Preset Dimensions**: 30+ SDXL-optimized resolution presets across all major aspect ratios
- **Logging**: Uses Python `logging` module (set to DEBUG level to see internal details)

## Troubleshooting

### Node Not Appearing

- Ensure you've restarted ComfyUI after installation
- Check the console for any error messages during startup
- Verify all files are in the correct directory

### Migrating from v2.x

v3.0.0 renamed the internal data type from `CONTROL` to `WARPPIPE`. If you load an old workflow, you may need to reconnect the Warp-to-Unwarp links once. All node names and functionality remain the same.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details
