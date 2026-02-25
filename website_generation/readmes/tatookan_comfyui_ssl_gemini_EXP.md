# ComfyUI Gemini Flash 节点

这是一个用于ComfyUI的Google Gemini API集成节点，支持文本生成和图像生成功能。通过此节点，您可以在ComfyUI工作流中直接使用Google的Gemini 2.0系列模型。
特别说明：关于出现[ERROR]API调用错误:'NoneType'object has no attribute'parts  说明你上传的图片或者提示词已经违反了《Generative AI Prohibited Use Policy》，请先使用场景或者产品图测试。

![](https://github.com/tatookan/comfyui_ssl_gemini_EXP/blob/main/demo/demo.png?raw=true)
---
![](https://github.com/tatookan/comfyui_ssl_gemini_EXP/blob/main/demo/demo2.png?raw=true)

## 更新
2025.3.19：更新支持多图处理功能
## 功能特点

- 支持Gemini 2.0系列模型（gemini-2.0-flash, gemini-2.0-flash-exp, gemini-2.0-pro）
- 支持文本到文本生成
- 支持图像到文本生成（图像理解）
- 支持文本到图像生成（仅在其他.py文件中实现）
- 内置代理支持，方便中国用户使用
- 自动依赖检查和安装
- 完善的错误处理和日志记录

## 安装方法

1. 确保您已经安装了ComfyUI
2. 将此仓库克隆或下载到ComfyUI的`custom_nodes`目录中：
   ```
   cd ComfyUI/custom_nodes
   git clone https://github.com/tatookan/comfyui_ssl_gemini_EXP.git
   ```
3. 安装依赖：
   ```
   cd comfyui_ssl_gemini_EXP
   pip install -r requirements.txt
   ```
4. 重启ComfyUI

## 使用方法

### 1. 配置API密钥

首先，您需要获取Google Gemini API密钥：
1. 访问[Google AI Studio](https://makersuite.google.com/app/apikey)
2. 创建一个API密钥
3. 在ComfyUI中使用`💠SSL/API/Gemini/API Key Config`节点输入您的API密钥

### 2. 文本生成

使用`💠SSL/API/Gemini/Text Prompt`节点进行文本生成：

- 连接API密钥配置节点到`config`输入
- 在`prompt`中输入您的提示文本
- 调整生成参数（温度、top_p、top_k等）
- 如果需要，可以连接图像到`input_image`输入，实现图像理解功能

### 3. 代理设置

如果您在中国或其他需要代理的地区：

1. 将`use_proxy`设置为`True`
2. 设置`proxy_host`（默认为127.0.0.1）
3. 设置`proxy_port`（默认为7890）

## 参数说明

### API密钥配置节点

- `api_key`: Google Gemini API密钥

### 文本生成节点

#### 必填参数

- `config`: API密钥配置
- `prompt`: 提示文本
- `model`: 选择模型（gemini-2.0-flash, gemini-2.0-flash-exp, gemini-2.0-pro）
- `temperature`: 生成温度（0.0-1.0），控制创意程度
- `top_p`: 核采样参数（0.0-1.0）
- `top_k`: 考虑的候选词数量（1-100）
- `max_output_tokens`: 最大输出标记数（1-8192）
- `include_images`: 是否在响应中包含图像（True/False）

#### 可选参数

- `input_image`: 输入图像（用于图像理解）
- `use_proxy`: 是否使用代理（True/False）
- `proxy_host`: 代理主机地址
- `proxy_port`: 代理端口

## 输出

文本生成节点输出：
- `text`: 生成的文本
- `image`: 如果启用了图像生成，则输出图像

## 注意事项
-根据谷歌的《Generative AI Prohibited Use Policy》，Gemini API 有以下限制：
-不得用于生成违反法律法规的内容
-不得用于生成有害、欺诈、色情或暴力内容
-不得用于生成侵犯他人隐私或知识产权的内容
-图像生成可能受到额外限制，某些类型的图像可能无法生成

- 使用此节点需要稳定的网络连接或有效的代理设置
- API请求可能会受到Google服务器负载的影响
- 大型请求可能需要更长的处理时间
- 图像生成功能需要使用支持图像生成的模型（如gemini-2.0-flash-exp）

## 故障排除

- 如果遇到网络连接问题，请检查代理设置
- 如果API请求失败，请检查API密钥是否有效
- 如果依赖安装失败，请手动安装所需的依赖包

## 致谢

感谢Google提供的Gemini API服务。

# Contact Details
Email: dianyuanan@vip.qq.com  
加入我的粉丝群: 联系微信: Miss-Y-s-Honey, 并注明来意
查看我的教程频道 [bilibili@深深蓝hana](https://space.bilibili.com/618554?spm_id_from=333.1007.0.0)
日常作品分享 [douyin@深深蓝](https://www.douyin.com/user/MS4wLjABAAAAJGu7yCfV3XwKoklBX62bivvat3micLxemdDT0FAmdcGfqbuFS3ItsKWKrBt5Hg16?from_tab_name=)
