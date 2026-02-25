# ComfyUI Random Resolution Selector

[ComfyUI](https://github.com/comfyanonymous/ComfyUI) 向けのカスタムノードです。
設定された基準解像度（Width/Height）をもとに、**「そのまま」「縦横入れ替え」「正方形」** の3つのパターンから解像度をランダム（または指定順）に決定して出力します。

同じプロンプトで「縦長・横長・正方形」の構図をまとめてテスト生成したい場合や、画角のバリエーションをランダムに持たせたい場合に便利です。

## インストール方法

`ComfyUI/custom_nodes/` ディレクトリに移動し、このリポジトリをクローンしてください。

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/fudosanit/ComfyUI-Random-Resolution.git