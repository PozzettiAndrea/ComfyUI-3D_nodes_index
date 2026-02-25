# ComfyUI-reboot

This is a custom ComfyUI node to reboot (i.e. restart) ComfyUI at the end of a workflow. It does exactly the same thing as either of the following:

* hitting the **Restart** button in the ComfyUI Manager window, or
* right-clicking in an empty area and selecting **Reboot ComfyUI**

It is registered in the [Comfy Registry](https://registry.comfy.org/nodes/reboot).

### Why reboot?

This node was written to fix issues with some Apple MLX Flux model loaders. These loaders were super-quick compared with regular Flux loaders but failed to free the system memory on completion of the workflow. None of the usual utilities could clear the memory (_Manager -> Unload models_, _Manager -> Free model & node cache_ plus various custom nodes such as _EasyUse -> Clean VRAM_, _Unload Model_, and _Unload All Models_). Nothing worked, the memory was never freed.

So this is a solution of last resort. I use it in workflows when calling ComfyUI from Open WebUI to generate images. The automated ComfyUI reboot on completion of a workflow allows the system to reclaim the memory without having to manually reboot the ComfyUI server after each image generation.

### Installation

If you have [comfy-cli](https://github.com/Comfy-Org/comfy-cli) installed then you can run `comfy node install reboot`.

Alternatively, use `git` thus:
* `cd /path/to/ComfyUI`
* `cd custom_nodes`
* `git clone https://github.com/bobosola/ComfyUI-reboot.git`
* Restart ComfyUI

### Usage
You should then find **Reboot ComfyUI** in the **utils** folder of the nodes menu. Alternatively, you can double-click in an empty area of the workspace and enter _reboot_ into the node search box.

Place it at end of your workflow attached to the output of any node. If your final node has no output to attach to, then attach it to the node nearest to the end which does have an output connector. You must then set the delay period accordingly to allow enough time for your workflow to complete before the reboot.

The example shown below is near end of a workflow:

![How to use the Reboot node](https://raw.githubusercontent.com/bobosola/ComfyUI-reboot/refs/heads/main/assets/Screenshot01.png)

### Parameters

Adjust these according to your needs:
* `server_url` (_string_) - the ComfyUI server URL in the standard format `{scheme}://{host}:{port}`. Default is the local server and standard ComfyUI port (`http://127.0.0.1:8188`).
* `wait_seconds` (_integer_) - the number of seconds to wait until ComfyUI reboots. Default is 5 seconds.

### Acknowledgements

This is based on watarika's [ComfyUI-exit](https://github.com/watarika/ComfyUI-exit). I just amended it for my purpose. So many thanks to him for leading the way.

### Change Log
- v1.0.0 (07-Oct-2025) - first release.
- v1.0.1 (07-Oct-2025) - fix broken logo for Comfy Registry
