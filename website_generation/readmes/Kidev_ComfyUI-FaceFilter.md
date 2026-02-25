# ComfyUI Face Filter

Two nodes for ComfyUI (face based filtering and batch merge).

## What you get

1) FaceFilter node (filter images by face similarity relative to reference images)
2) MergeImageBatches (merge two image batches index by index with simple rules)

## Install

You can install it directly from the manager.  

Otherwise, manually:
1) Install the node manually by going to `ComfyUI/custom_nodes/` and running `git clone git@github.com:Kidev/ComfyUI-FaceFilter.git`
2) Install Python deps: `pip install -r ComfyUI-FaceFilter/requirements.txt`

3) Models (InsightFace packs)
   * Default search paths (both are supported automatically)  
     * `~/.insightface/models` (home cache)  
     * `<this repo>/models/insightface` (local repo models)  
   * Example pack folder name `antelopev2`  
4) Restart ComfyUI  

#### Optional helper

```bash
python install.py
```

This only ensures the two model folders exist and prints where to drop packs.

## Nodes

### FaceFilter

#### Inputs

* `ref_images` (IMAGE) reference images that define the target identity set  
* `candidate_images` (IMAGE) images to test and filter  
* `threshold` (FLOAT) cosine similarity threshold (default `0.30`)  
* `on_empty_matching` (CHOICE) behavior when matching is empty (`black_512` or `return_empty` or `pass_through`)  
* `on_empty_rejected` (CHOICE) behavior when rejected is empty (same choices)  
* `debug` (BOOLEAN) return a debug string with counts and scores  
* `model_name` (CHOICE) an auto discovered InsightFace pack name (example `antelopev2`)  
* `providers` (CHOICE) `auto(cuda+cpu)` or `cpu_only`  
* `detector_size` (INT) face detector working size  
* `resize_mode` (CHOICE) `fit_min_side` or `fit_longest_side`  

#### Outputs

* `MATCHING` (IMAGE) batch of accepted candidates (faces matching one of the reference faces)  
* `REJECTED` (IMAGE) batch of rejected candidates  
* `DEBUG` (STRING) multi line diagnostics when enabled  

#### Behavior

* Embeddings are L2 normalized  
* Cosine similarity against the reference set  
* Accept if any ref is above `threshold`  
* Stable fallbacks keep downstream graphs valid when a batch is empty  

### MergeImageBatches

#### Inputs

* `batch1` (IMAGE)  
* `batch2` (IMAGE)  
* `prefer` (CHOICE) pick `batch1` or `batch2` when both look valid  

#### Output

* `MERGED` (IMAGE)  

#### Rule

* For each index pick the non black image if the other is black or empty  
* If both valid pick according to `prefer`  

## Examples

### Required nodes well installed to use the example workflows  
- [FaceFilter](https://github.com/Kidev/ComfyUI-FaceFilter) (of course)  
- [ReActor](https://github.com/Gourieff/ComfyUI-ReActor)  
- [Facetools](https://github.com/dchatel/comfyui_facetools)  
- [VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite) (only for video workflow)  

### A simple filter 

Workflow avaiable here: ([FaceFilter-simple.json](https://raw.githubusercontent.com/Kidev/ComfyUI-FaceFilter/refs/heads/main/examples/FaceFilter-simple.json))

A simple usage of the FaceFilter node: the images in the candidates that have pictures with the same face in the reference batch of images are passed to the matching group, the others to the rejected group.  
![FaceFilter-simple](https://raw.githubusercontent.com/Kidev/ComfyUI-FaceFilter/refs/heads/main/examples/FaceFilter-simple.png)

### Face matching faceswap using FaceFilter and [ReActor](https://github.com/Gourieff/comfyui-reactor)  

Workflow avaiable here: 
- Picture to picture: ([FaceFilter-Faceswap.json](https://raw.githubusercontent.com/Kidev/ComfyUI-FaceFilter/refs/heads/main/examples/FaceFilter-Faceswap.json))
- Video to video: ([FaceFilter-Faceswap-Video.json](https://raw.githubusercontent.com/Kidev/ComfyUI-FaceFilter/refs/heads/main/examples/FaceFilter-Faceswap-Video.json))

A simple faceswap tool that will swap the faces of particular persons with another. It does not uses indices or face position, only the face of the target using the FaceFilter node.  
![FaceFilter-Faceswap](https://raw.githubusercontent.com/Kidev/ComfyUI-FaceFilter/refs/heads/main/examples/FaceFilter-Faceswap.png)  

Here is a view of the most important blocks in the architecture:  
![FaceFilter-previews](https://raw.githubusercontent.com/Kidev/ComfyUI-FaceFilter/refs/heads/main/examples/FaceFilter-clean.png)  

Here is a simplified view for you to see the evolution of the image batches across all the nodes and understand the logic:  
![FaceFilter-previews](https://raw.githubusercontent.com/Kidev/ComfyUI-FaceFilter/refs/heads/main/examples/FaceFilter-previews.png)  

## Performance tips

* Use `providers=auto(cuda+cpu)` on machines with CUDA  
* `detector_size=256` is a good balance  
* Keep one model pack (example `antelopev2`) available in either supported path  
