# 🐧 Comfyui-TextEditor-Penguin

一个用于 **ComfyUI** 的文本叠加节点，支持渐变、描边、阴影等丰富效果，适用于在图像上添加高度自定义的文字内容。

## 📦 功能概述

该节点允许用户在图像任意位置叠加文字，支持以下核心功能：

* ✅ **支持多种字体格式**：`.ttf` / `.ttc` / `.otf`
* ✅ **精确定位**：基于百分比坐标 + 锚点 + 偏移
* ✅ **字体与样式设置**：

  * 字体大小与选择
  * 单色 / 渐变填充（带角度控制）
  * 不透明度控制
* ✅ **描边效果**：宽度、颜色、不透明度
* ✅ **阴影效果**：偏移、颜色、不透明度

## 🧩 输入参数

| 参数名                 | 类型              | 描述                                              |
| ------------------- | --------------- | ----------------------------------------------- |
| `text`              | string          | 要叠加的文本内容                                        |
| `image`             | image           | 输入图像                                            |
| `x_pct/y_pct`       | int (0–100)     | 文字相对图像的百分比坐标位置                                  |
| `h_anchor/v_anchor` | enum            | 水平/垂直锚点位置（left/center/right, top/center/bottom） |
| `offset_x/y`        | int             | 文字偏移量（像素）                                       |
| `font_size`         | int             | 字体大小                                            |
| `font_file`         | dropdown        | 字体文件名（来自 `font/` 目录）                            |
| `text_color`        | hex string      | 主文字颜色                                           |
| `text_opacity`      | float (0–1)     | 主文字不透明度                                         |
| `use_gradient`      | bool            | 是否启用渐变色                                         |
| `start_color`       | hex string      | 渐变起始颜色                                          |
| `end_color`         | hex string      | 渐变结束颜色                                          |
| `angle`             | int (-180\~180) | 渐变角度                                            |
| `stroke_width`      | int             | 描边宽度                                            |
| `stroke_color`      | hex string      | 描边颜色                                            |
| `stroke_opacity`    | float (0–1)     | 描边不透明度                                          |
| `shadow_x/y`        | int             | 阴影偏移（x/y）                                       |
| `shadow_color`      | hex string      | 阴影颜色                                            |
| `shadow_opacity`    | float (0–1)     | 阴影不透明度                                          |

## 🖼️ 输出

* 返回修改后的图像（含叠加文字），格式为 ComfyUI `IMAGE` 类型。

## 📁 安装与使用

1. 将项目放置到`custom_nodes/` 目录下（覆盖旧版本）。
2. 确保存在 `font/` 目录，并放入所需字体文件（`.ttf` / `.ttc` / `.otf`）。
3. 重启 ComfyUI

## 📂 项目结构

```
Comfyui-TextEditor-Penguin/
├── project.py        # 节点实现
└── __init__.py       # 与 ComfyUI 的接口
```
   
## 🛠 兼容性与备注

* 推荐使用 PIL ≥ 10.0，以确保 `font.getbbox()` 正常工作。
* 图像需为 RGBA 模式，节点内部会自动处理 tensor → PIL 转换。
* 若未输入文字，节点将直接返回原图。

---

