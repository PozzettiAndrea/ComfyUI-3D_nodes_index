# Chye ComfyUI Toolset

A comprehensive collection of ComfyUI custom nodes organized by category for enhanced workflow productivity.

## 🎯 Features

### 🔹 Latent Tools
- **Model-Specific Aspect Ratios**: Optimized presets for Flux, Qwen Image, and SDXL models
- **Phone Screen Sizes**: Common mobile device resolutions including modern tall screens
- **Video Formats**: Standard video resolutions from 480p to 4K including cinema formats
- **Social Media Formats**: Optimized sizes for Instagram, TikTok, YouTube, Facebook, and Twitter
- **Smart Orientation Control**: Automatic Portrait/Landscape switching
- **Precision Scaling**: Multiplier with automatic rounding to multiples of 32
- **Batch Generation**: Support for multiple latents at once

### 🔸 Post Process Tools
- **Realistic Film Grain**: Apply photographic film grain simulation with ISO control
- **ARRI Halation Effect**: Simulate film bloom around highlights with comprehensive color grading controls
- **Global Color Grading**: Apply comprehensive color grading to entire images (temperature, saturation, tint, gamma, exposure, contrast)
- **Chromatic Aberration**: Lens color fringing simulation with barrel distortion
- **Spatially Correlated Noise**: Advanced noise generation using scipy for realistic grain patterns
- **Color Channel Control**: Option for monochrome or colored grain effects

### 🔤 Prompt Tools
- **Multi-Provider LLM Integration**: DeepSeek, OpenAI, Anthropic, and custom providers
- **Dual Template Systems**: File-based templates AND editable text input options
- **Secure API Key Management**: File-based storage with gitignore protection
- **Automatic Setup**: Dedicated setup node creates folder structure with examples
- **Professional Templates**: Photography, cinematic, and high-detail enhancement templates
- **Error Handling**: Graceful degradation with comprehensive error reporting
- **Wildcard Generation**: Randomize prompts with {option1|option2|option3} syntax for models without native wildcard support

### 📁 File Tools
- **📁 CYH File | Folder Filename Builder** - Construct file paths with project name, subfolder, and filename
- **📄 CYH File | Text File Loader** - Load text content from .txt files with trigger button and editable text box
- **📄 CYH File | Text File Editor** - Editable text widget with action modes for controlling output behavior (use_input/use_edit_mute_input)
- **🎬 CYH File | Video Loader** - Load video files from text paths for ComfyUI video processing


### 🔧 Utility Tools *(Coming Soon)*
- Workflow helpers
- Data conversion utilities
- Debug and analysis tools

## 📦 Installation

### Method 1: Git Clone (Recommended)
```bash
cd custom_nodes
git clone https://github.com/chyer/Chye-ComfyUI-Toolset.git
cd Chye-ComfyUI-Toolset
echo "Chye-ComfyUI-Toolset" > .git/.cnr-id

# Install dependencies
pip install -r requirements.txt
```

### Method 2: Manual Copy
1. Copy the `Chye-ComfyUI-Toolset` folder to your ComfyUI `custom_nodes` directory
2. **Important**: Create a file named `.cnr-id` in the `.git` folder with content `Chye-ComfyUI-Toolset` to avoid workflow errors
   ```bash
   echo "Chye-ComfyUI-Toolset" > .git/.cnr-id
   ```
3. Install dependencies:
   ```bash
   cd Chye-ComfyUI-Toolset
   pip install -r requirements.txt
   ```
4. Restart ComfyUI

## 🚀 Usage

### Latent Tools
Find the nodes under the **latent** category:

#### Model-Specific Nodes
- **🔹 CYH Latent | Flux Aspect Ratio** - Flux-optimized latent generation
- **🔹 CYH Latent | Qwen Aspect Ratio** - Qwen Image-optimized latent generation
- **🔹 CYH Latent | SDXL Aspect Ratio** - SDXL-optimized latent generation

