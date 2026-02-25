RizzNodes for ComfyUI
Welcome to RizzNodes, a collection of custom nodes for ComfyUI designed to streamline various workflows, from loading images and models in batches to dynamic prompt generation and memory management.

🚀 Installation
Navigate to your custom_nodes directory:

cd ComfyUI/custom_nodes

Clone this repository:

git clone https://github.com/Rizzlord/ComfyUI-RizzNodes.git

Restart ComfyUI:
Your new nodes should now appear in the node selection menu under the "RizzNodes" category.

✨ Nodes Overview
This section provides a detailed look at each node included in the RizzNodes collection.

RizzNodes/Image
Load Latest Image (Rizz)
Loads the numerically highest-indexed image from a specified directory based on a filename base. Useful for continuously processing outputs from other nodes.

Category: Image

Function: load_latest_image

Inputs:

directory (STRING): The directory to search for images. Can be relative to ComfyUI's output directory or an absolute path. Default: ""

filename_base (STRING): The base name of the image files (e.g., "Image" for files like Image_0001.png). Default: "Image"

Outputs:

IMAGE (IMAGE): The loaded image tensor.

MASK (MASK): The alpha channel of the loaded image as a mask.

latest_filename (STRING): The filename of the loaded image.

Batch Image Loader
Iterates through images in a specified directory, loading one image per execution. Supports resetting the index and looping.

Category: Image

Function: load_next_image

Inputs:

directory (STRING): The directory containing the images. Can be relative to ComfyUI's input directory or an absolute path. Default: "input/images"

reset_index (BOOLEAN): A button to reset the current image index to the beginning of the list. Default: False

Outputs:

IMAGE (IMAGE): The current image tensor.

CURRENT_FILENAME (STRING): The filename of the currently loaded image.

CURRENT_INDEX (INT): The index of the currently loaded image in the batch.

TOTAL_IMAGES (INT): The total number of images in the directory.

Batch Upscale Image
Applies an upscale model to a batch of images. Can output images as a batch or concatenated into a single grid.

Category: Image

Function: upscale_batch

Inputs:

images (IMAGE): A batch of image tensors to be upscaled.

upscale_model (UPSCALE_MODEL): The upscale model to use.

output_type (ENUM): How to output the upscaled images (BATCH or CONCATENATED_GRID). Default: "BATCH"

Outputs:

UPSCALE_IMAGES (IMAGE): The upscaled image(s).

RizzNodes/Model
Load Latest Mesh (Rizz)
Loads the numerically highest-indexed GLB mesh from a specified directory based on a filename base.

Category: Model

Function: load_latest_mesh

Inputs:

directory (STRING): The directory to search for mesh files. Can be relative to ComfyUI's output directory or an absolute path. Default: ""

filename_base (STRING): The base name of the mesh files (e.g., "Unrefined" for files like Unrefined_0001.glb). Default: "Unrefined"

Outputs:

MESH (TRIMESH): The loaded mesh object.

latest_filename (STRING): The filename of the loaded mesh.

Batch Model Loader
Iterates through 3D model files (GLB, OBJ, GLTF, STL, PLY) in a specified directory, loading one model per execution. Supports resetting the index and looping.

Category: Model

Function: load_next_model

Inputs:

directory (STRING): The directory containing the 3D models. Can be relative to ComfyUI's input directory or an absolute path. Default: "input/models/glb"

reset_index (BOOLEAN): A button to reset the current model index to the beginning of the list. Default: False

Outputs:

MESH (TRIMESH): The current mesh object.

FULL_PATH_AND_FILENAME (STRING): The full path and filename of the currently loaded model.

CURRENT_INDEX (INT): The index of the currently loaded model in the batch.

TOTAL_MODELS (INT): The total number of models in the directory.

RizzNodes/Prompt
Dynamic Prompt Generator
Generates prompts by dynamically replacing a [subject] placeholder in a base prompt with subjects from a provided list. Iterates through the subject list on each execution.

Category: Prompt

Function: generate_dynamic_prompt

Inputs:

base_prompt (STRING): The base prompt string containing [subject] as a placeholder. Multiline input supported. Default: "digital painting of a game asset concept of a medieval [subject], from a dark fantasy setting, resembling the artstyle of elden ring and dark souls, intecrite highly detailed. The background is beige."

subject_list (STRING): A hyphen-separated list of subjects (e.g., "chair-lamp-torch"). Multiline input supported. Default: "chair-lamp-torch"

reset_index (BOOLEAN): A button to reset the current subject index to the beginning of the list. Default: False

Outputs:

PROMPT (STRING): The generated prompt with the subject inserted.

CURRENT_SUBJECT (STRING): The subject used in the current prompt.

CURRENT_INDEX (INT): The index of the current subject.

TOTAL_SUBJECTS (INT): The total number of subjects in the list.

RizzNodes/Utilities
Memory Cleaner
Triggers a memory cleanup, unloading all models and clearing the cache in ComfyUI. Useful for freeing up VRAM.

Category: Utilities

Function: clean_memory

Inputs:

trigger (ANY): Connect any node to this input to trigger the memory cleanup when it executes.

Outputs:

anything (ANY): Passes the input trigger through, allowing chaining.

Anything Passthrough (Reroute)
A simple passthrough node that accepts any input and returns it. Can be used for rerouting connections or as a placeholder.

Category: Utilities

Function: passthrough

Inputs:

anything (ANY): Any input value.

Outputs:

anything (ANY): The input value passed through.

Feel free to contribute or suggest improvements!
