# IXIWORKS Tools

Video description, storyboard, and utility custom nodes for ComfyUI.

## Features

### Video Category
- **Video Description (Qwen3-VL)**: Full video analysis with Qwen3-VL-8B-Instruct

### StoryBoard Category
- **JSON Parser**: Parse storyboard JSON files into scene/character data
- **Build Prompt**: Combine scene data into prompts
- **Build Character Prompt**: Generate character descriptions
- **Select Index**: Select specific scene by index
- **Merge Strings**: Combine string arrays with separator

### Utils Category
- **Switch**: Boolean switch between two inputs
- **Switch Case**: Select one of N inputs by index (2~8 inputs)
- **String to List**: Convert multiple string inputs to a list for batch processing
- **Join Strings**: Concatenate two strings with configurable separator
- **Set / Get**: Virtual nodes for wire-free connections (frontend only)

## Installation

### Step 1: Install Base Dependencies

```bash
cd ComfyUI/custom_nodes/ComfyUI-VideoDescription
pip install -r requirements.txt
```

This installs:
- transformers, tokenizers, accelerate (for Qwen3-VL)
- qwen-vl-utils (Qwen3-VL helper library)

## Model Download

**Important**: You need to download the models before using these nodes.

### Model Locations

Models will be downloaded to:
```
ComfyUI/models/video_description/
└── Qwen3-VL-8B-Instruct/    # Full video analysis model
```

This follows ComfyUI's standard model organization structure.

### Option 1: Pre-download (Recommended)

Download the models before first use to avoid waiting:

```bash
cd ComfyUI/custom_nodes/ComfyUI-VideoDescription
python download_models.py
```

This will download models to `ComfyUI/models/video_description/`

### Option 2: Automatic Download

Models will download automatically on first use. However, this will cause delays:
- **Qwen3-VL**: 10-30 minute delay (16GB download)

**Download behavior**:
1. Node checks model directory
2. If not found: Downloads from Hugging Face
3. If found: Loads directly (fast!)

### Disk Space Requirements

- **Qwen3-VL-8B (FP16)**: ~16GB
- **With 4-bit quantization**: ~8GB
- **Recommended free space**: 20GB+

### Hardware Requirements

- ✅ Works on: NVIDIA CUDA, Apple Silicon (MPS), CPU
- Recommended: 16GB+ RAM, GPU with 8GB+ VRAM

## Quick Start

### Usage Example

1. **Place your video in ComfyUI/input/ directory** (Recommended)
   ```bash
   # Example: Copy video to input folder
   cp my_video.mp4 ComfyUI/input/
   ```

2. **Add the node in ComfyUI**
   - Look for "video" category in the node menu
   - Add "Video Description (Qwen3-VL)" node

3. **Configure the node**
   - `video_path`: Enter just the filename (e.g., `my_video.mp4`)
     - The node automatically searches in `ComfyUI/input/` directory
     - Supports subfolders: `videos/my_video.mp4`
     - Or use absolute path: `/full/path/to/video.mp4`
   - Set your prompt and parameters
   - Run to generate description

### Testing the Node

1. Restart ComfyUI
2. Copy a test video to `ComfyUI/input/`
3. Add "Video Description (Qwen3-VL)" node
4. Enter the video filename in `video_path` (e.g., `test.mp4`)
5. Run the workflow

## Current Nodes

### Video Description (Qwen3-VL) - v1.2.0

**Status**: Fully functional with smart path resolution and analysis type presets

**Required Inputs**:
- `video_path` (STRING): Path to video file
  - **Just filename**: `video.mp4` → searches in `ComfyUI/input/`
  - **Subfolder**: `videos/scene1.mp4` → searches in `ComfyUI/input/videos/`
  - **Absolute path**: `/full/path/to/video.mp4`
- `analysis_type` (DROPDOWN): Type of video analysis
  - **detailed**: Comprehensive description with rich details (384 tokens, temp 0.7)
  - **summary**: Brief 2-3 sentence overview (128 tokens, temp 0.5)
  - **keywords**: Structured metadata extraction (256 tokens, temp 0.3)
  - Default: "detailed"
- `fps` (FLOAT): Frames per second for video sampling
  - Default: 1.0, Min: 0.1, Max: 30.0
  - Higher FPS = more frames analyzed = slower but more detailed
  - Recommended: 0.5-1.0 for most videos

**Optional Inputs**:
- `custom_prompt` (STRING): Custom analysis prompt
  - Overrides the analysis_type preset
  - Use when you need specific questions answered
  - Default: "" (uses analysis_type preset)
- `use_4bit` (BOOLEAN): Enable 4-bit quantization
  - Default: False
  - Reduces VRAM usage from ~16GB to ~8GB
- `temperature` (FLOAT): Text generation creativity (LLM parameter)
  - Default: 0.7, Min: 0.0, Max: 1.0
  - Only used when custom_prompt is provided
  - **Note**: This is NOT the same as "denoise" in image generation

**Outputs**:
- `description` (STRING): Generated video description
- `info` (STRING): Processing information (duration, resolution, FPS, etc.)

