# ComfyUI-Workarounds

A collection of practical and specialized nodes for ComfyUI, providing advanced face overlay, region masking, and scheduling solutions for various AI models.

[![GitHub stars](https://img.shields.io/github/stars/alisson-anjos/ComfyUI-Workarounds?style=social)](https://github.com/alisson-anjos/ComfyUI-Workarounds)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)

## 🌟 Features

- **Planar Face Overlay**: Fast face swapping with planar transforms only (no warping)
- **Face Region Options**: Flexible region masks for selective face part transfer
- **FlowMatch Scheduler**: Advanced scheduling for ai-toolkit models (Flux, Qwen, Z-Image-Turbo)
- **Color Matching**: LAB and mean-based color harmonization
- **JSON Diagnostics**: Detailed metrics and landmark data for automation

## 📦 Installation

### Via ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "ComfyUI-Workarounds"
3. Click Install and restart ComfyUI

### Manual Installation
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/alisson-anjos/ComfyUI-Workarounds.git
cd ComfyUI-Workarounds
pip install -r requirements.txt
# Restart ComfyUI
```

### Dependencies
- Python 3.10+
- OpenCV (`cv2`)
- NumPy
- MediaPipe
- SciPy
- PyTorch
- See `requirements.txt` for complete list

## 📚 Nodes Documentation

### 🎭 Face Overlay Nodes

#### WA_PlanarFaceOverlay
Overlays a source face onto a target body using only planar transforms (flip/mirror, rotation, translation, uniform scale). Perfect for fast face swapping without complex warping.

**Key Features:**
- ✨ Automatic orientation matching (mirror/flip) based on yaw heuristics
- 📐 Camera normalization aligning eye-line or nose-chin axis
- 🎯 Anchor-based alignment (nose tip, eye center, or bbox center)
- 🎨 Optional color matching (LAB or per-channel mean)
- 📊 JSON outputs for landmarks and metrics

**Inputs:**
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `source_face` | IMAGE | Face to transfer | Required |
| `target_body` | IMAGE | Destination image | Required |
| `auto_flip` | BOOLEAN | Auto mirror to match orientation | True |
| `align_rotation` | BOOLEAN | Align rotation to target | True |
| `pre_normalize_camera` | BOOLEAN | Pre-rotate source axis | True |
| `alignment_axis` | CHOICE | "nose" or "eyes" | "nose" |
| `anchor_point` | CHOICE | "nose_tip", "eye_center", "bbox_center" | "nose_tip" |
| `scale_method` | CHOICE | "interocular", "bbox_width", "bbox_height", "nose_to_chin" | "interocular" |
| `scale_adjust` | FLOAT | Fine-tune scale (0.5-2.0) | 1.0 |
| `offset_x/y` | INT | Manual pixel offsets | 0 |
| `feather` | INT | Gaussian blur radius | 8 |
| `mask_expand` | INT | Grow/shrink mask | 0 |
| `color_match` | BOOLEAN | Enable color matching | False |
| `color_match_method` | CHOICE | "lab" or "mean" | "lab" |
| `color_match_strength` | FLOAT | Blend strength (0-1) | 0.7 |

**Outputs:**
- `result` (IMAGE): Final composited image
- `face_mask` (MASK): Applied mask after transformation
- `debug_preview` (IMAGE): Debug visualization with metrics
- `src_landmarks_in_target_json` (STRING): Transformed landmarks JSON
- `metrics_json` (STRING): Detailed metrics and diagnostics

#### WA_FaceRegionOptions
Builds customizable region masks from landmark geometry. Control exactly which facial features to transfer.

**Presets:**
- `face_oval`: Standard facial oval (no forehead)
- `face_with_forehead`: Broader coverage including forehead
- `full_head`: Convex hull of all landmarks (widest coverage)
- `custom`: Mix and match individual regions

**Custom Region Options:**
- Face skin
- Forehead
- Eyebrows
- Eyes
- Nose
- Mouth

**Parameters:**
| Parameter | Type | Description | Default |
|-----------|------|-------------|---------|
| `image` | IMAGE | Source for landmarks | Required |
| `preset` | CHOICE | Region preset | "face_oval" |
| `expand` | INT | Morphology size | 0 |
| `feather` | INT | Edge feathering | 0 |

### ⚡ FlowMatch Scheduler Nodes (New!)

Advanced scheduling system compatible with ai-toolkit models, implementing flow matching ODE for modern diffusion models.

#### FlowMatchScheduler (Advanced)
Full control over all scheduling parameters for custom workflows.

**Features:**
- 🔄 Multiple scheduler types (linear, sigmoid, shift, exponential)
- 📏 Dynamic resolution-based shifting
- 📈 Bell curve timestep weighting
- 🎯 Terminal stretching for models like Qwen

**Scheduler Types:**
- `linear`: Standard linear distribution
- `sigmoid`: Concentrated in center (ai-toolkit style)
- `shift`: Linear time shift
- `shift_exponential`: Exponential shift (Qwen/Z-Image-Turbo)
- `flux_shift`: Flux-specific with doubled patch size
- `lognorm_blend`: Lognormal + linear blend
- `weighted`: Bell-shaped weighting

#### FlowMatchSchedulerPresets
Quick presets for popular models - no configuration needed!

**Available Presets:**
| Model | Steps | CFG | Shift Type | Terminal |
|-------|-------|-----|------------|----------|
| `flux_dev` | 20-50 | 3.5-7.0 | Linear | 0.0 |
| `flux_schnell` | 4-8 | 1.0 | Linear | 0.0 |
| `qwen_image` | 20 | 2.5 | Exponential | 0.02 |
| `z_image_turbo` | 20-30 | 2.0-3.0 | Exponential | 0.02 |
| `lumina` | 20-30 | 3.0-5.0 | Exponential | 0.0 |
| `hidream` | 20-30 | 3.5-7.0 | Linear | 0.0 |
| `stable_diffusion` | 20-50 | 7.0 | Linear | 0.0 |
| `mochi` | 20-30 | 3.5 | Linear + Inverted | 0.0 |

#### FlowMatchAutoConfig
Automatically outputs optimal sampling parameters for your model.

**Outputs:**
- Steps count
- CFG scale
- Denoise strength
- Recommended sampler name
- Scheduler type

#### FlowMatchGuide
Displays detailed recommendations and best practices for each model type.

## 🎨 Example Workflows

### Full Head Transfer with Color Match
```
1. WA_FaceRegionOptions
   ├─ image: source_face
   ├─ preset: "full_head"
   ├─ expand: 8
   └─ feather: 12
   
2. WA_PlanarFaceOverlay
   ├─ source_face: [same]
   ├─ target_body: [body_image]
   ├─ auto_flip: True
   ├─ alignment_axis: "nose"
   ├─ anchor_point: "nose_tip"
   ├─ scale_method: "nose_to_chin"
   ├─ use_region_mask: True
   ├─ region_mask: [from step 1]
   ├─ color_match: True
   ├─ color_match_method: "lab"
   └─ color_match_strength: 0.7
```

### Qwen Image Edit with FlowMatch
```
1. FlowMatchSchedulerPresets
   ├─ preset: "qwen_image"
   ├─ steps: 20
   └─ latent_image: [your_latent]
   
2. SamplerCustomAdvanced
   ├─ sigmas: [from scheduler]
   ├─ sampler: "euler"
   └─ cfg: 2.5
```

### Custom Face Parts Transfer
```
1. WA_FaceRegionOptions
   ├─ preset: "custom"
   ├─ include_eyes: True
   ├─ include_eyebrows: True
   └─ include_mouth: True
   
2. WA_PlanarFaceOverlay
   ├─ use_region_mask: True
   └─ region_mask: [from step 1]
```

## 🔧 Technical Details

### Face Overlay Algorithm
1. **Landmark Detection**: MediaPipe face mesh (478 points)
2. **Orientation Matching**: Yaw-based auto-flip with fallback to eye ordering
3. **Transform Calculation**: Planar only (rotation + scale + translation)
4. **Color Harmonization**: LAB space matching within masked region
5. **Composition**: Feathered mask blending

### FlowMatch Implementation
Based on ai-toolkit's `CustomFlowMatchEulerDiscreteScheduler`:
- **Flow ODE**: `x_t = (1-t)*x_0 + t*noise`
- **Dynamic Shift**: `mu = m * seq_len + b`
- **Bell Weighting**: `exp(-2 * ((x - n/2) / n)^2)`
- **Terminal Stretching**: Ensures final sigma reaches specified value

## 📊 JSON Output Examples

### Metrics JSON (Face Overlay)
```json
{
  "alignment_axis": "nose",
  "anchor_point": "nose_tip",
  "angle_deg": 12.3,
  "scale": 0.98,
  "flipped": true,
  "yaw_sign": {"source": 1, "target": 1},
  "anchor_src_xy": {"x": 123.0, "y": 210.5},
  "anchor_tgt_xy": {"x": 340.0, "y": 400.0},
  "applied_color_match": true,
  "color_match_method": "lab",
  "color_match_strength": 0.7,
  "applied_bbox_xyxy": [300, 250, 480, 520],
  "target_size_hw": {"h": 1024, "w": 768}
}
```

## ⚠️ Limitations

- **Face Overlay**: Planar transforms only - no perspective/3D warping
- **Landmark Dependency**: Quality relies on MediaPipe detection
- **Extreme Profiles**: May require manual flip adjustment
- **FlowMatch**: LogNormal distribution requires scipy

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [MediaPipe Face Mesh](https://google.github.io/mediapipe/) by Google
- [ai-toolkit](https://github.com/ostris/ai-toolkit) by Ostris
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) by comfyanonymous
- OpenCV and NumPy communities

## 👤 Author

**Alisson Anjos (NRDX)**
- GitHub: [@alisson-anjos](https://github.com/alisson-anjos)
- HuggingFace: [@Alissonerdx](https://huggingface.co/Alissonerdx)
- CivitAI: [NRDX](https://civitai.com/user/NRDX)
- LinkedIn: [/in/alissonpereiraa](https://www.linkedin.com/in/alissonpereiraa)

<a href="https://buymeacoffee.com/nrdx" target="_blank" style="display: inline-block; margin-bottom: 10px;">
                <img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&amp;emoji=&amp;slug=nrdx&amp;button_colour=FFDD00&amp;font_colour=000000&amp;font_family=Cookie&amp;outline_colour=000000&amp;coffee_colour=ffffff" alt="Buy Me A Coffee" height="40">
            </a>

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=alisson-anjos/ComfyUI-Workarounds&type=Date)](https://star-history.com/#alisson-anjos/ComfyUI-Workarounds&Date)


## 💬 Support

If you have any questions or issues:
1. Check the [Issues](https://github.com/alisson-anjos/ComfyUI-Workarounds/issues) page
2. Join the discussion in ComfyUI Discord
3. Create a new issue with detailed description

---

Made with ❤️ for the ComfyUI community