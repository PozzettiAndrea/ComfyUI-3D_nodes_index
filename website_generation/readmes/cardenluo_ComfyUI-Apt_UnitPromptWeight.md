[中文](#中文) | [English](#english)

<a id="english"></a>
# Unit Prompt Weight

A powerful ComfyUI node for precise control of prompt weights, supporting multiple processing modes and visual weight allocation.

<img width="3210" height="1586" alt="image" src="https://github.com/user-attachments/assets/c0b7a6c0-4faf-4c3c-85a5-0990bb75e038" />


## Core Working Principle

### Weight Parsing Algorithm

The Unit Prompt Weight node employs an advanced **Semantic Weight Dynamic Allocation Algorithm**, which achieves precise control of prompt weights through a multi-stage processing flow:

1. **Regular Expression Pattern Matching**: Uses an optimized regular expression `\[([^\]]+)@([0-9.]+)\]` for semantic-weight pair identification, which can accurately capture nested structures and edge cases.
   
2. **Text Segmentation Processing**: Adopts **Adaptive Segment Segmentation** strategy, which can intelligently identify structured information in prompts. The algorithm first identifies core semantic units with weight markers (such as `[girl@1.5]`) through regular expressions, then processes unmarked parts as context units with default weight (1.0). This method ensures accurate capture of user semantic intent even in complex prompt structures, while preserving natural language coherence. The segmentation process also includes text cleaning steps to automatically remove excess punctuation and whitespace characters, optimizing subsequent encoding efficiency.
   
3. **Weight Vector Normalization**: Executes **L1-Norm Normalization**, a key technique for maintaining numerical stability in high-dimensional feature spaces. The algorithm first calculates the absolute sum of all weight values, then divides each weight by this sum to ensure the normalized weight vector satisfies the unit L1 norm constraint. This normalization method is particularly suitable for prompt weight adjustment scenarios as it maintains the relative proportional relationships of weights while preventing numerical overflow or gradient vanishing problems. When all weights are detected to be equal, the algorithm automatically switches to uniform distribution mode, simplifying the calculation process.
   
4. **Independent Feature Encoding**: Performs **CLIP Context-Aware Encoding** on each semantic segment, which fully leverages the powerful semantic understanding capabilities of the CLIP model. Each segment is individually input into CLIP's text encoder to generate 768-dimensional high-dimensional feature representations. The encoding process preserves the complete contextual information of each semantic unit, ensuring that combined concepts like "girl with umbrella" are correctly understood as a whole rather than a simple bag-of-words model. For encoding failures, the algorithm implements graceful degradation processing to ensure the robustness of the entire process.
   
5. **Weighted Feature Fusion**: Applies **Linear Weighted Fusion** strategy, an advanced technique for achieving precise semantic weight control in feature space. The algorithm first performs alignment processing on feature vectors of different lengths (especially in qwen-image mode), then executes convex combination operations based on normalized weight vectors. This fusion method ensures that the final conditional embedding can accurately reflect the user's weight intentions while maintaining the geometric properties of the feature space. The fusion process also implements balance control between the overall prompt and individual weighted segments, providing additional adjustment freedom through the main_prompt_ratio parameter.

### Feature Fusion Mechanism

The node implements two key feature fusion mechanisms:

1. **Individual Feature Fusion**: Fuses features of each segment with different weights according to weight proportions
2. **Overall and Individual Balance**: Controls the balance between the overall prompt and individual weighted segments through the `main_prompt_ratio` parameter

## Features

- **Prompt Weight Adjustment**: Use `[semantic@weight]` syntax to enhance or weaken specific semantics
- **Multiple Processing Modes**: Supports normal, flux2.klein, z-image, qwen-image and other processing modes
- **Weight Ratio Adjustment**: Adjust the ratio between overall prompt and individual weights through the `main_prompt_ratio` parameter
- **Weight Visualization**: Real-time display of weight allocation information in the format `Weight allocation: main_prompt(overall content)percentage%|part1 percentage%|part2 percentage%|...`
- **Automatic Weight Processing**: Automatically sets `main_prompt_ratio` to 1.0 when no custom weights are present, automatically processes separators, ensures weight sum is 100%

## Installation Method

1. Download this plugin
2. Copy the `ComfyUI-Apt_UnitPromptWeight` folder to the `custom_nodes` directory of ComfyUI
3. Restart ComfyUI

### Prompt Syntax

- Default weight is 1.0
- Use `[semantic@weight]` syntax to set weights for specific semantics
- Weight range: 0~10, less than 1 means weakening, greater than 1 means strengthening

## Node Parameter Description

### Key Parameter Description

- **mode**: Processing mode, optional values: normal, flux2.klein, z-image, qwen-image (default is normal)
- **main_prompt_ratio**: Overall prompt proportion, range 0.0~1.0 (default is 0.5)

## Example Workflows

### Style Enhancement Example

```
Unit Prompt Weight
  clip: CLIP model
  pos: "[3d style@2.0], girl with umbrella, [sunlit park@1.5]"
  neg: "ugly, blurry, bad art, poor quality"
  mode: "flux2.klein"
  main_prompt_ratio: 0.6
```

### Style Weakening Example

```
Unit Prompt Weight
  clip: CLIP model
  pos: "high quality photo, [3d rendering style@0.3], [girl@1.2] walking in the rain"
  neg: "cartoon, anime, illustration"
  mode: "z-image"
  main_prompt_ratio: 0.7
```

## Update Log

### v1.0.0
- Initial version release
- Support for multiple processing modes
- Implementation of weight visualization functionality

---
<details id="chinese-details">
<summary><strong>中文</strong></summary>

<a id="中文"></a>
# Unit Prompt Weight

一个功能强大的ComfyUI节点，用于精确控制提示词权重，支持多种处理模式和可视化权重分配。

## 核心工作原理

### 权重解析算法

Unit Prompt Weight节点采用了先进的**语义权重动态分配算法**（Semantic Weight Dynamic Allocation Algorithm），该算法通过多阶段处理流程实现对提示词权重的精确控制：

1. **正则表达式模式匹配**：使用优化的正则表达式`\[([^\]]+)@([0-9.]+)\]`进行语义-权重对的识别，该模式能够准确捕获嵌套结构和边缘情况
   
2. **文本片段化处理**：采用**自适应片段分割策略**（Adaptive Segment Segmentation），该策略能够智能识别提示词中的结构化信息。算法首先通过正则表达式识别带权重标记的核心语义单元（如`[女孩@1.5]`），然后将未标记部分作为默认权重（1.0）的上下文单元处理。这种方法确保了即使在复杂的提示词结构中，也能准确捕捉用户的语义意图，同时保留自然语言的连贯性。分割过程中还包含文本清洗步骤，自动移除多余的标点符号和空白字符，优化后续编码效率。
   
3. **权重向量归一化**：执行**L1范数归一化**（L1-Norm Normalization），这是一种在高维特征空间中保持数值稳定性的关键技术。算法首先计算所有权重值的绝对和，然后将每个权重除以该总和，确保归一化后的权重向量满足单位L1范数约束。这种归一化方法特别适合提示词权重调整场景，因为它能保持权重的相对比例关系，同时防止数值溢出或梯度消失问题。当检测到所有权重相等时，算法会自动切换到均匀分布模式，简化计算流程。
   
4. **独立特征编码**：对每个语义片段执行**CLIP上下文感知编码**（Context-Aware Encoding），这一步骤充分利用了CLIP模型的强大语义理解能力。每个片段被单独输入到CLIP的文本编码器中，生成768维的高维特征表示。编码过程保留了每个语义单元的完整上下文信息，确保"女孩打伞"这样的组合概念被正确理解为一个整体，而不是简单的词袋模型。对于编码失败的情况，算法实现了优雅的降级处理，确保整个流程的鲁棒性。
   
5. **加权特征融合**：应用**线性加权融合策略**（Linear Weighted Fusion），这是一种在特征空间中实现语义权重精确控制的高级技术。算法首先对不同长度的特征向量进行对齐处理（特别是在qwen-image模式中），然后根据归一化权重向量执行凸组合操作。这种融合方式确保了最终的条件嵌入能够精确反映用户的权重意图，同时保持特征空间的几何特性。融合过程中还实现了整体提示词与个体加权片段之间的平衡控制，通过main_prompt_ratio参数提供额外的调整自由度。

### 特征融合机制

节点实现了两种关键的特征融合机制：

1. **个体特征融合**：将带有不同权重的各个片段特征按照权重比例进行融合
2. **整体与个体平衡**：通过`main_prompt_ratio`参数控制整体提示词与个体加权片段之间的平衡



## 功能特性

- **提示词权重调整**：使用`[语义@权重值]`语法来增强或减弱特定语义
- **多种处理模式**：支持normal、flux2.klein、z-image、qwen-image等多种处理模式
- **权重比例调节**：通过`main_prompt_ratio`参数调节整体提示词与个体权重的比例
- **权重可视化**：实时显示权重分配信息，格式为`权重分配：main_prompt(整体内容)占比%|部分1占比%|部分2占比%|...`
- **自动权重处理**：无自定义权重时自动设`main_prompt_ratio`为1.0，自动处理分隔符，确保权重总和为100%

## 安装方法

1. 下载本插件
2. 将`ComfyUI-Apt_UnitPromptWeight`文件夹复制到ComfyUI的`custom_nodes`目录下
3. 重启ComfyUI

### 提示词语法

- 默认权重为1.0
- 使用`[语义@权重值]`语法来设置特定语义的权重
- 权重值范围：0~10，小于1表示减弱，大于1表示增强

## 节点参数说明

### 关键参数说明

- **mode**：处理模式，可选值：normal、flux2.klein、z-image、qwen-image（默认为normal）
- **main_prompt_ratio**：整体提示词占比，范围0.0~1.0（默认为0.5）




## 示例工作流

### 风格增强示例

```
Unit Prompt Weight
  clip: CLIP模型
  pos: "[3d风格@2.0]，女孩打伞，[阳光下的公园@1.5]"
  neg: "ugly, blurry, bad art, poor quality"
  mode: "flux2.klein"
  main_prompt_ratio: 0.6
```

### 风格减弱示例

```
Unit Prompt Weight
  clip: CLIP模型
  pos: "高质量照片，[3d渲染风格@0.3]，[女孩@1.2]在雨中漫步"
  neg: "cartoon, anime, illustration"
  mode: "z-image"
  main_prompt_ratio: 0.7
```

## 更新日志

### v1.0.0
- 初始版本发布
- 支持多种处理模式
- 实现权重可视化功能


</details>


