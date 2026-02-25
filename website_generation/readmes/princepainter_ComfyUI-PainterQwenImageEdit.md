#  此2个节点由抖音博主：绘画小子 制作

#  1，ComfyUI-PainterQwenImageEditPlus 编辑图片无像素偏移

<img width="1811" height="802" alt="image" src="https://github.com/user-attachments/assets/0ddf26af-aa7f-4b74-8226-28ecb134d76d" />


# 基于Qwen-image-2511的图像编辑自定义节点，专为ComfyUI设计，提供像素级精准编辑和局部遮罩重绘功能。


![2026-01-06_18-00-25](https://github.com/user-attachments/assets/85890e0c-9a85-47c0-9ffd-66d882c5e318)



<img width="2590" height="1360" alt="image" src="https://github.com/user-attachments/assets/35eab8f9-f90b-43c6-93cd-ef8c6267b6df" />


<img width="2468" height="1169" alt="image" src="https://github.com/user-attachments/assets/7f65122c-817a-4f82-b483-4155eea32842" />


## ✨ 核心特性

- **像素零偏移**：当输出尺寸与原图比例一致时，自动启用填充模式，确保编辑前后像素位置完全对应
- **局部遮罩编辑**：支持连接遮罩实现仅对指定区域进行修改，其余像素保持不变
- **智能比例检测**：自动识别输入/输出宽高比，匹配时自动启用无偏移模式
- **三图参考**：支持同时输入3张参考图像，强化编辑指令的准确性

## 🎯 节点介绍

### PainterQwenImageEditPlus

增强版Qwen图像编辑节点，集成像素保护和遮罩编辑功能。


## 📝 使用示例

### 示例1：整图编辑
```python
# 修改整幅图像，输出1024x1024
PainterQwenImageEditPlus:
  image1: "input.jpg"
  width: 1024
  height: 1024
  prompt: "将场景改为日落时分，增加暖色调"
```

### 示例2：局部遮罩编辑（无偏移）
```python
# 当width/height与image1比例一致时，自动启用像素保护
PainterQwenImageEditPlus:
  image1: "car.jpg"          # 原图尺寸 1920x1080
  image1_mask: "mask.png"    # 白色区域为需要修改的部分
  width: 1920                 # 与原图比例一致 16:9
  height: 1080
  prompt: "将汽车改为红色跑车，其他区域保持完全一致"
```

### 示例3：多参考图编辑
```python
PainterQwenImageEditPlus:
  image1: "main_scene.jpg"
  image2: "style_reference.jpg"
  image3: "object_reference.jpg"
  width: 1024
  height: 1024
  prompt: "将image1的风格改为image2的油画风格，并添加image3中的花瓶"
```

## ⚙️ 关键参数说明

-  **`image1_mask`遮罩**  ：
  - 支持2D格式 `[H, W]` 或3D格式 `[B, H, W]` 
  - 白色（值=1.0）：AI编辑区域
  - 黑色（值=0.0）：原图保留区域
  
-  **"无偏移模式"**  ：
  - 自动检测：当 `width/height` 与 `image1` 的宽高比差值 < 1% 时触发

- **分辨率要求**：
  - `width` 和 `height` 必须是8的倍数
  - 推荐值：512, 768, 1024, 1344, 1536, 2048

## 💡 使用技巧

1. **确保零偏移**：计算输出尺寸 `width / height ≈ 原图宽 / 原图高`
2. **遮罩质量控制**：遮罩边缘建议羽化，避免生硬过渡
3. **参考图选择**：参考图越多，AI对指令的理解越准确
4. **批量处理**：可通过调整width/height快速切换分辨率

## 🎨 典型应用场景

- **换装/换妆**：遮罩人物衣服或面部，局部修改
- **物体替换**：遮罩待替换物体，描述新物体
- **背景替换**：遮罩前景主体，更换背景
- **多图融合**：参考多张图像的风格/元素进行创作
# ,2，ComfyUI-PainterQwenImageEdit

**Qwen多图编辑增强节点** | 支持8图输入 · 双条件输出 · 背景层优先
<img width="2708" height="1072" alt="image" src="https://github.com/user-attachments/assets/5a3056da-16ca-46fd-9645-f5e77ef0353e" />

---

## 功能特点
<img width="2144" height="756" alt="image" src="https://github.com/user-attachments/assets/553cb7b0-0d34-4a81-9643-4a3c8256bede" />

### 🎨 **八图协同编辑**
- **1张背景图** + **7张叠加图**的完整工作流程
- 背景图自动置于token序列首位，确保合成基准
- 所有图像输入均为**可选**，灵活适配不同场景

### ⚡ **双条件输出**
- **正面条件**：正常处理您的prompt和图像输入
- **负面条件**：自动生成零化(empty)条件，无需手动创建空提示词
- 输出端口清晰标注为"正面条件"和"负面条件"，直连KSampler使用

### 🎯 **原生功能完整保留**
- 完整支持Qwen的llama_template系统提示词
- 自动reference_latents编码（连接VAE时）
- 智能图像缩放（384px预览 + 1024px潜空间编码）
- 动态提示词(Dynamic Prompts)支持

---

## 安装方法

### 通过ComfyUI-Manager（推荐）
在Manager中搜索 `PainterQwenImageEdit` 直接安装

### 手动安装
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/princepainter/ComfyUI-PainterQwenImageEdit.git
```
安装后**重启ComfyUI**即可

---

## 节点参数说明

### 输入参数
| 参数 | 类型 | 说明 |
|------|------|------|
| `clip` | CLIP | 必需，CLIP模型 |
| `prompt` | STRING | 必需，编辑指令（支持多行和动态提示词） |
| `vae` | VAE | 可选，用于生成reference_latents |
| `background` | IMAGE | **可选**，背景图像（优先级最高） |
| `image1` - `image7` | IMAGE | 可选，叠加图像1-7 |

### 输出参数
| 参数 | 类型 | 说明 |
|------|------|------|
| `正面条件` | CONDITIONING | 处理后的正向条件，连至KSampler的`positive` |
| `负面条件` | CONDITIONING | 零化负向条件，连至KSampler的`negative` |

---

## 使用示例

**典型工作流：**
1. 加载背景图 → `background` 输入端
2. 加载前景元素 → `image1`, `image2` 等输入端
3. 输入编辑指令 → `prompt`（如："在背景上添加前景物体，保持风格一致"）
4. 连接CLIP和VAE
5. 输出直接连至 **KSampler** 的 `positive` 和 `negative` 端口

---

## 版本兼容

- **ComfyUI**: v0.6.0+ (支持传统节点格式)
- **Python**: 3.8+
- **框架**: 原生兼容ComfyUI的Qwen模型工作流

---


---

**问题反馈**：欢迎提交Issue或PR，好用请给我点个星星，多谢！🙏
