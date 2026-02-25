# ComfyUI_AspectRatioToSize

アスペクト比を維持した、横幅と高さの数値を計算する、ComfyUI 用のノードです。

任意のアスペクト比を維持した、複数の解像度の計算をする際に使用します。

## AspectRatioToSize
アスペクト比を計算して、サイズオブジェクトを返します。

### input
- aspect_ratio: アスペクト比を指定します。
- resolution: 長辺サイズを指定します。

### output
- Size: Size オブジェクトを返します。


## SizeToWidthHeight
サイズオブジェクトから横幅と高さの値を取り出します。

### input
- Size: サイズオブジェクトを指定します。

### output
- Width: 幅を返します
- Height: 高さを返します
- LongerSide: 長辺のサイズを返します
- SmallSide: 短辺のサイズを返します

## CalculateImagePadding
指定された縦横比になるために必要な、上下左右に追加すべき余白のサイズを計算します。

### input
 - image: 対象の画像
 - raito: 縦横比を表す文字

### output
 - top: 上に追加するべき余白
 - bottom: 下に追加するべき余白
 - left: 左に追加するべき余白
 - right: 右に追加するべき余白

## MatchImageToAspectRatio

画像と、Bool でアスペクト比を選択すると、最も近い形のアスペクト比を文字列および数値で返します。

AspectRatioToSize にアスペクト比として渡して、長辺サイズを指定すると、決められたアスペクト比＋決められた長辺サイズの矩形のための情報を作成できます。

aspect_ratio には、任意のサイズのアスペクト比を入力する事が出来て、チェックボックスに無いアスペクト比を、カンマ区切りで複数指定出来ます。

![image](https://github.com/user-attachments/assets/7b2c0577-9555-49cc-9db9-21478780c653)



# メリット

例えば、16:9 で、長辺が 1920 の解像度を計算して、それを Empty Latent に入力したい、と考えた時、自動計算しようとすると面倒でした。

これらのノードに、縦横比と長辺の値を指定するだけで、自動的に短辺のサイズも決まり、欲しい解像度の画像サイズの計算が楽になります。
