# RGB to CMYK for ComfyUI (Save as tif)

# Installation
Clone this repo into `custom_nodes` folder.

# Example
![example of use](/example/example.png)

# Note 
1.需要配置icc色彩配置文件，将他们放在`color_profiles`文件下\
2.rgb的icc色彩文件和cmyk的icc文件不能一样，否则会报错\
3.我测试下，当rgb的icc文件选择为`AppleRGB.icc`时，转换的色差最小，非专业人员，欢迎提出建议! \
4.提供了一些icc色彩配置文件在文件夹`color_profiles`里。
