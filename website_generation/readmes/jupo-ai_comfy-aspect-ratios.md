# Aspect Ratios

![prev](https://files.catbox.moe/191v3r.png)

アスペクト比を指定してlatentを作成します

### `fixed_side`
- noneのとき
  - `base`の2乗を基本面積としてその面積に近いサイズになります
- shortのとき
  - 短辺を`base`で固定します
- longのとき
  - 長辺を`base`で固定します

### `step`
`step`の倍数になるように丸めます

### `switch ⇅`
width と height を入れ替えます