# ComfyUI Video Overlay (FFmpeg)

基于 FFmpeg 的 ComfyUI 画中画合成节点。通过一条节点即可把带有 mask 的小视频叠加到主视频，支持透明度、位置与尺寸调节，并且自动处理不同长度的视频，还能在前端直接预览输出结果。**现已支持智能字幕添加和鼠标悬停播放预览！**

> English summary: Drop-in ComfyUI node that overlays a masked clip on top of a base clip using ffmpeg. It handles alpha masks, size/position, mismatched durations, and ships with a small web extension for instant previews. Now with smart subtitle support and hover-to-play preview!
![Demo](workflows/infinite_video_blend_add_subtitle.png)

---

## ✨ 功能亮点
- 纯 FFmpeg 流水线，合成结果无额外编解码器依赖
- 支持 mask/alpha 通道，透明度还可额外再调
- 可在五个常用锚点 + 自定义边距中定位小视频
- 自动对齐时长：小视频不足会自动补帧，主视频不足会自动循环
- 自动输出到 ComfyUI `output` 目录并推送前端预览
- **⭐ NEW**: 智能字幕添加，支持 Whisper alignment 直接连线，自动文本换行
- **⭐ NEW**: 鼠标悬停播放预览，参考 VideoHelperSuite 实现
- **⭐ NEW**: 视频调速功能，支持 0.25x-4x 播放速度（大视频默认1.8x加速，小视频默认1.0x）

---

## 📦 依赖
1. **系统安装 FFmpeg**（命令行可执行）
2. `pip install ffmpeg-python`（已列在 `requirement.txt`）
3. ComfyUI 最新版（tested on ComfyUI 0.2+）

> ⚠️ 如果你使用便携版 ComfyUI，请确认 `python_embeded/python.exe` 能调用 `ffmpeg`。

---

## 🚀 安装步骤
1. 复制整个仓库到 `ComfyUI/custom_nodes/ComfyUI-VideoOverlayFFmpeg`
2. 安装依赖：`pip install -r requirement.txt`
3. （可选，但推荐）把 `web/video_overlay_node.js` 复制到 `ComfyUI/web/extensions/`，即可启用前端视频预览
4. 重启 ComfyUI

---

## 🔧 节点类型

### 1. VideoOverlayNode (基础版)
基础画中画合成节点，无字幕功能。

| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `big_video_path` | STRING | 底图视频绝对路径或相对路径 |
| `small_video_path` | STRING | 叠加视频，通常是带透明背景或配合 mask 的人物 |
| `mask_video_path` | STRING | 与小视频同分辨率/时长的灰度或透明度视频 |
| `opacity` | FLOAT 0~1 | 对 mask 追加整体透明度控制 |
| `position` | 枚举 | `right_bottom/right_top/left_bottom/left_top/center` |
| `margin_x` / `margin_y` | INT | 基于 position 的水平/垂直边距（像素） |
| `size_ratio` | FLOAT | 小视频目标高度 ÷ 主视频高度（默认 0.25） |
| `big_video_audio_volume` | FLOAT 0~2 | 大视频音量（默认 0.0） |
| `small_video_audio_volume` | FLOAT 0~2 | 小视频音量（默认 1.0） |
| `big_video_speed` | FLOAT 0.25~4.0 | 大视频播放速度（默认 1.8x，支持快放/慢放） |
| `small_video_speed` | FLOAT 0.25~4.0 | 小视频播放速度（默认 1.0x，支持快放/慢放） |

### 2. VideoOverlayWithSubtitlesNode (增强版) ⭐
包含所有基础功能 + 字幕支持。

**额外字幕参数**：
| 参数 | 类型 | 说明 |
| --- | --- | --- |
| `alignment` | whisper_alignment | 字幕时间轴数据（支持直接连线或 JSON 字符串） |
| `font_path` | 下拉选择 | 字体文件（自动检测 fonts/ 目录和系统字体） |
| `font_size` | INT 12~200 | 字体大小（默认 48） |
| `font_color` | STRING | 字体颜色（默认 "white"） |
| `subtitle_position` | 枚举 | 字幕位置：bottom_center/top_center/bottom_left/bottom_right/center/custom |
| `x_position` / `y_position` | INT | 自定义位置坐标（仅 custom 模式） |
| `max_text_width` | INT | 文本最大宽度（0=自动为视频宽度的 80%） |
| `subtitle_bg_opacity` | FLOAT 0~1 | 背景透明度（默认 0.7） |
| `subtitle_bg_color` | STRING | 背景颜色（默认 "black"） |
| `video_fps` | FLOAT 1~120 | 视频帧率（默认 24.0） |

**输出**：
- `video_path`（STRING）——合成后的 MP4 文件路径
- 自动视频预览（鼠标悬停播放）

---

## 🧠 工作机制
1. **分析元数据**：读取主视频与小视频宽高、时长
2. **调整尺寸**：按 `h_size_ratio` 把小视频等比例缩放
3. **处理时长**  
   - 主视频更长 → `tpad` 克隆小视频与 mask 的最后一帧  
   - 小视频更长 → `loop` 方式循环主视频画面  
