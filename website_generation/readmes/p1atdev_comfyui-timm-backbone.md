# ComfyUI Timm Backbone Nodes

[English](#english) | [日本語](#japanese)

## English

### Overview

ComfyUI Timm Backbone Nodes is a custom node set that enables you to load and use pre-trained models from the [timm](https://github.com/huggingface/pytorch-image-models) library within ComfyUI workflows.

Since the output is provided as a `TENSOR` datatype, you can handle timm outputs by aligning with this when creating your own custom nodes.

### Features

Load timm models from Hugging Face Hub and encode images.

You can choose between two types of output: `pooler_output` and `hidden_state`. When selecting `hidden_state`, you can specify which layer to extract (final layer, second-to-last, etc.).

### Installation
1. Clone this repository into your ComfyUI `custom_nodes` directory:

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/p1atdev/comfyui-timm-backbone
```

2. Install required dependencies:

```bash
# Activate comfyui environment
cd comfyui-timm-backbone
pip install -r requirements.txt 
# or
pip install timm 
```

### Available Nodes

#### Timm Backbone Loader

Loads a pre-trained model from the timm library.

- Inputs:
  - `model`: Model name (e.g., `timm/vit_huge_patch14_clip_224.laion2b`)
- Outputs: 
  - `MODEL`: timm model

#### Timm Backbone Image Encode

Encodes images using the loaded model and extracts features.

- Inputs:
  - `model`: The loaded timm model
  - `image`: Input image to encode (requires preprocessing to match the model beforehand)
  - `feature_type`: `pooler_output` or `hidden_state`
  - `hidden_state_index`: Which layer to extract (only applies to `hidden_state`)
- Outputs:
  - `TENSOR`: `torch.Tensor` containing extracted features

#### Timm Embeds Print

A node that `print`s the shape and contents of input `torch.Tensor`. For debugging purposes.

- Inputs: 
  - tensor: `torch.Tensor` to `print`
- Outputs: None (prints to console)

---

## Japanese

### 概要

ComfyUI Timm Backbone Nodes は、[timm](https://github.com/huggingface/pytorch-image-models) ライブラリの事前学習済みモデルを ComfyUI ワークフロー内で読み込み、使用できるようにするカスタムノードセットです。

`TENSOR` の Datatype として出力されるので、自前でカスタムノードを作る時にこれに合わせると、`timm` の出力を扱えます。


### 機能

HuggingFace Hub 上の Timm モデルを読み込んで画像をエンコードできます。

出力を `poooler_output` と `hidden_state` の2種類から選択でき、`hidden_state` を選択した場合は、抽出する層を指定できます。(最終層、最後から2番目など)

### インストール
1. ComfyUI の `custom_nodes` ディレクトリにこのリポジトリをクローン:
 
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/p1atdev/comfyui-timm-backbone
```

2. 必要な依存関係をインストール:

```bash
# comfyui 環境をアクティベート
cd comfyui-timm-backbone
pip install -r requirements.txt 
# or
pip install timm 
```


### 利用可能なノード

#### Timm Backbone Loader

timmライブラリから事前学習済みモデルを読み込みます。

- Inputs:
  - `model`: モデル名（例：`timm/vit_huge_patch14_clip_224.laion2b`）
- Outputs: 
  - `MODEL`: timm モデル

#### Timm Backbone Image Encode

読み込まれたモデルを使用して画像をエンコードし、特徴を抽出します。

- Inputs:
  - `model`: 読み込まれた timm モデル
  - `image`: エンコードする入力画像 (事前にモデルごとに合うように前処理する必要がある)
  - `feature_type`: `pooler_output` または `hidden_state`
  - `hidden_state_index`: 抽出する層（`hidden_state` のみ適用）
- Outputs:
  - `TENSOR`: 抽出された特徴を含む `torch.Tensor`

#### Timm Embeds Print

入力された `torch.Tensor` の形状と中身を `print` するノード。デバッグ用。

- Inputs: 
  - tensor: `print` したい `torch.Tensor`
- Outputs: なし（コンソールに出力）
