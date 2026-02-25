# ComfyUI-SteadyDancer

A ComfyUI wrapper for SteadyDancer I2V (Wan I2V) with first-frame preservation. Two nodes:
- `SteadyDancerBasic`: minimal inputs, sane defaults.
- `SteadyDancerAdvanced`: all tunable parameters.

## Features
- Pose alignment (positive + optional negative) via upstream scripts, then calls `wan.WanI2VDancer` to generate frames.
- Outputs IMAGE_BATCH for generation and pose (viz).
- Basic node: prompt + model + images; Advanced node exposes align/sampling options.
