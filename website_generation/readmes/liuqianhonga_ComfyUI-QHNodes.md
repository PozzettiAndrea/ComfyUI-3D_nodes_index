# ComfyUI-QHNodes

为 ComfyUI 开发的自定义节点集合，提供预设尺寸预设Latent、从文件夹加载LoRA，以及集成了多个常用的自定义节点。

> 所有节点均为日常所用，偏定制化，如有需要，可参考

## 包含节点

### 主仓库节点

1. **预设尺寸 (Preset Size Latent)**: 提供常用的图像尺寸预设
2. **文件夹加载LoRA (Load LoRA from Folder)**: 批量加载指定文件夹中的 LoRA 模型
3. **采样器设置 (Sampler Settings)**: 提供采样器和调度器设置的配置节点
4. **JSON解包 (JsonUnpack)**: 解析JSON字符串并提取指定的键值，支持最多5个键的提取
5. **Gemini图像分析 (Gemini)**: 使用Google Gemini模型进行图像分析和描述
6. **文件夹图片统计 (Image Count From Folder)**: 统计指定文件夹中的图片数量
7. **文件夹加载图片 (Load Image From Folder)**: 从指定文件夹中批量加载图片，支持设置起始索引和加载数量
8. **文件保存 (File Save)**: 将文本内容保存到指定文件夹，支持多种文件格式
9. **动态表达式 (Dynamic Expression)**: 执行动态Python表达式，支持最多5个参数
### 集成的子模块

以下是集成的常用节点，如果不需要所有节点，可单独下载：