#### Phone Screen Nodes
- **🔹 CYH Latent | Phone Aspect Ratio** - Common mobile device resolutions

#### Video Format Nodes
- **🔹 CYH Latent | Video Aspect Ratio** - Standard video resolutions and formats

#### Social Media Nodes
- **🔹 CYH Latent | Social Media Aspect Ratio** - Optimized sizes for social platforms

#### Configuration Options:
- **Aspect Ratio**: Choose from category-specific presets
- **Orientation**: Portrait or Landscape (with smart defaults based on media type)
- **Multiplier**: Scale resolution (0.1-10.0)
- **Batch Size**: Number of latents to generate (1-64)

#### Example Workflow:
```
[🔹 CYH Latent | Flux Aspect Ratio] → [KSampler] → [VAE Decode]
```

#### Multiplier Example:
```
Model: SDXL
Aspect: 16:9
Orientation: Landscape
Multiplier: 1.5
→ Output: 1536×864 latent
```

## 🎬 Post Process Tools

Find the nodes under the **post_process** category:

- **🎬 CYH Post Process | Film Grain** - Apply realistic film grain simulation
  - **Strength**: Overall grain intensity (0.0 to 1.0)
  - **ISO**: Simulated film sensitivity (100-6400)
  - **Grain Size**: Particle size control (1.0-10.0)
  - **Colored**: Toggle between monochrome or colored grain

- **🎬 CYH Post Process | ARRI Halation** - Apply ARRI-style film bloom effect with comprehensive color grading
  - **Threshold**: Highlight detection threshold (0-255)
  - **Blur Size**: Glow effect size (1-101, odd numbers)
  - **Intensity**: Halation strength (0.0 to 1.0)
  - **Temperature**: Color temperature in Kelvin (1000-40000K) - warm to cool colors
  - **Saturation**: Color intensity (0.0-2.0) - desaturated to oversaturated
  - **Tint**: Green-magenta shift (-1.0 to 1.0) - green tint to magenta tint
  - **Gamma**: Gamma correction (0.5-2.5) - flat to contrasty
  - **Exposure**: Exposure adjustment in EV stops (-4.0 to 4.0) - dark to bright
  - **Contrast**: Contrast adjustment (0.5-2.0) - low to high contrast

- **🎨 CYH Post Process | Global Color Grading** - Apply comprehensive color grading to entire images
  - **Temperature**: Color temperature in Kelvin (1000-40000K) - warm to cool colors
  - **Saturation**: Color intensity (0.0-2.0) - desaturated to oversaturated
  - **Tint**: Green-magenta shift (-1.0 to 1.0) - green tint to magenta tint
  - **Gamma**: Gamma correction (0.5-2.5) - flat to contrasty
  - **Exposure**: Exposure adjustment in EV stops (-4.0 to 4.0) - dark to bright
  - **Contrast**: Contrast adjustment (0.5-2.0) - low to high contrast

- **🌈 CYH Post Process | Chromatic Aberration** - Apply lens color fringing effect
  - **Preset**: Quick configurations (None, Vintage, Modern, Extreme, Custom)
  - **Intensity**: Master effect strength multiplier (0.0-2.0)
  - **Center**: Adjustable distortion center point (0.0-1.0)
  - **Quality**: Fast (bilinear) or High (bicubic) interpolation
  - **Advanced Controls**: Individual RGB channel distortion coefficients (k1, k2, k3)

#### Preset Details:
- **None**: No chromatic aberration
- **Vintage**: Classic lens look with red/blue separation
- **Modern**: Subtle modern lens character
- **Extreme**: Strong artistic effect with complex distortion

