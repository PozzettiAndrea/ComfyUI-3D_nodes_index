# comfyui-jsonprompt

![preview](https://raw.githubusercontent.com/wwzhifeng/comfyui-jsonprompt/main/images/001.png)

这是一个给 ComfyUI 用的 JSON 提示词节点，可以把结构化的 JSON 文本展开成一条普通的 prompt，方便给 Gemini、Flux、OpenAI、Nanobanana、Sora 等模型使用。

## 安装方式

把本仓库 clone 到 ComfyUI 的 `custom_nodes` 目录下：

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/wwzhifeng/comfyui-jsonprompt.git
```

## 使用方式

插件会新增一个节点：

**JSON Prompt Builder（ZhiFeng）**

输入：

- **json_text**：JSON 字符串  
- **joiner**：拼接分隔符（默认 ", "）

输出：

- **prompt**：转换后的普通提示词

## 作者

ZhiFeng（王知风）  
https://wangzhifeng.vip
