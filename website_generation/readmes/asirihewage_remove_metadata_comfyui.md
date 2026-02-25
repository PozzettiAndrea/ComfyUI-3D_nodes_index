# 🧹 Remove Metadata for ComfyUI
![Version](https://img.shields.io/github/v/release/asirihewage/remove_metadata_comfyui)
![ComfyUI](https://img.shields.io/badge/ComfyUI-Compatible-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

A lightweight **custom ComfyUI node** that removes all metadata from images (EXIF, PNG text chunks, AI generation info) while keeping the image visually **unchanged**.

Perfect for:

* Cleaning AI-generated images
* Privacy‑focused workflows
* Preparing images for upload, sharing, or datasets
* Avoiding unwanted metadata leaks

---

## ✨ Features

* ✅ Removes EXIF metadata (camera, software, GPS, etc.)
* ✅ Strips PNG `tEXt`, `iTXt`, and `zTXt` chunks
* ✅ Removes AI generation comments
* ✅ Works with **batch images**
* ✅ No visible quality loss
* ✅ Fully offline & local

---

## 📂 Installation

1. Navigate to your ComfyUI installation:

```bash
cd ComfyUI/custom_nodes
```

2. Clone or create the node folder:

```bash
git clone https://github.com/yourname/remove-metadata-comfyui.git
```

3. Restart **ComfyUI**

---

## 🧩 Node Location

After restart, find the node at:

```
Image → Utils → Remove Image Metadata
```

---

## 🔌 Usage

Basic workflow:

```
Load Image
   ↓
Remove Image Metadata
   ↓
Save Image
```

* Input: `IMAGE`
* Output: `IMAGE` (cleaned, metadata‑free)

The output image will look **identical**, but all metadata is removed.

---

## 🧠 How It Works

* Converts ComfyUI image tensors to PIL images
* Re‑encodes images without metadata
* Returns clean tensors back to ComfyUI

No pixel manipulation, only metadata sanitization.

---

## ⚠️ Notes

* Color profile (ICC) is currently removed
* PNG output format is used internally
* Original filename metadata is not preserved

---

## 🚀 Planned Enhancements

* 🔘 Toggle: keep/remove ICC color profile
* 🗂 Batch filename suffix (`_clean`)
* 📸 JPEG / PNG format selector
* 🛰 Optional GPS spoof node (separate module)
* 🛡 Extra‑stealth recompression mode

---

## 📊 Compatibility Table

| Environment              | Supported | Notes                                     |
| ------------------------ | --------- | ----------------------------------------- |
| ComfyUI (source install) | ✅ Yes     | Fully supported                           |
| ComfyUI Windows Portable | ✅ Yes     | No venv required                          |
| ComfyUI Linux Portable   | ✅ Yes     | FFmpeg must be system-installed for video |
| ComfyUI Manager          | ✅ Yes     | Installable via `comfyui_node.yaml`       |
| Docker-based ComfyUI     | ✅ Yes     | Ensure FFmpeg available for video         |

---

## 🎞️ Supported Formats

### 🖼️ Images

| Format | Support Level | Notes                                               |
| ------ | ------------- | --------------------------------------------------- |
| PNG    | ✅ Full        | Lossless, pixel-identical                           |
| JPG    | ✅ Full        | One safe recompression (normal)                     |
| JPEG   | ✅ Full        | Same as JPG                                         |
| WEBP   | 🟡 Partial    | Metadata removal works, not recommended for stealth |
| TIFF   | 🟡 Partial    | Behavior varies by Pillow build                     |

### 🎥 Videos

| Format              | Support Level     | Notes                                  |
| ------------------- | ----------------- | -------------------------------------- |
| MP4 (H.264 / H.265) | ✅ Full            | No re-encode, stream copy              |
| MOV                 | ✅ Full            | Apple-safe remux                       |
| MKV                 | 🟡 Partial        | Some container headers remain (normal) |
| AVI / WMV / FLV     | ❌ Not Recommended | Metadata handling unreliable           |

---

## 🛡️ Stealth Guarantees by Format

| Format     | Pixel / Stream Integrity | Metadata Removed       |
| ---------- | ------------------------ | ---------------------- |
| PNG        | Pixel-identical          | AI / Media / Privacy   |
| JPG / JPEG | Visually identical       | AI / Media / Privacy   |
| MP4 / MOV  | Bitstream identical      | AI / Media / Privacy   |
| MKV        | Stream identical         | Partial container tags |

---

## 📜 License

MIT License – free to use, modify, and distribute.

---

## 🙌 Credits

Built for the **ComfyUI** ecosystem.

If you find this useful, feel free to ⭐ the repo and contribute!

---

## 📬 Support / Contributions

PRs, issues, and feature requests are welcome.

Happy generating 🧠✨
