# ComfyUI-JM-KlingAI-API
This is a custom node for ComfyUI that allows you to use the KLingAI API directly within the ComfyUI environment. It is developed based on the KLingAI API documentation. For more details, please refer to the official documentation.[KLingAI API Documentation](https://app.klingai.com/global/dev/document-api/quickStart/productIntroduction/overview)。

## Requirements
Before using this node, you need to have [a KLing AI API key](https://app.klingai.com/global/dev/document-api/quickStart/userManual).

## Installation
### Installing manually
1. Navigate to the `ComfyUI/custom_nodes` directory.
2. Clone this repository: `git clone https://github.com/synthetai/ComfyUI-JM-KLing-API.git`
3. Install the dependencies:
+ <font style="color:rgb(31, 35, 40);">Windows (ComfyUI portable): </font>`python -m pip install -r ComfyUI\custom_nodes\ComfyUI-JM-KLingAI-API\requirements.txt`
+ <font style="color:rgb(31, 35, 40);">Linux or MacOS: </font>`cd ComfyUI-JM-KLingAI-API && pip install -r requirements.txt`
4. <font style="color:rgb(31, 35, 40);">Start ComfyUI and enjoy using the KLing AI API node!</font>

## <font style="color:rgb(31, 35, 40);">Nodes</font>
### <font style="color:rgb(31, 35, 40);">KLingAI API Key</font>
<font style="color:rgb(31, 35, 40);">This node generates an API Token</font>

### <font style="color:rgb(31, 35, 40);">Text2Video</font>
<font style="color:rgb(31, 35, 40);">This node is used to generate a video given a text prompt.</font>

![](https://cdn.nlark.com/yuque/0/2025/png/226202/1743648058683-c964e841-e281-4c13-ab97-5af311be4ad0.png)

### <font style="color:rgb(31, 35, 40);">Image2Video</font>
<font style="color:rgb(31, 35, 40);">This node is used to generate a video given an image.</font>

![](https://cdn.nlark.com/yuque/0/2025/png/226202/1743646162371-59f6539c-64bd-4ff7-82d7-fb10640cc427.png)

### <font style="color:rgb(31, 35, 40);">KLingAI Lip Sync</font>
<font style="color:rgb(31, 35, 40);">This node is used to create a lip sync task that makes a video's mouth movements match with provided audio.</font>

### <font style="color:rgb(31, 35, 40);">KLingAI Lip Sync Async</font>
<font style="color:rgb(31, 35, 40);">This node processes longer audio files by automatically splitting them into segments and creates lip sync tasks asynchronously. It then monitors task progress, downloads the generated videos, and merges them into a single output video.</font>

<font style="color:rgb(31, 35, 40);">Features:</font>
- <font style="color:rgb(31, 35, 40);">Splits audio into 10-second segments (configurable)</font>
- <font style="color:rgb(31, 35, 40);">Supports both local audio files and audio URLs</font>
- <font style="color:rgb(31, 35, 40);">Maintains segment order during processing and final merging</font>
- <font style="color:rgb(31, 35, 40);">Asynchronously creates tasks for all segments</font>
- <font style="color:rgb(31, 35, 40);">Monitors task status with configurable poll interval</font>
- <font style="color:rgb(31, 35, 40);">Downloads and merges videos using FFmpeg</font>
- <font style="color:rgb(31, 35, 40);">Organizes files in a structured temporary directory</font>

<font style="color:rgb(31, 35, 40);">Note: This node requires the `pydub` package and FFmpeg to be installed on your system.</font>

### <font style="color:rgb(31, 35, 40);">KLingAI Image Generation</font>
<font style="color:rgb(31, 35, 40);">This node is used to generate images from text prompts using KLingAI's image generation API.</font>

<font style="color:rgb(31, 35, 40);">Features:</font>
- <font style="color:rgb(31, 35, 40);">Text-to-image generation with customizable parameters</font>
- <font style="color:rgb(31, 35, 40);">Support for reference images (both via direct upload and URL)</font>
- <font style="color:rgb(31, 35, 40);">Different reference modes: subject (clothing, pose, etc.) and face (appearance)</font>
- <font style="color:rgb(31, 35, 40);">Adjustable fidelity settings for reference images</font>
- <font style="color:rgb(31, 35, 40);">Multiple aspect ratios to choose from</font>
- <font style="color:rgb(31, 35, 40);">Ability to generate multiple images per request (up to 9)</font>
- <font style="color:rgb(31, 35, 40);">Support for both kling-v1 and kling-v1-5 models</font>
  
### <font style="color:rgb(31, 35, 40);">KLingAI Image Downloader</font>

该节点用于从URL下载图片并保存到本地。

### 功能特点

- 支持从URL直接下载图片
- 自动保存到ComfyUI输出目录
- 支持自定义输出子目录
- 自动生成序列文件名（如 KLingAI_0001.png）

### 输入参数

- `image_url` (必填): 图片的URL地址
- `filename_prefix` (必填): 图片文件名前缀，默认为 "KLingAI"
- `custom_output_dir` (可选): 自定义输出子目录，相对于ComfyUI输出目录

### 输出

- `IMAGE`: 下载的图片，可用于后续处理
- `image_path`: 图片在输出目录中的相对路径
- `image_url`: 原始图片URL

### 使用示例

1. 在ComfyUI中添加KLingAI Image Downloader节点
2. 输入图片URL和可选的文件名前缀
3. 运行工作流，图片将被下载并保存
4. 使用ComfyUI的预览节点查看下载的图片

### <font style="color:rgb(31, 35, 40);">KLingAI Video Downloader</font>
<font style="color:rgb(31, 35, 40);">This node downloads videos from a URL and saves them to a local directory.</font>

<font style="color:rgb(31, 35, 40);">Features:</font>
- <font style="color:rgb(31, 35, 40);">Downloads videos from a specified URL</font>
- <font style="color:rgb(31, 35, 40);">Saves videos with customizable filename prefixes</font>
- <font style="color:rgb(31, 35, 40);">Supports MP4 video format</font>
- <font style="color:rgb(31, 35, 40);">Optional custom output directory</font>
- <font style="color:rgb(31, 35, 40);">Returns the saved video path and original URL for further processing</font>

### <font style="color:rgb(31, 35, 40);">KLingAI Multi-Image to Image</font>
<font style="color:rgb(31, 35, 40);">这个节点使用可灵AI的多图参考生图API，支持使用2-4张图片作为主体参考来生成新图片。</font>

<font style="color:rgb(31, 35, 40);">功能特点:</font>
- <font style="color:rgb(31, 35, 40);">支持2-4张主体参考图片（必需）</font>
- <font style="color:rgb(31, 35, 40);">可选场景参考图和风格参考图</font>
- <font style="color:rgb(31, 35, 40);">支持文本提示词优化生成效果</font>
- <font style="color:rgb(31, 35, 40);">可生成1-9张图片</font>
- <font style="color:rgb(31, 35, 40);">多种画面比例选择</font>
- <font style="color:rgb(31, 35, 40);">支持自定义输出目录和文件名前缀</font>
- <font style="color:rgb(31, 35, 40);">内置图片预览功能</font>
- <font style="color:rgb(31, 35, 40);">支持随机种子控制</font>

<font style="color:rgb(31, 35, 40);">输入参数:</font>
- <font style="color:rgb(31, 35, 40);">主体图片1-2（必需）</font>
- <font style="color:rgb(31, 35, 40);">主体图片3-4（可选）</font>
- <font style="color:rgb(31, 35, 40);">场景参考图（可选）</font>
- <font style="color:rgb(31, 35, 40);">风格参考图（可选）</font>
- <font style="color:rgb(31, 35, 40);">文本提示词</font>
- <font style="color:rgb(31, 35, 40);">输出文件名前缀和目录</font>
- <font style="color:rgb(31, 35, 40);">生成数量、画面比例、随机种子</font>

### <font style="color:rgb(31, 35, 40);">KLingAI 混合视频生成</font>
<font style="color:rgb(31, 35, 40);">这是一个融合了文生视频和图生视频功能的节点，能够根据用户输入自动选择合适的API。</font>

<font style="color:rgb(31, 35, 40);">功能特点:</font>
- <font style="color:rgb(31, 35, 40);">智能判断：如果提供了图像则使用图生视频API，否则使用文生视频API</font>
- <font style="color:rgb(31, 35, 40);">统一界面：在一个节点中同时支持两种视频生成方式</font>
- <font style="color:rgb(31, 35, 40);">支持图像输入（Base64或URL方式）</font>
- <font style="color:rgb(31, 35, 40);">支持正向和负向提示词</font>
- <font style="color:rgb(31, 35, 40);">支持图生视频的摄像机控制功能</font>
- <font style="color:rgb(31, 35, 40);">支持尾帧图像设置</font>
- <font style="color:rgb(31, 35, 40);">兼容所有KLingAI视频模型</font>



