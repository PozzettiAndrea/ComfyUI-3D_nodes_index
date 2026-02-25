# ComfyUI-northTools

This is a collection of nodes I made (some are modified from other nodes) for ComfyUI. If used correctly they can automate a lot your workflow.

## Installation

Just download the zip from this repo and copy it to `ComfyUI/custom_nodes` folder. You can also clone the repo to the same folder.

## Nodes

### 1. Load Image List from Directory
This node is extracted from ComfyUI-Inspire Pack and edited by me. Other than doing the base things of the original node, it can also, for each image, outputs:
- `METADATA`: The metadata stored in the image loaded
- `INDEX_COUNT`: The index of the image in the list

### 2. Extract Metadata value by key
This node receive an image as input and output a string got from metadata JSON, in the relationship `KEY => Value`. Based on the key, it can output the value of the key stored.

### 3. Sum Integers
Simple node that sum two integers, no more no less.

### 4. Load Image batch/list from Directory with indexes
Similar to the load image list from directory node, but instead it also receives a string of indices of images to load.
Starting from `[0]` for first position, for example `0,2,5,8,15`.

It can output a batch or an image list.

### 5. Boolean list to index string
Useful for converting booleans to indexes to use with other nodes. Based on positions of booleans, it will convert them to indexes:
- `TRUE,FALSE,TRUE` -> `0,2` (position 0 is true, position 2 is true)

It accepts formats:
- `T,F,T`
- `1,0,1`
- `true,false,true`
- `truefalsetrue`
- `101`

Also: `true / false` are not case sensitive, so it accepts: `TRUE / True / true / T / t`

### 6. Concatenate and remember string
Useful to remember a value across the various runs. It accepts a boolean to reset the string, otherwise it always concatenate.

### 7. Image to true
Very simple node that everytime it receive an image, output a true boolean.

## Citations
[ComfyUI - Inspire Pack](https://github.com/ltdrdata/ComfyUI-Inspire-Pack)