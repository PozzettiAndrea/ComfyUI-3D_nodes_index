<div align="center">

## The patch file needs to be used with ComfyUI-ZML-Image. 

# [Click here to download](https://github.com/zml-w/ComfyUI-ZML-Image)

</div>

# ZZZ_ZML_English_Patch
- ### ComfyUI-ZML-Image English translation patch

- ### The documentation was translated by AI.

- ### Simply place the patch file in the same directory to use it!

- ### The name must remain "ZZZ_ZML_English_Patch"!

- ### Except for the drop-down options and the nodes with UI interfaces written in JS, everything else has been translated normally!

<img width="807" height="77" alt="屏幕截图 2025-09-03 124948" src="https://github.com/user-attachments/assets/5ff21b5f-12f5-4946-bc57-a97922dd2374" />

# 💕 Brief Introduction to the Nodes:
**This is a feature-rich COMFYUI custom node pack, mainly related to “Image, Text, Integer, LoRA Loader, Mask”, along with some miscellaneous small tools. Currently, there are 70+ nodes in total.**

`I developed these according to my own needs.`

`Some nodes have a “help” output interface, which contains detailed introductions of the nodes. If a node does not have help and you don’t know how to use it, you can check the previous version update notes.`

`All node names start with “ZML_” and are all placed under the “Image/ZML_Image” category.`

<details>
<summary>Click here to view Image Node introduction</summary>

> ### Initially designed for easy management of images and prompts, saving prompts as PNG text chunks within the images:
> <img width="1632" height="875" alt="1_1" src="https://github.com/user-attachments/assets/b23e248e-dc40-4000-9cb7-0f77dd448350" />
>
> ### For even more convenient management, I also created a visual UI:
> <img width="1739" height="877" alt="1_15" src="https://github.com/user-attachments/assets/14957496-ca5e-406d-8c07-e944371c98f3" />
>
> ### Text chunks can be edited in real-time:
> <img width="1796" height="889" alt="1_16" src="https://github.com/user-attachments/assets/49a5645c-61d7-4f90-88c4-bf137a63a808" />
>
> ### And then output:
> <img width="1413" height="617" alt="1_6" src="https://github.com/user-attachments/assets/9c805e33-40dc-468d-a4a1-6bd8df9ff7ee" />
>
> ### The "Load Image from Path" node can randomize images and text chunks. The "Load Image" node can output an alpha channel and text chunks; no images are provided for these.

> ### Next are other image nodes, such as visual image cropping:
> <img width="982" height="893" alt="1_2" src="https://github.com/user-attachments/assets/3bbf3bb4-9c4e-4d9a-bf0b-6a415d0eea7b" />
> <img width="1254" height="753" alt="1_3" src="https://github.com/user-attachments/assets/9c7d6257-9f81-4d61-9fde-1b606cc6a0ef" />
>
> ### Visual image merging:
> <img width="911" height="894" alt="1_4" src="https://github.com/user-attachments/assets/e79c6d57-1714-4347-8559-082a191ddf1c" />
> <img width="1290" height="760" alt="1_5" src="https://github.com/user-attachments/assets/8af17c60-e8e6-4758-a81a-415f37a71cf6" />
>
> ### Painting:
> <img width="1048" height="925" alt="1_8" src="https://github.com/user-attachments/assets/0b60dbbb-bf59-4fea-b93f-fc5470e6db2b" />

</details>

<details>
<summary>Click here to view LoRA Node introduction</summary>

> ### Due to the large number of features, I won't go into detail. The images should give you a general idea.
>
> ### However, there's one feature I really want to tell you about! The nodes can be used with Nunchuck!! Use the functions of the powerful LoRA node to manage your LoRAs, then connect the loaded LoRA list to the dedicated loading node I made for Nunchuck, and you can use Nunchuck with the powerful features of the LoRA Loader!!
>
> ### Give your LoRA a custom text or trigger word template, and you can quickly switch functions with a single click! One-click 3D, one-click realistic! One-click figure! One-click TY...
> <img width="1559" height="748" alt="1_13" src="https://github.com/user-attachments/assets/a8d2cc89-6572-4686-85b6-94b57e1cec96" />
>
> ### Visually manage your LoRAs with the UI:
> <img width="1069" height="826" alt="1_9" src="https://github.com/user-attachments/assets/379631be-4fbc-43c3-93a9-21c2c3e4ac23" />
>
> ### Preview MP4!
> https://github.com/user-attachments/assets/14200a30-581d-4fd1-9dfc-f145f91aa593
>
> ### Real-time changes to trigger words and LoRA descriptions:
> <img width="1103" height="759" alt="356" src="https://github.com/user-attachments/assets/65a3e0b3-04df-46e3-afa9-a2ff173ba6d5" />
>

