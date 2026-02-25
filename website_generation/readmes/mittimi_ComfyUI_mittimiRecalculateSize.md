# ComfyUI_mittimiRecalculateSize

This is the node that performs the magnification calculation.

Width と Height に Magnification の値を掛けた数字を出力します。


![Screenshot of sample02.](/assets/images/comfyuimittimirecalculatesize001s.jpg)


It would be easier to use if the Width and Height could be connected by right-clicking on the node and selecting "Convert Widget to Input".

ノードを右クリックから Convert Widget to Input を選択し Width と Height を接続できるようにすれば使いやすいと思います。

![Screenshot of sample02.](/assets/images/comfyuimittimirecalculatesize002s.jpg)

We created this function because it was troublesome to increase the number of nodes when processing INT and FLOAT conversions at the node level.

INT と FLOAT の変換処理をノードでする際に、ノード数が増えるのが面倒だったのでこの機能を作成しました。


I am not a professional. If there is a bug, please tell me how to fix it.

※私はプロではありません。バグがあった場合、直し方もコッソリ教えてください。

Autor by mittimi (https://mittimi.blogspot.com)
