[中文](README-CN.md) | [English](README.md)

# HeyGem Digital Human Node for ComfyUI

Currently (2025.05.22) the best open-source digital human, bar none. Basically capable of generating full-body, dynamic, and arbitrary resolution digital humans. **The input video frame rate should be consistent with the synthesized frame rate.**

![image](https://github.com/billwuhao/Comfyui_HeyGem/blob/main/images/2025-05-22_22-41-52.png)

## 📣 Updates

[2025-05-25]⚒️: Fixed bugs, automatically capture long videos to match audio duration.

[2025-05-23]⚒️: Optimize CPU usage for long videos, allowing short videos to be repeated or pingPong to audio duration.

[2025-05-22]⚒️: Released v1.0.0.

## Node Installation

```
cd ComfyUI/custom_nodes
git clone https://github.com/billwuhao/Comfyui_HeyGem.git
```

## WSL and Docker Installation

- Windows (taking X64 as an example):

1, Install Windows Subsystem for Linux: https://github.com/microsoft/WSL/releases (`wsl.2.5.7.0.x64.msi`). If already installed, run `wsl --update` with administrator privileges to update.

2, Install Docker: https://www.docker.com/ (download `AMD64` version). After installation, start it:

![](https://github.com/duixcom/Duix.Heygem/raw/main/README.assets/8.png)
![](https://github.com/duixcom/Duix.Heygem/raw/main/README.assets/13.png)
![](https://github.com/duixcom/Duix.Heygem/raw/main/README.assets/3.png)

The image is downloaded to drive C by default **(requires about 14GB of space)**. You can change it to another drive in the settings:

![](https://github.com/duixcom/Duix.Heygem/raw/main/README.assets/7.png)

OK! You are ready. Start Docker before running the node each time. The first time you run the node, it needs to download the image, which takes about 30 minutes, depending on your network speed. The installation is not complicated; just click a few times to install the software. Docker is an isolated image environment, so you don't need to worry about compatibility issues, and it rarely reports errors, making it simpler than installing other plugins.

- Linux (taking Ubuntu as an example):

1, Install Docker: Run `docker --version` to check if it is installed. If not installed, run the following commands to install it.
```
sudo apt update
sudo apt install docker.io
sudo apt install docker-compose
```

2, Install Drivers: Run `nvidia-smi` to check if they are installed. If not installed, refer to the official documentation (https://www.nvidia.cn/drivers/lookup/) for installation.

3, Install NVIDIA Container Toolkit:
  - Add the NVIDIA package repository:
  ```
  distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
  && curl -s -L https://nvidia.github.io/libnvidia-container/gpgkey | sudo apt-key add - \
  && curl -s -L https://nvidia.github.io/libnvidia-container/$distribution/libnvidia-container.list | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
  ```

  - Install the NVIDIA Container Toolkit:
  ```
  sudo apt-get update
  sudo apt-get install -y nvidia-container-toolkit
  ```

  - Configure the NVIDIA container runtime:
  ```
  sudo nvidia-ctk runtime configure --runtime=docker
  ```

  - Restart the Docker daemon to apply changes:
  ```
  sudo systemctl restart docker
  ```

OK! You are ready. The first time you run the node, it needs to download the image, which takes about 30 minutes, depending on your network speed.

## Acknowledgements

- [Duix.Heygem](https://github.com/duixcom/Duix.Heygem)
- https://github.com/duixcom/Duix.Heygem/blob/main/LICENSE