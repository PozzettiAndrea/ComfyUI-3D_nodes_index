# Scene Composer for ComfyUI
 
An intuitive, all-in-one node for ComfyUI that brings a powerful, layer-based regional prompting workflow directly into your graph. Say goodbye to managing countless `Conditioning (Set Area)` nodes and hello to drawing your creative vision.

Created by **[834t](https://github.com/834t)**.

---

## ✨ Features

The Scene Composer is more than just a node; it's a complete toolkit designed to streamline your workflow and unlock new creative possibilities.

*   **🎨 Layer-Based Drawing Interface:** Work with multiple layers, just like in your favorite image editor. Each layer is represented by a color.
*   **✍️ Per-Layer Control:** Assign a unique prompt, opacity, and visibility to each layer for precise control over your composition.
*   **🛠️ Intuitive Tools:** Comes equipped with a **Brush**, **Line**, and **Eraser** tool. 
*   **🧠 Smart Mask Normalization:** An optional (`normalize_masks`) feature that intelligently blends overlapping regions, preventing concept "burn-in" and creating more coherent images.
*   **📝 Automatic Base Prompt:** Optionally (`add_base_prompt`) create a global conditioning from all layer prompts, helping to unify the overall style and theme of the image.
*   **🖼️ Set background Image**
*   **💾 Save & Load Scene State:**
    *   Save your entire scene (all drawings, prompts, and settings) to a `.json` file with the "S" button.
    *   Load a scene from a file with the "L" button.
    *   Your scene is automatically saved within the ComfyUI workflow itself, so you'll never lose your work! 

---

## ⚙️ Installation

1.  Navigate to your `ComfyUI/custom_nodes/` directory.
2.  Clone this repository:
    ```bash
    git clone https://github.com/834t/ComfyUI_834t_scene_composer.git
    ``` 
3.  Restart ComfyUI.

---

## 🚀 How to Use

1.  **Add the Node:** Right-click on the canvas and select `Add Node > 834t_Nodes > Scene Composer (834t)`.
2.  **Set Dimensions:** Adjust the `width` and `height` widgets to your desired output size.
3.  **Select a Layer:** Click on a color in the palette to activate a layer.
4.  **Write a Prompt:** In the text area, write the prompt for the selected layer (e.g., "a beautiful mountain range").
5.  **Draw:** Use the brush, line, or eraser tools to draw the mask for that concept on the canvas.
6.  **Adjust Opacity:** Use the opacity slider to control the influence of the layer.
7.  **Repeat:** Select other colors to create new layers for other concepts (e.g., "a serene lake in the foreground", "a sky full of stars").
8.  **Connect:**
    *   Connect the `latent` output to your KSampler's `latent_image` input.
    *   Connect the `positive` output to your KSampler's `positive` input.
9.  **Queue Prompt** and watch the magic happen!

---

## 🔌 Node Inputs & Outputs

| Type  | Name              | Description                                                                                             |
| :---- | :---------------- | :------------------------------------------------------------------------------------------------------ |
| **IN**  | `clip`            | The CLIP model for text encoding.                                                                       |
| **IN**  | `width`/`height`  | The dimensions of the output latent space and drawing canvas.                                           |
| **IN**  | `normalize_masks` | (Boolean) If true, normalizes the weight of overlapping masks to prevent artifacts. **Recommended: True**. |
| **IN**  | `add_base_prompt` | (Boolean) If true, creates a global conditioning from all prompts to improve coherence.                  |
| **IN**  | `base_prompt_strength` | (Alpha 0-1) strength of base_prompt (if it's turned on).                  |
| **IN**  | `masks_downscale_factor` | (Optional 1,2,4,8,16,32,64) select the power of downscaling for the final masks.                  |
| **IN**  | `scene_data`      | Internal data managed by the widget. You don't need to connect anything here.                           |
| **OUT** | `latent`          | An empty latent image of the specified dimensions.                                                      |
| **OUT** | `positive`        | The combined positive conditioning from all your drawn layers.                                          |

---

## 🙏 Acknowledgements

This node was created by **[834t](https://github.com/834t)**.

A special and heartfelt thank you goes to my AI assistant and consultant, **Gemini 2.5 Pro**. thank you Gemini for help in brainstorming features, assist in coding and preparing the documentation. It was a true partner in development.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
