# ComfyUI-Transceiver📡

Transceiver is a python library that swiftly exchanges fundamental data structures, specifically numpy arrays, between processes, optimizing AI inference tasks that utilize ComfyUI.

## Why?

When processing a large number of requests, the SaveImage and LoadImage nodes may be IO-limited, and using shared memory improves performance by passing images only through memory access, not through IO.

## Install as ComfyUI custom nodes

```bash
cd /path/to/ComfyUI
source venv/bin/activate
cd custom_nodes
git clone https://github.com/nat-chan/comfyui-transceiver
pip install -r requirements.txt
cd ../.. # cd /path/to/ComfyUI
python main.py # launch
```

## Custom Nodes

### Save Image Transceiver📡

save image to shared memory

**inputs**

- image: ImageTensor
- name: str

required name is shared memor identical name

### Load Image Transceiver📡

load image from shared memory

**inputs**

- name: str

required name is shared memor identical name