</details>

<details>
<summary>Click here to view Other Node introductions</summary>

> ### Desktop Pet! Chat! Entertainment! NSFW...
> <img width="1356" height="865" alt="1_7" src="https://github.com/user-attachments/assets/5aa82821-520e-4d8e-9e55-44af75f40412" />
>
> ### Generating text images and adding text to images:
> <img width="1582" height="843" alt="1_11" src="https://github.com/user-attachments/assets/97caad3f-ac3d-44a8-acaf-b0719a65fc79" />
>
> ### Feature-rich text nodes, no detailed introduction needed; see the images:
> <img width="1662" height="869" alt="1_14" src="https://github.com/user-attachments/assets/bf64f1bb-c476-403c-a01e-eb649bcfde8c" />
>
> ### Multiple mask nodes created for multi-person images:
> <img width="1225" height="743" alt="1_10" src="https://github.com/user-attachments/assets/e8a3dfd8-9d76-4f16-b47b-d5b8e177eb30" />
>
> #### There are many nodes and they are updated quickly, so they won't all be introduced here. You can check the version update descriptions! Every new node will have an introduction.

</details>

## ✨ Version Update Notes

> ### Latest Update Date: **2025.09.21**
>

> - #### Fixed a bug where the brush display in the Drawing node was abnormal after zooming, and added a default image for the Drawing node.
>
> - #### The UI for preset text in the Text Selection V3 node now supports storing text in folders.
>
> - #### The Text to Format node now includes a "Comma Append Newline" option.
>
> - #### Added a new "Color to Mask" node.

<details>

> ### Update Date: **2025.09.18**
>

> - #### Added a "Merge Same Prompts" node, which can combine identical prompts into one.
>
> - #### Added an "Append Prompt" node. After detecting keywords, you can choose to Append/Replace a pre-set prompt, or perform a full replacement.
>
> - #### Removed the Text Block Loader node.
>
> - #### Fully optimized the Tagged Image Selection node. It now offers two sorting modes (descending or ascending by name) and has added buttons for quickly reaching the top or bottom. The functionality of the Text Block Loader node has been merged into the Tagged Image node.
>
> - #### Fixed a bug in the Drawing node.
>
> - #### The Powerful LoRA Loader node now supports searching for LoRA names.
>
> - #### Optimized the functionality of the Text Selection V3 node.
>
> - #### Optimized the user experience of the Visual Color Adjustment node.
>
> - #### Optimized the functionality of the Preset Resolution node.

> ### Update Date: **2025.09.13**
>

> - #### Added Integer-String Conversion nodes.
>
> - #### Added a Transition Animation node, to generate animations transitioning from image A to image B.
>
> - #### Fully optimized the Tagged Image Selection node. It can now randomly select images and includes a new "Medium Icon" mode, making it easier to observe image differences. It can also output folder paths to the "Load Image from Path" node for parallel random selection. When the "Remember Open Location" button is enabled, it outputs the path of the open location; when disabled, it outputs the address bar path.
>
> - #### The UI for the Text Block Extractor node has been removed and now reuses the UI of the Tagged Image Selection node. Unlike the Tagged Image Selection node, it doesn't display path indexes, but directly extracts and displays text blocks within the node frame. This allows for modifications to prompts without altering the text blocks within the image.
>
> - #### Added a Visual Color Adjustment node, supporting various parameters such as "Brightness, Contrast, Noise, Vignette..." and many more not listed individually.
>
> - #### Various other minor optimizations will not be detailed at this time.


