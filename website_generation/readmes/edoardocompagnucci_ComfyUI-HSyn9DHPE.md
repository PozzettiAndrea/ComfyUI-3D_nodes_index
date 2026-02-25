# ComfyUI-HSyn9DHPE

ComfyUI custom nodes for 9D Human Pose Estimation, integrating the [HSyn9DHPE](https://github.com/edoardocompagnucci/HSyn9DHPE) project.

## Description

This extension provides custom nodes for ComfyUI that enable 9D human pose estimation from video inputs. The node processes videos to extract 3D pose keypoints and generates rendered outputs using Houdini integration.

## Node Usage

[Download Node Usage Video](https://github.com/edoardocompagnucci/ComfyUI-HSyn9DHPE/raw/main/images/node_usage_edit.mp4)

## Features

- **Video-based 3D Pose Estimation**: Process videos to extract 9D human pose data
- **Smoothing Options**: Optional smoothing for both 2D detections and 3D poses
- **Houdini Integration**: Automatic rendering of pose keypoints and body meshes
- **Multiple Camera Views**: When `use_hython` is disabled, Houdini opens automatically allowing you to re-frame the render camera and capture the same motion from different camera angles; a key feature of the project
- **ComfyUI Workflow Integration**: Seamlessly integrates into existing ComfyUI workflows

## Example Results

[Download Results Example Video](https://github.com/edoardocompagnucci/ComfyUI-HSyn9DHPE/raw/main/images/results_example.mp4)

## Installation

### Step 1: Clone the Custom Node Repository

Navigate to your ComfyUI custom nodes directory and clone this repository:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/edoardocompagnucci/ComfyUI-HSyn9DHPE.git
```

### Step 2: Clone the HSyn9DHPE Core Project

Navigate into the custom node folder and clone the HSyn9DHPE project:

```bash
cd ComfyUI-HSyn9DHPE
git clone https://github.com/edoardocompagnucci/HSyn9DHPE.git
```

### Step 3: Create the Conda Environment

Navigate into the HSyn9DHPE folder and create the conda environment:

```bash
cd HSyn9DHPE
conda env create -f environment.yml -p ./env
```

### Step 4: Activate the Environment

Activate the newly created conda environment:

```bash
conda activate ./env
```

### Step 5: Install MMCV

Install the required MMCV version:

```bash
mim install mmcv==2.1.0
```

### Step 6: Download MMPose Model

Download the MMPose model configuration and checkpoint:

```bash
mim download mmpose --config td-hm_hrnet-w48_8xb32-210e_coco-wholebody-384x288 --dest ./checkpoints
```

### Step 7: Configure Houdini Paths

**IMPORTANT**: Before using the node, you need to update the hardcoded Houdini paths in the `inference_core.py` file to match your Houdini installation.

Open `ComfyUI-HSyn9DHPE/inference_core.py` and locate these lines (around line 14-15):

```python
self.houdini_exe = r"C:\Program Files\Side Effects Software\Houdini 20.5.445\bin\houdini.exe"
self.hython_exe = r"C:\Program Files\Side Effects Software\Houdini 20.5.445\bin\hython.exe"
```

Update these paths to match your Houdini installation directory and version.

### Step 8: Restart ComfyUI

After completing the installation and configuration, restart ComfyUI to load the new custom nodes.
