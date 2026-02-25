# ComfyUI ContactSheet Auto 🎞️

A lightweight ComfyUI extension designed to automate the creation of video contact sheets (preview grids). 

It solves the common problem of **"How many frames should I skip to get exactly X images from this video?"** by dynamically calculating the `select_every_nth` parameter based on the video length and your desired grid layout.

## ✨ Features

- **Dynamic Interval Calculation**: Automatically calculates the frame skip interval (`select_every_nth`) based on the video file duration and your target Rows/Columns.
- **Resource Efficient**: Uses OpenCV to read video metadata without loading the entire video into memory.
- **Batch to Grid**: Includes a simple node to stitch a batch of images into a single grid image (Contact Sheet).
- **Workflow Automation**: Designed to pipe values directly into **Video Helper Suite (VHS)** nodes for a fully automated workflow.

## 🛠️ Installation

### Method 1: Manual Installation
1. Navigate to your ComfyUI `custom_nodes` directory.
2. Clone this repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ComfyUI_ContactSheet_Auto.git
Install dependencies (if not already installed):

bash
pip install opencv-python numpy
Restart ComfyUI.

🔗 Dependencies
Required: opencv-python (usually pre-installed in ComfyUI environments).

Highly Recommended: ComfyUI-VideoHelperSuite (VHS). This node calculates the values, but VHS is the best tool to actually load the video frames using those values.

📖 Usage Guide
1. The Logic
Instead of guessing "I need to skip every 50 frames to get 20 images," you simply tell this node: "I want a 4x5 grid." It does the math for you.

2. Step-by-Step Workflow
Add Node: Search for Video Interval Auto-Calc.

Configure:

video_path: Path to your video file.

rows: Desired number of rows (e.g., 4).

cols: Desired number of columns (e.g., 5).

Connect to VHS Loader:

Add a Load Video (Path) node from Video Helper Suite.

Right-click the VHS node -> Convert Widget to Input -> Select frame_load_cap and select_every_nth.

Connect select_every_nth from Auto-Calc to VHS.

Connect frame_load_cap from Auto-Calc to VHS.

Create Grid:

Connect the IMAGE output from VHS to the Batch to Grid Image node (included in this pack).

Set the cols to match your setting in step 2.

Save: Connect to a Save Image node.

🧩 Node Description
🎥 Video Interval Auto-Calc
Inputs:

video_path (STRING): Absolute path to the video file.

rows (INT): Number of rows in the final grid.

cols (INT): Number of columns in the final grid.

Outputs:

select_every_nth (INT): The calculated frame skip interval.

frame_load_cap (INT): Total number of frames to load (Rows * Cols).

total_count (INT): Same as cap, useful for other calculations.

🖼️ Batch to Grid Image
Inputs:

images (IMAGE): The image batch (usually from a video loader).

cols (INT): How many columns per row.

Outputs:

IMAGE: A single image containing the grid.

🤝 Contributing
Feel free to submit Pull Requests or report issues. This is a simple utility node, but improvements are welcome!
