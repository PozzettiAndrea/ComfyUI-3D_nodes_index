# Jurdns Iterative Noise KSampler

A ComfyUI custom node that adds controlled noise injection during the sampling process for enhanced image generation quality and detail.

## Features

- **Iterative Noise Injection**: Adds carefully controlled noise at specified intervals during sampling
- **Progressive Noise Control**: Start and end noise strength parameters for gradual transitions
- **Flexible Timing**: Configure how often noise is added with the step interval parameter
- **Full Compatibility**: Works with all ComfyUI samplers and schedulers
- **Deterministic Results**: Seeded noise generation for reproducible outputs

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| **add_noise_every_n_steps** | INT | 1 | Add noise every N steps |
| **start_noise_strength** | FLOAT | 0.1 | Initial noise strength |
| **end_noise_strength** | FLOAT | 0.0 | Final noise strength |

Plus all standard KSampler parameters (model, conditioning, steps, CFG, sampler, scheduler, etc.)

## How It Works

The node injects controlled noise during the sampling process at specified intervals. The noise strength progressively changes from the start value to the end value, allowing for enhanced detail generation, improved texture quality, and better handling of complex compositions. The noise injection uses the current sigma values for proper scaling and maintains deterministic behavior through seeded random generation.

## Installation

### ComfyUI Manager
Search for "Jurdns Iterative Noise KSampler" in ComfyUI Manager and install.

### Manual Installation
```bash
cd /path/to/ComfyUI/custom_nodes/
git clone https://github.com/jurdnf/ComfyUI-JurdnsIterativeNoiseKSampler.git
```
Then restart ComfyUI.
