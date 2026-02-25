# HuMo Audio Attention Boost (Advanced)

**⚠️ EXPERIMENTAL NODE - Use at your own risk**

ComfyUI custom node for granular Q/K/V/O attention boosting in HuMo models. Provides 12 independent controls for fine-tuning audio-driven motion response.

## What it does

This node uses runtime hooks to modify attention mechanisms in HuMo's transformer blocks. It allows independent control over Query, Key, Value, and Output projections across three attention types:

- **Audio Cross-Attention** - Direct audio → motion pathway
- **Text Cross-Attention** - Text conditioning (shares latent space with audio)
- **Self-Attention** - Spatial motion coherence within frames

Each attention type gets 4 independent numeric controls (Q/K/V/O), totaling 12 adjustable parameters.

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/ckinpdx/comfyui-humo-audio-motion
```
Restart ComfyUI.

## Usage

Place this node after your WanVideo Model Loader:

```
WanVideo Model Loader → HuMo Audio Attention Boost → HuMo Embeds → ...
```

### Parameters

Each attention type (audio/cross/self) has 4 component controls:

**q_boost** - Query projection (what to look for)
**k_boost** - Key projection (what's available)  
**v_boost** - Value projection (actual content)
**o_boost** - Output projection (final result)

**Block ranges:**
- early_0-10_body
- early_mid_0-20_full_body
- mid_10-25_gestures
- most_0-30_aggressive
- all_0-39_maximum
- custom (specify your own range)

### How boosting works

- **0.0-0.9** = attenuate (reduce influence)
- **1.0** = neutral (no change)
- **1.1-5.0+** = amplify (increase influence)

The node automatically cleans up old hooks on each run, so changes don't accumulate across generations.

## Important Limitations

**⚠️ Does NOT work with torch.compile**
- Hooks bypass compilation optimization
- You must disable torch.compile for this node to function

**⚠️ Memory intensive**
- Hooks duplicate tensors at each attention layer
- Higher resolutions may cause OOM errors
- Fewer hooks = less memory (use narrower block ranges)

**⚠️ Experimental**
- No stable parameter values have been established
- May cause artifacts, desaturation, or other visual issues
- Intended for experimentation and research

## Technical Details

The node registers forward hooks on attention projection layers in HuMo's transformer blocks. Each hook multiplies the output by the specified boost factor.

Hooks are cleaned up automatically on each execution to prevent accumulation. Original model weights are never modified - hooks only affect runtime computation.

## Requirements

- ComfyUI
- Kijai's ComfyUI-WanVideoWrapper
- HuMo model weights
- torch.compile must be **disabled**

No additional Python dependencies needed.

## Troubleshooting

**"Hooks not firing / no effect":**
- Ensure torch.compile is disabled
- Check console output for hook registration messages

**"Out of memory errors":**
- Reduce block range (fewer blocks = fewer hooks)
- Lower resolution
- Disable some attention types

**"Visual artifacts/desaturation":**
- Lower boost values
- Try different component combinations
- This is an ongoing research area

## Credits

Created while investigating audio-driven motion mechanisms in HuMo. This is a research tool for understanding attention pathways.

## License

MIT
