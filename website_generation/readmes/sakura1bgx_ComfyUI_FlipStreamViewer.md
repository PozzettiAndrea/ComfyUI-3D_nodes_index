# ComfyUI_FlipStreamViewer

**ComfyUI_FlipStreamViewer** is a tool that provides a customizable viewer interface for flipping images with frame interpolation.

<div><video controls src="https://github.com/user-attachments/assets/2a40c7c6-045e-4d86-a0fd-51a24f5472b4"></video></div>

## Getting Started
1. **Run ComfyUI** and from ComfyUI-Manager, select Manager -> Custom Node Manager and install ComfyUI_FlipStreamViewer.
2. **Restart ComfyUI** and load the `simple.json` file located in the `workflows` folder.
3. Access the viewer at the following URL if ComfyUI is running at localhost port 8188:

`http://localhost:8188/flipstreamviewer`

4. To respond to viewer input:

- **NOW NO NEED TO USE INSTANT MODE, JUST RUN.**
- ~~Check 'Extra options', 'Auto Queue', and 'instant' on the ComfyUI control panel.~~
- ~~Then click the 'Queue Prompt' button.~~

5. The UI nodes will refresh after the workflow is completed once, so you need to click 'Update' after that.

6. The 'preset' folder may be created in the current directory for saving and loading preset files.

## Limitations

- Please note that this tool is not designed with security measures against third-party attacks. Therefore, it should only be used for personal purposes within a secure network.
- There is no save video function available; please customize your workflow as needed.

## Optional Custom Nodes dependencies

The following custom nodes can be used as needed:
- ComfyUI-Inspyrenet-Rembg: For FlipStreamRembg
- ComfyUI-Frame-Interpolation: For FlipStreamFilmVfi

The following custom nodes may also be used within workflows:
- ComfyUI Impact Pack
- LoRA Tag Loader for ComfyUI
- ComfyUI-WD14-Tagger
- ComfyUI-AnimateDiff-Evolved
- ComfyUI-VideoHelperSuite
- ComfyUI-DepthAnythingV2
- ComfyUI-Advanced-ControlNet

## Optional Python Packages Dependencies

llama-cpp-python for FlipStreamChat:
```
REM Before that, may be need to install Visual Studio 2022, VC++ development options and cmake
set PATH=D:\ComfyUI_windows_portable\python_embeded;D:\ComfyUI_windows_portable\python_embeded\Scripts;%PATH%
cd python_embeded
python -m pip install scikit-build-core
python -m pip install cmake
set CMAKE_ARGS="-DGGML_CUDA=on"
python -m pip install llama-cpp-python
```

## UI Features

- **Customizable Left Panel**: The left panel UI is customizable with UI Nodes.
- **UI Node Ordering**: These UI nodes are ordered by their titles, and you can change the node titles to something like '10.steps' or '11.cfg'. You can also click on the title to compact the node on the workflow.
- **Label Input**: Each UI node has a 'label' input, which should be a unique identifier used as the parameter name. 'lora' is internally used, so they cannot be used for labels.
- **Enable Output**: Each UI node also has an 'enable' output to use with 'Control Bridge' for switching to bypass some nodes or FlipStreamSwitch* for switching input.
- **Right Panel**: You can operate several prepared functions such as Status, Darker, Preset, and Lora.
- **Status**: The right panel shows ComfyUI status and error information.
- **Darker**: You can adjust the image brightness on the viewer using the darker parameter. It can also be set via query:
`http://localhost:8188/flipstreamviewer?darker=0.33`
- **Preset**: You can save and load parameters that are set on viewer controls. There are joking level XOR crypt mode for preset files, it can be use with &px query. The 'M' button means Move to another folder. It can also be set via query:
`http://localhost:8188/flipstreamviewer?showPresetDialog=1&presetFolder=folder_name&presetFile=file_name.json`
- **Lora**: You can select LoRA and choose tags. It can also choose random tags. The LoRA preview box can be clicked to jump to the Civitai LoRA page if found. The 'M' button means Move to another folder. The 'T' button means Toggle. The 'R' button means Random choose.
- **Toggle View**: You can click the center panel to hide the left/right panels and the message box, a subsequent click will show them. It can also be set via query: 
`http://localhost:8188/flipstreamviewer?toggleView=1`
- **Message Box**: If a message is set by FlipStreamSetMessage, you can view it at the top left of the center panel.
- **Auto Hide**: Stream and preview in the viewer will automatically hide after 5 minutes if the page is not reloaded.

## UI Nodes

