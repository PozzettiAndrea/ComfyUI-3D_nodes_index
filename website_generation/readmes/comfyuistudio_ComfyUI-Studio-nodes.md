# 🎨 Aspect Ratio Nodes for ComfyUI

Smart nodes for calculating and resizing images to any aspect ratio.  
Supports manual size, auto 1MP sizing, crop/stretch, and horizontal/vertical orientation.

## 💡 Usage Examples

**Default 1MP:**  
```
width=0, height=0, aspect_ratio="16:9" → ~1333x750
```

**Width-Based:**  
```
width=1920, height=0, aspect_ratio="16:9" → 1920x1080
```

**Manual Override:**  
```
width=1920, height=1200, aspect_ratio="16:9" → 1920x1200
```

**Vertical Orientation:**  
```
width=0, height=0, aspect_ratio="16:9", direction="Vertical" → ~750x1333
```

---

# 🔧 Git Clone Manager

Manage and clone GitHub, HuggingFace, or any Git repositories with ease.  
Supports custom paths, branches, submodules, and authentication tokens.

## ⚡ Key Features

- Clone Repos Anywhere: GitHub → custom_nodes/, HF → models/, or custom paths
- Advanced Git Ops: Branch selection, shallow clones, submodules, force update
- Auth Support: HuggingFace & GitHub tokens with automatic URL handling
- Professional Tools: Concurrent cloning, progress tracking, repo history, size calculation, interrupts
- Repo Info: Current branch, last commit, remote URL, clone date, total size

## 📝 Usage Examples

**Clone nodes:**  
https://github.com/ltdrdata/ComfyUI-Manager  
https://github.com/WASasquatch/was-node-suite-comfyui

**Clone models with custom paths:**  
https://huggingface.co/runwayml/stable-diffusion-v1-5 models/sd15

**Clone specific branches:**  
branch:main https://github.com/user/experimental-node

**Mixed operations:**  
https://github.com/comfyanonymous/ComfyUI-3D-Pack  
https://huggingface.co/facebook/bart-large models/bart

## 🚀 Advantages

- Easy Git-based workflow for nodes & models
- Clean interface with full repo awareness
- Fast batch cloning with detailed progress & history
- Interrupt-safe and professional-grade Git handling

Perfect for managing ComfyUI nodes, models, and any Git workflow without hassle.

---

# 🤖 HuggingFace Downloader Node

Custom ComfyUI node for downloading HuggingFace models efficiently.

## ⚡ Features

- Multi-line input for multiple links
- Flexible formats: url folder filename or url folder
- Skips existing files automatically
- Shows download progress and file sizes
- Error handling with reports
- Threaded downloads for speed
- Optional auto-download toggle

## 📝 Usage Example
https://huggingface.co/path/to/model.safetensors unet model_name.safetensors
https://huggingface.co/path/to/vae.safetensors vae
https://huggingface.co/path/to/checkpoint.ckpt checkpoints my_checkpoint.ckpt
