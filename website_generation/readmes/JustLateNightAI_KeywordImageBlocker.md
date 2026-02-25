# KeywordImageBlocker
A ComfyUI node that will block images that flag custom set key words

## How It Works
plug your VAE Decode Image node into a image tagger, and into the Keyword Image Blocker. Then plug the text output from the image tagger into the tags node (the top text box on Keyword Image Blocker) and plug your image output node into your save image. Type in the words you want to flag for in the bottom text box and separate with commas. If the image is tagged with any of the filter words then it will be replace with the warning.png in the assets folder. 

This is just the blocker, not also a image tagger you will have to also get an image tagger such as WD14 Tagger.

Here’s a quick peek at the node in action:

<img src="workflow example/Screenshot.png" alt="Workflow Example" width="600"/>