**How It Works**:
1. Resolves video path (searches in ComfyUI/input/ if relative)
2. Validates video file format and accessibility
3. Loads Qwen3-VL model (cached after first load)
4. Extracts frames at specified FPS rate
5. Generates natural language description using Vision-Language Model
6. Returns description and metadata

**Performance**:
- 3-second video: ~14 seconds (model loading + inference)
- 30-second video: ~130 seconds
- First run includes model loading (5-6 seconds), subsequent runs reuse cached model

---

## StoryBoard Nodes

### JSON Parser (StoryBoard)

Parses JSON storyboard files and extracts scene/character data.

**Inputs**:
- `file_name` (STRING): JSON filename in `ComfyUI/input/prompt/` directory

**Outputs**:
- `zipped_prompt` (ZIPPED_PROMPT): Scene data tuples (description, time_weather, camera_info, composition)
- `zipped_character` (ZIPPED_PROMPT): Character data tuples
- `count` (INT): Number of scenes

**JSON Format**:
```json
{
  "scene": {
    "1": {
      "mainCharacter": { "koName": "", "enName": "", "description": "" },
      "subCharacter": { "koName": "", "enName": "", "description": "" },
      "time": { "ko": "", "en": "" },
      "weather": { "ko": "", "en": "" },
      "cameraShot": { "ko": "", "en": "" },
      "cameraAngle": { "ko": "", "en": "" },
      "description": { "ko": "", "en": "" },
      "composition": { "ko": "", "en": "" }
    }
  }
}
```

---

### Build Prompt (StoryBoard)

Combines scene data into a single prompt string.

**Inputs**:
- `zipped_prompt` (ZIPPED_PROMPT): From JsonParserNode

**Outputs**:
- `prompt` (STRING): Combined scene prompt

---

### Build Character Prompt (StoryBoard)

Generates natural language character descriptions.

**Inputs**:
- `zipped_character` (ZIPPED_PROMPT): From JsonParserNode

**Outputs**:
- `character_prompt` (STRING): Character description (e.g., "Somyung is a female teenager...")

---

### Select Index (StoryBoard)

Selects a specific scene by index.

**Inputs**:
- `zipped_prompt` (ZIPPED_PROMPT): From JsonParserNode
- `index` (INT): Scene index (0-based)

**Outputs**:
- `selected_prompt` (ZIPPED_PROMPT): Single scene data

---

### Merge Strings (StoryBoard)

Merges two string arrays with a separator.

**Inputs**:
- `strings_a` (STRING): First string array
- `strings_b` (STRING): Second string array
- `separator` (STRING): Optional separator (default: " ")

**Outputs**:
- `merged_strings` (STRING): Merged result

---

## Roadmap

### Phase 1: Qwen3-VL Integration ✅
- ✅ Model loader implementation with caching
- ✅ Video validation and info extraction
- ✅ Inference pipeline with Qwen3-VL
- ✅ Error handling and cleanup
- ✅ Smart path resolution with ComfyUI/input/ search
- ✅ Performance optimization (removed tensor conversion overhead)
- ✅ Analysis type presets (detailed/summary/keywords)

### Phase 2: Advanced Features (Planned)
- [ ] Batch processing support for multiple videos
- [ ] Video timestamp-based analysis
- [ ] Advanced prompt templates library
- [ ] Performance optimization and caching improvements

### Phase 3: Production Ready (Future)
- [ ] Comprehensive testing
- [ ] Example workflows
- [ ] Performance benchmarks
- [ ] Community deployment

## Requirements

- Python 3.8+
- PyTorch 2.0+
- NVIDIA GPU with 16GB+ VRAM (recommended)
- ComfyUI

## Dependencies

See [requirements.txt](requirements.txt) for full list:
- torch>=2.0.0
- transformers>=4.50.0
- accelerate>=0.20.0
- qwen-vl-utils
- opencv-python
- pillow
- numpy

## Hardware Recommendations

| Configuration | GPU | VRAM | Performance |
|--------------|-----|------|-------------|
| Minimum | RTX 3060 | 12GB | Basic (with quantization) |
| Recommended | RTX 4090 | 24GB | Good (FP16) |
| Optimal | A100 | 40GB+ | Excellent (FP16, batch) |

## License

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Support

- **GitHub Issues**: Report bugs or request features
- **Documentation**: Check README and code comments

## Acknowledgments

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - Node-based UI for Stable Diffusion
- [Qwen-VL](https://github.com/QwenLM/Qwen-VL) - Vision-language model by Alibaba
## Changelog

### v1.3.2
- Added Switch Case node (select 1 of N inputs by index)
- Added Get/Set virtual nodes (frontend JS, wire-free connections)
- Added Join Strings node
- Added String to List node
- Updated node display names
- Added frontend JS support (WEB_DIRECTORY)

### v1.2.0
- Added StoryBoard category (JSON Parser, Build Prompt, Build Character Prompt, Select Index, Merge Strings)

### v1.1.0
- Smart video path resolution, performance optimization

### v1.0.0
- Full Qwen3-VL integration with model caching