> ### Update Date: **2025.09.10**
>
> #### This is a significant update.

> - #### Added a new Multi-Text Input_Five V2 node, for use with text images.
>
> - #### Changed the dependency file paths for Merge, Crop, and Draw nodes to dynamic loading. This resolves issues where nodes became unusable due to filenames ending with "main".
>
> - #### Added a new Cylindrical Projection node.
>
> - #### Added a new Panorama Preview node, for VR previewing your images. Can be used with a Kontexet LoRA. Currently still in testing; released early because someone just reported a bug in the previous version, and I didn't want to meticulously troubleshoot it, so I released my current working version directly.
>
> - #### The LoRA name list output type for the Powerful LoRA Loader node has been changed to a string, meaning it can now be saved into a text block! Save all LoRA and artist strings within a single image, then simply load that image when you want to use them. This method also prevents your artist strings and LoRAs from being displayed in the workflow, so even if you send the original image, your art style won't be revealed! To support this feature, I've also added a Text Classification node, allowing you to set specific delimiters to separate LoRAs and prompts in the text block, and then use the Text Split node to break them apart. An example workflow has been uploaded!
>
> - #### Major update to the Text Image node! Now supports image input. When an image is input, the node will automatically stitch the text image onto the input image, useful for adding annotations and creating comparison images. Supports batch loading of images! When loading multiple batches of images, it will automatically sort them and calculate font size and text image resolution. If you want to specify the starting sort number, step, prefix, and suffix, simply use the syntax "#x:x#", where x is a number. For example, entering "ZML_#0:0.5#W" will result in the first image's sequence number being "ZML_0_W", the second "ZML_0.5_W", and so on! To complement this node, I've also optimized the Unified Resolution node for easier combined use!

> ### Updated: **2025.09.06**
>
> - #### Optimized the UI of the powerful LoRA Loader node, making it more comfortable to use! Multiple color theme options have also been added!
>
> - #### Optimized all text nodes! They now all support line breaks! And I've changed the default delimiter to ",\n\n" for all of them, making the prompt structure much clearer and more visible!
>
> - #### The Text Selector V3 node now includes a preset text button, allowing you to add presets to the text box with a single click!
>
> - #### Added a new "Load LoRA by Name (nunchaku)" node. Yes, it's adapted for nunchaku, allowing for more convenient use of nunchaku by combining the "Powerful LoRA Loader" node with "Load LoRA by Name (nunchaku)"!
>

> ### Update Date: **2025.09.04**

> - #### The Tagged Image Selection Node can now remember the last opened location, so you no longer have to search for subfolders every time you open it.
>
> - #### Removed the regular LORA loading node.
>
> - #### When parsing LORA metadata and fetching C-site information for powerful LORAs, if a "wan" LORA is encountered, both the MP4 and the initial frame will now be saved simultaneously.
> 
> - #### The powerful LORA Loader node, and the batch add LORA page, now support MP4 playback!!
>
> - #### There are also some minor optimizations, which won't be detailed here.

> ### Update Date: **2025.09.03**
>
> - #### Fixed a minor bug in the Random Text Weight node.
>
> - #### Fixed a bug where the Save Image node could not preview images.
>
> - #### Added diagonal mask support to the Mask Split node.
> 
> - #### Removed the GIF File Path node and added a Load Video from Path node, which also supports loading GIFs.
>
> - #### Optimized the Text Format Conversion node. Now, in addition to converting NAI weights to SD, it also supports clearing all weights in one click (both NAI and SD). It also supports appending spaces after commas in prompts. Removed help text (punctuation normalization replaces non-standard commas, periods, and the “BREAK” syntax with SDXL-compatible syntax).
>
> - #### Added the Limit Image Ratio node, which can pad or crop images to a specified ratio. Later, you can use the Limit Solid Background node to remove the padding background.
>
> - #### Optimized the Powerful LoRA Loader node, mainly its UI for batch loading LoRAs.
>
>   * In addition to square previews, it now supports vertical and horizontal previews.
>   * You can view and edit txt and log files (trigger words and descriptions) in real-time, and also delete LoRAs and related files with one click. Deleted LoRAs will be labeled “Deleted” to prevent incorrect loading.
>

