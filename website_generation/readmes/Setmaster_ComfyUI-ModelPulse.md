# ModelPulse

A ComfyUI extension that tracks model usage frequency, helping you identify abandoned or underutilized models to manage storage efficiently.

![ComfyUI](https://img.shields.io/badge/ComfyUI-0.3.0+-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

## Features

- **Automatic Tracking** - Monitors usage of all model types: checkpoints, LoRAs, VAEs, ControlNets, CLIP, UNETs, upscalers, GGUF, and more
- **Sidebar Panel** - View usage statistics directly in ComfyUI's sidebar
- **File Size Display** - Shows model file sizes (GB/MB) to help identify storage-heavy models
- **Time Filtering** - View usage for all time, this month, or this week
- **Smart Sorting** - Sort by last used, usage count, or name
- **Stale Detection** - Models unused for 30+ days are highlighted (configurable threshold)
- **Category Grouping** - Models organized by type with collapsible sections
- **Reset Tracking** - Clear all usage data from the settings panel
- **Zero Dependencies** - Uses only Python standard library

## Installation

### Option 1: ComfyUI Manager (Recommended)

Search for "ModelPulse" in ComfyUI Manager and click Install.

### Option 2: Manual Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Setmaster/ComfyUI-ModelPulse.git
```

Restart ComfyUI after installation.

## Usage

1. Click the **chart icon** in the ComfyUI sidebar to open ModelPulse
2. Run workflows as usual - model usage is tracked automatically
3. Use the tabs to filter by time period (All Time / Month / Week)
4. Use the dropdown to sort by Last Used, Usage Count, or Name
5. Click category headers to collapse/expand sections

## Tracked Model Types

| Category | Loader Nodes |
|----------|-------------|
| Checkpoints | CheckpointLoaderSimple, CheckpointLoader |
| LoRAs | LoraLoader, LoraLoaderModelOnly |
| VAEs | VAELoader |
| ControlNets | ControlNetLoader |
| CLIP | CLIPLoader, DualCLIPLoader |
| UNETs | UNETLoader |
| Upscalers | UpscaleModelLoader |
| Style Models | StyleModelLoader |
| GLIGEN | GLIGENLoader |
| GGUF | UnetLoaderGGUF, CLIPLoaderGGUF, DualCLIPLoaderGGUF, TripleCLIPLoaderGGUF, QuadrupleCLIPLoaderGGUF |

Custom node loaders (Impact Pack, Efficiency Nodes, etc.) are also detected via pattern matching.

## API Endpoints

ModelPulse exposes REST endpoints for programmatic access:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/modelpulse/usage` | GET | Get all usage data (supports `?timeframe=` and `?sort=` params) |
| `/modelpulse/model/{id}` | GET | Get detailed data for a specific model |
| `/modelpulse/categories` | GET | Get category list with counts |
| `/modelpulse/reset` | POST | Reset all tracking data (requires `{"confirm": true}`) |

## Data Storage

Usage data is stored in:
```
ComfyUI/user/default/modelpulse/usage_data.json
```

The data persists across ComfyUI restarts and can be backed up or edited manually.

## Requirements

- ComfyUI 0.3.0 or later (Vue 3 frontend)
- Python 3.10+
- No external Python dependencies

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.
