# Dragos-SceneBuilder
ComfyUI node for structured scene building

With these nodes you can easaly build a scene by selecting what you want from a list using the "Dragos Structured Builder".
The list have these pre build for you
camera
character (female and male)
enviroment
style

If you want to add your own you can do that by building a .json file and put it in the Dragos-SceneBuilder\web\schema folder
You can also modify the existing files.

<img width="938" height="788" alt="Compact Scenebuilder Node" src="https://github.com/user-attachments/assets/e92256f5-949f-4e79-a65d-3e62712d2c7b" />


If you want to build the json from the ground up you can do that with the Custom scene nodes "Dragos Variable" and "Dragos Object"

<img width="914" height="528" alt="Custom Scene builder Node" src="https://github.com/user-attachments/assets/1404b4f2-0c2a-4a41-894a-681e60911b0c" />

to make the json string and see it beeing built use the "Dragos Scene Compiler" node as this will compile and convert it to a string you can use with outher nodes.

<img width="496" height="652" alt="Compiler Node" src="https://github.com/user-attachments/assets/cbba933d-5b7c-4fea-b6d8-809854a508cc" />

To get a proper Image prompt you can use to generate a image you need a way to convert the json string to a proper Image prompt for your type of model.
To do that the easiest way is to use a LLM with a prompt to convert the json string.

I have a node that lets you select a prompt to use with the LLM to convert it to the right format.
<img width="477" height="392" alt="Promp Loader" src="https://github.com/user-attachments/assets/d7103b96-b29e-4d68-ae76-717e65cec329" />

You can connect this node to a node that talks to your LLM backend. I Reccomend [Comfyui-Z-Image-Utilities](https://github.com/Koko-boya/Comfyui-Z-Image-Utilities) as the prompts are build for it.

The LLM model i use to convert the json to an Image prompt is [Llama-Joycaption-Beta-One-Hf-Llava-Q4_K](https://huggingface.co/concedo/llama-joycaption-beta-one-hf-llava-mmproj-gguf/blob/main/Llama-Joycaption-Beta-One-Hf-Llava-Q4_K.gguf). Small enugh to fit on the CPU freeing up the GPU for your Image Models. Or if you use smaller Image models and have a GPU with more Vram you can fith both on the GPU for more speed.
