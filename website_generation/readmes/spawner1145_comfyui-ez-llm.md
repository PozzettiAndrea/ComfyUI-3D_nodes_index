# comfyui-ez-llm

在`models/LLM`文件夹下创建文件夹，例如我这边的` Qwen3-0.6B-Prompt-Gen-v0.1`
<img height="147" alt="image" src="imgs/dec3380e-0dfc-42e2-b203-1f7673595cd3.png" />

并把你从huggingface拿到的所有模型仓库的东西都放进去:
<img width="300" alt="image" src="imgs/04adbe75-0fb8-465f-baa0-02fcfeb1e7e8.png" />

启动以后这么用：
<img height="1074" alt="image" src="imgs/4e7d10e9c985e091e7d89cf2bf6918bd.png" />

这边的model_mode如果是gemma2,llama,qwen这种纯文本模型就选text，如果是qwen 2.5 vl和gemma3这种有视觉能力的就选multimodal

multimodal的可以输入图片，这样搞:
<img height="1051" alt="image" src="imgs/1cd4a646-a29e-420f-8133-368df2551d36.png" />

感觉没了,有话请给我提issue(
