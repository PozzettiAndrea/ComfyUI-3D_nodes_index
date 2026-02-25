# 🎬 ComfyUI Auto-Edit Workbench

A powerful Custom Node for **ComfyUI** that acts as a **mini video editing studio**. 
It automatically assembles (concatenates) multiple video clips from a folder into a single sequence, handling resolution resizing, aspect ratios, and frame rates intelligently.

## ✨ Key Features

*   **Batch Assembly**: Loads all video files from a specific folder automatically.
*   **3 Resize Modes**:
    *   **Crop (Fill Screen)**: Fills the screen, cropping edges if necessary (perfect for mixing vertical/horizontal footage).
    *   **Fit (Black Bars)**: Adds black borders (letterboxing) so the entire video is visible.
    *   **Stretch**: Distorts the video to fit the target resolution perfectly.
*   **Smart Strategies**:
    *   **Resolution**: Auto-detect from the *First Video*, *Smallest*, *Largest*, or use a *Custom* size.
    *   **FPS**: Auto-detect from *First Video*, *Lowest*, *Highest*, or *Custom*.
*   **Audio Support**: Concatenates audio tracks seamlessly.
*   **Safety Limits**: `limit_duration_sec` parameter to trim the output (great for testing without Out-Of-Memory errors).

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)
1.  Install [ComfyUI Manager](https://github.com/ltdrdata/ComfyUI-Manager).
2.  Click **"Install via Git URL"**.
3.  Paste this repository URL: `https://github.com/Verolelb/ComfyUI-Video-Workbench`.

### Method 2: Manual Installation
1.  Navigate to your `ComfyUI/custom_nodes/` directory.
2.  Clone this repository:
    ```bash
    git clone https://github.com/Verolelb/ComfyUI-Video-Workbench.git
    ```
3.  Open a terminal in this folder and install the requirement:
    ```bash
    pip install -r requirements.txt
    ```
    *(This node relies on `moviepy` and `numpy`).*

## 🛠️ How to use

### 1. Inputs

*   **`directory_path`**: Absolute path to your video folder (e.g., `C:/Users/You/Desktop/MyClips`).
*   **`sort_strategy`**: Order of clips (Alphabetical, Date, Random).
*   **`resize_mode`**: 
    *   Use **Crop** for immersive, full-screen montages (e.g., Shorts/Reels).
    *   Use **Fit** to preserve all details with black bars.
*   **`resolution_strategy`**: Keep it on **"First Video"** to let the first clip dictate the format of the whole timeline.
*   **`fps_strategy`**: Keep on **"First Video"** or force a **Custom** value (e.g., 24, 30, 60).

### 2. Outputs

1.  **`IMAGE`**: The assembled video stream.
2.  **`AUDIO`**: The combined audio track.
3.  **`FLOAT` (fps)**: The final frame rate (useful to connect to the "frame_rate" input of saving nodes).

### 3. Recommended Workflow for Saving

To save the video **with audio**, it is highly recommended to use the **Video Combine** node from the [ComfyUI-VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite).

*   Connect `AutoEditWorkbench` **IMAGE** -> `Video Combine` **images**.
*   Connect `AutoEditWorkbench` **AUDIO** -> `Video Combine` **audio**.
*   Connect `AutoEditWorkbench` **FPS** -> `Video Combine` **frame_rate** (Convert widget to input).
*   Set format to **`video/h264-mp4`**.

## ❤️ Credits

Created by **Verolelb**.
Powered by [MoviePy](https://zulko.github.io/moviepy/).