<div align="center">

# ComfyUI Pixabay Gallery
### A powerful node for browsing and importing media from Pixabay directly within ComfyUI.
一个功能强大的 ComfyUI 节点，可直接在工作流中浏览和导入 Pixabay 的媒体资源。

</div>

![image](https://github.com/user-attachments/assets/bd7fbc43-04dd-41bd-9e24-d871254e2263)

---
## Overview

**ComfyUI Pixabay Gallery** provides two powerful custom nodes that integrate a seamless media browser for the Pixabay website directly into your ComfyUI workflow. These nodes allow you to browse, search, and select high-quality, royalty-free images and videos from Pixabay and instantly import them and their metadata into your projects.

The gallery features a fluid, responsive waterfall (masonry) layout, ensuring a beautiful and efficient browsing experience.

## Features

-   **Separate Image and Video Nodes**: Dedicated nodes for an optimized search experience: `Pixabay Image Gallery` and `Pixabay Video Gallery`.
-   **Direct Pixabay Browsing**: Browse media from Pixabay without ever leaving the ComfyUI interface.
-   **Advanced Filtering**:
    -   **For Images**: Filter by query, language, image type (photo, vector), orientation, category, and color.
    -   **For Videos**: Filter by query, language, video type (film, animation), and category.
-   **Video Resolution Control**: Select the desired download resolution for videos (`Large`, `Medium`, `Small`, `Tiny`) directly in the node's UI.
-   **One-Click Import**: Simply click on a media card to select it. When the workflow runs, the node will output:
    -   `image`: The full-resolution image tensor (for the Image node).
    -   `video_url`: The URL for the selected video resolution (for the Video node).
    -   `info`: A detailed JSON string containing all available metadata (tags, user, resolution, etc.).
-   **Optimized Previews**: Image cards use a faster-loading 340px preview, while video cards use the `tiny` preview to ensure a smooth browsing experience.
-   **Secure API Key**: Your Pixabay API key is stored locally in a `config.json` file and is not exposed in the UI.

## Installation

1.  Navigate to your ComfyUI installation directory.
2.  Go to the `ComfyUI/custom_nodes/` folder.
3.  Clone or download this repository into the `custom_nodes` folder. The final folder structure should be `ComfyUI/custom_nodes/ComfyUI_Pixabay_Gallery/`.
4.  **Install Dependencies**: This node requires the `requests` library. Open a terminal, activate your ComfyUI's Python environment, and run:
    ```bash
    pip install requests
    ```
5.  **Configure API Key**:
    -   In the `ComfyUI/custom_nodes/ComfyUI_Pixabay_Gallery/` directory, find the `config.json` file.
    -   Open it and replace the empty quotes with your personal Pixabay API key. You can get a free key from the [Pixabay API Documentation](https://pixabay.com/api/docs/).
    ```json
    {
        "pixabay_api_key": "YOUR_PIXABAY_API_KEY_HERE"
    }
    ```
6.  Restart ComfyUI.

## How to Use

1.  **Add the Node**: Double-click on the canvas, search for `Pixabay Image Gallery` or `Pixabay Video Gallery`, and add the desired node to your graph.
2.  **Browse and Filter**:
    -   Use the dropdown menus and the search box at the top of the node to filter the media.
    -   Click the "Search" button to apply filters and load results.
    -   Scroll down within the gallery to automatically load more media (infinite scroll).
3.  **Select Media**: Click on any image or video card in the gallery. A colored border will appear around your selection.
4.  **(For Videos)** Select a download resolution from the "Resolution" dropdown. This can be changed at any time for a selected video.
5.  **Connect the Outputs**:
    -   Connect the `image` output to a `Preview Image` or `Save Image` node.
    -   Connect the `video_url` output to a text display node (like `Show Text`) or any node that accepts a video URL.
    -   Connect the `info` output to a `Show Text` node to view all metadata.
6.  **Queue Prompt**: Run your workflow. The selected media's data will be fed into the connected nodes.

---
![video](https://github.com/user-attachments/assets/d968e714-006e-446e-8236-daa63b542446)

## 概述

**ComfyUI Pixabay Gallery** 提供了两个功能强大的自定义节点，它将一个为 Pixabay 网站打造的无缝媒体浏览器直接集成到了您的 ComfyUI 工作流中。这些节点允许您直接浏览、搜索和选择来自 Pixabay 的高质量、免版权的图片和视频，并能一键将其本身及元数据导入到您的项目中。

本插件的图库拥有一个流畅且响应式的瀑布流（砌体）布局，确保了美观高效的浏览体验。

## 功能特性

-   **独立的图片和视频节点**: 为了优化搜索体验，提供了专属的节点：`Pixabay Image Gallery` (图片库) 和 `Pixabay Video Gallery` (视频库)。
-   **直连 Pixabay 浏览**: 无需离开 ComfyUI 界面即可浏览来自 Pixabay 的媒体资源。
-   **高级筛选**:
    -   **图片节点**: 可按关键词、语言、图片类型 (照片, 矢量图)、方向、分类和颜色进行筛选。
    -   **视频节点**: 可按关键词、语言、视频类型 (影片, 动画) 和分类进行筛选。
-   **视频分辨率控制**: 可直接在节点UI的下拉菜单中选择期望的视频下载分辨率 (`大`, `中`, `小`, `微`)。
-   **一键导入**: 只需单击一张媒体卡片即可选中它。当工作流运行时，节点将输出：
    -   `image`: 完整分辨率的图片张量 (适用于图片节点)。
    -   `video_url`: 所选分辨率的视频 URL (适用于视频节点)。
    -   `info`: 一个包含所有可用元数据 (如标签、作者、分辨率等) 的详细 JSON 字符串。
-   **优化的预览体验**: 图片卡片使用加载更快的 340px 预览图，而视频卡片使用 `tiny` (微) 预览，以确保流畅的浏览体验。
-   **安全的 API 密钥管理**: 您的 Pixabay API 密钥存储在本地的 `config.json` 文件中，不会在UI界面中暴露。

## 安装说明

1.  导航至您的 ComfyUI 安装目录。
2.  进入 `ComfyUI/custom_nodes/` 文件夹。
3.  将此仓库克隆或下载到 `custom_nodes` 文件夹中。最终的文件夹结构应为 `ComfyUI/custom_nodes/ComfyUI_Pixabay_Gallery/`。
4.  **安装依赖库**: 本节点需要 `requests` 库。请打开命令行，激活您的 ComfyUI 的 Python 环境，然后运行：
    ```bash
    pip install requests
    ```
5.  **配置 API 密钥**:
    -   在 `ComfyUI/custom_nodes/ComfyUI_Pixabay_Gallery/` 目录下，找到 `config.json` 文件。
    -   打开它，并将空字符串替换为您个人的 Pixabay API 密钥。您可以从 [Pixabay API 官方文档](https://pixabay.com/api/docs/)免费获取。
    ```json
    {
        "pixabay_api_key": "在此处填入您的PIXABAY_API密钥"
    }
    ```
6.  重启 ComfyUI。

## 使用方法

1.  **添加节点**: 在画布上双击，搜索 `Pixabay Image Gallery` 或 `Pixabay Video Gallery`，然后将所需的节点添加到您的工作流中。
2.  **浏览与筛选**:
    -   使用节点顶部的下拉菜单和搜索框来筛选媒体资源。
    -   点击 "Search" 按钮来应用筛选条件并加载结果。
    -   在图库区域内向下滚动，即可自动加载更多媒体（无限滚动）。
3.  **选择媒体**: 在图库中单击任意一张图片或视频卡片。您选中的卡片周围会出现一个彩色的边框。
4.  **(仅限视频)** 从“分辨率”下拉菜单中选择一个下载分辨率。对于已选中的视频，您可以随时更改此选项。
5.  **连接输出端口**:
    -   将 `image` 输出连接到 `Preview Image` (预览图像) 或 `Save Image` (保存图像) 等节点。
    -   将 `video_url` 输出连接到文本显示节点 (如 `Show Text`) 或任何接受视频 URL 的节点。
    -   将 `info` 输出连接到 `Show Text` (显示文本) 节点，以查看所有元数据。
6.  **执行工作流**: 点击 "Queue Prompt"。所选媒体的数据将被送入已连接的节点中。
