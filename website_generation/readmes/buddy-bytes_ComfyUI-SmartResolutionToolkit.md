# ComfyUI-SmartResolutionPicker

A lightweight yet powerful resolution assistant for ComfyUI.  
It allows you to **select image size using human-friendly dropdowns** instead of typing width and height manually.

Designed for:
✓ EmptyLatentImage  
✓ Video / TikTok / IG / Story formats  
✓ ControlNet / AnimateDiff / Sampler  
✓ Latent-safe (auto snap to 64)

---

## ✨ Features

🧠 Smart width & height calculation  
– Choose **Resolution Preset** (HD, FullHD, 2K, 4K, 8K)  
– Choose **Aspect Ratio** (1:1, 9:16, 4:5, 21:9 etc.)  
– Output: clean `width` and `height` (INT values)

⚙ Latent-safe scaling  
– Automatically snaps resolution to the nearest multiple of 64  
– 100% compatible with latent operations

🎯 Two Nodes Included

| Node | Description |
|------|-------------|
| Smart Resolution Picker | Returns width & height (INT) for image/latent initialization |
| Smart Latent Generator | Directly creates empty LATENT tensor from resolution + ratio |

---

## 📐 Available Resolution Presets

| Name | Size |
|------|------|
| SD | 512 × 512 |
| HD | 1280 × 720 |
| FullHD | 1920 × 1080 |
| 2K Cinema | 2048 × 1080 |
| QHD | 2560 × 1440 |
| 4K UHD | 3840 × 2160 |
| 8K UHD | 7680 × 4320 |

---

## 📸 Available Aspect Ratios

| Ratio | Common Usage |
|-------|--------------|
| 1:1 | Square / Album Cover |
| 4:5 | Instagram Portrait |
| 3:4 | Classic Portrait / Photography |
| 2:3 | DSLR Photo / Print |
| 5:4 | Medium Format |
| 9:16 | TikTok / Reel / Story |
| 16:9 | YouTube / Widescreen |
| 21:9 | Cinematic Ultra-wide |

---

## 🚀 SmartLatentGenerator Node  
Generates latent **directly**, no need for EmptyLatentImage.

```mermaid
flowchart LR
    A[SmartLatentGenerator] --> B[Sampler / KSampler]
