# ComfyUI Friendly Pipe

A ComfyUI custom node pack that provides flexible, user-friendly pipe nodes for bundling and unbundling multiple connections of any type.

## Features

- **Dynamic Slots**: Start with 1 slot and add up to 80 slots as needed
- **Custom Labels**: Name each slot for easy identification
- **Type Passthrough**: Connected types are preserved through the pipe, maintaining compatibility with typed inputs
- **Auto-Sync**: Output nodes automatically update to match the connected input node's configuration
- **Any Type Support**: Works with any ComfyUI data type (STRING, IMAGE, MODEL, CLIP, VAE, CONDITIONING, etc.)

## Installation

### Option 1: ComfyUI Manager (Recommended)

1. Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager) if you haven't already
2. Open ComfyUI and click on "Manager" in the menu
3. Click "Install Custom Nodes"
4. Search for "Friendly Pipe"
5. Click "Install" and restart ComfyUI

### Option 2: Clone into custom_nodes

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/logicalor/comfyui_friendly_pipe.git
```

### Option 3: Manual Installation

1. Download or clone this repository
2. Place the `comfyui-friendly-pipe` folder in your `ComfyUI/custom_nodes/` directory
3. Restart ComfyUI

## Nodes

### Friendly Pipe In

Bundles multiple inputs into a single pipe output.

**Features:**
- Add/remove input slots dynamically with the ➕/➖ buttons
- Label each slot with a custom name using the text fields
- Labels are reflected on the input slot names
- All connected data is bundled into a single `FRIENDLY_PIPE` output

**Usage:**
1. Add the "Friendly Pipe In" node to your workflow
2. Click "➕ Add Slot" to add more input slots (up to 80)
3. Optionally rename slots using the Label fields
4. Connect any node outputs to the input slots
5. Connect the `pipe` output to a "Friendly Pipe Out" node

### Friendly Pipe Out

Unpacks a pipe back into individual outputs.

**Features:**
- Automatically syncs slot count and labels with the connected "Friendly Pipe In" or "Friendly Pipe Edit" node
- Output slot types match the original input types
- Updates dynamically when the source node changes

**Usage:**
1. Add the "Friendly Pipe Out" node to your workflow
2. Connect the `pipe` input to a "Friendly Pipe In" or "Friendly Pipe Edit" node's output
3. The output slots will automatically match the input node's configuration
4. Connect the individual outputs to downstream nodes

### Friendly Pipe Edit

Extends an existing pipe by adding new slots while preserving the original slots.

**Features:**
- Takes an existing pipe as input and passes it through with additional slots
- Add/remove additional input slots dynamically with the ➕/➖ buttons
- Label each additional slot with a custom name
- Downstream "Friendly Pipe Out" nodes see all accumulated slots (original + new)
- Can be chained multiple times to progressively add more slots

**Usage:**
1. Add the "Friendly Pipe Edit" node to your workflow
2. Connect the `pipe` input to an existing "Friendly Pipe In" or another "Friendly Pipe Edit" node
3. Click "➕ Add Slot" to add additional input slots
4. Optionally rename slots using the Label fields
5. Connect node outputs to the new input slots
6. Connect the output `pipe` to a "Friendly Pipe Out" node or another "Friendly Pipe Edit"

## Example Workflows

### Basic Pipe

```
[String Node] ──→ slot_1 (text)     ┐
[Image Node]  ──→ slot_2 (image)    ├──→ [Friendly Pipe In] ──pipe──→ [Friendly Pipe Out] ──→ slot_1 (text)  ──→ [Show Text]
[Model Node]  ──→ slot_3 (model)    ┘                                                     ──→ slot_2 (image) ──→ [Preview Image]
                                                                                          ──→ slot_3 (model) ──→ [KSampler]
```

### Extended Pipe with Edit Node

```
[String Node] ──→ slot_1 ┐                                                                      
[Image Node]  ──→ slot_2 ├──→ [Friendly Pipe In] ──pipe──→ [Friendly Pipe Edit] ──pipe──→ [Friendly Pipe Out]
                         ┘                                  ↑                                   ├──→ slot_1 (original)
                                                   [VAE Node] ──→ slot_1 (vae)                  ├──→ slot_2 (original)
                                                   [CLIP Node] ──→ slot_2 (clip)                ├──→ slot_3 (vae - added)
                                                                                                └──→ slot_4 (clip - added)
```

## Use Cases

- **Workflow Organization**: Bundle related connections to reduce visual clutter
- **Subgraph Interfaces**: Create clean input/output interfaces for logical sections of your workflow
- **Reusable Templates**: Build reusable workflow sections with standardized pipe interfaces
- **Dynamic Workflows**: Easily add or remove connections without rewiring everything

## File Structure

```
comfyui-friendly-pipe/
├── __init__.py            # Node registration and exports
├── friendly_pipe_in.py    # FriendlyPipeIn node class
├── friendly_pipe_out.py   # FriendlyPipeOut node class
├── friendly_pipe_edit.py  # FriendlyPipeEdit node class
├── any_type.py            # AnyType class for universal type compatibility
├── js/
│   └── friendly_pipe.js   # Frontend JavaScript for dynamic UI
├── pyproject.toml         # ComfyUI Manager metadata
└── README.md
```

## Technical Details

### Type System

The nodes use a special `AnyType` class that is compatible with all ComfyUI types. This allows:
- Inputs to accept connections from any node type
- Outputs to connect to any typed input without validation errors

### Data Flow

1. **Friendly Pipe In** collects all connected inputs into a dictionary structure:
   ```python
   {
       "slot_count": 3,
       "slots": {1: <data>, 2: <data>, 3: <data>},
       "names": {1: "text", 2: "image", 3: "model"}
   }
   ```

2. **Friendly Pipe Out** unpacks this dictionary back into individual outputs

### Frontend Sync

The JavaScript frontend handles:
- Dynamic slot addition/removal using LiteGraph's `addInput()`/`removeInput()` methods
- Label synchronization between text widgets and slot labels
- Automatic notification of connected output nodes when configuration changes
- Type tracking for visual feedback

## Compatibility

- ComfyUI (latest recommended)
- Works with all standard ComfyUI nodes
- Compatible with most custom node packs

## License

MIT License - Feel free to use, modify, and distribute.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## Credits

Developed for the ComfyUI community.
