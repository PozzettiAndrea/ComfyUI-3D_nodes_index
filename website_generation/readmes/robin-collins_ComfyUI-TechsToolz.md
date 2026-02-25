# ComfyUI-TechsToolz

A modular collection of ComfyUI custom nodes with advanced dependency management and ComfyUI Manager integration.

## 🚀 Features

### 🖥️🛠 Available Nodes

- **🖥️🛠TechsToolz: Model Name Extractor** - Extracts model names from ComfyUI MODEL objects
- **🖥️🛠TechsToolz: Save Image w/Metadata** - Advanced image saving with embedded metadata

### 🔍 Dependency Management

- **Automatic Dependency Scanning** - Scans all Python files and identifies dependencies
- **Runtime Dependency Checking** - Validates dependencies at startup
- **Missing Dependency Reporting** - Clear reports on missing packages with installation suggestions
- **Dependency Health Monitoring** - Ongoing validation of package availability

### 🔧 ComfyUI Manager Integration

- **Node Enable/Disable** - Toggle individual node modules on/off
- **Configuration Management** - Persistent configuration storage
- **Manager API Support** - Full integration with ComfyUI Manager
- **Modular Architecture** - Easy addition of new node modules

## 📦 Installation

### Via ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "ComfyUI-TechsToolz"
3. Click Install
4. Restart ComfyUI

### Manual Installation

1. Clone this repository into your ComfyUI custom_nodes directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/robin-collins/ComfyUI-TechsToolz.git
```

2. Run the installation script:
```bash
cd ComfyUI-TechsToolz
python install.py
```

3. Restart ComfyUI

## 🔧 Dependencies

### Required
- `piexif` - EXIF metadata handling
- `numpy` - Numerical operations
- `Pillow` (PIL) - Image processing

### ComfyUI Dependencies
- `folder_paths` - ComfyUI path utilities
- `comfy` - ComfyUI core modules
- `nodes` - ComfyUI node system

All dependencies are automatically checked and reported at startup.

## 📖 Usage

### Model Name Extractor

Extracts the filename from ComfyUI MODEL objects:

**Inputs:**
- `model` (MODEL) - Any ComfyUI model object

**Outputs:**
- `model_name` (STRING) - Extracted model filename

**Supported Model Types:**
- GGUF models
- Standard checkpoints (.ckpt, .safetensors)
- Various model formats with fallback handling

### Save Image w/Metadata

Advanced image saving with embedded generation metadata:

**Inputs:**
- `images` (IMAGE) - Images to save
- `filename` (STRING) - Filename pattern with placeholders
- `path` (STRING) - Output directory path
- `extension` - Format: PNG, JPEG, WebP
- `steps`, `cfg`, `sampler_name`, `scheduler` - Generation parameters
- `positive`, `negative` - Prompts
- `modelname` - Model identifier
- And more configuration options...

**Features:**
- **Metadata Embedding**: PNG metadata and EXIF data
- **Filename Placeholders**: `%time`, `%seed`, `%model`, `%counter`, `%date`
- **Directory Management**: Automatic path creation
- **Quality Control**: Configurable compression settings

## ⚙️ Configuration

### Node Configuration

Configuration is stored in `node_config.json`:

```json
{
  "enabled_modules": ["image_nodes"],
  "disabled_modules": [],
  "package_info": {
    "name": "ComfyUI-TechsToolz",
    "version": "0.0.1",
    "supports_manager": true
  }
}
```

### ComfyUI Manager Integration

The package provides several API functions for ComfyUI Manager:

- `get_node_list()` - List available nodes
- `get_package_info()` - Package metadata
- `enable_node_module(module_name)` - Enable a module
- `disable_node_module(module_name)` - Disable a module
- `get_dependency_report()` - Current dependency status

## 🏗️ Architecture

### Modular Design

```
ComfyUI-TechsToolz/
├── __init__.py                 # Main initialization with dependency checking
├── image_nodes.py              # Image processing nodes
├── node_list.json             # ComfyUI Manager node definitions
├── install.py                 # Installation script
├── node_config.json           # Configuration storage
└── requirements.txt           # Python dependencies
```

### Dependency Checking System

The `DependencyChecker` class:
1. Scans all Python files using AST parsing
2. Extracts import statements
3. Validates package availability
4. Generates detailed reports
5. Provides installation suggestions

### Node Manager System

The `NodeManager` class:
1. Loads configuration from JSON
2. Manages module enable/disable states
3. Dynamically imports enabled modules
4. Provides ComfyUI Manager API functions

## 🚧 Development

### Adding New Modules

1. Create your module file (e.g., `utility_nodes.py`)
2. Export `NODE_CLASSES` and `NODE_DISPLAY_NAMES` dictionaries
3. Add the module to `available_modules` in `__init__.py`
4. Update `node_list.json` with new node definitions

Example module structure:
```python
# utility_nodes.py
class MyUtilityNode:
    # ... node implementation ...

NODE_CLASSES = {
    "MyUtilityNode": MyUtilityNode,
}

NODE_DISPLAY_NAMES = {
    "MyUtilityNode": "🖥️🛠TechsToolz: My Utility Node",
}
```

### Code Standards

- **Type Hints**: Full type annotation required
- **Documentation**: Comprehensive docstrings
- **Error Handling**: Graceful failure handling
- **Logging**: Structured logging throughout
- **Testing**: Pytest for unit tests

### Tools

```bash
# Linting and formatting
ruff check --fix .
ruff format .

# Type checking
mypy .

# Testing
pytest
```

## 📊 Dependency Report Example

```
============================================================
ComfyUI-TechsToolz Dependency Report
============================================================
Python files scanned: 3
Total unique dependencies: 8
Available dependencies: 6
Missing dependencies: 2

✅ Available Dependencies:
------------------------------
  ✓ numpy
  ✓ piexif
  ✓ PIL
  ✓ folder_paths
  ✓ comfy
  ✓ json

❌ Missing Dependencies:
------------------------------
  ✗ some_package
  ✗ another_package

Installation suggestions:
pip install some_package another_package
============================================================
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Update documentation
6. Submit a pull request

## 📄 License

GNU General Public License v3.0

## 🙏 Acknowledgments

- ComfyUI community for the excellent platform
- ComfyUI Manager for the integration framework
- All contributors and users of this project

## 📞 Support

- GitHub Issues: [Report bugs or request features](https://github.com/robin-collins/ComfyUI-TechsToolz/issues)
- Discussions: [Community support and questions](https://github.com/robin-collins/ComfyUI-TechsToolz/discussions)

---

*Built with ❤️ for the ComfyUI community*