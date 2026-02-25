# ComfyUI-WBLESS
ComfyUI custom node package. This custom node features multiple practical functions, including global variables, flow control, obtaining image or mask dimensions, and Dominant Axis Scale.
# Get Started
### Recommended
- Install via [ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager).
### Manual
- Clone this repo into : `custom_nodes`
   ```
   cd ComfyUI/custom_nodes
   git clone https://github.com/LaoMaoBoss/ComfyUI-WBLESS.git
   ```
- Start up ComfyUI.
# NOTICE
- V2.9.0 Update RunningHUB API, API Core-RustFS Node.
- V2.8.0 Add API Core Node.
- V2.7.0 Add Image Mask Blend Node.
- V2.6.0 Add the Jimeng Image 4.0 node and enhance the functionality of the Text Block node.
- V2.5.0 Added Baseline Alignment (X) and Baseline Alignment (Y) nodes.
- V2.4.2 Fix the calculation error issue of the Area Based Scale (Pixel) node.
- V2.4.1 Restore the name `Area Based Scale (Size)` to `Area Based Scale`.
- V2.4.0 Add ImageHasAlpha and Area Based Scale (Pixel) nodes,Rename the Area Based Scale node to Area Based Scale (Size).
- V2.3.1 Add an ApplyMaskToAlpha node and add new settings to the Gradient node.
- V2.3.0 Add Gradient Node.
- V2.2.4 Fix the adaptation of the switch series nodes in the new version of ComfyUI.
- V2.2.3 Fix switch node runtime errors in certain environments.
- V2.2.2 Update the Overlay Text and Text Block nodes.
- V2.2.0 Update the Area Based Scale Node.
- V2.1.2 Import the cozy_comfyui module and fix the issue where users cannot import the cozy_comfyui module.
- V2.1.1 Fixed the Get Mask Size node returning wrong dimensions in certain scenarios.
- V2.1.0 Updated the Dominant Axis Scale, Get Image Size, and Get Mask Size nodes.
- V2.0.0 is released. This is the first public version. Version 1.0 is an internal test version and will not be made public.
# The Nodes
### Set Global Variable
> The `Set Global Variable` node allows you to store your data in variables.
> <details>
> <summary>See More Information</summary>
>
> - The `Input` and `Output` nodes form a direct pipeline for better integration within workflows.
> - The `variable data` is used for inputting variable values.
> - `Scope` is used to set the order in which variables are obtained. You just need to connect them in sequence one after another.
> - `variable_name` Here you can set the name of your variable.
><img width="800" height="457" alt="image" src="https://github.com/user-attachments/assets/e5cdebc6-febd-4d1f-8535-4d26da658ef1" />
>
> </details> 
### Get Global Variable
> The `Get Global Variable` node can retrieve data stored in variables.
> <details>
> <summary>See More Information</summary>
>
> - The `Input` and `Output` nodes form a direct pipeline for better integration within workflows.
> - `variable data` is used for outputting the variable's value.
> - `Scope` is used to set the order in which variables are obtained. You just need to connect them in sequence one after another.
> - `variable_name` Here you can specify the variable you want to retrieve.
><img width="721" height="409" alt="image" src="https://github.com/user-attachments/assets/c49fc13b-be0c-4a5c-a9c1-c4e0034e3880" />
>
> </details> 
### Inversed Switch
> Used to control the direction of the workflow.
> <details>
> <summary>See More Information</summary>
>
> - Connect the main workflow to the `Input` interface, then connect the `Output` to different branch workflows. By controlling the `path` value of the node, you can determine which branch the workflow will take.
> - This node needs to be used in conjunction with `Switch`.
> - The core logic of this node draws inspiration from [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack?tab=readme-ov-file). We would like to express our gratitude to the author of `ComfyUI-Impact-Pack` here.
><img width="4507" height="2165" alt="workflow" src="https://github.com/user-attachments/assets/9a0cc5fe-e7fb-46c7-8751-4a11445433a3" />
>
> </details> 
### Switch
> Select and retrieve data from different processes.
> <details>
> <summary>See More Information</summary>
>
> - This node is usually used in conjunction with the `Inversed Switch` node; of course, you can also use it independently.
> - The `Input` interface connects to different branch workflows, while the `Output` interface will output data from the corresponding workflow based on the value of `path`.
><img width="1088" height="471" alt="image" src="https://github.com/user-attachments/assets/3a228452-94fa-4cee-b558-d2ccf2ca4ffa" />
>
> </details> 
### Dominant Axis Scale
> Smart scale input group A relative to input group B, using its longest side as the scaling axis.
> <details>
> <summary>See More Information</summary>
>
> - Height a, Width a — these are the input dimensions you need to scale.
> - Height b, Width b — these reference dimensions serve as the scaling baseline, which you can conceptualize as canvas dimensions.
> - ratio — Input your scaling factor here.
> - The output Width, Height, and scale_ratio govern different output formats.
><img width="3303" height="1224" alt="workflow (1)" src="https://github.com/user-attachments/assets/8c286089-8346-47e1-94a4-f757997d0e9a" />
>
> </details>
### Area Based Scale
> Smart scale the area of input group A with reference to input group B, based on size.
> <details>
> <summary>See More Information</summary>
>
> - Height a, Width a — these are the input dimensions you need to scale.
> - Height b, Width b — these reference dimensions serve as the scaling baseline, which you can conceptualize as canvas dimensions.
> - ratio — Input your scaling factor here.
> - The output Width, Height, and scale_ratio govern different output formats.
> - cap_threshold — the upper scaling limit threshold, beyond which the object will not scale any.
> - enable_cap — threshold activation switch.
><img width="3467" height="1237" alt="workflow (4)" src="https://github.com/user-attachments/assets/65e88b78-a1cf-41e8-95b2-78ff04f21e79" />
>
> </details>
### Area Based Scale (Pixel)
> Smart scale the area of input group A with reference to input group B, based on Pixel.
> <details>
> <summary>See More Information</summary>
>
> - The image_alpha port connects to an image with a transparency channel. You may need to use it in conjunction with ApplyMaskToAlpha. Unless you explicitly clear the transparency information of the image, please use it alongside ApplyMaskToAlpha to generate an image with transparency channel information. For specific usage, refer to the ApplyMaskToAlpha section.
> - The image input port is used to connect the background image, or it can be referred to as the reference for scaling.
><img width="2327" height="1280" alt="Area Based Scale (Pixel)" src="https://github.com/user-attachments/assets/b270bb50-5865-47a9-9738-7aebebcff390" />
>
> </details>
### Get Image Size
> Get Image Dimensions.
> <details>
> <summary>See More Information</summary>
>
><img width="509" height="348" alt="image" src="https://github.com/user-attachments/assets/0f2121c4-0641-4fb2-aaaf-48fac71d0fbb" />
>
> </details>
### Get Mask Size
> Get Mask Dimensions.
> <details>
> <summary>See More Information</summary>
>
><img width="757" height="527" alt="image" src="https://github.com/user-attachments/assets/935a2181-1113-4217-aa2c-eb11340463bf" />
>
> </details> 
### Overlay Text & Text Block
> The function of drawing text on images consists of two nodes: a parent node and a child node. The parent node is `Overlay Text`, which is used to control the overall settings, while the child node is `Text Block`, responsible for controlling individual text blocks. These two nodes work together to build a powerful text system with professional-level text adjustment functions.
> <details>
> <summary>See More Information</summary>
>
> - The `text_block` input of `Overlay Text` is used to connect `text blocks`. If multiple styles need to be controlled separately, connect multiple `text blocks`.
><img width="2543" height="2032" alt="workflow (4)" src="https://github.com/user-attachments/assets/bfb779b7-fe4e-4a84-956e-2c18db2af401" />
>
> </details>
### Gradient
> Used to generate `gradients` or `transparent gradients` for images.
> <details>
> <summary>See More Information</summary>
>
> - `gradient_type` is used to set the gradient style.
> - `rotation_angle` is used to set the gradient direction.
> - The `position` series settings are used to control the gradient effect in detail.
> - The `color` series settings are used to set gradient colors.
> - The `alpha` series settings are used to set gradient transparency.
> - The `mask` output port will output the corresponding `mask` based on the transparent gradient.
><img width="1430" height="1078" alt="workflow" src="https://github.com/user-attachments/assets/4064cab1-44f3-45e1-aea3-11fcddeab489" />
>
> </details>
### ApplyMaskToAlpha
> Set the image transparency based on the mask.
> <details>
> <summary>See More Information</summary>
>
> - Connect the mask information to the mask input, and it will output an image with an alpha channel.
><img width="2017" height="1050" alt="workflow" src="https://github.com/user-attachments/assets/3826eab6-4e5c-43da-bd99-0536dbf82efc" />
>
> </details>
### ImageHasAlpha
> Determine whether the image contains transparency channel information.
> <details>
> <summary>See More Information</summary>
>
><img width="842" height="965" alt="ImageHasAlpha" src="https://github.com/user-attachments/assets/56dfe66c-00fa-475e-8fb1-a03ea7323c34" />
>
> </details>
### Baseline Alignment (X) & Baseline Alignment (Y)
> Input two different heights, then set a baseline. The output will be how much the center position of height a needs to be adjusted so that its bottom position aligns with the baseline position of height b.
> <details>
> <summary>See More Information</summary>
>
><img width="1947" height="994" alt="Baseline_Alignment_demo" src="https://github.com/user-attachments/assets/000ecd6a-43ab-4473-bcfb-148985e34107" />
>
> </details>
### Jimeng Image 4.0
> Jimeng Image 4.0 node.
> <details>
> <summary>See More Information</summary>
>
> - Please go to [火山引擎](https://www.volcengine.com) to complete the key application.
> - Since Jimeng 4.0 does not currently support base64, please go to [PicGo](https://www.picgo.net) to obtain the image hosting key.
><img width="1701" height="960" alt="workflow (5)" src="https://github.com/user-attachments/assets/ed4b45e1-770e-48f4-a4f9-8b1275ffe83c" />
>
> </details>
### Image Mask Blend
> Input a background image and an image to be blended, then input the mask of the area in the background image where blending is required. The node will scale and move the layer image based on the size and position of the mask.
> <details>
> <summary>See More Information</summary>
>
><img width="1322" height="1108" alt="workflow (1)" src="https://github.com/user-attachments/assets/73492dc4-1a03-4df2-ab94-cc00d3758132" />
>
> </details>
### API Core
> API Core Transfer Node.
> <details>
> <summary>See More Information</summary>
>
> - Please go to [API Core](https://api.apicore.ai/console/token) to complete the key application.
> - Please fill in your ComfyUI web address in `server_origin` for uploading reference images. Note that this address must be a public IP address or domain name.
> - Once you fill in the `api_key`, the node will automatically retrieve available models for you to select.
><img width="670" height="460" alt="image" src="https://github.com/user-attachments/assets/9006aa94-0765-467f-bf2f-d41f333c5390" />
>
> </details>
### API Core-RustFS
> API Core variant that uses RustFS to upload image URLs, and requires self-deployment of RustFS.
> <details>
> <summary>See More Information</summary>
>
><img width="617" height="553" alt="image" src="https://github.com/user-attachments/assets/67002d7c-9443-40f9-a589-92754e37012b" />
>
> </details>
### RunningHUB API
> RunningHUB API Invocation Node.
> <details>
> <summary>See More Information</summary>
>
><img width="627" height="398" alt="image" src="https://github.com/user-attachments/assets/503f3cc5-a818-4475-9b62-89b72035dd09" />
>
> </details>
