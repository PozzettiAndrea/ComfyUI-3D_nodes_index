# Installation
You can install this node via ComfyUI Manager or comfy-cli.

## Via ComfyUI Manager

Search ComfyUI-SoX-Mixdown and install it.

[https://github.com/ltdrdata/ComfyUI-Manager?tab=readme-ov-file#how-to-use](https://github.com/ltdrdata/ComfyUI-Manager?tab=readme-ov-file#how-to-use)

## Via comfy-cli

```comfy node registry-install comfyui-sox-mixdown```

https://registry.comfy.org/publishers/johndoesmithee/nodes/comfyui-sox-mixdown

https://docs.comfy.org/comfy-cli/getting-started

# ComfyUI-SoX-Mixdown
![2to1](./examples/workflow1_2to1.png)

ComfyUI custom node for sox's mixdown function such as "sox --combine inputfile1.wav inputfile2.wav outputfile.wav".

You can mixdown two same length audio clips to one with this node.

To use this node, let's install the SoX command first ;-)
You can install SoX with following command.

<details>
<summary>SoX Installing Commands</summary>

Windows
```
winget install ChrisBagwell.SoX
```

Mac
```
brew install sox
```

Linux(too many way...)
```
apt install sox
```
```
dnf install sox
```
```
pacman -S sox
```

</details>

Never forget to add "sox" command to your path.

# External Links
## ComfyUI's docs for making and publishing custom nodes
https://docs.comfy.org/custom-nodes/overview

https://docs.comfy.org/registry/publishing

<details> <summary> <strong> Tutorials for Making Custom Nodes</strong> </summary>

### Suzie1/ComfyUI_Guide_To_Making_Custom_Nodes: A guide to making custom nodes in ComfyUI
https://github.com/Suzie1/ComfyUI_Guide_To_Making_Custom_Nodes

### [TUTORIAL] Create a custom node in 5 minutes! (ComfyUI custom node beginners guide) : r/comfyui
https://www.reddit.com/r/comfyui/comments/18wp6oj/tutorial_create_a_custom_node_in_5_minutes/

### A Basic Guide to Creating ComfyUI Custom Nodes | Civitai
https://civitai.com/articles/4934/a-basic-guide-to-creating-comfyui-custom-nodes

</details>

## SoX
https://sourceforge.net/projects/sox/

## pysox
https://github.com/marl/pysox

## 日本語参考情報

<details> <summary> <strong> カスタムノード作成日本語参考情報 </strong> </summary>

### ComfyUIのプラグインを作る！
https://zenn.dev/4kk11/articles/4e36fc68293bd2

### ComfyUIのカスタムノードを作るには｜にゃおき
https://note.com/nyaoki_board/n/n96ab9293291c

### 「ComfyUI ノードを作ろう」タグが付けられた記事一覧 | 謎の技術研究部
https://www.ultra-noob.com/tag/comfy-ui-%E3%83%8E%E3%83%BC%E3%83%89%E3%82%92%E4%BD%9C%E3%82%8D%E3%81%86/

### ComfyUIのコードをまるごとGemini 1.5 Proに読ませてみた😂｜一般オーク
https://note.com/ippan_orc/n/naed830f52f99

### 【西川和久の不定期コラム】NVIDIAがローカルで手軽に動せるAIチャット「Chat with RTX」をリリース！その実力は？ - PC Watch
https://pc.watch.impress.co.jp/docs/column/nishikawa/1571371.html

</details>

いずれかの検索拡張生成（RAG）に ComfyUI のソース一式を読ませると、いい感じにサポートしてくれるかもしれません。
