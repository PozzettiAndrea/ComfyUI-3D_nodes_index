# ComfyUI_Element_easy


3个方便我自己使用的小节点，我不是程序员，所以可能不会继续更新。

Empty Image RGB：支持RGB和16位色彩信息输入，节点会自动识别色彩信息color_code。输出纯色图像，附带图像尺寸输出端口,图像尺寸会根据divisibale_by（整除）取近似值。

Text Line Break： 将输入的文本按字符数量换行，支持中文、英文和中英文混搭，支持标点符号避首尾。方便将提示词与生成的图像连接到一起，这要借助其它的节点，例如：Kjnode中的Add Label节点。

Random Chars (Append)：为输入的文本添加无效的特殊字符（可以自定义字符和个数），主要是为了不破坏提示词意图的前提下使生成的图像有更大的变化（不知是否起作用），因为qwen_image 和Z_image模型生成的图像构图的随机变化小。这里的“无效”是相对的。
                       可简单设置插入位置（before,end,insert）,其中insert的插入方式是将字符个数平均分配插入到原文本的每个标点符号后面，从后向前分配。




<img width="1590" height="1080" alt="节点截图 2025-12-04 164008" src="https://github.com/user-attachments/assets/1cdacfe2-7c7a-4434-9f48-1ec571bb19ab" />



## Version
**v0.0.8**

  添加Image Noise Using Mask节点，方便在图像的mask区域添加随机噪点，可调整噪点大小，透明度，可选择是否为灰度模式。
  
  添加Image Pad & Blur节点， terget width 和 terget height，有输入时会自动计算扩展（当参数小于原图像时为clip模式），此时aligment参数生效，可选择对齐模式（中心对齐、左对齐、右对齐、上对齐、下对齐、左上对齐、左下对齐、右上对齐、右下对齐）。
  pad模式可选择constant、reflect、edge，另一个和reflect效果相同。当选择constant模式时，feathering控制整体模糊程度，content_blur控制原图像扩展出的区域模糊度。constant模式时，background_color参数生效，兼容rgb色和HEX色码（16位色码）。

<img width="1724" height="878" alt="屏幕截图 2026-01-17 134457" src="https://github.com/user-attachments/assets/17b9af6d-e8d2-4c35-9e13-6822e6bfa266" />
<img width="2147" height="1092" alt="屏幕截图 2026-01-17 134251" src="https://github.com/user-attachments/assets/e864a294-c70c-4409-9573-c357b6437158" />

  

  
## Version
**v0.0.7**

  添加Mask Stroke节点，mask描边，支持内外描边宽度和模糊度单独控制,支持非描边区域整体添加权重（使输出的mask没有权重为0的区域）。
  
  <img width="1295" height="731" alt="节点截图 2025-12-05 011534" src="https://github.com/user-attachments/assets/56b86fb6-758a-4d6c-8fa1-997b6bc9ee9d" />

  
## Version
**v0.0.6**

