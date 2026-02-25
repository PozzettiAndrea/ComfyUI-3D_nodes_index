# ErosDiffusion — ComfyUI ControlNet Map Cache & Browser

**Handle your controlnet maps like a pro!**
Save resources by skipping already done work!
Generate, tag, cache, search and use ControlNet maps inside ComfyUI.


> [!WARNING]
> This is a **beta** stage plugin and as such it might change often.
> If you want to support development feel free to [donate](https://donate.stripe.com/3cI7sDgZg4rr2Ln0HfcV202)



## Installation
### Option 1 (**with comfy ui manager**):

1. search for ControlnetMaps and install
  <img width="1348" height="265" alt="image" src="https://github.com/user-attachments/assets/97477570-3219-44be-827d-d7681d10df88" />

1.1. _optional_, if you need to generate maps you can install comfyui_controlnet_aux

<img width="1349" height="234" alt="image" src="https://github.com/user-attachments/assets/d4e855ff-dbf5-4998-988a-c3ad5fd28294" />



### Option 2 (**Manual installation**):

1. **Clone** this folder into your ComfyUI `custom_nodes` directory:
   1. `cd <your comfy ui custom_nodes directory>`   
   1. `git clone https://github.com/erosDiffusion/ComfyUI-ErosDiffusion-ControlnetMaps.git`
  
### After installation    

2. **Restart ComfyUI**: the nodes appear under the `ErosDiffusion` category or in the templates.
3. **Optional** open the "ControlNet Maps Browser" sidebar and import this file:

   [eros_maps_export_2025-12-17T22-07-25-112Z.zip](https://github.com/user-attachments/files/24222985/eros_maps_export_2025-12-17T22-07-25-112Z.zip)
   
   it contains two pre-generated maps and some tags to play with
   
   <img width="866" height="709" alt="image" src="https://github.com/user-attachments/assets/d165f3c4-1545-4e80-8c6f-33ad882ee45d" />


### Do you already have maps ?
...and don't want to generate them ? paste them in the input/maps folder under the proper folder! files are synchronized by name.

## Usage (all workflows are accessible from comfyUi templates)

3. **generateMaps**: open the baseWorkflowCanny from templates to generate your first map and cache it. pick a photo you licke and run. the map will now be available under "canny" filter and "original". this workflow requires no additional dependency.
4. **useMaps**: to select the map and use it choose the useCachedMaps workflow. open the Controlnet Map Browser sidebar and connect the node using the button "Open/Connect to map browser" in the map browser node. select a cached map. run the flow.
5. **optional**, to **generate all maps** use the generateMaps workflow (requires you to install the map generator node).

> [!important]
> **This node does NOT generate the maps**:
> - It helps you organize in a well known folder input/maps them and use them fast via browser.
> - To generate the maps you will need other nodes ([Aio AUX preprocessor](https://github.com/Fannovel16/comfyui_controlnet_aux), [depth anything v2](https://github.com/kijai/ComfyUI-DepthAnythingV2) or  [depth anything v3](https://github.com/PozzettiAndrea/ComfyUI-DepthAnythingV3), canny (from comfy core) or whatever you like/need!)

### But wait... do you have to generate maps if you already have some ?

**Not at all !** -  **If you have some just copy them in the appropriate folder** (input/maps/<type>) and refresh
(images that don't have an equivalent name in another folder won't show the original overlay and when switching type won't match anything), no need to generate them!
<img width="625" height="513" alt="image" src="https://github.com/user-attachments/assets/fe2f43c0-a123-446a-b82b-1c3640da4333" />


## Changelog
**07.01.2026 - 15:02**
- published to comfy registry
- udpaded workflows and readme

**17.12.2025 - 17.22**

- refactored code to use more features from comfy, sidebar, toasts, messaging
- added import, export, reset, fixed some regressions, update newly generated maps on the fly

**16.12.2025 - 17.22**

- There was a tiny initialization issue that would prevent you from opening the map browser if the file reference would be empty. this would be a common scenario for a new installation, and it is now solved.
please go to your extension directory, and in a terminal from the extension folder where you cloned do `git fetch` and `git pull` to get the newer version
- The good news is a fresh install of comfy requires no dependency install so it should work out of the box, the necessary sqlite db are created on the fly when missing. 


<img width="1415" height="1051" alt="image" src="https://github.com/user-attachments/assets/6594ff91-23cd-454d-ab89-6284460ef585" />


### Video preview for usage (slightly older version)

https://github.com/user-attachments/assets/f7881a43-2fc4-41ca-9655-8090d4b42c64

## Overview

This package provides two ComfyUI nodes that simplify working with ControlNet maps by caching generated maps to disk and exposing a visual browser as well as tag them and store references in a local sqlite db:

- `ControlnetMapCache` — smart cache layer that checks a disk cache before requesting expensive preprocessors and can save and tag generated maps for reuse.
- `ControlnetMapBrowser` — sidebar/browser integration to preview and load cached maps (returns the selected map) ideally you would use this node to quickly select a cached map and use it in your workflow.
- `Load Image ErosDiffusion` — Loads an image and returns the filename and other info (attempts to read the prompt) useful when generating maps.


These nodes are designed to reduce repeated preprocessing work and help organize map assets by filename and type.
Ideally later share and reuse high quality maps in a standard format.
You can as well import and export the data set with the tags. to share it.

## Key Features

- Cache lookup by filename and map type (supports multiple extensions).
- Browse and select images , once a node is connected the selection shows in the node and sets the filename to pass to other nodes (eg to apply the controlnet)
- `generate_all` option to batch-save all connected preprocessors and the original image tags them and saves all maps to cache folder
- Tagging: comma-separated `tags` input is persisted to a lightweight metadata DB for later retrieval and UI updates. You can connect an llm to the source image and have comma separated list of tags of your choice.
- Browse and search the nodes by tag or type and easily select the image for reuse.
- `auto` mode detects existing map types and only runs connected preprocessors when needed (returns the first connected, top to bottom) - auto mode is currently bugged.
- Import and Export, db reset
- Easily add remove and filter with tagging
- Start and filter by favorite
- Resize the sidebar
- Responsive image column and sizing

## Example Workflows 

There are **three workflows** preset in the workflow examples folder
You also find them in the ComfyUI templates sidebar

  <img width="2005" height="1298" alt="image" src="https://github.com/user-attachments/assets/0431e3fa-792e-4346-a592-6092164f468d" />



## Remarks

- Modifier keys can be used for advanced usage of tags, they are described on top of the tag filtering
- Tags are not duplicated, so you can freely re-insert them
- To insert multiple tags while generating or after, comma separate them. the input field can be submitted pressing enter.
- **automatic tagging is not yet implemented. but you can link an llm when generating maps**
- You filter typing a tag name, that also filters the images otherwise click on the tag
- Clicking a different tag uses the new cone, ctrl+click deselect, shift+click adds to the current selection
- Import is non destructive but additive (adds missing tags and images so feel free to import on top of what you have)

## Known Issues

- The preview does not show in ControlnetMapBrowser node  when using nodes 2.0...if you want to see the preview in the node use the older gui, tested in comfyui v0.4. 

## Troubleshooting

- If cached maps are not being found, verify `cache_path` and that filenames use the same basename (node strips extensions when checking).
- For `auto` mode misses, ensure the corresponding `source_<type>` input is connected so the preprocessor can run and generate the map.
- If browser doesn't show files, confirm the UI has access to the configured `cache_path` and any `extra_path` you provided.

## Further Roadmap
- [x] Provide downloadable starter import .zip
- [x] Integrate with ComfyUI Registry
- [ ] Test and Optimize for large number of images
- [ ] Implement automatic tagging
- [ ] Implement automatic map generation (we'll see, AIO there's plugins for that)

## Contributing
- have you created a stunning set of controlnet maps ? give me a link to the donwload and I will feature them here!
- PRs welcome. Keep changes focused and add tests/examples where possible. Test it and tell me what's wrong.

## Supporting

If you feel like rich:  [donate](https://donate.stripe.com/3cI7sDgZg4rr2Ln0HfcV202)






