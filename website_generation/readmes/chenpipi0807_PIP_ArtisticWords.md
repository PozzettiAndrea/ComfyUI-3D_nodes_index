# PIP Artistic Words for ComfyUI - 艺术文字生成器

一款强大的ComfyUI扩展节点，能够为您的图像添加各种精美的艺术文字效果，支持丰富的文字样式和特效。
【字体版权问题请自行了解后使用】

## ✨ 特色功能
![微信截图_20250321151732](https://github.com/user-attachments/assets/5dc29a4b-ff34-4e8e-a335-746e6d5610c0)

![微信截图_20250313103634](https://github.com/user-attachments/assets/901211c6-e56b-4c36-b82a-91d628980666)

![微信截图_20250311110539](https://github.com/user-attachments/assets/7906acb5-6532-4ae7-a0d3-354bb20df90d)

![微信截图_20250310131945](https://github.com/user-attachments/assets/a4668e66-6ea3-4d83-ae6a-defc1d957967)

![微信图片_20250309090648](https://github.com/user-attachments/assets/59fbc3ff-ed2c-4a8e-9f50-780883fcc066)


- 🎨 多种艺术效果：渐变填充、描边、阴影、发光、内阴影等效果组合
- 🖼️ 智能排版：自动调整字体大小和位置，确保文字优雅地融入图像
- 📏 自动换行：基于单词数量智能分行，排版更美观
- 🎯 安全区域：自动将文字放置在图像的可视安全区域内
- 🔄 随机样式：支持随机生成样式或指定特定样式
- 📋 SVG导入：支持从SVG文件导入自定义文字样式
- 🌟 高级特效：全新优化的内阴影效果，边缘清晰自然，不遮挡渐变填充

## 🔥 最新功能更新

0310 修复了安全区域失效的问题;修复了节点生成debug图像到桌面的问题；
     增加了示例工作流；
0311 新增了PIP SVG Recorder节点用于测试全部的svg样式以及保存svg模板（其中测试模式是仅测试，保存模式是保存SVG模板到项目的SVG路径）；修复了内阴影的样式问题，现在它和设计软件里一样了。     

0313 新增了简易样式（无渐变和外发光）的实现以及智能拾色节点，自测处理速度＜1s。工作流同步在workflow里了。

0315 移除了过多的终端打印（确实看着挺烦人~）

0321 新增了一个看上去很高级但是我也不知道有啥用的功能

### 内阴影效果全面优化
- ✅ 全新边缘检测算法：只在文字内边缘产生内阴影效果，不再覆盖整个填充区域
- ✅ 智能偏移处理：完美实现从边缘到偏移方向的连续阴影过渡，避免边缘间隙
- ✅ 参数精确控制：内阴影宽度、模糊程度、偏移值等均直接遵循SVG文件定义
- ✅ 渐变可见性：优化后的内阴影不会遮挡文字的渐变填充效果
- ✅ 边缘平滑：通过高斯模糊实现平滑边缘过渡，减少锯齿

## 📊 节点说明

### PIP 艺术文字生成器

此节点可在输入图像上叠加艺术文字，智能定位并调整文字大小，使其完美融入图像。

#### 输入参数:
- **image**: 输入的背景图像
- **text**: 要显示的文字（支持多个单词和自动换行）
- **seed**: 随机种子，用于复现效果（0表示每次随机）
- **style**: 要应用的文字样式（从可用样式中选择或'random'随机选择）
- **color_match**: 启用或禁用颜色匹配（与背景图像匹配颜色）
- **margin_top** (可选): 上边距，图像高度的比例（默认: 0.25）
- **margin_bottom** (可选): 下边距，图像高度的比例（默认: 0.15）
- **margin_left** (可选): 左边距，图像宽度的比例（默认: 0.1）
- **margin_right** (可选): 右边距，图像宽度的比例（默认: 0.1）
- **opacity** (可选): 文字透明度（默认: 1.0）
- **debug_info** (可选): 调试信息级别（none, basic, detailed）

#### 输出:
- **image**: 添加了艺术文字的图像

### PIP 文字预览生成器

此节点生成带透明背景的艺术文字，可用于图像合成。

#### 输入参数:
- **text**: 要显示的文字（支持多个单词和自动换行）
- **seed**: 随机种子，用于复现效果（0表示每次随机）
- **style**: 要应用的文字样式（从可用样式中选择或'random'随机选择）
- **width** (可选): 输出图像宽度（默认: 1440）
- **height** (可选): 输出图像高度（默认: 1440）

#### 输出:
- **image**: 带有艺术文字的透明图像
- **alpha_mask**: 文字的Alpha蒙版

## 📥 安装方法

1. 克隆此仓库到您的ComfyUI自定义节点文件夹:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/chenpipi0807/PIP_ArtisticWords.git
```

2. 安装所需依赖:
```bash
pip install -r requirements.txt
```

## 🧩 依赖项

- Python 3.8+
- Pillow >= 9.0.0
- NumPy >= 1.20.0
- OpenCV (opencv-python) >= 4.5.0

## 🚀 使用指南

1. 在ComfyUI工作流中添加"PIP Artistic Text Generator"节点
2. 连接输入图像，输入您想要的文字
3. 选择一种样式或使用"random"随机选择
4. 根据需要调整其他参数
5. 执行工作流，欣赏生成的艺术文字效果！

## 🎨 自定义样式

您可以通过添加或修改SVG文件来创建自己的自定义样式：

1. 在`SVG`文件夹中创建一个新的SVG文件
2. 定义样式属性（渐变、描边、阴影等）
3. 重启ComfyUI，新样式将自动加载

### 从设计软件导出SVG样式

设计师可以直接从专业设计软件（如Sketch）创建并导出SVG样式：

1. 在Sketch中创建您想要的文字样式（渐变填充、描边、阴影等）
2. 确保文字已转换为矢量路径（文本 > 转换为轮廓）
3. 应用所需的所有效果（填充、描边、阴影、内阴影等）
4. 导出为SVG文件（文件 > 导出 > 选择SVG格式）
5. 将导出的SVG文件放入`PIP_ArtisticWords/SVG/`目录
6. 重命名文件为有意义的名称（例如：`elegant-gold.svg`、`neon-blue.svg`）
7. 重启ComfyUI，新样式将自动加载

### 自定义样式文件结构

为确保SVG样式正确加载，建议遵循以下结构：

```xml
<svg>
  <defs>
    <!-- 渐变和滤镜定义 -->
    <linearGradient id="填充渐变ID">...</linearGradient>
    <linearGradient id="描边渐变ID">...</linearGradient>
    <filter id="滤镜ID">...</filter>
  </defs>
  
  <g>
    <!-- 文字路径定义 -->
    <path d="..." fill="url(#填充渐变ID)" stroke="url(#描边渐变ID)" filter="url(#滤镜ID)" />
  </g>
</svg>
```

### 自定义颜色匹配关系

您可以修改颜色匹配配置，自定义颜色与样式的映射关系：

1. 打开配置文件：`PIP_ArtisticWords/config/style_color_mapping.json`
2. 修改`color_style_mapping`部分，为每种颜色指定合适的样式：

```json
"color_style_mapping": {
  "红色名称": ["样式1", "样式2"],
  "绿色名称": ["样式3"]
}
```

例如，如果您想让棕色图像使用"classic-black-gold"样式：

```json
"brown": ["classic-black-gold", "fire-orange-red"]
```

3. 每种颜色可以指定多个样式选项，系统会随机选择其中一个
4. 您也可以在`style_descriptions`部分添加样式的描述信息
5. 保存文件后重启ComfyUI即可生效

### 支持的颜色类别

颜色匹配系统支持以下基本颜色类别：
- red（红色）
- orange（橙色）
- yellow（黄色）
- green（绿色）
- cyan（青色）
- blue（蓝色）
- purple（紫色）
- pink（粉色）
- brown（棕色）
- white（白色）
- black（黑色）
- gray（灰色）

## 📝 注意事项

- 对于包含发光和阴影效果的样式，建议为文字留出足够的空间
- 如果您遇到任何问题，可以尝试调整安全区域边距参数
- 复杂效果可能需要更多处理时间

## 🤝 贡献指南

欢迎贡献新功能、样式或修复bug！请通过Pull Request提交您的贡献。

## 📜 许可证

[MIT License](LICENSE)
