# ComfyUI-MinDalle

This is a quick-and-filthy wrapper of
[min-dalle](https://github.com/kuprel/min-dalle) for ComfyUI. min-dalle
downloads and loads the actual model itself, making for a very simple, but very
non-idiomatic, ComfyUI node.

min-dalle's internal tensor format doesn't match what ComfyUI nodes expect, so
the output of this node is a PIL image. If you need it to be tensors (which you
probably do), then you can convert it with something like the “PIL to Image”
node in
[ComfyUI-Ib-CustomNodes](https://github.com/Chaoses-Ib/ComfyUI_Ib_CustomNodes).
This means that the image will be generated in Torch tensors, converted to PIL,
then converted back to Torch tensors. How efficient!

This code was mostly written by AI, and then fixed and made to actually work by
Yahweasel.

A simple example workflow is provided in
[mindalle-example.json](mindalle-example.json).

![The given example workflow loaded into ComfyUI](example.png)

## How to install

Clone this repository into `custom_nodes/ComfyUI-MinDalle` and
`pip install -r requirements.txt`.
