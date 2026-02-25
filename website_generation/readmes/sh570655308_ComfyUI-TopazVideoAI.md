## Language

- [English](#english)
- [中文](#中文)

### English
**Requirements:**

Licensed installation of TopazVideoAI

**Installation:**

method 1: search 'TopazVideoAI' in manager and install it.

method 2: git clone this project to custom_nodes folder
```
git clone https://github.com/sh570655308/ComfyUI-TopazVideoAI.git
```

First, set up environment variables
Open Topaz Video AI UI, log in to your account, press Ctrl+Shift+T to open the command window, and it will automatically set the model directory in environment variables. 
If the automatic setup of the model directory fails, it is necessary to manually configure it by adding TVAI_MODEL_DATA_DIR and TVAI_MODEL_DIR to the user's environment settings, with their values set to the corresponding directories of the models.
![image](https://github.com/user-attachments/assets/996eba42-a356-4324-a697-706536cb4da4)
~~Then add Topaz's installation directory to the PATH. This step is for setting up FFmpeg. If you have previously set other paths, please remove them~~
The path to ffmpeg is specified within the node, with the default value being "C:\Program Files\Topaz Labs LLC\Topaz Video AI", which is the installation directory. This specific ffmpeg is mandatorily designated only for the processes of upscaling and frame interpolation. Users have the flexibility to customize ffmpeg in their environment variables for handling other tasks.

Close the GUI, open shell terminal

```cd "C:\Program Files\Topaz Labs LLC\Topaz Video AI"```

```.\login```

The path may vary when you have custom installation path
Then close the shell terminal, now you can use this node normally

**Usage:**

Simply connect this nodes between video output and video save.
Workflows contained in examples folder.

**Notification:**

The models have scaling limitations; for example, thm-2 is fixed at a 1x scale. As not all models have undergone comprehensive testing and standardization for various scaling factors, it is advisable to use either 2x or 4x. If you encounter errors when attempting a 4x scale, please default to using a 2x scale.
~~Model selection is not ready yet, now only works with default~~
This node is designed for short AI generated videos. I didn't test it with long video, because comfyui transfer video as image batch, the node will encode and decode which cost longer time than TopazVideoAI GUI. 

Common errors:
No such filter: 'tvai_up'
Make sure the ffmpeg path is correct ~~and unique - you must use the ffmpeg that comes with TopazVideoAI. Remember to remove ffmpeg from other paths and from the ComfyUI environment.~~

### 中文
**要求：**

已安装的 TopazVideoAI，要登录账户

**安装：**

方法1.通过comfyui manager搜索topazvideoai后安装

方法2.将此项目git clone到 custom_nodes 文件夹

```
git clone https://github.com/sh570655308/ComfyUI-TopazVideoAI.git
```

首先要设置环境变量

打开topaz video ai的应用程序，登录账号，快捷键ctrl+shift+T打开命令窗口，会自动设置模型目录到环境变量。

如果自动设置模型目录失败，则需要手动设置，在用户环境配置中添加TVAI_MODEL_DATA_DIR 和TVAI_MODEL_DIR，数值为模型对应的目录

![image](https://github.com/user-attachments/assets/996eba42-a356-4324-a697-706536cb4da4)

~~然后在path中添加topaz的安装目录，这一步是设置ffmpeg，如果之前有设置过其他路径的ffmpeg请删除~~

ffmpeg路径在节点中指定，默认值是C:\Program Files\Topaz Labs LLC\Topaz Video AI，即安装目录。此ffmpeg只在放大和补帧过程强制指定，可以自行在环境变量中自定义ffmpeg负责其他环节。

设置完成后关闭gui，打开shell终端输入：

```cd "C:\Program Files\Topaz Labs LLC\Topaz Video AI"```

```.\login```

之后就可以正常使用了，

**使用：**

接在视频输入前即可。

examples文件夹中包含工作流。

**注意事项：**

模型有倍数限制，例如thm-2只能1倍，由于未对全部模型的倍数进行测试和规范化，所以放大倍数请使用2或者4，当4报错时请使用2。
~~模型选择功能尚未就绪，目前仅支持默认设置~~
此节点专为AI生成的短视频设计。由于ComfyUI以图像批次方式传输视频，节点需要进行编码和解码，因此相比TopazVideoAI图形界面处理时间更长，故未对长视频进行测试。

常见错误：
No such filter: 'tvai_up’
确保ffmpeg的path路径正确 ~~，必须用TopazVideoAI自带的ffmpeg。记得删除其他路径的ffmpeg以及comfyui环境中的ffmpeg。~~
