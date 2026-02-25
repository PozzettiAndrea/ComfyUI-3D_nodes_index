# ComfyUI Arena Suite v6.0.0

🚀 **Modern ComfyUI Custom Node Suite** - Automatic model caching and workflow optimization for ComfyUI.

## ✨ Features

- **🅰️ Arena AutoCache v6.0.0** - Fixed critical caching bugs, universal model parser, three Arena button modes (Gray/Red/Green)
- **🔧 Settings UI** - Complete ComfyUI Settings integration with "💾 Save to .env" button
- **🎯 Universal Model Detection** - Automatic detection of all model types without hardcoded node support
- **⚡ Parallel Caching** - Multi-threaded model caching with background workers
- **🛡️ Safe Defaults** - Always disabled by default, user must explicitly enable

## 🚀 Quick Start

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/3dgopnik/comfyui-arena-suite.git
   cd comfyui-arena-suite
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Copy to ComfyUI custom_nodes:**
   ```bash
   cp -r . /path/to/ComfyUI/custom_nodes/ComfyUI-Arena/
   ```

4. **Restart ComfyUI** and navigate to Settings → Arena

## 🎯 Arena AutoCache

### Three Modes

**🔘 Gray Mode (Default)** - System disabled
- `ARENA_AUTO_CACHE_ENABLED=0`, `ARENA_AUTOCACHE_AUTOPATCH=0`
- Uses original model paths

**🔴 Red Mode** - Active caching
- `ARENA_AUTO_CACHE_ENABLED=1`, `ARENA_AUTOCACHE_AUTOPATCH=1`
- Caches new models + uses cache
- Parallel prefetching of all workflow models

**🟢 Green Mode** - Cache usage only
- `ARENA_AUTO_CACHE_ENABLED=1`, `ARENA_AUTOCACHE_AUTOPATCH=0`
- Uses cache, doesn't cache new models
- Shows uncached model count in tooltip

### Setup

1. **Open ComfyUI Settings** → Arena section
2. **Fill Cache Root** path (e.g., `f:\ComfyUIModelCache\`)
3. **Click "💾 Save to .env"** (creates `user/arena_autocache.env`)
4. **Use Arena button** in header to switch modes

### Supported Model Categories

- `checkpoints`, `loras`, `clip`, `vae`, `controlnet`
- `upscale_models`, `embeddings`, `hypernetworks`
- `gguf_models`, `unet_models`, `diffusion_models`
- **SUPIR**, **Flux**, **Wan**, and all custom model types

## 🛠️ Technical Details

### Architecture

- **Settings Panel** - Primary interface for configuration
- **Arena Button** - Intuitive mode switching
- **Optional Node** - Advanced users can override settings
- **Deferred Autopatch** - Always active, patching `folder_paths.get_full_path()`

### Universal Model Parser

Instead of hardcoded node support, the system:
1. Scans `widgets_values` for model file extensions
2. Detects category using `categoryByNodeType` mapping
3. Falls back to filename-based category detection
4. Works with any node type automatically

### Environment Variables

```bash
ARENA_AUTO_CACHE_ENABLED=1          # Enable/disable caching
ARENA_AUTOCACHE_AUTOPATCH=1         # Enable/disable autopatch
ARENA_CACHE_ROOT=f:\ComfyUIModelCache\  # Cache directory
ARENA_CACHE_MIN_SIZE_MB=10          # Minimum file size
ARENA_CACHE_MAX_GB=0                # Max cache size (0=unlimited)
ARENA_CACHE_MODE=ondemand           # Caching mode
ARENA_CACHE_VERBOSE=1               # Detailed logging
```

## 📁 Project Structure

```
ComfyUI-Arena/
├── autocache/                      # Core caching logic
│   ├── arena_auto_cache_simple.py  # Main caching engine
│   ├── arena_path_manager.py       # Path management
│   └── arena_smart_cache.py        # Smart caching strategies
├── web/                            # Frontend extensions
│   ├── arena_simple_header.js      # Arena button with 3 modes
│   ├── arena_settings_save_button.js # Settings UI
│   └── arena_workflow_analyzer.js  # Universal model parser
├── docs/                           # Documentation
│   ├── ru/                         # Russian documentation
│   └── en/                         # English documentation
└── config/                         # Configuration files
    └── extra_model_paths.yaml      # Model path definitions
```

## 🔧 Development

### Testing

```bash
# Test caching with different workflows
python -m pytest tests/
```

### Debugging

Enable verbose logging:
```bash
ARENA_CACHE_VERBOSE=1
```

Check logs in ComfyUI console for detailed caching information.

## 📝 Changelog

### v6.0.0 (2025-01-27)

**Fixed:**
- Critical model caching pipeline issues
- WindowsPath + str concatenation errors
- Double path creation (Flux\flux\, Wan\Wan\)
- SUPIR model detection and categorization
- Python indentation errors preventing autopatch
- folder_paths.get_full_path() filename resolution

**Changed:**
- Universal model parser replaces hardcoded node detection
- Enhanced cache path construction with Path/str consistency
- Improved model type detection for all categories

**Added:**
- Automatic model detection across all node types
- Enhanced error handling and cross-platform compatibility
- Comprehensive testing across SUPIR, Wan, and Flux workflows

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

MIT License - see LICENSE file for details.

## 🔗 Links

- **GitHub Repository:** https://github.com/3dgopnik/comfyui-arena-suite
- **Issues:** https://github.com/3dgopnik/comfyui-arena-suite/issues
- **Documentation:** [docs/](docs/)

---

**Made with ❤️ for the ComfyUI community**