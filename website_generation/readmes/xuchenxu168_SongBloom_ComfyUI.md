# ComfyUI SongBloom 插件（完整文档）

面向 ComfyUI 的 SongBloom 音乐生成插件，集成歌词规范、模型加载、生成、保存与预览等全流程能力，并提供 DeepSeek V3 辅助“歌词格式化”。

## 亮点功能

- **端到端歌曲生成**：最长约 150s（取决于模型配置）
- **结构化歌词驱动**：规范的标签格式，生成更稳定
- **参考音频提示**：可选风格参考（自动重采样/裁剪）
- **质量优化预设**：一键切换 Ultra/High/Balanced/Fast
- **低显存保护**：支持低显存模式、自动降级与重试
- **音频工具集**：截取、维度修复、保存与内置预览
- **DeepSeek V3 对齐实现**：用于“歌词格式转换”的 API 节点，支持从 JSON/环境变量读取 Key

## Installation

### Prerequisites

- ComfyUI installed and working
- Python 3.8 or higher
- CUDA-compatible GPU (recommended)
- At least 8GB VRAM for float32, 6GB for bfloat16

### Step 1: Clone the Plugin

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/your-repo/ComfyUI_SongBloom.git
```

### Step 2: Install Dependencies（依赖安装）

```bash
cd ComfyUI_SongBloom
pip install -r requirements.txt
```

### Step 3: 安装脚本（可选）

```bash
cd ComfyUI_SongBloom
python install.py
```

This script will:
- Check system requirements
- Verify dependencies
- Set up model directories
- Test SongBloom components

## 模型设置

### 模型下载链接（参考官方仓库）

下表与官方仓库的“Models”保持一致，便于直接跳转下载模型文件。[官方仓库链接](https://github.com/tencent-ailab/SongBloom)

| 名称 | 规模 | 最长时长 | 提示类型 | 下载/说明 |
| --- | --- | --- | --- | --- |
| songbloom_full_150s | 2B | 2m30s | 10s wav | [HuggingFace](https://huggingface.co/CypressYang/SongBloom) |
| songbloom_full_150s_dpo | 2B | 2m30s | 10s wav | [HuggingFace](https://huggingface.co/CypressYang/SongBloom) |

说明：当前两个版本权重均托管在同一模型卡页面，请在页面内选择对应的 `.pt` 与配置文件。


#### 本地模型（推荐）

如果您已经有本地模型文件，请将它们放置在以下目录：

```
ComfyUI/models/SongBloom/
├── songbloom_full_150s.pt              # 基础模型
├── songbloom_full_150s_dpo.pt          # DPO微调模型（推荐）
├── songbloom_full_150s.yaml            # 配置文件（可选）
├── songbloom_full_150s_dpo.yaml        # 配置文件（可选）
├── stable_audio_1920_vae.json          # VAE配置
├── autoencoder_music_dsp1920.ckpt      # VAE权重
└── vocab_g2p.yaml                      # G2P词汇表
```

**支持的模型文件：**
- `songbloom_full_150s.pt`: 基础模型 (2B参数)
- `songbloom_full_150s_dpo.pt`: DPO微调模型 (推荐使用)

### 自动下载模型

如果没有本地模型，插件会自动从HuggingFace Hub下载。确保有网络连接。

**下载的文件：**
- 模型权重 (.pt文件)
- 配置文件 (.yaml)
- VAE组件
- G2P词汇文件

总下载大小: ~8GB

### 加载模式

在`SongBloomModelLoader`节点中，您可以选择不同的加载模式：

- **local_first** (默认): 优先使用本地模型，如果不存在则下载
- **local_only**: 仅使用本地模型，不下载
- **download_only**: 强制从网络下载

### 自动配置修复

插件包含智能配置修复功能，会自动处理常见的配置问题：

- **VAE配置自动修复**: 自动检测和配置VAE设置，解决"Missing key vae"错误
- **文件智能匹配**: 支持多种文件名和扩展名（`.pt`, `.ckpt`, `.pth`）
- **详细错误日志**: 提供清晰的修复过程信息

## 音频质量优化

### 质量配置节点（SongBloomQualityConfig）

新增的 `SongBloomQualityConfig` 节点提供专业级音频质量优化：

#### **质量预设**
- **Ultra High**: CFG=4.0, Steps=200, Top_k=50 - 最高质量，适合最终作品
- **High**: CFG=3.0, Steps=100, Top_k=100 - 高质量，日常推荐
- **Balanced**: CFG=2.0, Steps=75, Top_k=150 - 质量与速度平衡
- **Fast**: CFG=1.5, Steps=50, Top_k=200 - 快速生成，适合测试

#### **参数说明**
- **CFG系数**: 控制对歌词的遵循程度，越高质量越好但生成时间越长
- **推理步数**: 扩散模型去噪步数，越多细节越丰富
- **Top_k采样**: 限制采样候选数，越低越稳定

#### **使用方法**
1. 添加 `SongBloomQualityConfig` 节点
2. 选择质量预设或自定义参数
3. 连接到 `SongBloomGenerator` 的 `quality_config` 输入
4. 生成高质量音频

### 质量优化建议

**如果音频质量不佳，请尝试：**
- 使用 "High" 或 "Ultra High" 质量预设
- 确保歌词格式规范（使用 `SongBloomLyricProcessor` 验证）
- 提高CFG系数到3.0以上
- 增加推理步数到100以上
- 降低Top_k值到100以下

详细的质量优化指南请参考：[音频质量优化指南.md](音频质量优化指南.md)

## 快速开始

### 基础工作流

1. **加载模型**: 使用 `SongBloomModelLoader` 加载SongBloom模型
   - 选择模型: `songbloom_full_150s` 或 `songbloom_full_150s_dpo` (推荐)
   - 选择加载模式: `local_first` (优先本地), `local_only` (仅本地), `download_only` (仅下载)
   - 选择数据类型: `float32` (高质量) 或 `bfloat16` (节省显存)

2. **处理歌词**: 使用 `SongBloomLyricProcessor` 格式化歌词
   - 支持中文和英文歌词
   - 自动验证歌词格式
   - 提供格式建议和错误修正

3. **准备音频提示**: 使用 `SongBloomAudioPrompt` 选择音频风格参考 (可选)
   - **智能文件选择**: 下拉菜单自动显示系统中的音频文件
   - **多目录搜索**: 自动搜索音乐文件夹、桌面、ComfyUI输入目录等
   - **格式支持**: WAV, FLAC, MP3, OGG, M4A, AAC等格式
   - **自动处理**: 自动重采样到48kHz，调整到10秒长度
   - **可选使用**: 选择"无 (不使用音频提示)"可跳过音频风格参考

4. **生成歌曲**: 使用 `SongBloomGenerator` 创建歌曲
   - 可调节CFG系数、步数等参数
   - 支持不同质量设置
   - 显示生成进度和信息

5. **保存音频与预览**: 使用 `SongBloomAudioSaver` 保存结果（节点面板会显示预览）
   - 支持FLAC, WAV, MP3格式
   - 自动文件命名和时间戳
   - 可自定义输出目录
   - **内置音频预览功能** - 保存的同时提供音频预览输出

6. **音频预览**: 使用 `SongBloomAudioPreview` 试听音频（本插件自带的高级预览器）

### 示例工作流

插件提供了多个示例工作流，位于 `example_workflows/` 目录：

1. **local_quick_start.json** - 快速开始工作流
   - 最简单的本地模型使用示例
   - 预配置参数，开箱即用

2. **audio_file_selection_demo.json** - 音频文件选择演示
   - 展示音频风格参考功能
   - 智能音频文件搜索和选择

3. **audio_playback_demo.json** - 音频播放功能演示 (新增)
   - 展示音频保存和播放功能
   - 包含音频预览和专门的播放器节点
   - 完整的音频处理工作流

## 音频文件选择功能（SongBloomAudioPrompt）

新版本的 `SongBloomAudioPrompt` 节点提供了智能音频文件选择功能：

#### **自动搜索目录**
插件会自动搜索以下目录中的音频文件：

**ComfyUI相关目录:**
- `ComfyUI/input/` - ComfyUI输入目录
- `ComfyUI/models/audio/` - 音频模型目录

**用户常用目录:**
- `~/Music` 或 `~/音乐` - 用户音乐文件夹
- `~/Desktop` - 桌面目录
- `~/Downloads` 或 `~/下载` - 下载文件夹
- `~/Documents/Music` - 文档音乐文件夹

**系统目录 (Windows):**
- `C:/Users/Public/Music` - 公共音乐文件夹
- `C:/Windows/Media` - 系统音频文件夹

**音频软件目录:**
- FL Studio、Audacity等音频软件的文档目录

#### **支持的音频格式**
- WAV (推荐，无损格式)
- FLAC (无损压缩)
- MP3 (有损压缩)
- OGG (开源格式)
- M4A (Apple格式)
- AAC (高效压缩)

#### **使用方法**
1. 在 `SongBloomAudioPrompt` 节点中点击 `audio_file` 下拉菜单
2. 从列表中选择您想要的音频文件作为风格参考
3. 选择 "无 (不使用音频提示)" 可以不使用音频风格参考
4. 插件会自动处理音频文件（重采样、调整长度等）

**智能处理特性**
- 自动搜索多个系统目录
- 智能文件去重和排序
- 自动格式验证和错误提示
- 支持多种音频格式

#### **音频质量建议**
- **最佳长度**: 5-15秒的音频片段
- **推荐格式**: WAV或FLAC无损格式
- **采样率**: 任意采样率（插件会自动转换为48kHz）
- **声道**: 支持单声道和立体声（会自动转换为单声道）

## 歌词格式示例

```
[intro] [intro] [intro] [intro] [intro] [intro] [intro] [intro] [intro] [intro] , 
[verse] City lights flicker through the car window. Dreams pass fast where the lost ones go. Neon signs echo stories untold. I chase shadows while the night grows cold , 
[chorus] Run with me down the empty street. Where silence and heartbeat always meet. Every breath. a whispered vow. We are forever. here and now , 
[inst] [inst] [inst] [inst] [inst] [inst] [inst] [inst] [inst] [inst] [inst] [inst] , 
[verse] Footsteps loud in the tunnel of time. Regret and hope in a crooked rhyme. You held my hand when I slipped through the dark. Lit a match and you became my spark , 
[bridge] We were nothing and everything too. Lost in a moment. found in the view. Of all we broke and still survived. Somehow the flame stayed alive , 
[chorus] Run with me down the empty street. Where silence and heartbeat always meet. Every breath. a whispered vow. We are forever. here and now , 
[outro] [outro] [outro] [outro] [outro] [outro] [outro] [outro] [outro] [outro] [outro]
```

## 节点一览（本插件提供）

### SongBloomModelLoader（模型加载）
加载本地或自动下载的 SongBloom 模型，并支持 dtype/加载模式等设置。

**Inputs:**
- `model_name`: Choose between available models
- `dtype`: Precision (float32/bfloat16)
- `force_reload`: Force re-download of model files

**Outputs:**
- `model`: Loaded SongBloom model

### SongBloomLyricProcessor（歌词处理与校验）

**Inputs:**
- `lyrics`: Multi-line text with structure tags
- `validate_format`: Enable format validation

**Outputs:**
- `processed_lyrics`: Formatted lyrics
- `validation_info`: Validation results

### SongBloomAudioPrompt（参考音频处理）

**Inputs:**
- `audio_path`: Path to audio file
- `audio`: Audio tensor (alternative to path)
- `target_duration`: Duration in seconds (default: 10s)

**Outputs:**
- `processed_audio`: Prepared audio prompt
- `info`: Processing information

### SongBloomGenerator（歌曲生成）

**Inputs:**
- `model`: SongBloom model
- `lyrics`: Processed lyrics
- `audio_prompt`: Audio prompt
- `cfg_coef`: Classifier-free guidance coefficient
- `steps`: Number of diffusion steps
- `top_k`: Top-k sampling parameter
- `seed`: Random seed (-1 for random)

**Outputs:**
- `generated_audio`: Generated song
- `generation_info`: Generation statistics

### SongBloomAudioSaver（音频保存，带节点内预览）

**Inputs:**
- `audio`: Audio to save
- `filename`: Output filename
- `format`: Audio format (FLAC/WAV/MP3)
- `output_dir`: Output directory (optional)
- `enable_preview`: Enable audio preview output (optional)

**Outputs:**
- `file_path`: Path to saved file
- `audio_preview`: Audio preview for playback (when enabled)

### SongBloomAudioPreview（音频预览输出节点）

**Inputs:**
- `audio`: Audio to play
- `title`: Display title for the audio (optional)
- `auto_play`: Enable automatic playback (optional)

**Outputs:**
- `audio`: Pass-through audio for further processing
- `info`: Audio information (duration, sample rate, etc.)

## 歌词格式规范

### Structure Tags
- `[intro]` - Introduction section
- `[verse]` - Verse section with vocals
- `[chorus]` - Chorus section with vocals
- `[bridge]` - Bridge section with vocals
- `[inst]` - Instrumental section
- `[outro]` - Outro section

### Formatting Rules
1. Use structure tags to mark different sections
2. Separate sentences with `.` in vocal sections
3. Separate sections with `,`
4. Repeat tags for longer instrumental sections
5. Include at least one vocal section

## DeepSeek V3（歌词格式转换）

- 节点：`SongBloom DeepSeek Lyric Formatter`
- 实现：使用 OpenAI SDK，`base_url=https://api.deepseek.com`，模型 `DeepSeek-V3`（内部映射为 `deepseek-chat`）
- 读取 API Key 优先级：
  1) 节点输入 `api_key`
  2) 环境变量 `DEEPSEEK_API_KEY`
  3) `DeepseekAP-config.json`（本项目根目录）
  4) `config.yaml` 中 `deepseek.api_key`（兜底）
