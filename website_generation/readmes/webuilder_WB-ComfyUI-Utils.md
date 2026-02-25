# ComfyUI WB Utils

一个ComfyUI实用工具节点集合，包含音频处理、文本处理等实用功能。

## 功能

### 当前节点

#### WB Audio Duration
- 支持1D, 2D, 3D音频张量格式
- 支持 `waveform` 和 `audio` 键格式
- 提供详细的调试信息
- 格式化时长显示（秒、分、小时）

### 计划中的节点

- 文本处理节点
- 图像处理节点
- 数据转换节点
- 更多实用工具...

## 安装

### 方法1: 通过Node Manager (推荐)
1. 在ComfyUI中打开Node Manager
2. 搜索 "WB Utils" 或 "WB Audio Duration"
3. 点击安装

### 方法2: 手动安装
1. 将此文件夹复制到ComfyUI的 `custom_nodes` 目录
2. 重启ComfyUI
3. 在节点列表中找到 "WB Audio Duration"

## 使用方法

### WB Audio Duration 节点

1. 添加 "Load Audio" 节点加载音频文件
2. 添加 "WB Audio Duration" 节点
3. 连接音频输出到时长节点
4. 运行工作流查看结果

## 输出

### WB Audio Duration
- `duration_seconds`: 时长（秒，浮点数）
- `duration_text`: 格式化的时长文本

## 支持格式

### WB Audio Duration
- 1D张量: `[samples]`
- 2D张量: `[channels, samples]` 或 `[batch, samples]`
- 3D张量: `[batch, channels, samples]`

## 调试信息

节点会在控制台输出详细的调试信息，包括：
- 音频输入类型
- 音频字典键
- 音频数据形状
- 计算过程

## 示例

```python
# WB Audio Duration 输入音频字典格式
{
    'waveform': torch.tensor([...]),  # 音频数据
    'sample_rate': 22050              # 采样率
}

# 输出
(19.59, '19.59秒')  # (时长秒数, 格式化文本)
```

## 许可证

MIT License

## 作者

webuilder

## 问题反馈

如果您遇到任何问题，请在 [GitHub Issues](https://github.com/webuilder/WB-ComfyUI-Utils/issues) 上提交Issue。

## 贡献

欢迎提交Pull Request来添加新的实用节点！ 