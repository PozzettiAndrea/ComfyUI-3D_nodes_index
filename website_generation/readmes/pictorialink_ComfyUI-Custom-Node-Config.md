# ComfyUI-Custom-Node-Config

## 简介

本项目为 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 的自定义节点插件，提供一个表单节点用于配置和保存 LLM（如 OpenAI、Kimi、DeepSeek）相关参数。用户可通过节点输入 API Key、Base、Version、Model 等信息，节点会自动保存配置到本地文件，并设置为环境变量，方便后续调用。

---

## 安装方法

1. **克隆或下载本仓库**  
   将本插件放入你的 ComfyUI `custom_nodes` 目录下，例如：
   ```
   git clone https://github.com/pictorialink/ComfyUI-Custom-Node-Config.git
   # 或直接复制文件夹到 ComfyUI/custom_nodes/
   ```

2. **重启 ComfyUI**  
   启动或重启 ComfyUI，插件会被自动加载。

---

## 节点功能

- **表单输入**：支持选择 LLM 类型（OpenAI/Kimi/DeepSeek），并填写 API Key、API Version、API Base、API Model。
- **配置保存**：提交后自动将配置信息保存到 `custom_nodes/ComfyUI-Custom-Node-Config/files/config.json` 文件。
- **环境变量设置**：自动将配置信息写入环境变量，方便后续节点或脚本读取。

---

## 使用方法

1. 在 ComfyUI 工作流界面，添加 `FormSubmitNode` 节点（在“Form Submit”分类下）。
2. 在节点表单中填写相关参数。
3. 运行节点，参数会被保存到本地文件，并设置为环境变量。
4. 其他节点或脚本可通过读取环境变量或配置文件获取参数。

---

## 文件结构

```
custom_nodes/ComfyUI-Custom-Node-Config/
├── nodes/
│   └── form_submit_node.py      # 主节点实现
├── files/
│   └── config.json              # 配置保存文件
└── README.md
```

---

## 代码说明

- `form_submit_node.py`  
  实现了 `FormSubmitNode` 类，定义了输入表单、参数保存逻辑和环境变量设置。

- `config.json`  
  自动生成，用于持久化保存表单参数。

---

## 常见问题

- **Q: 为什么节点没有显示自定义 HTML 表单？**  
  A: ComfyUI 仅支持通过 `INPUT_TYPES` 定义的标准输入控件，不支持直接渲染自定义 HTML。

- **Q: 配置文件保存在哪里？**  
  A: 默认保存于 `custom_nodes/ComfyUI-Custom-Node-Config/files/config.json`。

- **Q: 如何扩展表单字段？**  
  A: 修改 `form_submit_node.py` 中 `INPUT_TYPES` 和 `func` 方法即可。

---

## 许可证

MIT License

---

## 联系方式

如有问题或建议，请提交 Issue 或 PR。