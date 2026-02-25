# ComfyUI HiTem3D Integration

A comprehensive ComfyUI node collection that integrates with the HiTem3D API to generate high-quality 3D models from images, featuring advanced HTML preview capabilities and dynamic content generation.

**Created by:** Geekatplay Studio by Vladimir Chopine  
**Website:** [www.geekatplay.com](https://www.geekatplay.com)  
**Patreon:** [https://www.patreon.com/c/geekatplay](https://www.patreon.com/c/geekatplay)  
**YouTube:** [@geekatplay](https://www.youtube.com/@geekatplay) and [@geekatplay-ru](https://www.youtube.com/@geekatplay-ru)  

## 💰 Get HiTem3D Credits
**Special Referral Link:** [https://www.hitem3d.ai/?sp_source=Geekatplay](https://www.hitem3d.ai/?sp_source=Geekatplay)  
Use this link to sign up and get credits for HiTem3D API usage!

## 🎯 New Features

### � Latest Updates
- **New Resolutions**: Support for 1536 and 1536pro (Pro Quality)
- **New Format**: Support for USDZ output format
- **New Models**: Support for hitem3dv2.0 and scene-portraitv1.5

### �🌐 HTML Previewer System
- **Live HTML Preview** in ComfyUI with floating panel interface
- **Auto-refresh functionality** with dynamic tokens
- **Secure file serving** with path validation
- **Interactive controls** with drag & drop support

### 🔄 Dynamic Value Generation
- **Dynamic Value Generator** - Create timestamps, counters, UUIDs, random values
- **Text Template System** - Process templates with dynamic placeholders
- **Auto-refresh Tokens** - Trigger HTML preview updates automatically

### 📊 Complete Node Collection
- **8 specialized nodes** for 3D generation, HTML preview, and history tracking

## 📁 Examples & Workflows
Check out the **`examples/`** folder for:
- `hitem3d_basic_workflow.json` - Basic 3D generation workflow
- `html_previewer_workflow.json` - HTML preview with auto-refresh
- `basic_workflow_with_history.json` - Complete workflow with history tracking
- Complete integration examples and documentation

## 🚀 Quick Start

**⚠️ SETUP REQUIRED:** This node requires your personal HiTem3D API keys!

1. **Run Setup Wizard:**
   ```cmd
   # Windows
   setup_wizard.bat
   
   # Linux/Mac
   python setup_wizard.py
   ```

2. **Get API Keys:** [https://www.hitem3d.ai/?sp_source=Geekatplay](https://www.hitem3d.ai/?sp_source=Geekatplay)

3. **Add Credits** to your HiTem3D account

4. **Restart ComfyUI** and try the example workflows!

📖 **Detailed Setup:** See `QUICK_SETUP.md`

## 🔧 Node Collection

### Core 3D Generation Nodes

#### HiTem3D Generator Node
Converts images to 3D models using HiTem3D API.

**Required Inputs:**
- `front_image`: The front view image (required)

**Optional Inputs:**
- `back_image`, `left_image`, `right_image`: Additional view images
- `model`: Model version (`hitem3dv1`, `hitem3dv1.5`, `hitem3dv2.0`, `scene-portraitv1.5`)
- `resolution`: Output resolution (`512`, `1024`, `1536`, `1536pro`)
- `output_format`: File format (`obj`, `glb`, `stl`, `fbx`)
- `generation_type`: Generation type (`geometry_only`, `staged`, `all_in_one`)
- `face_count`: Number of faces (100,000 - 2,000,000)
- `timeout`: Maximum wait time in seconds

**Outputs:**
- `model_url`: URL to download the generated 3D model
- `cover_url`: URL to download the preview image
- `task_id`: Unique task identifier

#### HiTem3D Downloader Node
Downloads 3D models from HiTem3D URLs.

**Inputs:**
- `model_url`: URL from the Generator node
- `file_name`: Base filename for the downloaded model

**Outputs:**
- `model_path`: Local path to the downloaded model file
- `status`: Download status message

#### HiTem3D Config Node
Updates API configuration.

**Inputs:**
- `access_key`: Your HiTem3D access key
- `secret_key`: Your HiTem3D secret key
- `api_base_url`: API base URL (optional)
- `save_config`: Whether to save configuration to file

#### HiTem3D 3D Preview Node
Interactive 3D model viewer for generated models.

**Inputs:**
- `model_path`: Path to the 3D model file
- `width`, `height`: Preview window dimensions
- `background_color`: Background color
- `auto_rotate`: Enable automatic rotation
- `show_wireframe`: Show model in wireframe mode
- `show_grid`: Display reference grid

**Outputs:**
- `preview_html`: HTML preview of the 3D model
- `preview_file_path`: Path to saved preview file
- `preview_url`: URL for opening preview

### HTML Preview System Nodes

#### HTML Previewer (Local)
Displays HTML content in ComfyUI with live preview panel.

**Inputs:**
- `html_content`: HTML content to display
- `auto_refresh_token`: Token for triggering auto-refresh

**Outputs:**
- `preview_url`: URL for accessing the HTML preview

**Features:**
- 🎯 **Floating Preview Panel** - Draggable interface
- 🔄 **Auto-refresh Detection** - Automatically detects when to refresh
- 🛡️ **Secure File Serving** - Safe path validation
- 🎮 **Interactive Controls** - Toolbar with refresh and settings

#### Dynamic Value Generator
Generates dynamic values for auto-refresh and templating.

**Inputs:**
- `value_type`: Type of value (`timestamp`, `counter`, `uuid`, `random`, `custom`)
- `custom_prefix`: Optional prefix for generated values
- `counter_start`: Starting value for counter mode
- `format_string`: Timestamp format string

**Outputs:**
- `dynamic_value`: Generated dynamic value

**Value Types:**
- **Timestamp**: Current date/time in configurable format
- **Counter**: Incremental counter with custom starting value
- **UUID**: Unique identifier (8-character short form)
- **Random**: Random number (1000-9999)
- **Custom**: Unix timestamp with custom prefix

#### Text Template
Processes text templates with dynamic placeholders.

**Inputs:**
- `template`: Text template with `{{placeholder}}` syntax
- `value1`, `value2`, `value3`: Dynamic values for template
- `timestamp_format`: Format for built-in timestamp placeholders

**Outputs:**
- `text_output`: Processed template with values replaced

**Built-in Placeholders:**
- `{{timestamp}}` - Current timestamp
- `{{date}}` - Current date
- `{{unix}}` - Unix timestamp
- `{{year}}`, `{{month}}`, `{{day}}` - Date components
- `{{hour}}`, `{{minute}}`, `{{second}}` - Time components
- `{{value1}}`, `{{value2}}`, `{{value3}}` - Input values

#### HiTem3D History
Tracks and manages generated model history with organized download interface.

**Inputs:**
- `model_url`: Model download URL from HiTem3D Generator
- `cover_url`: Cover image URL from HiTem3D Generator
- `task_id`: Task ID for tracking (optional)
- `model_name`: Custom name for the model (optional)
- `max_history_items`: Maximum number of history entries to keep (10-200)

**Outputs:**
- `history_html`: Beautiful HTML interface showing model history
- `history_status`: Status message with operation results

**Features:**
- 📚 **Organized History** - Chronological list of all generated models
- 🎯 **Direct Downloads** - Clickable links for models and covers
- 📊 **Smart Tracking** - Automatic timestamps and file format detection
- 🌟 **Professional UI** - Modern scrollable interface with hover effects
- 💾 **Persistent Storage** - History saved to JSON file between sessions
- 🔍 **Model Details** - Shows format, task ID, generation date/time

**History Display Features:**
- **Alternating Rows** - Easy visual scanning
- **Download Buttons** - Separate buttons for 3D model and cover image
- **Format Badges** - GLB, OBJ, STL, FBX format indicators
- **Timestamp Display** - Date and time of generation
- **Scrollable Interface** - Handles large history collections
- **Responsive Design** - Works on different screen sizes

## Installation

The node collection is already installed in your ComfyUI directory:
```
ComfyUI/custom_nodes/comfyui-hitem3d/
```

Install dependencies using one of these methods:

**Method 1 - Direct Installation (Recommended):**
```powershell
cd "ComfyUI/custom_nodes/comfyui-hitem3d"
.\install_direct.bat
```

**Method 2 - PowerShell Script:**
```powershell
cd "ComfyUI/custom_nodes/comfyui-hitem3d"
.\install.ps1
```

**Method 3 - Manual Installation:**
```powershell
cd "ComfyUI/custom_nodes/comfyui-hitem3d"
& "../../python_embeded/python.exe" -m pip install -r requirements.txt
```

## Configuration

### Initial Setup Required

**⚠️ IMPORTANT: Configure your personal API keys before using this node!**

1. **Get Your API Keys:**
   - Visit [https://www.hitem3d.ai/?sp_source=Geekatplay](https://www.hitem3d.ai/?sp_source=Geekatplay)
   - Register/Login to your account
   - Navigate to the API/Developer section
   - Generate your personal Access Key and Secret Key

2. **Configure the Node:**
   - Run the setup wizard: `python setup_wizard.py`
   - Or manually edit `config.json` with your keys
   - Or use the `HiTem3DConfigNode` in ComfyUI

3. **Add Credits:**
   - Purchase a resource package at [HiTem3D](https://www.hitem3d.ai/?sp_source=Geekatplay)
   - Each 3D generation consumes credits based on resolution and complexity

## Usage Examples

### Basic 3D Generation Workflow

1. **Load Image**: Use ComfyUI's Load Image node
2. **Configure API**: Use HiTem3DConfigNode with your credentials
3. **Generate 3D**: Connect image to HiTem3DNode
4. **Download Model**: Use HiTem3DDownloaderNode
5. **Preview**: Use HiTem3DPreviewNode for interactive 3D preview

### HTML Preview Workflow

1. **Generate Content**: Create HTML content (from 3D preview or custom)
2. **Add Auto-refresh**: Use DynamicValueGenerator for refresh tokens
3. **Process Template**: Use TextTemplate for dynamic content
4. **Preview HTML**: Use HTMLPreviewer for live preview in ComfyUI

## Supported Parameters

### Model Versions
- `hitem3dv1`: General model version 1.0
- `hitem3dv1.5`: General model version 1.5 (recommended)
- `scene-portraitv1.5`: Specialized for portrait/character models

### Resolutions
- `512`: 512³ resolution (fastest)
- `1024`: 1024³ resolution (recommended)
- `1536`: 1536³ resolution (high quality)
- `1536pro`: 1536³ Pro resolution (highest quality)

### Output Formats
- `obj`: Wavefront OBJ format
- `glb`: Binary glTF format (recommended)
- `stl`: STL format (for 3D printing)
- `fbx`: Autodesk FBX format

### Generation Types
- `geometry_only`: Generate only the mesh geometry
- `texture_only`: Generate textures for existing geometry
- `both`: Generate both geometry and textures (recommended)

## Troubleshooting

### Common Issues

1. **"Insufficient balance" (余额不足)**: Your account needs more credits
   - Visit [https://www.hitem3d.ai/?sp_source=Geekatplay](https://www.hitem3d.ai/?sp_source=Geekatplay) to purchase credits

2. **"Invalid credentials"**: Check your access key and secret key in config

3. **"Task timeout"**: Increase the timeout value or try lower resolution

4. **"Some Nodes Are Missing"**: 
   - Restart ComfyUI completely to reload node definitions
   - Check that all dependencies are installed correctly

5. **HTML Previewer not working**:
   - Ensure server imports are available
   - Check that no other process is using the same port

For detailed troubleshooting, see `TROUBLESHOOTING.md`.

### API Limits

- Maximum image size: 20MB per image
- Maximum images: 4 images (front, back, left, right)
- Supported formats: PNG, JPEG, JPG, WebP
- Face count range: 100,000 - 2,000,000

## Documentation

- `HTML_PREVIEWER_README.md` - Detailed HTML preview system guide
- `QUICK_SETUP.md` - Quick setup instructions
- `TROUBLESHOOTING.md` - Comprehensive troubleshooting guide
- `examples/README.md` - Example workflows and usage patterns

## API Reference

For detailed API documentation, visit:
- [HiTem3D API Documentation](https://docs.hitem3d.ai/en/api/api-reference/)
- [Getting Started Guide](https://docs.hitem3d.ai/en/api/getting-started/)
- [Quick Start](https://docs.hitem3d.ai/en/api/getting-started/quickstart)

## Support

For issues related to:
- **This ComfyUI node**: Visit [www.geekatplay.com](https://www.geekatplay.com) or contact Geekatplay Studio
- **HiTem3D API**: Contact [apicontact@hitem3d.ai](mailto:apicontact@hitem3d.ai)
- **ComfyUI**: Check the [ComfyUI documentation](https://github.com/comfyanonymous/ComfyUI)

## Support Geekatplay Studio

If you find this node collection useful, please consider supporting:
- **Patreon:** [https://www.patreon.com/c/geekatplay](https://www.patreon.com/c/geekatplay)
- **YouTube:** [@geekatplay](https://www.youtube.com/@geekatplay) and [@geekatplay-ru](https://www.youtube.com/@geekatplay-ru)
- **Website:** [www.geekatplay.com](https://www.geekatplay.com)

## License

This project is created by Geekatplay Studio by Vladimir Chopine for integration with the HiTem3D API service.

## Version History

- **v2.0.0**: Complete HTML Preview System
  - Added HTML Previewer with live preview panel
  - Dynamic Value Generator for auto-refresh functionality
  - Text Template system with placeholder processing
  - Enhanced 3D Preview with interactive controls
  - Cleaned project structure and comprehensive documentation

- **v1.0.0**: Initial release with full HiTem3D API integration
  - Single and multi-view image support
  - All model versions and formats
  - Configurable parameters
  - Automatic download functionality
  - Created by Geekatplay Studio