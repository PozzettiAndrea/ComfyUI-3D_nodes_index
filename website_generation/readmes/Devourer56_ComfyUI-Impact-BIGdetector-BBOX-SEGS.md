FOREWORD

This was created using AI, and the node functionality would probably have been much simpler to implement using standard Impact Pack nodes, but I decided to go the extra mile and created a node in half a day using AI for my own needs.

The guarantee of operation is the same as for any code written using AI.

![Node ScreenShot](https://github.com/user-attachments/assets/95b9472d-192e-4ffa-97da-a00a03c39130)


The node functionality can be used for sequential detection on a single image (use the node as a magnifying glass to accurately detect the fragment). Or, it can be used in parallel if you need to aggregate multiple SEGS from a single source image into a single output with IoU filtering.

While developing the node logic, I tested it on my local ComfyUI. Everything seems to work.

It's recommended to use the node with Include masks in output = true. Without it, most nodes receiving SEGS will not work or will return errors. I don't know why the large language model was concerned about this feature significantly increasing the load. (Even complex SEGM masks were generated in an acceptable time of about 0.5 seconds.) Therefore, I asked the large language model to add mask simplification.

The node previews turned out so-so (but I didn't want to spend any more time on them when I had the SEGS Preview from the Impact Pack).

I also asked the large language model to add descriptions for the inputs, outputs, switches, and the node itself.



Cascade Detector

A node for ComfyUI that implements a cascade object detection system (bbox/segm) using the yolo BBOX/SEGM models.



Key features:

Two operation modes: Sequential and parallel.

Multi-stage processing: Up to 3 detection stages, each with its own settings.

Flexible settings: Individual detector\_type, confidence, scale\_mode, crop\_factor, target\_size, max\_size, classes, and other parameters for each stage.

Combined output: segs\_output\_all\_stages combines the results of all stages.

Impact Pack Integration: Output in SEGS format, compatible with other Impact Pack nodes (e.g., SEGSPaste, SEGSDetailer).

Filtering: Option to filter results by confidence, min\_bbox\_width, and min\_bbox\_height.

Mask Management: The include\_masks\_in\_output switch enables experimental mask recalculation for correct compatibility between stages and the generation of masked\_fragments\_image.

Mask Simplification: When include\_masks\_in\_output is enabled, the simplify\_masks switch applies morphological operations to masks to reduce complexity.

Visualization: Output previews (preview\_image, cropped\_fragments\_image, masked\_fragments\_image).

Alternative path: image\_bypass returns the original image if no segments are found in segs\_output\_all\_stages after filtering; otherwise, it returns a black square. This is useful for organizing processing chains where, if detection fails, the original image should be used in another node.

Important features:

Requires Impact Pack.

segs\_input is used only in sequential mode to transfer initial segments (e.g., from another node).

The scale\_mode, target\_size, and max\_size parameters are now individually configurable for each stage.

masked\_fragments\_image displays isolated segments bounded by their masks if include\_masks\_in\_output=True. Otherwise, it displays a black square.

Output assignments:

segs\_output\_all\_stages: The main SEGS output, combining the results of all stages.

preview\_image: Image with overlaid BBox detections (yellow).

Cropped\_fragments\_image: An image containing cropped fragments of all detected segments.

stage1\_segs, stage2\_segs, stage3\_segs: SEGS output for the results of each stage individually (deprecated outputs if not used in other nodes).

masked\_fragments\_image: An image containing cropped and masked fragments (only the inner part of the mask is visible) of all detected segments (requires include\_masks\_in\_output=True).

Image Bypass: Returns the original image if no segments are found in segs\_output\_all\_stages after filtering; otherwise, returns a black square. Useful for organizing processing chains where, if detection fails, the original image should be used in another node.


