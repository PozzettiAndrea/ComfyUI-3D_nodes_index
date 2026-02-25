# ComfyUI 图片回调节点

一个简单的 ComfyUI 自定义节点，支持图片回调功能。

## 节点描述

### ImageCallbackNode - 图片回调节点

一个输出节点，用于处理多张图片并发送回调请求。

**功能特性**:
- 支持批量图片处理
- 自动保存图片到指定目录
- 发送 HTTP 回调请求
- 返回 ComfyUI 格式的图片链接
- 支持任务 UUID 标识

**输入参数**:
- `images` (IMAGE): 多张图片输入
- `task_uuid` (STRING): 任务唯一标识符
- `callback_url` (STRING): 回调地址
- `save_images` (BOOLEAN): 是否保存图片
- `output_path` (STRING): 输出目录
- `image_format` (COMBO): 图片格式 (JPEG/PNG/WEBP)
- `quality` (INT): 图片质量 (1-100)
- `include_metadata` (BOOLEAN): 是否包含元数据

**输出**: 无（输出节点）

## 快速开始

### 1. 安装

#### 从 GitHub 克隆
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/upseem/comfyui_callback.git
```

### 2. 启动回调服务器

```bash
cd custom_nodes/comfyui_callback
python fastapi_callback_server.py
```

服务器启动后会显示：
- 本机IP地址
- 所有接口链接
- 端口: 6688

### 3. 配置回调节点

1. 在 ComfyUI 中添加 "图片回调节点"（作为最后的输出节点）
2. 连接图片输入
3. 设置参数：
   - `task_uuid`: 任务标识（如：test123）
   - `callback_url`: `http://localhost:6688/images_callback`
   - 其他参数保持默认

### 4. 测试

1. 执行工作流
2. 查看控制台输出
3. 访问 http://localhost:6688/status 查看回调状态
4. 查看 `callback_logs/` 目录中的日志文件

## 回调数据格式

```json
{
  "task_uuid": "test123",
  "message": "图片处理完成",
  "images": ["callback/test123_1760090252_000.jpg"],
  "comfyui_images": ["/api/view?filename=test123_1760090252_000.jpg&subfolder=callback&type=output"]
}
```

## 主要接口

- **主页**: http://localhost:6688/
- **API文档**: http://localhost:6688/docs
- **状态**: http://localhost:6688/status
- **日志**: http://localhost:6688/logs

## 参数说明

- `task_uuid`: 任务唯一标识符
- `callback_url`: 回调地址
- `save_images`: 是否保存图片（默认：true）
- `output_path`: 输出目录（默认：callback）
- `image_format`: 图片格式（默认：JPEG）
- `quality`: 图片质量（默认：95）

## 故障排除

1. **节点不显示**: 检查 ComfyUI 是否重启
2. **回调失败**: 检查回调服务器是否启动
3. **文件保存失败**: 检查输出目录权限

## 项目信息

- **仓库**: [https://github.com/upseem/comfyui_callback.git](https://github.com/upseem/comfyui_callback.git)
- **语言**: Python 100%
- **许可证**: MIT License