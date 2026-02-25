# ComfyUI-Load-DirectoryFiles

## 概要

[ComfyUI](https://github.com/comfyanonymous/ComfyUI)のCustomNode

![](./sample.png)

指定したディレクトリにあるプロンプト(txt)と画像(png)を読み込みます。   
indexを指定することで、指定したファイルを出力します。

これは、計画した画像生成をすることを想定して作りました。  
プロンプトと画像を合わせて参照することで、プロンプトだけでは描きにくい問題を緩和します。    
例えば、ControlNetやi2iを使用することでプロンプトを補うことができるため、試行回数を減らすことに繋がります。

## ファイル形式について

以下のように、同じ番号で名前を付けたテキストと画像の組み合わせを1つのフォルダに格納します。なお、ネガティブプロンプトも対応させたので、名前に"_n"を付けています

```
# プロンプト
001.txt
002.txt
003.txt

# 画像
001.png
002.png
003.png

# ネガティブプロンプト
001_n.txt
002_n.txt
003_n.txt
```

## 前提

- ComfyUIのインストールを完了していること

## 導入

```
git clone https://github.com/educator-art/ComfyUI-Load-DirectoryFiles ./custom_nodes/ComfyUI-Load-DirectoryFiles
```

## 応用

ComfyUIの[basic_api_example.py](https://github.com/comfyanonymous/ComfyUI/blob/master/script_examples/basic_api_example.py)を参考にしてComfyUIのAPIを活用したプログラムを作成し、指定した枚数の画像生成を自動化しました。 これにより、当初の目的を実現できました。

※ [応用](https://note.com/educator/n/ncf9a3ef40191)は拡張機能の範囲外となりますので、詳しい方法は割愛します。

## ライセンス

 - GPL-3.0 License