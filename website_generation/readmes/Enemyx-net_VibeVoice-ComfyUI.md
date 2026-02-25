# VibeVoice ComfyUI Nodes

A comprehensive ComfyUI integration for Microsoft's VibeVoice text-to-speech model, enabling high-quality single and multi-speaker voice synthesis directly within your ComfyUI workflows.

## ✨ Features

### Core Functionality
- 🎤 **Single Speaker TTS**: Generate natural speech with optional voice cloning
- 👥 **Multi-Speaker Conversations**: Support for up to 4 distinct speakers
- 🎯 **Voice Cloning**: Clone voices from audio samples
- 🎨 **LoRA Support**: Fine-tune voices with custom LoRA adapters (v1.4.0+)
- 🎚️ **Voice Speed Control**: Adjust speech rate by modifying reference voice speed (v1.5.0+)
- 📝 **Text File Loading**: Load scripts from text files
- 📚 **Automatic Text Chunking**: Handles long texts seamlessly with configurable chunk size
- ⏸️ **Custom Pause Tags**: Insert silences with `[pause]` and `[pause:ms]` tags (wrapper feature)
- 🔄 **Node Chaining**: Connect multiple VibeVoice nodes for complex workflows
- ⏹️ **Interruption Support**: Cancel operations before or between generations
- 🔧 **Flexible Configuration**: Control temperature, sampling, and guidance scale

### Performance & Optimization
- ⚡ **Attention Mechanisms**: Choose between auto, eager, sdpa, flash_attention_2 or sage
- 🎛️ **Diffusion Steps**: Adjustable quality vs speed trade-off (default: 20)
- 💾 **Memory Management**: Toggle automatic VRAM cleanup after generation
- 🧹 **Free Memory Node**: Manual memory control for complex workflows
- 🍎 **Apple Silicon Support**: Native GPU acceleration on M1/M2/M3 Macs via MPS
- 🔢 **8-Bit Quantization**: Perfect audio quality with high VRAM reduction
- 🔢 **4-Bit Quantization**: Maximum VRAM savings with minimal quality loss

### Compatibility & Installation
- 📦 **Self-Contained**: Embedded VibeVoice code, no external dependencies
- 🔄 **Universal Compatibility**: Adaptive support for transformers v4.51.3+
- 🖥️ **Cross-Platform**: Works on Windows, Linux, and macOS
- 🎮 **Multi-Backend**: Supports CUDA, CPU, and MPS (Apple Silicon)

## 🎥 Video Demo
<p align="center">
  <a href="https://www.youtube.com/watch?v=fIBMepIBKhI">
    <img src="https://img.youtube.com/vi/fIBMepIBKhI/maxresdefault.jpg" alt="VibeVoice ComfyUI Wrapper Demo" />
  </a>
  <br>
  <strong>Click to watch the demo video</strong>
</p>

## 📦 Installation

