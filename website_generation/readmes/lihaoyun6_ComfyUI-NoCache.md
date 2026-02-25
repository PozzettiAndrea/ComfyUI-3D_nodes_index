# ComfyUI-NoCache  
Ignore caching of any nodes in ComfyUI to save your RAM.  
**[[📃中文版](./README_zh.md)]**

## Installation  

#### Install the node:  
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/lihaoyun6/ComfyUI-NoCache.git
```

## Usage

#### Basic usage:  
- Add `@NC` (case-insensitive) to the title of the node where you want to ignore caching.  
- Add `@GC` (case-insensitive) to the title of the node where you want to free up your RAM.  

    > A `@GC` node must be located after a `@NC` node. The `@NC` node cannot clear its own RAM usage.

#### Advanced:
- When using the `@NC` label, you can append an index (e.g. `@NC#1`)  
- An indexed NC node will only be released when a GC node with the same index is encountered (e.g. `@NC#1` / `@GC#1`)  
- You can override the configuration by adding a `NoCache Config` node to the workflow

## Credits  
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) @comfyanonymous
