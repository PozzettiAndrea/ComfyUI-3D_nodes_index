# ComfyUI LoadImageWithInfo 节点

这是一个用于ComfyUI的自定义节点，可以获取图像的详细信息，包括名称、格式（后缀）、DPI、尺寸、长边、短边、体积大小和EXIF数据，并支持保存图像功能。

## 功能

### LoadImageWithInfo 节点

该节点可以提取以下图像信息：

- 文件名称（不带后缀）
- 文件格式（无点后缀）
- DPI
- 宽度和高度
- 长边和短边长度
- 文件大小（字节）
- EXIF元数据（如果存在）

### SaveImageWithInfo 节点

该节点可以保存图像并保留原始图像的元数据：

- 支持保存为原始格式或指定格式（avif、webp、jpg、png、tiff）
- 保留原始图像的DPI信息
- 保留原始图像的EXIF数据（对支持EXIF的格式）
- 可选非png格式时同时保存png格式到 LoadImageWithInfoPNG 文件夹内

## 安装

1. 将此仓库克隆或下载到ComfyUI的`custom_nodes`目录中：

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/sjh00/ComfyUI-LoadImageWithInfo.git
```

或者直接下载ZIP文件并解压到`custom_nodes`目录。

2. 重启ComfyUI

## 使用方法

### LoadImageWithInfo 节点

1. 在ComfyUI工作流中，找到`image`分类下的`Load Image With Info`节点
2. 将图像连接到节点的`image`输入
3. 节点将输出图像及其详细信息

### SaveImageWithInfo 节点

1. 在ComfyUI工作流中，找到`image`分类下的`Save Image With Info`节点
2. 将要保存的图像连接到节点的`image`输入
3. 设置以下参数：
   - `filename`：保存的文件名（不含扩展名）
   - `format`：保存格式（original、avif、webp、jpg、png、tiff）
   - `original_format`：原始格式（当format设为original时使用）
   - `quality`：保存质量（1-100，AVIF默认80，其他默认95，png/tiff格式不受影响）
   - `dpi`：图像DPI值
   - `exif`：EXIF元数据（JSON格式字符串）
4. 节点将保存图像

## 示例输出

### LoadImageWithInfo 节点输出

```
LoadImageWithInfo:
  - image -> 导入图像

输出:
  - filename
  - format
  - dpi
  - width
  - height
  - long_edge
  - short_edge
  - file_size
  - exif => {
    "Make": "Canon",
    "Model": "Canon EOS 5D Mark IV",
    "DateTime": "2023:01:15 14:30:22"
    // 更多EXIF数据...
  }
```

### SaveImageWithInfo 节点使用示例

将LoadImageWithInfo节点的输出连接到SaveImageWithInfo节点：

```
LoadImageWithInfo:
  - image -> 选择输入图像

输出:
  - image -> SaveImageWithInfo.images
  - filename -> SaveImageWithInfo.filename
  - format -> SaveImageWithInfo.original_format
  - dpi -> SaveImageWithInfo.dpi
  - exif -> SaveImageWithInfo.exif

SaveImageWithInfo:
  - image <- LoadImageWithInfo.image
  - filename <- LoadImageWithInfo.filename
  - format -> 选择保存格式（original/avif/webp/jpg/png/tiff）
  - original_format <- LoadImageWithInfo.format
  - quality -> 设置保存质量（1-100）
  - dpi <- LoadImageWithInfo.dpi
  - exif <- LoadImageWithInfo.exif
```

这样设置可以保证保存的图像保留原始图像的所有元数据。

## 注意事项

### LoadImageWithInfo 节点

- EXIF数据的可用性取决于图像是否包含这些元数据
- 对于ComfyUI生成的图像，某些信息（如DPI和EXIF）可能不存在或为默认值
- 文件大小是基于内存中的图像估算的，可能与实际保存到磁盘的文件大小略有不同

### SaveImageWithInfo 节点

- 若文件名重名，则自动增加数字以区分
- 并非所有图像格式都支持EXIF数据，目前只有JPG格式支持保存EXIF数据
- 如果选择的保存格式不支持EXIF，EXIF数据将被忽略
- 如果指定的格式无法保存，将自动回退到PNG格式
- quality参数对不同格式的影响：
  - JPG/JPEG：直接影响图像质量（1-100，值越高质量越好）
  - PNG/TIFF：不受影响
  - WEBP/AVIF：影响图像质量（1-100，值越高质量越好，AVIF高于80肉眼无区别，所以已锁定AVIF质量上限为80；若设置100则WEBP/AVIF开启无损模式）
  - 其他格式：如果格式支持quality参数则使用，否则忽略

## 许可证

MIT