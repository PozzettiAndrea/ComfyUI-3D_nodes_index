<div align="center">

  <img src="https://github.com/abdozmantar/ComfyUI-DeepExtractV2/blob/main/assets/Logo.png?raw=true?raw=true" style="border-radius: 24px;" alt="logo" width="180px"/>

  [![Commit activity](https://img.shields.io/github/commit-activity/t/abdozmantar/ComfyUI-DeepExtractV2/main?cacheSeconds=0)](https://github.com/abdozmantar/ComfyUI-DeepExtractV2/commits/main)
  ![Last commit](https://img.shields.io/github/last-commit/abdozmantar/ComfyUI-DeepExtractV2/main?cacheSeconds=0)
  ![License](https://img.shields.io/github/license/abdozmantar/ComfyUI-DeepExtractV2)

<a href="https://www.buymeacoffee.com/abdullahozmantar"><img src="https://img.buymeacoffee.com/button-api/?text=Support%20DeepExtract&emoji=%F0%9F%9A%80&slug=abdullahozmantar&button_colour=FFDD00&font_colour=000000&font_family=Poppins&outline_colour=000000&coffee_colour=ffffff"/></a>

<img src="https://github.com/abdozmantar/ComfyUI-DeepExtractV2/blob/main/assets/qr-code.png?raw=true?raw=true" style="border-radius: 24px;" alt="logo" width="116px"/>

# DeepExtractV2 Node for ComfyUI
</div>

### Transform any track in seconds: our DeepExtractV2 node isolates each audio element flawlessly, letting you remix, analyze, or enhance your music faster than ever, all from a single, ultra-efficient node.

<div align="center">

---

[**Installation**](#installation) | [**Usage**](#usage) | [**Example**](#example)  | [**Node Inputs - Outputs**](#node-inputs---outputs)

---
</div>

## Installation

Follow these steps to add **ComfyUI-DeepExtractV2** to your ComfyUI setup and start separating audio tracks instantly:

### 1. Navigate to the ComfyUI `custom_nodes` Folder

Locate your ComfyUI installation folder. Inside, you will find a folder named `custom_nodes`.

> **Tip:** This is where all third-party nodes should be placed.

```text
ComfyUI/
└─ custom_nodes/
```

### 2. Clone the Repository

You can clone this repository directly into the `custom_nodes` folder. Open a terminal or command prompt and run:

```bash
cd path/to/ComfyUI/custom_nodes
git clone https://github.com/abdozmantar/ComfyUI-DeepExtractV2.git
```

This will download all necessary files into a folder named `ComfyUI-DeepExtractV2`.

### 3. (Optional) Update the Repository

If you already have the repository and want to update it with the latest version:

```bash
cd path/to/ComfyUI/custom_nodes/ComfyUI-DeepExtractV2
git pull origin main
```

### 4. Install Dependencies

Go to the node folder and install the requirements:

```bash
cd path/to/ComfyUI/custom_nodes/ComfyUI-DeepExtractV2
python setup.py
```

> 💡 **Windows Users:** You can alternatively double-click `setup.bat` to install all dependencies automatically.

This will ensure all necessary Python packages are installed in the environment ComfyUI uses.

### 5. Restart ComfyUI

After installing the node and its dependencies, restart ComfyUI.
The **DeepExtractV2 node** should now appear in the node list under your custom nodes.

### 6. Add the Node to Your Graph

Double-click anywhere in ComfyUI and **search for the node** by typing `DeepExtractV2`.
Alternatively, **right-click** anywhere, then navigate to:

```
Add Node > DeepExtractV2 > DeepExtractV2 - Separator
```

Click to add it to your graph and start separating audio tracks instantly.

<img src="https://github.com/abdozmantar/ComfyUI-DeepExtractV2/blob/main/assets/NodePath.png?raw=true" style="border-radius: 24px;" alt="webui-demo" width="100%"/>


# Usage
---
### Overview

- The DeepExtractV2 Node allows you to separate audio tracks into individual stems, such as vocals, drums, bass, and other elements. By connecting your mixed audio to this node in ComfyUI, you can isolate specific components of a song or audio file for further processing, manipulation, or preview.

 <img src="https://github.com/abdozmantar/ComfyUI-DeepExtractV2/blob/main/assets/NodeUsage.png?raw=true" style="border-radius: 24px;" alt="webui-demo" width="100%"/>

---

# Example

Suppose you want to separate a song into individual components like vocals, drums, bass, and other instruments. Here’s how you can use the **DeepExtractV2 Node** to achieve this:

### Load an Audio File

First, load your mixed audio track into ComfyUI. This is the input that the **DeepExtractV2 Node** will process.

### Add the DeepExtractV2 Node

Insert the **DeepExtractV2 Node** into your workflow. You will see options to:

* **Select which stem to isolate**: e.g., `vocals`, `drums`, `bass`, `other`
* **Choose the method for the remaining stems**:

  * `add` → sums all other stems into one track (useful for “no_vocals” type outputs)
  * `minus` → subtracts the selected stem from the original track
  * `none` → does not produce any complementary track
* **Set processing parameters**: device (CPU/GPU), chunk overlap, number of shifts, segment size, bit depth, audio format, etc.

### Connect Inputs and Outputs

* Connect your audio file to the **track** input of the node.
* Specify an output folder for the separated tracks.
* Adjust optional parameters like `clip_mode` or `audio_format` if needed.

### Configure Stem Selection

* **Extract all stems**: Leave the **stem** input empty and set **other_method = none**. This will give you all four audio outputs separately:

  * `vocals`
  * `drums`
  * `bass`
  * `other`

* **Extract only one stem**: Specify the stem name (e.g., `vocals`). Then you can choose how to handle the remaining audio:

  * `minus_{stem}` → the original track minus the selected stem
  * `no_{stem}` → sum of all other stems (works if **other_method = add**)

> ⚠️ Tip: If you only want all individual stems without combining anything, leave the stem input empty and set **other_method = none**. This is the recommended way to get `vocals`, `drums`, `bass`, and `other` as separate outputs.


### Process the Audio

Run the workflow. The node will separate your audio based on your configuration and save the results in the specified folder. The file names will be automatically generated using the stem name and track name.

### Preview and Further Manipulation

* Connect the outputs to **Preview Audio** nodes to listen to each separated track in real-time.
* You can also route the outputs to other nodes for further processing, effects, or mixing.


**Example Workflow for Extracting All Stems:**

1. Load your song into ComfyUI.
2. Add the DeepExtractV2 Node.
3. Leave **stem** empty and set **other_method = none**.
4. Connect outputs to Preview Audio nodes to listen to each stem.
5. Run the node → outputs: `vocals.wav`, `drums.wav`, `bass.wav`, `other.wav`

This setup ensures you can hear or use every component of your song individually without any missing tracks.

---

## Node Inputs - Outputs

- **Purpose:** This node separates an input audio track into different stems (e.g., vocals, bass, drums) using AI-based separation.

<img src="https://github.com/abdozmantar/ComfyUI-DeepExtractV2/blob/main/assets/NodeInterface.png?raw=true" style="border-radius: 24px;" alt="webui-demo" width="100%"/>

---

### 1. **Track**

* **Type:** Audio
  - The input audio track to be processed. This is the main file the model will analyze to extract the selected stem.

### 2. **Drums**

* **Type:** Audio Output
  - Contains the isolated drum track extracted from the input audio. Useful for remixing or drum-only analysis.

### 3. **Bass**

* **Type:** Audio Output
  - Contains the isolated bass line from the original track. Allows you to manipulate or process only the bass.

### 4. **Other**

* **Type:** Audio Output
  - Captures all remaining instruments or sounds not classified as drums, bass, or vocals. Useful for background or instrumental extraction.


### 5. **Vocals**

* **Type:**  `Audio Output`
  - Provides the isolated vocal track. Ideal for vocal editing, remixing, or karaoke purposes.

### 6. **Derived Stem**

* **Type:** `Audio Output`
  Automatically generated complementary stem based on the selected separation method (`other_method`). Can represent “everything except selected stem” or a custom mix.

### 7. **Out**

* **Type:** `String`
  - Defines the folder name where the separated tracks will be saved. This folder is automatically created inside the main ComfyUI directory.

### 8. **Device**

* **Type:** Enum (`cuda`, `cpu`)
  - Selects the processing device. Using `cuda` enables GPU acceleration for faster inference, while `cpu` works on systems without GPU support.

### 9. **Overlap**

* **Type:** `Float (0.0–1.0)`
  - Controls the overlap between audio chunks during separation. Higher values may improve quality but require more processing time.

### 10. **Shifts**

* **Type:** `Integer (1–20)`
  - Sets the number of random shifts used to stabilize predictions. More shifts improve quality but increase computation time.

### 11. **Segment**

* **Type:** `Integer (0–600)`
  - Defines the segment length (in seconds) to split the input audio. Set to `0` to process the full track without splitting.

### 12. **Bit Depth**

* **Type:** Enum (`default`, `int24`, `float32`)
  - Determines the bit depth of the output audio. `int24` provides higher precision, while `default` uses system settings.

### 13. **Clip Mode**

* **Type:** Enum (`rescale`, `clamp`, `none`)
  - Controls how clipping is handled in output audio. `rescale` normalizes peaks, `clamp` limits them, and `none` disables clipping correction.

### 14. **Audio Format**

* **Type:** Enum (`wav`, `flac`, `mp3`)
  - Specifies the format of the exported audio files. Choose `wav` for uncompressed output or `mp3` for smaller file sizes.

### 15. **MP3 Bitrate**

* **Type:** `Integer (64–320)`
  - Sets the bitrate when exporting as MP3. Higher values improve audio quality but increase file size.

### 16. **MP3 Preset**

* **Type:** `Integer (2–7)`
  - Adjusts the MP3 encoding speed and quality. Lower numbers mean better quality but slower encoding.

### 17. **Jobs**

* **Type:** `Integer (0–32)`
  - Defines how many parallel jobs (threads) to use. Increasing this speeds up processing on multi-core CPUs.

### 18. **Split**

* **Type:** `Boolean`
  - Enables splitting the input audio into smaller chunks to save memory. Recommended for long or high-resolution tracks.

### 19. **Other Method**

* **Type:** Enum (`none`, `add`, `minus`)
  - Determines how to generate the complementary stem (`no_{STEM}`). `add` sums the remaining stems, while `minus` subtracts the selected stem from the original track.

### 20. **Stem**

* **Type:** `String`
  - Defines which stem to isolate (e.g., `vocals`, `drums`, `bass`). The node will separate only this stem and its complementary version.

### 21. **Filename**

* **Type:** `String`
 - Sets the naming pattern for output files. You can use variables like `{track}`, `{stem}`, and `{ext}` to dynamically generate filenames.

---

### Author

**Name:** Abdullah OZMANTAR  
**GitHub:** [https://github.com/abdozmantar](https://github.com/abdozmantar)  

> Developed by Abdullah OZMANTAR
