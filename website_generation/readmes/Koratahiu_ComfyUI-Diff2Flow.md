# ComfyUI-Diff2Flow

[![arXiv](https://img.shields.io/badge/arXiv-2506.02221-b31b1b.svg)](https://arxiv.org/abs/2506.02221)

>⚠️ Experimental, to be improved.

This is an unofficial implementation of the **Diff2Flow** method for ComfyUI, based on the paper:

**[Diff2Flow: Training Flow Matching Models via Diffusion Model Alignment (arXiv:2506.02221)](https://arxiv.org/abs/2506.02221)**.

This repository provides a custom KSampler node, `Diff2FlowODESampler`, that applies the Diff2Flow principles to standard diffusion models at inference time.

## What is Diff2Flow?

**Diff2Flow** is a framework designed to bridge the gap between two powerful generative modeling paradigms:

1.  **Diffusion Models (DMs):** Like Stable Diffusion, these are known for their high-quality results  but often require many sampling steps  and can suffer from issues like the "non-zero terminal SNR" problem (difficulty producing pure black or white).
2.  **Flow Matching (FM) Models:** A newer paradigm known for faster inference, improved performance , and simpler, straighter sampling paths.

The challenge is that these two models are not directly compatible. They use different timestep definitions , paths from noise to data (interpolants) , and training objectives.

The key idea of the paper is to **efficiently transfer the knowledge** from a pre-trained diffusion model into a flow matching model. It does this by "warping" the diffusion process into a flow matching one by:

* **Rescaling Timesteps:** Systematically mapping the diffusion model's discrete 0-1000 timesteps to the flow matching 0-1 continuous time.
* **Aligning Interpolants:** Mathematically aligning the path from noise-to-data between the two model types.
* **Deriving Velocity:** Calculating the **velocity field** (which FMs use) directly from the diffusion model's standard prediction (e.g., `epsilon` or `v-prediction`).

This allows a model to be sampled using a flow-matching objective, which can lead to faster, more efficient inference.

## How This Node Works

This implementation provides a single node, `Diff2Flow ODE KSampler`.

This node **patches your diffusion model** (e.g., SD1.5, SD2.1, SDXL) at runtime, enabling diff2flow.

When you sample, the `enable_diff2flow` function:
1.  **Patches** your loaded model by adding the `Diff2Flow` mathematical conversions based on the model's original `beta_schedule`.
2.  The `Diff2FlowODESampler` then intercepts the sampling call. At each step, it:
    * Rescales the FM timestep to the equivalent DM timestep.
    * Aligns the FM latent to the equivalent DM latent.
    * Feeds these aligned inputs into the original UNet.
    * Takes the UNet's output (`epsilon` or `v-prediction`) and converts it into a **velocity field** of Flow-Matching.
3.  This derived velocity is then used by a true **Ordinary Differential Equation (ODE) solver** from the `torchdiffeq` library to perform the sampling step.

## 🚀 Key Features

* **Works with Standard Checkpoints or Finetuned Diff2Flow Models:** Use your existing `v-prediction` (like SD 2.1)  and `epsilon-prediction` (like SDXL) models. Or the models you finetuned using Diff2FLow.
* **True ODE Solvers:** Integrates with `torchdiffeq` to provide a wide range of solvers, including adaptive-step-size solvers (`dopri5`, `bosh3`, etc.) and fixed-step-size solvers (`euler`, `rk4`, `midpoint`, etc.).
* **Single Node:** A simple, drop-in KSampler alternative.

## 💾 Installation

1.  **Clone the Repository:**
    Navigate to your `ComfyUI/custom_nodes/` directory and clone this repo:
    ```bash
    git clone https://github.com/Koratahiu/ComfyUI-Diff2Flow
    ```

2.  **Install Dependencies:**
    This node has a **critical dependency** on `torchdiffeq`.

    Activate your ComfyUI virtual environment (if you have one) and run:
    ```bash
    pip install torchdiffeq
    ```

3.  **Restart ComfyUI:**
    Completely shut down and restart ComfyUI.

## 💡 Usage

1.  After installation, find the **`Diff2Flow ODE KSampler`** node in the `sampling/custom_sampling` menu.
2.  Connect your `MODEL`, `positive`, `negative`, and `latent_image` just like a standard KSampler.
3.  **Select an ODE `solver`**.
    * `euler` is the simplest and fastest, equivalent to the standard Euler sampler.
    * Adaptive solvers like `dopri5` or `bosh3` may offer different quality/speed trade-offs. You can tune them with the `log_relative_tolerance` and `log_absolute_tolerance` parameters.
4.  Adjust `steps`, `cfg`, and `seed`.
5.  Generate!

---

> ### ⚠️ Important Note: Inference vs. Finetuning
>
> The original paper achieves its most impressive results (e.g., high-quality 2-step generation ) by **finetuning** a model *using* the Diff2Flow objective.
>
> This node applies the Diff2Flow math for **inference only**. Your results will vary! As you need to finetune the model on diff2flow for replicating the results of a fully finetuned diff2flow model in the paper.
>
> That said, the paper also shows that simply converting a diffusion model to its flow-matching counterpart for the *same* task can lead to performance improvements.
>
> You can finetune the model in diff2flow, either using [the offical code](https://github.com/CompVis/diff2flow) or using this PR of OneTrainer (which is up to now is yet to be merged but it's pretty much stable and tested):
https://github.com/Nerogar/OneTrainer/pull/1052

## Known Issues

- ODE samplers don't support masks well.

## Acknowledgements

* Main code adopted from:
  https://github.com/CompVis/diff2flow
* All credit for the methodology goes to the paper's authors: Johannes Schusterbauer, Ming Gui, Frank Fundel, and Björn Ommer!
* Also part of the credit for ODE solvers goes to this node that inspired us: https://github.com/redhottensors/ComfyUI-ODE
