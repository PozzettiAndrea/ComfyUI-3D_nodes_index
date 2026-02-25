

# ComfyUI-TorchMonitor

A fixed-position real-time CPU / RAM / VRAM / GPU-temperature monitor for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).

Zero-config, zero-console-spam, single-file install.

![demo](demo.png)


## Install

1. Clone this repo into `custom_nodes`:
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/love530love/ComfyUI-TorchMonitor.git
cd ComfyUI-TorchMonitor
pip install --no-deps -r requirements.txt
```

2. Restart ComfyUI – a green monitor bar appears before the AITechLab button.

Requirements
- `psutil` (auto-installed by ComfyUI)
- `nvidia-smi` in PATH (for GPU data)

Uninstall
Delete the folder and restart ComfyUI.

Directory Structure

```
ComfyUI-TorchMonitor/
├── __init__.py          # Main Python script
├── README.md            # This file
├── requirements.txt     # Optional: list dependencies
├── web/
│   └── torch_monitor.js # Frontend script
└── __pycache__/         # Python cache files
```

License
MIT


## 安装方式补充说明
1. ComfyUI-Manager 搜索 `torchmonitor` 一键安装  
2. 或 `git clone` 到 `custom_nodes` 后重启 ComfyUI
3. 或 `pip install comfy-cli` 后运行 `comfy node install torchmonitor` 后重启 ComfyUI
```
pip install comfy-cli
comfy node install torchmonitor
```
