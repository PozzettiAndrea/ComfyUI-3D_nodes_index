# ComfyUI-SuperUltimateVaceTools
超究VACE工具，一些基于万象2.1 VACE模型的Comfyui插件工具，尝试以更好的方式实现VACE的视频生成/编辑功能。  
SuperUltimateVaceTools, some Comfyui custom nodes for wan2.1 VACE, attempt to implement VACE video generation/editing in a better way.  
包含以下插件：  
Including following nodes:  

- 超究视频放大 | Super Ultimate Vace Upscale
- 超究长视频 | Super Ultimate VACE Long Video
- 更多功能待添加 | pending to add more...

## 1. SuperUltimateVaceUpscale
对视频进行分割放大，支持空间分割以及时间分割。  
Upscale video by splitting it into tiled areas, supports spatial tiling and temporal tiling.  

https://github.com/user-attachments/assets/ba9f91a1-b097-4ff2-9780-db85d014c978

### 空间分割 | Spatial tiling
默认情况下视频将由左向右、由上向下平均分割成矩形，分割块的数目由放大后尺寸与生成尺寸共同决定。块之间叠加区域同样由这些数值决定，为了避免出现明显分割痕迹，放大尺寸对生成尺寸取余的数值不能过小。  
如果不满足于默认的分割方案，可以尝试把`Custom Crop Area`节点连接到`croparea_list`，它有更多特殊的分割方案。  
By default, the video will be evenly divided into rectangles from left to right and top to bottom, with the number of segmentation blocks determined by both the upscale dimensions and the generate dimensions. The overlapping area between blocks is also determined by these values. In order to avoid obvious segmentation marks, the remainder value of upscaled to generated should not be too little.  
If you are not satisfied with the default segmentation plan, you can try connecting the `Custom Crop Area` node to the `croarea_ist`, which has more special segmentation plans.

### 时间分割 | Temporal tiling
当输入视频帧数比`length`设置值更大时，将启用时间分割，将视频分割为多个部分分别进行放大，最后拼接在一起。为了避免分割时间点出现跳变，需要设置适当的`crossfade_frame`作为过渡区域。  
如果输入视频是循环视频，希望放大后仍然保持首尾间无缝循环，应当设置适当的`loopback_crossfade`作为循环过渡区域。  
When the input video frame count is more than the `length` value, temporal tiling will be enabled, dividing the video into multiple parts for upscale, and finally splicing them together. To avoid sudden change in the segmentation time points, it is necessary to set an appropriate `crossfade-frame` as the transition part.   
If the input video is a looped video and you want to maintain seamless looping between the beginning and end after upscale, you should set an appropriate `loopback_crossfade` as the transition part for the loop.

### 参考和控制 | Reference and control
为了获得更加稳定的结果，建议使用参考图片和控制视频。参考图片最好是输入视频的第一帧的高清放大版本（因此本节点适合用于你用一张高清图片进行i2v结果的放大）  
当使用参考图片后，启用`crop_ref`将按照分割视频的方式分割参考图片，并在每个分割部分重绘时使用分割后的参考图进行该区域参考。启用`ref_as_init_frame`后会直接用参考图替换为视频的第一帧，并以此为参考指导各区域重绘生成。  
对于控制视频，VACE支持许多控制方法，你可以尽情尝试不同的控制方式带来的区别。
To get more controlable result, it is recommended to use reference image and control video. It is recommended that the reference image is a high-definition and detailed version of the first frame of the input video (therefore, this node is suitable for the situation when you are using a high-resolution image to do i2v and then upscale the i2v result)  
After using the reference image, enabling 'crop-ref' will divide the reference image according to the video segmentation plan, and use the segmented reference image for the region reference when denoising each segmented part. If enable 'ref_as_init_frame', the first frame of the video will be directly replaced with the reference image, and this will be used as a reference to guide the following frames denoising of each region.   
For control video, VACE supports many control methods, and you can freely try the differences brought by different control methods.

## 2. SuperUltimateVaceLongVideo
利用VACE拼接功能生成长视频，支持多种控制手段，自动修复过渡帧，缓解多轮接续生成带来的视频质量劣化  
Generate long length videos with the feature 'temporal extension' of VACE. Support many control methods, automatically refine the crossfade frames, mitigating the quality downgrade from multiple extensions.

### 多轮生成 | Multi-Round generation
你可以在多个`VACE Prompt Combine`节点内编写不同的提示词，指定不同的参考图片，只需要将它们连在一起在连接到`SuperUltimate VACE Long Video`节点。轮次数目没有上限，但由于多轮接续生成花费的时间很长，并且存在不可控的随机性，不建议过长的视频生成。  
You can write different prompts within multiple `VACE Prompt Combine` nodes, specify different reference images, and cascade them together and connect to the `SuperUltimate VACE Long Video` node. There is no upper limit to the number of rounds, but due to the long time it takes to generate multiple extensions and the uncontrollable randomness, it is not recommended to generate too long videos.

### 多种控制 ! Multi-Methods control
VACE模型支持许多种控制，包括关键帧、骨骼姿势、深度图、线稿、轨迹动画等等。你可以在一个视频中使用多种不同类型的控制，只需要使用多个`VACE Control Image Combine`节点。但需要注意控制图的帧位不能重复。  
如果需要无缝首尾循环视频，只需要为`loopback_crossfade`设置一个大于0的适当数字即可，不需要进行额外的图片控制。  
VACE models support many kinds of controls, including keyframes, pose, depth, lineart, trajectory animation, and more. You can use multiple different types of controls in a single video, simply by using multiple `VACE Control Image Combine` nodes. However, you need to be careful that the frame positions of the control image are not duplicated.  
If you need a seamless first and last loopback video, just set an appropriate number greater than 0 for `loopback_crossfade`, no additional image controls are needed.  

### 缓解多轮接续造成的质量下降 | Mitigating quality degradation due to multiple rounds of generation
VACE可以使用上一轮视频最后几帧作为新一轮生成视频的前几帧，以此实现视频的接续。但一直以来有个问题制约它的应用，那就是随着接续轮次数目增多，生成视频的质量不断下降，出现过饱和、色差、模糊等等问题。  
本节点通过为新一轮视频的前几个参考帧进行“修复”的途径，有效缓解了多轮次生成造成的质量下降。但是这么做也会造成一个后果，接续过渡部分的帧的颜色或者亮度会出现不自然变化。  
好在副作用并不明显，你也可以自行修改`Custom Refine Option`节点的参数尝试获得更自然的过渡。  
VACE can use the last few frames of the previous round of video as the initial few frames of the new round of generation, thus realizing the extension of video. However, there has been a problem that constrains its application, that is, as the number of extent rounds increases, the quality of the generated video decreases, and problems such as oversaturation, chromatic aberration, blurring, etc. occur.  
This node effectively mitigates the quality degradation caused by multiple rounds of generation by “refine” the inital few reference frames of a new round of video. However, this also has the consequence that the color or brightness of these frames may change unnaturally.  
The side effect is not obvious, but you can also modify the parameters of the `Custom Refine Option` node to try to get a more natural transition.

## 安装 | Install
方法1：在`ComfyUI\custom_nodes`路径下执行命令  
Way 1: run following cmd command at the path `ComfyUI\custom_nodes`

    git clone https://github.com/bbaudio-2025/ComfyUI-SuperUltimateVaceTools

方法2：下载本项目并解压缩到`ComfyUI\custom_nodes`  
Way 2: Clone this repo into `custom_nodes` folder.  
