![ComfyUI_00026_](https://github.com/user-attachments/assets/57fdbf91-51d5-43ad-9ec7-3873003dca1b)

<div align="center"><h1>ComfyUI MUSUBI-TUNNER WAN LORA TRAINER</h1></div>








**Tested environment** (This is made for ComfyUI windows portable, not tested in other envirionments, you are free to fork the project to make it compatible in different instalations) :
* ComfyUI Portable 0.3.44 (last versions)
* Python 3.12
* Visual Studio tools (seems to be needed for path compatibility).
* Pytorch 2.7.1 cuda 128
* "Include python scripts" Zip-package for 3.12 (In case you don't have it see the tutorial installtion below).
* Custom bat file (see installation below).
*  **Don't use Sageattention**.

**2025: August 1**
* Added Include_package.zip (Extract this python into the "Include" folder of your environment (python_embeded/Include/<--).
  
**2025: June 25** 
Update version 1.1.0:
![image](https://github.com/user-attachments/assets/c6356bfb-f19d-4991-a748-96db4d0a1701)

* Added Sampler node to generate images every n steps or epochs (Images are in the folder "sample" in your output Lora path).
* BlockSwap node fix triggering it to the launcher.
* Network weights fix triggering the assigned path (now you are able to train from a previous lora assigning her's path location).
* Network args trigger fix.
* Optimizer args trigger fix.
* Tom argument image extension setted up to ".txt" as default.
* Enable bucket no upscale setting trigger fix. (no works correctly to prevent upscale).
* Max train step setted up to 2048 as default (taking in account this set is multiplied by epochs and images).
* Setted up timestep_sampling to "shift" as default.
* Setted up epoch to 128 as default.
* Added 2 example workflows for 14B and 1.3B models, (located in the folder "workflows", you can also download form the website).
* Code improvements.
* Code mods for full compatibility with the last version of ComfyUi.
* Added 6 nodes for training.
* Added Example Workflow in the custom node folder.
* Made for ComfyUi windows portable package.
* Automated process for the creation of the TOM file, cache latents, cache texts & trainning run (Nodes triggered by this order to do the complete process in one shot).
* You can skip latents and text caches if you need to restart the training (taking into account data has not changed vae, clipvision, text models).
* For more info about setting up correctly parameters you can check the Wan Doc on https://github.com/kohya-ss/musubi-tuner/blob/main/docs/wan.md



**About max_train_epochs**: The max train epochs is an equations that takes into account several arguments as gradients, number of images etc. This must be set up between 16/128 depending of the number of images you want to train. To ensure a little package of 30 images, set up it as maximum (128) to train more than 5000 steps. Take into account network dropout to not overfitting, also dim and alpha. All is relative but for sure you will find you custom setting depending of your purpose. For the moment max train epochs have a limit to 128, but if is needed to add a bigger max value i can update it.


Performances test with 312 images with default settings (spda) :
![image](https://github.com/user-attachments/assets/15222364-f1db-42fa-abf3-0ccc08a953b5)


**Instructions**:
1. Clone this repository into your custom node folder.
2. install requirements.txt from custom_nodes\ComfyUI_Wan2_1_lora_trainer :
```  
 ..\..\..\python_embeded\python -m pip install -r requirements.txt
````
3. You must to create your custom bat adding  and run ComfyUi from it to avoid issues with paths. You can name it "Run_Wan_LoRa_trainer.bat" (this gives you the ability to connect Musubi with the workflow) Example:
```
@echo off
REM Load Visual Studio Build Tools for the Wan subprocess environment
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" amd64
REM Start ComfyUI
.\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build
pause
```
4. Extract the Include_package.zip, place the folder "Include" of your python environment (python_embeded/Include) and "libs" into (python_embeded/).
5. Run ComfyUI from your custom bat. Enjoy.
6. Remember to have the folder "libs" in your python embeded folder with this two dev files :
7. <img width="660" height="90" alt="image" src="https://github.com/user-attachments/assets/cdc801d9-b683-408c-af18-d144bfbe622f" />


**NOTE** : The reason of adding this windows call is because the Trainer runs in a new sub process inheriting the ComfyUI environment, but is needed to setup ComfyUI as root path to work with.

**CLIP VISION** : Clip vision is just setted up for I2V models, for training T2V Models, set clip to None. 

* Path into an empty folder for the cache (use different folders for each lora to not mix you cache data (cleaner and probably faster).
Then conect the compiler and memory nodes and choose the attention [SPDA, XFORMERS] (Sage seems to burn the Lora, avoid it for the moment):
![image](https://github.com/user-attachments/assets/63f8862e-544d-4718-89f1-1c34067e5ee1)

If you have high VRAM you can bybass Torch compile, memory settings. Also if you don't need to see the progress you can bypass sampling settings:
![image](https://github.com/user-attachments/assets/b4624251-88f4-4f1b-95ab-116ac2042a0d)


* Image data input are not exclusive to videos! you can train just with images as the following example (path to your images and text captions):
![Captura de pantalla 2025-05-23 161441](https://github.com/user-attachments/assets/465448fe-f347-431f-b3e7-e13436d5c039)


* Performances test with 312 images with 1.3B T2v, default settings (spda) :
![image](https://github.com/user-attachments/assets/15222364-f1db-42fa-abf3-0ccc08a953b5)

And the results :

https://github.com/user-attachments/assets/41b439ee-6e90-49ac-83dd-d1ba21fd1d63

For any concern no doubt to contact me.
