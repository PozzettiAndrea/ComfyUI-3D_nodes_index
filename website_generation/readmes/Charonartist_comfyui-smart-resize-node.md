# ComfyUI Smart Resize Node

ComfyUIのカスタムノードで、短辺・長辺を指定して画像を自動的にリサイズまたはクロップできます。

## 機能

- **スマートリサイズ**: 縦長・横長に関係なく、短辺と長辺の値を指定するだけで適切にリサイズ
- **リサイズモード**: 
  - `resize`: アスペクト比を維持してリサイズ後、不足部分を黒で埋める
  - `crop`: アスペクト比を維持してリサイズ後、指定サイズにクロップ
- **クロップ位置指定**: center, top, bottom, left, right から選択可能

## インストール

1. ComfyUIの`custom_nodes`フォルダ内にこのフォルダを配置
2. ComfyUIを再起動

## 使用方法

1. ノードメニューから `image/resize` → `Smart Resize (Short/Long Side)` を選択
2. パラメータを設定:
   - `short_side`: 短辺のサイズ（デフォルト: 512）
   - `long_side`: 長辺のサイズ（デフォルト: 768）
   - `method`: リサイズ方法（resize または crop）
   - `crop_position`: クロップ位置（centerなど）

## 例

- 縦長画像（600x900）→ short_side=512, long_side=768 → 512x768
- 横長画像（900x600）→ short_side=512, long_side=768 → 768x512

数値を変更せずに縦長・横長両方に対応できるのが特徴です。