- JSON 配置文件示例（`DeepseekAP-config.json`）：
```json
{
  "api_key": "sk-xxxxxxxxxxxxxxxxxxxx"
}
```

### DeepSeek API 申请指南与使用说明

1. 申请步骤（以 DeepSeek 官方为准）
   - 前往 DeepSeek 官网注册并完成实名认证（若需）
   - 进入控制台创建 API Key，复制得到形如 `sk-...` 的密钥
   - 建议为本项目单独创建一个 Key，便于额度管理

2. 在本项目中配置 API Key（四选一，按优先级覆盖）
   - 方式 A（节点内最直观）：在 `SongBloom DeepSeek Lyric Formatter` 或 `SongBloom Lyric Generator`（勾选 use_deepseek）节点的 `api_key` 输入框中粘贴 Key
   - 方式 B（环境变量）
     - Windows PowerShell（会话级）：`$env:DEEPSEEK_API_KEY = "sk-xxxx"`
     - 永久：在系统环境变量新增 `DEEPSEEK_API_KEY`
   - 方式 C（推荐）在项目根目录创建/编辑 `DeepseekAP-config.json`：
     ```json
     {
       "api_key": "sk-xxxxxxxxxxxxxxxxxxxx"
     }
     ```
   - 方式 D（兜底）在 `config.yaml` 中新增：
     ```yaml
     deepseek:
       api_key: "sk-xxxxxxxxxxxxxxxxxxxx"
     ```

