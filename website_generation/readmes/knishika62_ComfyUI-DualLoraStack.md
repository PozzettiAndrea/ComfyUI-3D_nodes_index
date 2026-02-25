# Knishika Dual Lora Stack

2つのモデルに同じLoraを適用し、CLIPを共有するComfyUIカスタムノードです。

## 機能

- **デュアルモデル対応**: 同じLora設定で2つのモデルを同時処理
- **CLIP共有**: 2つのモデル間で1つのCLIPを共有
- **複数Loraスタック**: 最大6つのLoraモデルを個別強度制御で対応
- **柔軟な設定**: 各Loraを個別に有効/無効化、強度調整可能

## インストール

### 方法1: ComfyUI Manager（推奨）
1. ComfyUI Managerがインストールされていない場合はインストール
2. ComfyUI Managerで「Knishika Dual Lora Stack」を検索
3. ノードをインストール

### 方法2: 手動インストール
1. このリポジトリをクローンまたはダウンロード
2. フォルダをComfyUIの`custom_nodes`ディレクトリにコピー:
   ```
   ComfyUI/custom_nodes/knishika-dual-lora-stack/
   ```
3. ComfyUIを再起動

## 使用方法

1. ワークフローに「Knishika Dual Lora Stack」ノードを追加
2. 2つのモデルを`model_1`と`model_2`入力に接続
3. CLIPを`clip`入力に接続
4. 最大6つのLoraモデルとそれぞれの強度を設定
5. ノードは2つの修正されたモデルと1つの共有CLIPを出力

## 入力

- `model_1` (MODEL): 第1モデル入力
- `model_2` (MODEL): 第2モデル入力
- `clip` (CLIP): 共有CLIP入力
- `lora_01`～`lora_06`: Loraモデル選択
- `lora_01_strength`～`lora_06_strength`: 強度値（-10.0～10.0）

## 出力

- `model_1` (MODEL): 第1修正モデル
- `model_2` (MODEL): 第2修正モデル
- `clip` (CLIP): 修正された共有CLIP

## ライセンス

このプロジェクトはMITライセンスでリリースされています。

## 作者

knishika