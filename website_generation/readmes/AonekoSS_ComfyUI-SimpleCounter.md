# ComfyUI-SimpleCounter
Node: "utils/Simple Counter"<br>
This node is a simple counter, when pressing "Queue Prompt" resets the count.<br>
Use this with batche count and "Load Image Batch (WAS Node Suite)" etc.<br>

## 概要
画像の順次読み込み等を補助するシンプルなカスタムノードです。<br>
以下のようにバッチ数を設定して使います。（WAS Node SuiteのLoad Image Batch等と一緒に使うのがオススメ）<br>
<img src="sample.jpg"><br>

## 動作
ノードはメニューの「utils」カテゴリーの中にいます。<br>
バッチ実行中「start」に設定した値からカウントアップしていきます。<br>
「Queue Prompt」を押すとカウントがリセットされます。<br>

## ライセンスとか
配布や改変等ご自由にどうぞ。<br>

Python側はノードの定義のみ、全部JavaScript側で処理してます。<br>
（バッチ開始を知る術が無かったので……）<br>