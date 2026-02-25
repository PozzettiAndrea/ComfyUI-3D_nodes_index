# ComfyUI Character Selector + Action

支持「角色 × 动作」二维下拉，自动拼接提示词。

## 安装
把本目录放入 `ComfyUI/custom_nodes/` 后重启。

## 添加角色/动作
- 编辑 `characters.json` 增加角色
- 编辑 `actions.json` 增加动作，可用 `{character}` 占位符自动替换角色描述

## 使用
1. 添加节点  
2. 选角色 → 选动作  
3. 连接 `positive` 到 `CLIPTextEncode`  
4. 生成
