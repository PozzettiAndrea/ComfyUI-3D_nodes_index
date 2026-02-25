# ComfyUI_Eagleshadow
My custom nodes for ComfyUI, mostly made using GPT-4.

## Select Model 20
Modified ComfyRoll "CR Select Model" node to load 20 models instead of 5.

## Round Float to String
Rounds a given floating-point number to two decimal places and concatenates it with a provided string. It returns the resulting concatenated string. I use it to add a number with a little text prefix into the filename.

## Save Image To Folder
Takes an image, folder path, and file name as input, and saves the image to that folder using that filename. Kind of shocking I had to make a custom node for something this basic.

## Fix Checkpoint Name
Takes a file path as input and extracts the checkpoint name by finding the substring between the last backslash (\) and the .safetensors extension. It returns this extracted checkpoint name as a string.

## Select Control Net
Modified ComfyRoll "CR Select Model" node to load control nets instead of models.

## Simple Load Image Batch
This is the same as Load Image Batch from WAS Node Suite but with all extra functionality removed, stripped down to barebones functionality. I was working with processing 10000 video frames with ComfyUI and found this WAS node to be a speed bottleneck (only noticeable in such a scenario where every millisecond counts). My stripped-down version is like 100 times faster and still gets the job done. I had to add seed output to it just to make it execute on Auto Queue.

## KSampler Same Noise
Same as regular KSampler except ensuring that the same noise is applied across all batches. Normally each image in the batch will have different noise even when using the same seed, as this allows making two different images in parallel. This is not desirable when trying to use batching with video frames as in that case using the same noise makes the consecutive frames much more temporally stable by default. Unfortunately, there is some deeper level of Comfy that introduces some small difference to the noise even when noise is made to be the same, which defeated the purpose of this for me. This node gets this idea 90% of the way there, but for me, it wasn't good enough in the end and I instead use 3 ComfyUI instances in parallel when operating on video frames, in order to get 100% the same noise between frames. Thought I'd share the node anyways.

## Batch 12 Images
Takes 12 individual images as input and stacks them into a single batch tensor.

## Image Linear Gamma Composite Masked
Composite two images with optional resizing of the top layer and masking. It applies linear gamma correction before compositing and re-applies gamma correction afterward.

## Mask Glow
This node adds a glow effect to a mask image. It provides various parameters to control the size, blur, and intensity of the glow, as well as options for overlaying the original mask and applying fadeout.

It's like blurring the binary mask but without having the blur extend into both sides, but only to one side.

## Offset Image
Offsets an image by the specified horizontal and vertical amounts, works the same as the offset filter in Photoshop.

## Detect Transparency
Analyzes a mask image to determine if there is any transparency. It considers any non-zero value in the mask as indicating transparency. If transparency is detected, the node outputs 1; otherwise, it outputs 2.
