# comfyui_my_img_util

ComfyUI 用の実験用のノードです。

# Nodes

## Image Resize And Crop

画像のサイズを変更する際に、アスペクト比を維持しながら、どこを中心として画像を切り落とすかを選択出来ます。

<img width="2435" height="1487" alt="image" src="https://github.com/user-attachments/assets/67b26190-7e23-42d1-a131-516867b674f0" />

## OpenCV Denoise (Luma/Chroma)

OpenCVの `fastNlMeansDenoisingColored` を利用して、画像のノイズを除去します。

特に高ISO感度の写真などで見られる「輝度ノイズ（ザラザラした粒子感）」と「色ノイズ（赤や緑の斑点）」を個別の強度で除去できるのが特徴です。ディテールを保持しつつ、色ノイズを強力に除去したい場合に有効です。

### Inputs
- `image`: (IMAGE) 処理対象の画像
- `h_luminance`: (FLOAT) 輝度ノイズの除去強度。値を大きくするとノイズがよく消えますが、ディテールが失われやすくなります（目安 1.5 ~ 2.5）
- `h_color`: (FLOAT) 色ノイズの除去強度。一般的に `h_luminance` より少し大きい値を設定します。
- `search_window`: (INT) 類似パッチを探索するウィンドウサイズ。大きいほど処理が重くなりますが、細かい部分までノイズが取れて品質が上がります。
- `template_window`: (INT) 類似性を計算するためのテンプレートパッチサイズ。

### Outputs
- `IMAGE`: (IMAGE) ノイズ除去後の画像

<img width="2238" height="1793" alt="image" src="https://github.com/user-attachments/assets/2a982667-3c08-4533-a8bb-92890cbc7786" />


## Simple Image Rotate

角度を指定して画像を回転します。はみ出した部分を調整するために、画像のサイズが変更されることがあります。

回転によって生じた隙間は、出力画像のアルファチャンネルで透明になります。

### Inputs
- `image`: (IMAGE) 回転させる画像。
- `angle`: (FLOAT) 回転角度。プラスの値で反時計回り、マイナスの値で時計回りに回転します。

### Outputs
- `image`: (IMAGE) 回転後の画像（RGBA）。
- `mask`: (IMAGE) 回転によって生じた隙間部分を白、元の画像部分を黒としたマスク画像。

![image](https://github.com/user-attachments/assets/6569dee8-f8e6-4bf8-8ee2-6b2fdfbb4100)

## Auto Image Selector

複数の画像入力の中から、設定されたランクに基づいて1つの画像を選択して出力します。

ワークフローの条件分岐などで、使用する画像ソースを自動的に切り替えたい場合に便利です。

### Inputs
- `image1` - `image4`: (IMAGE, optional) 選択候補の画像。
- `rank1` - `rank4`: (INT, optional) 各画像の優先順位。数値が小さいほど優先度が高くなります（最小値: 1）。
- `ng_image`: (IMAGE, optional) この画像と完全一致する入力は、選択候補から除外されます。

### Outputs
- `image`: (IMAGE) 選択された画像。
- `rank`: (INT) 選択された画像のランク。

![image](https://github.com/user-attachments/assets/eb658c74-02eb-4064-bce2-c5852e80358f)
