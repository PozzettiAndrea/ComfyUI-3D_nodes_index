# ComfyUI-QwenMultiangle Lightning

**Authors / 作者:** aiwood & wallen

[English](#english) | [中文](#中文)

---

<a name="english"></a>
## English

A ComfyUI custom node for 3D lighting angle control. Provides an interactive Three.js viewport to adjust light direction, elevation, intensity and color, outputs formatted prompt strings for relighting image generation.

![preview](img.png)

### Features

- **Interactive 3D Lighting Control** - Drag handles in the Three.js viewport to adjust:
  - Light Azimuth: 0° - 360° (horizontal direction)
  - Light Elevation: -90° to 90° (vertical angle)
  - Light Intensity: 0 - 10
  - Light Color: HEX color picker with real-time preview
- **Real-time Preview** - Connect an image input to see it displayed in the 3D scene
- **Cinematic Mode** - Professional cinematic relighting with raytraced shadows
- **Scene Lock** - Maintains character consistency, pose, and composition while only adjusting lighting
- **Bidirectional Sync** - Slider widgets and 3D handles stay synchronized
- **Color Preview** - Real-time color preview block on the node

### Installation

1. Navigate to your ComfyUI custom nodes folder:
   ```bash
   cd ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/ComfyUI-QwenMultiangle-Lightning.git
   ```

3. Restart ComfyUI

### Usage

1. Add the **Qwen Multiangle Lightning** node from the `image/lighting` category
2. Optionally connect an IMAGE input to preview in the 3D scene
3. Adjust lighting parameters by:
   - Dragging the colored handles in the 3D viewport
   - Using the slider widgets
   - Picking a light color from the color widget
4. Toggle `cinematic_mode` for professional lighting effects
5. The node outputs a prompt string describing the lighting setup

### Widgets

| Widget | Type | Range | Description |
|--------|------|-------|-------------|
| light_azimuth | Slider | 0° - 360° | Light horizontal direction |
| light_elevation | Slider | -90° to 90° | Light vertical angle |
| light_intensity | Slider | 0 - 10 | Light strength |
| light_color_hex | Color | HEX | Light color with preview |
| cinematic_mode | Checkbox | - | Enable cinematic lighting |

### 3D Viewport Controls

| Handle | Color | Control |
|--------|-------|---------|
| Ring handle | Pink | Light azimuth (horizontal) |
| Arc handle | Cyan | Light elevation (vertical) |
| Line handle | Gold/Custom | Light intensity/distance |

### Output Prompt Example

```
SCENE LOCK, CONSTANT BACKGROUND, FIXED SCENERY. STATIC SHOT, FIXED VIEWPOINT, NO CAMERA MOVEMENT. 
maintaining character consistency, keeping the same character pose and action, maintaining the same composition, 
RELIGHTING ONLY: only the light rays and shadows change, the scene remains untouched. 
professional cinematic relighting, bright directional colored light (hex: #FF6B35), 
light hitting from the front-right side, high-positioned light source, raytraced shadows, realistic global illumination
```

---

<a name="中文"></a>
## 中文

一个用于 ComfyUI 的 3D 光照角度控制自定义节点。提供交互式 Three.js 视口来调整光照方向、仰角、强度和颜色，输出格式化的提示词用于重光照图像生成。

![预览](img.png)

### 功能特点

- **交互式 3D 光照控制** - 在 Three.js 视口中拖拽控制柄来调整：
  - 光照方位角：0° - 360°（水平方向）
  - 光照仰角：-90° 到 90°（垂直角度）
  - 光照强度：0 - 10
  - 光照颜色：HEX 颜色选择器，带实时预览
- **实时预览** - 连接图像输入可在 3D 场景中预览
- **电影模式** - 专业电影级重光照，带光线追踪阴影
- **场景锁定** - 保持角色一致性、姿势和构图，仅调整光照
- **双向同步** - 滑块控件和 3D 控制柄保持同步
- **颜色预览** - 节点上显示实时颜色预览色块

### 安装方法

1. 进入 ComfyUI 自定义节点文件夹：
   ```bash
   cd ComfyUI/custom_nodes
   ```

2. 克隆此仓库：
   ```bash
   git clone https://github.com/your-repo/ComfyUI-QwenMultiangle-Lightning.git
   ```

3. 重启 ComfyUI

### 使用方法

1. 从 `image/lighting` 分类中添加 **Qwen Multiangle Lightning** 节点
2. 可选：连接 IMAGE 输入以在 3D 场景中预览
3. 通过以下方式调整光照参数：
   - 在 3D 视口中拖拽彩色控制柄
   - 使用滑块控件
   - 从颜色控件中选择光照颜色
4. 开启 `cinematic_mode` 获得专业光照效果
5. 节点输出描述光照设置的提示词

### 控件说明

| 控件 | 类型 | 范围 | 描述 |
|------|------|------|------|
| light_azimuth | 滑块 | 0° - 360° | 光照水平方向 |
| light_elevation | 滑块 | -90° 到 90° | 光照垂直角度 |
| light_intensity | 滑块 | 0 - 10 | 光照强度 |
| light_color_hex | 颜色 | HEX | 光照颜色（带预览） |
| cinematic_mode | 复选框 | - | 启用电影级光照 |

### 3D 视口控制

| 控制柄 | 颜色 | 控制项 |
|--------|------|--------|
| 圆环控制柄 | 粉色 | 光照方位角（水平） |
| 弧形控制柄 | 青色 | 光照仰角（垂直） |
| 线条控制柄 | 金色/自定义 | 光照强度/距离 |

### 输出提示词示例

```
SCENE LOCK, CONSTANT BACKGROUND, FIXED SCENERY. STATIC SHOT, FIXED VIEWPOINT, NO CAMERA MOVEMENT. 
maintaining character consistency, keeping the same character pose and action, maintaining the same composition, 
RELIGHTING ONLY: only the light rays and shadows change, the scene remains untouched. 
professional cinematic relighting, bright directional colored light (hex: #FF6B35), 
light hitting from the front-right side, high-positioned light source, raytraced shadows, realistic global illumination
```

---

## Project Structure / 项目结构

```
ComfyUI-QwenMultiangle-Lightning/
├── __init__.py          # Module entry point / 模块入口
├── nodes.py             # Node implementation / 节点实现
├── pyproject.toml       # Project configuration / 项目配置
├── README.md            # Documentation / 文档
├── LICENSE              # MIT License / MIT 许可证
└── web/
    └── js/
        ├── camera_viewer.js   # Three.js 3D viewer / Three.js 3D 视图
        └── qwen_camera.js     # ComfyUI extension / ComfyUI 扩展
```

## Authors / 作者

- **aiwood**
- **wallen**

## Acknowledgments / 致谢

Special thanks to / 特别感谢：

- [jtydhr88](https://github.com/jtydhr88) - For the original ComfyUI-qwenmultiangle implementation / 原始 ComfyUI-qwenmultiangle 实现
- [multimodalart/qwen-image-multiple-angles-3d-camera](https://huggingface.co/spaces/multimodalart/qwen-image-multiple-angles-3d-camera) - Hugging Face Spaces inspiration / Hugging Face Spaces 灵感来源
- [fal.ai](https://fal.ai/models/fal-ai/qwen-image-edit-2511-multiple-angles/) - Qwen Image Edit model / Qwen 图像编辑模型

## License / 许可证

MIT License - See [LICENSE](LICENSE) for details / 详见 [LICENSE](LICENSE) 文件

