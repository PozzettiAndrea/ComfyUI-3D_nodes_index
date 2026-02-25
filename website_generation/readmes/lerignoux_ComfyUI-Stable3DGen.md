# ComfyUI-Stable3DGen
A ComfyUI custom node to generate 3D assets using [Stable3D](https://github.com/Stable-X/Stable3DGen)

## Setup:
Copy the node in your ComfyUI/custom_nodes directory
```
git clone
```
install the dependencies:
```
python -m pip install -r requirements.txt
```
load the example workflow

## Stable3DGen update
Stable3DGen is included as a subtree in the project.
To update it you can run:
```
git subtree pull -P Stable3DGen git@github.com:Stable-X/Stable3DGen.git main --squash
```

## Contribution:
Open Source contribution and bug reports are welcome.
Please follow the standard open source contribution process.

## Thanks
* ComfyUI Team
* Stable-X team
