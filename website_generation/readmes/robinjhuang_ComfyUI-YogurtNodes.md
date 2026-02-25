# ComfyUI-YogurtNodes

ComfyUI-YogurtNodes is a collection of custom nodes for ComfyUI, providing a series of practical image processing and workflow enhancement functionalities.

## ✨ Features

- Custom node integration
- Easy-to-use image processing functions
- Full compatibility with ComfyUI workflows
- Text and image manipulation capabilities
- Advanced string processing utilities
- Model management and selection tools
- Comprehensive I/O operations support
- Integrated Gemini API for language and image understanding
- Logic control nodes for complex workflows

## 📦 Installation

### Requirements

- ComfyUI (installed and running)
- Python 3.x
- Required Python packages:
  - numpy
  - pillow
  - google-genai (for Gemini nodes)
  - openai (for OpenAI and OpenRouter nodes)
  - requests (for API calls)
  - opencv-python (for Poisson Blend)

### Installation Steps

1. Navigate to your ComfyUI custom nodes directory:
```bash
cd custom_nodes
```

2. Clone this repository:
```bash
git clone https://github.com/yogurt7771/ComfyUI-YogurtNodes.git
```

3. Install dependencies:
```bash
cd ComfyUI-YogurtNodes
pip install -r requirements.txt
```

## 🚀 Usage

1. Start ComfyUI
2. Look for "Yogurt Nodes" category in the node browser
3. Drag and drop desired nodes into your workflow

## 🔧 Available Nodes

All nodes are marked with "YogurtNodes" prefix for easy identification in the ComfyUI interface.

### Image Processing Nodes

#### Batch Images
- **Category:** YogurtNodes/Image
- **Description:** Combines multiple images into a batch with customizable settings
- **Features:**
  - Support for up to 16 input images
  - Multiple interpolation methods (nearest, bilinear, bicubic, etc.)
  - Various resizing methods (stretch, fill/crop, pad)
  - Customizable padding values
  - Flexible batch slicing with start, end, and step parameters

#### Add Text To Image
- **Category:** YogurtNodes/Image
- **Description:** Adds text overlay to images with extensive customization options
- **Features:**
  - Text placement at top or bottom
  - Center alignment option
  - Multiple font support
  - Customizable font size
  - Text and background color configuration
  - Multi-line text support with automatic wrapping

#### Poisson Blend
- **Category:** YogurtNodes/Image
- **Description:** Uses OpenCV Poisson blending (seamlessClone) to blend foreground into background
- **Features:**
  - Seamless blending using OpenCV's Poisson editing
  - Customizable blend position and size
  - Automatic mask processing and resizing
  - Supports various image formats

#### Range
- **Category:** YogurtNodes/Number
- **Description:** Generate a sequence of numbers within a specified range
- **Features:**
  - Customizable start, end, step, or count
  - Outputs torch tensor, count, and step

#### RangeItem
- **Category:** YogurtNodes/Number
- **Description:** Extract a value from a range sequence by index
- **Features:**
  - Supports negative index
  - Outputs string, int, and float

### String Processing Nodes

#### String Lines Count
- **Category:** YogurtNodes/String
- **Description:** Counts the number of lines in a multiline string
- **Features:**
  - Optional line stripping
  - Empty line filtering control
  - Configurable counting behavior

#### String To Value
- **Category:** YogurtNodes/String
- **Description:** Converts string input to multiple value types
- **Features:**
  - Automatic conversion to integer
  - Automatic conversion to float
  - Preserves original string
  - Safe conversion with fallback values

#### String Lines Switch
- **Category:** YogurtNodes/String
- **Description:** Extracts a specific line from a multiline string by index
- **Features:**
  - Line indexing
  - Multiple output formats (string, int, float)
  - Line count output
  - Empty line handling options

#### Replace Delimiter
- **Category:** YogurtNodes/String
- **Description:** Replaces delimiters in strings with custom separators
- **Features:**
  - Regular expression support
  - Custom delimiter specification
  - Flexible replacement options

