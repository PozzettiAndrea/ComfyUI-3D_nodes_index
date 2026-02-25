# ComfyUI-TCD-Sampler
## 目录
- [ComfyUI-TCD-Sampler](#comfyui-tcd-sampler)
  - [目录](#目录)
  - [介绍](#介绍)
  - [安装](#安装)
    - [通过命令安装](#通过命令安装)
    - [通过 ComfyUI-Manager 安装](#通过-comfyui-manager-安装)
    - [通过绘世启动器安装](#通过绘世启动器安装)
  - [使用](#使用)


## 介绍
一个为 [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 添加 TCD 采样算法的扩展，算法来源：[dfl/comfyui-tcd-scheduler](https://github.com/dfl/comfyui-tcd-scheduler)。

## 安装
### 通过命令安装

进入 ComfyUI 的 custom_nodes 目录
```bash
cd custom_nodes
```

使用 Git 命令下载该扩展
```bash
git clone https://github.com/licyk/ComfyUI-TCD-Sampler
```

### 通过 ComfyUI-Manager 安装
进入 ComfyUI 界面后，进入 ComfyUI-Manager，在 ComfyUI-Manager 界面点击`通过 Git URL 安装`，将下方的链接填入输入框
```
https://github.com/licyk/ComfyUI-TCD-Sampler
```
点击`确定`下载该扩展

### 通过绘世启动器安装
打开绘世启动器，点击`版本管理`->`安装新扩展`，在下方的`扩展 URL`输入框填入下方的链接
```
https://github.com/licyk/ComfyUI-TCD-Sampler
```
点击输入框右侧的`安装`下载该扩展

## 使用
扩展安装完成后，可在 ComfyUI K采样器的`采样器`中看到 TCD 采样算法，选中后即可使用
