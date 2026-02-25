
# Vantage Long Wan Video 

**VantageLongWanVideo** is a lightweight project management system for **ComfyUI**, designed for long-running, prompt-driven video generation. It simplifies workflow management by saving prompts to disk, handling continuity across runs, and allowing resuming or regenerating from any point.

## ✨ Highlights

- This project includes **three nodes**:
	 - **Vantage Project Loader** → Project manager node (saves/loads scripts, computes start points)
	 - **Vantage I2V Single Model Looper** → For **Wan 2.1 / Wan 2.2 AIO** workflows
	 - **Vantage I2V Dual Model Looper** → For **Wan 2.2 High/Low noise** workflows

## ✨ Features

-   Save and load prompt scripts as JSON files
-   Automatic `start_prompt` calculation based on existing output folders    
-   Resume generation from any prompt index    
-   Extend projects with new prompts without re-rendering previous clips    
-   Regenerate selected segments by specifying a positive `start_prompt`    
-   Organized output structure for easy project management    
-   Works with both **single-model** and **dual-model** workflows

[![Watch the video](https://github.com/vantagewithai/VantageLongWanVideo/blob/main/example_workflows/vantage-video.png)](https://youtu.be/wC87B7rIvyQ)

```

## 🧰 Requirements
- ComfyUI (current version).
- Python 3.10+ recommended.
## ⚙️ Installation

### Method 1: Using ComfyUI Manager (Recommended)

1.  Open ComfyUI Manager.
2.  Click on `Install Custom Nodes`.
3.  Search for `VantageLongWanVideo` and click `Install`.
4.  Restart ComfyUI.

### Method 2: Manual Installation
1.  Navigate to your ComfyUI `custom_nodes` directory.
    ```bash
    cd ComfyUI/custom_nodes/
    ```
2.  Clone this repository:
    ```bash
    git clone https://github.com/vantagewithai/VantageLongWanVideo.git
    ```
4.  Restart ComfyUI.

---

