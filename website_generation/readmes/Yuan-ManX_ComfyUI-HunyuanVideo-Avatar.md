# ComfyUI-HunyuanVideo-Avatar

ComfyUI-HunyuanVideo-Avatar is now available in ComfyUI, [HunyuanVideo-Avatar](https://github.com/Tencent-Hunyuan/HunyuanVideo-Avatar) is a multimodal diffusion transformer (MM-DiT)-based model capable of simultaneously generating dynamic, emotion-controllable, and multi-character dialogue videos. 


## Installation

1. Make sure you have ComfyUI installed

2. Clone this repository into your ComfyUI's custom_nodes directory:
```
cd ComfyUI/custom_nodes
git clone https://github.com/Yuan-ManX/ComfyUI-HunyuanVideo-Avatar.git
```

3. Install dependencies:
```
cd ComfyUI-HunyuanVideo-Avatar
pip install -r requirements.txt
```

### Installation Guide for Linux

We recommend CUDA versions 12.4 or 11.8 for the manual installation.

Conda's installation instructions are available [here](https://docs.anaconda.com/free/miniconda/index.html).

```shell

# Install PyTorch and other dependencies using conda
# For CUDA 11.8
conda install pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 pytorch-cuda=11.8 -c pytorch -c nvidia
# For CUDA 12.4
conda install pytorch==2.4.0 torchvision==0.19.0 torchaudio==2.4.0 pytorch-cuda=12.4 -c pytorch -c nvidia

# Install pip dependencies
python -m pip install -r requirements.txt

# Install flash attention v2 for acceleration (requires CUDA 11.8 or above)
python -m pip install ninja
python -m pip install git+https://github.com/Dao-AILab/flash-attention.git@v2.6.3
```

In case of running into float point exception(core dump) on the specific GPU type, you may try the following solutions:

```shell
# Option 1: Making sure you have installed CUDA 12.4, CUBLAS>=12.4.5.8, and CUDNN>=9.00 (or simply using our CUDA 12 docker image).
pip install nvidia-cublas-cu12==12.4.5.8
export LD_LIBRARY_PATH=/opt/conda/lib/python3.8/site-packages/nvidia/cublas/lib/

# Option 2: Forcing to explicitly use the CUDA 11.8 compiled version of Pytorch and all the other packages
pip uninstall -r requirements.txt  # uninstall all packages
pip install torch==2.4.0 --index-url https://download.pytorch.org/whl/cu118
pip install -r requirements.txt
pip install ninja
pip install git+https://github.com/Dao-AILab/flash-attention.git@v2.6.3
```

Additionally, you can also use HunyuanVideo Docker image. Use the following command to pull and run the docker image.

```shell
# For CUDA 12.4 (updated to avoid float point exception)
docker pull hunyuanvideo/hunyuanvideo:cuda_12
docker run -itd --gpus all --init --net=host --uts=host --ipc=host --name hunyuanvideo --security-opt=seccomp=unconfined --ulimit=stack=67108864 --ulimit=memlock=-1 --privileged hunyuanvideo/hunyuanvideo:cuda_12
pip install gradio==3.39.0 diffusers==0.33.0 transformers==4.41.2

# For CUDA 11.8
docker pull hunyuanvideo/hunyuanvideo:cuda_11
docker run -itd --gpus all --init --net=host --uts=host --ipc=host --name hunyuanvideo --security-opt=seccomp=unconfined --ulimit=stack=67108864 --ulimit=memlock=-1 --privileged hunyuanvideo/hunyuanvideo:cuda_11
pip install gradio==3.39.0 diffusers==0.33.0 transformers==4.41.2
```




## Model

### Download Pretrained Models

HunyuanVideo-Avatar Pretrained [Models](https://huggingface.co/tencent/HunyuanVideo-Avatar)

All models are stored in `ComfyUI/models/HunyuanVideo-Avatar/weights` by default, and the file structure is as follows

```shell
HunyuanVideo-Avatar
  ├──weights
  │  ├──ckpts
  │  │  ├──README.md
  │  │  ├──hunyuan-video-t2v-720p
  │  │  │  ├──transformers
  │  │  │  │  ├──mp_rank_00_model_states.pt
  │  │  │  │  ├──mp_rank_00_model_states_fp8.pt
  │  │  │  │  ├──mp_rank_00_model_states_fp8_map.pt
  │  │  │  ├──vae
  │  │  │  │  ├──pytorch_model.pt
  │  │  │  │  ├──config.json
  │  │  ├──llava_llama_image
  │  │  │  ├──model-00001-of-00004.safatensors
  │  │  │  ├──model-00002-of-00004.safatensors
  │  │  │  ├──model-00003-of-00004.safatensors
  │  │  │  ├──model-00004-of-00004.safatensors
  │  │  │  ├──...
  │  │  ├──text_encoder_2
  │  │  ├──whisper-tiny
  │  │  ├──det_align
  │  │  ├──...
```

### Download HunyuanVideo-Avatar model

To download the HunyuanCustom model, first install the huggingface-cli. (Detailed instructions are available [here](https://huggingface.co/docs/huggingface_hub/guides/cli).)

```shell
python -m pip install "huggingface_hub[cli]"
```

Then download the model using the following commands:

```shell
# Switch to the directory named 'HunyuanVideo-Avatar/weights'
cd HunyuanVideo-Avatar/weights
# Use the huggingface-cli tool to download HunyuanVideo-Avatar model in HunyuanVideo-Avatar/weights dir.
# The download time may vary from 10 minutes to 1 hour depending on network conditions.
huggingface-cli download tencent/HunyuanVideo-Avatar --local-dir ./
```


## Requirements

* An NVIDIA GPU with CUDA support is required. 
  * The model is tested on a machine with 8GPUs.
  * **Minimum**: The minimum GPU memory required is 24GB for 704px768px129f but very slow.
  * **Recommended**: We recommend using a GPU with 96GB of memory for better generation quality.
  * **Tips**: If OOM occurs when using GPU with 80GB of memory, try to reduce the image resolution. 
* Tested operating system: Linux

