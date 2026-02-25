# ComfyUI EasyFilePaths 
 
A curated collection of nodes covering file selection, loaders, JSON automation, image helpers, and workflow utilities. 
 
## Installation 
1. Copy this folder into ComfyUI/custom_nodes. 
2. Restart or refresh ComfyUI so the nodes register. 
 
## Configuration 
- configs/storylist_config.json: base_folder and story_pattern drive Easy File Name dropdowns. 
- users.json: defines the chooser list used by Easy File Name and User Select. 
- configs/character_config.json: maps characters to LoRA hints and prompts. 
- configs/action_config.json: WAN, Chroma, and QWEN actions for the action selectors. 
 
## Node catalog 
### File helpers 
- Easy File Name, User Select, Easy GetLine, Image Save To Path. 
### Image loaders and processors 
- Load Images From Directory Path, Load Image From Path, Load Random Image From Folder Path, Load Image From Match, Easy Image Failsafe/Base64/URL loaders, Easy Image Bloom Filter, Easy Filmgrain, Easy Grow Mask And Blur, Easy Gamma, Easy Image Compare. 
### JSON and control nodes 
- Easy JSON Job Import/Update, Easy JSON Extractor, Easy Basic Json Extractor, Easy JSON Saver, Easy Array Filter, Line Counter, Easy Compare, Easy Math. 
### Loaders and model helpers 
- Easy Lora/UNET/Checkpoint/CLIP/VAE loaders, Easy Depth Anything V2, Easy Color Nodes, Easy Resize, Easy DType, Easy Latent Clamp, Easy Stability Utilities, Easy Wardrobe. 
### Workflow utilities 
- Dynamic Bypass Controller/Selector, Easy Smart Bypass, General Switch, Latent Switch, Remove Noise Mask, stability helpers. 
### Detection and segmentation 
- Easy YOLOv8 nodes, Fresh YOLO Segmentation, Easy Ultralytics Detector Provider. 
 
## Notes 
- Ultralytics detectors require ultralytics, torch, and opencv-python, and print guidance if dependencies fail. 
- Loader nodes reuse the Impact Pack folder_paths registry, so adding new model folders is enough for discovery. 
- Delete and re-add nodes after editing JSON configs to refresh dropdowns without restarting.