<summary>Click to view more past updates</summary>

> ### Update Date: **2025.09.02**
>
> - #### Fixed an issue where the Powerful LoRA node could not be used due to a missing punctuation mark.
>   
> - #### Added the Limit Mask Shape node.
>   
> - #### Fixed a bug where the Desktop Pet could not load properly.
>   
> - #### Optimized the Tagged Prompt Loader.
>   
> - #### The Drawing node added several preset colors and optimized UI and usability.
>   
> - #### Optimized the Tagged Image Loader node.
>

> ### Update Date: **2025.08.27**
>
> - #### Fixed a bug in the Powerful LoRA Loader code that caused UI issues in ComfyUI settings page.
>   
> - #### Fixed an issue where the Auto-Censor node sometimes could not read the YOLO model.
>   
> - #### Added a YOLO-to-Mask node.
>   
> - #### Optimized Preset Resolution and Preset Text nodes.
>   
> - #### Added a Mask Separation node, which can split one mask into two or three masks (useful for conditional partitioning, e.g., YOLO auto-detection for face retouching).
>   
> - #### Added a Unified Image Resolution node.
>   
> - #### Desktop Pet now supports chatting! Right-click to select Chat Mode and enter your Google API key in settings.
>   
>   * Added feeding function! Buy food in the store and feed the little sister! With subtitles and sound effects!
>     
>   * Added a countdown timer function.
>     
>   * You can replace Desktop Pet’s assets (sound effects/images) by replacing files in `ComfyUI-ZML-Image\zml_w\web\images`.
>     
>   * If you don’t like Desktop Pet, right-click to hide it or delete `ComfyUI-ZML-Image\zml_w\web\js\zml_floating_ball.js`.
>     

> ### Update Date: **2025.08.27**
>
> - #### Optimized Mask Split node.
>   
> - #### Major update to the Drawing node: now supports drawing on input images, drawing mosaics, and simple shapes (“Square, Triangle, Circle, Heart, Pentagon, Arrow”).
>   
> - #### Added Image Deformation node (simulates liquify/warp in Photoshop, transparency not supported yet).
>   
> - #### Custom text input boxes in Select Text V3 and Powerful LoRA Loader nodes changed to read-only. Click to open popup window for easier editing.
>   
> - #### Fixed a bug where Powerful LoRA Loader node required a CLIP connection. Now it’s optional.
>   
> - #### Added a popup window in Powerful LoRA Loader node for batch adding LoRAs, with one-click LoRA info fetching. Buttons now have CSS visual feedback.
>   
> - #### Added Categorize Images node, which classifies images into “No Metadata, With Metadata, With Text Blocks”. Example workflow uploaded.
>   
> - #### Added Name-Based LoRA Loader node. Powerful LoRA Loader now outputs loaded LoRA names/weights, which can be passed to the Name-Based LoRA Loader node to affect multiple nodes simultaneously. Example workflow uploaded.
>   

> ### Update Date: **2025.08.22**
>
> - #### All inputs of Powerful LoRA Loader node are now optional.
>   
> - #### Fixed all UI bugs of Powerful LoRA Loader and Select Text V3 nodes!!
>   

> ### Update Date: **2025.08.19**
>
> - #### Fixed some bugs and optimized functions in Tagged Prompt node.
>   
> - #### Text-to-Image and Text Watermark nodes now support transparency in all modes (not just fullscreen).
>   
> - #### Added folder support to Powerful LoRA Loader node. You can now organize LoRAs in folders. Only empty folders can be deleted. Folder styles are customizable.
>   
> - #### Since LoRA nodes have folder support, Select Text V3 also got it!
>

> ### Update Date: **2025.08.16**
>
> ### Major Update!!
> 
> - #### Text Line node can now randomize multiple lines at once.
>   
> - #### LoRA Parsing node now supports tree-folder structures.
> - #### Added Select Text V3 node: add new text boxes dynamically, each with toggle/delete buttons and custom names. Outputs combined active texts.
>   
> - #### Added Powerful LoRA Loader node (inspired by RG).
>   
>   * Features: tree-folder LoRA structure, hover image preview, outputs preset txt prompts. Dynamically add LoRAs like RG’s loader. Supports naming/custom text stored in workflow.
>     
>   * Resizable UI. Supports quick toggle/delete, draggable with lock option.
>     
>   * Known bug: After refreshing, node resets visually but data remains intact. Clicking refresh updates restores it.
>

