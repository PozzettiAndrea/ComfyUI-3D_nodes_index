# ComfyUI 学习中心

ComfyUI学习中心插件，提供交互式学习体验，帮助用户从零开始学习ComfyUI。

## 功能特点

### 教程分章节学习
- 从基础到高级的渐进式学习路径
- 每个章节包含详细说明和学习目标
- 难度分级：初级、中级、高级
- 章节之间有前置和关联关系，引导学习路径

### 练习与参考答案
- 每个章节包含练习工作流和参考答案
- 可以直接加载练习开始实践
- 完成练习后可查看参考答案进行对比
- 进度跟踪，记录已完成的章节

### 其他实用的工作流收集

### 学习成就系统
- 根据完成的章节数自动确定成就级别
- 提供可自定义的成就证书生成器
- 支持不同成就级别：初学者、学徒、实践者、专家、大师、宗师
- 显示已完成章节和下一级别所需章节数

## 安装方法

### 方法1：通过Git克隆
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/assemly/comfyui-learningcenter.git
```

### 方法2：下载ZIP文件
1. 下载本仓库的ZIP文件
2. 解压到 `ComfyUI/custom_nodes/` 目录下
3. 重启ComfyUI

## 使用方法

### 浏览教程
1. 启动ComfyUI
2. 点击顶部菜单栏的"学习中心"按钮
3. 在侧边栏浏览可用的章节
4. 可以使用搜索框和难度过滤器找到特定章节

### 学习流程
1. 点击你感兴趣的章节卡片查看详情
2. 阅读章节描述和学习目标
3. 点击"加载练习工作流"开始练习
4. 完成练习后，点击"标记为已完成"
5. 查看参考答案进行对比学习

### 使用成就系统
1. 点击左侧菜单栏的"学习中心"
2. 学习并完成教程章节，每完成一个章节会记录到用户进度中
3. 添加"成就信息显示"节点查看当前成就级别和完成章节数
4. 添加"成就证书生成器"节点生成个性化的成就证书图像
5. 根据完成章节数，自动解锁不同的成就级别

### 偷偷告诉你们还有个隐藏成就

### 添加自己的教程章节
1. 在插件目录下的`templates`文件夹中创建一个新文件夹（名称格式：chapterX_name）
2. 添加`metadata.json`文件提供章节信息
3. 添加`exercise.json`作为练习工作流
4. 添加`answer.json`作为参考答案工作流
5. 可选：添加`preview.png`作为预览图

## 章节目录结构
```
templates/
├── chapter1_intro/             # 第一章：介绍
│   ├── metadata.json           # 章节元数据
│   ├── exercise.json           # 练习工作流
│   ├── answer.json             # 参考答案工作流
│   └── preview.png             # 预览图（可选）
├── chapter2_basics/            # 第二章：基础知识
│   ├── ...
```

### metadata.json 格式
```json
{
  "title": "章节标题",
  "description": "章节详细描述",
  "difficulty": "beginner",  // 可选：beginner, intermediate, advanced
  "model":"模型类型",
  "learning_objectives": ["目标1", "目标2"],
  "prerequisites": ["chapter1_intro"],  // 前置章节
  "estimated_time": 30,  // 预计完成时间(分钟)
  "related_chapters": ["chapter3_text"]  // 相关章节
}
```

## 项目结构
```
comfyui-learningcenter/
├── server/                   # 后端服务
│   ├── __init__.py
│   ├── learningcenter.py     # 核心功能实现
│   ├── remote_image.py       # 远程图像处理
│   └── achievement_certificate.py # 成就证书生成器
├── resources/                # 资源文件
│   ├── opai.png              # 成就证书吉祥物
│   └── images/               # 其他图像资源
├── web/                      # 前端界面
│   ├── learningcenter.js     # 主要功能实现
│   ├── learningcenter-ui.js  # UI组件
│   ├── templates.js          # 模板处理
│   └── utils.js              # 工具函数
├── templates/                # 教程章节存储目录
│   ├── chapter1_intro/       # 第一章：介绍
│   ├── chapter2_basics/      # 第二章：基础知识
│   ├── chapter3_text/        # 第三章：文本提示
│   ├── chapter4_controlnet/  # 第四章：ControlNet
│   ├── chapter5_inpainting/  # 第五章：修复绘制
│   └── chapter6_workflow/    # 第六章：工作流技巧
├── user_progress/            # 用户进度存储目录
├── __init__.py               # 插件初始化
├── requirements.txt          # 依赖包
├── pyproject.toml            # 项目配置
├── preview.png               # 插件预览图
└── README.md                 # 文档
```

## 注意事项
- 请确保您有足够的磁盘空间用于存储教程文件
- 推荐使用最新版本的ComfyUI以获得最佳体验
- 教程中的工作流可能需要相应的模型和其他自定义节点的支持



## 许可证
MIT 