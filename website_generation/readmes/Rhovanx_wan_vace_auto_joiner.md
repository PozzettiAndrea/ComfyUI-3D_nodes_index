# WAN VACE Auto Joiner v2.0.0 (ComfyUI Custom Nodes)

Seamlessly join multiple video clips in a folder using **WAN VACE** and **ComfyUI Easy-Use For Loop** automation — with **one-click solution**.

This node set ensures:

* VACE runs **exactly N-1 times** for **N input videos**
* **Seamless transitions** with automatic color/brightness correction
* **Audio preservation** from original clips
* Finalization runs **once**, after the loop completes

Nodes appear under: **WAN VACE / Auto Joiner**

---

## 🆕 What's New in v2.0.0

### Seamless Transitions
VACE can introduce brightness/color shifts at transition boundaries. v2.0.0 automatically corrects this with:

- **Temporal Color Smoothing** — Gaussian + linear interpolation across transition regions
- **Per-Channel Correction** — Independent R, G, B adjustment for accurate color matching
- **Dynamic Calculation** — All correction values computed from your actual source frames (no hardcoded values)

### Audio Support
- **Automatic Audio Transfer** — Extracts and concatenates audio from all source clips
- **Direct Video Combine Integration** — Standard ComfyUI `AUDIO` output connects directly to VHS Video Combine
- **Fail-Safe Handling** — Generates silent audio track when source clips have no audio (prevents workflow errors)

---

## Key Features

| Feature | Description |
|---------|-------------|
| ✅ One-click batch joining | Process unlimited video clips automatically |
| ✅ Seamless transitions | No visible brightness/color jumps between clips |
| ✅ Audio preservation | Original audio transferred to final output |
| ✅ Loop barrier system | Prevents early exit & race conditions |
| ✅ Clean lifecycle | INIT → PROCESS → FINALIZE |
| ✅ Security | Input sanitization prevents path traversal |

---

## Requirements

| Requirement | Notes |
|-------------|-------|
| **ComfyUI** | Base requirement |
| **ComfyUI-Easy-Use** | Required for For Loop nodes |
| **WAN VACE workflow** | Your existing VACE setup |
| **ffmpeg** | Required for audio features (optional) |
| **scipy** | Recommended for best smoothing (optional, has numpy fallback) |

---

## Installation

### Option 1 — ComfyUI-Manager (Recommended)

1. Open **ComfyUI → Manager**
2. Go to **Install Custom Nodes**
3. Search for **Wan Vace Auto Joiner**
4. Install and restart ComfyUI

### Option 2 — Manual Install

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/Rhovanx/wan_vace_auto_joiner.git
```

Restart ComfyUI.

### Optional Dependencies

```bash
# For best color smoothing results
pip install scipy

# For audio features (check if already installed)
ffmpeg -version
```

---

## The Three Nodes

| Node | Display Name | Location | Purpose |
|------|--------------|----------|---------|
| `WanVaceAutoJoiner` | WAN VACE Auto Joiner | Inside loop | INIT (first iteration) / PROCESS (subsequent) |
| `WanVaceAutoJoinerSave` | WAN VACE Auto Joiner – Save | Inside loop | Saves VACE output, acts as loop barrier |
| `WanVaceAutoJoinerFinalize` | WAN VACE Auto Joiner – Finalize | After loop | Applies smoothing, outputs frames + audio |

---

## Finalize Node Options (v2.0.0)

| Option | Default | Description |
|--------|---------|-------------|
| `smooth_transitions` | ✅ True | Enable temporal color smoothing |
| `smooth_window` | 12 | Gaussian sigma (1-30, higher = smoother) |
| `blend_region` | 25 | Context frames before/after VACE (10-50) |
| `transfer_audio` | ✅ True | Extract audio from source clips |
| `cleanup` | ❌ False | Delete temp folder after completion |

---

## Output Connections

```
WAN VACE Auto Joiner - Finalize
├── batch_images ────→ Video Combine (images)
├── audio ───────────→ Video Combine (audio)
├── frame_rate ──────→ Video Combine (frame_rate)
├── status ──────────→ (optional debug output)
└── is_complete ─────→ (optional boolean flag)
```

---

## Workflow Setup

### 1️⃣ Prepare Input Directory

Clips must follow this naming format:

```
clip_00001.mp4
clip_00002.mp4
clip_00003.mp4
...
```

The prefix (`clip`) is configurable in the Auto Joiner node.

### 2️⃣ Set Loop Count

For **N videos**, set:

```
For Loop Start → total = N - 1
```

| Videos | Loop Total |
|--------|------------|
| 3 | 2 |
| 4 | 3 |
| 5 | 4 |
| 10 | 9 |

### 3️⃣ Connect the Nodes

```
For Loop Start ─────────────► For Loop End (flow)
        │
        ├── value1 ─► Save ─► initial_value1
        │
        └── index ─► Auto Joiner
                           │
                           ▼
                      WAN VACE
                           │
                       VAE Decode
                           │
                           └──► Save

