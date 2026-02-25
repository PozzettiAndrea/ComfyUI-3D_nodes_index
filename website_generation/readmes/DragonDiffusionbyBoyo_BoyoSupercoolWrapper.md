# BoyoSupercoolWrapper

This is a ComfyUI wrapper for Andrew DalPino's SuperCool upscaler, enabling its use directly within ComfyUI's node workflow. No extra dependencies required—just drop in the models and go.

## 💡 What This Is

The original SuperCool repo ([https://github.com/andrewdalpino/SuperCool](https://github.com/andrewdalpino/SuperCool)) provides a fast and high-quality image upscaler. This wrapper integrates that functionality into ComfyUI using its native Python environment—no external pip installs needed.

All upscaling models are fixed at **4x** internally—despite the file naming for compatibility with ComfyUI conventions (see below).

---

## 🔄 Version 2.0 - Memory Optimised + Internal Batching

### New Features:
- **Memory Management**: Automatic model unloading and VRAM cleanup
- **Internal Batching**: Process large image sequences without external batching nodes
- **Mixed Precision**: Reduced VRAM usage with torch.autocast
- **Better Error Handling**: Comprehensive error reporting and recovery
- **Progress Feedback**: Visual progress for batch processing

### Memory Optimisation Controls:
- `unload_after_run`: Automatically unloads model after processing (default: True)
- `force_gc`: Forces garbage collection for thorough memory cleanup (default: True)
- `batch_size`: Process images in chunks to prevent OOM errors (default: 10)

### Perfect for Video Workflows:
No more complex batching setups! Process hundreds of video frames directly:
1. Load your video frames
2. Set appropriate batch size for your VRAM
3. The node handles everything automatically

**Credit**: Memory optimisations contributed by **Maelstrom2014** - cheers for making this production-ready!

---

## 🧱 Setup

### 1. Clone or install this repo into your ComfyUI custom nodes directory:

```
git clone https://github.com/DragonDiffusionbyBoyo/BoyoSupercoolWrapper
```

So it ends up like:

```
ComfyUI/custom_nodes/BoyoSupercoolWrapper/
```

### 2. Download the models

| Model Size              | Download Link                                                                                                        | Rename To     |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------- | ------------- |
| Small (fast)            | [https://huggingface.co/andrewdalpino/SuperCool-4x-Small](https://huggingface.co/andrewdalpino/SuperCool-4x-Small)   | supercool_2x |
| Medium                  | [https://huggingface.co/andrewdalpino/SuperCool-4x-Medium](https://huggingface.co/andrewdalpino/SuperCool-4x-Medium) | supercool_4x |
| Large (slow, high qual) | [https://huggingface.co/andrewdalpino/SuperCool-4x-Large](https://huggingface.co/andrewdalpino/SuperCool-4x-Large)   | supercool_8x |

**Note:** All models upscale by **4x**. The naming (`2x`, `4x`, `8x`) is just used for node dropdown compatibility—they do not reflect actual scale factors.

### 3. Put the renamed models here:

```
ComfyUI/models/upscale_models/SuperCool/
```

If the `SuperCool` folder does not exist, create it manually.

---

## ✅ Usage

### Basic Usage
Once everything is in place, launch ComfyUI and look for the **SuperCool Upscaler (Memory Optimised + Batching)** node under the `upscale` category. You can select from three quality/speed presets via dropdown.

### Memory Management Settings
- **Batch Size**: Start with 10, adjust based on your VRAM:
  - RTX 3060 (8GB): Try 5-8
  - RTX 4070/4080 (12-16GB): Try 10-15
  - RTX 4090 (24GB): Try 20-30+
- **Unload After Run**: Keep enabled to free VRAM for other nodes
- **Force GC**: Keep enabled for thorough memory cleanup

### Video Workflow Tips
1. **Interpolation First**: Use RIFE or similar interpolation nodes before upscaling
2. **Batch Appropriately**: Lower batch sizes if you're running other memory-intensive nodes
3. **Monitor Progress**: Watch the console for batch processing updates

---

## 🫼 No Extra Dependencies

This wrapper uses only ComfyUI's standard packages. No additional installations are required.

---

## 🐉 Credits & Contributors

**Original SuperCool**: [Andrew DalPino](https://github.com/andrewdalpino/SuperCool)  
**Memory Optimisations**: **Maelstrom2014** - massive thanks for the production-ready improvements!  
**Wrapper & Integration**: Dragon Diffusion UK

---

## 🐉 Made by Dragon Diffusion UK

Maintained by Dragon Diffusion UK: [https://www.dragondiffusionuk.co.uk](https://www.dragondiffusionuk.co.uk)
We build practical, bleeding-edge AI integrations for actual humans.

Pull requests, feedback, and banter welcome. 
PS please note I am a vibe coder so if you ask me something that is not on sport I will struggle haahahahah