# ComfyUI Video Extend Counter

A simple utility node that counts active Video S2V Extend nodes in your workflow and returns that number plus one. Now you don't have to remember to update the batch number. Just set your extend nodes and go. It was easy to forget so I made this quick and dirty.


<img width="971" height="799" alt="image" src="https://github.com/user-attachments/assets/f5faa256-7706-4cb8-a138-0906210f5710" />


## What it does

- Scans your workflow for active `Video S2V Extend` nodes
- Ignores bypassed nodes automatically  
- Returns the count + 1 (so 3 extend nodes = output of 4)
- Updates every execution - no caching issues
- Returns 1 if there are 0 extend nodes or all are bypassed

## Installation

### Method 1: Git Clone
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/yourusername/Urabewe-CountS2VExtend.git
```

### Method 2: Manual Download
1. Download this repository as ZIP
2. Extract to `ComfyUI/custom_nodes/Urabewe-CountS2VExtend/`
3. Restart ComfyUI

## Usage

1. Add the node and connect it directly to the "Value" of the "Batch Sizes" node.
2. Run your workflow and the batch count will update on each run


## Why +1?

The Wan 2.2 S2V model counts the sampler node plus all existing extend nodes. Number must be 1 or higher.

---

Built for native S2V workflows.
