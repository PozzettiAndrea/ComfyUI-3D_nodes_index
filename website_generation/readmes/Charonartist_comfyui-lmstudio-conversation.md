# ComfyUI LM Studio カスタムノードパック

ComfyUI環境でLM Studioと連携するための包括的なカスタムノードセットです。画像で提供された機能と完全に同等のLM Studio (Text Gen)ノードと、会話ログ維持機能を提供します。

## 含まれるノード

### 1. LM Studio (Text Gen) - メインノード
画像と同等の機能を持つテキスト生成ノード:
- **完全なパラメータ対応**: model_key, auto_unload, seed, 生成後の制御など
- **ネットワーク設定**: IP address, port設定
- **デバッグモード**: 詳細なログ出力
- **タイムアウト制御**: カスタマイズ可能な待機時間

### 2. LM Studio Conversation - 会話維持ノード  
- **会話ログ維持**: 同一実行キュー内で会話履歴を自動保存
- **自動メモリ管理**: 指定した最大会話長を超えると古い会話を自動削除
- **会話リセット機能**: 必要に応じて会話履歴をクリア

### 3. LM Studio Clear Conversations - 管理ノード
- **履歴クリア**: 保存されている全会話履歴をリセット

## インストール方法

### 1. 手動インストール
1. ComfyUIの `custom_nodes` フォルダにこのフォルダをコピー
2. ComfyUIを再起動

### 2. 依存関係インストール
```bash
pip install requests
```

## 前提条件

1. **LM Studio起動**: LM Studioがローカルで起動している
2. **サーバー有効**: LM Studioの「Local Server」が開始されている
3. **モデル読み込み**: 使用したいモデルが読み込まれている

## 使用方法

### 基本的な使用手順

1. **ノード配置**: ComfyUIエディタで「LM Studio Conversation」ノードを配置
2. **パラメータ設定**:
   - `prompt`: 送信したいメッセージを入力
   - `lm_studio_url`: LM StudioのURL（通常は `http://localhost:1234`）
   - `max_conversation_length`: 保持する最大会話ペア数
3. **実行**: キューを実行して応答を取得

## パラメータ詳細

### LM Studio (Text Gen) ノード

**必須パラメータ**:
| パラメータ | 型 | デフォルト値 | 説明 |
|-----------|----|---------|----|
| `prompt` | STRING | "" | 生成するテキストのプロンプト |
| `model_key` | STRING | "qwen/qwen-4b-2507" | モデルキー |
| `auto_unload` | BOOLEAN | True | 自動アンロード |
| `unload_delay` | INT | 0 | アンロード遅延時間（秒） |
| `seed` | INT | 1039310740569363 | ランダムシード値 |
| `max_tokens` | INT | 4096 | 最大生成トークン数 |
| `temperature` | FLOAT | 0.7 | 生成ランダム性（0.0-2.0） |
| `debug` | BOOLEAN | False | デバッグモード |
| `timeout_seconds` | INT | 300 | タイムアウト時間（秒） |
| `model` | STRING | "qwen/qwen-4b-2507" | モデル名 |
| `ip_address` | STRING | "192.168.0.120" | LM StudioサーバーIP |
| `port` | INT | 1234 | ポート番号 |

**オプションパラメータ**:
| パラメータ | 型 | デフォルト値 | 説明 |
|-----------|----|---------|----|
| `system_prompt` | STRING | "Qwen-Image About Qwen..." | システムプロンプト |
| `生成後の制御` | STRING | "randomize" | 生成後の制御方式 |
| `reset_conversation` | BOOLEAN | False | 会話リセット |

**出力**: `Generated Text` (STRING) - 生成されたテキスト

### LM Studio Conversation ノード

**入力パラメータ**:
| パラメータ | 型 | デフォルト値 | 説明 |
|-----------|----|---------|----|
| `prompt` | STRING | "Hello, how are you today?" | 送信するメッセージ |
| `lm_studio_url` | STRING | "http://localhost:1234" | LM StudioサーバーURL |
| `max_conversation_length` | INT | 10 | 保持する最大会話ペア数 |

**出力**:
| 出力 | 型 | 説明 |
|------|----|-----|
| `response` | STRING | LM Studioからの応答テキスト |
| `conversation_log` | STRING | 会話全履歴（JSON形式） |
| `message_count` | INT | 現在の会話メッセージ数 |

## 会話クリアノード

**LM Studio Clear Conversations**ノードを使用して、保存されている全ての会話履歴をクリアできます。

### 使用例ワークフロー

```
[Text Input] -> [LM Studio Conversation] -> [Text Output]
                           |
                    [Conversation Log Display]
```

## トラブルシューティング

### よくある問題

**1. 接続エラー**
```
Error: Cannot connect to LM Studio. Please ensure LM Studio is running and the server is started.
```
**解決方法**:
- LM Studioが起動していることを確認
- Local Serverが開始されていることを確認
- URLが正しいことを確認（通常は `http://localhost:1234`）

**2. 応答タイムアウト**
```
Error: Request to LM Studio timed out
```
**解決方法**:
- モデルが正しく読み込まれていることを確認
- より軽量なモデルを試す
- `max_tokens`を小さく設定する

**3. メモリ不足**
**解決方法**:
- `max_conversation_length`を小さく設定
- 定期的に会話をリセット

### デバッグ情報

エラーが発生した場合、ComfyUIのコンソールで詳細なエラーメッセージを確認できます。

## 技術仕様

- **Python**: 3.x対応
- **依存関係**: requests
- **API**: OpenAI互換APIを使用
- **メモリ管理**: 会話長制限による自動管理
- **エラーハンドリング**: 包括的な例外処理

## 更新履歴

- **v1.0.0**: 初回リリース
  - 基本的な会話機能
  - 会話ログ維持
  - LM Studio連携

## ライセンス

MIT License

## サポート

問題が発生した場合は、以下を確認してください：

1. LM Studioの起動状況
2. ネットワーク接続
3. モデルの読み込み状況
4. ComfyUIコンソールのエラーメッセージ

技術的な質問やバグレポートは、プロジェクトのIssuesページで受け付けています。