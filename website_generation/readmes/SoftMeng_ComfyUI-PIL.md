<div align="center">
    <img src="./image/icon.png" width="256px"/>
</div>
<div align="center">
    富强、民主、文明、和谐、合规
</div>
<div align="center">
    自由、平等、公正、法治、合法
</div>
<div align="center">
    爱国、敬业、诚信、友善、合理
</div>

# ComfyUI PIL Nodes

PIL Nodes, 提供了3个插件Nodes：

1. PIL TITLE (Mexx)   -- 增加留白
2. PIL Merge Image (Mexx) -- 合并图像
3. PIL Effects (Mexx) -- 图片特效
4. PIL Remove Black Dots (Mexx)  -- 给线稿脱色，去除一些黑色的噪点


## Workflow Example

[PIL图像处理DEMO.json](example/PIL%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%86DEMO.json)

## PIL TITLE (Mexx) & PIL Merge Image (Mexx)

![00007.jpg](image/00007.jpg)

## PIL Effects (Mexx)

### 原始
![Origin.jpg](image/Origin.jpg)
### 线稿-LINE0
![Mexx_0190.jpg](image/Mexx_0190.jpg)
### 线稿-LINE1
![Mexx_0191.jpg](image/Mexx_0191.jpg)
### 线稿-LINE2
![Mexx_0192.jpg](image/Mexx_0192.jpg)
### 线稿-LINE3
![Mexx_0193.jpg](image/Mexx_0193.jpg)
### 线稿-LINE3.1
![Mexx_0194.jpg](image/Mexx_0194.jpg)
### 线稿-LINE3.2
![Mexx_0195.jpg](image/Mexx_0195.jpg)
### 线稿-LINE4
![Mexx_0196.jpg](image/Mexx_0196.jpg)
### 线稿-LINE5
![Mexx_0197.jpg](image/Mexx_0197.jpg)
### 边缘检测-FIND_EDGES
![Mexx_0198.jpg](image/Mexx_0198.jpg)
### 轮廓-CONTOUR
![Mexx_0199.jpg](image/Mexx_0199.jpg)
### 灰度-L
![Mexx_0200.jpg](image/Mexx_0200.jpg)
### 锐化-SHARPEN
![Mexx_0201.jpg](image/Mexx_0201.jpg)
### 锐化-UNSHARP_MASK
![Mexx_0202.jpg](image/Mexx_0202.jpg)
### 边缘增强-EDGE_ENHANCE
![Mexx_0203.jpg](image/Mexx_0203.jpg)
### 边缘增强-EDGE_ENHANCE_MORE
![Mexx_0204.jpg](image/Mexx_0204.jpg)
### 浮雕-EMBOSS
![Mexx_0205.jpg](image/Mexx_0205.jpg)
### 平滑-SMOOTH
![Mexx_0206.jpg](image/Mexx_0206.jpg)
### 平滑-SMOOTH_MORE
![Mexx_0207.jpg](image/Mexx_0207.jpg)
### 细节-DETAIL
![Mexx_0208.jpg](image/Mexx_0208.jpg)
### 模糊-BLUR
![Mexx_0209.jpg](image/Mexx_0209.jpg)
### 模糊-BOX_BLUR
![Mexx_0210.jpg](image/Mexx_0210.jpg)
### 模糊-GAUSSIAN_BLUR
![Mexx_0211.jpg](image/Mexx_0211.jpg)
### 反相-INVERT
![Mexx_0212.jpg](image/Mexx_0212.jpg)
### 去燥-中值滤波器
![Mexx_0213.jpg](image/Mexx_0213.jpg)