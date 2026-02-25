# ComfyUI Image to Video Inserter

動画に画像を挿入するComfyUIカスタムノード

<img width="1652" height="1010" alt="image" src="https://github.com/user-attachments/assets/953c5794-40af-4b71-bc56-7b5dc157219a" />

## 出力

https://github.com/user-attachments/assets/ee8c115f-81fc-4299-af9a-1381d90b1e4a

## ComfyUIへの導入

1. ComfyUIの `custom_nodes` フォルダにこのプロジェクトをクローン
2. ComfyUIを再起動
3. ノードメニューから以下のノードが利用可能:
   - `Create Blank Frames`: 空白フレーム作成
   - `Image Batch Assembler`: 複数画像の収集・整列・積層
   - `Multi Image Inserter`: 複数画像の挿入

## ノード詳細

### Create Blank Frames
- **機能**: 指定したサイズと色で空白フレームを作成
- **入力**: width, height, frame_count, color_r, color_g, color_b
- **出力**: 空白フレーム画像

### Image Batch Assembler
- **機能**: 複数の画像を選択・整理してリストまたはテンソル形式で出力
- **入力**: 
  - inputcount: 画像数を指定
  - output_type: 出力形式（"list" or "tensor"）
  - resize_mode: tensor 出力時の整形モード
    - pad: リサイズなしで中央パディング
    - fit_short_side: 目標サイズ内に収まるよう縮小（黒縁でレターボックス）
    - cover_fill: 目標サイズを覆うよう拡大（中央クロップで全体を埋める）
  - image_1, image_2, ... image_N: 動的に追加される画像入力
- **出力**: 選択された画像
- **使用方法**: inputcountを設定後、「Update inputs」ボタンで画像入力を動的に追加

### Multi Image Inserter  
- **機能**: 複数の画像を指定したフレーム位置に挿入
- **入力**:
  - frames: ベースとなるフレーム画像
  - images: 挿入する画像（Image Batch Assemblerから接続）
  - frame_indices: 挿入位置をカンマ区切りで指定（例："10,20,30"）
  - fade_width: フェード幅
  - min_opacity: 最小透明度
  - blend_mode: ブレンドモード
- **出力**: 処理済みフレーム画像

## スクリプト使用方法

### insert_image_to_video.py
```bash
python insert_image_to_video.py
```
動画フレーム処理のメイン機能を含むスクリプト

### test_multiple_images.py
```bash
python test_multiple_images.py
```
複数画像挿入のテスト・デモ用スクリプト
