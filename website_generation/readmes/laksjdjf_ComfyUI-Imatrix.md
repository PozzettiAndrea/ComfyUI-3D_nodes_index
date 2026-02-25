# ComfyUI-Imatrix

[ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF)で利用するGGUFファイルの量子化誤差を小さくするための、imatrixファイルを作るための実験的ノードです。

↓Flux-dev Q2_Kでの実験

モデルは[ここ](https://huggingface.co/furusu/experimental-ggufs)においてます。
![ああ](https://github.com/user-attachments/assets/33b2fca2-0b61-4e3e-82be-d3e4ec81e7ec)


# 使い方
+ MODELをImatrixUNETLoaderノードで読み込みます。
+ 何かしらのワークフローを実行します。
+ SaveImatrixノードでimatrixをセーブできます。
+ ファイルはこのフォルダのimatrix_dataに保存されます。

SaveImatrixノードにあるImage入力は実行順をコントロールするためのものであり使われませんが、
生成IMAGEをつけるといいタイミングで実行してくれそうです。

モデルをロードしてから、実行のたびにimatrixが更新され続けるはずなので、
何度か実行した結果を平均したい場合は、最後の実行時にだけセーブノードを追加するといいと思います。

# 量子化
[ComfyUI-GGUF](https://github.com/city96/ComfyUI-GGUF)のtoolsにある説明文通りGGUFファイルをつくって、
量子化時に`--imatrix <imatrix_file>`を追加するとできます。

# 注意
GGUFファイルのテンソルは1次元目が256の倍数になるよう変換されるため、一部のモデルではconvert.pyを買い替える必要があると思います。
ただし256の倍数でないとQX_K量子化ができないので、解決策もとむ。

またConv層があるモデルもconvert.pyの書き換えが必要です。カーネル次元をflattenして2次元テンソルにしてください。
