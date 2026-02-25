## Introduction

This repository is a fork of wildminder/ComfyUI-DyPE. 

It includes partially hand-written, partially AI-genererated changes that make the DyPE node compatible with Nunchaku FLUX models.
The node still supports the standard models as before.
I'm not a professional programmer and I have no plans on maintaining this repository.

In my tests I got a 100% speed boost when generating a 2048x2048 sized image on a RTX 2070.

All other functionality, documentation, and usage instructions are preserved from the original project — see the sections below for installation, usage, and known limitations.


## About The Project

DyPE is a novel, training-free method that allows pre-trained diffusion transformers like FLUX to generate images at resolutions far beyond their training data, with no additional sampling cost.

It works by taking advantage of the spectral progression inherent to the diffusion process. By dynamically adjusting the model's positional encodings at each step, DyPE matches their frequency spectrum with the current stage of the generative process—focusing on low-frequency structures early on and resolving high-frequency details in later steps. This prevents the repeating artifacts and structural degradation typically seen when pushing models beyond their native resolution.

<div align="center">

  <img alt="ComfyUI-DyPE example workflow" width="70%" src="https://github.com/user-attachments/assets/e5c1d202-b2c4-474b-b52f-9691ab44c47a" />
      <p><sub><i>A simple, single-node integration to patch your FLUX model for high-resolution generation.</i></sub></p>
  </div>
  
This node provides a seamless, "plug-and-play" integration of DyPE into any FLUX-based workflow.

**✨ Key Features:**
*   **True High-Resolution Generation:** Push FLUX models to 4096x4096 and beyond while maintaining global coherence and fine detail.
*   **Single-Node Integration:** Simply place the `DyPE for FLUX` node after your model loader to patch the model. No complex workflow changes required.
*   **Full Compatibility:** Works seamlessly with your existing ComfyUI workflows, samplers, schedulers, and other optimization nodes like Self-Attention or quantization.
*   **Fine-Grained Control:** Exposes key DyPE hyperparameters, allowing you to tune the algorithm's strength and behavior for optimal results at different target resolutions.
*   **Zero Inference Overhead:** DyPE's adjustments happen on-the-fly with negligible performance impact.

<div align="center">
<img alt="Node" width="70%" src="https://github.com/user-attachments/assets/3ef232d2-6268-4e3d-8522-b704dade03ac" />
</div>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🚀 Getting Started

The easiest way to install is via **ComfyUI Manager**. Search for `ComfyUI-DyPE` and click "Install".

Alternatively, to install manually:

1.  **Clone the Repository:**

    Navigate to your `ComfyUI/custom_nodes/` directory and clone this repository:
    ```sh
    git clone https://github.com/wildminder/ComfyUI-DyPE.git
    ```
2. **Start/Restart ComfyUI:**
   Launch ComfyUI. No further dependency installation is required.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## 🛠️ Usage

Using the node is straightforward and designed for minimal workflow disruption.

1.  **Load Your FLUX Model:** Use a standard `Load Checkpoint` node to load your FLUX model (e.g., `FLUX.1-Krea-dev`).
2.  **Add the DyPE Node:** Add the `DyPE for FLUX` node to your graph (found under `model_patches/unet`).
3.  **Connect the Model:** Connect the `MODEL` output from your loader to the `model` input of the DyPE node.
4.  **Set Resolution:** Set the `width` and `height` on the DyPE node to match the resolution of your `Empty Latent Image`.
5.  **Connect to KSampler:** Use the `MODEL` output from the DyPE node as the input for your `KSampler`.
6.  **Generate!** That's it. Your workflow is now DyPE-enabled.

> [!NOTE]
> This node specifically patches the **diffusion model (UNet)**. It does not modify the CLIP or VAE models. It is designed exclusively for **FLUX-based** architectures.

### Node Inputs

