# ComfyUI-Bagel

ComfyUI-Bagel is now available in ComfyUI, [BAGEL](https://github.com/ByteDance-Seed/Bagel) is an open‑source multimodal foundation model with 7B active parameters (14B total) trained on large‑scale interleaved multimodal data.



## Installation

1. Make sure you have ComfyUI installed

2. Clone this repository into your ComfyUI's custom_nodes directory:
```
cd ComfyUI/custom_nodes
git clone https://github.com/Yuan-ManX/ComfyUI-Bagel.git
```

3. Install dependencies:
```
cd ComfyUI-Bagel
pip install -r requirements.txt
```


## Model

### Download pretrained checkpoint

```
from huggingface_hub import snapshot_download

save_dir = "/path/to/save/BAGEL-7B-MoT"
repo_id = "ByteDance-Seed/BAGEL-7B-MoT"
cache_dir = save_dir + "/cache"

snapshot_download(cache_dir=cache_dir,
  local_dir=save_dir,
  repo_id=repo_id,
  local_dir_use_symlinks=False,
  resume_download=True,
  allow_patterns=["*.json", "*.safetensors", "*.bin", "*.py", "*.md", "*.txt"],
)

```

### Or

```
# Clone model using git lfs (recommended)
git lfs install
git clone https://huggingface.co/ByteDance-Seed/BAGEL-7B-MoT models/bagel/BAGEL-7B-MoT

# Or use huggingface_hub
pip install huggingface_hub
python -c "from huggingface_hub import snapshot_download; snapshot_download(repo_id='ByteDance-Seed/BAGEL-7B-MoT', local_dir='models/bagel/BAGEL-7B-MoT')"
```
