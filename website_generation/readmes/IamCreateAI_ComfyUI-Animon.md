# ComfyUI-Animon

This repository provides **Animon integration for ComfyUI**, offering a set of custom nodes powered by the [Animon API](https://www.animon.ai/). With these nodes, you can generate videos from images, interpolate between start and end frames, and upscale videos — all with more flexibility and control than the Animon web interface.

We are actively working to bring more features and APIs to match the full capabilities of the Animon platform.

> ⚠️ **Note:** This extension requires a **newer version of ComfyUI**, as it depends on updated node definitions. It also utilizes official ComfyUI nodes like `SaveVideo` to write video files to disk.

Currently, only **custom nodes** are supported. Support for **official ComfyUI API nodes** is in development and will be released soon.


# 🚀 Quick Start

## Installation

You can install this repository either by using `git clone` or via the [ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager) (a fantastic project that makes managing custom nodes effortless).

**Option 1: Git Clone**

1. Clone this repository into the `custom_nodes` folder of your ComfyUI directory:

   ```bash
   git clone https://github.com/IamCreateAI/ComfyUI-Animon.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

**Option 2: ComfyUI-Manager**

1. Make sure ComfyUI-Manager is up to date.

2. Open the **Custom Nodes Manager** and install the node as shown below:

![comfyui_manager_install](https://github.com/user-attachments/assets/28ded1b9-c782-427b-8fdc-51af3a4ea56a)

## How to Use

1. Start or restart ComfyUI to load the newly installed nodes.

2. Obtain your API key from the [Animon API Platform](https://www.animon.ai/).

3. Open one of the example workflows (e.g., `AnimonI2V`), enter your API key, and run the workflow.


# 🗂️ Workflow Examples

You can find several example workflows in the `workflows` folder. Try them out to explore different use cases!

## 📽️ Image to Video

Generates a video from a **single first-frame image** and a **text prompt**.

![workflow_i2v](https://github.com/user-attachments/assets/2c02d7b0-b55c-4349-9e56-2f590aa1e65a)


## 🔁 Start-End to Video

Generates a video using both a **starting image** and an **ending image**.

![workflow_ib2v](https://github.com/user-attachments/assets/90b7279e-f0c4-4838-bc7d-ead2cb9440e6)

**Notes:**

- If using **more than one image**, you must **upload them to the server first**.
- This workflow demonstrates two upload methods:
  1. `Animon Upload Image` – upload local image files directly.
  2. `ComfyUI Load Image` → `Animon Upload Image (from Tensor)` – load and upload images from tensors.

> 💡 **Tip:** The start and end frames can be the **same image**. In that case, you can reuse the `VIDEO_ID` from a previous generation instead of uploading again.


## 🔼 Upscale Video

Upscales a video to **1080P at 24 FPS**.

![workflow_sr](https://github.com/user-attachments/assets/d46ba28f-f220-4797-9ed7-595d10505b5b)


**Requirements:**

- Input video must be **smaller than 1080P**.
- Input must contain **no more than 360 frames**.

## 🎬 Image to Video + Upscale

This workflow combines both generation and upscaling in a seamless process: it first generates a video from an image and a text prompt, then upscales the resulting video to 1080P resolution, and finally outputs the high-resolution result.

![workflow_i2v_sr](https://github.com/user-attachments/assets/15056be1-2984-42dc-a7dc-b1e52c09b466)


# 🧩 Node Overview

Animon provides **three types of nodes** for use in ComfyUI:

1. **Key Node** – for setting your API key.
2. **Generate Nodes** – for generating videos.
3. **Upload Nodes** – for uploading images/videos.

To add a node: **Right-click** in the ComfyUI workspace → `Add Node` → `Animon` → `Node Name`.

![menu](https://github.com/user-attachments/assets/97133254-1837-46dd-91e7-f6ab5facc561)


## 🔐 Key Node

This node is used to input your **Animon API key**, available from the [Animon API platform](https://www.animon.ai/).

> ⚠️ **Important:**  
> Always **remove your API key** before sharing workflows.  
> If you forget, disable the key immediately via the Animon platform.

## 🎥 Generate Nodes

These nodes handle video generation. Currently supported: `Image to Video`, `Start-End Frame to Video`, `Upscale Video`.

![node_i2v_ib2v](https://github.com/user-attachments/assets/4ec049aa-608b-4517-b21f-7ad21bef7f95)

You can choose the generation model in the node settings.

**Supported Models**

- `1-5` and `pro-1-5` serials
   - Up to **81 frames** at **16 FPS** for **480P / 720P**
- `pro-1-6` serials
   - Up to **81 frames** at **16 FPS** for **480P / 720P / 1080P**


## ⬆️ Upload Nodes

When using **multiple images** or **videos**, you must upload them to the server **before generation**.

### 1. Upload Local Resources

Use `Animon Upload Image` or `Animon Upload Video` like ComfyUI’s `LoadImage` or `LoadVideo`.

![node_upload_direct](https://github.com/user-attachments/assets/33f19beb-d1de-4a6a-8856-8cd02943c511)

Then connect the resulting `IMAGE_ID` or `VIDEO_ID` to a generation node.

### 2. Upload from ComfyUI Tensors

If you generate images/videos using other ComfyUI nodes (e.g., Stable Diffusion), use: `Animon Upload Image (from Tensor)` or `Animon Upload Video (from Tensor)`.

![node_upload_from_tensor](https://github.com/user-attachments/assets/6f65d508-05aa-4cc6-8ec4-120cb2a2cb1a)

These convert ComfyUI's internal `IMAGE` type into an `IMAGE_ID` or `VIDEO_ID` usable by Animon.

### 3. Upload from Generated Video Bytes

To reuse a video generated by Animon, use `Animon Upload Video (from Bytes)` and link `VIDEO_BYTES` from any Animon generation node.

![node_upload_from_bytes](https://github.com/user-attachments/assets/2eac8344-54dd-49f7-82ab-98ad38cf9b46)

> 💡 This method avoids re-encoding and is faster than uploading from tensor.

# 📫 Feedback & Contributions

We welcome feedback, feature requests, and contributions!  
Feel free to open an issue or pull request on [GitHub](https://github.com/IamCreateAI/ComfyUI-Animon).