#### Split Path
- **Category:** YogurtNodes/String
- **Description:** Splits file paths into their component parts
- **Features:**
  - Path component extraction
  - Returns parent directory
  - Filename and extension separation
  - Multiple format options for extensions

#### Regex Node
- **Category:** YogurtNodes/String
- **Description:** Regex-based extraction and replacement for multiline text
- **Features:**
  - Supports 'extract' and 'replace' modes
  - Group reference and formatting
  - Extract or replace by count/order
  - Suitable for complex text processing

### Logic Processing Nodes

#### None Node
- **Category:** YogurtNodes/Logic
- **Description:** A utility node that returns None as its output
- **Use Case:** Useful for conditional workflows where a null value is needed

#### Pack Any
- **Category:** YogurtNodes/Logic
- **Description:** Packs multiple input items into a single output
- **Features:**
  - Support for up to 8 input items
  - Handles any data type
  - Simplifies complex workflows

#### Unpack Any
- **Category:** YogurtNodes/Logic
- **Description:** Unpacks input items into multiple outputs
- **Features:**
  - Seamlessly works with Pack Any node
  - Outputs up to 8 separate items
  - Useful for data distribution

#### Switch
- **Category:** YogurtNodes/Logic
- **Description:** Condition-based switch node
- **Features:**
  - Regular expression matching support
  - Up to 8 condition branches
  - Default value option
  - Flexible condition control

### Model Selection Nodes

#### ControlNet Selector
- **Category:** YogurtNodes/Models
- **Description:** Advanced ControlNet model selection and configuration
- **Features:**
  - Dynamic model list from available ControlNets
  - Adjustable strength parameter
  - Start and end percentage control
  - Model path and name extraction
  - None option for conditional workflows

#### Diffusion Model Selector
- **Category:** YogurtNodes/Models
- **Description:** Stable Diffusion model selection utility
- **Features:**
  - Dynamic list of available diffusion models
  - Trigger word support
  - Model path and name extraction
  - None option for conditional workflows

#### Checkpoint Selector
- **Category:** YogurtNodes/Models
- **Description:** Checkpoint model selection and management
- **Features:**
  - Dynamic checkpoint list
  - Trigger word support
  - Model information extraction
  - None option for conditional workflows

#### Lora Selector
- **Category:** YogurtNodes/Models
- **Description:** LoRA model selection and configuration
- **Features:**
  - Dynamic LoRA model list
  - Separate model and CLIP strength controls
  - Trigger word support
  - Model path and name extraction
  - None option for conditional workflows

### I/O Operation Nodes

#### Save Image Bridge Ex
- **Category:** YogurtNodes/IO
- **Description:** Enhanced image saving functionality with extensive options
- **Features:**
  - Multiple format support (PNG, JPEG)
  - Customizable output directory
  - Dynamic filename prefixes with variables
  - Metadata control
  - Overwrite protection
  - Compression level control
  - Quality settings for JPEG
  - Custom suffix support

#### Save Image Bridge
- **Category:** YogurtNodes/IO
- **Description:** Basic image saving functionality
- **Features:**
  - PNG and JPEG support
  - Basic output options
  - Metadata handling
  - Compression settings

#### Preview Image Bridge
- **Category:** YogurtNodes/IO
- **Description:** Quick image preview functionality
- **Features:**
  - Temporary file handling
  - Fast preview generation
  - Automatic cleanup

#### Save Text Bridge
- **Category:** YogurtNodes/IO
- **Description:** Text file saving with multiple format support
- **Features:**
  - Multiple format support (.txt, .json, .md, .csv)
  - Custom file extensions
  - Dynamic filename generation
  - Overwrite protection
  - UTF-8 encoding support

#### Any Bridge
- **Category:** YogurtNodes/IO
- **Description:** Universal data bridge for workflow control
- **Features:**
  - Handles any data type
  - Optional blackhole mode
  - Workflow control support

#### Create Directory
- **Category:** YogurtNodes/IO
- **Description:** Directory creation utility
- **Features:**
  - Creates single directory
  - Automatic parent directory creation
  - Path validation

