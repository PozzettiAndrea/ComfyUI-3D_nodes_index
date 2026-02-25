# ComfyUI Vidu API Nodes (comfyui_VIDU_API)

这是一个为 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 设计的自定义节点包，它无缝集成了 [Vidu (生数科技)](https://www.vidu.cn/) 的全系列视频生成API。您可以在 ComfyUI 的可视化工作流中，轻松实现文生视频、图生视频、多参考图视频生成等强大功能。

## ✨ 功能节点

本插件包提供了一套完整的 Vidu API 节点，涵盖了从获取灵感、生成视频到兼容原生工作流的全过程：

* **`comfyui_VIDU_API/推荐提示词`**: 根据一张图片，智能推荐多种视频生成提示词和特效模板。
* **`comfyui_VIDU_API/文生视频`**: 根据文本提示词直接生成视频。
* **`comfyui_VIDU_API/图生视频`**: 以一张图片为基础，结合提示词生成动态视频。
* **`comfyui_VIDU_API/参考生视频`**: 使用1-7张参考图片，生成主体一致的视频。
* **`comfyui_VIDU_API/首尾帧生视频`**: 提供视频的起始和结束画面，让AI智能生成中间的过渡动画。
* **`comfyui_VIDU_API/特色预设`**: 使用官方预设好的高级模板（如“穿搭展示”）快速生成特定效果的视频。

---

## 🚀 安装

推荐使用 `git clone` 进行手动安装，以确保获取最新版本。

1.  打开您的电脑终端或命令行工具。
2.  使用 `cd` 命令进入 ComfyUI 的自定义节点目录：
    ```bash
    # 将 "path/to/your/ComfyUI" 替换为您的真实路径
    cd path/to/your/ComfyUI/custom_nodes/
    ```
3.  运行以下命令克隆本仓库：
    ```bash
    git clone [https://github.com/your_github_username/comfyui_VIDU_API.git](https://github.com/your_github_username/comfyui_VIDU_API.git)
    ```
    *(请将 `https://github.com/your_github_username/comfyui_VIDU_API.git` 替换为您自己的仓库地址)*

  
4.  **完全重启 ComfyUI**。

---

## 🚀 通过ComfyUI Manager安装

<img width="5120" height="2739" alt="image" src="https://github.com/user-attachments/assets/ca0be3b5-5258-4915-9f40-5dae22af9be8" />


## 🔑 配置 API Key

为了您的账户安全，API Key 需要通过配置文件来加载。

获取API方式点击：https://platform.vidu.cn/

1.  进入 `ComfyUI/custom_nodes/comfyui_VIDU_API/` 文件夹。
2.  创建一个名为 `api.json` 的文件。
3.  打开 `api.json` 并填入以下内容：

    ```json
    {
      "api_key": "vda_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    }
    ```
4.  请将 `vda_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx` 替换为您从 Vidu 官方获取的真实 API Key。
5.  保存文件并重启 ComfyUI。节点将会自动读取这个文件。


## 📖 使用示例
### 示例一：基础的图生视频
<img width="1665" height="615" alt="image" src="https://github.com/user-attachments/assets/f21270bf-07e8-42f3-9e37-801ecac4a8ff" />


##  节点说明
### 文生视频
<img width="2657" height="1329" alt="image" src="https://github.com/user-attachments/assets/237e530a-4e99-4a29-86a4-8bef183126b9" />

https://github.com/user-attachments/assets/e6440404-1b15-48cb-adae-2a5fb026737f

### 图生视频
<img width="2392" height="1331" alt="image" src="https://github.com/user-attachments/assets/563e0a83-14fe-4c58-bde1-d261d4816591" />

https://github.com/user-attachments/assets/8c09788b-daba-4fbb-998e-18d57eef2504

### 多参考图生视频
<img width="900" height="1006" alt="image" src="https://github.com/user-attachments/assets/160c7268-cb8c-4518-b520-fca749ff45db" />

<img width="3401" height="1979" alt="image" src="https://github.com/user-attachments/assets/95330bae-0a95-437f-b4c0-daac30c4b931" />

https://github.com/user-attachments/assets/23c6181d-9bcb-40e9-9bb4-5075163419bd





## 📝 未来计划

* [ ] 支持更多 `特色预设` 模板。
* [ ] 增加独立的 `取消任务` 和 `查询任务状态` 节点，用于更高级的工作流控制。
* [ ] 探索视频超分、补帧等更多 Vidu API 功能。
## 许可证

本项目采用 [MIT License](LICENSE) 开源。