3. 在工作流中的用法
   - 仅格式化：直接使用 `SongBloom DeepSeek Lyric Formatter`，填入 `prompt`（你的主题/要求），其余保持默认（model 选 `DeepSeek-V3`）
   - 融入生成链：在 `SongBloom Lyric Generator` 勾选 `use_deepseek`，将 `style/mood/language/theme_keywords/user_requirements` 等参数作为上下文传入，由 DeepSeek 生成结构化歌词；本节点会自动做格式清洗与校验
   - 默认系统提示词已内置，保证输出严格遵循 SongBloom 标签格式；如需定制，可在节点的 `deepseek_system_prompt` 中覆盖

4. 常见问题
   - 400/401 错误：通常是 Key 无效或模型名不匹配（本插件已将 `DeepSeek-V3` 映射为 `deepseek-chat`）
   - 代理：若系统设置了 `HTTP_PROXY/HTTPS_PROXY`，SDK 将继承；需要直连时清空相关环境变量
   - 额度：请在 DeepSeek 控制台查看用量与账单，避免因额度不足导致失败

## 工具节点

### SongBloomAudioCropper（音频截取）
- 输入：音频、`start_sec`、`end_sec`、`pad_to_end`
- 输出：裁剪后的音频与信息字符串
- 特性：自动矫正形状为 (channels, samples)，支持空结果兜底（可补 0.01s 静音）

