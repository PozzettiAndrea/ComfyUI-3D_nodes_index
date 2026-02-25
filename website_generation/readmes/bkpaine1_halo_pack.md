# HALO Debug Pack

**AMD Strix Halo Diagnostic Tools for ComfyUI**

Diagnose bf16 precision issues that cause NaN values and black images on AMD ROCm.

## The Problem

AMD Strix Halo APUs (and potentially other ROCm devices) have issues with bfloat16 (bf16) precision. When ComfyUI tries to convert bf16 tensors to numpy for image output, you get:

```
RuntimeWarning: invalid value encountered in cast
```

Result: **Black images** or **NaN values** throughout the pipeline.

## What This Pack Does

1. **Debug nodes** to identify exactly where NaN/precision issues occur in your workflow
2. **FP32 VAE nodes** to force VAE encode/decode to use float32 (fixes the numpy bf16 bug)

## Installation

1. Navigate to your ComfyUI custom_nodes folder:
   ```bash
   cd /path/to/ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/bkpaine1/halo_pack.git
   ```

3. Restart ComfyUI

4. Find nodes under the **HALO** category

## Nodes Included

| Node | Purpose |
|------|---------|
| **HALO VAE Decode (FP32)** | Force VAE decode to FP32. Fixes the numpy bf16 conversion bug. |
| **HALO VAE Encode (FP32)** | Force VAE encode to FP32. Use for img2img workflows. |
| **HALO Latent Debug** | Check sampler output for NaN/dead latents. Put between sampler and VAE. |
| **HALO Conditioning Debug** | Check text encoder output for NaN. Put after CLIP Text Encode. |
| **HALO Model Debug** | Check model dtype (bf16/fp16/fp32). Put after model loader. |

## Usage

### Diagnosing Black Images

Add debug nodes throughout your workflow to find where NaN appears:

```
CLIPLoader → CLIPTextEncode → HALO Conditioning Debug
                                      ↓
UNETLoader → Sampler → HALO Latent Debug → HALO VAE Decode → SaveImage
```

Check the console output for diagnostic information:

```
============================================================
  HALO LATENT DEBUG
============================================================
  dtype:  torch.float32
  shape:  torch.Size([1, 16, 64, 64])
  device: cuda:0
  min:    -4.234521
  max:    3.891234
  mean:   0.012345
  std:    1.234567

  ✓ Latent looks valid!
============================================================
```

### Quick Fix for Black Images

If you're getting black images from bf16 VAE:

1. Replace `VAE Decode` with `HALO VAE Decode (FP32)`

If still getting black/NaN:

2. Add `HALO Latent Debug` before VAE to check if the problem is upstream
3. Add `HALO Conditioning Debug` after text encode to check conditioning
4. Add `HALO Model Debug` after model loader to see dtype

## Console Output Examples

### Healthy VAE Decode
```
[HALO-VAE] === DECODE START ===
[HALO-VAE] Latent: dtype=torch.float32, shape=torch.Size([1, 16, 64, 64])
[HALO-VAE] Latent stats: min=-3.2451, max=4.1234
[HALO-VAE] Forced VAE model to fp32 (was torch.bfloat16)
[HALO-VAE] Output stats: min=0.0000, max=1.0000
[HALO-VAE] ✓ Output looks valid!
[HALO-VAE] === DECODE COMPLETE ===
```

### Dead Latent (Problem Upstream)
```
[HALO-VAE] ⚠️ LATENT IS DEAD (all zeros) - problem is upstream!
```

### NaN from Model
```
  ❌ 1234 NaN values!
      Model is producing garbage - precision issue.
```

### NaN in Conditioning
```
    ❌ 1234 NaN values in conditioning!
       TEXT ENCODER is outputting garbage!
```

## Important Notes

- These are **diagnostic tools** - they help you find where the problem is
- If NaN appears in the latent, the problem is in the diffusion model (try `--force-fp32` flag)
- If NaN appears in conditioning, the problem is in the text encoder
- The HALO VAE nodes fix the specific bf16→numpy issue, but can't fix upstream NaN

## The Elephant in the Room

The root cause of many bf16 black image issues is that **numpy does not support bfloat16**. When PyTorch tensors in bf16 format get converted to numpy arrays for image saving, the cast fails silently and produces garbage.

This affects everyone: AMD ROCm, older NVIDIA cards, Apple Silicon, and any unified memory architecture where bf16 is common.

If numpy added native bf16 support, a significant portion of these "black image" issues across the ML ecosystem would simply disappear. Until then, we have workarounds like this pack.

*Dear numpy maintainers: bfloat16 has been standard in ML for years. We believe in you.*

## Tested On

- AMD Strix Halo APU (Ryzen AI Max+ 395 w/ Radeon 8060S)
- 128GB Unified Memory
- ROCm 6.x
- Ubuntu Linux

## Why "HALO"?

Named after AMD Strix **Halo** - the first APU with enough unified memory to run large diffusion models locally. This pack was created while debugging Z-Image on Strix Halo hardware.

## Credits

Created by **bkpaine1** & **Claude** (Anthropic)

*Heroes of the Unified Memory Revolution*

## License

MIT License - Use freely, attribution appreciated.

## Links

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [Report Issues](https://github.com/bkpaine1/halo_pack/issues)
