# comfyui-better-flow 

Nodes for controlling workflow and reducing VRAM fingerprint.
All assembled for ComfyUI for the goal of making workflows easier and spare computing space. 

***progress***
- (Model Offload/Recall)
	- fixed for GGUF flux model by unpatching the model (ModelPatcher and GGUFModelPatcher)
      - overrides the patch_on_device property


***TODO: untested release***
- offload/recall not tested on low_vram and high_vram flags and other models besides flux
- evtl nunchaku support?
- Cache any cleanup not working


***TODO: add image use cases for each custom node***

## Custom Nodes

### Model offload/ Model recall

When triggered during runtime, it moves models on their load_device (e.g. cuda) or offload device(e.g. cpu).
For finer control of VRAM use.

Works for flux  via gguf model and .safetensor model, regardless of the low_vram flag (when calling ComfyUI) or the load_on_device property (from GGUFModelPatcher)
Nunchaku is unsupported/ignored since it mangages its own VRAM usage outside python.

![example offload and recall](./resources/offload_recall.png)

###  Any to Hash
returns a md5 hash for the input object.
Limitations:
- doesn't support None inputs
- Inconsistent with objects of type Tensor: Those can be located on RAM or VRAM, hence returning different values. In the case of an image, we migrate the image to CPU before calculating the Hash

###  Any to Hash x2
Same as any to Hash but combines two individual hashes.
It re-hashes the concatenation of the md5 hash of each input

###  Cache any
For caching/ignoring time consuming steps in a workflow.

This node saves new input into a .pkl file, referenced by
- a key name
- a hash calculated by its input
During the next execution, if a matching name+hash is found it will skip the heavy computing and return the pickled value instead.

> [!Tip ]Multiple inputs keys can be used when combined with "any to hash x2" (e.g. image + text)

```
Checks whether the name+key exists:
- NO: 
	- requests the any_to_cache input
	- write cache file
	- returns input
- YES:
	- ignores input
	- reads from cache file
	- returns from cached file
- Finally
	- deletes other cached files in the `output/cached_outputs` folder (todo: fix it)
```
![example cache any](./resources/cache_any.png)

Known issues:
- Tensor type objects seem to produce unreliable hashes. I put a fix for images but some data types must dealt with (e.g. Conditionnings)

### Experimental nodes (not even tested)

####  Wait
Stops the execution of the workflow until the trigger value has been executed. Due to lazy loading, this specific  node is deprioritized.

#### Wait Multi (experimental)
Wait multiple triggers at once, (dynamic number of input?: the node dynamically adds new inputs after new input connected)

#### Reroute Triggerable
Reroute that can be triggered using the advanced Mode>OnTrigger UI elements. It enables a leaf node such as "image preview" not not be a leaf anymore if connected.

## Install

Don't forget to remove the `comfyui-offload-models` (because it only works on the `.safetensor` models, and can be confusing).

### Via ComfyUI

Search for "comfyui-better-flow" in the available node, or paste the github repo link to install from it. 

### Manual Install
```sh
# Go to the custom nodes
cd ./ComfyUI/custom_nodes
# Install the repo
git clone https://github.com/lokinou/comfyui-better-flow.git
```

## versions
- 0.1.3
	- Model Offload/Recall
		- handling of failed Nunchaku import
- 0.1.2
	- Model Offload/Recall
		- fixed for GGUF flux model by unpatching the model (ModelPatcher and GGUFModelPatcher)
		- ModelPatcher: overrides the patch_on_device property
	- Hash, Cache Any: images now produce consistent hashes
- 0.1.1
    - bug fixes
- 0.1.0
    - initial release from all node
    - migrated here ([comfyui-offload-models 1.1.0](https://github.com/lokinou/comfyui-offload-models))