# ComfyUI ModelScope API Node

这是一个为ComfyUI设计的自定义节点，它允许用户通过魔搭（ModelScope）的官方API，调用 **FLUX.1-Kontext-Dev**以及 **FLUX.2-Dev** 模型进行图生图（Image-to-Image）操作。


---

### ✨ 功能特性

- **直接的 API 调用**：无需在本地下载模型，直接通过 API 在云端生成图像。
- **完整的参数控制**：支持调整分辨率（宽度和高度）、随机种子（Seed）、采样步数（Steps）和提示词引导系数（Guidance）。
- **内置图床服务**：自动将输入的图像上传到免费图床，以获取可供 API 使用的公开 URL。

### 🖼️ 节点截图

![example-workflow](https://raw.githubusercontent.com/Onionman61/ComfyUI-ModelScope-Kontext/refs/heads/main/exmple.png)

![example-workflow](https://github.com/Onionman61/ComfyUI-ModelScope/blob/main/Exmple2.png)

---

### ⚙️ 安装

#### 方法一：使用 Git

1.  打开一个终端或命令行窗口。
2.  导航到你的 ComfyUI 安装目录下的 `custom_nodes` 文件夹。
    ```bash
    cd /path/to/your/ComfyUI/custom_nodes/
    ```
3.  运行以下命令克隆本仓库：
    ```bash
    git clone https://github.com/Onionman61/ComfyUI-ModelScope.git
    ```
4.  重启 ComfyUI。

#### 方法二：手动下载

1.  点击本页面右上角的 `Code` 按钮，然后选择 `Download ZIP`。
2.  解压下载的 ZIP 文件。
3.  将解压后的文件夹（确保文件夹名为 `ComfyUI-ModelScope`）移动到 ComfyUI 的 `custom_nodes` 目录下。
4.  重启 ComfyUI。

### 🚀 使用方法

1.  在 ComfyUI 中，通过右键菜单或双击搜索 `ModelScope Universal API` 来添加此节点。
2.  将一个图像输出连接到本节点的 `image` 输入。
3.  在 `api_key` 字段中，填入你的 [ModelScope API Key](https://modelscope.cn/my/myaccesstoken)。
4.  在 `prompt` 字段中，输入你想要对图像进行的修改描述。
5.  根据需要调整 `width`, `height`, `seed`, `steps`, 和 `guidance` 参数（调用FLUX2不需要这些参数，传送请求时将自动无视这些参数）。
6.  将节点的 `IMAGE` 输出连接到 `PreviewImage` 或 `SaveImage` 节点以查看结果。

### 🙏 致谢

-   **模型提供方**: [魔搭 ModelScope](https://modelscope.cn/models/MusePublic/FLUX.1-Kontext-Dev/summary)
-   **图片上传服务**: [freeimage.host](https://freeimage.host/)

### 📄 许可证


本项目采用 [MIT License](LICENSE) 开源。





