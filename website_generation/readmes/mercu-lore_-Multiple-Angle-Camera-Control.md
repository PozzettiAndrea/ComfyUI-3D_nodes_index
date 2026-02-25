# Camera Control & Relighting Prompt Nodes

Advanced prompt generators for ComfyUI, optimized for **dx8152's MultiAngle LoRA** and relighting workflows.

## Author
**Lorenzo Mercugliano**

## Description
A collection of powerful ComfyUI custom nodes that convert camera control and lighting parameters into bilingual prompts (Chinese + English). Designed to work seamlessly with dx8152's MultiAngle LoRA for precise camera control and relighting in image generation workflows.

## Features
- **Multi-directional camera movements** (horizontal, vertical, forward)
- **Camera rotation** with precise angle control (-90° to 90°)
- **Special view modes** (top-down, wide-angle, close-up)
- **Relighting control** with 10 directional light sources
- **Bilingual output** (Chinese + English prompts)
- **Optimized interface** with sliders, toggles, and dropdowns
- **No redundancy** - smart parameter organization

## Installation
1. Clone or download this folder to: `ComfyUI/custom_nodes/`
2. The folder structure should be: `ComfyUI/custom_nodes/camera_control_prompt/`
3. Restart ComfyUI

## Nodes

### 1. Camera Control Prompt Generator

#### Node Inputs
**Dropdowns:**
- **move_horizontal**: Left/Right camera movement
  - none = No movement
  - left = Move left
  - right = Move right

- **move_vertical**: Up/Down camera movement
  - none = No movement
  - up = Move up
  - down = Move down

- **move_forward**: Forward camera movement
  - no = No movement
  - yes = Move forward

**Sliders:**
- **rotate** (-90 to 90, step 45): Camera rotation
  - -90 = Rotate 90° left
  - -45 = Rotate 45° left
  - 0 = No rotation
  - 45 = Rotate 45° right
  - 90 = Rotate 90° right

**Buttons (Boolean):**
- **view_top_down**: Enable top-down view
- **view_wide_angle**: Enable wide-angle lens
- **view_close_up**: Enable close-up view
- **view_bottom_up**: Enable bottom-up view

---

### 2. Relighting Prompt Generator

#### Node Inputs
**Dropdown:**
- **light_direction**: Select the light source direction
  - front = 前方 (Front)
  - front_left = 左前方 (Front Left)
  - left = 左方 (Left)
  - back_left = 左后方 (Back Left)
  - back = 后方 (Back)
  - back_right = 右后方 (Back Right)
  - right = 右方 (Right)
  - front_right = 右前方 (Front Right)
  - above = 上方 (Above)
  - below = 下方 (Below)

**Buttons (Boolean):**
- **use_chinese**: Toggle between Chinese (True) and English (False) output
  - True = Chinese prompt (default)
  - False = English prompt

## Output
Both nodes output a single STRING containing the complete prompt, ready to use with dx8152's MultiAngle LoRA and relighting workflows.

## Example Usage

### Camera Control Prompt Generator
**Inputs:**
- move_horizontal: right
- move_vertical: none
- move_forward: yes
- rotate: 45
- view_top_down: False
- view_wide_angle: True
- view_close_up: False
- view_bottom_up: False

**Output:**
```
将镜头向右移动 Move the camera right. 将镜头向前移动 Move the camera forward. 将镜头向右旋转45度 Rotate the camera 45 degrees to the right. 将镜头转为广角镜头 Turn the camera to a wide-angle lens.
```

---

### Relighting Prompt Generator
**Inputs (Chinese):**
- light_direction: front_left
- use_chinese: True

**Output:**
```
使用图2的亮度贴图对图1重新照明(光源来自左前方)
```

**Inputs (English):**
- light_direction: back_right
- use_chinese: False

**Output:**
```
Relight Figure 1 using the luminance map from Figure 2 (light source from the back right)
```

## Compatibility
- **ComfyUI**: Latest versions
- **LoRA**: Optimized for dx8152's MultiAngle LoRA
- **Language**: Python 3.8+

## License
MIT

## Credits
- **Node Author**: Lorenzo Mercu
- **Optimized for**: dx8152's MultiAngle LoRA