- **FlipStreamSection**: A section label for UI Nodes.
- **FlipStreamButton**: Run and Capture buttons. The Capture button can be use with FlipStreamGetFrame to get captured image.
- **FlipStreamSlider**: A slider for adjusting values.
- **FlipStreamTextBox**: A text box for inputting multiline text.
- **FlipStreamInputBox**: An input box for various boxtype inputs. The 'U' button means update. You can choose special boxtype 'seed' or 'r4d' with the 'R' button, which means randomize. The boxtype 'r4d' can be used to generate a 4-digit part of a prompt like 'MOV_{num}'. In this case, FlipStreamTextReplace can help find '{num}' and replace with the output of the input box.
- **FlipStreamSelectBox_Samplers**: A select box for choosing samplers.
- **FlipStreamSelectBox_Scheduler**: A select box for choosing schedulers.
- **FlipStreamSizeSelect**: A select box for choosing size by aspect ratio. The size can also get using FlipStreamGetSize.
- **FlipStreamFileSelect_Checkpoints**: A file selector for checkpoints. 'mode' is used to select a subfolder such as 'sd15', 'sdxl', 'pony', or 'flux' in 'checkpoints'. 'use_sub' means using subfolders in the 'mode' folder. 'use_move' means using the move file selector.
- **FlipStreamFileSelect_VAE**: A file selector for VAE models.
- **FlipStreamFileSelect_LLM**: A file selector for LLM models.
- **FlipStreamFileSelect_ControlNetModel**: A file selector for ControlNet models.
- **FlipStreamFileSelect_TensorRT**: A file selector for TensorRT models. It may be used with ComfyUI_TensorRT.
- **FlipStreamFileSelect_AnimateDiffModel**: A file selector for AnimateDiff models. It may be used with ComfyUI-AnimateDiff-Evolved.
- **FlipStreamFileSelect_Input**: A file selector for ComfyUI input folder.
- **FlipStreamFileSelect_Output**: A file selector for ComfyUI output folder.
- **FlipStreamPreviewBox**: A box for previewing the input image. You can select the ROI (Region of Interest) in the preview by dragging the mouse.
- **FlipStreamPasteBox**: A box for paste an input image. You can select the box by click once, then you can paste image from clipboard by Ctrl+V or delete image by DEL.
- **FlipStreamLogBox**: A box for displaying logs on the screen.

## Other Nodes

