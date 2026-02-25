# ComfyUI-Image-Embeddings

## 项目简介

本项目为 **ComfyUI** 提供一组实用的自定义节点，主要功能包括：

- **CustomImageLoader**：支持从本地路径或 URL 加载单张或批量图像，自动处理透明通道并返回 `IMAGE`、`MASK` 与文件名。
- **Image2Base64**：将 `IMAGE` 张量转为 Base64 编码的 JSON 字符串，便于在外部系统中传输图像数据。
- **VisionOutputEmbedding2JSON**：将 ComfyUI 的 CLIP Vision 输出（`CLIP_VISION_OUTPUT`）转换为可读的 JSON，支持后续分析或存储。
- **ImageHash**：基于 `imagehash` 库计算图像的哈希值（64 位有符号整数），返回 `STRING` JSON。
- **Base64ImageLoader**：从 Base64 编码字符串恢复图像，返回 `IMAGE`、`MASK` 与文件名。

这些节点可直接在 ComfyUI 工作流中使用，帮助你在图像预处理、特征导出以及数据序列化等场景下提升开发效率。

## 安装

```bash
# 1. 克隆仓库（或使用 ComfyUI-Manager 安装）
git clone https://github.com/baijunty/comfyui_image_embeddings.git
# 2. 进入目录并进行可编辑安装
cd comfyui_image_embeddings
pip install -e .[dev]   # 包含开发依赖
# 3. 安装 pre-commit（可选）
pre-commit install
```

> **提示**：如果你使用 **ComfyUI‑Manager**，只需在管理器中搜索 `image_embeddings` 并安装。

## 节点使用说明

### 1. `CustomImageLoader`

| 参数 | 类型 | 说明 |
|------|------|------|
| `image_path_or_url` | `STRING` | 支持本地相对/绝对路径、URL，或指向目录的路径。目录时会一次性加载该目录下所有图片。 |

返回值：

- `IMAGE`：图像张量（`[B, H, W, C]`）
- `MASK`：对应的遮罩张量
- `STRING`：文件名（或 URL 中的文件名）

**示例**：

```python
# 加载单张图片
loader = CustomImageLoader()
image, mask, name = loader.load_image("images/example.png")

# 加载目录
images, masks, names = loader.load_image("images/")
```

### 2. `Image2Base64`

| 参数 | 类型 | 说明 |
|------|------|------|
| `images` | `IMAGE` | 输入图像张量 |
| `names`  | `STRING` | 对应文件名（可列表） |

返回：

- `STRING`：包含 `{filename: base64}` 键值对的 JSON 字符串

**示例**：

```python
base64_str = Image2Base64().image_to_base64(images, names)[0]
```

### 3. `VisionOutputEmbedding2JSON`

| 参数 | 类型 | 说明 |
|------|------|------|
| `vision_output` | `CLIP_VISION_OUTPUT` | 来自 CLIP Vision 节点的输出 |
| `name` | `STRING` | 用作 JSON 键名 |

返回：

- `STRING`：`{"<name>": [embedding...]}` 的 JSON 字符串

### 4. `ImageHash`

| 参数 | 类型 | 说明 |
|------|------|------|
| `images` | `IMAGE` | 输入图像张量 |
| `names`  | `STRING` | 文件名（可列表） |

返回：

- `STRING`：`{"<filename>": <hash>}` 的 JSON 字符串

### 5. `Base64ImageLoader`

| 参数 | 类型 | 说明 |
|------|------|------|
| `base64_string` | `STRING` | 单张图像的 Base64 编码 |
| `name` | `STRING` | 文件名（仅用于返回） |

返回：

- `IMAGE`、`MASK`、`STRING`（文件名）

## 开发与测试

```bash
# 运行单元测试
pytest -q
# 代码检查（ruff）
ruff check .
```

项目已配置 GitHub Actions，会在每次 push 时运行测试与代码格式检查。

## 贡献

欢迎提交 Pull Request，或在 **Discord**（https://discord.com/invite/comfyorg）讨论新功能。若要发布到 ComfyUI Registry，请参考 `pyproject.toml` 中的 `tool.comfy` 配置，并在 Registry 创建 API Token。

---

> 本项目基于 [cookiecutter-comfy-extension](https://github.com/Comfy-Org/cookiecutter-comfy-extension) 模板创建，旨在提供即插即用的图像处理节点。祝你玩得开心！
