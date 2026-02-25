---

# ComfyUI Switch Samplers Pack

This custom node pack for **[ComfyUI](https://github.com/comfyanonymous/ComfyUI)** introduces advanced sampler and scheduler switching strategies. It allows users to dynamically change samplers, schedulers, models, VAEs, CFG scales, denoise values, and conditioning between stages of a generation.

The pack is designed for both **same-family checkpoints** (e.g. SDXL variants).

---

## ✨ Features

* **4 Fully Working Sampler Nodes**

  * Step Switch KSampler
 <img width="1424" height="904" alt="StepSwitchKSampler" src="https://github.com/user-attachments/assets/c779650e-a460-4d9b-b321-7d6e471e0649" />


  
  * MultiStep KSampler
 <img width="1492" height="1055" alt="MultiStepKSampler" src="https://github.com/user-attachments/assets/53a41831-e0fb-45ec-8c3f-5a7c36a08374" />


    
 

* **Upgraded Cross-Model Nodes**

  * **CrossStepSwitchKSampler** → Two-stage sampler with optional second model/vae/text encoder. Perfect for workflows like *SDXL → Flux*.
 <img width="1637" height="1275" alt="CrossStepSwitchKSampler" src="https://github.com/user-attachments/assets/07e04b99-4d55-4536-8805-d826526b64e6" />

    
  * **CrossMultiStepKSampler** → Three-stage sampler with full control over models, VAEs, CFGs, denoise values, samplers, schedulers, and conditioning for each stage.
 <img width="1764" height="1686" alt="CrossMultiStepKSampler" src="https://github.com/user-attachments/assets/cf709a04-8796-4352-be3a-e5aa175f640c" />

    

* **Flexible Conditioning**

  * Each stage can use its own **positive** and **negative** conditioning (from the correct text encoder for the model in that stage).
  
* **Latent Bridging**

  * Automatically performs **VAE decode → encode** when switching between different model/vae pairs.
  * Ensures compatibility when mixing architectures.

---

## 📦 Installation

1. Clone or download this repository into your ComfyUI `custom_nodes` folder:

   ```bash
   cd ComfyUI/custom_nodes
   git clone https://github.com/azazeal04/comfyui-switch-samplers.git
   ```

   Or manually place the folder inside `ComfyUI/custom_nodes`.

2. Restart ComfyUI.

3. The new nodes will appear under:

   * **Azazeal / Switch Samplers** (all original switching nodes)

              Or
     
* **Install from manager**

  Search for comfyui-switch-samplers
   
   
---

## 🛠️ Usage

* Connect a **Model**, **VAE**, **Conditioning** (positive/negative), and **Latent Image** into one of the switch nodes.
* Select samplers, schedulers, step counts, CFG values, and denoise levels per stage.
* Outputs a new **LATENT** tensor for further processing or decoding.

---

## ⚡ Example Workflows

* **StepSwitchKSampler**
  Run first 10 steps with Euler on SDXL, then switch to 10 steps with DPM++ 2M Karras for refinement.

* **MultiStepKSampler**
  Run 3 consecutive sampler stages with different samplers, schedulers, and denoise values.

* **CrossStepSwitchKSampler**
  Run SDXL for the first half, then seamlessly switch to Flux with its own VAE and text encoder for final refinement.

* **CrossMultiStepKSampler**
  Run three different models in sequence, e.g.:

  1. SDXL for base composition
  2. Flux for style transfer
  3. Qwen for final polish

---


## 🎁 Very Special
  A very special THANK YOU to Afroman4peace for testing the nodes with Flux, Qwen Image and Wan models enabling me to correct the errors, could not have done it without him.
  He has really great models, go check them out on [CivitAI](https://civitai.com/user/Afroman4peace).
  Afoman4peace, again thank you very much for your help testing the nodes these past 2 days, I really could not have done it without your help.

---

## 📖 Node Categories

* **Azazeal / Switch Samplers** → Single-model switch strategies.

---

## 📜 License

This project is licensed under the **MIT License**.
You are free to use, modify, and distribute it, with attribution.

---

## 🙌 Credits

* Built on top of [ComfyUI](https://github.com/comfyanonymous/ComfyUI).
* Extended sampler logic inspired by community contributions.
* Cross-model VAE bridging and conditioning handling by this custom pack.

---

