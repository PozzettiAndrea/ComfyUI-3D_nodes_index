# 🤖 ComfyUI Auto LoRA

テキストプロンプトからトリガーワードを自動検出し、対応するLoRAを自動適用するComfyUIカスタムノードです。

## 🌟 機能

- **自動トリガーワード検出**: 入力テキストから完全一致でトリガーワードを検出
- **自動LoRA適用**: 検出されたトリガーワードに対応するLoRAを自動適用
- **設定管理**: JSONファイルでLoRAとトリガーワードの対応を管理
- **WebUI**: ブラウザで簡単にLoRA設定を管理
- **柔軟な強度設定**: LoRAごとに強度を個別設定可能

## 📁 ファイル構成

```
comfyui-auto-lora/
├── __init__.py              # ComfyUI登録用
├── nodes.py                 # メインノード実装
├── lora_manager.py          # LoRA管理クラス
├── web_ui.py               # Web設定管理UI
├── setup_ui.py             # WebUI起動スクリプト
├── config/
│   └── lora_mapping.json   # LoRA設定ファイル
└── README.md               # このファイル
```

## 🚀 インストール方法

### 1. ComfyUIのカスタムノードディレクトリに配置

```bash
# ComfyUIディレクトリに移動
cd /path/to/ComfyUI

# custom_nodesディレクトリにクローン
git clone <このリポジトリ> custom_nodes/comfyui-auto-lora

# または手動でファイルをコピー
cp -r comfyui-auto-lora/ /path/to/ComfyUI/custom_nodes/
```

### 2. ComfyUIを再起動

ComfyUIを再起動すると、新しいノードが認識されます。

## 🎯 使用方法

### 基本的な使用手順

1. **LoRA設定の登録**
   - WebUIまたは設定ファイルでLoRAとトリガーワードを登録

2. **ComfyUIでノード使用**
   - `🤖 Auto LoRA` ノードをワークフローに追加
   - MODEL、CLIP、テキストを接続
   - テキストにトリガーワードを含めて実行

### ノードの種類

#### 🤖 Auto LoRA ノード
- **入力**: MODEL, CLIP, TEXT
- **出力**: MODEL, CLIP, TEXT, LoRA情報
- **機能**: トリガーワード検出と自動LoRA適用

#### ⚙️ LoRA Manager ノード  
- **機能**: LoRA設定の管理（追加・削除・一覧表示）

## ⚙️ LoRA設定管理

### 方法1: WebUI（推奨）

```bash
# WebUI起動
cd comfyui-auto-lora
python setup_ui.py

# ブラウザで http://localhost:8765 にアクセス
```

**WebUIの機能:**
- 登録済みLoRA一覧表示
- 新しいLoRA追加
- 既存LoRA削除
- リアルタイム設定更新

### 方法2: 設定ファイル直接編集

`config/lora_mapping.json` を直接編集：

```json
{
  "lora_mappings": [
    {
      "trigger_word": "miku",
      "lora_file": "hatsune_miku.safetensors",
      "strength": 1.0,
      "description": "初音ミク LoRA"
    },
    {
      "trigger_word": "anime_style", 
      "lora_file": "anime_style_v1.safetensors",
      "strength": 0.8,
      "description": "アニメスタイル LoRA"
    }
  ],
  "settings": {
    "case_sensitive": false,
    "max_lora_count": 3,
    "default_strength": 1.0
  }
}
```

### 方法3: LoRA Manager ノード

ComfyUI内で `⚙️ LoRA Manager` ノードを使用して設定管理

## 📝 使用例

### 例1: 基本的な使用

**プロンプト**: `"beautiful miku singing"`
**結果**: `miku` がトリガーワードとして検出され、対応するLoRAが自動適用

### 例2: 複数トリガーワード

**プロンプト**: `"anime_style miku portrait"`
**結果**: 最初に見つかった `anime_style` のLoRAが適用

### 例3: トリガーワード未検出

**プロンプト**: `"beautiful landscape"`
**結果**: トリガーワードなし、LoRA未適用

## 🔧 設定項目

### LoRA設定項目

| 項目 | 説明 | 例 |
|------|------|-----|
| `trigger_word` | トリガーワード | `"miku"` |
| `lora_file` | LoRAファイル名 | `"hatsune_miku.safetensors"` |
| `strength` | 適用強度 | `1.0` |
| `description` | 説明（任意） | `"初音ミクLoRA"` |

### 全体設定項目

| 項目 | 説明 | デフォルト |
|------|------|-----------|
| `case_sensitive` | 大文字小文字を区別 | `false` |
| `max_lora_count` | 最大LoRA数（将来拡張用） | `3` |
| `default_strength` | デフォルト強度 | `1.0` |

## 🔍 トラブルシューティング

### よくある問題

1. **LoRAファイルが見つからない**
   - LoRAファイルがComfyUIの`models/loras/`ディレクトリにあるか確認
   - ファイル名が正確か確認

2. **トリガーワードが検出されない**
   - 完全一致で検出されるため、スペルを確認
   - 大文字小文字の設定を確認

3. **ノードが表示されない**
   - ComfyUIを再起動
   - ファイルが正しいディレクトリに配置されているか確認

### ログ確認

ComfyUIのコンソールで `[AutoLoRA]` プレフィックスのログを確認

## 📋 要件

- ComfyUI
- Python 3.7+
- 対応LoRAファイル形式: `.safetensors`, `.ckpt`

## 🔄 更新履歴

### v1.0.0
- 初回リリース
- 基本的な自動LoRA適用機能
- WebUI による設定管理
- トリガーワード完全一致検出

## 📄 ライセンス

このプロジェクトはオープンソースです。

## 🤝 貢献

バグ報告や機能要望は、Issueやプルリクエストでお気軽にご連絡ください。

## 📞 サポート

使用方法でご不明な点がございましたら、ドキュメントを参照するか、コミュニティフォーラムでお尋ねください。