### Automatic Installation (Recommended)
1. Clone this repository into your ComfyUI custom nodes folder:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Enemyx-net/VibeVoice-ComfyUI
```

2. Restart ComfyUI - the nodes will automatically install requirements on first use

## 📥 Model Installation

### Manual Download Required
Starting from version 1.6.0, models and tokenizer must be manually downloaded and placed in the correct folder. The wrapper no longer downloads them automatically.

### Download Links

#### Models
You can download VibeVoice models from HuggingFace:

| Model                  | Size   | Download Link |
|------------------------|--------|---------------|
| **VibeVoice-1.5B**     | ~5.4GB | [microsoft/VibeVoice-1.5B](https://huggingface.co/microsoft/VibeVoice-1.5B) |
| **VibeVoice-Large**    | ~18.7GB | [aoi-ot/VibeVoice-Large](https://huggingface.co/aoi-ot/VibeVoice-Large) |
| **VibeVoice-Large-Q8** | ~11.6GB | [FabioSarracino/VibeVoice-Large-Q8](https://huggingface.co/FabioSarracino/VibeVoice-Large-Q8) |
| **VibeVoice-Large-Q4** | ~6.6GB | [DevParker/VibeVoice7b-low-vram](https://huggingface.co/DevParker/VibeVoice7b-low-vram) |

#### Tokenizer (Required)
VibeVoice uses the Qwen2.5-1.5B tokenizer:
- Download from: [Qwen2.5-1.5B Tokenizer](https://huggingface.co/Qwen/Qwen2.5-1.5B/tree/main)
- Required files: `tokenizer_config.json`, `vocab.json`, `merges.txt`, `tokenizer.json`

### Installation Steps
1. Create the models folder if it doesn't exist:
   ```
   ComfyUI/models/vibevoice/
   ```

2. Download and organize files in the vibevoice folder:
   ```
   ComfyUI/models/vibevoice/
   ├── tokenizer/                 # Place Qwen tokenizer files here
   │   ├── tokenizer_config.json
   │   ├── vocab.json
   │   ├── merges.txt
   │   └── tokenizer.json
   ├── VibeVoice-1.5B/           # Model folder
   │   ├── config.json
   │   ├── model-00001-of-00003.safetensors
   │   ├── model-00002-of-00003.safetensors
   │   └── ... (other model files)
   ├── VibeVoice-Large/
   │   └── ... (model files)
   └── my-custom-vibevoice/      # custom names are supported
       └── ... (model files)
   ```

3. For models downloaded from HuggingFace using git-lfs or the HF CLI, you can also use the cache structure:
   ```
   ComfyUI/models/vibevoice/
   └── models--microsoft--VibeVoice-1.5B/
       └── snapshots/
           └── [hash]/
               └── ... (model files)
   ```

4. Refresh your browser - the models will appear in the dropdown menu

### Notes
- The dropdown will show user-friendly names extracted from folder names
- Both regular folders and HuggingFace cache structures are supported
- Models are rescanned on every browser refresh
- Quantized models are automatically detected from their config files
- The tokenizer is searched in this priority order:
  1. `ComfyUI/models/vibevoice/tokenizer/` (recommended)
  2. `ComfyUI/models/vibevoice/models--Qwen--Qwen2.5-1.5B/` (if exists from previous installations)
  3. HuggingFace cache (if available)

## 🔧 Available Nodes

### 1. VibeVoice Load Text From File
Loads text content from files in ComfyUI's input/output/temp directories.
- **Supported formats**: .txt
- **Output**: Text string for TTS nodes

### 2. VibeVoice Single Speaker
Generates speech from text using a single voice.
- **Text Input**: Direct text or connection from Load Text node
- **Models**: Select from available models in dropdown menu
- **Voice Cloning**: Optional audio input for voice cloning
- **Parameters** (in order):
  - `text`: Input text to convert to speech
  - `model`: Select from dropdown list of available models found in `ComfyUI/models/vibevoice/`
  - `attention_type`: auto, eager, sdpa, flash_attention_2 or sage (default: auto)
  - `quantize_llm`: Dynamically quantize only the LLM component for non-quantized models. Options: "full precision" (default), "4bit", or "8bit". 4-bit provides major VRAM savings with minimal quality loss. 8-bit provides a good balance between quality and memory usage. Requires CUDA GPU. Ignored for pre-quantized models.
  - `free_memory_after_generate`: Free VRAM after generation (default: True)
  - `diffusion_steps`: Number of denoising steps (5-100, default: 20)
  - `seed`: Random seed for reproducibility (default: 42)
  - `cfg_scale`: Classifier-free guidance (1.0-2.0, default: 1.3)
  - `use_sampling`: Enable/disable deterministic generation (default: False)
- **Optional Parameters**:
  - `voice_to_clone`: Audio input for voice cloning
  - `lora`: LoRA configuration from VibeVoice LoRA node
  - `temperature`: Sampling temperature (0.1-2.0, default: 0.95)
  - `top_p`: Nucleus sampling parameter (0.1-1.0, default: 0.95)
  - `max_words_per_chunk`: Maximum words per chunk for long texts (100-500, default: 250)
  - `voice_speed_factor`: Speech rate adjustment (0.8-1.2, default: 1.0, step: 0.01)

### 3. VibeVoice Multiple Speakers
Generates multi-speaker conversations with distinct voices.
- **Speaker Format**: Use `[N]:` notation where N is 1-4
- **Voice Assignment**: Optional voice samples for each speaker
- **Recommended Model**: VibeVoice-Large for better multi-speaker quality
- **Parameters** (in order):
  - `text`: Input text with speaker labels
  - `model`: Select from dropdown list of available models found in `ComfyUI/models/vibevoice/`
  - `attention_type`: auto, eager, sdpa, flash_attention_2 or sage (default: auto)
  - `quantize_llm`: Dynamically quantize only the LLM component for non-quantized models. Options: "full precision" (default), "4bit", or "8bit". 4-bit provides major VRAM savings with minimal quality loss. 8-bit provides a good balance between quality and memory usage. Requires CUDA GPU. Ignored for pre-quantized models.
  - `free_memory_after_generate`: Free VRAM after generation (default: True)
  - `diffusion_steps`: Number of denoising steps (5-100, default: 20)
  - `seed`: Random seed for reproducibility (default: 42)
  - `cfg_scale`: Classifier-free guidance (1.0-2.0, default: 1.3)
  - `use_sampling`: Enable/disable deterministic generation (default: False)
- **Optional Parameters**:
  - `speaker1_voice` to `speaker4_voice`: Audio inputs for voice cloning
  - `lora`: LoRA configuration from VibeVoice LoRA node
  - `temperature`: Sampling temperature (0.1-2.0, default: 0.95)
  - `top_p`: Nucleus sampling parameter (0.1-1.0, default: 0.95)
  - `voice_speed_factor`: Speech rate adjustment for all speakers (0.8-1.2, default: 1.0, step: 0.01)

### 4. VibeVoice Free Memory
Manually frees all loaded VibeVoice models from memory.
- **Input**: `audio` - Connect audio output to trigger memory cleanup
- **Output**: `audio` - Passes through the input audio unchanged
- **Use Case**: Insert between nodes to free VRAM/RAM at specific workflow points
- **Example**: `[VibeVoice Node] → [Free Memory] → [Save Audio]`

### 5. VibeVoice LoRA
Configure and load custom LoRA adapters for fine-tuned VibeVoice models.
- **LoRA Selection**: Dropdown menu with available LoRA adapters
- **LoRA Location**: Place your LoRA folders in `ComfyUI/models/vibevoice/loras/`
- **Parameters**:
  - `lora_name`: Select from available LoRA adapters or "None" to disable
  - `llm_strength`: Strength of the language model LoRA (0.0-2.0, default: 1.0)
  - `use_llm`: Apply language model LoRA component (default: True)
  - `use_diffusion_head`: Apply diffusion head replacement (default: True)
  - `use_acoustic_connector`: Apply acoustic connector LoRA (default: True)
  - `use_semantic_connector`: Apply semantic connector LoRA (default: True)
- **Output**: `lora` - LoRA configuration to connect to speaker nodes
- **Usage**: `[VibeVoice LoRA] → [Single/Multiple Speaker Node]`

## 💬 Multi-Speaker Text Format

For multi-speaker generation, format your text using the `[N]:` notation:

```
[1]: Hello, how are you today?
[2]: I'm doing great, thanks for asking!
[1]: That's wonderful to hear.
[3]: Hey everyone, mind if I join the conversation?
[2]: Not at all, welcome!
```

**Important Notes:**
- Use `[1]:`, `[2]:`, `[3]:`, `[4]:` for speaker labels
- Maximum 4 speakers supported
- The system automatically detects the number of speakers from your text
- Each speaker can have an optional voice sample for cloning

## 🧠 Model Information

### VibeVoice-1.5B
- **Size**: ~5.4GB download
- **VRAM**: ~6GB
- **Speed**: Faster inference
- **Quality**: Good for single speaker
- **Use Case**: Quick prototyping, single voices

### VibeVoice-Large
- **Size**: ~18.7GB download
- **VRAM**: ~20GB
- **Speed**: Slower inference but optimized
- **Quality**: Best available quality (full precision)
- **Use Case**: Highest quality production, multi-speaker conversations
- **Note**: Latest official release from Microsoft

### VibeVoice-Large-Q8
- **Size**: ~11.6GB download (38% reduction from full model)
- **VRAM**: ~12GB (40% reduction from full precision)
- **Speed**: Balanced inference
- **Quality**: Identical to full precision - perfect audio preservation
- **Use Case**: Production-quality audio with 12GB VRAM GPUs (RTX 3060, 4070 Ti, etc.)
- **Quantization**: Selective 8-bit - only LLM quantized, audio components at full precision
- **Note**: Quantized by Fabio Sarracino

### VibeVoice-Large-Q4
- **Size**: ~6.6GB download
- **VRAM**: ~8GB
- **Speed**: Balanced inference
- **Quality**: Good quality with minimal loss
- **Use Case**: Maximum VRAM savings for lower-end GPUs
- **Note**: Quantized by DevParker

Models are automatically downloaded on first use and cached in `ComfyUI/models/vibevoice/`.

## ⚙️ Generation Modes

### Deterministic Mode (Default)
- `use_sampling = False`
- Produces consistent, stable output
- Recommended for production use

### Sampling Mode
- `use_sampling = True`
- More variation in output
- Uses temperature and top_p parameters
- Good for creative exploration

## 🎯 Voice Cloning

To clone a voice:
1. Connect an audio node to the `voice_to_clone` input (single speaker)
2. Or connect to `speaker1_voice`, `speaker2_voice`, etc. (multi-speaker)
3. The model will attempt to match the voice characteristics

**Requirements for voice samples:**
- Clear audio with minimal background noise
- Minimum 3–10 seconds. Recommended at least 30 seconds for better quality
- Automatically resampled to 24kHz

## 🎨 LoRA Support

### Overview
Starting from version 1.4.0, VibeVoice ComfyUI supports custom LoRA (Low-Rank Adaptation) adapters for fine-tuning voice characteristics. This allows you to train and use specialized voice models while maintaining the base VibeVoice capabilities.

### Setting Up LoRA Adapters

1. **LoRA Directory Structure**:
   Place your LoRA adapter folders in: `ComfyUI/models/vibevoice/loras/`
   ```
   ComfyUI/
   └── models/
       └── vibevoice/
           └── loras/
               ├── my_custom_voice/
               │   ├── adapter_config.json
               │   ├── adapter_model.safetensors
               │   └── diffusion_head/  (optional)
               ├── character_voice/
               └── style_adaptation/
   ```

2. **Required Files**:
   - `adapter_config.json`: LoRA configuration
   - `adapter_model.safetensors` or `adapter_model.bin`: Model weights
   - Optional components:
     - `diffusion_head/`: Custom diffusion head weights
     - `acoustic_connector/`: Acoustic connector adaptation
     - `semantic_connector/`: Semantic connector adaptation

### Using LoRA in ComfyUI

1. **Add VibeVoice LoRA Node**:
   - Create a "VibeVoice LoRA" node in your workflow
   - Select your LoRA from the dropdown menu
   - Configure component settings and strength

2. **Connect to Speaker Nodes**:
   - Connect the LoRA node's output to the `lora` input of speaker nodes
   - Both Single Speaker and Multiple Speakers nodes support LoRA

3. **LoRA Parameters**:
   - **llm_strength**: Controls the influence of the language model LoRA (0.0-2.0)
   - **Component toggles**: Enable/disable specific LoRA components
   - Select "None" to disable LoRA and use the base model

### Training Your Own LoRA

To create custom LoRA adapters for VibeVoice, use the official fine-tuning repository:
- **Repository**: [VibeVoice Fine-tuning](https://github.com/voicepowered-ai/VibeVoice-finetuning)
- **Features**:
  - Parameter-efficient fine-tuning
  - Support for custom datasets
  - Adjustable LoRA rank and scaling
  - Optional diffusion head adaptation

### Best Practices

- **Voice Consistency**: Use the same LoRA across all chunks for long texts
- **Memory Management**: LoRA adds minimal memory overhead (~100-500MB)
- **Compatibility**: LoRA adapters are compatible with all VibeVoice model variants
- **Strength Tuning**: Start with default strength (1.0) and adjust based on results

### Compatibility Note

⚠️ **Transformers Version**: The LoRA implementation was developed and tested with `transformers==4.51.3`. While our wrapper supports `transformers>=4.51.3`, LoRA functionality with newer versions of transformers is not guaranteed. If you experience issues with LoRA loading, consider using `transformers==4.51.3` specifically:
```bash
pip install transformers==4.51.3
```

### 🙏 Credits

LoRA implementation by [@jpgallegoar](https://github.com/jpgallegoar) (PR #127)

## 🎚️ Voice Speed Control

### Overview
The Voice Speed Control feature allows you to influence the speaking rate of generated speech by adjusting the speed of the reference voice. This feature modifies the input voice sample before processing, causing the model to learn and reproduce the altered speech rate.

**Available from version 1.5.0**

### How It Works
The system applies time-stretching to the reference voice audio:
- Values < 1.0 slow down the reference voice, resulting in slower generated speech
- Values > 1.0 speed up the reference voice, resulting in faster generated speech
- The model learns from the modified voice characteristics and generates speech at a similar pace

### Usage
- **Parameter**: `voice_speed_factor`
- **Range**: 0.8 to 1.2
- **Default**: 1.0 (normal speed)
- **Step**: 0.01 (1% increments)

### Recommended Settings
- **Optimal Range**: 0.95 to 1.05 for natural-sounding results
- **Slower Speech**: Try 0.95 (5% slower) or 0.97 (3% slower)
- **Faster Speech**: Try 1.03 (3% faster) or 1.05 (5% faster)
- **Best Results**: Provide reference audio of at least 20 seconds for more accurate speed matching

### Important Notes
- The effect works best with longer reference audio samples (20+ seconds recommended)
- Extreme values (< 0.9 or > 1.1) may produce unnatural-sounding speech
- In Multi Speaker mode, the speed adjustment applies to all speakers equally
- Synthetic voices (when no audio is provided) are not affected by this parameter

### 📖 Examples
```
# Single Speaker
voice_speed_factor: 0.95  # Slightly slower, more deliberate speech
voice_speed_factor: 1.05  # Slightly faster, more energetic speech