> ### Update Date: **2025.08.14**
> 
> - #### Added “Other” category.
>   
> - #### Added Rotate Image node.
>   
> - #### Added Bridge Preview Image node.
>   
> - #### Merge Image node now supports adjusting foreground opacity.
>   
> - #### Desktop Pet saves last position.
>   
> - #### Random Text Weight node added text box.
>   
> - #### Text Watermark/Text Image nodes now support outline. Empty color = transparent, “ZML” = random color. Transparent watermarks don’t affect visibility and are harder to remove.
>

> ### Update Date: **2025.08.11**
> 
> - #### Updated Drawing node.
>   

> ### Update Date: **2025.08.08**
> 
> - #### Added Tagged Prompt Loader node (similar to old Weilin). Rewritten in JS. Supports batch txt import (format “Chinese,English”). Semi-finished.
>

> ### Update Date: **2025.08.07**
> 
> - #### Added Floating Ball!! Interactive! Default = PNG, Running = GIF, Double-click changes image and plays sound. Hover = breathing effect. Right-click = settings. Entertainment-only feature (customizable via replacing files).
>   
> - #### Added Simple Save Image node (clean UI, only 3 options: mode, path, store text).
>   
> - #### Fixed small bugs and optimizations.
>

> ### Update Date: **2025.08.06**
> 
> - #### Another major update!!
> 
> - #### Added Tagged Image Loader node (UI inspired by Weilin). Supports batch load + text block reading. Hover preview supported.
>   
> - #### Added Single Text Block Loader node.
> 
> - #### Added Audio Player node (with built-in audio).
>   
> - #### Removed LoRA Layer Control node.
>   
> - #### Optimized several nodes.
>   

> ### Update Date: **2025.08.03**
> 
> - #### Manager installation should work now. Bug fixed.
>   
> - #### Added Double Float node.
>   
> - #### Added Preset Resolution node (similar to Preset Text).
>   
> - #### Added Double Integer V3 (judgment node): compares input width/height, outputs preset resolution accordingly. Made for wan2.1 video generation.
>   
> - #### Added LoRA Metadata Parser node: auto-generates txt, log, and preview image in “zml” folder when loading LoRA.
>   
> - #### Visual Crop node now supports output at original resolution.
>   

> **Below are earlier node introductions:**
>
> 0. Enhanced Save Image node: adds support for saving text blocks into metadata, customizable naming, scaling, stripping workflow metadata.  
> 1. Enhanced Load Image node: loads single frame (even GIFs), supports transparency, reads filename/metadata.  
> 2. Load Image from Path node: supports fixed/sequential/random index loading.  
> 3. Image/GIF-to-HTML node: hides content until downloaded and opened locally.  
> 4. NAI-to-SD weight conversion node: supports tag filtering, punctuation normalization, and character removal.  
> 5. Random Text Line & Random Artist nodes: supports custom count/weights. Built-in txt of 1000 artists.  
> 6. Multiple text input/selection nodes: pre-store prompts and enable selectively.  
> 7. Resolution Limiter node: standardizes resolutions for generation or wan video frames.  
> 8. Auto-Censor node using YOLO or manual mask.  
> 9. Text Watermark node: auto line-breaks, full-screen watermarks, commercial fonts.  
> 10. Random/Predefined Integer nodes for random resolution switching.  
> 11. Based on LoRA Loader (pysss) from [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts). Supports preview, categorization, metadata linking (txt/log/image).  
> 12. Visual Crop node: manual cropping (rect/circle/path/brush).  
> 13. Limit Solid Background node: auto-remove extra pixels (supports white/green/transparent).  
> 14. Add Solid Background node: outlines subject with customizable colors.  
> 15. Merge Image node: combine 2–4 images via interactive UI. Saves internal edits. Can be used for censoring.  
> 16. Drawing node: freehand paint on images.  
> 17. Image Pause node: pauses 15s, allows output channel selection. Optimized to avoid saving placeholder images.  

