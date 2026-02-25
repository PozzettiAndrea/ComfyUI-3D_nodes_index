# Comfyui JTnodes

这个项目包含了一些自定义的ComfyUI节点，用于图像处理、AI对话和辅助工具任务。

[![Version](https://img.shields.io/badge/version-1.3.0-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()

## 功能

当前版本 (v1.3.0) 包含以下节点：

- **JT Siliconflow LLM**: Siliconflow API对话节点
  - 输入：
    - API密钥 (STRING)
    - 提示词 (STRING，支持多行输入)
    - 系统设定 (STRING，支持多行输入)
    - 模型选择 (四种可选模型)
    - 上下文大小 (INT，0-30)
    - 最大生成长度 (INT，512-200000)
  - 输出：
    - 生成的文本 (STRING)
    - 完整对话记录 (STRING)
    - 会话历史 (STRING)
  - 特点：
    - 支持多个Siliconflow模型
    - 支持自定义系统设定
    - 维护会话历史
    - 灵活的上下文管理

- **JT Brightness Adjustment**: 图像亮度调节节点
  - 输入：
    - 图像 (IMAGE)
    - 亮度调节系数 (0.0 到 2.0)
  - 输出：
    - 处理后的图像 (IMAGE)

- **JT Save Image to Path**: 高级图像保存节点，支持灵活的文件命名和批量保存
  - 输入：
    - 图像 (IMAGE)
    - 文件夹路径 (STRING，默认: "/path")
    - 文件名 (STRING，默认: "Image")
    - 格式 (COMBO ["PNG", "JPG"]，默认: "JPG")
    - 使用序号 (BOOLEAN，默认: False)
    - 分隔符 (COMBO ["none", "hyphen", "underscore"]，默认: "hyphen")
      - none: 无分隔符
      - hyphen: 连字符 (-)
      - underscore: 下划线 (_)
    - 序号位数 (INT，1-5位，默认: 4)
    - 允许覆盖 (BOOLEAN，默认: True)
  - 输出：
    - 原始图像传递 (IMAGE) - 用于工作流程继续
    - 保存文件夹路径 (STRING) - 图像保存的目录完整路径
    - 保存文件名列表 (STRING) - 所有保存的文件名，每个文件名占一行
    - 保存数量 (INT) - 本次保存的图像总数

  - 文件命名规则：
    1. 无序号模式：
       - 直接使用输入的文件名保存
       - 当不允许覆盖且文件存在时跳过保存
    
    2. 序号模式：
       - 使用 文件名 + 分隔符 + 序号 的格式
       - 序号位数在1-5位之间自动调整
       - 允许覆盖时：从1开始按顺序编号
       - 不允许覆盖时：从1开始查找未被使用的序号
    
    3. 批量保存时：
       - 允许覆盖：使用连续的序号
       - 不允许覆盖：自动跳过已存在的序号

  - 特点：
    - 自动创建完整的输出目录结构
    - 提供完整的文件名列表预览
    - 支持PNG格式的元数据保存
    - 高质量的图像保存（JPG使用95质量）
    - 实时显示所有保存文件名，每行一个
    - 智能的序号管理系统
    - 灵活的覆盖控制

- **JT Serial Counter**: 序号生成工具节点
  - 输入：
    - 数字 (INT，0-99999)
    - 序号位数 (INT，1-5位)
  - 输出：
    - 格式化的序号字符串 (STRING)
  - 特点：
    - 支持1-5位序号长度
    - 智能的位数自动调整
    - 自动处理数字溢出
    - 适用于批处理文件命名

- **JT Save Text to File**: 文本文件保存节点
  - 输入：
    - 文本内容 (STRING，支持多行输入)
    - 文件夹路径 (STRING，默认: "/path")
    - 文件名 (STRING，默认: "output.txt")
    - 写入模式 (COMBO ["append", "overwrite"]，默认: "append")
  - 输出：
    - 保存的文本内容 (STRING)
  - 特点：
    - 支持追加和覆盖两种写入模式
    - 自动创建目录结构
    - 自动处理换行符
    - 支持多行文本保存

- **JT Save Text to Excel**: Excel表格保存节点
  - 输入：
    - 文本内容 (STRING，支持多行输入)
    - 文件夹路径 (STRING，默认: "/path")
    - 文件名 (STRING，默认: "output")
    - 工作表名 (STRING，默认: "Sheet1")
    - 行号 (INT，1-1048576)
    - 列号 (INT，1-16384)
  - 输出：
    - 保存到表格中的第一行文本 (STRING)
  - 特点：
    - 自动处理文件扩展名(.xlsx)
    - 支持新建或更新已有文件
    - 可指定单元格位置
    - 如果输入文本包含多行，仅保存第一行
    - 自动创建或使用指定工作表

- **JT Find Text From Excel**: Excel文本查找节点
  - 输入：
    - Excel_Filepath (STRING，默认: "/path")
    - Excel_Filename (STRING，默认: "table")
    - Find_Text (STRING)
    - Output_Column (INT，1-16384)
  - 输出：
    - found_text: 找到的文本所在行的指定列内容
    - row_number: 找到的文本所在行号
    - column_number: 找到的文本所在列号
  - 特点：
    - 支持查找指定文本
    - 返回查找结果同行的指定列内容
    - 返回找到文本的精确位置
    - 自动处理文件扩展名(.xlsx)

- **JT Read From Excel**: Excel文本读取节点
  - 输入：
    - Excel_Filepath (STRING，默认: "/path")
    - Excel_Filename (STRING，默认: "table")
    - Row_Number (INT，1-1048576)
    - Column_Number (INT，1-16384)
  - 输出：
    - cell_text: 指定位置的单元格文本
    - row_number: 读取位置的行号
    - column_number: 读取位置的列号
  - 特点：
    - 精确读取指定位置的内容
    - 自动处理文件扩展名(.xlsx)
    - 支持大规模Excel表格
    - 返回完整的位置信息

## 安装说明

1. 找到你的ComfyUI安装目录
2. 进入 `custom_nodes` 目录（如果不存在则创建）
3. 将此项目克隆或复制到该目录：
   ```bash
   cd custom_nodes
   # 通过克隆仓库
   git clone [你的仓库URL]
   # 或直接将 Comfyui_JTnodes 文件夹复制到此目录
   ```
4. 安装依赖：
   ```bash
   pip install openai>=1.0.0 openpyxl>=3.0.0
   ```
5. 重启ComfyUI

## 使用方法

1. 启动ComfyUI
2. 在节点选择菜单中，查找对应节点（在JT分类下）
3. 将节点添加到你的工作流中
4. 设置所需参数
5. 运行工作流

## 系统要求

- ComfyUI (最新版本)
- Python 3.x
- PyTorch >= 1.12
- NumPy >= 1.23
- Pillow (PIL) >= 9.0
- openai >= 1.0.0
- openpyxl >= 3.0.0

## 许可证

MIT License

## 更新日志

### v1.3.0
- 添加Excel处理节点：
  - JT Find Text From Excel：在Excel文件中查找文本并返回指定列内容
  - JT Read From Excel：读取Excel指定位置的文本内容
- 优化文本处理功能
- 改进参数命名规范
- 加强错误处理机制

### v1.2.0
- 添加文本处理节点：
  - JT Save Text to File：支持文本文件的追加和覆盖写入
  - JT Save Text to Excel：支持将文本保存到Excel表格指定位置
- 新增依赖项 openpyxl >= 3.0.0
- 优化代码结构和注释

### v1.1.0
- 添加 JT Siliconflow LLM 节点，支持以下功能：
  - Siliconflow API调用
  - 多模型支持（DeepSeek-V3, QwQ-32B, Qwen2.5-32B-Instruct, DeepSeek-R1）
  - 会话历史管理
  - 自定义系统设定
- 优化API密钥输入显示
- 更新OpenAI客户端初始化方式
- 添加新的依赖项要求（openai>=1.0.0）

### v1.0.0
- 初始版本发布
- 实现基础图像处理功能
- 添加高级图像保存功能
- 添加序号生成工具
