# ComfyUI_Float_Animator

A custom node package for ComfyUI that integrates the powerful [FLOAT](https://github.com/deepbrainai-research/float) project, enabling audio-driven talking portrait video generation directly within your ComfyUI workflow.


---
---

## Nodes

*   **Float_Animator**: Generates speaking portrait video frames from an image and audio.

## Node Descriptions

### 1. Float_Animator

*   **Function**: Takes a still portrait image and an audio file to generate a sequence of animated frames, synchronizing lip movements and allowing emotion control based on the FLOAT model.
*   **Key Inputs**:
    *   `ref_image`: (IMAGE) The still portrait image to animate.
    *   `audio`: (AUDIO) The driving audio to synchronize with the portrait.
    *   `seed`: (INT) Random seed for reproducibility of results, with "control after generate" options.
    *   `emotion`: (ENUM) Specify a target emotion style. Choose 'none' to infer emotion from the driving audio.
    *   `fps`: (FLOAT) Frames per second for the output animation.
    *   `aud_cfg_scale`: (FLOAT) Classifier-free guidance scale for audio control (default: 2.0).
    *   `ref_cfg_scale`: (FLOAT) Classifier-free guidance scale for reference image control (default: 1.0).
    *   `emo_cfg_scale`: (FLOAT) Classifier-free guidance scale for emotion control (default: 1.0).
    *   `model`: (COMBO) Select the FLOAT main model file (.pth) to use from `ComfyUI/models/Float/`.
    *   `auto_crop`: (BOOLEAN) Automatically crop the face in the reference image. (Default: Off, enables black padding if needed)
*   **Outputs**:
    *   `animated_frames`: (IMAGE) The generated sequence of animated image frames (ComfyUI standard `IMAGE` format for video output).
    *   `audio`: (AUDIO) The input audio object passed through.
    *   `fps`: (FLOAT) The frames per second used for the output animation.
*   **Usage**: Connect a `Load Image` node to `ref_image` and a `Load Audio` node to `audio`. Select your desired FLOAT model from the `model` dropdown. Adjust `fps`, guidance scales (`aud_cfg_scale`, `ref_cfg_scale`, `emo_cfg_scale`), `emotion`, and `auto_crop` as needed. Set a `seed` for reproducible results. The output `animated_frames` can be connected to `Save Image` for an image sequence or a `Video Combine` node (e.g., `VHS_VideoCombine`) to create a video. The `audio` output can be passed to audio-related nodes, and `fps` output can be used to drive video combining nodes.

![image](https://github.com/KERRY-YUAN/ComfyUI_Float_Animator/blob/main/Examples/ComfyUI_Float_Animator.png)
![image](https://github.com/KERRY-YUAN/ComfyUI_Float_Animator/blob/main/Examples/Spark_TTS_&_Float_Animator.png)
---
---

## Installation Steps

1.  **Navigate to ComfyUI `custom_nodes` directory:**
    ```bash
    cd path/to/your/ComfyUI/custom_nodes
    ```
2.  **Clone this repository:**
    ```bash
    git clone https://github.com/KERRY-YUAN/ComfyUI_Float_Animator.git ComfyUI_Float_Animator
    cd ComfyUI_Float_Animator
    ```
3.  **Install Dependencies:**
    Install the required Python libraries using your ComfyUI Python environment.
    ```bash
    # Example for ComfyUI's embedded Python on Windows:
    # path/to/your/ComfyUI/python_embeded/python.exe -m pip install -r requirements.txt
    # 
    # Or for a system-wide/venv Python:
    pip install -r requirements.txt
    ```
    *Note: Ensure `torch` and `torchaudio` versions are compatible with your system and ComfyUI's existing PyTorch installation.*

## 📥 Model and Data Setup

The FLOAT model and its associated data **must be placed in specific default locations** for the node to function correctly. **This node package now supports automatic model download when the node is executed for the first time or if models are missing.** You can also use the `Model_Download.bat` script provided with this node package to download and place them automatically beforehand.


1.  **Model Location:**
    The `float.pth` main model, `wav2vec2-base-960h` folder, and `wav2vec-english-speech-emotion-recognition` folder must be located at: `ComfyUI/models/Float/`
	`float.pth`: https://drive.google.com/file/d/1rvWuM12cyvNvBQNCLmG4Fr2L1rpjQBF0/view?usp=sharing
	`wav2vec2-base-960h`: https://huggingface.co/facebook/wav2vec2-base-960h
	`wav2vec-english-speech-emotion-recognition`: https://huggingface.co/r-f/wav2vec-english-speech-emotion-recognition

2.  **Automatic Download (Node Execution):**
    Simply open the `Float_Animator` node in ComfyUI. If the required models are not found, the node will initiate their download automatically.

3.  **Manual Download (Optional / Troubleshooting):**
    If the automatic download within ComfyUI fails, or you prefer to pre-download models, navigate to the `ComfyUI_Float_Animator` directory and run the provided batch script:
    ```bash
    cd ComfyUI/custom_nodes/ComfyUI_Float_Animator
    .\Model_Download.bat # Run this script on Windows
    ```
    (For Linux/macOS users, refer to the `Model_Download.bat` content or the original FLOAT repository for manual download commands, or run `python model_download/model_download.py` directly).

4.  **Directory Structure Reference:**
    The required final file structure is:

    ```
    ComfyUI/
    ├── custom_nodes/
    │   └── ComfyUI_Float_Animator/
    │       ├── models/             # FLOAT's internal model definitions
    │       │   ├── float/          
    │       │   │   ├── encoder.py
    │       │   │   ├── FLOAT.py
    │       │   │   ├── FMT.py
    │       │   │   ├── generator.py
    │       │   │   ├── styledecoder.py
    │       │   │   └── __init__.py
    │       │   ├── wav2vec2.py
    │       │   ├── wav2vec2_ser.py
    │       │   └── __init__.py
    │       ├── model_download/     # Model download scripts and configuration
    │       │   ├── model_download.py
    │       │   ├── model_list.json # Model list in JSON format
    │       │   └── __init__.py
    │       ├── options/
    │       ├── Node.py
    │       ├── Model_Download.bat  # Manual download script
    │       ├── requirements.txt
    │       └── ... (other package files)
    └── models/
        └── Float/
            ├── float.pth                           # Main FLOAT model checkpoint
            ├── wav2vec2-base-960h/                 # Audio encoder model folder
            │   └── ... (files from Hugging Face)
            └── wav2vec-english-speech-emotion-recognition/  # Emotion encoder model folder
                └── ... (files from Hugging Face)
    ```


## 💡 Optimization Tips for Synthesis Quality

*   **Frontal Head Pose**: The FLOAT model performs best on images with a frontal head pose. Non-frontal images may lead to suboptimal results.
*   **Face Cropping**: The `auto_crop` option is now *off* by default. If your reference image contains a full head shot that might benefit from automatic cropping and scaling (which may introduce black padding regions around the face), you should enable this option. The original FLOAT project recommends cropping for optimal results.
*   **Audio Quality**: For best lip-sync and emotion generation, use clean audio with minimal background music. Tools like [ClearVoice](https://github.com/modelscope/ClearerVoice-Studio) can help in extracting vocals.

## ❗ License ❗

This ComfyUI node wrapper's code is released under the MIT License (see `LICENSE.md` in this repository).

**However, the underlying FLOAT model and its core inference code (including files in the `models/` and `options/` directories, and parts adapted from the official `generate.py`) are released under the [Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International Public License (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).**

**This means the underlying FLOAT technology cannot be used for commercial purposes and no adaptations are permitted (beyond necessary technical integration for framework compatibility).** 请查阅 `LICENSE.md` 文件了解完整详情。

For commercial inquiries regarding the original FLOAT project, please contact `daniel@deepbrain.io` as per their official repository.

## 🙏 Acknowledgements

This project is a ComfyUI wrapper around the excellent work by Taekyung Ki, Dongchan Min, and Gyeongsu:
```bibtex
@article{ki2024float,
  title={FLOAT: Generative Motion Latent Flow Matching for Audio-driven Talking Portrait},
  author={Ki, Taekyung and Min, Dongchan and Chae, Gyeongsu},
  journal={arXiv preprint arXiv:2412.01064},
  year={2024}
}
```
We are grateful to the original authors for their valuable contributions and for open-sourcing their code. We thank the developers of the original [FLOAT](https://github.com/deepbrainai-research/float) project for the powerful model and library components used in this node.

---
---

# ComfyUI_Float_Animator (中文)

一个用于 ComfyUI 的自定义节点包，集成了强大的 [FLOAT](https://github.com/deepbrainai-research/float) 项目，可以直接在 ComfyUI 工作流中实现音频驱动的说话肖像视频生成。

<div align="center">
  <video src="https://github.com/user-attachments/assets/36626b4a-d3e5-4db9-87a7-ca0e949daee0" /> <!-- 引用示例视频 -->
</div>

---
---

## 节点列表

*   **Float_Animator**: 由肖像生成音频驱动的说话视频。

## 节点说明

### 1. Float_Animator

*   **功能**: 接收一张静态肖像图像和一个音频文件，基于 FLOAT 模型生成一系列动画帧，同步唇部动作并支持情感控制。
*   **主要输入**:
    *   `ref_image`: (图像) 用于动画的静态肖像图像。
    *   `audio`: (音频) 驱动肖像动画的音频。
    *   `seed`: (整数) 用于结果复现的随机种子，带有“生成后控制”选项。
    *   `emotion`: (枚举) 指定目标情感风格。选择 'none' 将从驱动音频中推断情感。
    *   `fps`: (浮点数) 输出动画的每秒帧数。
    *   `aud_cfg_scale`: (浮点数) 音频控制的无分类器引导尺度（默认值：2.0）。
    *   `ref_cfg_scale`: (浮点数) 参考图像控制的无分类器引导尺度（默认值：1.0）。
    *   `emo_cfg_scale`: (浮点数) 情感控制的无分类器引导尺度（默认值：1.0）。
    *   `model`: (组合框) 从 `ComfyUI/models/Float/` 目录中选择要使用的 FLOAT 主模型文件 (.pth)。
    *   `auto_crop`: (布尔值) 自动裁剪参考图像中的人脸。 （默认：关闭，可能需要时启用黑色填充）
*   **输出**:
    *   `animated_frames`: (图像) 生成的动画图像帧序列（ComfyUI 标准 `IMAGE` 格式用于视频输出）。
    *   `audio`: (音频) 输入的音频对象。
    *   `fps`: (浮点数) 输出动画的每秒帧数。
*   **用法**: 将 `Load Image` 节点连接到 `ref_image`，将 `Load Audio` 节点连接到 `audio`。从 `model` 下拉列表中选择您想要使用的 FLOAT 模型。根据需要调整 `fps`、引导尺度（`aud_cfg_scale`、`ref_cfg_scale`、`emo_cfg_scale`）、`emotion` 和 `auto_crop`。设置 `seed` 以便结果可复现。输出的 `animated_frames` 可以连接到 `Save Image` 节点以保存图像序列，或连接到 `Video Combine` 节点（例如 `VHS_VideoCombine`）以创建视频。输出的 `audio` 可以传递给音频相关节点，`fps` 输出可以用于驱动视频合成节点。

![image](https://github.com/KERRY-YUAN/ComfyUI_Float_Animator/blob/main/Examples/ComfyUI_Float_Animator.png)
![image](https://github.com/KERRY-YUAN/ComfyUI_Float_Animator/blob/main/Examples/Spark_TTS_&_Float_Animator.png)
---
---

## 安装步骤

1.  **导航到 ComfyUI `custom_nodes` 目录：**
    ```bash
    cd path/to/your/ComfyUI/custom_nodes
    ```
2.  **克隆此仓库：**
    ```bash
    git clone https://github.com/KERRY-YUAN/ComfyUI_Float_Animator.git ComfyUI_Float_Animator
    cd ComfyUI_Float_Animator
    ```
3.  **安装依赖项：**
    使用您的 ComfyUI Python 环境安装所需的 Python 库。
    ```bash
    # Windows 上 ComfyUI 嵌入式 Python 示例:
    # path/to/your/ComfyUI/python_embeded/python.exe -m pip install -r requirements.txt
    # 
    # 或者对于系统级/虚拟环境 Python:
    pip install -r requirements.txt
    ```
    *注意：请确保 `torch` 和 `torchaudio` 版本与您的系统以及 ComfyUI 现有的 PyTorch 安装兼容。*

## 📥 模型和数据设置

FLOAT 模型及其相关数据**必须放置在特定的默认位置**，节点才能正常工作。此节点包现在支持**在首次加载节点或模型缺失时自动下载模型**。 你也可以使用此节点包提供的 Model_Download.bat 脚本预先自动下载并放置模型。

1.  **模型位置：**
    `float.pth` 主模型、`wav2vec2-base-960h` 文件夹和 `wav2vec-english-speech-emotion-recognition` 文件夹必须位于：`ComfyUI/models/Float/`
	`float.pth`：https://drive.google.com/file/d/1rvWuM12cyvNvBQNCLmG4Fr2L1rpjQBF0/view?usp=sharing
	`wav2vec2-base-960h`：https://huggingface.co/facebook/wav2vec2-base-960h
	`wav2vec-english-speech-emotion-recognition`：https://huggingface.co/r-f/wav2vec-english-speech-emotion-recognition

2.  **节点内自动下载：**
    在 ComfyUI 中加载工作流 `Float_Animator` 节点。节点会自动检查并下载所需的模型。请耐心等待下载完成，这可能需要一段时间。下载完成后，您可以重新加载页面或刷新节点以确保模型被正确加载。

3.  **手动下载（可选/故障排除）：**
    如果节点内的自动下载过程失败，或者您希望提前下载所有模型，请导航到 `ComfyUI_Float_Animator` 目录并运行提供的批处理脚本：
    ```bash
    cd ComfyUI/custom_nodes/ComfyUI_Float_Animator
    .\Model_Download.bat # 在 Windows 上运行此脚本
    ```
    （对于 Linux/macOS 用户，请参考 `Model_Download.bat` 的内容或原始 FLOAT 仓库以获取手动下载命令，或者直接运行 `python model_download/model_download.py`）。

4.  **目录结构参考：**
    必需的最终文件架构如下：

    ```
    ComfyUI/
    ├── custom_nodes/
    │   └── ComfyUI_Float_Animator/
    │       ├── models/             # FLOAT 的内部模型定义
    │       │   ├── float/          
    │       │   ├── wav2vec2.py
    │       │   ├── wav2vec2_ser.py
    │       │   └── __init__.py
    │       ├── model_download/     # 模型下载脚本和配置文件
    │       │   ├── model_download.py
    │       │   ├── model_list.json # 模型列表（JSON 格式）
    │       │   └── __init__.py
    │       ├── options/
    │       │   ├── base_options.py
    │       │   └── __init__.py
    │       ├── Node.py
    │       ├── Model_Download.bat  # 手动下载脚本
    │       ├── requirements.txt
    │       └── ... (其他包内文件)
    └── models/
        └── Float/
            ├── float.pth                           # 主 FLOAT 模型检查点
            ├── wav2vec2-base-960h/                 # 音频编码器模型文件夹
            │   └── ... (Hugging Face 文件)
            └── wav2vec-english-speech-emotion-recognition/  # 情感编码器模型文件夹
                └── ... (Hugging Face 文件)
    ```

## 💡 合成质量优化提示

*   **正面头部姿态**: FLOAT 模型在正面头部姿态的图像上表现最佳。非正面图像可能会导致效果不佳。
*   **人脸裁剪**: `auto_crop` 选项现在默认处于**关闭**状态。如果您的参考图像是完整的头部照片，并且可能从自动裁剪和缩放中受益（这可能会在人脸周围引入黑色填充区域），您应该**启用**此选项。原始的 FLOAT 项目建议裁剪以获得最佳效果。
*   **音频质量**: 为了获得最佳的唇形同步和情感生成效果，请使用干净的音频，避免背景音乐过重。像 [ClearVoice](https://github.com/modelscope/ClearerVoice-Studio) 这样的工具可以帮助提取人声。

## ❗ 许可证 ❗

此 ComfyUI 节点封装器的代码根据 MIT 许可证发布（详见此仓库中的 `LICENSE.md`）。

**然而，底层的 FLOAT 模型及其核心推理代码（包括 `models/` 和 `options/` 目录中的文件，以及从官方 `generate.py` 改编的部分）根据 [知识共享署名-非商业性-禁止演绎 4.0 国际公共许可证 (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/) 发布。**

**这意味着底层的 FLOAT 技术不能用于商业目的，并且不允许进行改编（除了为框架兼容性而进行的必要技术集成）。** 请查阅 `LICENSE.md` 文件了解完整详情。

有关原始 FLOAT 项目的商业咨询，请按照其官方仓库的说明联系 `daniel@deepbrain.io`。

## 🙏 致谢

此项目是 Taekyung Ki、Dongchan Min 和 Gyeongsu 优秀工作的 ComfyUI 封装：
```bibtex
@article{ki2024float,
  title={FLOAT: Generative Motion Latent Flow Matching for Audio-driven Talking Portrait},
  author={Ki, Taekyung and Min, Dongchan and Chae, Gyeongsu},
  journal={arXiv preprint arXiv:2412.01064},
  year={2024}
}
```
我们感谢原作者的宝贵贡献并开源其代码。感谢原始 [FLOAT](https://github.com/deepbrainai-research/float) 项目的开发者提供了此节点中使用的强大模型和库组件。