# zer0gear's ComfyUI Utils

A short collection of personal use nodes that I thought may be useful to others. No real coherence or theme here, just nodes that I wanted that I couldn't easily find.

## List Combine Node
Combines a list of strings into a single string, with each item separated by a specified separator. Intended for use with a tokenizer + prompt splitter, but could theoretically be used with anything that returns a list of strings.

Includes a Combine Last X Items variable to pre-combine the last X items in the list before adding the separator.

## Multiline String Node
Similar to a Note node, allows you to enter a multiline string but has an output widget to allow its contents to be passed to another node.

## Prompt Minimizer And Splitter Node
(Pardon the name, I couldn't think of a more elegant one)

Based heavily on the Tiktoken Tokenizer and String Cleaning nodes from [MNeMiC Nodes](https://github.com/MNeMoNiCuZ/ComfyUI-mnemic-nodes), this node is meant to strip trailing and leading whitespace from tags as well as optionally break prompt into X-token long chunks. Again, major kudos and thanks to MNeMoNiCuZ for the inspiration, I just wanted to combine a few different nodes from different repos into one node for my purposes.

## Tavern Card Info Node
Reads basic fields from an uploaded PNG in v2 spec character card format.

## Tavern Card Creation Node
Allows for the creation of a basic v2 spec character card using an input image as a base.