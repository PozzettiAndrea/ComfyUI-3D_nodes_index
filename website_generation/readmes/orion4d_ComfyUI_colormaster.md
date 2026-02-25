# 🎨 ComfyUI Colormaster Nodes

This project offers a collection of custom nodes for ComfyUI, dedicated to creating/manipulating hexadecimal color palettes, the tools can be diverted for other functionalities.
---

## 📦 Included Nodes

### 1. `Image Collage`

![image](https://github.com/user-attachments/assets/4420a4a1-ab7a-4f48-a47a-2013f1597509)

Combines up to **8 images** into a single canvas either horizontally or vertically with adjustable spacing.

- **Inputs:**  
  `image_1` to `image_8` (optional),  
  `direction`: horizontal / vertical  
  `spacing`: space in pixels between images  

- **Output:** A single merged image  
- 🔧 Use case: create simple image strips, side-by-side comparisons, mood boards

---

### 2. `Annotate Hex Lines`

![image](https://github.com/user-attachments/assets/42a2e187-7f55-4243-a25e-92ca08b2c326)

Adds text annotations (typically hexadecimal color codes) directly onto an image.

- **Inputs:** image, text lines
- **Use case:** labeling generated or extracted colors visually

---

### 3. `Select Hex Line`

![image](https://github.com/user-attachments/assets/f9346541-33ac-49c9-9f31-fa9cd59ce82b)

Dropdown node to **select a line** from a `.txt` or `.csv` list of hex color codes.

- **Inputs:**  
  `list_file`: input file  
  `reload_dropdown`: boolean  
  `mode`: random / selected  
  `selected_line`: shows dropdown if mode is set to "selected"  
- **Output:** selected string (typically a color or color set)

---

### 4. `Hex Color to Image`

![image](https://github.com/user-attachments/assets/f4b556c8-9a27-4442-89f9-72405f8e1e8d)

Generates a **solid color image** from a hexadecimal color string.

- **Inputs:**  
  `hex_color`: e.g. `#ff6600`  
  `width`, `height` (in pixels)

- **Output:** flat color image  
- 🎯 Use case: display a color block or build swatches dynamically

---

### 5. `Color Palette Extractor`

![image](https://github.com/user-attachments/assets/2eb3351d-76d7-4114-af1a-fe912f4b338f)

Extracts a **dominant color palette** from a given image using clustering.

- **Inputs:** image  
- **Output:** list of dominant hexadecimal colors

---

## 🛠️ Installation

1. Clone or download the folder
:
    ```bash
    git clone https://github.com/orion4d/ComfyUI_colormaster.git
    ```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

<div align="center">

<h3>🌟 <strong>Show Your Support</strong></h3>

<p>If this project helped you, please consider giving it a ⭐ on GitHub!</p>

<p><strong>Made with ❤️ for the ComfyUI community</strong></p>

<p><strong>by Orion4D</strong></p>

<a href="https://ko-fi.com/orion4d">
<img src="https://ko-fi.com/img/githubbutton_sm.svg" alt="Buy Me A Coffee" height="41" width="174">
</a>

</div>

