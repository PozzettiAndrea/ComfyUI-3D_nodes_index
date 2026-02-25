# 🎨 ComfyUI-productfix

![git_header](assets/middlek_git_header.png)
ComfyUI custom node that helps generate images while preserving the text, logos, and details of e-commerce products.

## 🎬 Demo

![project_header](assets/project_header.png)

AI-generated images of items in my room taken with a smartphone (no color correction).

## 📌 Index

- [Introduction](#-introduction)
- [Features](#-features)
- [Models and Custom Nodes](#-models-and-custom-nodes)
- [Application](#-application)
- [Approach](#-approach)
- [Install](#-install)
- [How to use](#-how-to-use)

## 🚀 Introduction

Images generated with Stable Diffusion are visually natural and high-fidelity, but there is an issue where the input object is deformed during generation. This problem is especially noticeable with elements that have artificial regularity, such as text and brand logos. Such **deformation issues are a serious limitation when applied to real products sold in e-commerce environments**.

**Productfix** provides an AI application called **Latent Injection**, which generates images while preserving the characteristics of the input object (text, logo, details, etc.). It also offers additional nodes that help retain fine details of objects.

With these nodes, it is expected that much of the post-processing work that previously had to be done with design tools (like Photoshop or Illustrator) can be greatly reduced. You can integrate these custom nodes into your workflow in ComfyUI.

## 💡 Features

<details>
  <summary><strong>Apply Latent Injection</strong></summary>
  <ul>
    <li>Hijacks the KSampler node in ComfyUI to perform Latent Injection.</li>
    <li>Restores the original KSampler node after execution.</li>
  </ul>
</details>

<details>
  <summary><strong>Get Text Mask</strong></summary>
  <ul>
    <li>Node that loads a text mask as a tensor using the Easy OCR package.</li>
    <li>Although an Easy OCR custom node already exists (<a href="https://github.com/JaidedAI/EasyOCR">https://github.com/JaidedAI/EasyOCR</a>), this node is recommended because PIL usage is not stable.</li>
  </ul>
</details>

<details>
  <summary><strong>Reset Model Patcher Calculate Weight</strong></summary>
  <ul>
    <li>Many custom nodes (e.g., ComfyUI-Easy-Use <a href="https://github.com/Acly/ComfyUI-Easy-Use">https://github.com/yolain/ComfyUI-Easy-Use.git</a>) cause errors if another node has injected the calculate weight function of Modelpatcher.</li>
    <li>This node resets it to the original Modelpatcher calculate weight to resolve such issues.</li>
  </ul>
</details>

## 📝 Models and Custom Nodes

### Models
- [realisticVisionV60B1_v51HyperVAE](https://huggingface.co/JCTN/Juggernaut/blob/main/realisticVisionV60B1_v51HyperVAE.safetensors)
- [ic light](https://huggingface.co/lllyasviel/ic-light/blob/main/iclight_sd15_fc.safetensors)
- [depth controlnet v1.1](https://huggingface.co/lllyasviel/ControlNet-v1-1/blob/main/control_v11f1p_sd15_depth.pth)
- [more detail lora](https://civitai.com/models/82098/add-more-details-detail-enhancer-tweaker-lora)

### Custom nodes
- [ComfyUI-productfix](https://github.com/MiddleKD/ComfyUI-productfix)
- [comfyui_controlnet_aux v1.0.7](https://github.com/Fannovel16/comfyui_controlnet_aux)
- [ComfyUI Impact Pack v8.14.2](https://github.com/ltdrdata/ComfyUI-Impact-Pack)
- [ComfyUI-Easy-Use v1.3.0](https://github.com/yolain/ComfyUI-Easy-Use)
- [ComfyUI_essentials v1.1.0](https://github.com/cubiq/ComfyUI_essentials)
- [ComfyUI-IC-Light-Native v1.0.1](https://github.com/huchenlei/ComfyUI-IC-Light-Native) **(not [ComfyUI-IC-Light](https://github.com/lllyasviel/IC-Light))**

## 🏃🏻‍♂️ Application
- ### **Comparing “IC-Light + Text” / “IC-Light + Text + Latent Injection”**
    
    condition / Input / IC-Light / **latent injection($\sigma_{end}$=1.0)** / **latent injection($\sigma_{end}$=0.5)**
    ![ic_light_text](assets/iclight_injection.png)
    prompt: product photo, professional photography, realistic, leaf, outdoors / seed: 42

- ### **Comparing “IC-Light + IP-Adapter” / “IC-Light + IP-Adapter + Latent Injection”**
    
    condition / Input / IC-Light / **latent injection($\sigma_{end}$=1.0)** / **latent injection($\sigma_{end}$=0.5)**
    ![ic_light_adapter](assets/iclight_injection_adapter.png)
    prompt: product photo, professional photography, realistic / seed: 42
    <br/><br/>
    Latent injection truly shines when used together with IC-Light and IP-Adapter. Try it when compositing template-style images and products!
- ### **IC-Light + controlnet + text condition + Text transfer + Latent Injection**

    ![latent_injection_text](assets/more_results_0.png)
    Items in my room captured with my phone camera
    ![latent_injection_text](assets/more_results_1.png)
    prompt: product photo, professional photography, realistic, water, bubble / seed: 42 / controlnet: depth
    ![latent_injection_text](assets/more_results_2.png)
    prompt: product photo, professional photography, realistic, flowers, outdoors / seed: 42 / controlnet: depth
- ### **IC-Light + controlnet + IP-Adapter + Text transfer + Latent Injection**

    ![latent_injection_adapter](assets/more_results_0.png)
    Items in my room captured with my phone camera

    ![latent_injection_adapter](assets/more_results_3.png)

    prompt: product photo, professional photography, realistic / seed: 42 / controlnet: depth

    ![latent_injection_adapter](assets/more_results_4.png)
    prompt: product photo, professional photography, realistic / seed: 42 / controlnet: depth
- ### **Text transfer**

    ![producfix_src](assets/productfix_src.png)
    Input / text condition / image condition(IP-Adapter)

    ![productfix_text](assets/productfix_text.png)
    only IC-Light / **Latent injection** / detail transfer / **Text transfer**
  
    ![producfix_text_closeup](assets/productfix_text_closeup.png)
    close up
    <br/><br/>
    ![productfix_adapter](assets/productfix_adapter.png)
    only IC-Light / **Latent injection** / detail transfer / **Text transfer**
  
    ![producfix_adapter_closeup](assets/productfix_adapter_closeup.png)
    close up
    <br/><br/>
    Text transfer is a detail transfer application based on OCR text masks, developed to preserve the text of input objects. You can implement it using the `GetTextMask` node and the `DetailTransfer` node.

- ### **Upscaled results + Text detail transfer**
    ![upsvaled_results](assets/upscaled_results.png)


## 🛠 Approach

- ### Background: Inpainting
  Inpainting in diffusion models generates images conditioned on a mask. At each sampling step, the latent space of the original and the generated image is composited based on the mask. This method allows for generation while preserving the input object, but **for low-quality input objects (e.g., taken with a smartphone), the output image quality is also limited**.

- ### Background: IC-Light
  IC-Light is an innovative Adapter UNet that manipulates foreground and background lighting. By relighting the input object, even low-quality objects can be transformed into high-quality output images. However, **there are still issues with deformation of object details during foreground generation**.

- ### Background: Kandinsky Inpainting Process
  Kandinsky diffusion inpainting differs from typical inpainting. When compositing latent spaces at each sampling step, **it uses a latent space with noise added according to the scheduler's sigma value instead of the original**. This approach improves quality through consistent noise.

- ### Background: CLIP Skip
  CLIP Skip is an inference method where text conditioning is not applied until the last sampling step but is stopped midway. This allows for more contextually appropriate results by controlling the conditioning process.

- ### Solution: Latent injection
    
    ![latent_injection_flow](assets/latent_injection_flow.jpg)
    
    ![math](assets/math.svg)
    
    $X_t$ : sample
    
    $M$ : product mask
    
    $P$ : product latent
    
    $CO$ : composition operation(ex: add, overlay, soft light etc.)
    
    To achieve both preservation of object features and meaningful lighting changes, a composite strategy is applied. **During the sampling process, latent spaces with added noise are composited to preserve fine object details.** Additionally, to reflect the global lighting changes of IC-Light, the initial and final steps of sampling are selectively skipped. This method operates based on the scheduler's sigma value, ensuring stable performance across various scheduler types. As a result, it is possible to flexibly apply lighting effects while preserving the unique characteristics of the object.
    

## 📥 Install

```bash
cd custom_nodes
git clone {this repository}
pip install -r requirements.txt
```

## 🖥 How to use

### **ComfyUI-workflows**

- **IC-Light + controlnet + text condition + Text transfer + Latent Injection**
    ![latent_injection_flow](assets/productfix_text_comfyui.png)
    
    You can download the workflow [here](workflows/productfix_text.json).

- **IC-Light + controlnet + IP-Adapter + Text transfer + Latent Injection**
    ![latent_injection_flow](assets/productfix_adapter_comfyui.png)

    You can download the workflow [here](workflows/productfix_adapter.json).

### **Demo Example Assets**
- [Product example image](assets/demo_example/pr_example.png)
- [Style example image](assets/demo_example/style_example.jpg)

## 📚 Reference

This project is based on research and code from several papers and open-source repositories.

- IC-Light: https://github.com/lllyasviel/IC-Light
- kandinsky2.2: https://github.com/ai-forever/Kandinsky-2
- clip-skip: https://medium.com/@natsunoyuki/clip-skip-with-the-diffusers-library-b2b63f38a443
- Anton Razzhigaev, Arseniy Shakhmatov, Kandinsky: an Improved Text-to-Image Synthesis with Image Prior and Latent Diffusion, **arXiv**, 2023
- Chuanxia Zheng, Long Tung Vuong, Jianfei Cai, Dinh Phung, MoVQ: Modulating Quantized Vectors for High-Fidelity Image Generation, **arXiv**, 2022
