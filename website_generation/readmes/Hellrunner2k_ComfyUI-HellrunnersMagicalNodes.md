# Hellrunner's Magical Nodes
Magical nodes that are meant for integration and science of course. ^^ Foundational Helpers and smart Containers that use automated functionalities to make room for creative use. A magical pack-synergy is at hand that does not require much extra clutter to make advanced techniques pop beautifully. The idea was to create universal artist's precision tools that do not care what you throw at them.  
if you enjoy my work and you feel your new found power for the first time, if i have inspired and you make amazing stuff ... click the button ;)

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/M4M2PZ0ZH) 

:D have fun! ^^  
&ndash; Helllrunner

PS: I'm around somewhere. Probably at the Tzatzik Kebaperist.

## Installation
`git clone https://github.com/Hellrunner2k/ComfyUI-HellrunnersMagicalNodes.git` into the `ComfyUI/custom-nodes/` folder.
You know what to do ^^. There might be the possibility to download the Pack in comfy directly, via the comfyUI-Manager, but that can be buggered. ^^ 

# Magical Nodes
![simple](https://raw.githubusercontent.com/Hellrunner2k/References/main/nodes/MagicalNodes.png) 
Main Pack utilizable as Comfy-Flow foundation.
#### Comfy-Flows
-  #### <a href="https://github.com/Hellrunner2k/References/blob/main/comfy-flows/MagicalNodes_Basic.json">Basic Generation</a>
-  #### <a href="https://github.com/Hellrunner2k/References/blob/main/comfy-flows/MagicalNodes_Upscale.json">Load and Upscale</a>
-  #### <a href="https://github.com/Hellrunner2k/References/blob/main/comfy-flows/MagicalNodes_Mask-Maps.json">Basic Mask-Maps</a> (and <a href="https://raw.githubusercontent.com/Hellrunner2k/References/main/comfy-flows/MaskGradB.bmp">Mask-Map</a> used)
Tutorial Videos are coming

## Magical Save Node
![simple](https://raw.githubusercontent.com/Hellrunner2k/References/main/nodes/MagicalSave.png)  
Compiles meta-data based on renamed nodes (right-click -> "Title") and optionally includes it and the comfy-flow in a text file and/or a png image.

### Inputs
Key|Type|Tooltip|Default
|-|-|-|-|
Active|BOOLEAN|Boolean On/Off Switch for better integration in complex comfy-flows|On
Output_Path|STRING|Subfolder Path into "output"|[time(%Y-%m-%d)]
Name | STRING | File Name | ComfyUI
Extension | 'png', 'jpg', 'tiff', 'bmp', 'none' | Image Type | png
Quality | INT | jpg compression 1-100, png compression 0-9  (if > 9 = 0 lossless) | 95
Save_gen_data_to_txt | BOOLEAN | On saves meta-data based on renamed nodes (right-click -> "Title") and the comfy-flow to a text file | On
Save_gen_data_to_png | BOOLEAN | On saves meta-data based on renamed nodes (right-click -> "Title") and the comfy-flow to a png image | Off
Formatting | 'Human Readable' | Meta Data Format. Included for future expandability without node breakage | Human Readable

## Thermal Latenator
![simple](https://raw.githubusercontent.com/Hellrunner2k/References/main/nodes/Latenator.png)  
Latent seed and batch controller with extra information outputs, so it can be used as resolution and seed master.

### Inputs
Key|Type|Tooltip|Default
|-|-|-|-|
Ratio_Selected | List | SDXL Native resolution selection | 1:1 [1024x1024 square]
Width_Override | INT | >0 Overrides Width | 0
Height_Override | INT | >0 Overrides Height | 0
Batch_Count | INT | Number of seeded batches | 1
Batch_Size | INT | Number of batched sub-images | 1
First_Seed | INT:seed | Initial seed | 1
Batch_Seeds | STRING | Seed Override for easy chaining. Can deal with hyphen separation (1234-1235) and line breaks. | -
Reseed_Latents | LATENT | Input latents to be rebatched and reseeded with current seed options | -
### Outputs
Key|Type|Tooltip
|-|-|-|
Latents|LATENT|Latents
Seeds|INT|Batch Seeds
Seed String|STRING|Seed String for easy chaining
Width|INT|Latent Width
Height|INT|Latent Height

## Load Mask-Map
![simple](https://raw.githubusercontent.com/Hellrunner2k/References/main/nodes/Mask-Maps.png)  
Open, optionally scale and split a Mask-Map bmp. Smooth gradient masks with 100% combined prompt coverage. Ready for use in one go. A usage guide can be found <a href="https://civitai.com/articles/5319/hellrunners-mask-maps-attention-masking">here</a>

### Inputs
Key|Type|Tooltip|Default
|-|-|-|-|
image | IMAGE | RGB Mask-Map as bmp | -
Width | INT | Width Override, >0 initializes scaling | 0
Height | INT | Height Override, >0 initializes scaling | 0
upscale_method | Upscale Methods | Upscaling method to use if scaling | lanczos
### Outputs
Key|Type|Tooltip
|-|-|-|
Mask-Map|MASKMAP|Latents
Red|MASK|Red Mask (Center Piece)
Green|MASK|Green Mask (Theme)
Blue|MASK|Blue Mask (Background)

# Mojo
![simple](https://raw.githubusercontent.com/Hellrunner2k/References/main/nodes/Mojo.png)  
Lightweight interflow exchange format geared towards lossless upscaling and refinement. To have generalized, comparable outcomes when model testing, play a game of conditioning-telephone or simply to share your prompt without sharing your prompt. ^^  
Supports 3 full TextEncoder (clip) sources in any combination. I made a .mojo that ran with XL, AuraFlow and Flux. :D

## Mojo Maker
![simple](https://raw.githubusercontent.com/Hellrunner2k/References/main/nodes/MMaker.png)  
Weaves the clips and prompts into a unified Mojo Flow and outputs the Main_clip conditioning. Ensures feature complete usage of common models.

### Inputs
Key|Type|Tooltip|Default
|-|-|-|-|
Main_clip | CLIP | Main Clip source | -
Alternative_clip | CLIP | Alternative Clip source. Enrich the possibilities of your Mojo | -
Special_clip | CLIP | YES... MORE.. more clip... or t5, who knows?! | -
Mojo_Intake | MOJO | Join the incoming Mojo Flow into the output | -
Phrases | IMSTRINGAGE | l,hydit_clip,h - Normal Prompt. Comma separated, short phrases. Object and detail focused. (Local, Character) | -
Tags | STRING | g - Simplified, tag-based prompting. Strong conceptional influence. (General, Action) | -
Sentences | STRING | t5xxl,pile_t5xl,mt5xl - Go nuts. Write an epic novel. But set the mood... the t5s want dinner first. ^^ Might be generalized and reliant on lower clip concepts. | -
Mask_set_cond_area | 'default', 'mask bounds' | Mask area behavior. "default": black pixel = (tag:0) - merges well with other areas  "mask bounds": black pixel = tag removed... off  gone from vocabulary - hard separation | default
Mask_strength | FLOAT | Mask strength. leave at 1.0 if you are using Mask-Maps | 1.0
guidance | FLOAT | Flux specific. Parameter for simulated guidance based on conditioning | 3.5
width | INT | SDXL and Pony specific. Set the current image resolution to match the Mojo perfectly. | 1024
height | INT | SDXL and Pony specific. Set the current image resolution to match the Mojo perfectly. | 1024
crop_w | INT | SDXL and Pony specific. Crop Factor Width | 0
crop_h | INT | SDXL and Pony specific. Crop Factor Height | 0
target_width | INT | SDXL and Pony specific. Set the target image resolution after upscale. | 1024
target_height | INT | SDXL and Pony specific. Set the target image resolution after upscale. | 1024
step_start | FLOAT | Step influence clamp start. Starts at 0-1. <0 Disabled | -1.0
step_end | FLOAT | Step influence clamp end. Ends at 0-1. <0 Disabled | -1.0
Squeeze_Mojo_Intake | 'Disabled', 'Squeeze + Toss' | Merge all Intake Mojo to the smallest possible count. Only maskless Mojo can be squeezed. | Disabled
Intake_Strength | FLOAT | Mixing strength of the squeezed Intake. | 1.0
Conditioning_Output | 'Disabled', 'Mojo', 'Mojo + Intake (Combine)' | How to construct the Conditioning Output. "Mojo + Intake (Combine)" is equivalent to the "Mojo (Combine)" Loader method | Mojo
mask | MASK | Weave a Mask into the Mojo Flow | -
### Outputs
Key|Type|Tooltip
|-|-|-|
Mojo | MOJO | Mojo Flow
Conditioning | CONDITIONING | Main_clip Conditioning, if not "Disabled"

## Save Mojo
![simple](https://raw.githubusercontent.com/Hellrunner2k/References/main/nodes/MSave.png)  
Saves a .mojo file using safetensors with lightweight information, to further refine or recreate an image. Provide various clip sources to make your mojo more versatile.

### Inputs
Key|Type|Tooltip|Default
|-|-|-|-|
Active | BOOLEAN | Boolean On/Off Switch for better integration in complex comfy-flows | On
Output_Path | STRING | Subfolder Path into "output" | Hellkars/Mojos
Name | STRING | Mojo File Name | ShareMy
Override | BOOLEAN | Saves over the exact file name on "True/On" or creates numbered unique files on "False/Off" | On
latent | LATENT | Latents to Mojo file. Provide decoding info. | -
Positive_Mojo | MOJO | Positive Mojo Flow | -
Negative_Mojo | MOJO | Negative Mojo Flow | -
Info | STRING | Extra Mojo information. Provide models used. With what VAE to decode the latent... and such | -

## Mojo Loader
![simple](https://raw.githubusercontent.com/Hellrunner2k/References/main/nodes/MLoad.png)  
Loads a .mojo file for further refinement or recreation of an image. The usage of the content may vary dependent on it's construction.

### Inputs
Key|Type|Tooltip|Default
|-|-|-|-|
Main_clip|CLIP|Main Clip source|-
Output_Path|STRING|Subfolder Path into "output"|Hellkars/Mojos
Name | STRING | Mojo File Name | ShareMy
Clip_Choice | 'Main', 'Additional', 'Special' | Biases the assembly towards a clip source. IF such source is provided. The only mandatory source is Main. Usage is heavily dependent on how the .mojo file was made. | Main
Conditioning_Output | 'Disabled','Mojo (Combine)' | How to construct the Conditioning Output. | Mojo (Combine)
### Outputs
Key|Type|Tooltip
|-|-|-|
Latents|LATENT|Latents
Positive|CONDITIONING|Positive Conditionings, if not "Disabled"
Negative|CONDITIONING|Negative Conditionings, if not "Disabled"
Positive_Mojo|MOJO|Positive Mojo Flow
Negative_Mojo|MOJO|Negative Mojo Flow
Info|STRING|Info String with useful information about the Mojo and it's assembly.
Positive_Masks|MASK|Positive Masks, if provided
Negative_Masks|MASK|Negative Masks, if provided

## Adjust Mojo
![simple](https://raw.githubusercontent.com/Hellrunner2k/References/main/nodes/MAdjust.png)  
Inject new values into a Mojo flow and/or weave in another

### Inputs
Key|Type|Tooltip|Default
|-|-|-|-|
Mojo | MOJO | Mojo Flow | -
Main_clip | CLIP | Main Clip source. Needed if Conditioning is enabled | -
Mojo_Intake | MOJO | Join the incoming Mojo Flow into the output | -
guidance | FLOAT | Flux specific. Parameter for simulated guidance based on conditioning | 3.5
width | INT | SDXL and Pony specific. Set the current image resolution to match the Mojo perfectly | 1024
height | INT | SDXL and Pony specific. Set the current image resolution to match the Mojo perfectly | 1024
crop_w | INT | SDXL and Pony specific. Crop Factor Width | 0
crop_h | INT | SDXL and Pony specific. Crop Factor Height | 0
target_width | INT | SDXL and Pony specific. Set the target image resolution after upscale. | 1024
target_height | INT | SDXL and Pony specific. Set the target image resolution after upscale. | 1024
step_start | FLOAT | Step influence clamp start. Starts at 0-1. <0 Disabled | -1.0
step_end | FLOAT | Step influence clamp end. Ends at 0-1. <0 Disabled | -1.0
Squeeze_Mojo | 'Disabled', 'Squeeze + Toss', 'Keep Masks' | Merge all Mojo to the smallest possible count. Only maskless Mojo can be squeezed. | Disabled
Squeeze_Mojo_Intake | 'Disabled', 'Squeeze + Toss', 'Keep Masks' | Merge all Intake Mojo to the smallest possible count. Only maskless Mojo can be squeezed. | Disabled
Intake_Strength | FLOAT | Mixing strength of the squeezed Intake. | 1.0
Clip_Choice | 'Main', 'Additional', 'Special' | Biases the assembly towards a clip source. IF such source is provided. The only mandatory source is Main. Usage is heavily dependent on how the Mojo was made. | Main
Conditioning_Output | 'Disabled', 'Mojo (Combine)', 'Intake (Combine)', 'Mojo + Intake (Combine)' | How to construct the Conditioning Output. | Mojo (Combine)
### Outputs
Key|Type|Tooltip
|-|-|-|
Mojo |MOJO | Mojo Flow
Conditioning |CONDITIONING | Main_clip Conditioning, if not "Disabled"
Info |STRING | Info String with useful information about the Mojo and the assembly of it.

# Change Log
**v1.0 - release**  
Added **Load Mask-Map**, **Mojo Maker**, **Save Mojo**, **Mojo Loader** and **Adjust Mojo**  
* **Magical Save Node** 
    - added "Active" Boolean (On/Off Switch), to get it more in line with other nodes that support advanced comfy-flow usability.
    - changed "Save_gen_data_to_txt" and "Save_gen_data_to_png" to be actual booleans instead of selection boxes
    - added "Formatting" selection for future meta parser compatibility options.

**v0.1**  
sneaky unnamed hotfix no one noticed
 * **Thermal Latenator** 
	- now properly overrides the First_Seed with the Batch_Seeds first input. For upscale rebatch chainability, regarding reseeding.

**v0.1 - release**  
Added **Magical Save Node** and **Thermal Latenator**

# License
löl... thrive and kick back. Share my shi...iiiny stuff, mention me. you know... duh ^^
Use the power to bring beauty and excitement into the world. To tell your stories and make mama laugh.

i don't know how legally binding any of this is... so is a true license... HEYOOO ;D

oh.. i'm not liable ... forgot that one... for anything
unless you make a million bucks.. then it was all me :D
