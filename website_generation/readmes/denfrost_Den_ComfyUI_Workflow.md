Den_ComfyUI_Workflows
==============
Custom nodes make easy Advanced Workflows. 
Focus on Image\Video and ControlNet efficiency and performances.
Manipulation of Latent Space, Automatic pipeline with a bit efforts.
--------------
New Nodes in pack Den Workflow ComfyUI
#### ImageToLatent node: `Den_ImageToLatentSpace`
#### GPT Sampler: `Den_GPTSampler_llama`
#### GPT load: `Den_GPTLoaderSimple_llama`
#### SD Video: `Den_SVD_img2vid`
#### FaceRestore Model codeformer: `Den_FaceRestoreCFWithModel`
--------------
#### Using GPT & LLM models : Llava,GGUF
https://huggingface.co/models?library=gguf&sort=trending&search=llava

#### can put models to path comfyui
**ComfyUI\models\GPTcheckpoints\llava**

Have 2 folders for Clip and Model gguf or must create this folders and put new models

**ComfyUI\models\GPTcheckpoints\llava\clips**

**ComfyUI\models\GPTcheckpoints\llava\models**

#### GPT load: `Den_GPTLoaderSimple_llama`
- Load Model and Clip for LLM

![](18d83b489b44ea98d3ac277a53036568.png)

#### GPT Sampler: `Den_GPTSampler_llama`
- Sampler Llama with using Cache for Acceleration

![](ba951e180cc4c9304541abe2843c28ce.png)

- Example Workflow GPT-SD

![](6da778c85399f187e2829a3e460b2938.jpg)

#### SD Video: `Den_SVD_img2vid`

- SVD from size Image for init Latent Space SVD Model

![](dfdbcbea00bdfcbdcf7d0d73b3cb83f7.png)

#### ImageToLatent node: `Den_ImageToLatentSpace`

![](17b6e18ef0deec9f82138b66ca7aace6.png)

- Latent space from size Image

![](d88f68c317f3f790055be5978e2689dc.png)

- FaceRestore With Model Gan or CodeFormer

![](b64810ce1266a038ccd532aa9389c996.png)
--------------
![ComfyUI Screenshot](e92381a5d7c26f138d1451c8b4f52142.jpg)

--------------
How Install. Manager->Install via Git URL -> Enter Git Address 
![ComfyUI Screenshot](88ab9b2c48fb20688935a1bf8ea4b44e.png)