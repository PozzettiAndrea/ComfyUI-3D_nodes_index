# Comfyui-Image-Concat - A Powerful Image Concatenation Tool (v1.1)

---

## ✨ Core Features (Latest Update: v1.1 - Critical Bug Fix + All Features from v1.1)

This node is a powerful image concatenation tool for ComfyUI, with True Alpha Channel Support and Multiple Image-title Fill Modes.

---
### ✨ I. Key Capabilities (v1.1)
---

#### 1. Six Image-title Fill Modes (Image resizing mode for each title block)

| Mode | Description |
|------|-------------|
| **(1) smaller value filler** | Fill the block with the smaller value of the origin image's long side and the block's width (maintains aspect ratio) |
| **(2) Stretches image to fill** | Stretches image to fill block (may distort aspect ratio) |
| **(3) zoom by long side (recommended)** | Zoom long side of origin image to block width (maintains aspect ratio), then fill the block |
| **(4) crop square by short side** | Crops square by short side of origin image (maintains aspect ratio), then zoom it to fill the block fully |
| **(5) equal title width up_down** | Equal-width mode, images stack vertically (ideal for long strip images) |
| **(6) equal title height left_right** | Equal-height mode, images stack horizontally (ideal for panorama images) |

#### 2. Flexible Title Block Start Position Control

- **(1) start_from margin**: Blocks start directly at page margin (top/left aligned)
- **(2) start_from margin + padding**: Blocks start with extra padding (top aligned)
- **(3) start_from margin + padding(vertical centering)**: Auto vertical centering + horizontal centering (optimized for incomplete rows/pages)

#### 3. Optional Vertical/Horizontal Centering

- **Horizontal Centering**: Automatically centers incomplete rows (multi-column mode)
- **Vertical Centering**: Enabled via `start_from margin + padding(vertical centering)` option

#### 4. Multiple Background Styles

- **Light (white)** / **Dark (black)** / **Transparent (alpha channel)** (True 4-channel RGBA support)

![background_style][def1]

#### 5. Custom Border Styles (Dual Layer: Title Block + Whole Page)

- **Border shapes**: None / Rectangle / Rounded (radius 10/20/30)
- **Border line styles**: Solid / Dashed (4px,4px) / Dashed (8px,8px) / Dotted (1px,2px) / Dash-dot (8px,4px,2px,4px)
- **Auto border color adaptation**: White on dark background, black on light/transparent background

#### 6. Filename Customization

- **Display filename** on/around title blocks (position: none/above/top/middle/bottom/below)
- **16 customizable filename colors** (black/white/red/dark red/blue/dark blue/green/dark green/yellow/orange/purple/pink/light gray/dark gray/slate gray/cyan/magenta)

#### 7. Save Individual Titles/Images

- **Save modes**: none / save single title (with padding/border) / save single image (original size, no whitespace)
- All saved files retain alpha channel (PNG format)

---
### ✨ II. Input Parameters (v1.1 Full List)
---

| Parameter Name | Type | Default | Description |
|----------------|------|---------|-------------|
| **a0_images** | IMAGE | "" | connect input image(s) from other node (Optional) |
| **a1_image_dir** | STRING | "" | Absolute path of image folder (Required) |
| **a2_page_width** | INT | 4000 | Total width of canvas (px), height auto-calculated by aspect ratio (max 50000px) |
| **a3_page_aspect_ratio** | COMBO | 3:2 | Overall canvas aspect ratio (10:1 ~ 1:10, e.g., 9:16 for vertical layout) |
| **a4_cols_rows_per_page** | INT | 3 | Global layout count: <br>- Mode 1-4: Columns per row <br>- Mode 5: Groups per column <br>- Mode 6: Rows per page |
| **a5_page_margin** | INT | 50 | Canvas border margin (px, 0~500) |
| **a6_title_padding** | INT | 30 | Padding between title blocks (px, 0~200) |
| **a7_title_draw_mode** | COMBO | 3.zoom by long side | 6 image fill modes (see Section I.1) |
| **a8_title_first_position** | COMBO | start_from margin | Title block start position (vertical centering option included) |
| **a9_background_style** | COMBO | Light (white) | Canvas background style (Light/Dark/Transparent) |
| **a10_title_border** | COMBO | Rounded (radius=10px) | Single title block border style |
| **a11_title_border_style** | COMBO | Solid | Title block border line style |
| **a12_page_border** | COMBO | Rounded (radius=30px) | Whole page border style |
| **a13_page_border_style** | COMBO | Solid | Page border line style |
| **a14_filename_position** | COMBO | none | Filename display position (none/above/top/middle/bottom/below) |
| **a15_filename_color** | COMBO | black | Filename color (16 options) |
| **a97_title_save_mode** | COMBO | none | Save individual title/image mode (none/save single title/save single image) |
| **a98_title_save_dir** | STRING | ./output/concat_titles | Save path for individual titles/images |
| **a99_title_save_filename** | COMBO | source file name | Save filename mode（source file number/source file name/page + number）|

