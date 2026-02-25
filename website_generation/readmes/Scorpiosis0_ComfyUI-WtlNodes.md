# 🧩 My ComfyUI Custom Node Pack

![ComfyUI](https://img.shields.io/badge/ComfyUI-Custom%20Nodes-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10%2B-yellow?style=for-the-badge)
![Stable Diffusion](https://img.shields.io/badge/Stable%20Diffusion-Compatible-green?style=for-the-badge)

---

## 📌 Overview

This repository contains a collection of **custom nodes for ComfyUI**, designed to simplify workflows and add new creative / utility features and genral QOL improvements.  

---

## 🎯 Features

- Easy plug-and-play installation  
- Organized node categories  
- Clear controllable parameters  
- Designed for efficiency and expanded capability  

---

## 📥 Installation

### **Option 1 — Git Clone (Recommended)**

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/Scorpiosis0/ComfyUI-WtlNodes.git
```

### **Option 2 — Manual Install**

1. Click Code → Download ZIP
2. Extract into:
```bash
ComfyUI/custom_nodes/YourNodePack/
```

## ⭐ Custom Nodes Overview
A complete list of all custom nodes included in this pack.  
Use the summary table below to quickly jump to any node’s documentation.

---

## 📚 Summary Table
| Node Name | Short Description | Link |
|---|---|---|
| Saturation (HSV) | [Jump to Section](#saturation-hsv) |
| Dual Ease Cosine Scheduler | [Jump to Section](#dual-ease-cosine-scheduler) |
| Empty Latent (Advanced) | [Jump to Section](#empty-latent-advanced) |
| Depth of Field (DOF) | [Jump to Section](#depth-of-field-dof) |
---

## 🧩 Node Documentation

### Saturation (HSV)
*This node allows you to tweak image saturation through a live preview.*

**Settings:**
| Setting Name | Description |
|-------------|-------------|
| saturation | Controls how many steps will be made. |
| apply_type | Controls how to handle batches. |
| Apply Effect | This button applies the effect of saturation. |
| Skip Effect | This button skips the effect of saturation. |

### Dual Ease Cosine Scheduler
*This node is a custom scheduler I made that needs further testing. It's been tested using FID (Fréchet Inception Distance) along ablation to find the rough best default values.*

**Settings:**
| Setting Name | Description |
|-------------|-------------|
| steps | Controls how many steps will be made. |
| sigma_max | Controls the maximum sigma (max noise). |
| min_sigma | Controls the minimum sigma (min noise). |
| rho_start | Controls the strenght of the easing curve at the top. |
| rho_end | Controls the strenght of the easing curve at the bottom. |

**Recomended Usage:**

You can reduce the sigma_min value but I wouldn't recommend changing sigma_max setting.

### Empty Latent (Advanced)
*This node will offer easy ratio selection along a plethora of resolutions, portrait and landscape mode, with still a manual mode.*

**Settings:**
| Setting Name | Description |
|-------------|-------------|
| use_ratio | Enables you to switch between Ratio Mode and Manual Mode. |
| portrait_landscape | Enables you to switch between Portrait and Landscape while in ratio mode, thus inverting x and y values. |
| ratio | Allows you to select a ratio from a predefined list. |
| resolution | Allows you to select a resolution from a predefined list based on the ratio. All resolutions are multiples of 64 to avoid generation artifacts. |
| width & height | Allows you to select the x and y resolution of the image manually. |
| batch | Allows you to select the amount of created latent in one run. |

### Depth of Field (DOF)
*This node uses a depth map that you can make via any depth map model to apply a depth blur effect with a real time preview.*

**Settings:**
| Setting Name | Description |
|-------------|-------------|
| focus_depth | Enables you to set the focus point in the depth map, where 0 is the background and 1 the foreground. |
| blur_strenght | Allows you to apply more or less blur on the depth that isn't in focus. |
| focus_range | Allows you to choose the range/fall-off from the focus point to enlarge the focus range. |
| edge_fix | On some depth models you might want to set this setting at a recomended value of 3 to remove sharp balck edges of foreground objects, when foreground objects are not the main focus, but midground/background objects. |
| Apply Effect | This button applies the effect of blur. |
| Skip Effect | This button skips the effect of blur. |

**Recomended Usage:**

Use Depth Anything V2 or DepthPro for best results, Depth pro is the best for characters but struggles with backgrounds.

# Notes 🗒️:

- All good.
