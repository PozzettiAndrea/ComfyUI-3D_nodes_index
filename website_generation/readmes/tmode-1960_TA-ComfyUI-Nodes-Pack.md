# TA-ComfyUI-Nodes-Pack  
A collection of various useful ComfyUI custom nodes  

**Tested with Python 3.12 and pytorch 2.9.1+cu130 and LM-Studio-0.3.37-1-x64**  
**Tested with Python 3.12 and pytorch 2.9.1+cu128 and LM-Studio-0.3.34-1-x64**  
**Tested with Python 3.11 and pytorch 2.9.1+cu128 and LM-Studio-0.3.36-1-x64**

## Installation

### Requirements
This custom node pack requires:
- **ComfyUI-GGUF** - Install it via ComfyUI Manager

### Installing ComfyUI-GGUF
1. Open ComfyUI Manager
2. Search for "ComfyUI-GGUF"
3. Click "Install"
4. Restart ComfyUI

___

## 1. Model Loaders   
1. ta_load_diffusion_model_with_name  
2. ta_load_checkpoint_model_with_name 
3. ta_load_gguf_model_with_name  

_These are model loaders with an additional output that displays the model name so that it can be used in the further workflow._  

![Load Diffusion Model](images/TA_Load_Diffusion_Model_(with_Name).png)

___  
  
## 2. Extension for EBU-LMStudio
#### (https://github.com/burnsbert/ComfyUI-EBU-LMStudio)  
  
1. ***ta_lmstudio_load_on_run (text2prompt & image2prompt)*** \
Loads the LLM Model in the LM Studio server when you click RUN  
2. ***ta_lmstudio_model_selector (ext2prompt & image2prompt)*** \
Selection field for all models installed in LM Studio. Vision models are marked with (V).  
3. ***ta_ebu_lmstudio_vision_node (image2prompt)*** \
Settings for Image2Prompt Generation
  
_These are extensions for the EBU-LMStudio custom node. The ComfyUI-EBU-LMStudio node must be installed on your system._

![LM Studio Load On Run](images/TA_LMStudio_Load_(On_Run).png) ![LM Studio Vision Node](images/TA_EBU_LMStudio_Vision_Node.png)

___ 

## 3. Filename Generator
The TAFilenameGenerator is a utility node for ComfyUI designed to automatically generate complex and organized file paths for saving images.

It outputs two separate strings:  
filename: The complete path and name for the main generated image.  
filename_up: A corresponding path and name for an upscaled version (it adds a suffix like "UPSCALED").

_Key Features_  
Dynamic Folders: It allows you to specify a main output_folder and a subfolder.

Date Parsing: The subfolder field can parse date/time codes (e.g., an input of %Y-%m-%d will be converted to a folder named 2025-11-13).  
Custom Naming: It builds the filename by combining several user-defined widgets:

name_prefix (e.g., "TA")  
wf_version (e.g., "v2.50")  
The model_name (from its input)  
A date_format (selected from a dropdown list)  
A delimiter (e.g., "-")

Ready to Use: The final strings (like TA-Outputs\2025-11-13\TA-v2.50-Modelname-202511132027.png) are passed to a SaveImage node, which will automatically create the directories and save the image.

![TA Filename Generator](images/TA_Filename_Generator.png)

---

## 4. Prompt Controller
TA Prompt Controller (Switch) A custom node for ComfyUI designed to manage and route text inputs within a workflow. It serves as a central control unit to switch between manual text input and generated text (e.g., from LLMs or Vision models).

Key Features:  
    - Dual Input: Accepts both a manual text string and a generated prompt string.  
    - Mode Switching: Offers five modes to control the output:  
      1. Manual Only: Passes through the user's manual text, ignoring generated input.  
      2. Generated Only: Passes through the generated text (e.g., from LM Studio), ignoring manual input.  
      3. Combine: Manual + Generated: Prepends the manual text to the generated text.  
      4. Combine: Generated + Manual: Appends the manual text to the generated text.  
      5. Clear / Empty: Outputs an empty string (acts as a reset/mute).  
    - Custom Delimiter: Allows defining a separator (e.g., , ) for combining modes.

Use Case: Ideal for workflows that alternate between Text-to-Image (manual prompting), Image-to-Prompt (vision analysis), and Text-Expansion (LLM enhancement) without needing to rewire nodes.

---

## 5. Directory Captioning
The `TA Directory Captioning` node is a powerful tool for batch-processing images in your workflow.  
  
  **Functionality:**

1.  **LM Studio Integration:** Connects seamlessly to a local LM Studio server, utilizing a user-selected Vision Language Model (VLM) for multimodal processing.
2.  **Batch Captioning:** Takes a specified folder path, iterates through all image files (`.png`, `.jpg`, etc.) within it, and sends each image to the VLM.
3.  **English Output Focus:** Generates detailed, descriptive captions specifically tailored for use as prompts in English, ensuring high quality for subsequent text-to-image generation.
4.  **Automatic Saving:** Saves the generated caption for each image as a corresponding `.txt` file in the same directory, enabling easy integration with datasets and other workflow steps.  
  
  ![TA Directory Captioning](images/ta_directory_captioning_node.png)

---

## 6. TA Save Image & Prompt TXT
  
  **Functionality:**

1.  The `TA Save Image & Prompt TXT` node is a node that can save an additional .txt file in your output-directory with the used positive and negative prompt inside. You can switch this functionality on or off.

![TA Save Image & Prompt TXT](images/ta_save_image_with_prompt-1.png)  

![TA Save Image & Prompt TXT](images/ta_save_image_with_prompt-2.png) 


---
## v1.0.17 (2026-02-15)  
1. TA Save Image & Prompt TXT Node: Added an image output.
---
## v1.0.16 (2025-12-18)  
1. TA Save Image & Prompt TXT Node: I fixed a bug that prevented the workflow data from being saved correctly in the .png file.
---
## v1.0.15 (2025-12-18)  
1. changed TA Save Image & Prompt TXT Node (it can save now the positive and negative prompt)
---
## v1.0.14 (2025-12-17)  
1. added TA Save Image & Prompt TXT Node  

---
## v1.0.13 (2025-12-12)  
1. added TA Directory Captioning Node

---
## v1.0.10-v1.0.12 (2025-11-25)  
1. increased max. possible max_tokens
2. increased max. possible context_lenght
3. increased max. possible wait_time

---
## v1.0.9 (2025-11-25)  

1. added ***ta_prompt_controller***, a node designed to manage and route text inputs within a workflow.
---
## v1.0.6 (2025-11-13)

1. added ***ta_filename_generator***, a node for creating image output filenames and folders
---
## v1.0.5 (2025-11-01)

1. added ***ta_lmstudio_smart_loader***, a simple and fast loader for LM Studio Models
2. changed ***ta_lmstudio_load_on_run*** for more control if needed

![LM Studio Smart Loader](images/TA_LMStudion_Smart_Loader.png) ![LM Studio Load On Run](images/TA_LMStudio_Load_(On_Run)_new.png)
![LM Studio Load On Run](images/TA_LMStudio_Load_(On_Run)_new2.png)
