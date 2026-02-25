可以直接在comfyui中使用腾讯的混元3D。输出的glb和obj需要通过https://github.com/MrForExample/ComfyUI-3D-Pack的view mesh看到

但是由于ComfyUI-3D-Pack太难装了，所以你们也可以直接到输出目录看结果。输出目录是在你的comfyui的output下面的3D_output下面看到

每次模型都会生成一个编号，里面包含了所有生成的内容。glb和obj模型可以直接用windows的3D viewer查看，没有的可以商店装一个https://apps.microsoft.com/detail/9nblggh42ths?hl=en-US&gl=US


使用comfyui安装的话会自动安装依赖，如果你使用git clone下载到了comfyui的custom_nodes目录下的话，请在我的插件目录下使用安装依赖，一般情况都会装好
```shell
../../../python_embeded/python.exe install.py
```
如果安装失败了，一定是万恶的编写版本的python的错，去这里
https://github.com/MrForExample/Comfy3D_Pre_Builds/tree/main/_Python_Source_cpp
下载对应版本的文件，全部放入python_embeded的目录下


在我的插件目录下新建 weights目录，把所有的模型文件扔进去
https://huggingface.co/spaces/tencent/Hunyuan3D-1/tree/main

如果你安装了huggingface-cli,可以在我的插件根目录下使用这个命令一次下载：
```shell
mkdir weights
huggingface-cli download tencent/Hunyuan3D-1 --local-dir ./weights
```
当然是不想用comfyui我也有整合包提供，不用搞环境
链接: https://pan.baidu.com/s/1woQf2eUpI6wXbX_6BDeiMw?pwd=3tef 提取码: 3tef 


目前因为我不会写代码，所有前端没写，obj必须用3D-pack才能在comfyui中看到，gif不会动，我也不会写前端，能写的可以教我，感激不尽！
顺便我阉割混元1.1文生图，帮助大家自由选择模型生成
顺便，我做了个预处理，处理图片到1024*1024，记得第一次用我的预处理插件，选一下颜色，不然会报错，我也不知道为什么，知道的可以教我
以上
![image](https://github.com/user-attachments/assets/eb032ef1-394e-40a9-9b41-2e03c8186dc6)![output](https://github.com/user-attachments/assets/de5c048e-eca6-4d66-a3af-9fccf4a59a7f)

