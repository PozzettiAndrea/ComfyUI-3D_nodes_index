<h1 align='center'>HelloMeme: Integrating Spatial Knitting Attentions to Embed High-Level and Fidelity-Rich Conditions in Diffusion Models</h1>

<div align='center'>
    <a href='https://github.com/songkey' target='_blank'>Shengkai Zhang</a>, <a href='https://github.com/RhythmJnh' target='_blank'>Nianhong Jiao</a>, <a href='https://github.com/Shelton0215' target='_blank'>Tian Li</a>, <a href='https://github.com/chaojie12131243' target='_blank'>Chaojie Yang</a>, <a href='https://github.com/xchgit' target='_blank'>Chenhui Xue</a><sup>*</sup>, <a href='https://github.com/boya34' target='_blank'>Boya Niu</a><sup>*</sup>, <a href='https://github.com/HelloVision/HelloMeme' target='_blank'>Jun Gao</a> 
</div>

<div align='center'>
    HelloVision | HelloGroup Inc.
</div>

<div align='center'>
    <small><sup>*</sup> Intern</small>
</div>

<br>
<div align='center'>
    <a href='https://songkey.github.io/hellomeme/'><img src='https://img.shields.io/badge/Project-HomePage-Green'></a>
    <a href='https://arxiv.org/pdf/2410.22901'><img src='https://img.shields.io/badge/Paper-Arxiv-red'></a>
    <a href='https://huggingface.co/songkey'><img src='https://img.shields.io/badge/%F0%9F%A4%97%20HuggingFace-Model-yellow'></a>
    <a href='https://github.com/HelloVision/HelloMeme'><img src='https://img.shields.io/badge/GitHub-Code-blue'></a>
    <a href='https://www.modelscope.cn/studios/songkey/HelloMeme'><img src='https://img.shields.io/badge/modelscpe-Demo-red'></a>
</div>


## 🔆 New Features/Updates
- ✅ `02/09/2025` **HelloMemeV3** is now available.
[YouTube Demo](https://www.youtube.com/watch?v=DAUA0EYjsZA)

- ✅ `12/17/2024` Support modelscope ([Modelscope Demo](https://www.modelscope.cn/studios/songkey/HelloMeme)).
- ✅ `12/08/2024` Added **HelloMemeV2** (select "v2" in the version option of the LoadHelloMemeImage/Video Node). Its features include:
a. Improved expression consistency between the generated video and the driving video.
b. Better compatibility with third-party checkpoints.
c. Reduced VRAM usage.
[YouTube Demo](https://www.youtube.com/watch?v=-2s_pLAKoRg)

- ✅ `11/29/2024` a.Optimize the algorithm; b.Add VAE selection functionality; c.Introduce a super-resolution feature.
[YouTube Demo](https://www.youtube.com/watch?v=fM5nyn6q02Y)

- ✅ `11/14/2024` Added the `HMControlNet2` module, which uses the `PD-FGC` motion module to extract facial expression information (`drive_exp2`); restructured the ComfyUI interface; and optimized VRAM usage.
[YouTube Demo](https://www.youtube.com/watch?v=ZvoMHyRm310)

- ✅ `11/12/2024` Added a newly fine-tuned version of [`Animatediff`](https://huggingface.co/songkey/hm_animatediff_frame12) with a patch size of 12, which uses less VRAM (Tested on 2080Ti).
- ✅ `11/11/2024` ~~Optimized VRAM usage and added `HMVideoSimplePipeline` (`workflows/hellomeme_video_simple_workflow.json`), which doesn’t use Animatediff and can run on machines with less than 12G VRAM.~~
- ✅ `11/6/2024` The face proportion in the reference image significantly affects the generation quality. We have encapsulated the **recommended image cropping method** used during training into a `CropReferenceImage` Node. Refer to the workflows in the `ComfyUI_HelloMeme/workflows directory`: `hellomeme_video_cropref_workflow.json` and `hellomeme_image_cropref_workflow.json`.


## Introduction

This repository is the official implementation of the [`HelloMeme`](https://arxiv.org/pdf/2410.22901) ComfyUI interface, featuring both image and video generation functionalities. Example workflow files can be found in the `ComfyUI_HelloMeme/workflows` directory. Test images and videos are saved in the `ComfyUI_HelloMeme/examples` directory. Below are screenshots of the interfaces for image and video generation.

> [!Note]
> [Custom models should be placed in the directories listed below.](https://github.com/HelloVision/ComfyUI_HelloMeme/issues/5#issuecomment-2461247829)
> 
> **Checkpoints** under: `ComfyUI/models/checkpoints`
> 
> **Loras** under: `ComfyUI/models/loras`

### Installation

Keyword of ComfyUI Manager : `hellomeme-api`
<p align="center">
  <img src="examples/ComfyUI_Manager.jpg" alt="hellomeme-api">
</p>


### Workflows

| workflow file | Video Generation | Image Generation | HMControlNet | HMControlNet2 |
|---------------|------------------|------------------|-----------|---------------|
| image_generation.json |                  | ✅                |  | ✅ |
| image_style_transfer.json |                  | ✅                |  | ✅ |
| video_generation.json | ✅                |                  |  | ✅ |

### Image Generation Interface

<p align="center">
  <img src="example_workflows/hellomeme_image_workflow.jpg" alt="image_generation_interface">
</p>

### Style Transfer Interface

<p align="center">
  <img src="example_workflows/hellomeme_style_workflow.jpg" alt="image_generation_interface">
</p>

### Video Generation Interface

<p align="center">
  <img src="example_workflows/hellomeme_video_workflow.jpg" alt="video_generation_interface">
</p>

