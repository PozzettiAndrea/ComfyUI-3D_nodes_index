# ComfyUi-ConditioningTimestepSwitch

A custom node for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that allows temporal switching between prompts.

## ✨ Use case.

- Some models such as **Z-Image Turbo** exhibit low seed variance, meaning they generate very similar images even when the seed changes.

- This node starts the denoising process with an empty (or alternative) prompt and then switches to your desired prompt after a specified timestep **threshold**.

- By delaying the main prompt, you introduce more randomness early in the diffusion process, which can significantly improve output diversity.

<img src="https://github.com/user-attachments/assets/c49fe009-dace-4479-8c40-fcc2e68e270f" width="700" />

## 📥 Installation

Navigate to the **ComfyUI/custom_nodes** folder and run the following command in your terminal:

```git clone https://github.com/BigStationW/ComfyUi-ConditioningTimestepSwitch```

## 🛠️ Usage

<img src="https://github.com/user-attachments/assets/a305dd07-ef65-4040-b581-7c6bc9fd3b8b" width="700" />

An exmple workflow (for Z-image turbo) can be found [here](https://github.com/BigStationW/ComfyUi-ConditioningTimestepSwitch/blob/main/workflow_Z-image_turbo.json).
