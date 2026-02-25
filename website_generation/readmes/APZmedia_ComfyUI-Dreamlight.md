# ComfyUI DreamLight Node

## Installation
1. Clone this repository into your ComfyUI's `custom_nodes` directory:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/APZmedia/ComfyUI-Dreamlight.git
```

2. Install dependencies:
```bash
cd ComfyUI-Dreamlight
pip install -r requirements.txt
```

3. Set up HuggingFace authentication (REQUIRED for FLUX.1-dev):
```bash
# Copy the example environment file
cp .env.example .env

# Get your HuggingFace token and request access to FLUX.1-dev
# 1. Get your token from: https://huggingface.co/settings/tokens
# 2. Request access to FLUX.1-dev: https://huggingface.co/black-forest-labs/FLUX.1-dev
# 3. Add your token to .env file:
echo "HF_TOKEN=your_huggingface_token_here" > .env
```

**⚠️ IMPORTANT**: FLUX.1-dev is a **gated model** that requires:
- Valid HuggingFace token
- Access approval from the model authors
- Authentication for all downloads

4. Download DreamLight models:
```bash
# Create model directories
mkdir -p ckpt/FLUX/transformer
mkdir -p ckpt/CLIP

# Download FLUX transformer weights
curl -L "https://huggingface.co/LYAWWH/DreamLight/resolve/main/FLUX/transformer/model.pth" -o ckpt/FLUX/transformer/model.pth

# Download CLIP model
curl -L "https://huggingface.co/LYAWWH/DreamLight/resolve/main/CLIP/models/config.json" -o ckpt/CLIP/config.json
curl -L "https://huggingface.co/LYAWWH/DreamLight/resolve/main/CLIP/models/pytorch_model.bin" -o ckpt/CLIP/pytorch_model.bin
```

## Node Usage
The node appears under "image/postprocessing" as "DreamLightNode"

**Inputs:**
- `foreground_image`: Subject to be relit (IMAGE)
- `background_image`: New background (IMAGE)
- `mask`: Foreground subject mask (MASK)
- `prompt`: Lighting guidance text
- `seed`: Random seed for reproducibility
- `resolution`: Output resolution (256-2048)
- `environment_map`: Optional environment map (IMAGE)

**Output:**
- `relit_image`: Final image with consistent lighting

## Example Workflow
1. Load `test_dreamlight_workflow.json` in ComfyUI
2. Provide these files in the project root:
   - `example_foreground.png`
   - `example_background.png`
   - `example_mask.png`

## Model Management
- **Pre-Flight Validation**: All models are downloaded, validated, and tested during node initialization - before any inference is attempted
- **Complete FLUX Pipeline**: Downloads and validates the entire FLUX.1-dev pipeline (transformer, VAE, text encoders, tokenizers, scheduler)
- **Smart Model Detection**: Automatically searches for existing FLUX transformer weights and reuses them to save bandwidth
- **Comprehensive Flight Checks**: Validates all required components with detailed logging before proceeding
- **HuggingFace Authentication**: Set `HF_TOKEN` in `.env` file for authenticated downloads
- **Fail-Fast Design**: Node initialization will fail immediately if models can't be downloaded or validated

## Notes
- First run will take longer as it downloads additional dependencies
- Requires GPU with at least 8GB VRAM
- For optimal results, use 1024x1024 resolution
- Environment maps should be 360° equirectangular images

## Troubleshooting

### Automatic Setup Issues
If the automatic model setup fails, you can manually install the required models:

#### Manual FLUX Model Installation

1. **Create the complete FLUX directory structure:**
```bash
# Navigate to your ComfyUI models directory
cd ComfyUI/models

# Create the dedicated FLUX directory
mkdir -p dreamlight/flux_complete
cd dreamlight/flux_complete
```

2. **Download the complete FLUX.1-dev model from HuggingFace:**
```bash
# ⚠️ FLUX.1-dev is GATED - authentication required!

# Option A: Using git (requires authentication)
git clone https://huggingface.co/black-forest-labs/FLUX.1-dev .
# You'll be prompted for your HuggingFace username and token