#### Example Workflows:
```
[KSampler] → [VAE Decode] → [🎬 CYH Post Process | Film Grain]
```
```
[KSampler] → [VAE Decode] → [🎬 CYH Post Process | ARRI Halation]
```
```
[KSampler] → [VAE Decode] → [🌈 CYH Post Process | Chromatic Aberration]
```
```
[KSampler] → [VAE Decode] → [🎨 CYH Post Process | Global Color Grading]

## 🔤 Prompt Tools

Find the nodes under the **prompt_tools** category:

- **🔤 CYH Prompt Tools | Setup** - Creates folder structure and example templates
  - **Force Recreate**: Overwrite existing files (True/False)
  - **Output**: Status message with setup results

- **🔤 CYH Prompt Tools | Enhancer** - Uses LLM APIs to refine and enhance prompts
  - **Prompt**: Input prompt to enhance (multiline text)
  - **Template Path**: Path to template file (e.g., "providers/deepseek/professional_photo.txt")
  - **Provider**: LLM provider (DeepSeek, OpenAI, Anthropic, Custom)
  - **API Key Override**: Optional API key override (skips file lookup)
  - **Temperature**: Creativity control (0.0-1.0)
  - **Max Tokens**: Response length limit (100-4000)

- **🔤 CYH Prompt Tools | Enhancer (Editable)** - Alternative version with editable preprompt template
  - **Prompt**: Input prompt to enhance (multiline text)
  - **Preprompt Template**: Editable template text (must include {prompt} placeholder)
  - **Provider**: LLM provider (DeepSeek, OpenAI, Anthropic, Custom)
  - **API Key Override**: Optional API key override (skips file lookup)
  - **Temperature**: Creativity control (0.0-1.0)
  - **Max Tokens**: Response length limit (100-4000)

### Setup Instructions:

1. **Run Setup Node First**: Use "🔤 CYH Prompt Tools | Setup" to create folder structure
2. **Configure API Keys**: Edit files in `Presets/api_keys/` with your actual API keys
3. **Customize Templates**: Modify or create templates in `Presets/Preprompts/` subdirectories
4. **Use Enhancer**: Connect prompts to "🔤 CYH Prompt Tools | Enhancer" for refinement

### Example Templates:
- **Professional Photography**: Camera settings, lighting, composition techniques
- **Cinematic Style**: Film terminology, director styles, visual storytelling
- **High Detail**: Ultra-realistic textures, technical precision, intricate patterns

### Supported Providers:
- **DeepSeek**: Fast and cost-effective Chinese LLM
- **OpenAI**: GPT-4 Turbo for high-quality enhancements
- **Anthropic**: Claude models for nuanced prompt refinement
- **Custom**: Template-only mode without API calls

### Example Workflows:
```
[Text Input] → [🔤 CYH Prompt Tools | Enhancer] → [KSampler]
```
```
[🔤 CYH Prompt Tools | Setup] → [Configure API Keys] → [🔤 CYH Prompt Tools | Enhancer]
```
```
[Text Input] → [🔤 CYH Prompt Tools | Enhancer (Editable)] → [KSampler]
```

### When to Use Each Version:
- **File-based Enhancer**: Use when you want to maintain reusable templates across workflows
- **Editable Enhancer**: Use when you want to quickly modify or experiment with preprompt text directly in the node
- **Both versions support the same API providers and configuration options**

### Wildcard Generator
- **🔤 CYH Prompt Tools | Wildcard Generator** - Generate randomized prompts using wildcard syntax {option1|option2|option3}
  - **Prompt**: Input text with wildcard expressions
  - **Seed**: Random seed for reproducible results (0 for random)
  - **Output**: Randomized prompt with wildcards replaced

#### Wildcard Examples:
- Input: "A {beautiful|stunning|gorgeous} {landscape|cityscape|seascape}"
- Possible outputs: "A beautiful landscape", "A stunning cityscape", "A gorgeous seascape"

#### Example Workflows:
```
[Text Input] → [🔤 CYH Prompt Tools | Wildcard Generator] → [KSampler]
```
```
[🔤 CYH Prompt Tools | Wildcard Generator] → [🔤 CYH Prompt Tools | Enhancer] → [KSampler]
```

### Folder Structure:
```
Presets/
├── api_keys/           # API key files (gitignored)
│   ├── deepseek_api_key.txt
│   ├── openai_api_key.txt
│   └── anthropic_api_key.txt
├── Preprompts/         # Template files (.txt)
│   ├── professional_photo.txt
│   ├── cinematic.txt
│   ├── high_detail.txt
│   └── custom/         # User-defined templates
```
```
## 📁 File Tools

