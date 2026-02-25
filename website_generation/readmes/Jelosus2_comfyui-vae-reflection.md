# ComfyUI VAE Reflection

A simple custom node and [SwarmUI](https://github.com/mcmonkeyprojects/SwarmUI) extension that modifies the padding mode of the conv layers of the VAE to use reflect mode. This is used to fix artifacts in the edges of the images that use a VAE trained with reflect padding.
<br/>
**Warning:** If the VAE in use wasn't trained with reflect padding the reflection mode can cause issues in the edges.
<br/>
<br/>
Here's a side to side comparison, if you can't see the difference try to zoom in the bottom left corner of both images and compare them.
![comparison](./images/comparison.png)
> Tested with [Anzhc's EQ VAE](https://huggingface.co/Anzhc/MS-LC-EQ-D-VR_VAE)

## Installation as custom node
Download it using the [ComfyUI Registry](https://registry.comfy.org/nodes/comfyui-vae-reflection).

### Manual Install
Clone the repository into the Comfy's `custom_nodes` directory with this command:
```
git clone https://github.com/Jelosus2/comfyui-vae-reflection
```
and restart ComfyUI.

You can integrate this node in your workflow very easily like shown in the picture below.
![workflow](./images/example_workflow.png)

## Installation as SwarmUI extension

1. Update SwarmUI to the latest version.
2. Go to Server -> Extensions tab.
3. Find `VAE Reflection` in the extension list and click Install.
4. Use the button at the top in the Extensions tab to reload SwarmUI.

### Manual Install
1. Update SwarmUI to the latest version.
2. If running, shutdown SwarmUI.
3. Open a terminal in `SwarmUI/src/Extensions`.
4. Clone the repository with `git clone https://github.com/Jelosus2/comfyui-vae-reflection`.
5. Run `launch-windows-dev.ps1` or `launch-linux-dev.sh` to recompile SwarmUI. Once it's done you can shutdown the dev version.
6. Launch SwarmUI and wait for the backend to finish loading.

### Updating
1. Update SwarmUI to the latest version.
2. Go to Server -> Extensions tab.
3. Click the Update button for the VAE Reflection extension.

Search for the VAE Reflection category in the paramaters list, if you don't see it you need to display the advanced options. To use the extension you only need to check the checkbox of the `Enable VAE Reflection` parameter.

![enable extension](./images/enable_extension.png)

## License

MIT License

Copyright (c) 2025 Jelosus1

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.