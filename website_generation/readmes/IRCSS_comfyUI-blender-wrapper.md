# ComfyUI Blender Wrapper

**ComfyUI Blender Wrapper** lets you call Blender in headless mode from ComfyUI (or any Python environment), run reusable pipeline stages stored inside `.blend` files, and pass configs in/out via JSON. It’s meant for tech-art / asset-pipeline tasks like cleanup, decimation, unwrap, baking, rigging, etc.

## What this repo gives you

- A **generic `wrapper.py`** that:
  - reads env vars from a caller,
  - imports input assets into Blender,
  - loads a `.blend` stage file,
  - executes scripts stored as **Text blocks** inside that `.blend`,
  - returns results via JSON.
- A **ComfyUI node** example showing how to call the wrapper.
- Example stage `.blend` files (e.g., mesh cleanup, simple rig, etc.) you can copy and modify.
- Some modifications to Kijai's Hunyuan wrapper, so that it plays nicely with my example of batch processing meshes (dealing with Windows Path issues and generations colliding with eachother in terms of file read write permissions)

## Why this exists

Blender already has a ridiculous amount of built-in functionality (mesh ops, baking, UVs, geo nodes, rigging, rendering…). Instead of re-implementing pipelines in your engine or custom tools, you can:

**Caller → Blender headless → wrapper.py → stage.blend scripts**

Write the actual stage logic once (inside a `.blend`), reuse it anywhere.

## Requirements

- Tested on Blender 4.5, but should work on most
- Python 3.9+ (same environment as ComfyUI if you use the node)

## Installation

1. Clone this repo in your Comfy Custome Nodes folder.
2. Make sure Blender is installed and set the path to the exe file in the blender_tools_config.json. Alternatively you can modify my code to get the path from system env variables and set it there.

3. Restart ComfyUI

## How to use it
You can call the generic wrapper like this: 

![screenshot](documentation/example.jpg)

Blend file is the path to whatever blend file should be used to run the stage, Input model is path to the model the wrapper imports for blender to act on, config file is a path to a json file that holds a dic of balancing paramters. This is only if your pipeline stage blend file needs it, if not you can leave it empty. Whether the stage needs it is up to whoever implements the code in the blend file. FBX path is where the model is exported once blender is done and the output config is a way to allow the person implementing the pipeline stage to talk up to the next node in comfy. 

For more in depth explaination of how everything works, read this post: https://medium.com/@shahriyarshahrabi/blender-as-a-pipeline-engine-make-rigged-characters-with-comfyui-3a1e81a3e623

## How to write your own stage
If you are interested in writing your stage, you can look at the mesh clean up blend file and simple rig file I provided as examples in the repo. Here is all you need to know:
1. Best would be to have one python text file in the Blend file named Main
2. The wrapper will import whatever is passed on to it in a collection called INPUT. In your Python code you can get all the objects in that collection to know what mesh to act on
3. The wrapper has passed down some info for you from Comfy. The important ones are input_model (path to the model imported, in case you want to export something next to it), blend_file, path to the blend file being called, and config itself. To get access to these properties, your blend file you need to do: 

``` blend_file      = globals().get("blend_file", None) ```

The config itself is already loaded into a Blender friendly dic. To accesss what is inside you can easily do:
```  
if config and isinstance(config, dict):
    if "decimate_ratio" in config:
        try:
            DECIMATE_RATIO = float(config["decimate_ratio"])
            log(f"Decimate ratio overridden by config: {DECIMATE_RATIO}")
        except Exception as e:
            log(f"Warning: invalid decimate_ratio in config ({config['decimate_ratio']}): {e}") 
```

You can also get a reference to output json and populate it like this: 

```  OUTPUT_JSON     = os.getenv("OUTPUT_JSON") ``` 

For how your json should look like have a look at the example. 

## On the Example Provided
The example provided is for generating 3D rigged characters. You can read the blog post for more info. I did modify Kijais wrapper to play nicely with very annoying windows issues. The changes are in the files ```ComfyUI-Hunyuan3DWrapper\nodes.py``` and ``ComfyUI-Hunyuan3DWrapper\hy3dgen\shapegen\postprocessors.py``. You will find both files included here, you can copy them over if you are hitting issues with permission for read and write. License wise all rights go to Kijai. 
