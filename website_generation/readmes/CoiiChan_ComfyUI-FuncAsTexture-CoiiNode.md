# Guide to Using CustomScript-Numpy Nodes
[English](https://github.com/CoiiChan/ComfyUI-FuncAsTexture-CoiiNode)|[中文](https://github.com/CoiiChan/ComfyUI-FuncAsTexture-CoiiNode/blob/main/README_CN.md)
## Overview
It allows for mathematical operations on input images and precise manipulation of channels through NumPy formulas, making it suitable for ComfyUI users with programming experience.

![overview](https://github.com/CoiiChan/Comfyui-FuncAsTexture-CoiiNode/blob/main/example/Overview.png?raw=true)

I hope that the calculation weights for basic images will no longer rely on guessing and trial - and - error, but instead have clear and visible rules.

This is because it's often difficult to distinguish the weight combinations of blending modes like normal, screen, and overlay, and it's even hard to find a Max (image a, image b) operation.

The main node is inspired by the Custom node in the Unreal Engine Material Editor.

![inspiredfromUE5](https://github.com/CoiiChan/ComfyUI-FuncAsTexture-CoiiNode/blob/main/example/inspiredfromUE5.png?raw=true)

## Core Functions
## Explanation of Input Parameters for the Main Node

| Parameter Name | Required | Description |
|--------|------|------|
| imga   | No   | The main input image, which is automatically decomposed into three channels: imga_r, imga_g, and imga_b, and serves as a reference for the output size. |
| imgb   | No   | An optional input image. If not provided, a zero - filled array is used. |
| imgc   | No   | An optional input image. If not provided, a zero - filled array is used. |
| pfloat1~3  | No   | Optional floating - point parameters that can accept negative values. The default value is 0.0, used for script calculations. |
| pint1~2  | No   | Optional integer parameters that can accept negative values. The default value is 0, used for script calculations. |
| formula| Yes  | Multi - line NumPy operation formulas used to process image data. |

![mainnode](https://github.com/CoiiChan/ComfyUI-FuncAsTexture-CoiiNode/blob/main/example/mainnode.png?raw=true)

## Notes
1. `import numpy as np` is included by default, so it can be omitted in the text. Use the assignment `result` for output.
2. The output will be automatically converted to a 4D tensor format `[:,H,W,C]`. The height and width (H, W) of the output are the same as the input `imga` by default. If `imga` is missing, they are set to 512, 512.
3. The multi - line text `formula` can use all NumPy mathematical functions (e.g., `np.sin`, `np.exp`, matrix calculations, and conditional statements).
4. When calculating multiple input images, pay attention to whether their resolutions need to be the same to avoid errors.

## Derived Nodes
- The derived nodes of the main node serve as usage examples and can be used directly or their function scripts can be modified directly.
- Derived nodes remove input items and parameter input ranges that are not needed by the node itself to make them more user - friendly.
- Learners studying NumPy calculations can copy the multi - line text of the derived node functions to the main node for verification and self - expansion.

The derived nodes include:

| Node Name | Description |
| --- | --- |
| Subtraction | Performs a subtraction operation on two optional input images and assigns the result to `result`. |
| Multiply | Performs a multiplication operation on two optional input images and assigns the result to `result`. |
| Divided | Performs a division operation on two optional input images and assigns the result to `result`. |
| Max | Takes the maximum value at the corresponding positions of two optional input images and assigns the result to `result`. |
| Min | Takes the minimum value at the corresponding positions of two optional input images and assigns the result to `result`. |
| Dot | Calculates the dot product of two optional input images on the last axis and assigns the result to `result`. |
| Distance | Calculates the Euclidean distance between the corresponding positions of two optional input images and assigns the result to `result`. |
| Power | Performs a power operation on the optional input image `imga`, where the exponent is specified by `pfloat1`, and assigns the result to `result`. |
| HueShift | Performs a hue shift on the optional input image `imga`, where the shift angle is specified by `pfloat1`, and assigns the result to `result`. |
| Panner | Performs a translation operation on the optional input image `imga`, where the offsets in the x and y directions are specified by `pint1` and `pint2` respectively, and assigns the result to `result`. |
| Outline | Implements four - way offset convolution. It calculates the images after shifting the input image left, right, up, and down by `pint1` pixels respectively, sums them, takes the average, and then subtracts the original image to obtain the image outline. |
| Lerp | Performs a linear interpolation between two optional input images `imga` and `imgb` based on the floating - point number `pfloat1`, and assigns the result to `result`. |
| Clamp | Limits the pixel values of the optional input image `imga` to the range specified by `pfloat1` and `pfloat2`, and assigns the result to `result`. |
| Ceil | Rounds up each pixel value of the optional input image `imga` and assigns the result to `result`. |
| 1 - x | Performs the operation of 1 minus each pixel value of the optional input image `imga` and assigns the result to `result`. |
| Sine | Calculates the sine value of each pixel value of the optional input image `imga` and assigns the result to `result`. |
| DDX | Performs a differential operation on the optional input image `imga` in the x - direction and assigns the result to `result`. |
| Contant3Vector(Color) | Create RGB solid color images using constants. |
| if (FuncAsTexture) | Based on the comparison result between `imga` and the constant `pfloat1`, it selects `imgb` or `imgc` as the output and assigns the result to `result`. |
| Chroma_Key_Alpha | Implements the green screen keying function. It converts the image from the RGB color space to the HSV color space, defines the green range, creates and feathers the mask, and finally applies the mask to the image. |
| Desaturation | Desaturation of Image 'imga' Using Three Channel Mean Method. |

## Texture Expansion Nodes

| Node Name | Description |
| --- | --- |
| UV Coordinate Generator | Creates a UV texture. |
| Texture Sampler | Performs a sampling transformation guided by UV coordinates. |
| Inverse UV Map Generator | Solves the inverse - transformed UV map from the input UV map. It is a beta version and is not suitable for images with too many pixels. |
| Rotator | Rotates the texture map. |

![extensionnode](https://github.com/CoiiChan/ComfyUI-FuncAsTexture-CoiiNode/blob/main/example/extension.png?raw=true)

## More Reference Links
- [NumPy Mathematical Functions](https://numpy.org/doc/stable/reference/routines.math.html)
- [NumPy Statistical Functions](https://numpy.org/doc/stable/reference/routines.statistics.html)
- [NumPy Linear Algebra](https://numpy.org/doc/stable/reference/routines.linalg.html)
- [Image Processing Techniques](https://docs.opencv.org/4.x/d2/d96/tutorial_py_table_of_contents_imgproc.html)

## Basic Operation Examples
### 1. Image Blending Operations
```python
# Simple addition
result = (imga + imgb) * 0.5
```
### 2. Channel Operations
```python
# Since it is frequently used, the `makergb(r, g, b)` function has been initially defined to combine three channels, and the parameters `imga_r`, `imga_g`, and `imga_b` are defined as copies of the r, g, and b channel values of `imaga`.
#Default already import numpy as np
imga_r = (imga_r + imga_g) * 0.5
imga = makergb(imga_r, imga_g, imga_b)
result = imga

# Weighted blending
result = imga*0.7 + imgb*0.3

# Binarization processing
threshold = 0.5
result = np.where(imga > threshold, 1.0, 0.0)# Convert RGB to grayscale
gray = 0.299 * imga_r + 0.587 * imga_g + 0.114 * imga_b
result = makergb(gray, gray, gray)
```
## Advanced Application Examples
### 3. mage Processing Effects
```python
# Edge detection (3x3 Sobel operator)
kernel_x = np.array([[-1,0,1], [-2,0,2], [-1,0,1]])
kernel_y = np.array([[-1,-2,-1], [0,0,0], [1,2,1]])
edge = np.sqrt(np.sum(kernel_x * imga[1:-1,1:-1])**2 + 
              np.sum(kernel_y * imga[1:-1,1:-1])**2)
result = makergb(edge, edge, edge)
```
### 4.Special Effects Processing
```python
# Add random noise
noise = np.random.random(imga.shape) * 0.1
result = np.clip(imga + noise, 0, 1)

# Green screen keying to obtain Alpha
#Choma threshold: pfloat1
#Soft Blend: pfloat2
imgb =imgc + imgb[0, 1, 1, :]
chomachannel = np.sum((imga * imgb), axis=-1)
softmask = chomachannel - np.sum(imga , axis=-1)/3
result = 1- np.ceil(softmask - pfloat1) - softmask * pfloat2
```

---
[![CoiiChan](https://avatars.githubusercontent.com/u/49615294?v=4)](https://github.com/CoiiChan)

The author will not create an all - in - one node package because nodes for various application scenarios have dependency requirements, and a large - scale tool would be very inconvenient to install.

Give a star to follow. An i person creating specialized custom nodes.
