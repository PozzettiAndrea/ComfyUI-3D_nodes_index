# ComfyUI-FaceKeypointsFilter

DWPose/OpenPose の出力から顔のキーポイントを選択的にフィルタリングする ComfyUI カスタムノードです。

[English](README_EN.md)

## 概要

OpenPose の 68点顔キーポイントから、特定の顔パーツ（あご・眉・目・鼻・口外周・口内周）を無効化できるノードです。ControlNet ワークフローで特定の顔の特徴を保持しながら、他の部分を無視したい場合に便利です。

## インストール

### ComfyUI Manager を使用（推奨）

ComfyUI Manager で「FaceKeypointsFilter」を検索してインストール。

### 手動インストール

1. ComfyUI の `custom_nodes` フォルダに移動
2. このリポジトリをクローン:
   ```bash
   git clone https://github.com/smartvain/ComfyUI-FaceKeypointsFilter.git
   ```
3. ComfyUI を再起動

## 使い方

1. DWPose Preprocessor（または `POSE_KEYPOINT` を出力するノード）の出力をこのノードに接続
2. **削除（無効化）したい**顔パーツを有効にする:
   - `remove_jaw`: あご輪郭（ポイント 0-16）
   - `remove_eyebrows`: 眉（ポイント 17-26）
   - `remove_eyes`: 目（ポイント 36-47）
   - `remove_nose`: 鼻（ポイント 27-35）
   - `remove_mouth_outer`: 口の外周（ポイント 48-59）
   - `remove_mouth_inner`: 口の内周（ポイント 60-67）
3. 出力を ControlNet Apply ノードに接続

## ノードの場所

`Pose/Face Utils` > `Face Keypoints Filter (OpenPose)`

## 互換性

- `comfyui_controlnet_aux` の DWPose Preprocessor と連携
- OpenPose JSON フォーマット（バージョン 1.3）に対応

## ライセンス

MIT License
