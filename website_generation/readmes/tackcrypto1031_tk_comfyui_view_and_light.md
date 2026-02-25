# TK View & Light

A professional ComfyUI node that provides an interactive 3D widget for controlling camera angles and lighting directions. This tool is designed to help creators easily visualize and generate precise prompts for 3D-aware image generation.

![Preview](https://github.com/tackcrypto1031/tk_comfyui_view_and_light/blob/main/sample/sample.png)
![Preview](https://github.com/tackcrypto1031/tk_comfyui_view_and_light/blob/main/sample/sample2.png)

## 🚀 Key Features

- **Interactive 3D Widget**: A real-time 3D viewport using Three.js to visualize camera and light positions.
- **Precision Camera Control**: Adjust horizontal angle (0-360°), vertical angle (-90 to 90°), and zoom levels.
- **Dynamic Lighting Control**: Enable/Disable lighting, adjust light source direction, and choose light colors with a built-in color picker.
- **Dual Prompt Output**: Automatically generates two separate prompts:
  - `camera_prompt`: Detailed camera positioning (e.g., "front-right quarter view, eye-level shot, medium shot").
  - `light_prompt`: Detailed lighting description (e.g., "(light source from the Right Front, High), #FFFFFF colored light").
- **Visual Feedback**: Real-time updates of the 3D scene based on your inputs.

## 🛠️ Installation

### Method 1: ComfyUI-Manager (Recommended)
1. Search for `TK View & Light` in the ComfyUI-Manager.
2. Click **Install**.
3. Restart ComfyUI.

### Method 2: Git Clone
1. Navigate to your ComfyUI `custom_nodes` directory.
2. Clone this repository:
   ```bash
   git clone https://github.com/tackcrypto1031/tk_comfyui_view_and_light.git
   ```
3. Restart ComfyUI.

## 📖 Usage

1. Add the **TK View & Light** node (found under `TK Nodes` category).
2. Use the sliders or the **3D Widget** directly:
   - **Left Click & Drag**: Adjust Camera View.
   - **Click "Light Mode"**: Switch the widget control to adjust the Light source position.
3. Connect the `camera_prompt` and `light_prompt` outputs to your text encoder or prompt merger.
4. (Optional) Connect an input `image` to see it reflected in the 3D widget's background or reference plane.

## 🙏 Acknowledgments

Special thanks to the following open-source projects for their technology and inspiration:
- [ComfyUI-qwenmultiangle](https://github.com/jtydhr88/ComfyUI-qwenmultiangle) - For the multi-angle camera prompt logic.
- [ComfyUI-AdvancedCameraPrompts](https://github.com/jandan520/ComfyUI-AdvancedCameraPrompts) - For advanced camera control techniques.

## ✉️ Contact

- **Author**: Tack
- **Email**: [tack1031@gmail.com](mailto:tack1031@gmail.com)

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
