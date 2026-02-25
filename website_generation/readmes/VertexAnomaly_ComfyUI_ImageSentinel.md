# ♻️ ComfyUI ImageSentinel Node Pack

**Author:** VertexAnomaly  
**Version:** 1.0.0

---

## What is ImageSentinel?

**ImageSentinel** is a custom node pack for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that automatically watches and reloads images from a specified folder. It supports common image formats (e.g., PNG, JPG) as well as PSD files, automatically converting them into standard RGB images using **psd-tools**. The node delivers the images as Torch FloatTensors, making them immediately usable in your ComfyUI workflows.

---

## Why Use ImageSentinel?

- **Automatic Image Reloading**  
  ImageSentinel continuously monitors your selected image file. If the image changes, the node detects this via hashing and automatically reloads it.

- **Built-in PSD Support**  
  Seamlessly loads PSD files, automatically converting them to a flattened RGB image for immediate use.

- **Integrated Delay for Instant Queue Mode**  
  In Instant Queue mode, ComfyUI can execute nodes repeatedly in quick succession. To manage this, ImageSentinel has an optional delay parameter to pause before each file check.  
  **This delay ensures your node doesn’t run repeatedly without a pause**, giving external processes (like editing and saving images) adequate time to complete.

- **Recommended Fixed Seed Usage**  
  It is recommended to use fixed seeds in Instant Queue mode when using this node. Fixed seeds help prevent ComfyUI from repeatedly resampling the same input unnecessarily when no actual changes to your image have occurred. This helps save computational resources and ensures consistent results across runs.

- **Failsafe Placeholder**  
  If the specified image cannot be found or loaded correctly, ImageSentinel returns a default black 512×512 placeholder to ensure your workflow continues smoothly.

---

## Dependencies and Installation

### Dependencies:
- [psd-tools](https://pypi.org/project/psd-tools/)
- [Pillow](https://pillow.readthedocs.io/)
- [numpy](https://numpy.org/)
- [torch](https://pytorch.org/)

---

## Installation Options

### ✅ Option 1: Install via ComfyUI Manager (Recommended)

1. Open **ComfyUI Manager**.
2. Click **"Install via Git URL"**, paste this URL, and click **Install**:
```bash
https://github.com/VertexAnomaly/ComfyUI_ImageSentinel
```
3. **Restart ComfyUI** to activate the node pack.

### ✅ Option 2: Manual Installation

1. Clone or download this repository:
```bash
git clone https://github.com/VertexAnomaly/ComfyUI_ImageSentinel.git
```
2. Move the downloaded folder into your ComfyUI custom nodes directory:
```markdown
ComfyUI/
└── custom_nodes/
    └── ComfyUI_ImageSentinel/
```
3. Install dependencies manually (if not using ComfyUI Manager):
```
pip install -r requirements.txt
```
3. **Restart ComfyUI** to activate the node pack.

---

## How to Use ImageSentinel

Follow these steps to integrate **ImageSentinel** into your ComfyUI workflow:

1. **Launch ComfyUI**  
   Open ComfyUI and right-click anywhere on the workflow canvas.

2. **Add the Node**  
   Navigate to the **♻️ ImageSentinel** category and select the **ImageSentinel** node.

3. **Configure the Node**  
   Set these properties in the node’s settings:
   - **`folder_path`**: The directory containing your image file.
   - **`image_name`**: The exact filename you want to monitor (e.g., `myimage.png` or `project.psd`).
   - **`delay_seconds`** *(Optional)*: Number of seconds to wait before checking the file. This delay is helpful in Instant Queue mode to ensure external file saves (from Photoshop or other editing software) are fully completed before the node reloads the image.

4. **Connect the Output**  
   Connect the **IMAGE** output pin from ImageSentinel to your subsequent nodes (e.g., Preview, VAE Encoder, or other image-processing nodes).

5. **Run Your Workflow**  
   Initially, ImageSentinel loads your selected image. After that, it continuously monitors the image file:
   - Each time you overwrite and save the monitored image file from external software, ImageSentinel detects the update.
   - The node automatically reloads the new image, seamlessly updating your workflow.

---

## Explanation of the Delay Mechanism (Instant Queue Mode)

When using ComfyUI’s **Instant Queue mode**, nodes may rapidly re-execute, potentially causing unnecessary reloads even when your monitored image hasn't fully updated yet. The built-in delay in ImageSentinel addresses this issue:

- **Controlled Reloading:**  
  ImageSentinel pauses execution for the duration set by the **`delay_seconds`** parameter before checking if the monitored image file has changed. This delay ensures that external file operations (such as saving in Photoshop) are fully completed, preventing premature reloads.

- **Efficiency and Stability:**  
  This brief pause helps stabilize your workflow by preventing rapid, unnecessary reloads, ensuring resources are conserved, and guaranteeing consistent results.

### Recommended Fixed Seeds

Additionally, when operating in Instant Queue mode, it's highly recommended that you use **fixed seeds** in your workflow configuration. Fixed seeds help prevent ComfyUI from repeatedly resampling and executing nodes unnecessarily when the monitored image hasn’t changed, further optimizing performance and consistency.

---

## Contributing

Your contributions, bug reports, suggestions, and enhancements are greatly appreciated! 

Here's how you can contribute:

1. **Fork** this repository.
2. Make your enhancements or fixes in your forked repository.
3. Submit a **pull request** clearly explaining your changes.
4. You can also open an issue on GitHub to report bugs or suggest new features.



