# ComfyUI Near-sighted Attention

This node splits its self-attention Q to focus on nearby samples.

This based on my old custom node `Slothful Attention`.

## What's this?

### Near-sighted Tile

Like HyperTile, this nodes split samples as Q for self-attention. 

And serves K, V that concatinated local(same tile) and global(other tile) samples by given ratio.

This may improve details of images.

### Slothful Attention

This nodes allow controlling output images by pooling K and V samples on self-attentions.


### Near-sighted Attention

Near-sighted Tile + Slothful Attention.


## Tips

### Near-sighted Tile

tile_size is in latent space, so tile_size: 64 is 512x512px.

Smaller tile_size may improve image details, but may break consistency of image.

Larger global_ratio may prevent breaking consistency.

If the batch size is 2 or more, the `concat_local` and `concat_global` options allows concatenate K, V across batches.

### Slothful Attention

`in_...` and `out_..` parameters: individual parameters for `in` and `out` blocks

Slothful is reduction rate. (this will be decreased by depth_decay and time_decay)

You can set another blend ratio for K, V

Bigger in_k_blend may reduce noises.

Bigger out_v_blend may affect image


## 概要

### Near-sighted Tile

HyperTileのように、self-attentionの入力を分割します。

同一タイルをローカル、他のタイルをグローバルとして、指定された比率で結合し、 K, V として利用します。

これにより、画像のディテールが改善するかもしれません。


### Slothful Attention

セルフアテンションの K,V をプーリングすることで、画像のコントロールを行います。


### Near-sighted Attention

Near-sighted Tile と Slothful Attention の両方の機能を持ったノードです。

設定項目は多いですが、速度向上とある程度の画質コントロールが可能となります。


## パラメータ

### Near-sighted Tile

tile_sizeは潜在空間での寸法です。なので、tile_size: 64 はピクセルでは 512x512px になります。
（SD1.5の最も浅い層では）

tile_sizeを下げるとディテールが改善するかもしれませんが、画像の一貫性は損なわれやすいです。

global_ratioを上げると一貫性は保たれやすいですが、ディテールは低下するかも知れません。

バッチサイズが２以上のとき、 `concat_local`  `concat_global` を有効にすると、
バッチ間でK, Vを結合します。
これにより、セルフアテンションにてバッチ間の他画像を参照するようになるため、ある程度の一貫性が保てるようになります。

### Slothful Attention
 
`in_...` `out_..` パラメータ: inブロック, outブロックに別のパラメータを適用できます

Slothful（を depth_decay, time_decayで減らした値）が削減比率になります。

time_decayについては、peak_time (開始が0、終了が1)のステップでは軽減無しで、そこから離れると time_decayに従って効果が軽減されます。
構図への影響を弱めたいときは、peak_time:0.5 time_decay: 2.5 などの設定が良いかもしれません
出力のディテールが悪いときは、time_decayを上げるか、peak_timeを下げてみてください。
（最後の方のstepで影響を減らす目的です）

削減時は n サンプルごとに 1 サンプル取り出す one と、n サンプルを mode によってプーリングする pool を
ブレンドします。ブレンド率は K, V で別の値を指定出来ます。

modeは avr（nサンプルの平均。ぼかしたような感じです） max（max_pooling。シャープネスに近いかもしれません）で、1Dのは横のみ。2Dは縦横でプーリングを行います。

ブレンド率上げたときの画像変化は状況によって違うのですが、影響が大きいのは in_k_blend と out_v_blend です

in_k_blend を上げると、ノイズや細かい描写を無視するような傾向があります。

in_mode による変化はそこまで大きくないですが、1D系だと陰影や光沢などが軽視される傾向があるようです。

in_v_blendは モードによる違いが出やすいみたいです。
AVGの場合は輪郭が不明瞭になったりします。服の模様とかは結構影響受けやすいみたいです。
MAXの場合はAVGよりドラスティックな変化になります。モデルによりますが絵画的な描画になることもあります。

in_k_blendを上げると、服の模様などが不鮮明になったり、被写界深度（ボケ）っぽい効果になったりするようです。
絵がくっきりしすぎている場合はここを調整すると良い具合になってくれることもあります。

out_v_blend はコントラストやシャープネスに関係するようです。
AVG系モードでは柔らかめ、コントラスト低めの出力、MAX系モードでは固め、コントラスト高めの出力の傾向が出ます。

1Dの方がより強く効果が出ますが、2Dに比べて描画が崩れやすい傾向にあるようです。

