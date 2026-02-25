# 📄 ComfyUI Document Auto Crop Node

This custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) automatically crops a document by detecting edges, rotates it based on face orientation using MediaPipe, and adjusts it to a target aspect ratio (default 11:14).

---

## ✨ Features
- Document edge detection and perspective warp
- Face-aware rotation (0/90/180/270°)
- Cropping to target aspect ratio
- Lossless output with color preservation

---

## 📦 Installation

```bash
git clone https://github.com/yourname/comfyui-document-auto-crop.git
cp -r comfyui-document-auto-crop ComfyUI/custom_nodes/
pip install -r ComfyUI/custom_nodes/comfyui-document-auto-crop/requirements.txt
```

---

## 🧠 Usage in ComfyUI

Search for node:
```
📄 Document Auto Crop + Rotate + Ratio
```

### Input
- `image`: Image input from ComfyUI
- `target_ratio`: Desired width/height ratio (e.g., 11/14)

### Output
- `processed_image`: Result image after crop, rotation, and aspect adjustment

---

## 📝 License
[MIT](LICENSE)