After loop:
For Loop End (value1) ─────► Finalize ─────► Video Combine
                                  │              │
                                  └── audio ─────┘
```

### 4️⃣ Run Once

Queue the workflow **one time** — the loop handles everything automatically.

---

## How Transition Smoothing Works

### The Problem
VACE processes 33 frames per transition (16 from clip A + 17 from clip B). The diffusion process can shift brightness and color temperature, creating visible "pulses" at transition points.

### The Solution
v2.0.0 applies **temporal color smoothing**:

1. **Analyzes** brightness and R/G/B values across the transition region
2. **Creates smooth target curves** using Gaussian smoothing + linear interpolation
3. **Calculates per-frame correction factors** dynamically from your source material
4. **Applies corrections** to eliminate visible jumps

**Before:** Transitions show +3-6 point brightness jumps  
**After:** Transitions show <1 point variation (imperceptible)

---

## Audio Handling

| Scenario | Behavior |
|----------|----------|
| All clips have audio | Audio extracted and concatenated |
| Some clips have audio | Available audio extracted |
| No clips have audio | Silent track generated |
| ffmpeg not installed | Silent track generated |
| `transfer_audio` = False | Silent track generated |

The audio output is **always valid** — you can permanently connect it to Video Combine without workflow errors.

---

## Troubleshooting

### Transitions still visible
- Increase `smooth_window` (try 15-20)
- Increase `blend_region` (try 30-40)
- Ensure `smooth_transitions` is enabled

### No audio in output
- Check if source clips have audio tracks
- Verify ffmpeg is installed: `ffmpeg -version`
- Check console for `[WAN VACE Auto Joiner]` messages

### Loop exits early
- Ensure `value1` passes through the Save node
- Do not use FLOW_CONTROL for the barrier

### Finalize runs too early
- Confirm Finalize is connected after For Loop End
- Do not place Finalize inside the loop

---

## FAQ

**Why temporal smoothing?**  
VACE's diffusion process modifies all 33 frames, not just the masked region. This creates color/brightness inconsistencies that are visible to the human eye. Smoothing corrects these artifacts automatically.

**Are the correction values hardcoded?**  
No. All correction factors are calculated dynamically from your actual source frames at runtime. The algorithm adapts to any video content.

**Why not FLOW_CONTROL?**  
FLOW_CONTROL does not block asynchronous WAN VACE execution. The `value1` barrier enforces true dependency completion.

**Can I disable smoothing?**  
Yes, set `smooth_transitions` to False in the Finalize node. You'll get the raw VACE output.

**What if scipy isn't installed?**  
The code falls back to a numpy-based Gaussian filter. Results are similar but scipy is slightly more accurate.

---

## Changelog

### v2.0.0 (Major Release)
- ✨ **NEW:** Temporal color smoothing for seamless transitions
- ✨ **NEW:** Per-channel (R, G, B) correction
- ✨ **NEW:** Audio transfer from original clips
- ✨ **NEW:** Standard ComfyUI AUDIO output
- ✨ **NEW:** Fail-safe silent audio generation
- 🔒 Input sanitization for security
- 📦 Dynamic correction (no hardcoded values)

### v1.0.0
- Initial release
- Three-node system (Auto Joiner, Save, Finalize)
- Loop barrier mechanism
- Zero VACE overhead design

---

## License

MIT

---

## Credits

- **WAN VACE** — Alibaba's video-to-video consistency model
- **ComfyUI-Easy-Use** — For Loop implementation
- **ComfyUI-VideoHelperSuite** — Video Combine node compatibility