### SongBloomAudioEnsure2D（维度修复）
- 将任意 0D/1D/3D/列表/ndarray 规约为 2D `(channels, samples)`，并保证 CPU/contiguous
- 建议在使用非本插件的保存节点前串联，避免“Dimension out of range”

## 生成与显存优化

### 低显存模式（SongBloomGenerator 可选项）
- `low_memory_mode`：启用后在 OOM 时自动清缓存、降步数/CFG/增大 top_k，并可重试
- `max_memory_retries`：最大重试次数（默认 2）
- `prompt_max_seconds`：限制参考音频最长秒数（默认 10），超出会裁剪

### 建议参数
- 紧张显存：`bfloat16` + `steps 40~60` + `cfg 1.5~2.0` + `prompt_max_seconds 5`
- 高质量：`float32` + `steps ≥100` + `cfg 3.0`

### 额外提示（与官方实现一致的显存管理）
- 在底层生成循环开始前会显式调用一次 `torch.cuda.empty_cache()`，以释放碎片显存。
- `max_frames` 值越大峰值显存越高，建议根据目标时长调节；显存紧张时将其下调（如 7500 或更低）。

## 故障排查（Troubleshooting）
### Common Issues

**"SongBloom dependencies not available"**
- Install requirements: `pip install -r requirements.txt`
- Ensure all dependencies are properly installed

