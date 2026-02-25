Simple yolov8 comfyui plugin. This plugin adds Yolov8DetectionSegmentation node and ImageCompositeBlurred node.

Yolov8DetectionSegmentation detects and crops an input image.

ImageCompositeBlurred blurs image borders and overlaps the image at the target location.

## Install

1. Install from the manager
2. put detect or seg models in comfyui `models/yolov8` dir

## How to use

If your yolov8 model has "seg" or "Seg" or "SEG" in the name, the node outputs segmentation mask.

Node name is Yolov8DetectionSegmentation and ImageCompositeBlurred.

### Sample workflow
![](https://github.com/dskjal/comfyui-yolov8-simple/blob/main/simple-yolov8-workflow-example-v2.png)

#### Segmentation workflow

![](https://github.com/dskjal/comfyui-yolov8-simple/blob/main/simple-yolov8-workflow-seg-example-v3.png)

### Mask

Mask output size equals imput image size.

Cropped mask size equals cropped image size.

### Why stop when nothing is detected?

To skip detailer when nothing is detected, it requires gate node.

It would be OOM if it returns an input image when nothing is detected.

If you want to handle these, use [comfyui-yolov8-dsuksampler](https://github.com/dskjal/comfyui-yolov8-dsuksampler/tree/main).