4. **合成透明度**：mask → 灰度 → `alphamerge`，再按需调节 `opacity`
5. **叠加**：使用 `ffmpeg.overlay` 按 position + margin 放置小视频
6. **封装输出**：`libx264 + aac`，带 `+faststart` 方便在线播放

---

## 🗂️ 示例流程
1. 使用 `Load Video` 节点读取主视频和小视频（或直接填路径）
2. 通过视频编辑工具提前导出小视频对应的 mask（黑白视频）
3. 配置本节点：  
   - `big_video_path`: `/data/base.mp4`  
   - `small_video_path`: `/data/portrait.mp4`  
   - `mask_video_path`: `/data/portrait_mask.mp4`  
   - `position`: `right_bottom`, `margin_x = 64`, `margin_y = 64`, `h_size_ratio = 0.3`
4. 执行图，等待终端提示 `[VideoOverlay] ✓`
5. 前端节点会自动显示输出视频；文件同时保存在 `ComfyUI/output/overlay_xxxx.mp4`

---

## 🎬 鼠标悬停播放预览

两个节点都支持视频预览功能：
- **鼠标移入视频**：自动播放并取消静音
- **鼠标移出视频**：自动暂停并静音
- **点击视频**：手动切换播放/暂停
- **自动循环**：视频会自动循环播放

预览功能由 `web/video_preview.js` 实现，ComfyUI 会自动加载。

---

## 📝 字幕格式示例

```json
[
    {
        "value": "One minute of Eldridge Cleaver is worth ten minutes of Roy Wilkins.",
        "start": 0.0,
        "end": 4.86
    },
    {
        "value": "The labor crisis settled at the negotiating table is nothing compared to the confrontation that results in a strike.",
        "start": 6.02,
        "end": 12.9
    }
]
```

**智能换行示例**（1920x1080，48px 字体）：

原文：
```
The labor crisis settled at the negotiating table is nothing compared to the confrontation that results in a strike, or better yet, violence along the picket lines.
```

自动换行后：
```
The labor crisis settled at the negotiating table
is nothing compared to the confrontation that
results in a strike, or better yet, violence
along the picket lines.
```

---

## 🎨 自定义字体

插件已包含 16 个字体（中文、英文、艺术字体等），存放在 `fonts/` 目录：
- YRDZST Semibold.ttf (中文)
- Roboto-Bold.ttf (英文粗体)
- Comic.ttf (漫画字体)
- Impact.ttf (冲击字体)
- ... 等

添加新字体：
1. 将 .ttf 或 .otf 文件放入 `fonts/` 目录
2. 重新加载 ComfyUI
3. 字体会自动出现在下拉列表中

---

## ❓ 常见问题

### 基础功能
- **报错 `文件不存在`**：确保路径无中文空格，或使用绝对路径
- **没有预览**：`web/video_preview.js` 会自动加载，确保 `WEB_DIRECTORY` 配置正确
- **ffmpeg command not found**：把 FFmpeg 加到系统 PATH
- **透明度不生效**：检查 mask 是否正确（白色=不透明，黑色=全透明）
- **输出颜色怪异**：请确保 mask 视频是灰度或单通道

### 字幕功能
- **字幕没有换行**：检查 `max_text_width` 参数，建议设置为视频宽度的 70-80%
- **字幕显示为乱码**：使用支持该语言的字体（中文需要中文字体）
- **字体下拉列表为空**：确保 `fonts/` 目录存在且包含字体文件

### 视频预览
- **视频不自动播放**：浏览器自动播放策略限制，鼠标悬停会自动重试
- **预览加载慢**：视频文件较大时需要时间，等待加载完成即可

---

## 📁 项目结构

```
ComfyUI-VideoOverlayFFmpeg/
├── video_overlay_node.py          # 主节点文件
├── __init__.py                     # 初始化文件
├── web/
│   └── video_preview.js           # 前端视频预览扩展
├── fonts/                         # 字体目录 (16个字体)
│   ├── YRDZST Semibold.ttf
│   ├── Roboto-Bold.ttf
│   └── ...
├── README.md                      # 本文档
├── README_SUBTITLES.md           # 字幕功能详细说明
└── README_VIDEO_PREVIEW.md       # 视频预览功能说明
```

---

## 📮 反馈 & 计划
- [x] 智能字幕添加（已完成）
- [x] 鼠标悬停播放预览（已完成）
- [ ] 支持自定义输出编码器参数
- [ ] 增加可视化遮罩生成辅助节点
- 如有问题，欢迎在 Issues/PR 提交复现信息与日志

---

## 📖 详细文档

- [字幕功能详细说明](README_SUBTITLES.md)
- [视频预览功能说明](README_VIDEO_PREVIEW.md)

Enjoy ComfyUI Video Overlay! 🎬✨