**"CUDA out of memory"**
- Use `bfloat16` dtype instead of `float32`
- Reduce batch size or song length
- Close other GPU-intensive applications

**"Model download failed"**
- Check internet connection
- Verify HuggingFace Hub access
- Try force reload option

### Performance Tips

- Use `bfloat16` for lower VRAM usage
- Start with shorter songs for testing
- Use lower step counts for faster generation
- Enable flash attention if available

### Advanced Usage

#### Custom Model Paths
You can specify custom model cache directories by modifying the `cache_dir` in the model loader.

#### Batch Processing
使用 `SongBloomBatchProcessor` 可批量生成多首歌曲（同一模型/提示，不同歌词）。

#### Quality Settings
- **High Quality**: `steps=100`, `cfg_coef=2.0`, `dtype=float32`
- **Balanced**: `steps=50`, `cfg_coef=1.5`, `dtype=bfloat16` (default)
- **Fast**: `steps=25`, `cfg_coef=1.0`, `dtype=bfloat16`

#### Memory Optimization
For systems with limited VRAM:
1. Use `bfloat16` dtype
2. Reduce `max_frames` in advanced config
3. Close other GPU applications
4. Consider using CPU offloading (slower but uses less VRAM)

## 故障排除

### 常见问题

#### 1. 模型加载失败
**问题**: "Model file not found" 或 "Failed to load model"
**解决方案**:
- 确保模型文件位于 `ComfyUI/models/SongBloom/` 目录
- 检查文件名是否正确: `songbloom_full_150s.pt` 或 `songbloom_full_150s_dpo.pt`
- 尝试使用 `download_only` 模式重新下载模型
- 运行 `python test_local_models.py` 检查模型状态

