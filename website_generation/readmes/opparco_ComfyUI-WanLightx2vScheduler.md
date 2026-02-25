# Wan2.2 Lightx2v Scheduler for ComfyUI

A custom ComfyUI node package designed specifically for **Wan2.2 Lightx2v** models to fix the "burnt-out" look, over-sharpening, and abrupt lighting shifts through proper denoising trajectory alignment.

## Problem & Solution

### The Issue
When using Wan2.2 with the lightx2v LoRA, users commonly experience:
- **"Burnt-out"** appearance with excessive contrast
- **Over-sharpening** artifacts  
- **Abrupt lighting shifts** between frames

### The Solution
This package generates **custom sigmas** that recreate the exact denoising trajectory the LoRA was trained on, ensuring consistent results across different step counts.

## Installation

1. Clone this repository to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes/
   git clone https://github.com/opparco/ComfyUI-WanLightx2vScheduler
   ```

2. Restart ComfyUI

## Nodes Included

### WanLightx2vSchedulerBasic **Recommended**
- **Purpose**: Precise sigma scheduling with theoretical accuracy
- **Inputs**:
  - `steps`: Number of sampling steps (1-10000, default: 4)
  - `sigma_max`: Maximum sigma value (**Use 1.0 for theoretical accuracy**)
  - `sigma_min`: Minimum sigma value (**Use 0.0 for theoretical accuracy**)
  - `shift`: Time shift parameter (0.1-100.0, **use 5.0 for lightx2v**)
- **Output**: `SIGMAS` tensor for custom sampling

### WanLightx2vSchedulerBasicFromModel
- **Purpose**: Automatic sigma scheduling using model parameters *(may not match theoretical values)*
- **Inputs**:
  - `model`: The model to extract sigma parameters from
  - `steps`: Number of sampling steps (1-10000, default: 4)
  - `shift`: Time shift parameter (0.1-100.0, default: 5.0)
- **Output**: `SIGMAS` tensor for custom sampling
- **Note**: Use `Lightx2vSchedulerBasic` with sigma_min=0.0, sigma_max=1.0 for best results

### KSamplerAdvancedPartialSigmas
- **Purpose**: Advanced sampler supporting custom sigma schedules and partial step execution
- **Inputs**:
  - `model`: Model for sampling
  - `positive`: Positive conditioning
  - `negative`: Negative conditioning
  - `latent_image`: Input latent
  - `sampler_name`: Sampler algorithm
  - `sigmas`: Custom sigma schedule
  - `cfg`: CFG scale (0.0-100.0, default: 1.0)
  - `steps`: Number of steps to execute (1-10000, default: 4)
  - `add_noise`: Whether to add noise (default: True)
  - `noise_seed`: Random seed for noise generation
- **Outputs**: 
  - `output`: Final sampled latent
  - `denoised_output`: Denoised output (when available)

## Usage Example

### Basic Workflow:
1. Load your Wan2.2 Lightx2v model
2. Add `WanLightx2vSchedulerBasic` node
3. Set parameters:
   - **sigma_min**: 0.0 (for theoretical accuracy)
   - **sigma_max**: 1.0 (for theoretical accuracy) 
   - **shift**: 5.0 (matches LoRA training trajectory)
   - **steps**: 4, 8, 16, or 20
4. Connect sigmas output to `KSamplerAdvancedPartialSigmas`
5. Configure sampler parameters as needed

## Contributing

Contributions are welcome! Please feel free to submit issues and enhancement requests.
