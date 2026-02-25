# ComfyUI Tag Remover

テキストから指定されたタグとその内容を除去するComfyUIカスタムノードです。

## 主な用途

- LM StudioのThinkモデルの出力から`<think>...</think>`タグを除去
- XMLやHTMLタグの除去
- その他のカスタムタグの除去

## インストール方法

1. ComfyUIのカスタムノードディレクトリに配置：
   ```
   ComfyUI/custom_nodes/comfyui-tag-remover/
   ```

2. ComfyUIを再起動

## 使用方法

### 基本的な使い方

1. ComfyUIのノードメニューから`text/processing` → `Tag Remover`を選択
2. 入力パラメータを設定：
   - **text**: 処理対象のテキスト
   - **tag_name**: 除去するタグ名（例：`think`）

### パラメータ詳細

#### 必須パラメータ
- **text** (STRING): 処理対象のテキスト
- **tag_name** (STRING): 除去するタグ名（デフォルト: `think`）

#### オプションパラメータ
- **remove_empty_lines** (BOOLEAN): 空行を除去するかどうか（デフォルト: `True`）
- **trim_whitespace** (BOOLEAN): 前後の空白を除去するかどうか（デフォルト: `True`）

### 使用例

#### LM StudioのThinkモデル出力の処理

**入力テキスト:**
```
これは普通のテキストです。
<think>
これは思考過程です。
複数行にわたる思考内容。
</think>
これは最終的な回答です。
```

**設定:**
- tag_name: `think`
- remove_empty_lines: `True`
- trim_whitespace: `True`

**出力:**
```
これは普通のテキストです。
これは最終的な回答です。
```

#### カスタムタグの除去

**入力テキスト:**
```
<summary>要約部分</summary>
メインコンテンツ
<note>注釈部分</note>
```

**設定:**
- tag_name: `note`

**出力:**
```
<summary>要約部分</summary>
メインコンテンツ
```

## 機能特徴

- **柔軟なタグ指定**: 任意のタグ名を指定可能
- **ネストしたタグ対応**: タグ内にタグがある場合も適切に処理
- **大文字小文字を区別しない**: `<Think>`, `<THINK>`, `<think>`すべて対応
- **改行を含むコンテンツ対応**: 複数行にわたるタグ内容も除去
- **属性付きタグ対応**: `<tag attr="value">`のような属性付きタグも対応

## ファイル構成

```
comfyui-tag-remover/
├── __init__.py              # ノード登録用ファイル
├── tag_remover_node.py      # メインのノードクラス
└── README.md               # このファイル
```

## ライセンス

MIT License

## 更新履歴

- v1.0.0: 初回リリース
  - 基本的なタグ除去機能
  - オプション設定（空行除去、空白除去）