Find the nodes under the **file** category:

- **📁 CYH File | Folder Filename Builder** - Construct file paths with project name, subfolder, and filename
  - **Project Name**: Base project identifier
  - **Filename**: Output filename (without extension)
  - **Use Subfolders**: Enable/disable subfolder organization
  - **Delimiter**: Path separator (/ or \ or _ or -)
  - **Subfolder**: Optional subfolder name

- **📄 CYH File | Text File Loader** - Load text content from .txt files with trigger button and editable text box
  - **File Path**: Path to .txt file (supports drag & drop)
  - **Trigger**: Load File button to load content
  - **Editable Text**: Loaded text content (editable)
  - **Encoding**: Text encoding (utf-8, utf-16, ascii, latin-1)
  - **Auto Load**: Automatically reload when file changes

- **📄 CYH File | Text File Editor** - Editable text widget with action modes for controlling output behavior
  - **Action**: Control output behavior (use_input/use_edit_mute_input)
  - **Editable Text Widget**: Editable text content
  - **Input Text**: Optional upstream text input

- **🎬 CYH File | Video Loader** - Load video files from text paths for ComfyUI video processing
  - **File Path**: Path to video file (supports drag & drop)
  
  
  
  

### Action Modes:
- **use_input**: Outputs connected text and updates widget display
- **use_edit_mute_input**: Outputs widget text and mutes upstream input








### Example Workflows:
```
[📄 CYH File | Text File Loader] → [📄 CYH File | Text File Editor] → [KSampler]
```
```
[Text Input] → [📄 CYH File | Text File Editor] → [KSampler]
```
```
[🎬 CYH File | Video Loader] → [Get Video Components] (for extracting frames and audio)
```
```
[Video Generator] → [🎬 CYH File | Video Loader] (for loading generated videos)
```
```
[File Path] → [🎬 CYH File | Video Loader] → [Video Processing Nodes] (for video processing workflows)
```

### When to Use Each Version:
- **Text File Loader**: Use when you want to load text from .txt files
- **Text File Editor**: Use when you want editable text with action modes and upstream muting
- **Video Loader**: Use when you want to load video files from text paths for ComfyUI video processing
- **Combined**: Use Text File Loader → Text File Editor for file loading with advanced editing features
## 📱 Phone Screen Resolutions

| Aspect Ratio | Resolution | Description |
|-------------|------------|-------------|
| 16:9 | 1080×1920 | Standard phone screens |
| 19.5:9 | 1080×2340 | Modern tall phones |
| 20:9 | 1080×2400 | Ultra tall phones |
| 18:9 | 1080×2160 | Tall phones |

**Default Orientation**: Portrait (optimized for mobile viewing)

## 🎬 Video Format Resolutions

| Aspect Ratio | Resolution | Description |
|-------------|------------|-------------|
| 16:9 | 1920×1080 | Standard video (Full HD) |
| 21:9 | 1920×810 | Cinema format |
| 4:3 | 1024×768 | Traditional video |
| 9:16 | 1080×1920 | Portrait video |

**Default Orientation**: Landscape (except 9:16 which defaults to Portrait)

## 📱 Social Media Resolutions

