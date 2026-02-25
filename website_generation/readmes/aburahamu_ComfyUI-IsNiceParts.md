# ComfyUI-IsNiceParts
このカスタムノードは、受け取った画像から体の部位（今は手だけ）と骨格を検出し、良い部位であればTrueを出力します。
![スクリーンショット 2024-05-19 010552](https://github.com/aburahamu/ComfyUI-IsNiceParts/assets/166828042/5628b00c-ba7b-4b5d-b76a-6bd95328e431)


## インストール方法
* 以下のどちらかの手段を採用してください。
* モデルファイルを入手し、ComfyUI-IsNiceParts内の「models」フォルダに格納してください。
### ComfyUI Manager
1. ComfyUIを起動し、ComfyUI Managerを開く
2. 「Install Custom Nodes」をクリック
3. 「IsNice」を検索し、ComfyUI-IsNicePartsをインストールする
4. ComfyUIを再起動する
5. 完了です
### git clone
* venvを用いている前提で記載しています
1. このWEBページの上部にある緑色のボタン「<> Code」をクリックする
2. 表示されたURLをコピーする
3. ComfyUIのフォルダをコマンドプロンプトで開く
4. 下記コマンドでcustom_nodesのフォルダに移動する
`cd custom_nodes`
5. 下記コマンドを実行する
`git clone https://github.com/aburahamu/ComfyUI-IsNiceParts.git`
6. コマンドプロンプトを閉じる
7. ComfyUIのフォルダをコマンドプロンプトで開く
8. 仮想環境を有効にする
`.\venv\scripts\activate`
9. ComfyUI-IsNicePartsのフォルダに移動する
`cd custom_nodes\ComfyUI-IsNiceParts`
10. 必要なモジュールをインストールする
`pip install -r requirements.txt`
11. コマンドプロンプトを閉じる
12. ComfyUIが開いていれば再起動する
13. 完了です


## モデルファイルの入手と格納
* 下記3つのモデルファイルをダウンロードしmodelsフォルダに格納してください。
`ComfyUI\custom_nodes\ComfyUI-IsNiceParts\models`
* modelsフォルダが無い場合は作成してください。

### hand_yolov8n.pt
https://huggingface.co/Bingsu/adetailer/tree/main
* 「hand_yolov8n.pt」をダウンロードしてください。

### dw-ll_ucoco_384.onnx
### yolox_l.onnx
https://huggingface.co/yzd-v/DWPose/tree/main
* 「dw-ll_ucoco_384.onnx」と「yolox_l.onnx」をダウンロードしてください。

## 使い方
1. Add Node > IsNiceParts > NiceHand でノードを追加する
2. image にパスを接続する
3. 下記パラメータを設定する
* filename_plefix：保存される画像の接頭辞です。初期値は「IsNiceParts」です
* confidence：良い手かを判断する境界値を0～1で入力します。高いほど厳しくなります。初期値は0.9です。
4. Queue Promptを押して生成を開始します
5. 良い手であれば出力ノードの「bool」に「True」が出力されます。良い手でなければ「False」が出力されます。


## 著者
[aburahamu](https://twitter.com/aburahamu_aa)


## ライセンス
AGPL-3.0