# Option B: Using huggingface-hub (recommended)
pip install huggingface-hub
python -c "
from huggingface_hub import snapshot_download
snapshot_download(
    repo_id='black-forest-labs/FLUX.1-dev',
    local_dir='.',
    local_dir_use_symlinks=False,
    token='your_hf_token_here'  # Required for gated models
)
"
```

3. **If you have existing FLUX weights, replace the transformer:**
```bash
# If you have flux1-dev.safetensors elsewhere, copy it:
cp /path/to/your/flux1-dev.safetensors transformer/diffusion_pytorch_model.safetensors
```

#### Manual CLIP Model Installation

1. **Create CLIP directory:**
```bash
mkdir -p ComfyUI/models/dreamlight/CLIP/models
cd ComfyUI/models/dreamlight/CLIP/models
```

2. **Download CLIP model files:**
```bash
# Download config and model files
wget https://huggingface.co/LYAWWH/DreamLight/resolve/main/CLIP/models/config.json
wget https://huggingface.co/LYAWWH/DreamLight/resolve/main/CLIP/models/pytorch_model.bin
```

#### Verification Steps

After manual installation, verify the structure:

```bash
# Check FLUX directory structure
ls -la ComfyUI/models/dreamlight/flux_complete/
# Should contain: model_index.json, vae/, text_encoder/, text_encoder_2/, transformer/, tokenizer/, tokenizer_2/, scheduler/

# Check each component has required files
ls -la ComfyUI/models/dreamlight/flux_complete/vae/
# Should contain: config.json, diffusion_pytorch_model.safetensors

ls -la ComfyUI/models/dreamlight/flux_complete/transformer/
# Should contain: config.json, diffusion_pytorch_model.safetensors

# Check CLIP directory
ls -la ComfyUI/models/dreamlight/CLIP/models/
# Should contain: config.json, pytorch_model.bin
```

#### Common Issues and Solutions

**Issue: "Error no file named diffusion_pytorch_model.bin found"**
- **Solution**: The FLUX directory is incomplete. Use the manual installation steps above.

**Issue: "Authentication failed" or "HuggingFace token required"**
- **Solution**: FLUX.1-dev is gated - you need:
  1. **Get HuggingFace token**: https://huggingface.co/settings/tokens
  2. **Request access to FLUX.1-dev**: https://huggingface.co/black-forest-labs/FLUX.1-dev
  3. **Set token in .env file**:
```bash
echo "HF_TOKEN=your_token_here" > .env
```
  4. **Wait for access approval** (may take time)
  5. **Restart ComfyUI** after setting token

**Issue: "Out of memory"**
- **Solution**: Reduce resolution or use CPU:
```python
# In the node, set resolution to 512 or lower
```

**Issue: "Model validation failed"**
- **Solution**: Check the logs for specific missing files and download them manually.

#### Directory Structure Reference

The complete directory structure should look like:
```
ComfyUI/models/dreamlight/
├── flux_complete/
│   ├── model_index.json
│   ├── vae/
│   │   ├── config.json
│   │   └── diffusion_pytorch_model.safetensors
│   ├── text_encoder/
│   │   ├── config.json
│   │   └── model.safetensors
│   ├── text_encoder_2/
│   │   ├── config.json
│   │   └── model.safetensors
│   ├── transformer/
│   │   ├── config.json
│   │   └── diffusion_pytorch_model.safetensors
│   ├── tokenizer/
│   │   └── tokenizer_config.json
│   ├── tokenizer_2/
│   │   └── tokenizer_config.json
│   └── scheduler/
│       └── scheduler_config.json
└── CLIP/
    └── models/
        ├── config.json
        └── pytorch_model.bin
```

### General Troubleshooting
If you encounter issues:
1. Verify all model files are in the correct directories
2. Ensure you have the required dependencies
3. Check console for specific error messages
4. Try reducing resolution if out of memory
5. Use the manual installation steps above if automatic setup fails
