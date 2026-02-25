# ComfyUI I2I-Slim

A lightweight version of the custom nodes originally developed by [ManglerFTW](https://github.com/ManglerFTW/ComfyI2I) for performing image-to-image tasks in ComfyUI.

This slimmed-down version **removes the ComfyShop feature** and includes only the following core nodes:

---

## ✂️ Cut – Inpaint Segments

Segments and crops your image and mask based on the bounding boxes of each mask region. Each segment is then resized to 1024×1024 (or a custom size you define).

---

## 📌 Paste – Combine and Paste

Takes generated images (e.g. from the VAE Decode node), resizes them to match the original mask regions, and pastes them back into the original image at the correct location.

---

## 🧩 Segment – Mask Ops

Performs various operations on a mask, which can be created from an image or a text prompt. Includes options like blur, invert, levels adjustment, and region separation.

---

## 🎨 Color Transfer

Transfers the color palette of one image to another. Supports palette matching, blending, and optional luminance preservation.

---

## 🚀 Installation

1. Copy this folder into `ComfyUI/custom_nodes/`
2. Install the required packages:

   ```bash
   pip install -r requirements.txt
