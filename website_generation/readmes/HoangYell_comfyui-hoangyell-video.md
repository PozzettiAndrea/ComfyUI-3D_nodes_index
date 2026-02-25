# 🦙 comfyui-hoangyell-video-edit 🎬✨

Professional ComfyUI custom nodes for video editing workflows. 🚀

---

**Author:** [hoangyell](http://hoangyell.com/)
*Coding for fun! If you like this project, visit my site or say hi!*
-----------------------------------------------------------------------------------

## ✨ Features

- 📂 Select video and image files via ComfyUI file picker
- 🖼️ Image is scaled and padded to fit video resolution (no crop/stretch)
- 🔍 Zoom transition animation between intro image and main video
- 🎥 All video properties (resolution, fps, pixel format, codec, bitrate) are matched to the original video
- 💾 Output is auto-saved and selectable in ComfyUI
- 🧩 Modular codebase, ready for future expansion (more nodes, helpers, and utilities)


## 🚦 How to Use

1. Move to your `ComfyUI/custom_nodes/` directory:
   ```bash
   cd /path/to/ComfyUI/custom_nodes/
   ```
2. Clone this repository:
   ```bash
   git clone https://github.com/HoangYell/comfyui-hoangyell-video
   ```

3. (Recommended) Activate your Python virtual environment, or create one if you haven't:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Restart ComfyUI.

6. See the example workflow below for how to use the node:

<p align="center">
  <img src="input/how_to_use_this_node.png" alt="How to use the VideoIntroImage node" width="600"/>
</p>

## 🎬 Before & After Example

**Before (Input Video):**

<video src="https://github.com/HoangYell/comfyui-hoangyell-video/blob/main/input/goat.mp4" controls width="320"></video>

**After (Output Video):**

<video src="https://github.com/HoangYell/comfyui-hoangyell-video/blob/main/input/this_is_output.mp4" controls width="320"></video>

## 📦 Requirements

- 🛠️ ffmpeg (system binary)
- 🛠️ ffprobe (system binary)
- 🐍 ffmpeg-python (for future extensibility, see requirements.txt)

## 🧩 Node: VideoIntroImage

**Inputs:**

- 🎞️ `video_path`: Path to the main video file
- 🖼️ `image_path`: Path to the intro image file
- ⏱️ `duration`: Duration (seconds) for the intro image

**Outputs:**

- 📤 `output_video_path`: Path to the output video file
- 📁 `output_video_file`: Output video file (for ComfyUI file output)

## 🛠️ Extensibility

- 🧰 All helpers are in `utils.py` for easy reuse.
- 🏗️ Node code is modular and ready for future splitting into multiple files/classes.
- 📚 Follow the structure in `Bjornulf_custom_nodes` for large-scale node collections.

## 📄 License

MIT
