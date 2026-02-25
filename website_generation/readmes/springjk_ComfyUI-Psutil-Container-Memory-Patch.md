# ComfyUI Psutil Container Memory Patch

## Overview

This extension is designed to address the issue where ComfyUI, when running in a memory-limited container, fails to correctly detect the available memory size. 

ComfyUI and some of its nodes use the `psutil` library. Due to historical reasons, the `psutil.virtual_memory` function cannot accurately read the container's available and maximum memory limits—it instead retrieves the host machine's memory statistics. This discrepancy can lead to OOM (Out of Memory) errors in certain tasks.

## Solution
This extension detects whether ComfyUI is running inside a container, reads the container's memory limits, and applies a Monkey Patch to override specific return values of `psutil.virtual_memory`. Currently, it modifies the following memory metrics:
- **Total memory (`total`)**
- **Used memory (`used`)**
- **Available memory (`available`)**
- **Memory usage percentage (`percent`)**

By doing so, the memory statistics correctly reflect the container's actual limits rather than the host machine's resources.

## Benefits
With this extension:  
- ComfyUI and its nodes can make informed decisions based on accurate memory constraints.  
- OOM (Out of Memory) errors are effectively prevented in containerized environments.  
- Memory-related nodes (such as **crytools' Statistic Node**) now display correct usage information.  

``` bash
# Run ComfyUI in container with 10GB memory limit

# Before installing node, console displays:
python /root/ComfyUI/main.py

	ComfyUI starting ..
	Total VRAM 24210 MB, total RAM 102400 MB

# After installing node, console displays: 
python /root/ComfyUI/main.py

	ComfyUI starting ..
	Total VRAM 24210 MB, total RAM 10240 MB
```


## Install

1. Look up `Psutil Container Memory Patch` in ComfyUI-Manager. If you are installing manually, clone this repository under `ComfyUI/custom_nodes`.
1. Restart ComfyUI.

# Features

- Make comfyui  and other custom node get correct memory information in the container (psutil monkey path)



## See Also 
* https://fabiokung.com/2014/03/13/memory-inside-linux-containers/
*  [psutil reports memory stats about host instead of container sutil#2100](https://github.com/giampaolo/psutil/issues/2100)