---
### ✨ III. Outputs (v1.1)
---

| Output Name | Type | Description |
|-------------|------|-------------|
| **b1_concat_images** | IMAGE | Final concatenated image tensor (multi-page as batch tensor) |
| **b2_page_count** | INT | Total pages of concatenated images (for counting/renaming) |
| **b3_size_per_title** | STRING | Base size of single title block (e.g., 300×300) |
| **b4_valid_image_count** | INT | Total valid images read from a1_image_dir (for verification) |
| **b5_title_save_path** | STRING | Final save path of individual titles/images (with timestamp) |
| **b6_help_info** | STRING | Full parameter guide (connect to "preview any" node to view) |

---
### ✨ IV. Get user guide qucikly
---

####  ONLY by connecting one port, you can get user guide of this node tool.
1. Connect `b6_help_info` to "Preview any" 
2. Drag below image `one_port.png`, which can be found in directory `./custom_nodes/Comfyui-Image-Concat/images/`, onto comfyui page
3. Run this node
![help_info][def11]

---
### ✨ V. Usage Examples
---

#### ✅ 1. Basic Usage (Quick Start)

- (1) In ComfyUI, double-click to search for "concat", select `Image Concatenate(QQ2540968810)` node (under `Image Processing/concat`)

- (2) Fill `a1_image_dir` with your image folder path (absolute path recommended)

- (3) Connect `b1_concat_images` to "Image Preview" or "Save Image" node

- (4) Adjust parameters (e.g., `a4_cols_rows_per_page` for rows/columns, `a7_title_draw_mode` for fill style)

- (5) Run the node → Get concatenated images in `ComfyUI/output` directory

- (6) (Optional) Connect `b6_help_info` to "Preview Any" node to view full parameter guide

![image_concat3][def4_v1.1]
V1.0 stitching image as below:
![image_concat3][def4]
*Note: Image path: `custom_nodes/Comfyui-Image-Concat/images/image_concat3.png`*

---

#### ✅ 2. Advanced Workflow Examples

**(1) smaller value filler (Mode 1)**

**Parameters:**
- a4_n_per_rows = 5 (5 columns per row, this port name was changed to `a4_cols_rows_per_page` from v1.1)
- a8_draw_mode = "1.smaller value filler"(this port name was changed to `a7_title_draw_mode` from v1.1)

**Result:** 
- `b2_page_count = 4` concatenated images(For v1.0), all title blocks saved to `a14_blocks_save_dir`(this port name was changed to `a98_title_save_dir` from v1.1)

![image_concat1][def5]
*Note: Image path: `custom_nodes/Comfyui-Image-Concat/images/image_concat1.png`*

---

**(2) stretches image to fill (Mode 2)**

**Parameters:**
- set Parameters like the image(For v1.0) as below
- Parameters for versions above V1.0 can be configured similarly to V1.0.

**Result:**
- `b2_page_count = 1` RGBA image (editable in Photoshop)

![image_concat2][def6]
*Note: Image path: `custom_nodes/Comfyui-Image-Concat/images/image_concat2.png`*

---

**(3) crop square by short side (Mode 4) + Vertical Centering**

**Parameters:**
- set Parameters like the image(For v1.0) as below
- Parameters for versions above V1.0 can be configured similarly to V1.0.

**Result:** 
- `b2_page_count = 2` vertically centered images

![image_concat4][def7]
*Note: Image path: `custom_nodes/Comfyui-Image-Concat/images/image_concat4.png`*

---

**(4) equal title width up_down (Mode 5)**

**Parameters:**
- a7_title_draw_mode = "5.equal title width up_down"
- a4_cols_rows_per_page = 1 (single column)
- a8_title_first_position = "start_from margin + padding(vertical centering)"

**Result:** 
- `b2_page_count = 2` vertically centered images(For v1.1+)

![image_concat5][def8]

*Note: Image path: `custom_nodes/Comfyui-Image-Concat/images/image_concat5.png`*

---

**(5) equal title height left_right (Mode 6)**