#### 1.1. OmegaConf Resolver错误
**问题**: "resolver 'eval' is already registered"
**解决方案**:
- 这是多次加载模型时的常见问题，已在v1.1.0中修复
- 重启ComfyUI应用修复
- 现在支持多次加载和切换模型
- 如果仍有问题，运行 `python test_model_loading.py` 验证修复

#### 2. 显存不足
**问题**: "CUDA out of memory"
**解决方案**:
- 使用 `bfloat16` 数据类型
- 减少生成步数 (steps)
- 关闭其他GPU应用程序
- 降低 `max_frames` 参数

#### 3. 歌词格式错误
**问题**: "Invalid lyric format" 或生成质量差
**解决方案**:
- 使用 `SongBloomLyricValidator` 检查歌词格式
- 确保包含必要的结构标签: `[intro]`, `[verse]`, `[chorus]`, `[outro]`
- 参考示例歌词格式
- 每个部分用逗号分隔

#### 4. 音频提示问题
**问题**: 音频加载失败或格式不支持
**解决方案**:
- 确保音频文件存在且可读
- 支持的格式: WAV, FLAC, MP3, OGG
- 音频长度建议5-15秒
- 使用 `SongBloomAudioAnalyzer` 检查音频质量

#### 5. 生成速度慢
**问题**: 生成时间过长
**解决方案**:
- 减少生成步数 (25-50步通常足够)
- 使用 `bfloat16` 数据类型
- 确保使用GPU而非CPU
- 检查CUDA版本兼容性

### 性能优化建议

1. **首次使用**: 选择 `local_first` 模式，让插件自动处理模型加载
2. **显存优化**: 使用 `bfloat16` + 50步数 + CFG系数1.5
3. **质量优化**: 使用 `float32` + 100步数 + CFG系数2.0
4. **速度优化**: 使用 `bfloat16` + 25步数 + CFG系数1.0

## License
遵循上游 SongBloom 项目的相同协议，详见仓库 LICENSE。

## Citation

If you use this plugin in your research, please cite the original SongBloom paper:

```bibtex
@article{yang2025songbloom,
title={SongBloom: Coherent Song Generation via Interleaved Autoregressive Sketching and Diffusion Refinement},
author={Yang, Chenyu and Wang, Shuai and Chen, Hangting and Tan, Wei and Yu, Jianwei and Li, Haizhou},
journal={arXiv preprint arXiv:2506.07634},
year={2025}
}
```

## Contributing
欢迎提交 Issue/PR 参与共建。

## Support
若遇到问题：
- 先参考本文"故障排查/性能优化"章节
- 查看 `example_workflows/` 示例工作流
- 反馈具体日志与截图，便于定位

## 联系方式
如有技术问题或合作需求，欢迎通过微信联系：

![微信二维码](https://img.shields.io/badge/微信-扫码联系-brightgreen?style=for-the-badge&logo=wechat&logoColor=white)

<div align="center">
  <img src="https://github.com/xuchenxu168/images/blob/main/%E5%BE%AE%E4%BF%A1%E5%8F%B7.jpg" alt="微信二维码" width="200" height="200">
  <p><em>扫码添加微信，备注"SongBloom"</em></p>
</div>
