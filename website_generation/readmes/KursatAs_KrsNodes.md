# **Comfyui Krs Nodes**

This repository contains a collection of custom nodes for ComfyUI. These nodes enhance the functionality of ComfyUI and provide additional features for users.
## **Installation**
To install the Krs nodes for ComfyUI, follow these steps:
1. Clone or download this repository.
2. Copy the contents of the repository into the `custom_nodes` directory of your ComfyUI installation.
3. Restart ComfyUI to load the new nodes.
## **Available Nodes**
- **TextEncodeQwenImageEditKrsSimple**: The idea behind this node is to provide a simple fix for well known Qwen Image Edit Shift "offset" Issue, as additionally to be able to adjust vl resolution for better clarity.


- **TextEncodeQwenImageEditKrsAdvanced**: Same as TextEncodeQwenImageEditKrsSimple with additional outputs for extra images and latent for more advanced workflows.


- **QwenImageEditLatentKrs**: Latent creation with extra controls for Qwen Image Edit to feed samplers. Still experimental.


- **CropPadAdvancedKrs**: Advanced Crop and Pad node with additional controls for precise image manipulation, ideal for outpainting operations.

![nodes.jpg](images/nodes.jpg)

![nodes2.jpg](images/nodes2.jpg)

Reference Photo by <a href="https://unsplash.com/@aminnaderloei?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">amin naderloei</a> on <a href="https://unsplash.com/photos/young-woman-peeking-through-tall-green-reeds-x-aW69vrYvQ?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a> 




## **Usage**
Simple as it gets, just replace your existing TextEncodeQwenImageEdit nodes with these custom nodes. Adjust the vl resolution as needed for your specific use case.

Just make sure to connect the input image directly to the TextEncodeQwenImageEditKrsSimple (or Advanced) node to avoid the offset issue.

Use node output_image (or latent for advanced node) for further processing in your workflow.

Defaults are set to match the original Qwen Image Edit behavior "Aligment= 32, Vl= 384". 1024 vl resolution is recommended for better clarity and identity following.

Generally 512 to 576 vl resolution is a good balance between clarity and prompt adherence.

## ****Limitations:**** 

Higher vl resolution expected to give better clarity and identity following, however higher vl resolutions can lead to lower prompt coherence or ignorance of certain prompt elements.

In such cases two different approach can be followed;
1. Simple way; Try adjusting the vl resolution downwards or experiment with different resolutions to find the optimal balance between clarity and prompt adherence.


2. Advanced way; 

Input Image -> TextEncodeQwenImageEditKrsAdvanced with vl_resolution set to "512", set system prompt to minimum -> Ksampler -> TextEncodeQwenImageEditKrsAdvanced "with vl_resolution set to 512" latent output -> And Then your main -> Ksampler

-Keep the same prompt for both TextEncodeQwenImageEditKrsAdvanced nodes, or advance from first prompt...

-Example prompt for second node: CRITICAL PRESERVATION REQUIREMENTS: Keep the person's head position, angle, and tilt EXACTLY as shown in the input image - same head rotation,   
same neck angle, same face direction, do not change head pose in any way. Preserve ABSOLUTE facial identity - exact same face,   
identical facial features, same eye shape, same eye color, same nose shape, same mouth shape, same facial structure, same skin tone, same hair,   
do not alter the person's face or head position at all. Lock face and head pose completely.

-Same seed for both Ksampler nodes.

-This way you can have both better clarity and prompt adherence, however it will require more VRAM and processing power.

These nodes are designed to work specifically with Qwen Image Edit models and may not be compatible with other models or workflows.

## **Contributing**
If you would like to contribute to this repository, please feel free to submit a pull request or open an issue for any bugs or feature requests.
