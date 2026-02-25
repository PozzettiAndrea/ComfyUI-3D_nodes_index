# comfy-mecha-utils

[comfy-mecha](https://github.com/ljleb/comfy-mecha.git)用の便利ノード


## ノード一覧

### Block Sliders

![blockSliders](assets/block_sliders.png)

ブロックごとの値をスライダーで直感的に調整できるノードです。  
**SD1 Blocks Slider**  
**SDXL Blocks Slider** 

- `round = True` を設定すると、小数点第2位まで四捨五入されて、スライダーの表示値と一致します。
- プロパティパネルから直接値を入力できます。



## 更新履歴
- v1.0.1
  - 各 Blocks ノードに、スライダー値と同期するプロパティを追加。
  - WAVEプリセットの位相を変えたWAVE_p0, WAVE_p1...プリセットを追加。
- v1.1.1
  - comfy-mecha v1.2.38に対応
  - **SD1 Blocks Slider** と **SDXL Blocks Slider** ノードのみに変更
  - 