| Platform | Format | Resolution | Aspect Ratio |
|----------|--------|------------|-------------|
| Instagram | Square | 1080×1080 | 1:1 |
| Instagram | Portrait | 1080×1350 | 4:5 |
| Instagram | Landscape | 1080×608 | 1.91:1 |
| Instagram | Stories/Reels | 1080×1920 | 9:16 |
| TikTok | Standard | 1080×1920 | 9:16 |
| TikTok | Wide | 1920×1080 | 16:9 |
| YouTube | Standard | 1920×1080 | 16:9 |
| YouTube | Shorts | 1080×1920 | 9:16 |
| Facebook | Feed | 1200×630 | 1.91:1 |
| Facebook | Stories | 1080×1920 | 9:16 |
| Twitter | Tweet | 1200×675 | 16:9 |
| Twitter | Header | 1500×500 | 3:1 |

**Default Orientation**: Platform-specific (Portrait for Instagram Stories/TikTok, Landscape for YouTube Standard, etc.)

## 📐 Resolution Reference

| Model      | 1:1      | 4:3      | 3:2      | 16:9     | 21:9     |
|------------|----------|----------|----------|----------|----------|
| **Flux**   | 1024×1024| 1280×960 | 1152×768 | 1344×768 | 1792×768 |
| **Qwen**   | 1328×1328| 1472×1140| 1536×1024| 1664×928 | 1984×864 |
| **SDXL**   | 1024×1024| 1024×768 | 1152×768 | 1024×576 | 1344×576 |

## 🏗️ Project Structure

```
Chye-ComfyUI-Toolset/
├── categories/
│   ├── latent_tools.py      # Aspect ratio latent generators
│   ├── post_process.py      # Image post-processing tools (film grain, etc.)
│   ├── prompt_tools.py      # LLM-based prompt enhancement tools
│   ├── image_tools.py       # Interactive painting and image processing tools
│   ├── file_tools.py        # File handling tools (text, video, etc.)
│   ├── video_tools.py       # Video loading tools for text path input
│   ├── utility_tools.py     # (Future) Workflow utilities
│   └── __init__.py
├── shared/
│   ├── constants.py         # Common configuration data
│   ├── validators.py        # Input validation utilities
│   ├── helpers.py          # Shared utility functions
│   └── __init__.py
├── Presets/                 # Prompt enhancement templates and API keys
│   ├── api_keys/           # API key files (gitignored)
│   └── Preprompts/         # Template files (.txt)
├── __init__.py             # Main entry point
├── pyproject.toml          # Project metadata
└── README.md              # This file
```
```

## 📝 Notes

- All dimensions are automatically rounded to multiples of 32 for ComfyUI compatibility
- Portrait orientation swaps width/height when the base resolution is landscape-oriented
- Multiplier scales base resolution before rounding
- Modular design allows for easy expansion with new tool categories
- Phone screen nodes default to Portrait orientation for optimal mobile viewing
- Video format nodes have smart defaults based on the aspect ratio (Landscape for most, Portrait for 9:16)
- Social media nodes have platform-specific default orientations for optimal results

## 🔄 Version History

- **v2.10.0**: Added Wildcard Generator node for randomized prompts using {option1|option2|option3} syntax
- **v2.9.0**: Added Video Loader node for loading videos from text paths
- **v2.8.0**: Added Text File Editor node with action modes (use_input/use_edit_mute_input) and UI widget updating
- **v2.7.0**: Added Interactive Painter node with freehand brush drawing
- **v2.6.0**: Added Global Color Grading node with comprehensive color controls
- **v2.5.0**: Enhanced ARRI Halation node with comprehensive color grading controls
- **v2.4.0**: Added PromptEnhancerEditable node with editable preprompt templates
- **v2.3.0**: Added Prompt Enhancement tools with multi-provider LLM integration
- **v2.2.0**: Added Chromatic Aberration node with realistic lens simulation
- **v2.1.0**: Added Phone, Video, and Social Media aspect ratio nodes
- **v2.0.0**: Complete restructure into modular toolset with shared utilities
- **v1.x.x**: Individual aspect ratio nodes

## 🤝 Contributing

This toolset is designed for extensibility. New categories and tools can be easily added following the established patterns in the `categories/` and `shared/` directories.

---

**Happy Creating! 🎨**