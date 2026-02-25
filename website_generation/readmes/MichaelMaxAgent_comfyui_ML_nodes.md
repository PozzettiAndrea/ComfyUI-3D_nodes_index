# ComfyUI Image Saver & Frame Rate Processor

ComfyUI custom nodes for saving images/videos without metadata, processing frame rates with GPU acceleration, and OpenPose skeleton processing.

[中文文档](#中文文档) | [English](#english-documentation)

---

## 中文文档

ComfyUI 自定义节点集合，提供以下功能：
- 保存不含工作流元数据的图片和视频
- GPU 加速的帧率重采样（如 25fps → 16fps）
- 支持多种插值算法
- OpenPose 骨架图像处理（移除头部/面部区域）

### 功能特点

#### 图片/视频保存节点
- **清除元数据**：保存的图片/视频不包含 ComfyUI 工作流数据
- **自定义保存路径**：可指定输出目录（相对路径或绝对路径）
- **完全自定义文件名**：支持两种命名模式
- **时间戳选项**：可选择在文件名中添加时间戳
- **批量处理**：支持批量保存多张图片或视频序列

#### 帧率重采样节点
- **灵活的帧率转换**：支持任意帧率之间的转换（如 25fps → 16fps）
- **GPU 加速**：支持 NVIDIA CUDA 硬件加速，显著提升处理速度
- **多种插值算法**：
  - **blend**：帧混合，平滑过渡（推荐）
  - **minterpolate**：运动补偿插值，高质量
  - **framestep**：简单帧选择，速度最快
- **智能回退**：GPU 失败时自动回退到 CPU 处理
- **多 GPU 支持**：可选择使用特定的 GPU 设备

#### OpenPose 骨架处理节点
- **移除头部区域**：从 OpenPose 骨架图像中移除头部/面部区域
- **支持完整模型**：完全支持 OpenPose Full Model（BODY_25 + FACE_70 + HAND_21×2）
- **智能检测**：自动检测颈部位置和 FACE_70 密集点云区域
- **多种模式**：
  - **auto_detect_neck**：自动检测颈部位置（推荐）
  - **manual_percentage**：手动指定移除百分比
  - **manual_pixels**：手动指定移除像素数
- **精确保留**：保留颈部以下的身体骨架和手部关键点

### 安装方法

#### 方法 1：使用 ComfyUI Manager（推荐）

1. 打开 ComfyUI Manager
2. 搜索 "ML Image Saver" 或 "ML Frame Rate"
3. 点击安装
4. 重启 ComfyUI

#### 方法 2：手动安装

```bash
cd /path/to/ComfyUI/custom_nodes/
git clone https://github.com/yourusername/comfyui_ML_nodes.git
cd comfyui_ML_nodes
pip install -r requirements.txt
```

然后重启 ComfyUI。

#### 方法 3：Git URL 安装

在 ComfyUI Manager 中使用 "Install via Git URL" 功能，输入仓库地址。

### 依赖要求

- Python >= 3.8
- PyTorch (ComfyUI 已包含)
- Pillow >= 9.0.0
- NumPy (ComfyUI 已包含)
- OpenCV (cv2) >= 4.0.0：用于 OpenPose 骨架处理
- **ffmpeg**（必须安装）：用于视频和帧率处理

#### 安装 ffmpeg

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
从 [ffmpeg.org](https://ffmpeg.org/download.html) 下载并添加到 PATH。

**验证安装:**
```bash
ffmpeg -version
```

### 使用方法

#### 1. ML Save Image (No Metadata)

完全不保存任何元数据的图片保存节点。

**输入参数：**
- `images`: 输入图片（IMAGE 类型）
- `output_path`: 输出目录路径（默认："output"）
- `naming_mode`: 命名模式
  - `prefix_number`: 前缀+序号（如 image_00001.png）
  - `custom`: 自定义文件名
- `filename_prefix`: 文件名前缀（prefix_number 模式）
- `custom_filename`: 自定义文件名（custom 模式）
- `start_number`: 起始序号（默认：1）
- `add_timestamp`: 是否添加时间戳

**输出：**
- `saved_path`: 保存路径信息字符串

**使用示例：**
```
prefix_number 模式：
  image_00001.png, image_00002.png, ...

custom 模式：
  my_render.png 或 my_render_1.png, my_render_2.png, ...

添加时间戳：
  image_00001_20251013_143022.png
```

#### 2. ML Save Image (Clean Metadata)

保存带有自定义元数据但不含工作流的图片。

**额外参数：**
- `custom_metadata`: 自定义元数据（多行文本，格式：key=value）

**元数据示例：**
```
Author=Your Name
Description=My artwork
Date=2025-10-13
```

#### 3. ML Save Video (No Metadata)

将图片序列保存为视频文件，不含元数据。

**输入参数：**
- `images`: 图片序列（IMAGE 类型）
- `output_path`: 输出目录
- `naming_mode`: 命名模式（同上）
- `fps`: 帧率（1-120，默认 30）
- `format`: 视频格式
  - `mp4`: H.264 编码（推荐）
  - `webm`: VP9 编码
  - `avi`: MPEG-4 编码
  - `mov`: QuickTime 格式
  - `gif`: 动画 GIF
- `quality`: 视频质量
  - `high`: CRF 18（最佳质量）
  - `medium`: CRF 23（平衡）
  - `low`: CRF 28（小文件）

#### 4. ML Frame Rate Resampler

CPU 版本的帧率重采样节点。

**输入参数：**
- `images`: 图片序列（IMAGE 类型）
- `input_fps`: 输入帧率（默认 25）
- `output_fps`: 输出帧率（默认 16）
- `interpolation_method`: 插值方法
  - `blend`: 帧混合（推荐，速度和质量平衡）
  - `minterpolate`: 运动补偿插值（最高质量，较慢）
  - `framestep`: 帧选择（最快，可能有跳跃）

**输出：**
- `resampled_images`: 重采样后的图片序列（IMAGE 类型）

**使用场景：**
- 将 25fps 的视频转换为 16fps（如 InfiniteTalk 工作流）
- 将 30fps 降为 24fps（电影帧率）
- 提升帧率（如 24fps → 60fps，使用 minterpolate）

#### 5. ML Frame Rate Resampler (GPU)

GPU 加速版本的帧率重采样节点，支持 NVIDIA CUDA。

**额外参数：**
- `gpu_device`: GPU 设备选择
  - `auto`: 自动检测（推荐，优先使用 GPU）
  - `cuda:0`: 使用第一块 GPU
  - `cuda:1`: 使用第二块 GPU
  - `cpu`: 强制使用 CPU

**性能优势：**
- 对于高分辨率图像（1080p+），GPU 加速可提升 3-10 倍速度
- RTX 系列显卡加速效果最明显
- 自动回退：GPU 失败时自动切换到 CPU

**推荐使用场景：**
- 处理大批量图像序列（>25 帧）
- 高分辨率图像（1080p, 4K）
- 需要快速处理的场景
- 多 GPU 工作站可指定特定 GPU

#### 6. ML Remove Pose Head

从 OpenPose 骨架图像中移除头部/面部区域的节点，保留身体和手部骨架。

**输入参数：**
- `images`: OpenPose 骨架图像序列（IMAGE 类型）
- `detection_mode`: 检测模式
  - `auto_detect_neck`: 自动检测颈部位置（推荐）
  - `manual_percentage`: 手动百分比模式
  - `manual_pixels`: 手动像素模式
- `neck_offset`: 颈部偏移量（像素，-100 到 200）
  - 正值：移除更多（向下偏移切割线）
  - 负值：保留更多（向上偏移切割线）
  - 默认：20 像素
- `manual_percentage`: 手动百分比（0-50%，manual_percentage 模式使用）
- `manual_pixels`: 手动像素数（0-1000，manual_pixels 模式使用）
- `detection_threshold`: 骨架检测阈值（0.01-1.0，默认 0.1）

**输出：**
- `images_no_head`: 移除头部后的骨架图像（IMAGE 类型）

**支持的 OpenPose 格式：**
- **BODY_25**: 25 个身体关键点
  - 移除：点 0（鼻子）、15-18（眼睛、耳朵）
  - 保留：点 1（颈部）及以下（2-14, 19-24）
- **OpenPose Full Model**: BODY_25 + FACE_70 + HAND_21×2
  - 移除：FACE_70 的 70 个面部关键点（密集点云）
  - 移除：BODY_25 的面部点
  - 保留：颈部、身体和双手的所有关键点

**使用场景：**
- 去除人脸信息，保护隐私
- 只保留身体姿态和手势动作
- 用于动作捕捉后处理
- ControlNet 姿态控制（无面部）

**检测模式说明：**

1. **auto_detect_neck（推荐）**：
   - 智能识别 FACE_70 密集点云区域
   - 自动定位颈部关键点位置
   - 使用 `neck_offset` 微调切割位置
   - 适用于标准 OpenPose 输出

2. **manual_percentage**：
   - 按图像高度百分比移除顶部区域
   - 例如：18% 表示移除顶部 18% 的区域
   - 适用于特殊角度或非标准姿态

3. **manual_pixels**：
   - 指定从顶部移除的精确像素数
   - 提供最精确的控制
   - 适用于已知固定尺寸的图像

### 技术实现

#### 元数据清除原理

ComfyUI 默认会在 PNG 图片中保存 workflow 和 prompt 信息。本节点通过以下方式清除：
1. 使用 PIL 保存图片时不传递 `pnginfo` 参数
2. 视频保存时使用 ffmpeg 的 `-map_metadata -1` 参数
3. 确保输出文件仅包含图像/视频数据本身

#### 帧率重采样原理

使用 ffmpeg 的高质量滤镜进行帧率转换：

1. **blend 模式**：使用 `fps` 滤镜进行帧混合
   ```
   ffmpeg -framerate 25 -i input_%06d.png -vf "fps=16" output_%06d.png
   ```

2. **minterpolate 模式**：运动补偿插值
   ```
   ffmpeg -framerate 25 -i input_%06d.png \
     -vf "minterpolate='fps=16:mi_mode=mci:mc_mode=aobmc'" output_%06d.png
   ```

3. **GPU 加速**（CUDA）：
   ```
   ffmpeg -hwaccel cuda -hwaccel_device 0 \
     -framerate 25 -i input_%06d.png \
     -vf "hwdownload,format=nv12,fps=16" output_%06d.png
   ```

### 项目结构

```
comfyui_ML_nodes/
├── __init__.py                      # 包入口
├── README.md                        # 说明文档（本文件）
├── requirements.txt                 # Python 依赖
├── LICENSE                          # MIT 许可证
├── pyproject.toml                   # 项目配置
├── src/
│   └── comfyui_ML_nodes/
│       ├── __init__.py              # 模块初始化
│       └── nodes.py                 # 节点实现（5个节点）
└── tests/
    └── ...                          # 测试文件
```

### 常见问题

**Q: 为什么需要清除元数据？**

A: ComfyUI 默认在图片中保存完整的工作流信息，这会：
- 增加文件大小
- 暴露您的工作流程
- 在某些平台上传时可能包含敏感信息

**Q: 清除元数据会影响图片质量吗？**

A: 不会。元数据和图片的实际像素数据是分开存储的，删除元数据不影响图片质量。

**Q: GPU 加速需要什么硬件？**

A: 需要 NVIDIA GPU 和支持 CUDA 的 ffmpeg。大多数 RTX/GTX 系列显卡都支持。可以运行 `ffmpeg -hwaccels` 检查是否支持 cuda。

**Q: 帧率重采样会降低画质吗？**

A:
- **降帧率**（如 25→16）：画质基本不变，blend 模式可能略微柔和
- **升帧率**（如 24→60）：使用 minterpolate 可以生成较自然的中间帧
- 建议使用 blend 模式以获得最佳平衡

**Q: 相对路径从哪里开始计算？**

A: 从 ComfyUI 的运行目录开始（通常是 ComfyUI 的根目录）。

**Q: ffmpeg 必须安装吗？**

A: 是的。视频保存和帧率重采样节点都需要 ffmpeg。图片保存节点和 OpenPose 处理节点不需要。

**Q: RemovePoseHead 节点适用于哪些图像？**

A: 仅适用于 OpenPose 生成的骨架图像（黑色背景上的白色/彩色骨架线条和关键点）。不适用于普通照片或视频。

**Q: 自动检测模式不准确怎么办？**

A: 可以尝试：
1. 调整 `neck_offset` 参数（增大或减小）
2. 调整 `detection_threshold` 参数（降低使检测更敏感）
3. 使用 `manual_percentage` 或 `manual_pixels` 模式手动指定

### 开发

#### 运行测试

```bash
pip install -e .[dev]
pytest tests/
```

#### 代码检查

```bash
ruff check .
```

### 许可证

MIT License - 详见 [LICENSE](LICENSE) 文件

### 贡献

欢迎提交 Issue 和 Pull Request！

请确保：
1. 代码符合项目风格
2. 添加适当的测试
3. 更新相关文档

### 致谢

- ComfyUI 团队提供的优秀框架
- ffmpeg 项目提供的强大视频处理能力

### 更新日志

#### v0.3.0 (2025-12-03)
- 新增：ML Remove Pose Head 节点
- 支持从 OpenPose 骨架图像中移除头部/面部区域
- 支持 OpenPose Full Model（BODY_25 + FACE_70 + HAND_21×2）
- 智能检测 FACE_70 密集点云和颈部位置
- 提供自动检测和手动控制多种模式
- 添加 OpenCV 依赖

#### v0.2.0 (2025-10-13)
- 新增：ML Frame Rate Resampler 节点（CPU 版本）
- 新增：ML Frame Rate Resampler (GPU) 节点（CUDA 加速）
- 新增：ML Save Video (No Metadata) 节点
- 支持多种插值算法（blend, minterpolate, framestep）
- 支持 GPU 硬件加速（NVIDIA CUDA）
- 支持多 GPU 选择
- 智能回退机制（GPU 失败时自动使用 CPU）

#### v0.1.0 (2025-10-10)
- 初始版本
- 实现基本的无元数据保存功能
- 支持两种命名模式：前缀+序号 / 完全自定义
- 支持自定义路径和文件名
- 添加时间戳选项
- 支持自定义清洁元数据模式

---

## English Documentation

ComfyUI custom nodes collection for:
- Saving images/videos without workflow metadata
- GPU-accelerated frame rate resampling (e.g., 25fps → 16fps)
- Multiple interpolation algorithms
- OpenPose skeleton processing (remove head/face region)

### Features

#### Image/Video Saving Nodes
- **Remove Metadata**: Save images/videos without ComfyUI workflow data
- **Custom Save Path**: Specify output directory (relative or absolute paths)
- **Flexible Naming**: Two naming modes supported
- **Timestamp Option**: Optionally add timestamps to filenames
- **Batch Processing**: Save multiple images or video sequences

#### Frame Rate Resampling Nodes
- **Flexible Frame Rate Conversion**: Convert between any frame rates (e.g., 25fps → 16fps)
- **GPU Acceleration**: NVIDIA CUDA hardware acceleration support for significant speedup
- **Multiple Interpolation Algorithms**:
  - **blend**: Frame blending, smooth transitions (recommended)
  - **minterpolate**: Motion-compensated interpolation, highest quality
  - **framestep**: Simple frame selection, fastest
- **Smart Fallback**: Automatically falls back to CPU if GPU fails
- **Multi-GPU Support**: Choose specific GPU devices

#### OpenPose Skeleton Processing Node
- **Remove Head/Face Region**: Remove head and face region from OpenPose skeleton images
- **Full Model Support**: Supports OpenPose Full Model (BODY_25 + FACE_70 + HAND_21×2)
- **Smart Detection**: Auto-detects neck position and FACE_70 dense point cluster
- **Multiple Modes**: Auto-detection, manual percentage, and manual pixel modes
- **Precise Preservation**: Preserves body skeleton and hand keypoints below neck

### Installation

#### Method 1: ComfyUI Manager (Recommended)

1. Open ComfyUI Manager
2. Search for "ML Image Saver" or "ML Frame Rate"
3. Click Install
4. Restart ComfyUI

#### Method 2: Manual Installation

```bash
cd /path/to/ComfyUI/custom_nodes/
git clone https://github.com/yourusername/comfyui_ML_nodes.git
cd comfyui_ML_nodes
pip install -r requirements.txt
```

Then restart ComfyUI.

#### Method 3: Git URL Installation

Use "Install via Git URL" in ComfyUI Manager with the repository URL.

### Requirements

- Python >= 3.8
- PyTorch (included with ComfyUI)
- Pillow >= 9.0.0
- NumPy (included with ComfyUI)
- OpenCV (cv2) >= 4.0.0: For OpenPose skeleton processing
- **ffmpeg** (required): For video and frame rate processing

#### Installing ffmpeg

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**macOS:**
```bash
brew install ffmpeg
```

**Windows:**
Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.

**Verify Installation:**
```bash
ffmpeg -version
```

### Usage

#### Available Nodes

1. **ML Save Image (No Metadata)** - Save images without any metadata
2. **ML Save Image (Clean Metadata)** - Save images with custom metadata (no workflow)
3. **ML Save Video (No Metadata)** - Save image sequences as videos without metadata
4. **ML Frame Rate Resampler** - CPU-based frame rate conversion
5. **ML Frame Rate Resampler (GPU)** - GPU-accelerated frame rate conversion
6. **ML Remove Pose Head** - Remove head/face region from OpenPose skeleton images

See Chinese documentation above for detailed usage instructions.

### Why "ML" Prefix?

The "ML" prefix distinguishes these nodes from other similar nodes in the ComfyUI ecosystem.

### GPU Acceleration

The GPU version supports:
- NVIDIA CUDA acceleration
- Multi-GPU selection (cuda:0, cuda:1, etc.)
- Automatic fallback to CPU on failure
- Significant speedup for high-resolution images

**Performance**: 3-10x faster for 1080p+ images on RTX series GPUs.

### License

MIT License

### Contributing

Issues and Pull Requests are welcome!

### Node List

- `SaveImageNoMetadata` → **ML Save Image (No Metadata)**
- `SaveImageCleanMetadata` → **ML Save Image (Clean Metadata)**
- `SaveVideoNoMetadata` → **ML Save Video (No Metadata)**
- `MLFrameRateResampler` → **ML Frame Rate Resampler**
- `MLFrameRateResampler_GPU` → **ML Frame Rate Resampler (GPU)**
- `RemovePoseHead` → **ML Remove Pose Head**