#### Glob Files
- **Category:** YogurtNodes/IO
- **Description:** Traverse folders using glob patterns and return matching file path lists
- **Features:**
  - Support for glob and rglob patterns
  - Flexible sorting options (alphabetical, reverse)
  - File-only filtering option
  - Path format options (POSIX, absolute, resolved)
  - Customizable search modes

#### Save Mask Bridge Ex
- **Category:** YogurtNodes/IO
- **Description:** Enhanced mask saving node, supports multiple formats and custom suffix
- **Features:**
  - Supports PNG/JPEG/custom formats
  - Custom output directory, filename prefix, suffix
  - Metadata, compression, overwrite protection

#### Save Mask Bridge
- **Category:** YogurtNodes/IO
- **Description:** Basic mask saving node
- **Features:**
  - Supports PNG/JPEG formats
  - Custom output directory, filename prefix
  - Metadata, compression, overwrite protection

#### Save Mask Bridge Simple
- **Category:** YogurtNodes/IO
- **Description:** Simplified mask saving node
- **Features:**
  - Minimal parameters, quick mask saving

#### Preview Mask Bridge
- **Category:** YogurtNodes/IO
- **Description:** Mask preview node
- **Features:**
  - Saves mask as temporary file for quick preview

### Language Model Nodes

#### Gemini Generate Text
- **Category:** YogurtNodes/LLM
- **Description:** Generate text using Gemini API
- **Features:**
  - Support for various Gemini models
  - System and user prompt control
  - Customizable generation parameters (temperature, top_p, top_k, etc.)
  - Safety settings control
  - Maximum output token count
  - Automatic retry mechanism

#### Gemini Image Understand
- **Category:** YogurtNodes/LLM
- **Description:** Image understanding using Gemini API
- **Features:**
  - Image content analysis
  - Combined with text prompts
  - Customizable generation parameters
  - Multi-language support
  - Detailed image descriptions

#### Gemini Generate Image
- **Category:** YogurtNodes/LLM
- **Description:** Generate images using Gemini API
- **Features:**
  - Support for various Gemini image generation models
  - System and user prompt control
  - Customizable generation parameters (temperature, top_p, top_k, etc.)
  - Safety settings control
  - Maximum output token count
  - Automatic retry mechanism
  - Outputs image (torch.Tensor), text description, and image count

#### OpenAI Generate Text
- **Category:** YogurtNodes/LLM
- **Description:** Generate text using OpenAI API
- **Features:**
  - Support for various OpenAI models (GPT-4, GPT-3.5, etc.)
  - Custom base URL support for compatible APIs
  - System and user prompt control
  - Customizable generation parameters (temperature, top_p, max_tokens, etc.)
  - Frequency and presence penalty controls
  - Seed support for reproducible outputs
  - Automatic retry mechanism
  - Dynamic model list fetching

#### OpenAI Image Understand
- **Category:** YogurtNodes/LLM
- **Description:** Image understanding using OpenAI vision models
- **Features:**
  - Support for OpenAI vision models (GPT-4V, GPT-4o, etc.)
  - Multi-image analysis support
  - Combined image and text prompt processing
  - Custom base URL support for compatible APIs
  - Customizable generation parameters
  - High-quality image detail processing
  - Automatic retry mechanism

#### OpenRouter Generate Text
- **Category:** YogurtNodes/LLM
- **Description:** Generate text using OpenRouter API
- **Features:**
  - Support for various OpenRouter models
  - Custom infrastructure provider selection
  - System and user prompt control
  - Customizable generation parameters (temperature, top_p, max_tokens)
  - Chat template support for message formatting
  - History support for conversation continuity
  - Automatic retry mechanism
  - Dynamic model list fetching

#### OpenRouter Image Understand
- **Category:** YogurtNodes/LLM
- **Description:** Image understanding using OpenRouter vision models
- **Features:**
  - Support for OpenRouter vision models
  - Multi-image analysis support
  - Combined image and text prompt processing
  - Custom infrastructure provider selection
  - Customizable generation parameters
  - History support for conversation continuity
  - Automatic retry mechanism

