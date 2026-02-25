In an effort to clean up image metadata, this custom node allows users to selectively choose what to add to the generated image's metadata. As a result, images will not be able to load ComfyUI workflows.

Currently, there are 5 inputs allowed, with each needing a key and corresponding metadata pair. If the key is empty, that key:metadata pair will be ignored.

The most prevalent use case for such selectivity is being able to save the prompt in a clear manner, as seen below. 
- To do so, the easiest method is to use a `String` node when typing the prompt, which can output text to both `CLIP Text Encode (Prompt)` as well as the `Save Image (Selective Metadata)` node. An example of this can be seen in the below workflow.
  -  (such as `Multiline String` which has been packaged with this node for convenience)


<img width="970" height="551" alt="image" src="https://github.com/user-attachments/assets/140c99cc-9f3f-406c-b1c7-daa69686ae19" />

<img width="2088" height="967" alt="workflow" src="https://github.com/user-attachments/assets/1ec4774f-5616-44aa-855b-7f39157dddf7" />

To install, simply follow the below instructions:
1. Navigate to ComfyUI directory in a command prompt / terminal window
2. `cd custom_nodes`
3. `git clone https://github.com/brucew4yn3rp/ComfyUI_SelectiveMetadata/`
4. `cd ComfyUI_SelectiveMetadata`
5. `pip install -r requirements.txt`

If you use a venv with ComfyUI, make sure to activate it before doing step 5. This is a pretty lightweight node so you should already have the Python libraries required (`numpy, Pillow`)