1. [字符串相关节点](https://github.com/liuqianhonga/ComfyUI-String-Helper) 
   - 字符串相关的自定义节点，提高在处理字符串时的效率和灵活性
   - 支持字符串列表、翻译、CSV导入导出等功能
   - 提供多种字符串选择方式：按序号选择、顺序循环、随机选择

2. [图像压缩节点](https://github.com/liuqianhonga/ComfyUI-Image-Compressor) 
   - 用于图像压缩的ComfyUI自定义节点，支持JPEG、WEBP、PNG压缩格式和参数调整

3. [Html2Image节点](https://github.com/liuqianhonga/ComfyUI-Html2Image) 
   - 提供ComfyUI网页截图、相机水印、自由模板转图片功能节点

4. [模型下载节点](https://github.com/liuqianhonga/ComfyUI-Model-Downloader) 
   - ComfyUI的模型下载节点，支持civitai和huggingface下的模型下载

## 安装方法

### 场景一：安装所有节点（推荐）

如果你想使用所有功能，可以一次性安装所有节点：

```bash
cd ComfyUI/custom_nodes/
git clone --recursive https://github.com/liuqianhonga/ComfyUI-QHNodes.git
```

### 场景二：仅安装主仓库节点

如果你只想使用预设尺寸和文件夹加载LoRA功能：

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/liuqianhonga/ComfyUI-QHNodes.git
```

### 子模块管理（可选）

1. 添加子模块：如果之前只安装了主仓库，现在想添加子模块
```bash
cd ComfyUI/custom_nodes/ComfyUI-QHNodes
git submodule init
git submodule update
```

2. 更新子模块：如果想更新子模块到最新版本
```bash
cd ComfyUI/custom_nodes/ComfyUI-QHNodes
git submodule update --remote
```

所有依赖会在 ComfyUI 启动时自动检查和安装。

## 更新说明

### 更新主仓库
```bash
cd ComfyUI/custom_nodes/ComfyUI-QHNodes
git pull
```

### 更新所有子模块
```bash
cd ComfyUI/custom_nodes/ComfyUI-QHNodes
git submodule update --remote
```

## 节点说明

### 🐟预设尺寸 (Preset Size Latent)

预设尺寸节点，支持以下预设：

#### 竖版尺寸预设

- **竖版通用 (1024×1536)**
  - 标准的 2:3 竖版比例
  - 适合壁纸和电子书封面

- **竖版高清 (1280×1536)**
  - 5:6 竖版比例
  - 适合社交平台/AI作画

- **竖版长图 (1024×2048)**
  - 1:2 竖版比例
  - 适合全身像/海报/建筑

- **竖版超清 (1536×2048)**
  - 适合精细插画/商业海报

- **竖版超长 (1080×2520)**
  - 9:21 竖版比例
  - 适合长图文/漫画

#### 横版尺寸预设

- **横版通用 (1536×1024)**
  - 3:2 横版比例
  - 适合风景/场景

- **横版宽屏 (1920×1080)**
  - 16:9 横版比例
  - 适合桌面壁纸

- **横版超宽 (2560×1080)**
  - 21:9 横版比例
  - 适合全景图

#### 手机尺寸预设

- **手机人像 16:9 (1080×1920)**
  - 适合人像/全身照
  - 标准的手机全屏比例

- **手机人像 4:3 (1440×1920)**
  - 适合证件照/半身像
  - 更宽的画面比例

- **手机场景 3:2 (1280×1920)**
  - 适合风景和建筑
  - 宽屏构图

- **手机通用 (1024×1024)**
  - 适合头像和产品图
  - 方形构图

- **手机高清 (1920×1920)**
  - 适合精致产品和艺术作品
  - 高分辨率方形

- **手机壁纸 Mobile Wallpaper (1280×2048)**
  - 适合手机壁纸和移动设备内容
  - 5:8 比例，垂直长图

#### 视频尺寸预设

- **4K (3840×2160)**
  - 超高清视频标准
  - 适合专业视频制作

- **2K (2048×1152)**
  - 高清视频标准
  - 适合一般视频制作

- **1080p (1920×1080)**
  - 全高清视频标准
  - 最常用的视频尺寸

- **电影 (2048×870)**
  - 2.35:1 电影比例
  - 适合电影级内容

#### 相片尺寸预设

- **4×6英寸 (1200×1800)**
  - 适合冲印照片
  - 标准相片尺寸

- **5×7英寸 (1500×2100)**
  - 适合相框装饰
  - 较大相片尺寸

#### 社交媒体预设

- **抖音/快手 (1080×1920)**
  - 适合短视频封面
  - 标准竖屏比例

- **朋友圈 (1080×1920)**
  - 适合生活分享
  - 移动端优化

- **小红书 (1080×1350)**
  - 适合美食/穿搭
  - 4:5 优化比例

- **微博 (1200×900)**
  - 适合图文/新闻
  - 横版展示

- **B站封面 (1146×717)**
  - 适合视频封面
  - 平台优化尺寸

#### 国际社交平台预设

- **Instagram Story (1080×1920)**
  - 适合故事/Vlog
  - Instagram 标准尺寸

- **TikTok Video (1080×1920)**
  - 适合短视频/舞蹈
  - TikTok 优化尺寸

- **Facebook Post (1200×630)**
  - 适合社交分享
  - Facebook 推荐尺寸

- **Twitter Post (1200×675)**
  - 适合资讯/新闻
  - Twitter 优化尺寸

- **Youtube Cover (2560×1440)**
  - 适合视频封面
  - Youtube 标准尺寸

#### 自定义预设

你可以通过编辑以下文件来添加自己的预设尺寸：
- `nodes/preset_sizes.json`: 社交媒体预设
- `nodes/camera_sizes.json`: 相机预设

格式如下：
```json
{
    "预设名称 (宽×高)": [宽度, 高度]
}
```

### 🐟Load LoRA (Folder)

从指定文件夹加载 LoRA 模型。支持以下功能：

- **基础模型**：接收基础模型（MODEL）作为输入
  - 所有的 LoRA 都将基于此模型进行加载
  - 节点会自动克隆基础模型，不会修改原始模型
- **文件夹路径**：支持多个文件夹路径，使用英文逗号分隔
  - 示例：`myLoras, character/style1`
  - 相对路径基于 ComfyUI 的 `models/loras` 目录
  - 如果路径不存在会在控制台输出提示信息
- **模型强度**：调整 LoRA 对模型的影响程度
  - 范围：-100.0 到 100.0
  - 默认值：1.0
  - 负值会产生相反的效果
- **合并加载**：控制多个 LoRA 的加载方式
  - 开启：将所有符合条件的 LoRA 合并加载到同一个模型中
  - 关闭（默认）：为每个 LoRA 创建单独的模型副本
- **实时预览**：执行后会显示找到的 LoRA 文件列表，方便确认是否正确加载

#### 使用示例

1. 分别加载多个 LoRA（默认模式）：
   ```
   model: 基础模型
   lora_folders: portraits, anime/style
   strength_model: 0.8
   merge_loras: False (默认)
   ```
   输出：多个模型，每个模型包含一个 LoRA

2. 合并加载多个 LoRA：
   ```
   model: 基础模型
   lora_folders: myLoras
   strength_model: 1.0
   merge_loras: True
   ```
   输出：一个包含所有 LoRA 的模型

#### 注意事项

- 文件夹路径使用正斜杠 `/` 分隔
- 目前仅支持 .safetensors 格式的 LoRA 文件
- 如果找不到任何符合条件的文件，节点会显示"No LoRA files found"
- 合并加载多个 LoRA 时，加载顺序与文件夹中的顺序一致
- 每个 LoRA 都会创建模型的副本，请注意内存使用

### 🐟采样器设置 (Sampler Settings)

采样器和调度器配置节点。支持以下功能：

1. 采样器设置：支持所有 ComfyUI 内置采样器
2. 调度器设置：支持所有 ComfyUI 内置调度器
3. 采样步数：可配置范围 1-100，默认 30 步
4. 降噪强度：可配置范围 0.0-1.0，默认 1.0

输出参数类型为 ANY，方便与其他节点对接。

### 🐟JSON解包 (JsonUnpack)

解析JSON字符串并提取指定的键值，支持最多5个键的提取。

- **JSON字符串**：接收JSON字符串作为输入
  - 支持标准JSON格式
  - 可以从文本文件或其他节点输出中获取
- **键值提取**：支持最多5个键的提取
  - 使用英文逗号分隔多个键
  - 键名不区分大小写
  - 如果键不存在会输出空值
- **输出类型**：输出类型为 ANY，方便与其他节点对接

#### 使用示例

1. 提取单个键值：
   ```
   json_string: {"name": "John", "age": 30}
   keys: name
   ```
   输出：John

2. 提取多个键值：
   ```
   json_string: {"name": "John", "age": 30, "city": "New York"}
   keys: name, age, city
   ```
   输出：John, 30, New York

#### 注意事项

- JSON字符串必须是标准格式
- 键值提取不支持嵌套JSON对象
- 如果键不存在会输出空值
- 输出类型为 ANY，方便与其他节点对接

### 🐟Gemini图像分析 (Gemini)

使用Google的Gemini模型对图像进行分析和描述，支持多种模型选择和参数调整。

#### 输入参数

- **图像 (image)**：需要分析的图像
  - 支持ComfyUI标准图像格式
  - 会自动转换为Gemini支持的格式

- **API密钥 (api_key)**：Google API密钥
  - 需要有效的Google API密钥
  - 可以从Google AI Studio获取

- **模型 (model)**：Gemini模型选择
  - gemini-2.0-flash-exp
  - gemini-1.5-flash
  - gemini-1.5-flash-8b
  - gemini-1.5-pro

- **prompt**：引导模型分析的提示文本
  - 默认值："Describe this image"
  - 可以使用自定义提示词引导分析方向

- **temperature**：生成文本的随机性
  - 范围：0.0-2.0
  - 默认值：0.8
  - 较低的值生成更确定的结果
  - 较高的值生成更多样化的结果

- **max_output_tokens**：生成文本的最大长度
  - 范围：1-8192
  - 默认值：2048

#### 输出

- **文本描述**：模型对图像的分析结果
  - 输出类型：STRING
  - 可以与其他文本处理节点配合使用

#### 使用示例

1. 基础图像描述：
   ```
   prompt: "Describe this image in detail"
   temperature: 0.8
   max_output_tokens: 2048
   ```

2. 特定分析任务：
   ```
   prompt: "List all the objects in this image"
   temperature: 0.3
   max_output_tokens: 1024
   ```

#### 注意事项

- 需要有效的Google API密钥
- API调用可能产生费用，请参考Google的定价政策
- 较大的图像可能需要更长的处理时间
- 建议根据具体需求调整temperature和max_output_tokens参数

### 🐟文件夹图片统计 (Image Count From Folder)

统计指定文件夹中的图片数量。

- **文件夹路径**：需要统计的文件夹路径
  - 支持绝对路径和相对路径
  - 相对路径基于 ComfyUI 的根目录

#### 输出

- **图片数量**：文件夹中的图片数量
  - 输出类型：INT
  - 可以与其他节点对接

#### 使用示例

1. 统计指定文件夹中的所有图片：
   ```
   folder_path: /path/to/folder
   ```
   输出：文件夹中的图片数量

#### 注意事项

- 文件夹路径必须正确
- 如果文件夹不存在会返回0
- 支持的图片格式包括常见图片格式（jpg、png、jpeg等）

### 🐟文件夹加载图片 (Load Image From Folder)

从指定文件夹中批量加载图片，支持设置起始索引和加载数量。

- **文件夹路径**：需要加载的文件夹路径
  - 支持绝对路径和相对路径
  - 相对路径基于 ComfyUI 的根目录
- **起始索引**：加载图片的起始索引
  - 范围：0-10000
  - 默认值：0
- **加载数量**：加载图片的数量
  - 范围：1-100
  - 默认值：1

#### 输出

- **图片列表**：加载的图片列表
  - 输出类型：LIST[IMAGE]
  - 可以与其他图像处理节点对接
- **图片名称**：加载的图片文件名列表
  - 输出类型：LIST[STRING]
  - 不包含路径，仅文件名
- **图片路径**：加载的图片完整路径列表
  - 输出类型：LIST[STRING]
  - 包含完整的文件路径

#### 使用示例

1. 加载指定文件夹中的所有图片：
   ```
   folder_path: /path/to/folder
   start_index: 0
   load_cap: 10
   ```
   输出：
   - images: 前10张图片的图像数据
   - image_names: 前10张图片的文件名
   - image_paths: 前10张图片的完整路径

2. 从中间开始加载图片：
   ```
   folder_path: /path/to/folder
   start_index: 5
   load_cap: 5
   ```
   输出：
   - images: 第5-9张图片的图像数据
   - image_names: 第5-9张图片的文件名
   - image_paths: 第5-9张图片的完整路径

#### 注意事项

- 文件夹路径必须正确
- 如果文件夹不存在会返回空列表
- 加载数量不能超过文件夹中的图片数量
- 图片按文件名排序
- 支持常见图片格式（jpg、png、jpeg等）

### 🐟文件保存 (File Save)

将文本内容保存到指定文件夹，支持多种文件格式。

- **文件夹路径**：需要保存的文件夹路径
  - 支持绝对路径和相对路径
  - 相对路径基于 ComfyUI 的根目录
- **文件名**：保存的文件名
  - 支持多种文件格式，例如txt、csv、json等
- **文本内容**：需要保存的文本内容
  - 支持标准文本格式
  - 可以从文本文件或其他节点输出中获取

#### 输出

- **文件路径**：保存的文件路径
  - 输出类型：STRING
  - 可以与其他节点对接

#### 使用示例

1. 保存文本内容到指定文件夹：
   ```
   folder_path: /path/to/folder
   file_name: example.txt
   text_content: Hello World!
   ```
   输出：保存的文件路径

#### 注意事项

- 文件夹路径必须正确
- 文件名必须正确
- 文本内容必须是标准格式
- 如果文件夹不存在会输出错误信息

### 🐟动态表达式 (Dynamic Expression)

执行动态Python表达式，支持最多5个参数。

- **表达式**：需要执行的Python表达式
  - 支持标准Python表达式
  - 可以从文本文件或其他节点输出中获取
- **参数**：表达式需要的参数
  - 支持任意类型
  - 支持最多5个参数

#### 输出

- **结果**：表达式执行结果
  - 输出类型：ANY
  - 可以与其他节点对接

#### 使用示例

1. 执行简单的加法表达式：
   ```
   expression: "return arg1 + arg2"
   arg1: 1
   arg2: 2
   ```
   输出：3

2. 执行复杂的字符串拼接表达式：
   ```
   expression: "return f'Hello, {arg1} {arg2}!'
   arg1: "John"
   arg2: "Doe"
   ```
   输出："Hello, John Doe!"

3. 执行复杂的列表操作表达式：
   ```
   expression: "return [arg1, arg2, arg3]"
   arg1: 1
   arg2: 2
   arg3: 3
   ```
   输出：[1, 2, 3]

4. 执行复杂的字典操作表达式：
   ```
   expression: "return {'a': arg1, 'b': arg2, 'c': arg3}"
   arg1: 1
   arg2: 2
   arg3: 3
   ```
   输出：{'a': 1, 'b': 2, 'c': 3}

5. if-else表达式：
   ```
   expression: "return 'Even' if arg1 % 2 == 0 else 'Odd'"
   arg1: 4
   ```
   输出："Even"

#### 注意事项

- 表达式必须是有效的Python代码
- 参数必须与表达式中的变量名匹配
- 表达式执行结果会作为输出返回