*   **`model`**: The FLUX model to be patched.
*   **`width` / `height`**: The target image resolution. **This must match the resolution set in your `Empty Latent Image` node.**
*   **`method`**: The core position encoding extrapolation method. `yarn` is the recommended default, as it forms the basis of the paper's best-performing "DY-YaRN" variant.
*   **`enable_dype`**: Enables or disables the **dynamic, time-aware** component of DyPE.
    *   **Enabled (True):** Both the noise schedule and RoPE will be dynamically adjusted throughout sampling. This is the full DyPE algorithm.
    *   **Disabled (False):** The node will only apply the dynamic noise schedule shift. The RoPE will use a static extrapolation method (e.g., standard YARN). This can be useful for comparison or if you find it works better at certain moderate resolutions.
*   **`dype_exponent`**: (λt) Controls the "strength" of the dynamic effect over time. This is the most important tuning parameter.
    *   `2.0` (Exponential): Recommended for **4K+** resolutions. It's an aggressive schedule that transitions quickly.
    *   `1.0` (Linear): A good starting point for **~2K-3K** resolutions.
    *   `0.5` (Sub-linear): A gentler schedule that may work best for resolutions just above the model's native 1K.
*   **`base_shift` / `max_shift`** (Advanced): These parameters control the interpolation of the dynamic noise schedule shift (`mu`). The default values (`0.5`, `1.15`) are taken directly from the FLUX architecture and are generally optimal. Adjust only if you are an advanced user experimenting with the noise schedule.

> [!WARNING]
> It seems the width/height parameters in the node are buggy. Keep the values below 1024x1024; doing so won’t affect your output.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<p align="center">══════════════════════════════════</p>

Beyond the code, I believe in the power of community and continuous learning. I invite you to join the 'TokenDiff AI News' and 'TokenDiff Community Hub'

<table border="0" align="center" cellspacing="10" cellpadding="0">
  <tr>
    <td align="center" valign="top">
      <h4>TokenDiff AI News</h4>
      <a href="https://t.me/TokenDiff">
        <img width="40%" alt="tokendiff-tg-qw" src="https://github.com/user-attachments/assets/e29f6b3c-52e5-4150-8088-12163a2e1e78" />
      </a>
      <p><sub>🗞️ AI for every home, creativity for every mind!</sub></p>
    </td>
    <td align="center" valign="top">
      <h4>TokenDiff Community Hub</h4>
      <a href="https://t.me/TokenDiff_hub">
        <img width="40%" alt="token_hub-tg-qr" src="https://github.com/user-attachments/assets/da544121-5f5b-4e3d-a3ef-02272535929e" />
      </a>
      <p><sub>💬 questions, help, and thoughtful discussion.</sub> </p>
    </td>
  </tr>
</table>

<p align="center">══════════════════════════════════</p>

## ⚠️ Known Issues and Limitations
*   **FLUX Only:** This implementation is highly specific to the architecture of the FLUX model and will not work on standard U-Net models (like SD 1.5/SDXL) or other Diffusion Transformers.
*   **Parameter Tuning:** The optimal `dype_exponent` can vary based on your target resolution. Experimentation is key to finding the best setting for your use case. The default of `2.0` is optimized for 4K.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License
The original DyPE project is patent pending. For commercial use or licensing inquiries regarding the underlying method, please contact the [original authors](mailto:noam.issachar@mail.huji.ac.il).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

*   **Noam Issachar, Guy Yariv, and the co-authors** for their groundbreaking research and for open-sourcing the [DyPE](https://github.com/guyyariv/DyPE) project.
*   **The ComfyUI team** for creating such a powerful and extensible platform for diffusion model research and creativity.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
[stars-shield]: https://img.shields.io/github/stars/wildminder/ComfyUI-DyPE.svg?style=for-the-badge
[stars-url]: https://github.com/wildminder/ComfyUI-DyPE/stargazers
[issues-shield]: https://img.shields.io/github/issues/wildminder/ComfyUI-DyPE.svg?style=for-the-badge
[issues-url]: https://github.com/wildminder/ComfyUI-DyPE/issues
[forks-shield]: https://img.shields.io/github/forks/wildminder/ComfyUI-DyPE.svg?style=for-the-badge
[forks-url]: https://github.com/wildminder/ComfyUI-DyPE/network/members
