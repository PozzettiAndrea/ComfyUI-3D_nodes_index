# ComfyUI-SocksLatentPatcher
This node circumnavigates the loss of detail, saturation/desaturation for infinite length video generation, the node bypasses the vae decode and directly patches the latent tensor. experimental covering i2v and vace extend (should work on all models apart from ti2v5b "wan2.1&amp;2.2Hs/Ls, hunyuan, ltxv and skyreel are compatable")

UPDATE - 10/10/25

Added a refined reference injection workflow,

below is a raw output using this node and the new workflow from a single image of a car "no upscaling, interpolation or fps correction" - 

https://github.com/user-attachments/assets/d4759379-3272-4ad1-8049-75955680b88b

below is an example screenshot of where this node should be attached between the last ksampler of the previous generation and the first ksampler of the next generation.
<img width="789" height="656" alt="Screenshot 2025-10-10 062041" src="https://github.com/user-attachments/assets/921b91fa-50b4-418c-8003-17b27785ae93" />

the new addition to the workflow is the addition of referance information that can be pulled from a previous generation to correct for abnomalities, the use of a mask for the control video/frames is also required as it helps the model to understand the intent of the process.

below is an example of pulling frames from a original generation from vae decode "this is for the conditionals (textEmbeds) only, they are overwrote in the latent by my node (ele0=previousFrame)"
<img width="1034" height="442" alt="Screenshot 2025-10-10 064845" src="https://github.com/user-attachments/assets/b94399ff-a73c-4566-8991-f4e108858432" />

Below shows how the reference is injected for the conds, and overwrote by my node.
<img width="875" height="574" alt="Screenshot 2025-10-10 064940" src="https://github.com/user-attachments/assets/45d38db0-76bb-4184-8024-d03053c25b8d" />


-----------------

Below is an example of the vace8frame patcher, patching from the i2v into vace, using the original ref and last 8 pixel-space frames "for the encode process" for the vace conditionals, then overwriting the vace reference dim with the last frame from the previous generation while patching the last 8 frames in latent space - 


https://github.com/user-attachments/assets/2f9cee88-d9ce-4693-8a74-6f891b1f5bc4

the issue is not the quality loss of the vae, yet the decompression and recompression of the last frames, like with downsampling, a division of 2 equates to 4 pixels becoming 1 pixel the condensed combination of all 4, this changes the colour overtime, degrading recursivly.

This is an Experimental node and is still a wip, currently runs on 8gb vram using gguf models.
the above video took 2 hours and 30 mins on an rtx 3060 ti 8gb.

The workflow allows for multiple conditionals, and has a bool at the end of each generation allowing testing before continuing to generate the next segment-

<img width="1897" height="609" alt="Screenshot 2025-10-05 035357" src="https://github.com/user-attachments/assets/318320a4-ce41-4bc9-988d-ea86ebd2088b" />

The node takes the output from the previous ksampler and patches it over the next ksampler input- 

<img width="1414" height="917" alt="Screenshot 2025-10-05 045029" src="https://github.com/user-attachments/assets/da04854b-3e14-4c31-a3b3-356b350e22ee" />

The results are compiled together at the end of all generations-

<img width="834" height="741" alt="Screenshot 2025-10-05 035744" src="https://github.com/user-attachments/assets/ec28d151-40a2-4bd0-8b0e-89d2b8298765" />
