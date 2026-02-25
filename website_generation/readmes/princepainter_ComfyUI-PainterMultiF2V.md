**PainterLongVideo - 分镜头长视频生成套件，可以一次生成15秒视频**

<img width="1706" height="1129" alt="image" src="https://github.com/user-attachments/assets/a6bef8cc-771e-47e5-ad20-56ddaec4ddc3" />

一键将多张关键帧图串联成连贯长视频，自动处理片段衔接与过渡。

**包含节点**

<img width="1550" height="607" alt="image" src="https://github.com/user-attachments/assets/58b13150-193d-4750-8658-912d61d53703" />


- **PainterPrompt**：管理多段提示词，支持批量输出
- 
- **PainterMultiF2V**：按顺序生成首尾帧控制的视频片段
- 
- **PainterCombineFromBatch**：自动叠化拼接多段视频，支持裁切与淡入淡出


**工作流程**

1. 准备关键帧图片（首张→中间过渡→尾张）
2. 在 PainterPrompt 中填写每段视频的提示词
3. PainterMultiF2V 按顺序生成各片段潜空间
4. 采样后通过 PainterCombineFromBatch 合并为完整长视频

