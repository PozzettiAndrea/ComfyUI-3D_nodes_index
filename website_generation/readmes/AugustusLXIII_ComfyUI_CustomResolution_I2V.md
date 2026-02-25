<img width="813" height="612" alt="image" src="https://github.com/user-attachments/assets/f5f1d4d2-de37-440c-bf14-39a7a5da8061" />

# ComfyUI Custom Resolution I2V (v1.1)

A specialized resolution utility node for **WanVideo Image-to-Video (I2V)** workflows. This node provides standard resolution presets while offering a manual override system with automatic compatibility rounding.

---

## ✨ What's New in v1.1
- **Expanded Aspect Ratios:** Now supports **16:9** and **9:16** specifically for cinematic and mobile formats.
- **Variable Framerates:** Choose between **16, 24, or 30 fps** to suit different motion styles.
- **Simplified Manual Override:** Removed manual rounding selection; the node now automatically rounds dimensions to the nearest multiple of 8 for maximum encoder compatibility.
- **Improved UI:** Updated tooltips and display names for better clarity within the ComfyUI interface.

---

## 🛠 Installation

### Option 1: Via ComfyUI Manager (Recommended)
1. Search for `Custom Resolution I2V` in the ComfyUI Manager.
2. Click **Install**.
3. Restart ComfyUI.

### Option 2: Manual Installation (Git)
1. Open a terminal in your `ComfyUI/custom_nodes/` folder.
2. Run the following command:
   ```bash
   git clone [https://github.com/AugustusLXIII/ComfyUI_CustomResolution_I2V.git](https://github.com/AugustusLXIII/ComfyUI_CustomResolution_I2V.git)
3. Restart ComfyUI.
---

## 🚀 How to Use

### 1. Aspect Ratio
Choose between:
* **Portrait (2:3 or 9:16)**
* **Landscape (3:2 or 16:9)**
* **Square**

### 2. Resolution Level
Select a preset tier (**k18 to k55**). These are optimized according to the WanVideo specification. The node automatically calculates the correct width and height based on your chosen aspect ratio.

### 3. Manual Override
* **Enabled:** The node uses `manual_width` and `manual_height`.
* **Automatic Rounding:** Your custom dimensions are automatically rounded to the nearest multiple of 8. This prevents "invalid shape" errors during video encoding.
* **Fallback:** If either dimension is set to 0, the node defaults back to the selected Preset Level.

### 4. Framerate & Duration
* **Framerate:** Select **16**, **24**, or **30** FPS.
* **Video Duration:** Set the total length in seconds (1.0 to 10.0).

---

## 📦 Node Outputs
- **width/height:** The calculated integer dimensions.
- **length:** Total frame count (calculated as `Duration × FPS + 1`).
- **framerate:** The selected FPS as a float.

---

## 📄 License
This project is licensed under the MIT License.
