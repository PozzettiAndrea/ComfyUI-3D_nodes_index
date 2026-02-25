# Random Prompt Builder for ComfyUI

Advanced AI-Powered Prompt Generation Custom Node for ComfyUI

---

## Overview

**Random Prompt Builder for ComfyUI** is a professional-grade custom node that brings intelligent AI prompt generation directly into your ComfyUI workflows. This is an adapted version of the standalone [Random Prompt Builder](https://github.com/btitkin/promptbuilder) desktop application, redesigned to work seamlessly within ComfyUI's node-based interface.

Using local GGUF language models via `llama-cpp-python`, this node transforms simple descriptions into detailed, structured prompts optimized for various AI image generation models including Stable Diffusion, SDXL, Pony Diffusion, Flux, and more.

### Key Advantages

- **Fully Local Operation**: All AI processing happens on your machine using GGUF models
- **Model-Aware Formatting**: Automatically formats prompts for your target model (tag-based or natural language)
- **Advanced Character Control**: Detailed customization of physical attributes and characteristics
- **Structured Generation**: Organizes prompts into semantic categories for consistent results
- **GPU Accelerated**: Configurable GPU layer offloading for optimal performance
- **Style-Aware Output**: Multiple style presets with automatic quality tag injection
- **Professional Controls**: Fine-tune creativity, temperature, and other LLM parameters

---

## Features

### Core Functionality

- Local LLM integration using GGUF models from your `ComfyUI/models/LLM` folder
- GPU acceleration with configurable layer offloading
- Multiple output formats:
  - Pony Diffusion (score tags)
  - SDXL / SD 1.5 (comma-separated tags)
  - Flux / SD3 (natural language)
  - Anime/Danbooru (booru tags)
  - Custom formats
- Quality tags with automatic style-specific injection
- BREAK separator support for SDXL/Pony workflows
- Seed control for reproducible generation

### Character Controls

Define your subject with precision:

- **Gender**: male, female, non-binary, couple, or any
- **Age Range**: 18-25, 26-35, 36-50, 50+, or any
- **Body Type**: slim, average, athletic, curvy, muscular, plus-size, or any
- **Ethnicity**: caucasian, asian, african, hispanic, middle eastern, mixed, or any
- **Height**: short, average, tall, or any
- **Physical Attributes**: breast size, muscle definition (NSFW-aware)
- **Scene Type**: solo, duo, group, or any
- **Character Overlays**: furry, monster, sci-fi character traits
- **Detailed Attributes**: hair style, hair color, eye color, facial hair, roleplay scenarios

### Structured Prompt Organization

Organize your prompt into semantic components:

1. **Subject**: Main character or object description
2. **Attributes**: Physical characteristics, facial features, expressions
3. **Action**: What the subject is doing
4. **Pose**: Body position, stance, gestures
5. **Clothing**: Outfits, accessories, wardrobe details
6. **Location**: Scene setting, environment
7. **Background**: Background elements, atmosphere, lighting

### Style System

**Style Presets:**
- Photographic
- Cinematic
- Anime
- Digital Art
- Comic Book
- Fantasy
- Cyberpunk
- 3D Render
- Oil Painting

**Style Filters:**
- Main Style: Realistic, Anime, Semi-realistic, or any
- Sub-Style (Realistic): Professional, Amateur, Flash, Film, or any
- Sub-Style (Anime): Ghibli, Modern, Vintage, Shoujo, Shounen, or any

**Content Controls:**
- NSFW Modes: Safe, NSFW, Hardcore
- NSFW Levels: Fine-grained control (0-10)
- Quality tag injection with style-specific enhancers

### Advanced LLM Controls

- **Creativity**: 0.0 (strict formatting) to 1.0 (highly creative)
- **Temperature**: 0.1-2.0 (sampling randomness)
- **Top-P**: Nucleus sampling threshold
- **Frequency Penalty**: Reduce token repetition
- **Presence Penalty**: Encourage topic diversity
- **Context Window**: 512-32768 tokens
- **GPU Layers**: Offload processing to GPU (0 = CPU only)

### Enhancement System

- **Enhancement Rounds**: 0-3 iterations of prompt refinement
- **Locked Phrases**: Preserve specific text across enhancement iterations
- **Selective Enhancement**: Toggle person, pose, and location enhancements
- **Mandatory Tags**: Force-include specific tags in final output
- **Negative Prompts**: Custom negative prompt support

---

## Installation

### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "Random Prompt Builder" or "RandomPromptBuilder"
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation

**Step 1: Clone the repository**

Navigate to your ComfyUI custom nodes directory and clone this repository:

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/yourusername/ComfyUI-RandomPromptBuilder.git
```

**Step 2: Install Python dependencies**

```bash
cd ComfyUI-RandomPromptBuilder
pip install -r requirements.txt
```

**Step 3: Install llama-cpp-python with GPU support**

Choose the appropriate installation method for your hardware:

**NVIDIA CUDA (Windows):**
```powershell
$env:CMAKE_ARGS="-DGGML_CUDA=on"
pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir
```

**NVIDIA CUDA (Linux/Mac):**
```bash
CMAKE_ARGS="-DGGML_CUDA=on" pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir
```

**AMD ROCm:**
```bash
CMAKE_ARGS="-DGGML_HIPBLAS=on" pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir
```

**Apple Silicon (Metal):**
```bash
CMAKE_ARGS="-DGGML_METAL=on" pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir
```

**CPU Only:**
```bash
pip install llama-cpp-python
```

**Step 4: Download GGUF model**

Download a GGUF model and place it in `ComfyUI/models/LLM/` (create the directory if it doesn't exist)

**Step 5: Restart ComfyUI**

---

## Recommended Models

Place GGUF model files in the `ComfyUI/models/LLM/` directory.

### Model Recommendations

| Model | Quantization | Size | Download Link | Notes |
|-------|--------------|------|---------------|-------|
| Qwen2.5-7B-Instruct | Q4_K_M | ~4.4GB | [HuggingFace](https://huggingface.co/bartowski/Qwen2.5-7B-Instruct-GGUF) | Best balance of quality and speed |
| Qwen2.5-7B-Instruct | Q5_K_M | ~5.4GB | [HuggingFace](https://huggingface.co/bartowski/Qwen2.5-7B-Instruct-GGUF) | Higher quality |
| Mistral-7B-Instruct-v0.3 | Q4_K_M | ~4.4GB | [HuggingFace](https://huggingface.co/bartowski/Mistral-7B-Instruct-v0.3-GGUF) | Excellent creativity |
| Llama-3.2-3B-Instruct | Q4_K_M | ~2.0GB | [HuggingFace](https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF) | Lightweight option |

### Quantization Guide

- **Q4_K_M**: Best speed/quality balance (recommended for most users)
- **Q5_K_M**: Higher quality with moderate file size increase
- **Q6_K**: Near-original quality, larger file size
- **Q8_0**: Maximum quality, largest file size

---

## Quick Start

### Basic Workflow Setup

**Step 1: Add the Node**

Right-click in ComfyUI → Add Node → Random → Random Prompt Builder (GGUF)

**Step 2: Connect Outputs**

- `POSITIVE_PROMPT` → `CLIPTextEncode` (positive)
- `NEGATIVE_PROMPT` → `CLIPTextEncode` (negative)
- Connect to your KSampler or other sampling nodes

**Step 3: Configure Settings**

- Select your GGUF model from the dropdown
- Choose target model format (SDXL, Pony, Flux, etc.)
- Set style preset and NSFW mode

**Step 4: Add Prompt Details (Optional)**

- Fill in character controls (gender, age, body type, etc.)
- Add structured prompt categories (subject, action, clothing, etc.)
- Add mandatory tags if needed

**Step 5: Generate**

Click "Queue Prompt" in ComfyUI to generate both positive and negative prompts.

### Example Workflow Structure

```
[Random Prompt Builder (GGUF)]
    ↓ POSITIVE_PROMPT
[CLIP Text Encode (Prompt)]
    ↓ CONDITIONING
[KSampler] ← + other inputs
    ↓ LATENT
[VAE Decode]
    ↓ IMAGE
[Save Image]
```

---

## Usage Examples

### Example 1: Anime Character (Pony Model)

**Settings:**
- Target Model: `Pony (Score Tags)`
- Style Preset: `Anime`
- NSFW Mode: `Safe`
- Use Quality Tags: `True`

**Character Controls:**
- Gender: `female`
- Age: `18-25`
- Body Type: `slim`

**Structured Inputs:**
- Subject: `magical girl`
- Attributes: `long pink hair, bright eyes, cheerful expression`
- Clothing: `frilly dress with ribbons`
- Location: `cherry blossom garden`

**Generated Output:**
```
score_9, score_8_up, score_7_up, masterpiece, best quality, highres, 18-25 years old, female, slim body type, magical girl, long pink hair, bright eyes, cheerful expression, frilly dress with ribbons, cherry blossom garden
```

---

### Example 2: Photorealistic Portrait (SDXL)

**Settings:**
- Target Model: `SDXL / SD 1.5 (Tags)`
- Style Preset: `Photographic`
- Main Style: `Realistic`
- Sub Style (Realistic): `Professional`
- Use BREAK: `True`
- Use Quality Tags: `True`

**Character Controls:**
- Gender: `female`
- Age: `26-35`
- Body Type: `athletic`
- Ethnicity: `asian`

**Structured Inputs:**
- Subject: `warrior princess`
- Attributes: `long flowing black hair, determined expression, battle scars`
- Action: `looking at camera with confidence`
- Pose: `dynamic stance, hand on sword hilt`
- Clothing: `ornate silver armor with red accents, flowing cape`
- Location: `ancient temple ruins`
- Background: `mystical fog, moonlight filtering through pillars`

**Generated Output:**
```
photorealistic, high detail, professional photography, best quality, 8k, BREAK 26-35 years old, asian, female, athletic body type, BREAK warrior princess, long flowing black hair, determined expression, battle scars, BREAK looking at camera with confidence, dynamic stance, hand on sword hilt, BREAK ornate silver armor with red accents, flowing cape, BREAK ancient temple ruins, BREAK mystical fog, moonlight filtering through pillars
```

---

### Example 3: Natural Language (Flux)

**Settings:**
- Target Model: `Flux / SD3 (Natural)`
- Style Preset: `Cinematic`
- Creativity: `0.8`

**Structured Inputs:**
- Subject: `cyberpunk detective`
- Attributes: `augmented eyes, weathered face`
- Action: `investigating a holographic crime scene`
- Location: `neon-lit alley in rain-soaked megacity`

**Generated Output:**
```
A cinematic scene of a cyberpunk detective with augmented eyes and a weathered face, investigating a holographic crime scene in a neon-lit alley within a rain-soaked megacity. The lighting is dramatic with high contrast, creating a moody atmosphere with shallow depth of field.
```

---

## Parameters Reference

### Required Parameters

| Parameter | Type | Default | Range | Description |
|-----------|------|---------|-------|-------------|
| llm_model | Dropdown | - | - | GGUF model from `models/LLM` folder |
| gpu_layers | INT | 20 | 0-100 | Number of layers to offload to GPU (0=CPU only) |
| n_ctx | INT | 2048 | 512-32768 | Context window size |
| seed | INT | 0 | 0-∞ | Random seed for reproducibility |
| control_after_generate | Dropdown | randomize | - | "fixed" or "randomize" seed after generation |

### LLM Tuning Parameters

| Parameter | Type | Default | Range | Description |
|-----------|------|---------|-------|-------------|
| creativity | FLOAT | 0.8 | 0.0-1.0 | 0.0=strict formatting, 1.0=highly creative |
| temperature | FLOAT | 0.7 | 0.1-2.0 | LLM sampling temperature |
| top_p | FLOAT | 1.0 | 0.0-1.0 | Nucleus sampling threshold |
| frequency_penalty | FLOAT | 0.0 | 0.0-2.0 | Penalize token repetition |
| presence_penalty | FLOAT | 0.0 | 0.0-2.0 | Penalize topic repetition |

### Output Format Parameters

| Parameter | Type | Default | Options |
|-----------|------|---------|---------|
| target_model | Dropdown | SDXL | Pony, SDXL, Flux, Anime, Custom |
| style_preset | Dropdown | Photographic | Photographic, Cinematic, Anime, Digital Art, Comic Book, Fantasy, Cyberpunk, 3D Render, Oil Painting |
| use_quality_tags | BOOLEAN | True | - |
| use_break | BOOLEAN | False | - |

### Style Filter Parameters

| Parameter | Type | Default | Options |
|-----------|------|---------|---------|
| main_style | Dropdown | any | any, realistic, anime, semi-realistic |
| sub_style_realistic | Dropdown | any | any, professional, amateur, flash, film |
| sub_style_anime | Dropdown | any | any, ghibli, modern, vintage, shoujo, shounen |

### NSFW Parameters

| Parameter | Type | Default | Range/Options |
|-----------|------|---------|---------------|
| nsfw_mode | Dropdown | Safe | safe, nsfw, hardcore |
| nsfw_level | INT | 0 | 0-10 |
| hardcore_level | INT | 0 | 0-10 |

### Character Control Parameters

All character parameters support "any" for random selection or "ignore" to exclude from prompt.

| Parameter | Options |
|-----------|---------|
| scene_type | any, solo, duo, group, ignore |
| gender | any, male, female, non-binary, couple, ignore |
| age | any, 18-25, 26-35, 36-50, 50+, ignore |
| body_type | any, slim, average, athletic, curvy, muscular, plus-size, ignore |
| ethnicity | any, caucasian, asian, african, hispanic, middle eastern, mixed, ignore |
| height | any, short, average, tall, ignore |
| breast_size | any, small, medium, large, huge, ignore |
| muscle_definition | any, soft, toned, defined, ripped, ignore |
| hair_style | Free text |
| hair_color | Free text |
| eye_color | Free text |
| facial_hair | any, clean_shaven, stubble, beard, mustache, goatee, ignore |
| character_style | Free text |
| roleplay | Free text |

### Character Overlay Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| overlay_furry | BOOLEAN | False | Apply furry character traits |
| overlay_monster | BOOLEAN | False | Apply monster/creature traits |
| overlay_scifi | BOOLEAN | False | Apply sci-fi/cybernetic traits |

### Enhancement Parameters

| Parameter | Type | Default | Range | Description |
|-----------|------|---------|-------|-------------|
| enhance_round | INT | 0 | 0-3 | Number of enhancement iterations |
| locked_phrases | STRING | "" | - | Phrases preserved across enhancement rounds |
| enhance_person | BOOLEAN | True | - | Enhance character descriptions |
| enhance_pose | BOOLEAN | True | - | Enhance pose descriptions |
| enhance_location | BOOLEAN | True | - | Enhance location descriptions |

### Structured Prompt Categories

All are multiline text inputs:

| Parameter | Description |
|-----------|-------------|
| subject | Main subject/character |
| attributes | Physical characteristics, expressions, features |
| action | What they're doing, activity |
| pose | Stance, body position, gestures |
| clothing | Outfit, accessories, wardrobe |
| location | Environment, setting, place |
| background | Background details, atmosphere, lighting |

### Additional Controls

| Parameter | Type | Default | Range | Description |
|-----------|------|---------|-------|-------------|
| mandatory_tags | STRING | "" | - | Tags forced into output |
| negative_prompt | STRING | "" | - | Custom negative prompt output |
| max_tokens | INT | 512 | 128-2048 | Maximum tokens for LLM generation |
| aspect_ratio | Dropdown | none | - | Target image aspect ratio |
| additional_params | STRING | "" | - | Additional instructions for the LLM |

---

## Advanced Usage

### GPU Layer Configuration

Adjust `gpu_layers` based on your GPU VRAM:

| VRAM | Recommended GPU Layers | Model Size |
|------|------------------------|------------|
| 24GB+ | 33 (full model) | Any Q4_K_M |
| 12-16GB | 25-30 | Q4_K_M 7B |
| 8-10GB | 15-20 | Q4_K_M 7B |
| 6GB | 10-15 | Q4_K_M 3B |
| 4GB | 0-10 (CPU recommended) | Q4_K_M 3B |

### Enhancement Rounds

Use `enhance_round` to iteratively refine prompts:

- **0**: No enhancement (direct generation)
- **1**: Single refinement pass
- **2**: Two refinement passes (high quality)
- **3**: Three refinement passes (maximum quality, slower)

When using enhancement rounds, any text in `locked_phrases` will be preserved exactly across all iterations.

### BREAK Formatting

When `use_break` is enabled, the output is structured with BREAK separators, useful for SDXL and Pony models:

```
quality tags, BREAK character attributes, BREAK action and pose, BREAK clothing, BREAK location, BREAK background
```

### Batch Processing

Use ComfyUI's native batch processing:

1. Set `control_after_generate` to "randomize"
2. Use a batch size > 1 in your workflow
3. Each batch item receives a unique seed and prompt variation

---

## Troubleshooting

### No models found in models/LLM

**Solution**: Place `.gguf` model files in the `ComfyUI/models/LLM/` folder. Create the directory if it doesn't exist.

### Out of Memory / CUDA Out of Memory

**Solutions:**
- Reduce `gpu_layers` (try 15-20 for 8GB VRAM, 10-15 for 6GB)
- Use a smaller quantization (Q4_K_M instead of Q5_K_M or Q6_K)
- Use a smaller model size (3B instead of 7B)
- Reduce `n_ctx` if you don't need long context

### Slow Generation

**Solutions:**
- Increase `gpu_layers` if you have VRAM available
- Ensure llama-cpp-python was installed with GPU support
- Use a more aggressive quantization (Q4_K_M)
- Reduce `n_ctx` to 1024 or 512
- Use a smaller model (3B parameters)

### llama_cpp not available

**Solution**: Install llama-cpp-python:
```bash
pip install llama-cpp-python
```
For GPU support, see installation instructions above.

### Prompt Output is Empty or Malformed

**Solutions:**
- Increase `temperature` (try 0.8-1.0)
- Increase `creativity` (try 0.7-0.9)
- Ensure your model is an instruction-tuned variant (e.g., *-Instruct)
- Try a different model
- Increase `max_tokens` to 512 or 1024

### Node Not Showing in ComfyUI

**Solutions:**
- Ensure the folder is named correctly in `custom_nodes/`
- Check ComfyUI console for Python errors
- Verify `requirements.txt` dependencies are installed
- Restart ComfyUI completely

### Model Loading is Slow

This is normal on the first load. The model is loaded into memory and cached. Subsequent generations will be much faster.

---

## Performance Optimization

### First-Time Setup
Model loading takes 10-30 seconds on first use. This is normal and only happens once per session.

### Recommended Settings

**For Speed:**
- `gpu_layers`: 20
- `n_ctx`: 1024
- `creativity`: 0.7
- `max_tokens`: 256

**For Quality:**
- `gpu_layers`: max available
- `n_ctx`: 2048
- `creativity`: 0.8
- `enhance_round`: 2
- `max_tokens`: 512

### Resource Usage

- **Context Window**: Higher `n_ctx` allows longer prompts but uses more VRAM. 2048 is usually sufficient.
- **VRAM Usage**: Approximately 4-6GB VRAM for Q4_K_M 7B model with 20-25 GPU layers
- **CPU Fallback**: If `gpu_layers` = 0, generation uses CPU (significantly slower but works on any system)

---

## Differences from Main Application

This ComfyUI node is adapted from the [Random Prompt Builder](https://github.com/btitkin/promptbuilder) desktop application.

| Feature | Desktop App | ComfyUI Node |
|---------|-------------|--------------|
| Interface | Electron GUI | ComfyUI Node Parameters |
| Model Loading | node-llama-cpp | llama-cpp-python |
| Batch Processing | Built-in batch UI | Uses ComfyUI batch system |
| History/Favorites | Built-in management | Use ComfyUI workflow saving |
| Prompt Display | Rich text preview | Separate Prompt Display node |
| API Providers | Google Gemini, Custom API | GGUF models only |
| Installation | Standalone executable | ComfyUI custom node |

The core prompt generation logic and LLM system prompts are shared between both versions for consistent output quality.

---

## Changelog

### v3.0 - Current (2025-12-03)
- Feature parity with main desktop application (98%+)
- Added style filter system (main style + realistic/anime sub-styles)
- Added enhancement iteration system (0-3 rounds + locked phrases)
- Added character overlays (furry, monster, sci-fi)
- Added scene type control (solo, duo, group)
- Extended character attributes (hair, eyes, facial hair, roleplay)
- Added separate enhance toggles (person, pose, location)
- Improved LLM system prompts for better output quality
- Better error handling and user feedback

### v2.0 - Enhanced (2025-11-30)
- Critical fix: Returns single string instead of list (fixes CLIPTextEncode error)
- Added structured prompt categories (attributes, action, background)
- Added character controls (gender, age, body_type, ethnicity, height, physical attributes)
- Added quality tags injection system with 9 style presets
- Added BREAK support for SDXL/Pony workflows
- Added model tuning parameters (top_p, frequency_penalty, presence_penalty)
- Improved LLM system prompts for better structured output
- Changed to control_after_generate for seed management
- Better error handling and model caching

### v1.0 - Initial (2024-11-29)
- Initial release with basic GGUF prompt generation
- Support for multiple target model formats
- Basic seed and creativity controls

---

## Additional Nodes

### Prompt Display Node

A companion node for previewing generated prompts in the ComfyUI interface.

**Usage:**
1. Add "Prompt Display (Preview Text)" node
2. Connect the `POSITIVE_PROMPT` or `NEGATIVE_PROMPT` output
3. The node displays the full prompt text in the node interface

This is helpful for reviewing prompts before they're encoded.

---

## License

MIT License - See LICENSE file for details.

This project is a ComfyUI adaptation of the Random Prompt Builder desktop application. Both projects are developed by btitkin.

---

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

### Reporting Issues

When reporting issues, please include:
- ComfyUI version
- Python version
- GPU type and VRAM amount
- GGUF model being used
- Full error message from console
- Node parameter values used

---

## Credits

- Original Application: [Random Prompt Builder](https://github.com/btitkin/promptbuilder) by btitkin
- ComfyUI: [ComfyUI](https://github.com/comfyanonymous/ComfyUI) by comfyanonymous
- llama.cpp: [llama.cpp](https://github.com/ggerganov/llama.cpp) by Georgi Gerganov
- llama-cpp-python: [llama-cpp-python](https://github.com/abetlen/llama-cpp-python) by Andrei Betlen

---

## Related Links

- [Random Prompt Builder Desktop App](https://github.com/btitkin/promptbuilder)
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [GGUF Model Collection](https://huggingface.co/models?library=gguf&sort=trending)
- [llama-cpp-python Documentation](https://llama-cpp-python.readthedocs.io/)

---

## Support

For questions, issues, or discussions:

- GitHub Issues: [Report bugs or request features](https://github.com/yourusername/ComfyUI-RandomPromptBuilder/issues)
- Discussions: [Ask questions and share workflows](https://github.com/yourusername/ComfyUI-RandomPromptBuilder/discussions)

