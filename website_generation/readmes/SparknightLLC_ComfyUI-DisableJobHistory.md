# ComfyUI-DisableJobHistory

This is a simple extension for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that automatically removes an item from the job queue after the job is finished. No custom nodes are required.

### Installation

You can clone this repo into `comfyui/custom_nodes/ComfyUI-DisableJobHistory` or search for "Disable Job History" in the ComfyUI Manager.

### Rationale

> [!IMPORTANT]  
> Per [#1](https://github.com/SparknightLLC/ComfyUI-DisableJobHistory/issues/1), the Comfy Frontend team fixed the issue described below. This extension is still useful if you want to auto-clear your job history, but it may no longer provide performance gains for most users. Just make sure your Frontend is updated to v1.34.4 or newer!

When using large workflows (100+ nodes), I noticed that every time I queued up a job, there was a significant delay before start of execution. On the first run, the delay was 0.15s. By the 10th run, it was maybe 1s. It can quickly grow to 3 or 4 seconds, which is very annoying if you're trying to rapidly test prompts.

I don't know if this is a bug or intended behavior, but ComfyUI seems to parse the entire job history in some way at the outset of every job. (It's also worth mentioning that setting "Queue history size" to the minimum value in the Comfy frontend does *not* fix this.)

With this extension, I can use ComfyUI for hours on end and every task will start immediately. You may still experience some slowdown if your `temp` folder is massive, but that's another matter.
