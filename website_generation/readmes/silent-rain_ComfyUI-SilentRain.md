# ComfyUI-SilentRain

本项目是基于Rust语言开发的ComfyUI自定义节点集合，旨在高效扩展comfyui生态。核心优势包括：

- **高性能计算**：Rust实现核心逻辑，保障内存安全与执行效率
- **无缝集成**：提供标准化接口与ComfyUI原生节点深度兼容
- **模块化架构**：支持灵活扩展与功能定制
- **预置功能集**：包含图像处理、文本生成等AI任务常用节点

项目配备完善的技术文档与部署方案，适合具备Rust/ComfyUI基础的开发者快速上手。

## 编译

### 环境搭建与编译文档

- [后端开发指南](docs/后端开发指南.md)
- [Maturin使用指引](docs/Maturin使用指引.md)

### 编译与本地部署

```shell
git clone git@github.com:silent-rain/ComfyUI-SilentRain.git

cd ComfyUI-SilentRain

# 编译
./scripts/build.sh

# 部署到comfyui中(注意调整comfyui安装路径)
./scripts/develop_comfyui.sh

# 提交到master分支
# 将nodes/comfyui_silentrain提交到master分支, 后续考虑拆分
```

## ComfyUI 使用

ComfyUI Manager中搜索 `ComfyUI-SilentRain` 安装.

或者使用命令行安装

```shell
comfy node install ComfyUI-SilentRain
```

## 发版

```shell
uv run comfy node publish
```

## 工作流示例

- [工作流示例](workflow)

## 参考文档

- [comfyanonymous/ComfyUI](https://github.com/comfyanonymous/ComfyUI)
- [节点注册](https://registry.comfy.org)
