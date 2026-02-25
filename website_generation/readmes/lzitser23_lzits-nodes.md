# lzits-nodes
A collection of custom nodes for Comfyui

## Included Nodes
- String Splitter
- String Appender (Suffix)
- String Prepender (Prefix)
- Index Picker
- LoRA Selector Multi-Output
- Image Outpaint (Color Canvas)

## Image Outpaint (Color Canvas)
This node lets you:
- Upload/load an image directly in the node UI.
- Expand the canvas on left/right/top/bottom without scaling the original image.
- Fill new outpaint regions with a chosen color (`#RRGGBB`, `#RGB`, `r,g,b`, or basic names like `white`).
- Output a mask where `1.0` is the new outpaint area and `0.0` is the original image.