</details>

## ✨ Node Update Image Showcase

<details>
<summary>Click to view updated node images</summary>

> ### Update Date： **2025.09.18**

> <img width="1416" height="735" alt="屏幕截图 2025-09-17 171252" src="https://github.com/user-attachments/assets/aa6bfc94-6970-41b4-a177-a2815f0d0eab" />
> <img width="1314" height="604" alt="屏幕截图 2025-09-17 171409" src="https://github.com/user-attachments/assets/e655ee31-e87d-4159-90b9-e61eb5df086a" />
> <img width="1850" height="922" alt="屏幕截图 2025-09-17 171441" src="https://github.com/user-attachments/assets/47520ee9-0fc6-4409-ba69-38f8271b562f" />
> <img width="1030" height="882" alt="屏幕截图 2025-09-17 171304" src="https://github.com/user-attachments/assets/508ee11d-6491-4f0e-9db0-653fd43b1c34" />
> <img width="567" height="623" alt="屏幕截图 2025-09-17 171416" src="https://github.com/user-attachments/assets/5ef10471-affc-4ec2-bf51-ee6ccc39357d" />

> ### Update Date： **2025.09.13**

> <img width="868" height="875" alt="1" src="https://github.com/user-attachments/assets/31466b9e-e28b-42b4-87e1-2e3c53986620" />
> 
> <img width="1762" height="880" alt="2" src="https://github.com/user-attachments/assets/f03631ce-dddc-4aa9-b0ef-13a3b004a4e0" />
> 
> <img width="1373" height="526" alt="3" src="https://github.com/user-attachments/assets/e709c63b-a835-4805-b264-3a554e3c2bd4" />
>
> https://github.com/user-attachments/assets/ffd4a564-1659-4322-92ae-f47234c06702

> ### Update Date： **2025.09.06**

