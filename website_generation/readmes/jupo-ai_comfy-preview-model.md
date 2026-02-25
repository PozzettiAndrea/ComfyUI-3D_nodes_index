# comfy-preview-model

![preview](https://files.catbox.moe/m2ts21.png)

モデルファイルの選択時にプレビューを表示します。  
プレビュー画像はモデルと同じディレクトリに以下のファイル名のどちらかで配置してください。

- モデルと同じ名前.拡張子(png, webp...)
- モデルと同じ名前.preview.拡張子(png, webp...)

ついでにLoad Imageノード等で画像や動画もプレビューできます。  

### 対応している拡張子
| type | exts |
| --- | --- |
| model | ckpt, safetensors, pt, pth, gguf |
| image | jpg, jpeg, bmp, png, webp, gif |
| video | mp4, webm |
| audio | ogg, wav, mp3, webm |