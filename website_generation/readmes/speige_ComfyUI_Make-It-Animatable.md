# ComfyUI_Make-It-Animatable: Auto-Rigging humanoid 3D meshes & guassian-splats

[![Original Repo](https://img.shields.io/badge/GitHub-Original_Repo-blue?logo=github)](https://github.com/jasongzy/Make-It-Animatable)
https://github.com/jasongzy/Make-It-Animatable

This repository wraps the original **Make-It-Animatable** repo into a **ComfyUI custom node**.

[![Project Page](https://img.shields.io/badge/Project-Page-green)](https://jasongzy.github.io/Make-It-Animatable/)
[![Paper](https://img.shields.io/badge/arXiv-2411.18197-b31b1b.svg)](https://arxiv.org/abs/2411.18197)
[![Demo (gradio version)](https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-Demo-orange)](https://huggingface.co/spaces/jasongzy/Make-It-Animatable)

![example](https://github.com/jasongzy/Make-It-Animatable/raw/main/assets/teaser.jpg)

### **Make-It-Animatable (Auto-Rig Mesh or Guassian-Splat)**

Converts an input 3D model into an animation-ready rigged **GLB** file in Mixamo bone format

### ComfyUI Wrapper

Exposes a single ComfyUI node, which automatically handles:

* Cloning the upstream repository
* Pinning known-working revisions
* Apply git patches for ComfyUI compatability
* Downloading pretrained models from HuggingFace
* Downloading Mixamo bone data
* Creating an isolated Python 3.11 virtual environment inside the node
* Running the Make-It-Animatable pipeline in a headless, Blender-based subprocess
* Converting FBX → GLB for ComfyUI compatibility

---

## 🔧 Installation

Place this folder into:

```
ComfyUI/custom_nodes/comfyui_make-it-animatable/
```

Then start ComfyUI. First node execution may take several minutes to do one-time setup.

---

## 🛠 Troubleshooting

### pip install errors

#### Enable long file paths in windows & restart PC
```powershell
Set-ItemProperty 'HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem' -Name 'LongPathsEnabled' -Value 1 -Type DWord; Write-Host "LongPathsEnabled set to 1. Reboot required."
```

#### Incorrect cuda version
The wrapped repo installs its own venv outside ComfyUI which needs to match your installed cuda toolkit version
```
nvcc --version
Modify \Make_It_Animatable\requirements.txt to match your environment
create a git patch file
save it to \ComfyUI_Make-It-Animatable\patches\01_requirements_txt.patch
```

### Blender errors

If Blender cannot import/export FBX/GLB, ensure your ComfyUI environment has Blender available in PATH.

### Missing pretrained models

Delete:

```
Make_It_Animatable/output/best/new/
```

Then restart ComfyUI to trigger a re-download.

### Missing Mixamo data

Delete:

```
Make_It_Animatable/data/Mixamo
```

Then restart ComfyUI to trigger a re-download.

### Virtual environment issues

Delete:

```
Make_It_Animatable/venv311/
```

Restart ComfyUI and it will recreate the venv.

[![Star History Chart](https://api.star-history.com/svg?repos=speige/ComfyUI_Make-It-Animatable&type=Date)](https://star-history.com/#speige/ComfyUI_Make-It-Animatable&Date)