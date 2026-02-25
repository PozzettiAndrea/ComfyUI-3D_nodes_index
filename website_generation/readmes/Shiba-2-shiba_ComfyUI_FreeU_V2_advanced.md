# ComfyUI_FreeU_advanced

このカスタムノードは、従来の FreeU V2をアップデートし、指定した区間（timestep）で効果を適用する機能とB1B2, S1S2の処理を分離させたものです。  

timestepを加えることで、いつ・どのように効果を反映するかを制御できます。

さらにSDXLの拡散モデルにおける画像生成過程に合わせられるように、B1B2, S1S2ノードを分けて適用させることが可能です。

推奨は、B1B2を画像生成の前半部、S1S2ノードを画像生成の後半に適用することでより理想的な効果が期待できます。


This custom node is an update to the conventional FreeU V2, adding the ability to apply the effect during a specified interval (timestep) and separating the B1B2 and S1S2 processing.

By adding timesteps, you can control when and how the effect is applied.

Furthermore, to align with the image generation process of SDXL diffusion models, the B1B2 and S1S2 nodes can be applied separately.

For the most ideal effect, it is recommended to apply B1B2 during the first half of the image generation process and the S1S2 node during the latter half.


## how to use

使用方法と生成結果例については以下の記事に記載しています。

https://note.com/gentle_murre488/n/nbd3373fb8b8f

Usage instructions and example results are described in the article at the URL linked above

## Install


以下のコマンドでインストール出来ます。

You can install it with the following command.


```bash
cd Yourdirectory/ComfyUI/custom_nodes
git clone https://github.com/Shiba-2-shiba/ComfyUI_FreeU_V2_timestepadd.git

```


---
## Reference Script
以下のスクリプトを参考にしています。

This custom node is based on the following script.

https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_freelunch.py#L25
