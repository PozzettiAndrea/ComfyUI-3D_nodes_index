# ComfyUI-PromptComment

ComfyUI のプロンプトでコメントアウト機能を提供するカスタムノードです。

[English](README_EN.md)

## 機能

プロンプト内で `#` や `//` などの記号を使ってコメントを記述できます。
コメント部分は自動的に除去され、クリーンなプロンプトが出力されます。

## インストール

### 手動インストール

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/YOUR_USERNAME/ComfyUI-PromptComment.git
```

### ComfyUI Manager

ComfyUI Manager から "PromptComment" で検索してインストールできます。

## ノード

### Prompt Comment (Strip)

シンプルなコメント除去ノード。1種類のコメントマーカーを指定できます。

**入力:**
| パラメータ | 説明 |
|-----------|------|
| text | 入力プロンプト（複数行対応） |
| comment_style | コメント記法: `#`, `//`, `--`, `Custom` |
| custom_marker | comment_style が Custom の時に使用する文字列 |
| remove_empty_lines | 空行を削除するか |
| trim_whitespace | 各行の前後の空白を削除するか |

**出力:**
- `text`: コメントが除去されたプロンプト

### Prompt Comment (Multi-Marker)

複数のコメントマーカーを同時に認識するノード。

**入力:**
| パラメータ | 説明 |
|-----------|------|
| text | 入力プロンプト（複数行対応） |
| use_hash | `#` をコメントとして認識 |
| use_double_slash | `//` をコメントとして認識 |
| use_double_dash | `--` をコメントとして認識 |
| remove_empty_lines | 空行を削除するか |
| trim_whitespace | 各行の前後の空白を削除するか |

## 使用例

### 入力プロンプト:
```
masterpiece, best quality,  # 品質タグ
1girl, solo,                # キャラクター
blue hair, red eyes,        # 外見
# sitting, standing,        # ← この行は全体がコメント
smile
```

### 出力 (remove_empty_lines=True):
```
masterpiece, best quality,
1girl, solo,
blue hair, red eyes,
smile
```

## ワークフロー例

```
[String Literal] → [Prompt Comment] → [CLIP Text Encode]
     (プロンプト)    (コメント除去)      (エンコード)
```

## ライセンス

MIT License
