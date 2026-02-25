# ComfyUI-PoseKeypointsToImage

POSE_KEYPOINT（DWPose/OpenPose形式）からポーズ画像を描画する ComfyUI カスタムノードです。

[English](README_EN.md)

## 概要

DWPose や OpenPose の JSON 形式のキーポイントデータから、ポーズ画像（IMAGE）を生成するノードです。FaceKeypointsFilter で顔パーツをフィルタリングした後の pose_kps を渡すことで、特定のパーツを除外したポーズ画像を作成できます。

## インストール

### ComfyUI Manager を使用（推奨）

ComfyUI Manager で「PoseKeypointsToImage」を検索してインストール。

### 手動インストール

1. ComfyUI の `custom_nodes` フォルダに移動
2. このリポジトリをクローン:
   ```bash
   git clone https://github.com/smartvain/ComfyUI-PoseKeypointsToImage.git
   ```
3. ComfyUI を再起動

## 使い方

1. DWPose Preprocessor（または `POSE_KEYPOINT` を出力するノード）の出力をこのノードに接続
2. パラメータを設定:
   - `width` / `height`: 出力画像のサイズ（デフォルト: 512x512）
   - `point_radius`: キーポイントの描画半径（デフォルト: 2）
   - `draw_body`: ボディキーポイントを描画するか
   - `draw_face`: 顔キーポイントを描画するか
   - `draw_hands`: 手のキーポイントを描画するか
3. 出力を他のノードに接続

## ノードの場所

`Pose/Face Utils` > `Pose Keypoints → Image`

## 互換性

- `comfyui_controlnet_aux` の DWPose Preprocessor と連携
- OpenPose JSON フォーマットに対応

## ライセンス

MIT License