#### History Builder
- **Category:** YogurtNodes/LLM
- **Description:** Build and manage conversation history compatible with all LLM nodes
- **Features:**
  - Compatible HISTORY type output for seamless integration
  - Incremental history building with user and assistant messages
  - Automatic message filtering (empty messages ignored)
  - Simple and focused functionality
  - Essential for maintaining conversation context across LLM calls

## 🔑 Gemini API Key Setup

Before using Gemini-related nodes, you must obtain and configure your Gemini API Key. There are three supported methods, in the following order of priority:

1. **Code Argument**
   - Pass the `api_key` argument directly when initializing `GeminiClient` (highest priority).

2. **api_key.json File**
   - Create an `api_key.json` file in `custom_nodes/ComfyUI-YogurtNodes/yogurt_nodes/llm/` with the following content:
     ```json
     {
       "gemini": "YOUR_API_KEY"
     }
     ```
   - This will be used only if the code argument is not provided.

3. **Environment Variable**
   - Set the environment variable `GEMINI_API_KEY` (used only if the above two are not set).
   - Example (Windows command line):
     ```cmd
     set GEMINI_API_KEY=YOUR_API_KEY
     ```

If the API Key is not configured correctly, Gemini nodes will not work. You can obtain your API Key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## 🔑 OpenAI API Key Setup

Before using OpenAI-related nodes, you must obtain and configure your OpenAI API Key. There are three supported methods, in the following order of priority:

1. **Code Argument**
   - Pass the `api_key` argument directly when initializing `OpenAIClient` (highest priority).

2. **api_key.json File**
   - Create an `api_key.json` file in `custom_nodes/ComfyUI-YogurtNodes/yogurt_nodes/llm/` with the following content:
     ```json
     {
       "openai": "YOUR_API_KEY",
       "openai_base_url": "https://api.openai.com/v1"
     }
     ```
   - The `openai_base_url` is optional and defaults to the official OpenAI API.
   - This will be used only if the code argument is not provided.

3. **Environment Variable**
   - Set the environment variables `OPENAI_API_KEY` and optionally `OPENAI_BASE_URL` (used only if the above two are not set).
   - Example (Windows command line):
     ```cmd
     set OPENAI_API_KEY=YOUR_API_KEY
     set OPENAI_BASE_URL=https://api.openai.com/v1
     ```

### Custom Base URL Support

The OpenAI nodes support custom base URLs, making them compatible with:
- Official OpenAI API
- Azure OpenAI Service
- OpenAI-compatible APIs (like LocalAI, Ollama, etc.)
- Self-hosted OpenAI-compatible servers

Simply set the `base_url` parameter to your preferred endpoint.

If the API Key is not configured correctly, OpenAI nodes will not work. You can obtain your API Key from [OpenAI Platform](https://platform.openai.com/api-keys).

## 🔑 OpenRouter API Key Setup

Before using OpenRouter-related nodes, you must obtain and configure your OpenRouter API Key. There are three supported methods, in the following order of priority:

1. **Code Argument**
   - Pass the `api_key` argument directly when initializing `OpenRouterClient` (highest priority).

2. **api_key.json File**
   - Create an `api_key.json` file in `custom_nodes/ComfyUI-YogurtNodes/yogurt_nodes/llm/` with the following content:
     ```json
     {
       "openrouter": "YOUR_API_KEY"
     }
     ```
   - This will be used only if the code argument is not provided.

3. **Environment Variable**
   - Set the environment variable `OPENROUTER_API_KEY` (used only if the above two are not set).
   - Example (Windows command line):
     ```cmd
     set OPENROUTER_API_KEY=YOUR_API_KEY
     ```

If the API Key is not configured correctly, OpenRouter nodes will not work. You can obtain your API Key from [OpenRouter Platform](https://openrouter.ai/keys).

## 🤝 Contributing

Pull Requests are welcome to help improve the project!

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

For questions, bug reports, or feature requests, please [open an issue](https://github.com/yogurt7771/ComfyUI-YogurtNodes/issues).

## 🙏 Acknowledgments

- ComfyUI Community
- All Contributors 