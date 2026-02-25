
# *Node* - Size Matcher

Takes two images or masks and matches their sizes using various methods, detailed below. Inlcudes a node to smart-composite (auto match sizes first then composite)

## cover_crop_center

> Expand the smaller image to cover the larger image without changing the aspect ratio. Then center it. Then crop any overflowing edges until sizes match.
> 
> <details>
> <summary> &nbsp; Expand </summary>
>
> 
> ![alt text](https://github.com/christian-byrne/size-match-compositing-nodes/blob/demo-files/wiki/demo/size-match/cover-crop-center.png?raw=true)
>
> </details>

## cover_crop

> Same as `cover_crop_center` but without centering the smaller after resizing.
>
> 
> <details>
> <summary>&nbsp; Expand </summary>
>
> 
> ![alt text](https://github.com/christian-byrne/size-match-compositing-nodes/blob/demo-files/wiki/demo/size-match/cover-crop.png?raw=true)
>
> </details>

## fit_center

> Expand the smaller image as much as possible to fit inside the larger image without changing the aspect ratio. Then center it. Then pad any remaining space until sizes match.
>
> 
> <details>
> <summary>&nbsp; Expand </summary>
>
> 
> ![alt text](https://github.com/christian-byrne/size-match-compositing-nodes/blob/demo-files/wiki/demo/size-match/fit-center.png?raw=true)
>
> </details>

## center_dont_resize

> Center the smaller image inside the larger image without changing either sizes. Then pad the smaller image until sizes match.
>
> 
> <details>
> <summary>&nbsp; Expand </summary>
>
> 
> ![alt text](https://github.com/christian-byrne/size-match-compositing-nodes/blob/demo-files/wiki/demo/size-match/center-dont-resize.png?raw=true)
>
> </details>

## fill

> Expand the smaller image to exactly match the size of the larger image, allowing the aspect ratio to change
>
> 
> <details>
> <summary>&nbsp; Expand </summary>
>
> 
> ![alt text](https://github.com/christian-byrne/size-match-compositing-nodes/blob/demo-files/wiki/demo/size-match/fill.png?raw=true)
>
> </details>

## crop_larger_center

> Center the smaller image on the larger image. Then crop the larger image to match the size of the smaller image
>
> 
> <details>
> <summary>&nbsp; Expand </summary>
>
> 
> ![alt text](https://github.com/christian-byrne/size-match-compositing-nodes/blob/demo-files/wiki/demo/size-match/crop-larger-center.png?raw=true)
>
> </details>

## crop_larger_topleft

> Same as `crop_larger_center` but crops the larger image from the top left corner (skip centering)
> 
> <details>
> <summary>&nbsp; Expand </summary>
>
> 
>
> ![alt text](https://github.com/christian-byrne/size-match-compositing-nodes/blob/demo-files/wiki/demo/size-match/crop-larger-topleft.png?raw=true)
>
> </details>
>

&nbsp;

# *Node* - Paste Cutout on Base Image (Compositing)

- Composites two images together
- Automatically matches size of the images with various size matching methods (if necessary)
- If the cutout doesn't have an alpha channel (not really a cutout), the bg is automatically inferred and made transparent
- `invert` option



## Base Layer Composite with Alpha Layer

> 
> <details>
> <summary>&nbsp; Expand </summary>
>
> 
> ![paste-cutout](https://github.com/christian-byrne/size-match-compositing-nodes/blob/demo-files/wiki/demo/composite/paste-cutout.png?raw=true)
>
> </details>


## BG Being Inferred when Alpha Layer is Missing



> 
> <details>
> <summary>&nbsp; Expand </summary>
>
> 
>
> ![inferred-bg](https://github.com/christian-byrne/size-match-compositing-nodes/blob/demo-files/wiki/demo/composite/inferred-bg.png?raw=true)
> 
>
> </details>

## Using with Auto Segmentation

> 
> <details>
> <summary>&nbsp; Expand </summary>
>
> 
>
> ![with-auto-segmentation](https://github.com/christian-byrne/size-match-compositing-nodes/blob/demo-files/wiki/demo/composite/with-auto-segmentation.png?raw=true)
>
>
> </details>


## With Chromakeying

> 
> <details>
> <summary>&nbsp; Expand </summary>
>
> 
> 
> ![with-chromakeying](https://github.com/christian-byrne/size-match-compositing-nodes/blob/demo-files/wiki/demo/composite/with-chromakeying.png?raw=true)
>
>
> </details>


# Installation

1. `cd` into `ComfyUI/custom_nodes`
2. `git clone` this repo

# Requirements

- Python3.10+