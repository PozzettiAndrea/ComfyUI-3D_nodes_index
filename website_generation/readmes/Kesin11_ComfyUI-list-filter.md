# ComfyUI-list-filter
https://registry.comfy.org/nodes/comfyui-list-filter

Custom nodes for convenient filtering image or string lists in ComfyUI workflow.

Motivation: By using [ComfyUI-Image-Selector](https://github.com/SLAPaper/ComfyUI-Image-Selector) in ComfyUI, it is possible to create a workflow that selects images and performs additional processing. However, the `selected_indexes` obtained in this process are strings, which cannot be directly connected to nodes that require indices. ComfyUI-list-filter was created to facilitate the creation of such complex workflows.

ComfyUI-list-filter provides nodes that convert string indices to integer lists and retrieve elements from string or image lists based on specified indices. Additionally, when combined with [ComfyUI-WD14-Tagger](https://github.com/pythongosssss/ComfyUI-WD14-Tagger), ComfyUI-list-filter provides nodes that are useful for extracting lists of images with specified tags from tagged image lists.

More generally, ComfyUI-list-filter provides convenient nodes for filtering lists in ComfyUI workflow.

## Example
![example](https://github.com/user-attachments/assets/b1485023-5d95-485a-9239-620784a05d74)

The sample workflow is in the [example](./example/) directory.

## Custom nodes
- `Index List From String` - Splits a string into a list of indices based on the provided delimiter.
- `Filter String List` - Filters the string list based on the provided index list.
- `Filter Image List` - Filters the image list based on the provided index list.
- `Find Any Strings` - Checks if any of the search strings are present in the string list and return indices.
- `Find Not Any Strings` - Checks if none of the search strings are present in the string list and return indices.
- `Random Normal Distribution` - Generates random samples float list from a normal distribution.

## Changelogs
See [GitHub Releases](https://github.com/Kesin11/ComfyUI-list-filter/releases).
