# ComfyUI-MochiEdit

ComfyUI nodes to edit videos using Genmo Mochi

https://github.com/user-attachments/assets/41830ff3-6ac6-4b5a-be35-4429c571aa97

## Installation

These nodes are built to work with the [ComfyUI-MochiWrapper](https://github.com/kijai/ComfyUI-MochiWrapper) nodes and soon will work with native ComfyUI Mochi too.
For now please follow the installation for the wrapper.

Then git clone this repo into your `ComfyUI/custom_nodes/` directory or use the ComfyUI Manager to install (when this repo is added there).

There are no additional requirements.



https://github.com/user-attachments/assets/88a9c4d4-a6d2-4d68-9c07-7fcba32ce84a



## How to Use

There is an example workflow in the `example_workflows` directory.

First, the input video is inverted into noise and then this noise is used to resample the video with the target prompt.
A similar strategy as [RF-Inversion](https://rf-inversion.github.io/) is used.

### Unsampling Nodes

<img width="993" alt="unsampling_nodes" src="https://github.com/user-attachments/assets/abd63fd8-0681-419f-a209-dc7dc769e8cf">

#### Mochi Unsampler

This node creates a sampler that can convert the video into noise.

-   `gamma`: the amount to do noise correction. Leave this to 0 as it does not work well with Mochi.
-   `seed`: if performing noise correction the seed to use for the random noise

#### Mochi Prepare Sigmas

This node makes a small change to the sigmas that the Mochi Sigma Schedule node from the wrapper produces.

#### SamplerCustom (MochiWrapper)

This is the classic KSampler or SamplerCustom from ComfyUI but for the MochiWrapper.

-   `positive` and `negative` should be blank prompts
-   `cfg`: should always be 1.0 for unsampling
-   `add_noise`: should always be False for unsampling
-   `seed`: there is no reason to change the seed
-   `sigmas`: must be prepared then flipped first

### Sampling Nodes

<img width="803" alt="sampling_nodes" src="https://github.com/user-attachments/assets/3f9606ef-0a3b-4000-8154-c02c80b8402a">

#### Mochi Resampler

This node creates a sampler that can convert the noise into a video.

-   `latents`: the latents of the original video
-   `eta`: the strength that the generation should align with the original video
    -   higher values lead the generation closer to the original
-   `start_step`: the starting step to where the original video should guide the generation
    -   a lower value (e.g. 0) will have much closer following but not allow for additional objects like a hat to be placed
    -   a higher value (e.g. 6) will allow for new objects like a hat to be placed, but may not follow the original video. Higher values can also lead to bad results (blurs)
-   `end_step` the step to stop guiding the generation closer to the original video
    -   a lower value will lead to more differences in the video output
-   `eta_trend`: whether the eta (strength of guidance) should stay constant, increase, or decrease as steps progress. `linear_decrease` is the recommended setting for most changes.

#### SamplerCustom (MochiWrapper)

This is the classic KSampler or SamplerCustom from ComfyUI but for the MochiWrapper.

-   `positive` and `negative` can be anything you like. `positive` shoud be the target prompt.
-   `cfg`: can have any cfg that would work with normal Mochi (e.g. 4.50)
-   `latents`: should be the latent from unsampling
-   `sigmas`: must be prepared but NOT flipped
-   `seed`: the seed has no effect

## Acknowledgements

[RF-Inversion](https://rf-inversion.github.io/)

```
@article{rout2024rfinversion,
  title={Semantic Image Inversion and Editing using Rectified Stochastic Differential Equations},
  author={Litu Rout and Yujia Chen and Nataniel Ruiz and Constantine Caramanis and Sanjay Shakkottai and Wen-Sheng Chu},
  journal={arXiv preprint arXiv:2410.10792},
  year={2024}
}
```

https://github.com/user-attachments/assets/d1d8e73a-680d-4671-b5f0-b2efd7ac05f2
