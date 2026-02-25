# ComfyUI-ImageBatch-Utility

[English][<a href="README_ja.md">日本語</a>]

This is a collection of custom nodes required for processing batch images.

Currently, it only includes "Image Batch To Sub Batches."
New nodes will be added as needed.

## Image Batch To Sub Batches
This node converts an Image Batch into multiple Image Batches with a specified Batch Size.
If the original batch size is not perfectly divisible, the size of the last Image Batch will be the remainder.

![image](https://github.com/user-attachments/assets/fe369aee-db20-452e-9b50-db0c1ce44d8f)