# Multi Speaker
voice_speed_factor: 0.98  # All speakers talk 2% slower
voice_speed_factor: 1.02  # All speakers talk 2% faster
```

## ⏸️ Pause Tags Support

### Overview
The VibeVoice wrapper includes a custom pause tag feature that allows you to insert silences between text segments. **This is NOT a standard Microsoft VibeVoice feature** - it's an original implementation of our wrapper to provide more control over speech pacing.

**Available from version 1.3.0**

### Usage
You can use two types of pause tags in your text:
- `[pause]` - Inserts a 1-second silence (default)
- `[pause:ms]` - Inserts a custom duration silence in milliseconds (e.g., `[pause:2000]` for 2 seconds)

### 📖 Examples

#### Single Speaker
```
Welcome to our presentation. [pause] Today we'll explore artificial intelligence. [pause:500] Let's begin!
```

#### Multi-Speaker  
```
[1]: Hello everyone [pause] how are you doing today?
[2]: I'm doing great! [pause:500] Thanks for asking.
[1]: Wonderful to hear!
```

### Important Notes

⚠️ **Context Limitation Warning**:
> **Note: The pause forces the text to be split into chunks. This may worsen the model's ability to understand the context. The model's context is represented ONLY by its own chunk.**

This means:
- Text before a pause and text after a pause are processed separately
- The model cannot see across pause boundaries when generating speech
- This may affect prosody and intonation consistency
- This may affect prosody and intonation consistency

### How It Works
1. The wrapper parses your text to find pause tags
2. Text segments between pauses are processed independently 
3. Silence audio is generated for each pause duration
4. All audio segments (speech and silence) are concatenated

### Best Practices
- Use pauses at natural breaking points (end of sentences, paragraphs)
- Avoid pauses in the middle of phrases where context is important
- Test different pause durations to find what sounds most natural

## 💡 Tips for Best Results

1. **Text Preparation**:
   - Use proper punctuation for natural pauses
   - Break long texts into paragraphs
   - For multi-speaker, ensure clear speaker transitions
   - Use pause tags sparingly to maintain context continuity

2. **Model Selection**:
   - Use 1.5B for quick single-speaker tasks (fastest, ~8GB VRAM)
   - Use Large for absolute best quality (~20GB VRAM)
   - Use Large-Q8 for production quality with 12GB VRAM (perfect audio, 38% smaller)
   - Use Large-Quant-4Bit for maximum VRAM savings (~7GB VRAM)

3. **Seed Management**:
   - Default seed (42) works well for most cases
   - Save good seeds for consistent character voices
   - Try random seeds if default doesn't work well

4. **Performance**:
   - First run downloads models (5-17GB)
   - Subsequent runs use cached models
   - GPU recommended for faster inference

## 💻 System Requirements

### Hardware
- **Minimum**: 8GB VRAM for VibeVoice-1.5B
- **Recommended**: 17GB+ VRAM for VibeVoice-Large
- **RAM**: 16GB+ system memory

### Software
- Python 3.8+
- PyTorch 2.0+
- CUDA 11.8+ (for GPU acceleration)
- Transformers 4.51.3+
- ComfyUI (latest version)

## 🔧 Troubleshooting

### Installation Issues
- Ensure you're using ComfyUI's Python environment
- Try manual installation if automatic fails
- Restart ComfyUI after installation

### Generation Issues
- If voices sound unstable, try deterministic mode
- For multi-speaker, ensure text has proper `[N]:` format
- Check that speaker numbers are sequential (1,2,3 not 1,3,5)

### Memory Issues
- Large model requires ~16GB VRAM
- Use 1.5B model for lower VRAM systems
- Models use bfloat16 precision for efficiency

## 📖 Examples

### Single Speaker
```
Text: "Welcome to our presentation. Today we'll explore the fascinating world of artificial intelligence."
Model: [Select from available models]
cfg_scale: 1.3
use_sampling: False
```

### Two Speakers
```
[1]: Have you seen the new AI developments?
[2]: Yes, they're quite impressive!
[1]: I think voice synthesis has come a long way.
[2]: Absolutely, it sounds so natural now.
```

### Four Speaker Conversation
```
[1]: Welcome everyone to our meeting.
[2]: Thanks for having us!
[3]: Glad to be here.
[4]: Looking forward to the discussion.
[1]: Let's begin with the agenda.
```

## 📊 Performance Benchmarks

| Model              | VRAM Usage | Context Length | Max Audio Duration |
|--------------------|------------|----------------|-------------------|
| VibeVoice-1.5B     | ~6GB       | 64K tokens | ~90 minutes |
| VibeVoice-Large | ~20GB      | 32K tokens | ~45 minutes |
| VibeVoice-Large-Q8 | ~12GB      | 32K tokens | ~45 minutes |
| VibeVoice-Large-Q4 | ~8GB       | 32K tokens | ~45 minutes |

## ⚠️ Known Limitations

- Maximum 4 speakers in multi-speaker mode
- Works best with English and Chinese text
- Some seeds may produce unstable output
- Background music generation cannot be directly controlled

## 📄 License

This ComfyUI wrapper is released under the MIT License. See LICENSE file for details.

**Note**: The VibeVoice model itself is subject to Microsoft's licensing terms:
- VibeVoice is for research purposes only
- Check Microsoft's VibeVoice repository for full model license details

## 🔗 Links

- [Original VibeVoice Repository](https://github.com/microsoft/VibeVoice) - Official Microsoft VibeVoice repository (currently unavailable)

## 🙏 Credits

- **VibeVoice Model**: Microsoft Research
- **ComfyUI Integration**: Fabio Sarracino
- **Base Model**: Built on Qwen2.5 architecture

## 💬 Support

For issues or questions:
1. Check the troubleshooting section
2. Review ComfyUI logs for error messages
3. Ensure VibeVoice is properly installed
4. Open an issue with detailed error information

## 🤝 Contributing

Contributions welcome! Please:
1. Test changes thoroughly
2. Follow existing code style
3. Update documentation as needed
4. Submit pull requests with clear descriptions

## 📝 Changelog

### Version 1.8.1
- Forced installation of the bitsandbytes>=0.48.1 library as version 0.48.0 has a critical bug that prevents the Q8 model from working.
- Bug Fixing

### Version 1.8.0
- **New Official 8-bit Quantized Model**: VibeVoice-Large-Q8
  - Released on HuggingFace: [FabioSarracino/VibeVoice-Large-Q8](https://huggingface.co/FabioSarracino/VibeVoice-Large-Q8)
  - Model size: 11.6GB (38% reduction from 18.7GB full precision)
  - VRAM usage: ~12GB (40% reduction from ~20GB)
  - **Perfect audio quality**: Identical to full precision model - no quality degradation
  - **Selective quantization approach**: audio-critical components (diffusion head, VAE, connectors) kept at full precision
  - Optimized for 12GB VRAM GPUs (RTX 3060, 4070 Ti, etc.)
  - Solves the common 8-bit "noise problem" by carefully selecting which components to quantize
- **Added 8-bit Dynamic LLM Quantization**
  - New "8bit" option in `quantize_llm` parameter for both Single and Multiple Speaker nodes
  - Options now: "full precision" (default), "4bit", "8bit"
  - Dynamically quantizes only the LLM component for non-quantized models
  - Skips all audio-critical components (diffusion_head, acoustic/semantic connectors, tokenizers)
  - Provides good balance between quality and VRAM savings
  - Requires CUDA GPU and bitsandbytes library
  - Automatically ignored for pre-quantized models

### Version 1.7.0
- Added dynamic LLM-only 4-bit quantization for non-quantized models
  - New `quantize_llm` parameter in both Single and Multiple Speaker nodes
  - Options: "full precision" (default) or "4bit"
  - Quantizes only the language model component while keeping diffusion head at full precision
  - Significantly faster generation with major VRAM savings
  - Minimal quality loss compared to full precision
  - Requires CUDA GPU for quantization
  - Automatically ignored for pre-quantized models
  - Uses NF4 (4-bit NormalFloat) quantization type optimized for neural networks

### Version 1.6.3
- Fixed tokenizer initialization error
  - Resolved `TypeError: expected str, bytes or os.PathLike object, not NoneType` when loading processor
  - Added robust fallback mechanism for tokenizer file path resolution
  - Improved handling of vocab.json and merges.txt file loading
  - Enhanced error handling for edge cases in tokenizer initialization

### Version 1.6.2
- Fixed tokenizer loading issue where HuggingFace cache could interfere with local files
- Tokenizer now loads directly from specified path, avoiding cache conflicts
- Added explicit file path loading for better reliability
- Improved logging to show which tokenizer files are being used

### Version 1.6.1
- Improved integration by removing HuggingFace unnecessary settings

### Version 1.6.0
- **Major Change**: Removed automatic model downloading from HuggingFace
  - Models must now be manually downloaded and placed in `ComfyUI/models/vibevoice/`
  - Dynamic model dropdown that scans available models on each browser refresh
  - Support for custom folder names and HuggingFace cache structure
  - Automatic detection of quantized models from config files
  - Better user control over model management
  - Eliminates authentication issues with private HuggingFace repos
- **Improved Logging System**:
  - Optimized logging to reduce console clutter
  - Cleaner output for better user experience

### Version 1.5.0
- Added Voice Speed Control feature for adjusting speech rate
  - New `voice_speed_factor` parameter in both Single and Multi Speaker nodes
  - Time-stretching applied to reference audio to influence output speech rate
  - Range: 0.8 to 1.2 with 0.01 step increments
  - Recommended range: 0.95 to 1.05 for natural results
  - Best results with 20+ seconds of reference audio

### Version 1.4.3
- Improved LoRA system with better logging and compatibility checks
  - Added model compatibility detection to prevent mismatched LoRA loading
  - Enhanced debug logging for LoRA component loading process
  - Automatic detection and clear error messages for incompatible model-LoRA combinations
  - Prevents loading errors when using quantized models with standard LoRAs
  - Minor optimizations to LoRA weight loading process

### Version 1.4.2
- Bug Fixing

### Version 1.4.1
- Fixed HuggingFace authentication error when loading locally cached models
  - Resolved 401 authorization errors for already downloaded models
  - Node now correctly uses local model snapshots without requiring HuggingFace API authentication
  - Prevents unnecessary API calls when models exist in `ComfyUI/models/vibevoice/`

### Version 1.4.0
- Added LoRA (Low-Rank Adaptation) support for fine-tuned models
  - New "VibeVoice LoRA" node for configuring custom voice adaptations
  - Support for language model, diffusion head, and connector adaptations
  - Dropdown menu for easy LoRA selection from `ComfyUI/models/vibevoice/loras/`
  - Adjustable LoRA strength and component toggles
  - Compatible with both Single and Multiple Speaker nodes
  - Minimal memory overhead (~100-500MB per LoRA)
  - Credits: Implementation by [@jpgallegoar](https://github.com/jpgallegoar)

### Version 1.3.0
- Added custom pause tag support for speech pacing control
  - New `[pause]` tag for 1-second silence (default)
  - New `[pause:ms]` tag for custom duration in milliseconds (e.g., `[pause:2000]` for 2 seconds)
  - Works with both Single Speaker and Multiple Speakers nodes
  - Automatically splits text at pause points while maintaining voice consistency
  - Note: This is a wrapper feature, not part of Microsoft's VibeVoice

### Version 1.2.5
- Bug Fixing

### Version 1.2.4
- Added automatic text chunking for long texts in Single Speaker node
  - Single Speaker node now automatically splits texts longer than 250 words to prevent audio acceleration issues
  - New optional parameter `max_words_per_chunk` (range: 100-500 words, default: 250)
  - Maintains consistent voice characteristics across all chunks using the same seed
  - Seamlessly concatenates audio chunks for smooth, natural output

### Version 1.2.3
- Added SageAttention support for inference speedup
  - New attention option "sage" using quantized attention (INT8/FP8) for faster generation
  - Requirements: NVIDIA GPU with CUDA and sageattention library installation

### Version 1.2.2
- Added 4-bit quantized model support
  - New model in menu: `VibeVoice-Large-Quant-4Bit` using ~7GB VRAM instead of ~17GB
  - Requirements: NVIDIA GPU with CUDA and bitsandbytes library installed

### Version 1.2.1
- Bug Fixing

### Version 1.2.0
- MPS Support for Apple Silicon:
  - Added GPU acceleration support for Mac with Apple Silicon (M1/M2/M3)
  - Automatically detects and uses MPS backend when available, providing significant performance improvements over CPU

### Version 1.1.1
- Universal Transformers Compatibility:
  - Implemented adaptive system that automatically adjusts to different transformers versions
  - Guaranteed compatibility from v4.51.3 onwards
  - Auto-detects and adapts to API changes between versions

### Version 1.1.0
- Updated the URL for downloading the VibeVoice-Large model
- Removed VibeVoice-Large-Preview deprecated model

### Version 1.0.9
- Embedded VibeVoice code directly into the wrapper
  - Added vvembed folder containing the complete VibeVoice code (MIT licensed)
  - No longer requires external VibeVoice installation
  - Ensures continued functionality for all users

### Version 1.0.8
- BFloat16 Compatibility Fix
  - Fixed tensor type compatibility issues with audio processing nodes
  - Input audio tensors are now converted from BFloat16 to Float32 for numpy compatibility
  - Output audio tensors are explicitly converted to Float32 to ensure compatibility with downstream nodes
  - Resolves "Got unsupported ScalarType BFloat16" errors when using voice cloning or saving audio

### Version 1.0.7
- Added interruption handler to detect user's cancel request
- Bug fixing

### Version 1.0.6
- Fixed a bug that prevented VibeVoice nodes from receiving audio directly from another VibeVoice node

### Version 1.0.5
- Added support for Microsoft's official VibeVoice-Large model (stable release)

### Version 1.0.4
- Improved tokenizer dependency handling

### Version 1.0.3
- Added `attention_type` parameter to both Single Speaker and Multi Speaker nodes for performance optimization
  - auto (default): Automatic selection of best implementation
  - eager: Standard implementation without optimizations
  - sdpa: PyTorch's optimized Scaled Dot Product Attention
  - flash_attention_2: Flash Attention 2 for maximum performance (requires compatible GPU)
- Added `diffusion_steps` parameter to control generation quality vs speed trade-off
  - Default: 20 (VibeVoice default)
  - Higher values: Better quality, longer generation time
  - Lower values: Faster generation, potentially lower quality

### Version 1.0.2
- Added `free_memory_after_generate` toggle to both Single Speaker and Multi Speaker nodes
- New dedicated "Free Memory Node" for manual memory management in workflows
- Improved VRAM/RAM usage optimization
- Enhanced stability for long generation sessions
- Users can now choose between automatic or manual memory management

### Version 1.0.1
- Fixed issue with line breaks in speaker text (both single and multi-speaker nodes)
- Line breaks within individual speaker text are now automatically removed before generation
- Improved text formatting handling for all generation modes

### Version 1.0.0
- Initial release
- Single speaker node with voice cloning
- Multi-speaker node with automatic speaker detection
- Text file loading from ComfyUI directories
- Deterministic and sampling generation modes
- Support for VibeVoice 1.5B and Large models