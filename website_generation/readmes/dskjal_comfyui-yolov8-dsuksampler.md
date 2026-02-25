# comfyui-yolov8-dsuksampler
This node performs detection and segmentation, as well as upsampling, sampling, and blurring the composite.

This node pass through when nothing detected. When this node finds multiple objects, it performs an action on each object it finds.

## Why do we need this node?

[The simple detection and composite node](https://github.com/dskjal/comfyui-yolov8-simple) can't handle following case.

1. Nothing detected
2. Multiple objectes detected

Simple workflow can't skip sample phase when nothing detected and the simple node can't action on multiple objects.

## Install

1. Install from the manager
2. put detect or seg models in comfyui `models/yolov8` dir

## Sample workflow

![](https://github.com/dskjal/comfyui-yolov8-dsuksampler/blob/main/comfyui-yolov8-dsuksampler-sample-workflow-v2.png)

## Parameters

|Name|Description|
|:---|:---|
|padding pixel|Add padding to the detected box. This is useful for small parts. For example, it can be used on eyes, hands, nipples, etc.|
|threshold|The process is skipped if a confidence score is lower than the threshold. You can check the scores in debug detected area socket|
|scale pixel to|Cropped image is scaled to this resolution.|
