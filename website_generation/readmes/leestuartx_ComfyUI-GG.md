# ComfyUI-GG

**Developer:** Garner Games

**Version:** 1.1 
**Date:** 7/22/24

ComfyUI-GG is a collection of ComfyUI nodes designed to enhance productivity in image processing workflows. This plugin provides a set of custom nodes that perform various image manipulations and metadata extractions to streamline your tasks.

## Changelog


### Version 1.2 - 7/22/24
- Added a 'for loop' node


Version 1.1 - 7/22/24
- Resolved issues with metadata extractor function.


## Nodes

### 1. Add Padding to Image
**Description:**  
This node adds pixel padding to the image to achieve a specified dimension.

<img src="./img/node_padding.jpg" alt="Node Padding" height="220" style="display:block; " />

**Usage:**  
- Input an image.
- Define the goal dimension.
- The node will add padding to the image to match the specified dimension.

---

### 2. Resize Image Proportionally
**Description:**  
This node resizes an image proportionally based on a user-defined width.

<img src="./img/resize_proportionally.jpg" alt="Node Padding" height="220" style="display:block; " />

**Usage:**  
- Input an image.
- Define the new width.
- The node will resize the image proportionally to match the specified width.

---

### 3. Image Metadata Extractor
**Description:**  
This node loads an image and extracts its metadata, which can be used for additional image processing.

<img src="./img/image_metadata.jpg" alt="Node Padding" height="320" style="display:block; " />

**Usage:**  
- Input an image.
- The node will extract and output the metadata from the image.

---

### 4. Metadata Extract by Seed
**Description:**  
This node iterates through images in a directory using a seed, loads each image, and extracts its metadata. This metadata can be used for upscale/resampling automation.

<img src="./img/extract_by_seed.jpg" alt="Node Padding" height="320" style="display:block; " />

**Usage:**  
- Input a seed value.
- Provide the directory containing the images.
- The node will extract metadata from each image in the directory based on the seed.

---

### 5. For Loop
**Description:**  
This node is used as a for loop, so that a process can be run for a set number of iterations. Contains

<img src="./img/for_loop.jpg" alt="Node Padding" height="320" style="display:block; " />

**Usage:**  
- Input a start and end range.
- The node will run until it reaches the end.
- This node can (for example) be tied into a 'seed' input in order to run a KSampler for a set number of iterations.

---