- **FlipStreamRunOnce**: Updates parameters, reloads pages, and run the current workflow once.
- **FlipStreamSetMessage**: Sets a message for the message box at the bottom of the center panel.
- **FlipStreamAnd(experimental)**: Multiple inputs AND operation node.
- **FlipStreamOr(experimental)**: Multiple inputs OR operation node.
- **FlipStreamSetState**: A node for setting internal state.
- **FlipStreamGetState**: A node for getting internal state.
- **FlipStreamSetParam**: A node for setting parameters. However, it needs a reload to update the value in the viewer UI.
- **FlipStreamGetParam**: A node for getting parameters. 'lora' is a prepared parameter that contains text at the Lora input. Some prompts can contain '{lora}' and FlipStreamTextReplace can help find '{lora}' and replace it with the output of the get param node of 'lora'. 'b64dec' is true for 'lora' and other 'FlipStreamTextBox' parameters, because these multiline parameters are internally base64 encoded.
- **FlipStreamGet(experimental)**: A node for getting internal state and parameters with independent node cache.
- **FlipStreamGetFrame**: A node for get image from frame buffer. It can be use with FlipStreamButton - Capture button to get captured image.
- **FlipStreamGetPreviewRoi**: A node for obtaining the preview ROI (Region of Interest) selection.
- **FlipStreamImageSize**: A node for getting image size.
- **FlipStreamTextReplace**: A node for replacing text. It will output the result of `text.replace(find, replace.format(value))`.
- **FlipStreamTextConcat**: A node for concatenate text.
- **FlipStreamScreenGrabber**: A node for grab multiframe screenshots.
- **FlipStreamVideoInput**: A node for input video frames.
- **FlipStreamSource**: A node for prepare image or latent source.
- **FlipStreamSwitchImage**: A node for switching images.
- **FlipStreamSwitchLatent**: A node for switching latents.
- **FlipStreamGate(deprecated)**: A node for consolidating input timing to ensure that inputs to the sampler do not occur sequentially.
- **FlipStreamRembg**: A node for remove background. It depends on ComfyUI-Inspyrenet-Rembg.
- **FlipStreamSegMask(deprecated)**: Currently cannot use, so please use original node ComfyUI-Florence2.
- **FlipStreamChat**: Loads an LLM (Large Language Model) and obtains chat responses. It only supports *.gguf files in the models/LLM folder and uses llama-cpp-python. The output format can be customized using the response_format parameter, which supports [JSON Schema](https://llama-cpp-python.readthedocs.io/en/latest/#json-schema-mode) for structured responses.
- **FlipStreamParseJson**: Extracts values for multiple keys from a JSON string and joins them using a specified delimiter.
- **FlipStreamChatJson**: Mix and simplified FlipStreamChat and FlipStreamParseJson using auto generated json scheme.
- **FlipStreamBatchPrompt**: A node for simple batch prompting. Use the following format for the input prompt of this node. The 'pre text' and 'append text' sections apply to all frames. The separator `----` should consist of four hyphens, and each line of 'frame text' applies evenly to the number of frames specified in 'frames'. For example, if 'frames' is 8 and there are 2 'frame text' lines, they will be applied starting from frames 0 and 4.
```
pre text,
----
- frame text,
- frame text,
----
append text
```
- **FlipStreamFilmVfi**: A node for video frame interpolation. It depends on ComfyUI-Frame-Interpolation.
- **FlipStreamViewer**: A node for viewing content. The 'allowip' parameter allows you to set IP addresses that can access the viewer. ComfyUI commandline options "--listen 0.0.0.0" and appropriate firewall settings are also needed for that. The 'w14exc' parameter is used to set exclude_tags for the WD14 Tagger. 'fps' can control flip speed.
- **FlipStreamViewerSimple**: Simplified FlipStreamViewer.
- **FlipStreamCurrent**: A node for setting current information text on the right panel status info.
- **FlipStreamAllowIp**: A node for setting allowip.
- **FlipStreamLoraMode**: A node for setting loraMode.
- **FlipStreamSaveApiWorkflow**: A node for save current workflow as api workflow.
- **FlipStreamRunApiWorkflow**: A node for run an api workflow.
- **FlipStreamFree**: A node for free model and comfy caches.
- **FlipStreamShutdown**: A node for scheduling shutdown (Windows only).

## For More Quality

- Use more higher-quality checkpoint models.
- To enhance stability between frames, use a deliberate prompt in the 'pre text' to establish a consistent background, such as `ideal background, on desk`.
- Select the appropriate words or LoRA in 'frame text' to achieve the desired motion.

## For More Speed

- ComfyUI commandline options '--mmap-torch-files --fast' are good for speed, however it depends on system and model.
- And '--use-sage-attention' option will good for RTX50xx speed up.
```
REM Before that, may be need to install Visual Studio 2022, VC++ development options and cmake. Also need to set PATH for git.
REM Before that, setup the same version of comfyui python from official installer, then place include and libs in python_embeded.
REM You can get build_sage.py from https://github.com/thu-ml/SageAttention/issues/228#issuecomment-3483944852
set PATH=D:\ComfyUI_windows_portable\python_embeded;D:\ComfyUI_windows_portable\python_embeded\Scripts;%PATH%
cd python_embeded
python -m pip install ninja
python -m pip install -U --pre triton-windows
git clone https://github.com/thu-ml/SageAttention.git
cd SageAttention
copy ..\build_sage.py .
python build_sage.py
```

## To Avoid OOM

- The ComfyUI commandline option '--reserve-vram 2' may good, it will work as buffer.
- Edit comfy code using try except pass around error points may practical for private use, but it may cause difficulty on update comfy.
- FlipStreamSaveApiWorkflow, FlipStreamRunApiWorkflow, FlipStreamSetState, FlipStreamGet nodes are useful to separate workflow to avoid OOE, because comfy keeps cache on each workflow and the cache take up large memory. FlipStreamGetState, FlipStreamGetParam, FlipStreamGet nodes have independent cache system, it can bridge any data on workflows.

## Workflow Examples

These workflow are sometimes old.

- **simple.json**: Customized a ComfyUI default workflow for FlipStreamViewer UI nodes.
- **dmd2_lora.json**: Using DMD2 and some LoRA, only needs 5 steps to generate an image.
- **segmask.json**: A 2-step process for generating frames using batch prompts and segmentation mask, followed by interpolation.
- **animate.json**: Using AnimateDiff with FlipStreamSource, FlipStreamBatchPrompt, and FlipStreamFilmVfi.
- **grab_rembg_depth_animate.json**: Using ControlNet and AnimateDiff with FlipStreamScreenGrabber, FlipStreamRembg.
- **quick_vid2vid.json**: Quick tuning workflow for vid2vid.
- **quick_vid2vid_roi.json**: An example demonstrating the use of FlipStreamGetPreviewRoi and FlipStreamGate.
- **visualnobel.json**: Visual nobel like UI using FlipStreamChat.











