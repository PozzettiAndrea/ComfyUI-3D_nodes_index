# ComfyUI 背景移除器

ComfyUI的背景移除扩展节点，使用rembg库提供高质量的图像背景移除功能。

## 功能特点

- 支持多种背景移除模型选择
- 自动提取图像掩码
- 支持Alpha matting处理，提高边缘质量
- 批量处理图像
- 完全集成到ComfyUI工作流程中
- 高级模式，支持自定义背景颜色

## 安装

1. 确保你已安装ComfyUI
2. 克隆仓库到ComfyUI的custom_nodes目录:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/assemly/comfyui-bgremover.git
```
3. 安装依赖:
```bash
cd comfyui-bgremover
pip install -r requirements.txt
```

或者直接运行安装脚本：
```bash
cd comfyui-bgremover
python install.py
```

## 使用方法

1. 在ComfyUI工作区添加"背景移除"或"高级背景移除"节点
2. 连接一个图像源到节点的输入
3. 使用输出的图像和掩码进行后续处理
4. 使用ComfyUI内置的MaskToImage节点将掩码转换为可保存的图像


### 节点列表

- **背景移除 (BGRemover)**: 基本背景移除节点
- **高级背景移除 (BGRemoverAdvancedMask)**: 带有更多控制选项的背景移除节点

## 节点说明

### 基础背景移除节点

#### 输入
- `images`: 输入图像

#### 可选输入
- `model_name`: 使用的模型 (u2net, u2netp, u2net_human_seg, u2net_cloth_seg, silueta, isnet-general-use)
- `alpha_matting`: 是否使用alpha matting处理
- `alpha_matting_foreground_threshold`: alpha matting前景阈值
- `alpha_matting_background_threshold`: alpha matting背景阈值
- `alpha_matting_erode_size`: alpha matting腐蚀大小

#### 输出
- 处理后的图像 (带透明背景)
- 提取的掩码

### 高级背景移除节点

除了基础节点的所有功能外，还包括：

#### 额外可选输入
- `post_process`: 是否进行后处理
- `background_color`: 背景颜色 (透明、白色、黑色、红色、绿色、蓝色，或HTML颜色代码如"#FF5733")

## 独立使用示例

本扩展还包含了一个独立使用的示例脚本，可以在命令行中使用：

```bash
cd examples
python save_transparent_image.py 输入图像路径 输出图像路径 [模型名称]
```

示例：
```bash
python save_transparent_image.py input.jpg output.png u2net
```

## 示例工作流

在`examples`目录中提供了两个示例工作流：

1. `workflow_example.json` - 基础背景移除节点的使用示例
2. `workflow_advanced.json` - 高级背景移除节点的使用示例，展示带有自定义背景颜色的功能

要使用这些示例，请在ComfyUI中通过"加载"按钮导入工作流JSON文件。

> **注意**: 示例中使用了 `MaskToImage` 节点来显示掩码，这是为了解决掩码不能直接连接到 `PreviewImage` 的问题。


## 性能提示

- 使用u2netp模型可以获得更快的处理速度，但精度略低
- 对于人像，推荐使用u2net_human_seg模型
- 启用alpha_matting可以获得更好的边缘质量，但会降低处理速度
- 如果在Windows上使用CUDA，确保已安装正确版本的CUDA工具包

## 许可证

MIT
