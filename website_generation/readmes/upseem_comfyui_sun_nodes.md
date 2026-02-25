🌍 [English](./README.en.md) | [中文说明](./README.md)


# ☀️ comfyui_sun_nodes
由 [**SunX AI**](https://github.com/upseem) 开发的一组适用于 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 的自定义节点插件。

目前主要功能：**图像循环处理（Loop）**

---

## 🧠 功能介绍

### ✅ Comfyui图片循环处理 `Batch Image Loop`
用于将图像批次逐张依次送入 ComfyUI 图像处理流程中，实现“逐帧处理”，尤其适合将视频帧一帧一帧处理的场景。

包含两个节点：

- `Batch Image Loop Open SunxAI`：读取图像批次，按索引逐张送出
- `Batch Image Loop Close SunxAI`：接收每次循环结果，自动拼接最终结果


![视频转动漫工作流](./example_workflows/Sun_sample_workflow.png)

📌 **特点：**

- 🚀 **逐帧处理**：每一张图像会被完整处理后，才进入下一张循环（不是在采样时同时执行多帧）
- 🔄 **完全同步**：处理流程严格串行，不会在采样阶段提前进入下一帧，确保前后图一致性

适用于：
- 视频逐帧处理
- 动态图像序列生成
- 任意逐帧风格迁移等任务

---

## 📦 安装方式

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/upseem/comfyui_sun_nodes.git
````

重启 ComfyUI 即可自动加载节点。

---

## 🗂 节点分类

所有节点将出现在 ComfyUI 的：


## 📄 License

本项目采用 **MIT License**，欢迎自由使用与扩展。

---

## ❤️ 关于我们

`SunX AI` 专注于图像生成、AI工作流、ComfyUI插件开发。
欢迎关注项目、提出 issue 或提交 PR！

GitHub 地址：[https://github.com/upseem/comfyui\_sun\_nodes](https://github.com/upseem/comfyui_sun_nodes)



