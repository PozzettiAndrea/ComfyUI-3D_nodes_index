# ComfyUI-color-ascii-art-node


png画像をカラーのアスキーアート化するカスタムノードです。

複数のフォントサイズを採用することで、濃淡の表現もある程度反映できるようになっています。

生成されるファイルの解像度は入力画像と同じになるように設定しています。

This is a custom node to convert png images into color ASCII art.

As noted below, multiple font sizes are used in the specification.

The resolution of the generated file is set to be the same as the input image.


## 修正歴

2025/4830　バッチ処理に対応しました。

2025/4/12　カスタムノードをv3のみにし、大幅に内容を修正しました。

2024/9/26　カスタムノードにシード値を追加しました。

2024/9/18　カスタムノードのデフォルト値を修正しました。

2024/9/5　カスタムノードにmaskの入力を追加しました。若干処理速度を上げるスクリプトを追加しました。

2024/9/3　カスタムノードの種類を3種類に追加しました。


## Installation

ComfyUIのカスタムノードディレクトリにインストールします。

Clone the repository and navigate to the project directory:

```bash
cd Yourdirectory/ComfyUI/custom_nodes
git clone https://github.com/Shiba-2-shiba/comfyui-color-ascii-art-node.git
cd comfyui-color-ascii-art-node
pip install -r requirements.txt

```

## Usage

![Example Workflow](https://github.com/Shiba-2-shiba/comfyui-color-ascii-art-node/blob/main/ref_image/img1.png)

「ASCIIARTNode v3」がノードに追加されます。

このノードは、「image」と「mask」の入力に対応し、カラーアスキー化した「Image」の出力を行います。

パラメーターを調整することで、出力画像を変えることが出来ます。


ASCIIARTNode v3” will be added to the node.

This node responds to “image” and “mask” inputs and outputs a color ASCII-ized “Image”.

The output image can be changed by adjusting the parameters.



## Parameters


![Example Workflow](https://github.com/Shiba-2-shiba/comfyui-color-ascii-art-node/blob/main/ref_image/img2.png)


①pixel size：ピクセル化するサイズの数値です。デフォルトは20にしています。これを小さくすると元画像に近いものになります。

②downscale_mode：ピクセル化に関連する方法です。デフォルトをareaにしています。

③aspect_ratio_correction：文字の重複が目立つ際にここの数値を大きくして調整します。

④font_name：fontフォルダ内にあるフォントファイルのリストから選択できます。デフォルトはChewy-Regular.ttfです。

⑤font_size_min：ここで設定したサイズが最も小さいフォントサイズとして採用されます。デフォルトは8です。

⑥font_size_max：ここで設定したサイズが最も大きいフォントサイズとして採用されます。デフォルトは16です。

⑦ascii_chars_filename：デフォルトはset4.txtです。set1-set5がありますが、文字に対応していないフォントを選択した場合は出力が白紙になります。

⑧char_selection_mode：文字の選択方法についてです。輝度や彩度などで文字が選択されます。luminance_hueがデフォルト。

⑨seed：文字の選択のランダム化を調整しています。

⑩sharpen_mode：unsharpが選択できます。

⑪brightness：画像の明るさの調整をします。基本は1.0です。色が薄いところを白くしたい場合はこの数値を上げます。

⑫contrast：画像のコントラストを上げます。デフォルトは1.0ですが、このみによって上げてください。

⑬mask_blend_radius：マスク画像を使用した際に調整できます。

⑭mask_edge_adjustment：マスク画像の辺縁部のフォントの調整です。

⑮mask_edge_factor：マスク画像を使用した際に調整できます。

⑯enable_color_match：これを「Enabled」にすることでカラーマッチを使用できます。

⑰color_match_method：いくつか選択可能です。リアル系やイラスト系で効果が変わります。「idt」は使用できません。

⑱log level：ログの出力を調整します。









