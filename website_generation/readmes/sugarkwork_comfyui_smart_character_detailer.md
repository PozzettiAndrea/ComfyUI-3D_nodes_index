# SmartCharacterDetailer

**SmartCharacterDetailer** は、[ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack) の `FaceDetailer` をベースに、**WD14 Tagger による画像解析とキャラクター自動識別機能** を追加した拡張ノードです。

通常の FaceDetailer では、全ての検出対象に対して同じ `positive` プロンプト（または固定の処理）が適用されますが、このノードでは**「誰が写っているか」を自動判別し、それぞれに最適なプロンプトを動的に適用**することができます。

---

## 🚀 主な機能と FaceDetailer との違い

### 1. WD14 Tagger による自動解析
検出された顔（または物体）領域を自動的に WD14 Tagger に通し、その特徴（髪色、目の色、装飾品など）をタグとして抽出します。これにより、事前のプロンプト指定なしでも、**元の絵柄や特徴を維持したままの高画質化（Detailing）** が可能です。

### 2. キャラクター定義と自動マッチング (`character_definitions`)
抽出されたタグに基づいて、事前に登録したキャラクター定義とマッチングを行います。
*   **FaceDetailer**: 全ての顔に同じプロンプトを適用（もし `positive` に "1girl, blue_hair" と書けば、赤髪のキャラも青髪に修正されてしまうリスクがある）。
*   **SmartCharacterDetailer**: 画像から「赤髪」が検出されればＡちゃんのプロンプト、「青髪」が検出されればＢちゃんのプロンプト、といった**描き分け**が自動で行われます。

**設定例:**
```text
red_hair, long_hair / character_A, best quality
blue_hair, short_hair / character_B, masterpiece
```

### 3. 排他的マッチングとサイズ優先処理
複数の顔が検出された場合、**面積が大きい（＝手前にいる重要な）顔から順に**処理を行います。
また、一度あるキャラクター定義が使用されると、その定義は「使用済み」となり、同じ画像内の他の顔には適用されません。これにより、**1枚の画像に同じキャラクターが重複して判定されるのを防ぎます**。

### 4. プロンプト入力不要 (Auto-Tagging Fallback)
`positive` 入力が空の場合、またはキャラクター定義にマッチしなかった場合、WD14で解析したタグそのものをプロンプトとして使用します。
これにより、**複雑なプロンプトを入力端子に繋がなくても、単体で「見たままを綺麗にする」ノード**として機能します。

---

## 📦 必須依存ノード (Dependencies)

このノードを使用するには、以下のカスタムノードがインストールされている必要があります。

1.  **[ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack)**
    *   ベースとなる検出・Detailer機能に必要です。
2.  **[ComfyUI-WD14-Tagger](https://github.com/pythongosssss/ComfyUI-WD14-Tagger)**
    *   画像のタグ解析に必要です。

※ `requirements.txt` は不要です。上記2つのカスタムノードが動作する環境（PyTorch, PIL, numpy 等）であれば動作します。

## 📥 インストール方法

`ComfyUI/custom_nodes/` ディレクトリ内に、このフォルダ（`my_detailer`）を配置してください。

```
ComfyUI/
  custom_nodes/
    ComfyUI-Impact-Pack/
    ComfyUI-WD14-Tagger/
    my_detailer/
       my_detailer_node.py
       README.md
```
