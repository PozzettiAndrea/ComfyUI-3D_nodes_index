# Ino Custom Nodes for ComfyUI

A comprehensive collection of custom nodes for ComfyUI that provides advanced file handling, S3 cloud storage integration, OpenAI-powered helpers, Basic Auth middleware, LoRA configuration management, and various utility functions.

## Installation

### Option 1: Using ComfyUI-Manager (Recommended)
1. Install [ComfyUI](https://docs.comfy.org/get_started)
2. Install [ComfyUI-Manager](https://github.com/ltdrdata/ComfyUI-Manager)
3. Search for "ComfyUI Ino Nodes" in ComfyUI-Manager and install
4. Restart ComfyUI

### Option 2: Manual Installation
1. Clone this repository into your ComfyUI custom_nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/nobandegani/comfyui_ino_nodes.git
   ```
2. Install dependencies:
   ```bash
   cd comfyui_ino_nodes
   pip install -r requirements.txt
   ```
3. Restart ComfyUI

### Dependencies
- `inocloudreve` - Cloudreve cloud storage integration
- `inopyutils` - Utility functions
- `openai` - OpenAI API client (used by OpenAI helper nodes)
- `aiohttp` - Async HTTP and server middleware support
- `numpy`, `Pillow`, `torch` - Core libraries required by ComfyUI and several nodes

## Node Categories & Documentation

### 🗂️ File & Path Utilities (InoNodes)

#### **Ino Parse File Path**
Extracts and parses components from file paths.
- **Inputs**: `file_path` (string)
- **Outputs**: File name, directory, extension, and other path components
- **Use Case**: Parse file paths for batch processing or file organization

#### **Ino Count Files**
Counts files in directories with optional pattern matching.
- **Inputs**: `file_path` (directory path), `file_pattern` (optional filter)
- **Outputs**: File count and directory information
- **Use Case**: Batch processing workflows that need to know dataset sizes

#### **Ino Branch Image**
Conditionally routes images based on boolean input.
- **Inputs**: `boolean` (condition), `input_image` (optional image)
- **Outputs**: Routed image based on condition
- **Use Case**: Conditional image processing workflows

#### **Ino Get Folder Batch ID**
Generates unique batch identifiers for folder-based workflows.
- **Inputs**: `enabled`, `seed`, `batch_type`, `creator_name`, `get_last_one`, `parent_path`
- **Outputs**: Unique batch ID for organizing outputs
- **Use Case**: Organize generated content into structured batches

#### **Ino DateTime As String**
Generates formatted datetime strings with customizable components.
- **Inputs**: `seed`, date/time component toggles, separators
- **Outputs**: Formatted datetime string
- **Use Case**: Timestamp generation for file naming and organization

### 🔧 Basic Utility Nodes (InoNodes)

#### **Ino Not Boolean**
Performs boolean negation operation.
- **Inputs**: `boolean` (input value)
- **Outputs**: Negated boolean value
- **Use Case**: Logic operations in conditional workflows

#### **Ino Int Equal**
Compares two integers for equality.
- **Inputs**: `int_a`, `int_b` (integer values)
- **Outputs**: Boolean result of equality comparison
- **Use Case**: Conditional logic based on numeric comparisons

#### **Ino String Toggle Case**
Toggles string case (upper/lower) based on settings.
- **Inputs**: `enabled`, `input_string`, `toggle_to` (case option)
- **Outputs**: Case-modified string
- **Use Case**: Text formatting and standardization

#### **Ino Bool To Switch**
Converts boolean values to switch/selector format.
- **Inputs**: `enabled`, `input_bool`
- **Outputs**: Switch-compatible output
- **Use Case**: Interface compatibility between different node types

#### **Ino String To Combo**
Converts string input to combo/dropdown selection format.
- **Inputs**: `enabled`, `input_string`
- **Outputs**: Combo-compatible selection
- **Use Case**: Dynamic UI element generation

#### **Ino Random Int In Range**
Generates random integers within specified range.
- **Inputs**: `enabled`, `int_min`, `int_max`, `length`
- **Outputs**: Random integer(s) within range
- **Use Case**: Randomization for procedural generation

#### **Ino Int To String**
Converts integer values to string format.
- **Inputs**: `input_int` (integer value)
- **Outputs**: String representation
- **Use Case**: Data type conversion for text processing

#### **Ino Int To Float**
Converts integer values to float.
- **Inputs**: `input_int`
- **Outputs**: Float value
- **Use Case**: Numeric conversions for downstream nodes

#### **Ino Float To Int**
Converts floating-point values to integer using a selected method.
- **Inputs**: `input_float`, `method` (round/floor/ceil)
- **Outputs**: Integer value
- **Use Case**: Numeric conversions and clamping

#### **Ino Save Images**
Saves a batch of images with a given filename prefix.
- **Inputs**: `images` (IMAGE), `filename_prefix` (string)
- **Outputs**: Saved images with standardized filenames
- **Use Case**: Persist generated outputs with consistent naming

#### **Ino Image Resize By Longer Side V1**
Resizes an image so that its longer side matches a target size, preserving aspect ratio.
- **Inputs**: `image`, `size`, `interpolation_mode`
- **Outputs**: Resized image
- **Use Case**: Preprocess images to a standard maximum side length

#### **Ino Image Resize By Longer Side And Crop V2**
Resizes then optionally crops/pads to target dimensions with positioning control.
- **Inputs**: `image`, `target_width`, `target_height`, `padding_color`, `interpolation`, `crop`, `position`, `x`, `y`
- **Outputs**: Processed image
- **Use Case**: Prepare images to exact sizes for models/pipelines while controlling crop position

### 📁 File Operations (InoFileHelper)

#### **Increment Batch Name**
Auto-increments batch names for sequential processing.
- **Inputs**: `enabled`, `seed`, batch naming parameters
- **Outputs**: Incremented batch name
- **Use Case**: Automated batch processing with sequential naming

#### **Zip**
Creates zip archives from files and folders.
- **Inputs**: `enabled`, `seed`, source path, destination path
- **Outputs**: Success status and archive information
- **Use Case**: Compress generated content for storage or sharing

#### **Unzip**
Extracts files from zip archives.
- **Inputs**: `enabled`, `seed`, zip path, output path
- **Outputs**: Extraction status and file information
- **Use Case**: Extract datasets or batch process archived content

#### **Remove File**
Safely removes files from the filesystem.
- **Inputs**: `enabled`, `seed`, `file_path`
- **Outputs**: Deletion status and confirmation
- **Use Case**: Cleanup operations and file management

#### **Remove Folder**
Safely removes folders and their contents.
- **Inputs**: `enabled`, `seed`, `folder_path`
- **Outputs**: Deletion status and confirmation
- **Use Case**: Cleanup operations and directory management

### 🌐 JSON & Data Processing (InoNodes)

#### **Ino Json**
Manipulates JSON objects by adding or modifying fields.
- **Inputs**: `base_json` (JSON string), `field_name`, `field_value`
- **Outputs**: Success status, message, modified JSON
- **Use Case**: Dynamic JSON configuration and data manipulation

#### **Ino Save Json**
Saves JSON strings to files in the output directory.
- **Inputs**: `json_string`, `local_path`
- **Outputs**: Save status and confirmation message
- **Use Case**: Export configuration data and processing results

### 🌍 HTTP Operations (InoNodes)

#### **Ino Http Call**
Performs HTTP requests with comprehensive options.
- **Inputs**: `enabled`, `url`, `request_type` (GET/POST/PUT/DELETE/PATCH), `headers`, `json_payload`
- **Optional**: `trust_env`, `follow_redirects`, `enable_retries`, `max_retries`
- **Outputs**: Success status, status code, message, response
- **Use Case**: API integration, webhook calls, external service communication

### ☁️ S3 Cloud Storage (InoS3Helper)

#### **Ino S3 Config**
Configures S3 connection settings and credentials.
- **Inputs**: S3 credentials and configuration parameters
- **Outputs**: S3 client configuration
- **Use Case**: Initialize S3 connections for upload/download operations

#### **Ino S3 Upload Image**
Uploads images to S3 storage with metadata preservation.
- **Inputs**: Image data, S3 path, metadata options
- **Outputs**: Upload status and S3 URL
- **Use Case**: Cloud backup of generated images

#### **Ino S3 Upload File**
Uploads any file type to S3 storage.
- **Inputs**: File path, S3 destination, upload options
- **Outputs**: Upload status and S3 location
- **Use Case**: Cloud backup of models, datasets, or processed files

#### **Ino S3 Upload Folder**
Uploads entire folders to S3 with structure preservation.
- **Inputs**: Local folder path, S3 destination path
- **Outputs**: Upload status and file count
- **Use Case**: Batch upload of training datasets or output collections

#### **Ino S3 Upload String**
Uploads a text/string payload as an object to S3.
- **Inputs**: String content, destination path, content type
- **Outputs**: Upload status and S3 URL
- **Use Case**: Save JSON, prompts, or logs directly to S3

#### **Ino S3 Download Image**
Downloads images from S3 storage.
- **Inputs**: S3 image path, download options
- **Outputs**: Downloaded image data
- **Use Case**: Retrieve reference images or previously uploaded content

#### **Ino S3 Download File**
Downloads files from S3 storage.
- **Inputs**: S3 file path, local destination
- **Outputs**: Download status and local file path
- **Use Case**: Retrieve models, datasets, or configuration files

#### **Ino S3 Download Folder**
Downloads entire folders from S3 with structure preservation.
- **Inputs**: S3 folder path, local destination path
- **Outputs**: Download status and file count
- **Use Case**: Retrieve complete datasets or backup collections

### ☁️ Cloudreve Integration (InoCloudreve)

#### **Cloudreve Init**
Initializes connection to Cloudreve cloud storage server.
- **Inputs**: `enabled`, `seed`, `server_address`
- **Outputs**: Connection status and messages
- **Use Case**: Setup Cloudreve cloud storage connection

#### **Cloudreve Signin**
Authenticates with Cloudreve using email and password.
- **Inputs**: `enabled`, `seed`, `email`, `password`
- **Outputs**: Authentication status and session information
- **Use Case**: Login to Cloudreve for file operations

#### **Cloudreve Upload File**
Uploads files to Cloudreve cloud storage.
- **Inputs**: `enabled`, `seed`, `local_path`, `cloud_path`, `storage_policy`
- **Outputs**: Upload status and confirmation
- **Use Case**: Cloud backup using Cloudreve storage

### 🎨 Prompt Generation (InoNodes)

#### **Ino Random Character Prompt**
Generates detailed random character prompts with facial features, makeup, and styling options.
- **Inputs**: Seed, various toggle options for different facial features
- **Outputs**: Complete character description prompt and seed
- **Use Case**: Generate diverse character prompts for portrait generation

### 🧮 LoRA Configuration (InoNodes)

#### **Ino Calculate Lora Config**
Calculates optimal LoRA training parameters based on dataset characteristics.
- **Inputs**: `enabled`, `dataset_count`, `max_batch_size`, `target_epochs`, `max_lora_parts`
- **Outputs**: Comprehensive LoRA training configuration (dim, alpha, steps, batch size, learning rate, etc.)
- **Use Case**: Optimize LoRA training settings for custom models

### 🔬 Sampling & Model Management (InoSamplerHelper)

#### **Ino Random Noise**
Generates random noise for sampling operations.
- **Outputs**: Random noise tensor for sampling
- **Use Case**: Initialize sampling processes with randomized starting points

#### **Ino Get Model Config**
Retrieves model configuration settings.
- **Inputs**: Model configuration parameters
- **Outputs**: Current model configuration
- **Use Case**: Load saved model settings for consistent generation

#### **Ino Show Model Config**
Displays current model configuration for review.
- **Inputs**: Configuration data
- **Outputs**: Formatted configuration display
- **Use Case**: Debug and verify model settings

#### **Ino Update Model Config**
Updates and modifies model configuration parameters.
- **Inputs**: Configuration data and new parameters
- **Outputs**: Updated configuration
- **Use Case**: Dynamically adjust model settings during workflows

#### **Ino Get Lora Config**
Retrieves LoRA configuration settings.
- **Inputs**: LoRA configuration parameters
- **Outputs**: Current LoRA settings
- **Use Case**: Load saved LoRA configurations

#### **Ino Show Lora Config**
Displays current LoRA configuration for review.
- **Inputs**: LoRA configuration data
- **Outputs**: Formatted LoRA configuration display
- **Use Case**: Debug and verify LoRA settings

#### **Ino Load Sampler Models**
Loads and manages sampling models.
- **Inputs**: Model specifications and loading parameters
- **Outputs**: Loaded model instances
- **Use Case**: Initialize models for generation workflows

#### **Ino Get Conditioning**
Extracts and processes conditioning data for generation.
- **Inputs**: Configuration, CLIP model, positive/negative prompts
- **Outputs**: Processed conditioning for positive and negative prompts
- **Use Case**: Prepare text conditioning for image generation

#### **Ino Get Sampler Config**
Retrieves sampling configuration and parameters.
- **Inputs**: Sampling configuration parameters
- **Outputs**: Complete sampling configuration
- **Use Case**: Load sampling settings for consistent generation results

### 🧩 Model Utilities (InoModelHelper)

#### **Ino Validate Model**
Validates that a required model file exists locally; if missing, downloads it from S3 using the provided configuration.
- **Inputs**: `enabled`, `s3_config` (STRING), `model_type` (e.g., checkpoints, vae, loras, etc.), `model_name` (e.g., flux1dev/ae.safetensors)
- **Outputs**: `success` (BOOLEAN), `msg` (STRING)
- **Use Case**: Ensure necessary models are present before running a workflow, fetching them automatically from S3 if needed

### 🔐 Basic Auth Middleware (InoBasicAuth)

Adds optional Basic Authentication to ComfyUI's HTTP endpoints using aiohttp middleware.
- Enable by setting environment variables before starting ComfyUI:
  - COMFYUI_USERNAME
  - COMFYUI_PASSWORD
- WebSocket path /ws is excluded to preserve UI connectivity.
- Also provides a simple node: Ino Basic Auth Node that outputs a BASIC_AUTH token for wiring in workflows if needed.

### 🤖 OpenAI Helpers (InoOpenaiHelper)

Nodes to interact with OpenAI's Responses API.
- Ino Openai Config: supply API key, timeout, and retry policy.
- Ino Openai Text Generation: send a prompt to a selected model (e.g., gpt-5) and receive output text and metadata.

## Usage

After installation, the nodes will appear in your ComfyUI node menu under the following categories:
- **InoNodes** - File utilities, basic operations, JSON processing, HTTP calls
- **InoS3Helper** - S3 cloud storage operations
- **InoCloudreve** - Cloudreve cloud storage integration
- **InoFileHelper** - Advanced file operations
- **InoSamplerHelper** - Model and sampling management
- **InoModelHelper** - Model utilities (validation/download)
- **InoOpenaiHelper** - OpenAI integration
- **InoBasicAuth** - Basic authentication utilities

Simply drag and drop the nodes into your ComfyUI workflow and configure them according to your needs. Most nodes include enable/disable toggles for conditional execution and detailed error handling.

## Requirements

- ComfyUI (latest version recommended)
- Python 3.8+
- Dependencies listed in `requirements.txt` (most are auto-installed when using pip or ComfyUI-Manager)

## License

This project is licensed under the terms specified in the LICENSE file.

## Support

For issues and questions, please visit the [GitHub repository](https://github.com/nobandegani/comfyui_ino_nodes).

---

**Version:** 1.2.2
**Publisher:** Inoland
**Contact:** contact@inoland.net
