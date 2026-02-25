# ⚡ ComfyUI Mohseni Kit

**ComfyUI Mohseni Kit** is a collection of useful custom nodes for **ComfyUI**, designed to improve visualization, workflow efficiency, and user experience.

## 🌟 Features

✅ **Float Preview Node** – A live floating image preview for ComfyUI
✅ **More nodes coming soon** – The kit will be expanded with additional functionality
✅ **Lightweight & Efficient** – Optimized for performance and fast updates

---

## 🖼️ Float Preview Node

### **🔹 What is Float Preview?**

The **Float Preview Node** allows you to preview generated images in a **floating, resizable, and always-on-top window** while using ComfyUI.
Unlike the built-in preview, this window persists **outside of the ComfyUI interface**, making it **perfect for multi-monitor workflows**.

### **🔹 Features**

- 🔍 **Live Image Preview** – View images in real-time while working in ComfyUI.
- 🖥️ **Floating Window** – Can be moved, resized, and stays always on top.
- 🏆 **Batch Image Support** – Scroll through multiple images when batch processing.
- 💾 **Save & Copy** – Easily save or copy previewed images.
- 🎨 **Nice Modern UI - PyQt6** – Supports dark/light themes and custom scaling based on system settings.
- 📌 **Always On Top** – Keep the window visible while switching between apps.
- 🖱️ **Window Dragging** - Move the window to anywhere just bu dragging.
- ⚙️ **Persistant Settings** - Your settings like window `size`, `position` and `Always on Top` will be save and load across workflows (inside this node directory itself).
- ⌨️ **Keyboard Shortcuts** – Navigate images & toggle settings quickly.
- ☰ **Right Click Menu** - Same as keyboard shortcuts but in a right click menu

---

## 📥 Installation

- ### Manual Installation

  - ***(Method 1)***

1. Goto ComfyUI/custom_nodes directory in terminal(cmd)

2. ```bash
    git clone https://github.com/mohseni-mr/ComfyUI-Mohseni-Kit
3. Restart ComfyUI

- ### Using ComfyUI Manager (Soon - to be confirmed)

  - ***(Method 2)***

1. Open ComfyUI.
2. Go to **ComfyUI Manager**.
3. Search for **ComfyUI Mohseni Kit** and click **Install**.
4. Restart ComfyUI.

---

🛠️ How to Use
Find the node in ComfyUI under:
> `⚡ Mohseni Kit \ Preview`

Connect an IMAGE output to the Float Preview Node.
Run the workflow.
The floating window will appear, showing the generated images.
Use arrow keys (← →) or to navigate batch images.
Right-click for additional options (Save, Copy, Always On Top).

---

## 📌 Settings & Controls

| Action             | Description                      |
|--------------------|----------------------------------|
| Up or Left         | Navigate to Previous Image       |
| Down or Right      | Navigate to Next Image           |
| CTRL + T           | Toggle Always on Top             |
| CTRL + C           | Copy Current Image to Clipboard  |
| CTRL + S           | Save Current Image (PNG or JPEG) |
| Esc                | Close the Window                 |
| Moouse Right Click | Open the Context Menu            |

---

## 📌 Dependencies

- PyQt6 (pip install PyQt6)
- ftfy (pip install ftfy)

---

## 📜 License

This project is licensed under the **Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)**.

- You **must credit** the original author: **Mohammadreza Mohseni**.
- If you modify this project, **you must share it under the same license**.
- Commercial use is **allowed**, but credit is required.

🔗 **Read the full license here:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)

---

## 📬 Contact & Support

For questions or feedback, contact:
> [Mohammadreza Mohseni](https://bio.mohseni.info)
