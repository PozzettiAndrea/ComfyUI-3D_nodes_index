# ComfyUI-Zero2JSON

**ZeroPrompt Integration for FLUX2-JSON** - Position-as-seed procedural text generation for structured prompt building.

## Overview

Zero2JSON provides shadow nodes that augment the FLUX2-JSON system with deterministic, profile-based procedural text generation. Each FLUX2-JSON input field receives a parallel ZeroPrompt node designed to generate contextually appropriate text.

**Core Philosophy:** Not replace, but augment and extend - providing unparalleled precision in multi-dimensional orchestration of procedural prompt inputs with guardrails in the form of user curation.

## Installation

1. Clone or copy this folder to your ComfyUI `custom_nodes` directory
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```
3. Restart ComfyUI

## Node Categories

### Subject Nodes (Zero2JSON/Subject)
- 🎯 **Z2J Subject Description** - Generate detailed subject descriptions
- 📍 **Z2J Subject Position** - Generate spatial positioning
- 🏃 **Z2J Subject Action** - Generate dynamic actions
- 🧘 **Z2J Subject Pose** - Generate static poses

### Scene Nodes (Zero2JSON/Scene)
- 🌍 **Z2J Scene** - Generate scene/environment descriptions
- 🖼️ **Z2J Background** - Generate background descriptions

### Style Nodes (Zero2JSON/Style)
- 🎨 **Z2J Style** - Generate artistic style descriptions
- 😊 **Z2J Mood** - Generate mood/atmosphere descriptions

### Lighting Nodes (Zero2JSON/Lighting)
- 💡 **Z2J Lighting** - Generate lighting setup descriptions

### Camera Nodes (Zero2JSON/Camera)
- 📐 **Z2J Camera Angle** - Generate camera angle descriptions
- 📏 **Z2J Camera Distance** - Generate shot framing descriptions
- 🔍 **Z2J Camera DoF** - Generate depth of field descriptions
- 🎯 **Z2J Camera Focus** - Generate focus target descriptions

### Composition Nodes (Zero2JSON/Composition)
- 📐 **Z2J Composition** - Generate composition rule descriptions

### Utility Nodes (Zero2JSON/Utility)
- ℹ️ **Z2J Profile Info** - Display profile statistics
- 📦 **Z2J Batch Generator** - Generate multiple prompts
- 🔀 **Z2J Seed Mixer** - Combine multiple seeds

## Common Inputs

All generation nodes share these inputs:

| Input | Type | Description |
|-------|------|-------------|
| `seed` | INT | World seed for deterministic generation (0 - 4294967295) |
| `prompt_index` | INT | Position in infinite prompt space (0 - 4294967295) |
| `profile` | DROPDOWN | Select vocabulary profile |
| `prefix` | STRING | Text to prepend to generated prompt |
| `suffix` | STRING | Text to append to generated prompt |

## Profile System

Profiles are JSON files in the `profiles/` directory that define vocabulary and templates:

```json
{
  "name": "Profile Name",
  "description": "What this profile generates",
  "version": "1.0.0",

  "templates": [
    "Template with {pool_a} and {pool_b}",
    "Another template: {pool_a}, {pool_b}"
  ],

  "pools": {
    "pool_a": ["option1", "option2", "option3"],
    "pool_b": ["choice1", "choice2", "choice3"]
  }
}
```

### Default Profiles

| Profile | Node | Combinations |
|---------|------|--------------|
| `subject_description_default.json` | Z2J_SubjectDescription | ~31M |
| `subject_position_default.json` | Z2J_SubjectPosition | ~7K |
| `subject_action_default.json` | Z2J_SubjectAction | ~11K |
| `subject_pose_default.json` | Z2J_SubjectPose | ~27K |
| `scene_default.json` | Z2J_Scene | ~32K |
| `background_default.json` | Z2J_Background | ~5K |
| `style_default.json` | Z2J_Style | ~19K |
| `mood_default.json` | Z2J_Mood | ~41K |
| `lighting_default.json` | Z2J_Lighting | ~91K |
| `composition_default.json` | Z2J_Composition | ~5K |
| `camera_angle_default.json` | Z2J_CameraAngle | ~8K |
| `camera_distance_default.json` | Z2J_CameraDistance | ~972 |
| `camera_dof_default.json` | Z2J_CameraDoF | ~7K |
| `camera_focus_default.json` | Z2J_CameraFocus | ~3K |

## Workflow Integration

Connect Zero2JSON nodes to FLUX2-JSON inputs:

```
[Z2J_SubjectDescription] → [FLUX2_SubjectCreator].description
[Z2J_SubjectPosition]    → [FLUX2_SubjectCreator].position
[Z2J_SubjectAction]      → [FLUX2_SubjectCreator].action
[Z2J_Scene]              → [FLUX2_PromptAssembler].scene
[Z2J_Style]              → [FLUX2_StyleSelector].custom_style
[Z2J_Lighting]           → [FLUX2_PromptAssembler].lighting
[Z2J_CameraAngle]        → [FLUX2_CameraRig].angle
...
```

## Determinism Guarantee

For any fixed `(seed, prompt_index, profile)`:
- Same hash values are always computed
- Same template is always selected
- Same components are always chosen
- Same output is always generated

This holds across different machines, Python versions (3.7+), operating systems, and execution times.

## Creating Custom Profiles

1. Copy an existing profile from `profiles/`
2. Rename with appropriate prefix (e.g., `subject_description_fantasy.json`)
3. Modify templates and pools for your use case
4. The node will automatically discover the new profile

### Profile Naming Convention

Profiles should follow the naming pattern: `{category}_{name}.json`

- `subject_description_*.json` - Subject description nodes
- `subject_position_*.json` - Subject position nodes
- `scene_*.json` - Scene nodes
- `style_*.json` - Style nodes
- `lighting_*.json` - Lighting nodes
- `camera_angle_*.json` - Camera angle nodes
- etc.

## Technical Details

### Hash Function

Uses xxhash32 for O(1) deterministic hashing:
```
prompt_hash(seed, prompt_idx, component_idx) → uint32
```

### Combination Calculation

```
total = len(templates) × Π(len(pool_i))
```

For example, a profile with 5 templates and 4 pools of sizes [10, 20, 15, 8] would have:
```
5 × 10 × 20 × 15 × 8 = 120,000 unique combinations
```

## License

MIT License

## Credits

- Based on DJZ_ZeroPrompt methodology
- Designed for integration with ComfyUI-FLUX2-JSON

## 📚 Citation

### Academic Citation

If you use this codebase in your research or project, please cite:

```bibtex
@software{comfyui_zero2json,
  title = {ComfyUI-Zero2JSON: ZeroPrompt Integration for FLUX2-JSON},
  author = {Drift Johnson},
  year = {2025},
  url = {https://github.com/MushroomFleet/ComfyUI-Zero2JSON},
  version = {1.0.0}
}
```

### Donate:

[![Ko-Fi](https://cdn.ko-fi.com/cdn/kofi3.png?v=3)](https://ko-fi.com/driftjohnson)
