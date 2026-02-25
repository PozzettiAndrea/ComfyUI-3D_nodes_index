# ComfyUI Custom Nodes - ERPK Collection

[![Publish to Comfy Registry](https://github.com/eRepublik-Labs/comfyui-nodes-erpk/actions/workflows/publish.yml/badge.svg)](https://github.com/eRepublik-Labs/comfyui-nodes-erpk/actions/workflows/publish.yml)
[![Registry](https://img.shields.io/badge/ComfyUI-Registry-blue)](https://registry.comfy.org/publishers/erpk/nodes/comfyui-nodes-erpk)

A monorepo for ERPK's custom ComfyUI nodes, extending ComfyUI's functionality through integrations with various AI services and APIs.

**Current Version:** 2026.2.15 (CalVer)

## Repository Structure

```
ComfyUI-Custom-Nodes/
├── wavespeed/                     # WaveSpeed AI integration
│   ├── README.md                  # Package documentation
│   ├── nodes.py                   # Core nodes
│   ├── seedream_v4*.py            # Seedream V4 nodes (4 variants)
│   ├── seedream_v4_5*.py          # Seedream V4.5 nodes (4 variants)
│   ├── qwen_image_*.py            # Qwen Image nodes
│   └── wavespeed_api/             # API integration layer
├── claude/                        # Claude API integration
│   ├── README.md                  # Package documentation
│   ├── nodes.py                   # Core nodes
│   ├── prompt_enhancer.py         # Prompt enhancement node
│   ├── vision_analysis.py         # Image analysis node
│   └── claude_api/                # API integration layer
├── gemini/                        # Google Gemini API integration
│   ├── README.md                  # Package documentation
│   ├── nodes.py                   # All Gemini nodes
│   ├── veo_nodes.py               # Veo video generation nodes
│   └── gemini_api/                # API integration layer
├── openai/                        # OpenAI API integration
│   ├── README.md                  # Package documentation
│   ├── nodes.py                   # Core nodes (Config, Text, Vision, Chat)
│   ├── image_nodes.py             # Image generation/editing nodes
│   └── openai_api/                # API integration layer
├── bgremoval/                     # Background removal utilities
│   ├── utils.py                   # Shared tensor/PIL conversion utilities
│   ├── rembg_node.py              # rembg backend (14+ ONNX models)
│   ├── inspyrenet_node.py         # InSPyReNet backend (PyTorch)
│   ├── birefnet_node.py           # BiRefNet backend (HuggingFace)
│   ├── ben2_node.py               # BEN2 backend (HuggingFace)
│   └── blur_fusion_node.py        # BlurFusion foreground refinement
├── apple/                         # Apple ML models integration
│   ├── README.md                  # Package documentation
│   └── sharp_nodes.py             # SHARP view synthesis nodes
├── utils/                         # String and general utilities
│   ├── __init__.py                # Module exports
│   └── concat_strings.py          # String concatenation node
├── settings.py                    # ComfyUI settings reader for API keys
├── shared_workflows.py            # Shared workflows CRUD for multi-user
├── shared_workflows/              # Legacy storage fallback (gitignored)
└── web/                           # Frontend extensions
    ├── erpk_settings.js           # API key settings in ComfyUI Settings UI
    ├── shared_workflows.js        # Browse/save/delete shared workflows UI
    ├── aspect_ratio.js            # Aspect ratio display in node titles
    └── concat_strings.js          # Dynamic UI for concat strings node
```

## Available Node Packages

### ERPK/WaveSpeedAI

Custom nodes for WaveSpeed AI's image generation and editing APIs.

**Category in ComfyUI:** `ERPK/WaveSpeedAI`
**Version:** 2026.2.15

#### ByteDance Seedream V4 Models

- **Seedream V4** - Text-to-image generation with configurable dimensions (320-4096px)
- **Seedream V4 Sequential** - Multi-image generation with cross-image consistency (1-15 images, $0.027/image)
- **Seedream V4 Edit** - AI-powered image editing with text prompts (up to 10 reference images)
- **Seedream V4 Edit Sequential** - Multi-image editing with coherent results (1-15 images, $0.027/image)

#### ByteDance Seedream V4.5 Models

- **Seedream V4.5** - Enhanced typography and text rendering for posters, logos, UI (1024-4096px)
- **Seedream V4.5 Sequential** - Multi-image generation with typography support (1-15 images, $0.027/image)
- **Seedream V4.5 Edit** - Image editing with enhanced text rendering (up to 10 reference images)
- **Seedream V4.5 Edit Sequential** - Multi-image editing with typography (1-15 images, $0.027/image)

#### Qwen Image Models

- **Qwen Image Text-to-Image** - Bilingual text-to-image generation (Chinese/English, max 1536×1536, $0.02/image)
- **Qwen Image Edit** - Single image editing with bilingual prompts (256-1536px, $0.02/image)
- **Qwen Image Edit Plus** - Advanced editing with up to 3 reference images ($0.02/image)

**Installation & Documentation:** See [wavespeed/README.md](wavespeed/README.md)

⚠️ **Note:** For the official WaveSpeed ComfyUI nodes and documentation, see the [official WaveSpeed ComfyUI repository](https://github.com/wavespeedai/ComfyUI-WaveSpeed).

### ERPK/Claude

Claude API integration for text generation, prompt enhancement, vision analysis, and conversational AI.

**Category in ComfyUI:** `ERPK/Claude`
**Version:** 2026.2.15

#### Nodes

- **Claude API Client** - Initialize Claude API connection with model selection (Sonnet 4.6, Opus 4.6, Haiku 4.5) and configuration. Optional if API key is configured in ComfyUI Settings, environment variable, or config.ini -- Claude nodes can run standalone.
- **Claude Prompt Enhancer** - Transform simple prompts into detailed descriptions with 51 artistic styles (photorealistic, cinematic, fantasy, cyberpunk, anime, oil painting, watercolor, and more)
- **Claude Vision Analysis** - Analyze images with Claude's multimodal capabilities (up to 20 images simultaneously)
- **Claude Text Generation** - General-purpose text completion and generation
- **Claude Conversation** - Multi-turn dialogues with context preservation and automatic memory management
- **Claude Conversation Info** - Display conversation statistics and token usage
- **Claude Tool Definition** - Build Anthropic tool definitions for structured output (chainable)
- **Claude Structured Output** - Force Claude to respond with structured JSON matching a tool schema
- **Claude Token Counter** - Count tokens and estimate API costs before making requests
- **Claude Usage Stats** - Track cumulative token usage and costs across all Claude nodes

**Key Benefits:**
- 51 artistic styles for prompt enhancement (photorealistic, cinematic, fantasy, anime, oil painting, impressionist, cyberpunk, and more)
- Prompt caching (up to 90% cost savings)
- Streaming support for real-time responses
- Automatic context window management
- Multi-image analysis capabilities
- Cost optimization with token counting

**Installation & Documentation:** See [claude/README.md](claude/README.md)

### ERPK/Gemini

Google Gemini API integration for text generation, vision analysis, multi-turn conversations, image generation, image editing, and **Veo video generation**.

**Category in ComfyUI:** `ERPK/Gemini` and `ERPK/Gemini/Veo`
**Version:** 2026.2.15

#### Nodes

- **Gemini API Config** - Initialize Gemini API connection (API key configuration). Optional if API key is configured in ComfyUI Settings, environment variable, or config.ini -- Gemini nodes can run standalone.
- **Gemini Text Generation** - General-purpose text generation with model selection (Gemini 3.1 Pro, 3 Pro, 3 Flash, 2.5 Pro, 2.5 Flash, 2.5 Flash-Lite)
- **Gemini Chat** - Multi-turn conversations with automatic context preservation
- **Gemini Vision** - Analyze images with multimodal capabilities
- **Gemini Image Generation** - Generate images from text descriptions (standalone node with dedicated image gen models)
- **Gemini Image Edit** - Edit and modify images with natural language prompts (up to 14 reference images)
- **Gemini System Instruction** - Set persistent system-level instructions to guide model behavior
- **Gemini Safety Settings** - Configure content safety filters (strict/balanced/permissive presets or custom)

#### Veo Video Generation Nodes

- **Veo Text to Video** - Generate videos from text prompts using Google's Veo models (Veo 3 includes synchronized audio)
- **Veo Image to Video** - Generate videos from an input image and optional text prompt

**Key Benefits:**
- Support for Gemini 3.1 Pro, 3 Pro, 3 Flash, and Gemini 2.5 models
- **Thinking level** control for Gemini 3+ models (none/low/medium/high reasoning depth)
- **Veo video generation** with text-to-video and image-to-video (Veo 3 includes audio)
- Each node selects its own model for maximum flexibility
- State-of-the-art reasoning with Gemini 3.1 Pro and 2.5 Pro
- Image generation with Gemini 2.5 Flash Image models
- Image editing with natural language instructions (up to 14 reference images)
- Simple, straightforward API integration
- Vision capabilities with batch image support
- Flexible safety controls
- Native multi-turn conversation support

**Installation & Documentation:** See [gemini/README.md](gemini/README.md)

### ERPK/OpenAI

OpenAI API integration for text generation, vision analysis, multi-turn conversations, image generation, and image editing.

**Category in ComfyUI:** `ERPK/OpenAI`
**Version:** 2026.2.15

#### Nodes

- **OpenAI API Config** - Initialize OpenAI API connection (API key configuration). Optional if API key is configured in ComfyUI Settings, environment variable, or config.ini -- OpenAI nodes can run standalone.
- **OpenAI Text Generation** - General-purpose text generation with model selection (GPT-5.2, GPT-4o, GPT-4.1, o3, o3-mini, o3-pro)
- **OpenAI Chat** - Multi-turn conversations with automatic context preservation
- **OpenAI Vision** - Analyze images with GPT-4 vision capabilities
- **OpenAI System Instruction** - Set persistent system-level instructions to guide model behavior
- **OpenAI Image Generation** - Generate images with GPT-Image-1.5 and DALL-E models
- **OpenAI Image Edit** - Edit and inpaint images with natural language prompts

**Key Benefits:**
- Support for latest GPT-5.2, GPT-4.1, GPT-4o, and o-series reasoning models
- Image generation with GPT-Image-1.5 (best quality) and DALL-E 3
- Image editing with optional mask support for inpainting
- Multi-turn conversation with session management
- Automatic retry with exponential backoff
- JSON response format support

**Installation & Documentation:** See [openai/README.md](openai/README.md)

### ERPK/Background Removal

Background removal utilities with multiple backend options for different quality/speed/memory tradeoffs.

**Category in ComfyUI:** `ERPK/Background Removal`

#### Nodes

- **Remove Background (rembg)** - ONNX-based with 14+ models including u2net, isnet, birefnet variants. Best for versatility and CPU support.
- **Remove Background (InSPyReNet)** - PyTorch-based via transparent-background. Supports TorchScript JIT for faster inference.
- **Remove Background (BEN2)** - Confidence-guided matting for accurate alpha mattes at fine edges (hair, fur). Built-in foreground refinement.
- **Remove Background (BiRefNet)** - HuggingFace transformers integration. 17 model variants, supports HR images (2048x2048).

#### Backend Comparison

| Backend | Runtime | Speed | Quality | Memory | License |
|---------|---------|-------|---------|--------|---------|
| **rembg** | ONNX | Fast | Good | Low-Med | MIT |
| **InSPyReNet** | PyTorch | Medium | Very Good | Medium | MIT |
| **BEN2** | PyTorch/HF | Medium | Excellent | High | MIT |
| **BiRefNet** | PyTorch/HF | Slower | Excellent | High | MIT |

#### Available Models

**rembg (14+ models):**
- `u2net` - General purpose (default)
- `u2netp` - Lightweight, faster
- `u2net_human_seg` - Human segmentation
- `u2net_cloth_seg` - Clothing parsing
- `silueta` - Compact u2net (43MB)
- `isnet-general-use` - General purpose ISNet
- `isnet-anime` - Anime characters
- `sam` - Segment Anything Model
- `birefnet-general`, `birefnet-general-lite`, `birefnet-portrait`, `birefnet-dis`, `birefnet-hrsod`, `birefnet-cod`, `birefnet-massive`

**BiRefNet variants:**
- `ZhengPeng7/BiRefNet` - Default
- `ZhengPeng7/BiRefNet_HR` - High resolution (2048x2048)
- `ZhengPeng7/BiRefNet-matting` - Alpha matting
- `ZhengPeng7/BiRefNet_HR-matting` - HR alpha matting
- `ZhengPeng7/BiRefNet-COD` - Camouflaged object detection
- `ZhengPeng7/BiRefNet_512x512` - Fast (lower resolution)

#### Node Outputs

All nodes output:
- `IMAGE` - RGB image (background removed, composited on black)
- `MASK` - Alpha mask for further compositing

#### Features

- Batch processing with progress display
- Alpha matting refinement (rembg only)
- Model caching to avoid reloading
- GPU acceleration where available
- Graceful fallback when dependencies missing

**Installation & Documentation:** See [bgremoval/README.md](bgremoval/README.md)

### ERPK/Apple

Apple ML models integration, currently featuring SHARP for single-image 3D view synthesis.

**Category in ComfyUI:** `ERPK/Apple/SHARP`
**Version:** 2026.2.15

#### SHARP Nodes

SHARP converts a single photograph into a 3D Gaussian splat representation that can be rendered from novel viewpoints.

- **SHARP Predict** - Convert image to 3D Gaussian splat (.ply file)
- **SHARP Render Views** - Render novel views from .ply (CUDA required)
- **SHARP Render Video** - Render orbit video from .ply (CUDA required)

**Key Features:**
- Single-image to 3D in under 1 second on GPU
- Outputs standard .ply Gaussian splat format
- Novel view rendering with customizable camera paths
- Video generation with orbit trajectories

**Installation & Documentation:** See [apple/README.md](apple/README.md)

### ERPK/utils

String manipulation and general utility nodes.

**Category in ComfyUI:** `ERPK/utils`

#### Nodes

- **Concatenate Strings** - Combine multiple text inputs with configurable delimiters. Supports up to 10 connectable inputs - drag STRING outputs from other nodes or enter text directly.

**Key Features:**
- 10 connectable text inputs (Text 1 through Text 10)
- Optional labels for each input (Label 1 through Label 10)
- Configurable delimiter with escape sequence support (\n, \t)
- Label placement options (same line or new line)
- Add/Remove buttons to dynamically manage inputs
- Visual separators between configuration and input sections

### Shared Workflows (Multi-User)

In multi-user ComfyUI (`--multi-user`), each user's workflows are sandboxed. Shared Workflows provides a common directory where any user can save, browse, load, and delete workflow templates. Also works in single-user mode.

**Access:** Right-click the canvas > **ERPK** submenu, or open **ERPK Settings** to see the inline shared workflows list below your API keys.

- **Browse Shared Workflows...** - View all shared workflows with name, size, date, and authorship (created by / last edited by). Load any workflow into your canvas or delete it.
- **Share Current Workflow...** - Save the current canvas workflow to the shared directory. The name field is pre-populated from the current workflow tab.
- **Save to "[name]"** - Appears after loading or sharing a workflow. Saves directly to the linked shared workflow without opening a dialog.
- **Settings panel** - The ERPK Settings panel shows an inline shared workflows list with Load, Delete, and Share Current buttons.

**Linked save-back:** When you load a shared workflow or share one, the workflow name is linked. Subsequent edits can be pushed back to the shared copy via the "Save to" menu item. Other users see the updated version when they browse.

**Authorship tracking:** Each shared workflow records who created it and who last modified it. On overwrite, the original creator is preserved while the modifier is updated.

**Toast notifications:** Success/error feedback appears as a brief toast in the top-right corner for all save, load, and delete operations.

**Storage:** Workflows are saved as JSON files in `shared_workflows/` under the ComfyUI base directory (e.g., `~/Documents/ComfyUI/shared_workflows/`), alongside `input/`, `output/`, and `models/`. This location persists across plugin upgrades and ComfyUI restarts. Falls back to the extension directory when running outside ComfyUI. Each file uses an envelope format (`{meta, workflow}`) that stores authorship metadata alongside the workflow graph. No API keys or user-specific data are stored.

**API Endpoints:**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/erpk/shared_workflows` | GET | List all shared workflows (metadata including authorship) |
| `/erpk/shared_workflows/{name}` | GET | Get a single workflow by name |
| `/erpk/shared_workflows` | POST | Save a workflow (`{name, workflow}`); records user as author |
| `/erpk/shared_workflows/{name}` | DELETE | Delete a workflow by name |

## Installation

### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Click **Install Custom Nodes**
3. Search for `erpk`
4. Find **ERPK Custom Nodes** and click **Install**
5. Restart ComfyUI

### Method 2: ComfyUI Registry

Install directly from the [ComfyUI Registry](https://registry.comfy.org/publishers/erpk/nodes/comfyui-nodes-erpk) web interface.

### Method 3: Manual Installation

1. Navigate to your ComfyUI custom_nodes directory:
   ```bash
   cd /path/to/ComfyUI/custom_nodes/
   ```

2. Clone this repository as `erpk`:
   ```bash
   git clone https://github.com/eRepublik-Labs/comfyui-nodes-erpk.git erpk
   ```

3. Install dependencies:
   ```bash
   cd erpk
   pip install -r requirements.txt
   ```

4. Restart ComfyUI

### Post-Installation

1. Configure API keys for the services you want to use.
   The easiest way is via right-click on the canvas > **ERPK Settings**, or **Settings > ERPK > API Keys** in ComfyUI -- keys are stored per-user and never saved in workflows.

   API keys are resolved in priority order:
   1. **ComfyUI Settings** (recommended) -- right-click canvas > ERPK Settings
   2. **Widget input** -- api_key field on client/config nodes
   3. **Environment variable** -- `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`, `OPENAI_API_KEY`, `WAVESPEED_API_KEY`
   4. **Config file** -- `provider/config.ini`

   **Multi-user support:** In multi-user ComfyUI installations, each user's API keys are stored separately in their own `comfy.settings.json`. The correct user's keys are resolved automatically during workflow execution. A "Current user: [name]" banner appears in the ERPK Settings panel when multi-user mode is active.

   - **WaveSpeed:** See [wavespeed/README.md](wavespeed/README.md#installation)
   - **Claude:** See [claude/README.md](claude/README.md#installation)
   - **Gemini:** See [gemini/README.md](gemini/README.md#installation)
   - **OpenAI:** See [openai/README.md](openai/README.md#installation)
   - **Background Removal:** No API keys required, models download automatically on first use
   - **Apple/SHARP:** No API keys required. Install with: `pip install git+https://github.com/apple/ml-sharp.git`

2. Find nodes under their respective categories: `ERPK/WaveSpeedAI`, `ERPK/Claude`, `ERPK/Gemini`, `ERPK/OpenAI`, `ERPK/Background Removal`, `ERPK/Apple/SHARP`, and `ERPK/utils`

## Backward Compatibility

This package uses the ComfyUI V3 node API. Saved workflows that reference older node IDs (e.g. `"WaveSpeed Custom SeedreamV4"`, `"ERPK Remove Background (rembg)"`, `"ERPK SHARP Predict"`) are automatically migrated to the current node IDs at load time via ComfyUI's NodeReplace system. No manual workflow editing is required.

## ComfyUI API Integration

ComfyUI provides a REST API that allows programmatic workflow creation and execution. This is useful for automation, testing, and integration with external tools.

### Available Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/system_stats` | GET | System information (OS, RAM, GPU, versions) |
| `/object_info` | GET | List all available nodes and their input/output types |
| `/prompt` | POST | Queue a workflow for execution |
| `/queue` | GET | View pending and running jobs |
| `/history` | GET | View execution history and results |
| `/history/{prompt_id}` | GET | Get results for a specific execution |

### Submitting a Workflow via API

```bash
curl -X POST http://localhost:8188/prompt \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": {
      "1": {
        "class_type": "GeminiAPIConfig",
        "inputs": {
          "api_key": ""
        }
      },
      "2": {
        "class_type": "GeminiTextGeneration",
        "inputs": {
          "client": ["1", 0],
          "prompt": "Write a haiku about ComfyUI",
          "model": "gemini-2.5-flash",
          "temperature": 0.7,
          "max_tokens": 256
        }
      },
      "3": {
        "class_type": "PreviewAny",
        "inputs": {
          "source": ["2", 0]
        }
      }
    }
  }'
```

**Note:** The port may vary (8000 for desktop app, 8188 for standard installation).

### Workflow JSON Format

Workflows can be saved as JSON files in your ComfyUI workflows directory. The format includes:

- `nodes`: Array of node definitions with `id`, `type`, `pos`, `inputs`, `outputs`, and `widgets_values`
- `links`: Array of connections in format `[link_id, source_node, source_slot, target_node, target_slot, type]`
- `last_node_id` / `last_link_id`: Tracking for ID generation

### Checking Available Nodes

```bash
# List all ERPK nodes
curl -s http://localhost:8188/object_info | jq 'keys' | grep -i -E "(gemini|claude|openai)"
```

## License

MIT License
