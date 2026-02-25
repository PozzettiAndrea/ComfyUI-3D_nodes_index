# PainterImageLoad 此节点由抖音博主：绘画小子 制作 
PainterImageLoad，一个 ComfyUI 节点：保存、预览并向下游节点传递图像，同时支持“仅执行此节点”中途遮罩编辑。
<img width="2886" height="1051" alt="Y}19GFM8IJ$B(U}57Q3AU6D" src="https://github.com/user-attachments/assets/2f70dd3f-5d02-4445-bb34-7109e95b7ae9" />

## 功能 | Features
- 自动将输入张量保存为 `painter_sync.png` 到 input 目录  
- 在节点内即时预览，方便确认
- 也可以手动选择上传图片
- 提取或生成 Alpha 遮罩，与图像一起输出  
- 右键“仅执行此节点”，然后打开遮罩编辑器，可对生成的图片进行遮罩编辑。修改后即时生效，后续节点直接获取最新遮罩  

## 用法 | Usage
1. 将本文件放入 `custom_nodes` 并重启 ComfyUI  
2. 在流程中添加 **PainterImageLoad**  
3. 连接图像输入 → 节点自动保存并显示预览  
4. 需要编辑遮罩：右键节点 → **Execute Selected Nodes** → 用内置遮罩编辑器修改 → 保存  
5. 下游节点立即收到更新后的图像与遮罩，无需重新运行整个流程  

## 输入输出 | I/O
| 名称 | 类型 | 说明 |
|---|---|---|
| image | IMAGE | 输入图像张量 |
| image_name | STRING | 文件名（仅用于前端展示） |
| 输出图像 | IMAGE | 原图张量 |
| 输出遮罩 | MASK | 0-1 浮点遮罩 |

## 许可证 | License
MIT
