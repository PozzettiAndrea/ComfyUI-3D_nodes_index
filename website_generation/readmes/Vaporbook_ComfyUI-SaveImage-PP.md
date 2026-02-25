# ComfyUI-SaveImage-PP

This is a better version of the native SaveImage node in ComfyUI. It updates the default naming convention (using date conventions and model names), and in keeping with previous efforts on a better save node, allows for saving in different formats (png still default), as well as turning off metadata if desired (default is on).

Credit where credit due: not a fork, but definitely owes [ComfyUI-SaveImage-Plus](https://github.com/Goktug/comfyui-saveimage-plus/tree/main) much gratitude. 

## Installation

1. git clone repository into `ComfyUI\custom_nodes\`
```
git clone https://github.com/replace-this-with-your-github-repository-url.git
```

2. Go to `ComfyUI\custom_nodes\ComfyUI-Your-CustomNode-Name` and run
```
pip install -r requirements.txt
```

If you are using the portable version of ComfyUI, do this:
```
python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-Your-CustomNode-Name\requirements.txt
```

