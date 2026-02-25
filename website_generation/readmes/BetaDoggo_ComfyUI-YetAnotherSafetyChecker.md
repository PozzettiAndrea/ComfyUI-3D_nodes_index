Just a simple node to filter out NSFW outputs. This node utilizes [AdamCodd/vit-base-nsfw-detector](https://huggingface.co/AdamCodd/vit-base-nsfw-detector) to score the outputs. I chose this model because it's small, fast, and performed very well in my testing. Nudity tends to be scored in the 0.95+ range, but I've set the default to 0.8 as a safe baseline.
# Usage
The node has 1 image input, 1 image output, a string output, a threshold slider and a cuda toggle. The first image output is the primary output. It will output black unless the input falls below the selected threshold. The string output outputs the score given to the image. This is intended to be used with a show text node to dial in your threshold setting. Finally, the node includes a toggle which will load the model on the gpu for faster processing.
# Preview
![preview](https://github.com/BetaDoggo/ComfyUI-YetAnotherSafetyChecker/blob/main/preview.png)