**Parameters:**
- a7_title_draw_mode = "6.equal title height left_right"
- a4_cols_rows_per_page = 2 (2 rows per page)
- a14_filename_position = "bottom" (show filename at image bottom)
- a15_filename_color = "white" (match dark background)


**Result:**
- `b2_page_count = 3` vertically centered images(For v1.1+)

![image_concat6][def9]

*Note: Image path: `custom_nodes/Comfyui-Image-Concat/images/image_concat6.png`*

---

**(6) input images example**

**Result:**
- `b2_page_count = 1` vertically centered images(For v1.1+)

![from_input_images][def12]

*Note: Image path: `custom_nodes/Comfyui-Image-Concat/images/from_input_images.png`*

---

**Source images download:**  
[Google Drive](https://drive.google.com/file/d/1in6XwuYF-DbZA8zPcgrFiY4NU4y-r_zp/view?usp=drive_link) | [Baidu Netdisk](https://pan.baidu.com/s/1fu2_7Z3oOLG_LrHBd1Mk0w?pwd=gpan) (59 test images)

---
#### ✅ 3. Image Resizer

##### use me as a Image  resize tool (Mode 3)

**Parameters:**
- a4_cols_rows_per_page = 1 (1 columns per row)
- a5_page_margin = 0
- a6_title_padding = 0
- a7_title_draw_mode = zoom by long side(recommend)
- a97_title_save_mode = "save single image"

![change_size_batchly_v1.1][def10]

---
### ✨ VI. Installation
---

- ✅ **Method 1: Manual Installation (Recommended)**

   (1) Navigate to ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```
   (2) Clone the repository:
   ```bash
   git clone https://github.com/shmbatom/Comfyui-Image-Concat.git
   ```
   (3) Restart ComfyUI service.


- ✅ **Method 2: ComfyUI Manager**

- (1) Open ComfyUI Manager
- (2) Search for "Comfyui-Image-Concat"
- (3) Click "Install"
- (4) Restart ComfyUI
- (5) Find the node: `Image Processing/concat` → `Image concatenate(QQ2540968810)`

---

### ✨ VII. Notes & Limitations
---

- **Output format**: All output images retain alpha channel (PNG format recommended for transparency)
- **a0_images**: input images from other node. You can use `a0_images` or `a1_image_dir` as source images, but `a1_image_dir` will be IGNORED if this two ports are both setted.
- **a4_cols_rows_per_page**: Columns/Rows Per Page
   - For Mode 1-5: Set the fixed number of columns per row
   - For Mode 6: Set the fixed number of rows per page
Min:1, Max:20, Default:3
- **Saved title/images**: Include borders and alpha channel (no quality loss)
- **Border color**: Auto-adapts to background (white on dark, black on light/transparent)
- **Centering rules**:
  - **Horizontal Centering**: Auto-enabled for incomplete rows (multi-column mode)
  - **Vertical Centering**: Only enabled when `a8_title_first_position = "start_from margin + padding(vertical centering)"`
- **Maximum canvas size**: 50000px (adjust `a2_page_width` max value in node code if needed)
- **Supported input formats**: PNG, JPG, JPEG, BMP, GIF, WEBP, TIFF (alpha channel only for PNG)
- **Filename display rules**:
  - "above/below" are mapped to "top/bottom" in "save single image" mode
  - Font size auto-scales with title block size (5% of block min side)

---

### ✨ VIII. Changelog
---

#### v1.1 (2025/01/18)

-  Add 1 optional IMAGES input port named `a0_image`.  
-  Add 2 new bitmap stitching modes: equal-width vertical stitching (top to bottom), equal-height horizontal stitching (left to right)
-  Optimized the tile saving mode, including three options: none/save single block/save single image
-  Added the function of displaying image filenames on the stitched tiles, with customizable text colors (16 colors)
-  Simply connect to the b6 port to view the usage help for this node
- 🎨 Standardized the port naming on the node page

---

### ✨ IX. Donation
---

If you find this tool helpful, you can buy me a cup of coffee ☕

![donate_me][def99]

---

[def1]: images/backgroud.png
[def2]: images/parameter.png
[def3]: images/out.png
[def4]: images/image_concat3.png
[def4_v1.1]: images/image_concat3_v1.1.png
[def5]: images/image_concat1.png
[def6]: images/image_concat2.png
[def7]: images/image_concat4.png
[def8]: images/image_concat5_v1.1.png
[def9]: images/image_concat6_v1.1.png
[def10]: images/change_size_batchly_v1.1.png
[def11]: images/one_port.png
[def12]: images/from_input_images_node.png
[def99]: images/donate.png




