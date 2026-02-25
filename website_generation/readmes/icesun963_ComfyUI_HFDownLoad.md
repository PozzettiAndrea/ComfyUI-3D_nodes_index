forked from smthemex/ComfyUI_Pipeline_Tool

简单修改：
ComfyUI Huggingface 下载工具。
很多节点并不提供自动下载，只提供XXX模型，下载到XXX目录。
为了方便使用进行了简单的修改。
Python技能不多，代码较丑，各位见谅。

C站 可搬运到Huggingface再进行下载。

1.支持子目录选项

2.支持绝对路径

3.支持添加自定义代理

新增：
1.增加 EasyOCR V2 节点搬运自：https://github.com/prodogape/ComfyUI-EasyOCR 
为批处理进行加速。

2.增加 Lama V2 节点，搬运自：https://github.com/chflame163/ComfyUI_LayerStyle
为批处理加速。

3.增加 SegmentAnythingUltra V2.1 节点，搬运自：https://github.com/chflame163/ComfyUI_LayerStyle
修复批量图片中出错后直接截断的bug