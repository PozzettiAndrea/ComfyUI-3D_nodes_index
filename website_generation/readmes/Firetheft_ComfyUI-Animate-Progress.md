<div align="center">
   
# ComfyUI Animate Progress

A progress bar beautification plugin designed for [ComfyUI](https://github.com/comfyanonymous/ComfyUI). It replaces the monotonous default progress bar with a vibrant and dynamic experience, complete with an animated character and rich visual effects.
![ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/2259bc23-1275-4485-bf16-caf1103ba4c1)

</div>

---

## ✨ Features

* **Animated GIF Character**: A delightful animated character runs along the progress bar as your task progresses.
* **Rich Customization Options**: Take full control over every detail of the progress bar through a convenient floating settings panel.
* **Multiple Bar Styles**: Comes with 8 unique progress bar animation styles, including Tech Scanner, Pulsing Glow, Plasma Flow, and more.
* **Full Color Customization**: Freely set the start, middle, and end gradient colors of the progress bar to create your own unique style.
* **GIF Selection & Preview**:
    * Choose from over 30 built-in fun GIF animated characters.
    * Supports a "Random" mode for a new surprise with every task.
    * **Live preview GIF animations by hovering** over them in the settings menu for quick and easy selection.
* **Unified UI Style**:
    * All dropdown menus feature a modern, custom style that blends seamlessly with the ComfyUI interface.
    * The progress bar background **automatically adapts to ComfyUI's light/dark themes**, providing a seamless visual experience.
* **Easily Add Your Own Content**: Simply drop your own GIF files into the designated folder to use them in the plugin instantly.

---

## 🛠️ Installation

1.  Open a terminal or command prompt.
2.  Navigate to the `custom_nodes` folder within your ComfyUI installation directory.
    ```bash
    cd path/to/your/ComfyUI/custom_nodes/
    ```
3.  Clone this repository using `git clone`.
    ```bash
    git clone https://github.com/Firetheft/ComfyUI-Animate-Progress.git
    ```
4.  Restart ComfyUI.

---

## 🚀 How to Use

After installing and restarting ComfyUI, the plugin will be enabled automatically.

You will see a floating **"🔜"** icon in the bottom-right corner of the interface. Click it to open or close the settings panel and begin your customization journey!

---

## ⚙️ Customization Options Explained

In the settings panel, you can adjust all of the following options:

* **Enable Plugin**: The master switch for the plugin.
* **GIF Animation**:
    * Select your favorite animated character from the dropdown menu, or choose `Random`.
    * Hover over an option to preview it and click to make your selection.
* **GIF Size (height)**: Adjust the height of the animated character using the slider.
* **GIF Position (top)**: Fine-tune the vertical position of the animated character using the slider.
* **Enable GIF Shadow**: Adds a drop shadow to the animated character for a more 3D look.
* **Shadow Blur**: Adjust the blur radius of the shadow.
* **Bar Style**:
    * Choose a preset background animation style for the progress bar.
    * This also features the unified custom dropdown menu.
* **Bar Gradient Colors**:
    * **Start, Middle, End**: Use the color pickers to define your own custom gradient.
    * **End Color Opacity**: Adjust the transparency of the end color for a smoother transition.
* **Fade In/Out Effect**: Toggle the fade-in/out effect for the progress bar at the beginning and end of a task.

---

## 🎨 Adding Your Own GIFs

Want to see your favorite character running on the progress bar? It's simple!

1.  Find the `.gif` file you want to add.
2.  Place it inside the `web/runners/` folder within the plugin's directory:
    > `ComfyUI/custom_nodes/ComfyUI-Animate-Progress/web/runners/`
3.  No restart is needed! Just reopen the settings panel, and your GIF will appear in the "GIF Animation" dropdown list.

---

## 📄 Other Projects

* **[ComfyUI_Local_Image_Gallery](https://github.com/Firetheft/ComfyUI_Local_Image_Gallery)**: The ultimate local image, video, and audio media manager for ComfyUI.
* **[ComfyUI_Local_Lora_Gallery](https://github.com/Firetheft/ComfyUI_Local_Lora_Gallery)**: A visual gallery node for ComfyUI to manage and apply multiple LoRA models.
* **[ComfyUI_Civitai_Gallery](https://github.com/Firetheft/ComfyUI_Civitai_Gallery)**: A seamless image browser for the Civitai website, integrated directly into your workflow.
