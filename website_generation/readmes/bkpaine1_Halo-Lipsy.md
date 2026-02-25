# Halo-Lipsy

**Native AMD Unified Memory Lip Sync for ComfyUI**

Finally, lip sync that actually works on AMD APUs with unified memory. No subprocess hacks, no ghost files, no venv escapes.

Created by **Brent & Claude Code** (Anthropic Claude Opus 4.5)

---

## Why This Exists

Other lip sync nodes fail on AMD unified memory systems because they:
- Use `subprocess.run()` which escapes the venv → library mismatches → crash
- Write 0-byte "ghost files" that OpenCV can't read
- Try to cast `vfloat16` tensors directly to NumPy → unified memory conflict
- Auto-detect CUDA and fail when they don't find NVIDIA drivers

**Halo-Lipsy fixes all of this:**
- All inference runs natively in the ComfyUI process
- Face detection forced to CPU (fast enough, no memory fighting)
- Wav2Lip on GPU - ROCm translates CUDA calls
- Safe tensor casting: always `.float().cpu().numpy()`
- Returns tensors directly, no temp files

---

## Installation

### Via ComfyUI Manager (Recommended)
Search for "Halo-Lipsy" in ComfyUI Manager and click Install.

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/YOUR_USERNAME/Halo-Lipsy.git
cd Halo-Lipsy
pip install -r requirements.txt
```

### Download the Model
Download `wav2lip_gan.pth` from the [original Wav2Lip repo](https://github.com/Rudrabha/Wav2Lip):

**Direct link:** [wav2lip_gan.pth](https://iiitaphyd-my.sharepoint.com/:u:/g/personal/radrabha_m_research_iiit_ac_in/Eb3LEzbfuKlJiR600lQWRxgBIY27JZg80f7V9jtMfbNDaQ?e=TBFBVW)

Place it in:
- `Halo-Lipsy/checkpoints/wav2lip_gan.pth` (recommended)
- OR `ComfyUI/models/wav2lip/wav2lip_gan.pth`

---

## Usage

1. Find **"Halo-Lipsy"** in the node menu (category: `Halo-Lipsy`)
2. Connect your video frames to `images` input
3. Connect your audio to `audio` input
4. Output goes to VHS Video Combine or any IMAGE consumer

---

## Settings

### Core
| Setting | Default | Description |
|---------|---------|-------------|
| `checkpoint` | auto | Wav2Lip model path (auto-detects) |
| `mode` | sequential | `sequential` = frames match audio order, `repetitive` = loops frames |

### Performance
| Setting | Default | Description |
|---------|---------|-------------|
| `face_detect_batch` | 4 | Batch size for face detection (CPU) |
| `inference_batch` | 64 | Batch size for Wav2Lip (GPU) |
| `force_cpu` | False | Run everything on CPU (slower, zero VRAM) |

### Sync Tuning
| Setting | Default | Description |
|---------|---------|-------------|
| `sync_offset` | 0 | Shift audio ±10 frames. Negative = audio earlier |
| `mel_step_multiplier` | 1.0 | Mouth speed. <1 = slower, >1 = faster |

### Quality
| Setting | Default | Description |
|---------|---------|-------------|
| `face_padding` | 10 | Extra pixels around face |
| `smooth_box_frames` | 5 | Smooth face tracking over N frames |
| `blend_edges` | True | Feather face edges for cleaner composite |
| `blend_radius` | 5 | Edge blend softness (pixels) |

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Lips behind audio | `sync_offset` = -2 or -3 |
| Lips ahead of audio | `sync_offset` = +2 or +3 |
| Mouth too slow | `mel_step_multiplier` = 1.1 |
| Mouth too fast | `mel_step_multiplier` = 0.9 |
| Face box jitters | Increase `smooth_box_frames` |
| Hard edges | Enable `blend_edges`, increase `blend_radius` |
| Out of VRAM | Lower `inference_batch` or enable `force_cpu` |

---

## Tested On

- **Ryzen AI Max+ 395 (Strix Halo)** - 128GB unified memory split 64/64 ram/vram
- **ROCm 7.11**
- **ComfyUI** with HunyuanVideo loaded (15GB+)

Should work on any AMD APU/GPU with ROCm, and NVIDIA too.

---

## Credits

- **Brent** - Testing, bug hunting, AMD hardware
- **Claude Code** (Anthropic Claude Opus 4.5) - Architecture, implementation
- **Wav2Lip** - Original model by [Rudrabha Mukhopadhyay](https://github.com/Rudrabha/Wav2Lip)

---

## License

MIT License - Do whatever you want, just don't blame us if it breaks.

---

*"We fixed what NVIDIA-centric code broke."*
