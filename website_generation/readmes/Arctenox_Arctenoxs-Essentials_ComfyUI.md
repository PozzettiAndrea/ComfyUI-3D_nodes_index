# Arctenox's Essentials

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-brightgreen.svg)](https://github.com/comfyanonymous/ComfyUI)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A collection of efficient workflow nodes for ComfyUI, designed to streamline and optimize your generation process with combined functionality and improved performance.
---
## 📧 Contact & Support

- **Discord**: https://discord.gg/UVXPdkgedh
- **GitHub**: [@Arctenox](https://github.com/Arctenox)
- **Issues**: [GitHub Issues](https://github.com/Arctenox/Arctenoxs-Essentials_ComfyUI/issues)
---
## 📦 Installation

### Via ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "Arctenoxs-Essentials_ComfyUI" or "Arctenox's Essentials"
3. Click Install
4. Restart ComfyUI

### Manual Installation

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/Arctenox/Arctenoxs-Essentials_ComfyUI
   ```

3. Restart ComfyUI

### Requirements

- ComfyUI (latest version recommended)
- PyTorch >= 1.12.0
- Python >= 3.8
- Optional: `psutil` for CPU memory monitoring

If you encounter missing dependencies, install them with:
```bash
pip install torch numpy psutil
```

---

## 🎯 Overview

Arctenox's Essentials provides a suite of powerful workflow nodes that enhance ComfyUI with advanced sampling techniques, intelligent seed management, temporal prompt processing, and workflow optimization tools. Each node is designed to integrate seamlessly into your existing workflows while adding sophisticated functionality.

### Key Features

- 🎲 **Advanced KSampler** - Combined latent generation and sampling with golden ratio sonar transformation
- 🗺️ **Seed Topology Mapping** - Generate mathematically related seed families
- ⏱️ **Temporal Prompt Splitting** - Progressive refinement through composition → detail → texture phases
- ⚠️ **Artifact Risk Prediction** - Detect potential issues before VAE decoding
- 💰 **Cost Estimation** - Real-time VRAM, time, and efficiency metrics
- 💾 **Metadata Preservation** - Save images with complete generation parameters
- 🎨 **Prompt Styling** - 40+ presets for different artistic styles
- 📦 **Workflow Utilities** - Organization boxes, checkpoint passthrough, and more
- 🚀 **Performance Optimized** - Memory-efficient processing across CUDA/MPS/CPU

---

## 📚 Node Documentation

### 🎲 KSampler (Arctenox's Essentials)

An enhanced sampler that combines latent generation with advanced sampling features and golden ratio sonar transformation.

**Location:** `Arctenox Essentials/Sampling`

#### Inputs

| Input | Type | Description |
|-------|------|-------------|
| `model` | MODEL | The model to use for sampling |
| `positive` | CONDITIONING | Positive conditioning (what you want) |
| `negative` | CONDITIONING | Negative conditioning (what to avoid) |
| `width` | INT | Image width (64-8192, step 8) |
| `height` | INT | Image height (64-8192, step 8) |
| `batch_size` | INT | Number of images (1-64) |
| `seed` | INT | Base random seed |
| `sonar` | INT | Golden ratio transformation offset |
| `steps` | INT | Sampling steps (1-10000+) |
| `cfg` | FLOAT | Classifier-free guidance scale (0.0-100.0+) |
| `sampler_name` | STRING | Sampling algorithm |
| `scheduler` | STRING | Noise schedule |
| `denoise` | FLOAT | Denoising strength (0.0-1.0) |
| `vae_decode` | BOOLEAN | Enable/disable automatic decoding |
| `latent_image` | LATENT (optional) | Input latent for img2img |
| `optional_vae` | VAE (optional) | VAE for decoding |

#### Outputs

| Output | Type | Description |
|--------|------|-------------|
| `MODEL` | MODEL | Passthrough of input model |
| `CONDITIONING+` | CONDITIONING | Passthrough of positive conditioning |
| `CONDITIONING-` | CONDITIONING | Passthrough of negative conditioning |
| `LATENT` | LATENT | Generated latent samples |
| `VAE` | VAE | Passthrough of input VAE |
| `IMAGE` | IMAGE | Decoded image (if vae_decode enabled) |

#### Features

##### Golden Ratio Sonar Transformation

The sonar parameter applies a sophisticated seed transformation based on the golden ratio (φ ≈ 1.618):

```
φ⁻¹ ≈ 0.618033988749895
```

**How It Works:**
1. Base hash transformation for deterministic offset
2. Golden ratio influence for values > 10
3. Conservative 10% influence factor
4. Sign preservation for negative sonar values
5. 32-bit seed space normalization

**Benefits:**
- Aesthetically pleasing variation patterns
- Deterministic and reproducible
- Smooth transitions between related seeds
- Natural-feeling exploration of latent space

**Example Usage:**
```
Base Seed: 42
Sonar: 0 → Standard generation
Sonar: 100 → Subtle golden ratio influenced variation
Sonar: -100 → Opposite direction variation
```

##### Intelligent CFG Handling

Handles extreme CFG values gracefully:
- Normal range (≤100): Direct passthrough
- Large values (>100): Logarithmic scaling
- Prevents sampling instability
- Maintains quality across extreme settings

##### Large Step Support

Intelligently handles astronomical step counts:
- Normal range (≤10000): Direct passthrough
- Large values: Capped at reasonable maximum
- Prevents memory issues
- Maintains sampling quality

##### Negative Seed Support

Deterministic hashing for negative seed values:
- Consistent results for negative seeds
- Reproducible transformations
- Expands exploration space

#### Use Cases

- Exploring seed variations systematically with sonar
- Batch generation with consistent quality
- Streamlined workflows without separate latent nodes
- Experimenting with extreme CFG values
- Quick iterations without manual latent creation

---

### 🗺️ Seed Topology Mapper

Generate families of mathematically related seeds for structured exploration of the latent space.

**Location:** `Arctenox Essentials/Sampling`

#### Inputs

| Input | Type | Description |
|-------|------|-------------|
| `base_seed` | INT | Starting seed for topology generation |
| `topology_type` | STRING | Mathematical spacing method |
| `num_seeds` | INT | Number of seeds to generate (1-16) |
| `spread` | FLOAT | Spacing multiplier (0.1-10.0) |

#### Outputs

Returns 16 seed outputs (`seed_1` through `seed_16`), each of type INT.

#### Topology Types

| Type | Description | Best For | Recommended Spread |
|------|-------------|----------|-------------------|
| **Golden Angle** | Seeds spaced by 137.5° golden angle | Natural, organic variations | 0.5-2.0 |
| **Harmonic** | Musical harmony ratios (1:2:3:4...) | Rhythmic, balanced sets | 1.0-5.0 |
| **Fibonacci** | Fibonacci sequence spacing | Natural progression patterns | 0.1-1.0 |
| **Chaos Neighbors** | Controlled chaotic spacing | Unpredictable but related results | 0.5-1.5 |
| **Prime Spiral** | Prime number spiral distribution | Mathematical exploration | 1.0-3.0 |
| **Phi Spacing** | Golden ratio (φ) based intervals | Aesthetically pleasing variations | 0.5-2.0 |

#### Mathematical Details

Each topology uses distinct mathematical spacing:

- **Golden Angle**: `137.5077°` rotation spacing
- **Harmonic**: Multiply by integer ratios
- **Fibonacci**: Add Fibonacci sequence values
- **Chaos**: Logistic map with `r=3.9`
- **Prime Spiral**: Prime number intervals
- **Phi Spacing**: Exponential golden ratio growth

#### Use Cases

- Create seed families with related characteristics
- Systematic exploration of variations
- Reproducible batch processing workflows
- Finding "neighboring" results in latent space
- Generating consistent variation sets

#### Example Workflow

```
Base Seed: 42
Topology: golden_angle
Num Seeds: 8
Spread: 1.0

Result: 8 deterministically related seeds, each exploring
a different "direction" in the latent space while maintaining
a golden angle relationship
```

---

### ⏱️ Prompt Phase Splitter

Split your generation into temporal phases for progressive refinement and enhanced control.

**Location:** `Arctenox Essentials/Sampling`

#### Phase System

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ COMPOSITION │ ──> │   DETAIL    │ ──> │   TEXTURE   │
│   Phase     │     │   Phase     │     │   Phase     │
│  (Early)    │     │  (Middle)   │     │   (Late)    │
└─────────────┘     └─────────────┘     └─────────────┘
```

#### Inputs

| Input | Type | Default | Description |
|-------|------|---------|-------------|
| `clip` | CLIP | - | CLIP model for text encoding |
| `composition_prompt` | STRING | "" | Early phase - overall composition and layout |
| `detail_prompt` | STRING | "" | Middle phase - subject details and refinement |
| `texture_prompt` | STRING | "" | Late phase - surface qualities and fine details |
| `composition_weight` | FLOAT | 1.0 | Strength of composition phase (0.0-2.0) |
| `detail_weight` | FLOAT | 1.0 | Strength of detail phase (0.0-2.0) |
| `texture_weight` | FLOAT | 1.0 | Strength of texture phase (0.0-2.0) |
| `phase_1_steps` | INT | 10 | Steps for composition phase |
| `phase_2_steps` | INT | 10 | Steps for detail phase |
| `phase_3_steps` | INT | 5 | Steps for texture phase |
| `enable_character_focus` | BOOLEAN | false | Optional character/subject emphasis |
| `character_focus_prompt` | STRING | "" | Subject-specific refinement |
| `character_weight` | FLOAT | 1.0 | Character focus strength (0.0-2.0) |

#### Outputs

| Output | Type | Description |
|--------|------|-------------|
| `combined_conditioning` | CONDITIONING | Weighted combination of all phases |
| `total_steps` | INT | Sum of all phase steps |

#### How It Works

The temporal phase system divides the sampling process into three cognitive stages:

```
Total Steps = Phase1 + Phase2 + Phase3

Phase 1 (Composition): Steps 0 → N₁
  └─ Global structure, layout, composition

Phase 2 (Detail): Steps N₁ → N₂  
  └─ Subject refinement, feature details

Phase 3 (Texture): Steps N₂ → Total
  └─ Surface qualities, fine textures
```

Each phase is weighted and combined to create a temporally-aware conditioning that guides the sampler through progressive refinement stages.

#### Use Cases

- Separate composition from detail refinement
- Better control over generation progression
- Prevent early detail interference with composition
- Character-focused image generation
- Architectural and landscape rendering with distinct phases
- Portrait generation with facial detail emphasis

#### Example: Portrait Generation

```
Phase 1 (10 steps, weight 1.0):
"portrait of a person, professional photography"

Phase 2 (10 steps, weight 1.0):
"detailed facial features, expressive eyes, natural skin"

Phase 3 (5 steps, weight 1.0):
"fine skin texture, hair detail, fabric texture"

Character Focus (enabled, weight 1.2):
"the subject's face and expression"
```

This ensures the composition establishes the overall portrait first, then refines facial features, and finally adds texture details, with extra emphasis on the face throughout.

---

### ⚠️ Artifact Risk Predictor

Analyze latent samples before VAE decoding to predict potential artifacts and quality issues.

**Location:** `Arctenox Essentials/Utilities`

#### Inputs

| Input | Type | Description |
|-------|------|-------------|
| `latent` | LATENT | Latent samples to analyze |

#### Outputs

| Output | Type | Description |
|--------|------|-------------|
| `risk_score` | FLOAT | Numerical risk assessment (0.0-1.0) |
| `risk_level` | STRING | Categorized risk level |
| `latent_passthrough` | LATENT | Original latent for downstream processing |

#### Detection Capabilities

The predictor analyzes latent samples for:

- **High-frequency noise patterns** - Excessive noise in high frequencies
- **Extreme value spikes** - Abnormal peaks in latent values
- **Abnormal distribution patterns** - Statistical anomalies in value distribution
- **Channel inconsistencies** - Imbalances between latent channels
- **Statistical anomalies** - Deviation from expected latent statistics
- **Overbakedness/Artifacts** - Signs of overprocessing

#### Risk Levels

| Level | Range | Color | Description |
|-------|-------|-------|-------------|
| **Low** | 0.0-0.3 | 🟢 | Clean generation expected, no issues detected |
| **Medium** | 0.3-0.6 | 🟡 | Minor artifacts possible, generally acceptable |
| **High** | 0.6-1.0 | 🔴 | Significant issues likely, consider regenerating |

#### Use Cases

- Quality control before VAE decoding
- Pre-publication image validation
- Automatic bad sample filtering
- Debugging problematic generations
- Batch processing optimization
- Saving time by catching issues early

#### Example Workflow

```
[KSampler] → [Artifact Risk Predictor] → [Conditional VAE Decode]
                      ↓
              [Filter High Risk]
```

Only decode latents with acceptable risk scores, saving computation time and storage.

---

### 💰 Execution Cost Estimator

Real-time performance metrics and resource usage estimation for your workflows.

**Location:** `Arctenox Essentials/Utilities`

#### Inputs

| Input | Type | Description |
|-------|------|-------------|
| `model` | MODEL | Model to analyze |
| `width` | INT | Target image width |
| `height` | INT | Target image height |
| `batch_size` | INT | Number of samples |
| `steps` | INT | Sampling steps |
| Additional analysis toggles | BOOLEAN | Enable various analysis features |

#### Outputs

| Output | Type | Description |
|--------|------|-------------|
| `cost_info` | STRING | Detailed cost breakdown |
| `vram_estimate` | FLOAT | Estimated VRAM usage (GB) |
| `time_estimate` | FLOAT | Expected generation duration (seconds) |
| `efficiency_score` | FLOAT | Performance optimization rating |

#### Metrics Provided

- **VRAM Usage**: GPU memory consumption estimate
- **Execution Time**: Expected generation duration
- **Efficiency Score**: Performance optimization rating
- **Bottleneck Analysis**: Identify performance limiters
- **Resource Recommendations**: Suggestions for optimization

#### Use Cases

- Workflow optimization
- Hardware upgrade planning
- Batch size optimization
- Performance debugging
- Resource allocation planning
- Preventing OOM errors

**Note:** Estimates are not 100% accurate but provide useful guidance for workflow planning.

---

### 💾 Save Image With Metadata (Arctenox's Essentials)

Save images with complete generation parameters embedded in metadata for full reproducibility.

**Location:** `Arctenox Essentials/Output`

#### Inputs

| Input | Type | Description |
|-------|------|-------------|
| `images` | IMAGE | Images to save |
| `filename_prefix` | STRING | Prefix for saved filenames |
| Various metadata fields | STRING/INT/FLOAT | Generation parameters to embed |

#### Features

- Embeds complete generation parameters in PNG metadata
- Supports Civitai resource detection via model hashes
- Compatible with A1111/Automatic1111 metadata format
- Preserves seed, prompt, model, sampler, and all settings
- Enables perfect reproducibility of generations

#### Use Cases

- Creating reproducible workflows
- Sharing generation settings with others
- Building dataset with complete provenance
- Documenting successful generations
- Civitai automatic resource linking

---

### 🎨 Prompt Styler (Arctenox's Essentials)

Apply professional styling presets to your prompts with 40+ built-in styles.

**Location:** `Arctenox Essentials/Prompting`

#### Available Styles

**Photography Styles:**
- Cinematic
- Portrait
- Landscape
- Macro
- Street Photography
- Fashion
- Product Photography
- Documentary

**Artistic Styles:**
- Oil Painting
- Watercolor
- Digital Art
- Anime
- Sketch
- Comic Book
- Concept Art
- Abstract

**Technical Styles:**
- Photorealistic
- Hyperrealistic
- Studio Lighting
- Natural Light
- Dramatic Lighting
- Soft Focus
- High Contrast
- Vintage

And many more...

#### Use Cases

- Quick style application without remembering complex prompts
- Consistent styling across batches
- Learning effective prompt structures
- Experimenting with different artistic styles
- Professional-quality prompt construction

---

### 📝 CLIP Text Encode + String (Arctenox's Essentials)

Standard CLIP text encoding with additional string output for metadata capture.

**Location:** `Arctenox Essentials/Conditioning`

#### Inputs

| Input | Type | Description |
|-------|------|-------------|
| `text` | STRING | Text to encode with CLIP |
| `clip` | CLIP | CLIP model |

#### Outputs

| Output | Type | Description |
|--------|------|-------------|
| `conditioning` | CONDITIONING | CLIP-encoded conditioning |
| `text` | STRING | Original text for metadata |

#### Use Cases

- Capturing prompts for metadata embedding
- Documenting exact prompts used
- Connecting to SaveImageWithMetadata
- Maintaining prompt history

---

### 🔧 Load Checkpoint + String (Arctenox's Essentials)

Load checkpoints with model name and hash output for Civitai detection.

**Location:** `Arctenox Essentials/Loaders`

#### Inputs

| Input | Type | Description |
|-------|------|-------------|
| `ckpt_name` | STRING | Name of checkpoint file |

#### Outputs

| Output | Type | Description |
|--------|------|-------------|
| `model` | MODEL | Loaded model |
| `clip` | CLIP | Loaded CLIP |
| `vae` | VAE | Loaded VAE |
| `model_name` | STRING | Checkpoint filename |
| `model_hash` | STRING | SHA256 hash (first 10 chars) |

#### Features

- Efficient hash caching to avoid recalculation
- SHA256 AutoHash format (compatible with A1111/Civitai)
- Automatic Civitai resource detection when embedded in metadata

#### Use Cases

- Metadata capture for reproducibility
- Civitai automatic model linking
- Documenting exact model versions used
- Building model usage databases

---

### 📦 Checkpoint Passthrough + Notes (Arctenox's Essentials)

Pass through MODEL, CLIP, and VAE together with optional documentation.

**Location:** `Arctenox Essentials/Utilities`

#### Inputs

| Input | Type | Description |
|-------|------|-------------|
| `model` | MODEL | Model to pass through |
| `clip` | CLIP | CLIP to pass through |
| `vae` | VAE | VAE to pass through |
| `notes` | STRING (optional) | Documentation notes |

#### Outputs

| Output | Type | Description |
|--------|------|-------------|
| `model` | MODEL | Passthrough of input model |
| `clip` | CLIP | Passthrough of input CLIP |
| `vae` | VAE | Passthrough of input VAE |

#### Use Cases

- Organizing checkpoint flows in complex workflows
- Adding documentation to checkpoint sections
- Creating clean connection points for checkpoints
- Improving workflow readability
- Zero processing overhead - direct passthrough

---

### 📦 Box (Empty Node)

Simple organizational box for workflow documentation and structure.

**Location:** `Arctenox Essentials/Utilities`

#### Features

- No inputs or outputs
- Pure visual organization
- Workflow sectioning
- Documentation anchor points

#### Use Cases

- Visually separate workflow sections
- Add structure to complex graphs
- Create workflow "chapters"
- Improve readability
- Label different workflow stages

---

## 🛠️ Advanced Configuration

### Custom Sonar Curves

For advanced users, the sonar transformation can be tuned by modifying the influence factor in `ArctenoxEssentials_KSampler.py`:

```python
golden_influence = (abs_sonar * PHI_INVERSE * 0.1) % 1.0  # 0.1 = 10% influence
golden_adjustment = int(base_noise_seed * golden_influence * 0.05)  # 5% max change
```

Adjust these percentages to control how strongly the golden ratio influences seed transformations.

### Topology Spread Optimization

Different topology types respond differently to spread values:

| Topology | Optimal Spread Range | Notes |
|----------|---------------------|-------|
| Golden Angle | 0.5-2.0 | Subtle to extreme variations |
| Harmonic | 1.0-5.0 | Musical spacing |
| Fibonacci | 0.1-1.0 | Natural progressions |
| Chaos | 0.5-1.5 | Controlled chaos |
| Prime Spiral | 1.0-3.0 | Mathematical spacing |
| Phi Spacing | 0.5-2.0 | Aesthetic distributions |

---

## 🛟 Troubleshooting

### Node Not Appearing

1. Verify installation in `ComfyUI/custom_nodes/`
2. Check console for import errors
3. Ensure PyTorch is properly installed
4. Restart ComfyUI completely
5. Clear browser cache if using web interface

### Import Errors

Missing dependencies? Install with:
```bash
pip install torch numpy psutil
```

### Performance Issues

- Reduce batch size for VRAM constraints
- Use Cost Estimator to identify bottlenecks
- Enable CPU offloading in ComfyUI settings
- Consider lower resolution for testing
- Close other GPU-intensive applications

### Unexpected Results

- Verify seed values are within valid range
- Check sonar values aren't too extreme (±1000000)
- Ensure prompt weights are reasonable (0.5-2.0)
- Review phase step distributions
- Check that total steps match your expectations

### Known Issues

- Cancelling KSampler may show an error message - this is expected and safe to ignore
- Very large sonar values (>1000000) may produce unpredictable results
- Artifact Risk Predictor is a heuristic - not 100% accurate

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

```bash
git clone https://github.com/Arctenox/Arctenoxs-Essentials_ComfyUI
cd Arctenoxs-Essentials_ComfyUI
# Make your changes
# Test in ComfyUI
# Submit PR
```

### Guidelines

- Follow existing code style
- Add documentation for new nodes
- Test thoroughly before submitting
- Update README with new features

---

## 📄 License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.


---

## 🗺️ Roadmap

- [ ] More Nodes that I find suitable for this node pack that I can think up
- [ ] Workflow templates

---

**Made with ❤️ by Claude Sonnet 4.5/3.5 and Arctenox**

*Version 1.2.0 - Last Updated: December 21st 2025*
