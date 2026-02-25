[English](#English) | [日本語](#日本語)

---
# English

# ComfyUI nodes to use [MMAudio](https://github.com/hkchengrex/MMAudio)

## WIP WIP WIP

https://github.com/user-attachments/assets/9515c0f6-cc5d-4dfe-a642-f841a1a2dba5

## About this custom node

This is a custom node that applies the pull request (pr52) fixing bugs in ComfyUI-MMAudio and adds pitch adjustment functionality.<br>
The pitch adjustment feature integrates [comfyui-audio-pitch](https://github.com/Takenoko3333/comfyui-audio-pitch).<br>
This makes MMAudio easier to implement and is expected to improve performance.<br>
We plan to add features like Bass/Treble adjustment in the future.

## Installation
Navigate to ComfyUI\custom_nodes
```
git clone https://github.com/Takenoko3333/ComfyUI-MMAudio-Suite.git
```
Please restart ComfyUI.

If dependency files are not installed in the portable version: Please run the following within the ComfyUI_windows_portable folder:
```
python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-MMAudio-Suite\requirements.txt
```

## Models

Models are loaded from `ComfyUI/models/mmaudio`

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 mmaudio/
│   │   ├── 📂 nvidia/
│   │   │   └── 📂bigvgan_v2_44khz_128band_512x
│   │   ├── apple_DFN5B-CLIP-ViT-H-14-384_fp16.safetensors
│   │   ├── mmaudio_large_44k_v2_fp16.safetensors
│   │   ├── mmaudio_synchformer_fp16.safetensors
│   │   └── mmaudio_vae_44k_fp16.safetensors
```

Download the fp16 safetensors model from the following link:
Safetensors available here:

[https://huggingface.co/Kijai/MMAudio_safetensors/tree/main](https://huggingface.co/Kijai/MMAudio_safetensors/tree/main)

Nvidia bigvganv2 (used with 44k mode)

is autodownloaded to `ComfyUI/models/mmaudio/nvidia/bigvgan_v2_44khz_128band_512x`

The first time takes longer because Nvidia files are downloaded.

If it does not download automatically, please download it from the link below and place it.

[https://huggingface.co/nvidia/bigvgan_v2_44khz_128band_512x](https://huggingface.co/nvidia/bigvgan_v2_44khz_128band_512x)

## Update

- 2025-12-15 Registered in the ComfyUI Registry
- 2025-11-09 Applied pull request (pr52) to fix bugs in ComfyUI-MMAudio and integrated pitch adjustment functionality

---
# 日本語

# ComfyUI nodes to use [MMAudio](https://github.com/hkchengrex/MMAudio)

## WIP WIP WIP

https://github.com/user-attachments/assets/9515c0f6-cc5d-4dfe-a642-f841a1a2dba5

## このカスタムノードについて

ComfyUI-MMAudioのバグを修正するプルリクエスト（pr52）を適用し、ピッチ調整機能を加えたカスタムノードです。<br>
ピッチ調整機能は[comfyui-audio-pitch](https://github.com/Takenoko3333/comfyui-audio-pitch)を統合しました。<br>
これによりMMAudioの導入がし易くなり、性能向上も期待できます。<br>
今後、Bass/Treble調整等の機能を追加していく予定です。

## インストール

ComfyUI\custom_nodes に移動
```
git clone https://github.com/Takenoko3333/ComfyUI-MMAudio-Suite.git
```
ComfyUI を再起動してください。

ポータブル版で依存ファイルがインストールされていない場合：ComfyUI_windows_portableフォルダ内で以下を実行してください：
```
python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-MMAudio-Suite\requirements.txt
```

## モデル

モデルは以下に配置します `ComfyUI/models/mmaudio`

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 mmaudio/
│   │   ├── 📂 nvidia/
│   │   │   └── 📂bigvgan_v2_44khz_128band_512x
│   │   ├── apple_DFN5B-CLIP-ViT-H-14-384_fp16.safetensors
│   │   ├── mmaudio_large_44k_v2_fp16.safetensors
│   │   ├── mmaudio_synchformer_fp16.safetensors
│   │   └── mmaudio_vae_44k_fp16.safetensors
```

Safetensorsは以下よりfp16をダウンロードしてください:

[https://huggingface.co/Kijai/MMAudio_safetensors/tree/main](https://huggingface.co/Kijai/MMAudio_safetensors/tree/main)

Nvidia bigvganv2 (used with 44k mode):

自動的にダウンロードされます `ComfyUI/models/mmaudio/nvidia/bigvgan_v2_44khz_128band_512x`

初回はNvidiaのファイルがダウロードされるため時間がかかります。

自動的にダウンロードされない場合は以下よりダウンロードし配置してください。

[https://huggingface.co/nvidia/bigvgan_v2_44khz_128band_512x](https://huggingface.co/nvidia/bigvgan_v2_44khz_128band_512x)

## 更新履歴

- 2025-12-15 ComfyUI Registryに登録
- 2025-11-09 ComfyUI-MMAudioのバグを修正するプルリクエスト（pr52）を適用し、ピッチ調整機能を統合