> <img width="1408" height="669" alt="屏幕截图 2025-09-09 013650" src="https://github.com/user-attachments/assets/4286f7b9-19fd-400e-8c98-16732a82815f" />
>
> ![5F46A8F3AA5F87588473C0F74707C213](https://github.com/user-attachments/assets/1452355a-ea95-4718-a835-bde0e791f379)
> 

> ### Update Date： **2025.09.06**

><img width="1687" height="786" alt="4" src="https://github.com/user-attachments/assets/151b4379-c9ce-4339-b512-c8aaf313d6a0" />
>
> <img width="1154" height="839" alt="1" src="https://github.com/user-attachments/assets/b8229940-2363-4d93-8c21-9185bdb4efd1" />
> 
> <img width="1204" height="664" alt="2" src="https://github.com/user-attachments/assets/7561e40b-4461-4a44-a70b-0dfb27c6d290" />
> 
> <img width="986" height="830" alt="3" src="https://github.com/user-attachments/assets/3f5dc8a2-5183-4cee-96e7-8b39ce197b3e" />
> 


> ### Update Date: **2025.09.03**
>
> <img width="896" height="429" alt="1" src="https://github.com/user-attachments/assets/16d79123-9689-476d-a1cf-65431ba03dd0" />
> 
> <img width="909" height="778" alt="2" src="https://github.com/user-attachments/assets/eb20dc55-62e8-499b-bb8c-70f0158397c0" />
> 
> <img width="1103" height="759" alt="3" src="https://github.com/user-attachments/assets/3fdbb9d7-276a-468d-ab4b-b52b334346fd" />
>

> ### Update Date: **2025.09.02**
> 
> <img width="1782" height="869" alt="2" src="https://github.com/user-attachments/assets/54bd9449-4034-4b1b-abdc-87dfefb1a3c4" />
> 
> <img width="1048" height="925" alt="4" src="https://github.com/user-attachments/assets/1607ebfc-0e33-4818-9845-9aa366a19ee1" />
> 
> <img width="1722" height="912" alt="3" src="https://github.com/user-attachments/assets/1ff2e9ce-0d44-473d-bf42-2c9b14366265" />
> 
> <img width="1356" height="865" alt="1" src="https://github.com/user-attachments/assets/e4b1370b-130a-419c-b0c4-d94ada5283df" />
>

> #### Early node screenshots (a small portion)
>
> <img width="1632" height="875" alt="1" src="https://github.com/user-attachments/assets/77ccda88-1851-4948-a45b-2f42b46d7f53" />
>
> <img width="1601" height="784" alt="2" src="https://github.com/user-attachments/assets/21f9d0aa-834e-48dd-9384-584e0a215284" />
>
> <img width="1210" height="913" alt="3" src="https://github.com/user-attachments/assets/3359a2fd-a55a-4068-aa25-0338298b7c0b" />
>
> <img width="1698" height="862" alt="4" src="https://github.com/user-attachments/assets/059746d8-31e0-4c97-a620-6e490a6a79b4" />
> 
> <img width="1607" height="755" alt="5" src="https://github.com/user-attachments/assets/8fe91394-8874-4eb4-85dc-d7f8ce6a86da" />
>
> <img width="1719" height="745" alt="6" src="https://github.com/user-attachments/assets/2eee7e21-52a0-4d6a-bd9f-8edd52e84eff" />
>
> <img width="1261" height="762" alt="7" src="https://github.com/user-attachments/assets/a1e67136-0ed7-4664-8f3a-3de69282f71b" />
>
> <img width="982" height="893" alt="8" src="https://github.com/user-attachments/assets/dd905d68-138d-4c30-a0e2-dbdb206c11e9" />
>
> <img width="1254" height="753" alt="9" src="https://github.com/user-attachments/assets/14e6f8df-8b36-4d06-a827-8bbdef1b0e8f" />
>
> <img width="1389" height="683" alt="10" src="https://github.com/user-attachments/assets/0757a6e3-d557-4284-ad56-dcc0e004b41c" />
>
> <img width="1294" height="816" alt="11" src="https://github.com/user-attachments/assets/de9b70a5-03b0-426a-90fc-bf1d8295abf2" />
>
> <img width="1131" height="712" alt="12" src="https://github.com/user-attachments/assets/c0d253aa-96c2-4a9e-b64f-682f3908fa2e" />
>
> <img width="1196" height="639" alt="13" src="https://github.com/user-attachments/assets/c1793444-d44f-47cd-89a4-67c408cde01e" />
>
> <img width="911" height="894" alt="14" src="https://github.com/user-attachments/assets/4f666b73-f968-4182-a327-e29187ddf202" />
>
> <img width="1290" height="760" alt="15" src="https://github.com/user-attachments/assets/5a520228-fe42-49c9-a43d-e545474254f4" />
>

</details>

## ✨ Video Introduction: [Click to Visit](https://www.bilibili.com/video/BV1i4twzDELr/?spm_id_from=333.1007.0.0&vd_source=0134812498ce59b7f53810ad84889d12)

`Less introduction, no updated video, Only the Chinese language`

### Auxiliary Script Repository:

`Here are some small tools I made. Some are to assist with node usage, others are extracted node functions.`

`The scripts run independently, not within ComfyUI.`

- **https://github.com/zml-w/ZML-Image-Script/tree/main**
  

## Some Nodes and Functions Were Inspired by Others

### Referenced Code:

- **LoRA Load Node: https://github.com/pythongosssss/ComfyUI-Custom-Scripts**

### Referenced Inspirations:

- **Desktop Pet: https://github.com/11dogzi/Comfyui-ergouzi-kaiguan**

- **Tagged Prompts: https://github.com/weilin9999/WeiLin-ComfyUI-prompt-all-in-one**

- **Bridge Preview Image: https://github.com/ltdrdata/ComfyUI-Impact-Pack**

- **Powerful LoRA Loader: https://github.com/rgthree/rgthree-comfy**

## You Can Submit Issues or Ideas

`Little sister is so cute, here’s a little sister pic`

<img width="1024" height="540" alt="妹相随_6" src="https://github.com/user-attachments/assets/bc18deae-6c3c-4e70-a642-1b4210accdc3" />
