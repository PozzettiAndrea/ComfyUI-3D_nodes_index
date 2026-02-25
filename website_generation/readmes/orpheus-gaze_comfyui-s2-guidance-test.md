# S²-Guidance for ComfyUI
This repository provides an attempted implementation of [S² guidance arxv:2508.12880](https://arxiv.org/abs/2508.12880) for DIT diffusion models in ComfyUI. I thought it looked interesting when the paper came out and decided to implement it as a personal exercise.

Currently only tested with Chroma and it at least does seem to affect the resulting image, although I do not know for sure if the implementation is correct. It is currently hardcoded to only work with the architecture of Flux models, which includes Chroma, I might change this later.

## Usage
You will find the node named as "✨ S2Guidance_DIT" under the "✨ S2GUIDANCE" category. Place the node in your model chain. The paper found a S²-scale of `0.25` a good number for their tests with SD3.5, but in Chroma this causes a grainy and blownout result, a S²-scale of `0.05` seems more appropriate here. Keeping the CFG scale at `3.5` seems to work though. Effects can be subtle but seem to improve sharpness and brightness.

## Installation
Install this extension by cloning this repository in your `custom_nodes` folder with `git clone https://github.com/orpheus-gaze/comfyui-s2-guidance-test`.
