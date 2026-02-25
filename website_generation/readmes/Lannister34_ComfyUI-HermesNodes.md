# Hermes Nodes

A collection of useful custom nodes for ComfyUI.

Feature requests and bug reports are welcome - please open an issue on GitHub.


## Installation

Clone the repo to `custom_nodes` folder

## Nodes

### WAN Dual LoRA Loader

A specialized LoRA loader designed for WAN 2.2 architecture, which uses separate HIGH and LOW noise models.

![WAN Dual LoRA Loader](images/WanDualLoraLoader.png)

#### Key Features

- **Two-Column Layout** - Separate LoRA lists for HIGH and LOW noise models
- **I2V/T2V Folder Structure** - Organize LoRAs by type:
  ```
  models/loras/wan/
  ├── I2V/
  │   ├── HIGH/
  │   └── LOW/
  └── T2V/
      ├── HIGH/
      └── LOW/
  ```
- **Shared Folders** - LoRAs placed in `I2V/` or `T2V/` root (not in HIGH/LOW subfolders) appear in both lists
- **Preset System** - Save and load LoRA+prompt configurations
- **Multiple Preset Lists** - Organize presets into categories (Default, I2V, T2V)
- **Wildcard Prompt Processing** - Built-in wildcard support in the prompt field
- **Auto-Match** - Automatically finds matching LoRAs between HIGH/LOW folders

#### Usage

1. Add **"WAN Dual LoRA Loader"** node (category: `loaders`)
2. Connect your WAN HIGH and LOW models
3. Select folder type (I2V or T2V)
4. Click **"+ Add"** to add LoRAs to each column
5. Use the preset system to save/load configurations
6. Enter your prompt (supports wildcards)

#### Wildcard Syntax

- `{option1|option2|option3}` - Random choice from options
- `__filename__` - Random line from `wildcards/filename.txt`
- `<random:0.5:1.0>` - Random float in range

#### Outputs

| Output | Description |
|--------|-------------|
| `model_high` | HIGH model with LoRAs applied |
| `model_low` | LOW model with LoRAs applied |
| `prompt` | Processed prompt with resolved wildcards |

---

## License

MIT License
