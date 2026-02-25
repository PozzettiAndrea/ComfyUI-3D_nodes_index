# ComfyUI Proxy Fix Extension

This extension fixes URL encoding issues when ComfyUI is accessed through reverse proxies like `jupyter-server-proxy`.

## Problem

When ComfyUI saves workflows, it uses paths like `workflows/filename.json`. This causes issues when:

1. The frontend URL-encodes the path as `workflows%2Ffilename.json`
2. `jupyter-server-proxy` automatically decodes `%2F` back to `/`
3. ComfyUI's router receives `workflows/filename.json` and interprets it as a subdirectory
4. API calls fail with routing errors

## Solution

This extension applies fixes at both frontend and backend:

### Frontend (JavaScript)
- Intercepts all `fetch()` API calls to `/api/userdata/`
- Replaces `workflows/` with `workflows__SLASH__` before sending requests
- Keeps the path flat, avoiding URL encoding issues entirely

### Backend (Python)
- Provides fallback path normalization for any server-side routing
- Ensures consistent behavior across different proxy configurations

## Installation

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/mochidroppot/ComfyUI-ProxyFix.git
```

## Usage

No configuration needed. The extension activates automatically when ComfyUI starts.

## Testing

To verify the fix is working:

1. Open ComfyUI through jupyter-server-proxy
2. Create a workflow
3. Try to save it - it should work without 405 errors

## Debug

To enable debug mode, set the environment variable:

```bash
export DEBUG_PROXYFIX=1
```

Debug mode will show detailed information in both browser console and server logs.

## Compatibility

- ComfyUI 0.3.57+
- jupyter-server-proxy
- Other reverse proxies that decode URL-encoded paths

## Technical Details

### How it Works

1. **Frontend**: Intercepts all API calls to `/api/userdata/` and replaces `workflows/` with `workflows__SLASH__`
2. **Backend**: Applies middleware that converts `workflows__SLASH__` back to `workflows/`
3. **`__SLASH__` Separator**: Uses a unique identifier that won't conflict with user filenames

### File Structure

- `__init__.py`: Backend middleware and ComfyUI integration
- `web/fix-workflow-slash.js`: Frontend fix script
- `web/__init__.py`: Frontend extension marker file

## License

MIT License

---

# ComfyUI Proxy Fix Extension

この拡張機能は、ComfyUIが`jupyter-server-proxy`などのリバースプロキシを通じてアクセスされる際のURLエンコーディング問題を修正します。

## 問題

ComfyUIがワークフローを保存する際、`workflows/filename.json`のようなパスを使用します。これが以下の問題を引き起こします：

1. フロントエンドがパスを`workflows%2Ffilename.json`としてURLエンコード
2. `jupyter-server-proxy`が自動的に`%2F`を`/`にデコード
3. ComfyUIのルーターが`workflows/filename.json`を受け取り、これをサブディレクトリとして解釈
4. APIコールがルーティングエラーで失敗

## 解決策

この拡張機能は、フロントエンドとバックエンドの両方で修正を適用します：

### フロントエンド（JavaScript）
- `/api/userdata/`へのすべての`fetch()` APIコールをインターセプト
- リクエスト送信前に`workflows/`を`workflows__SLASH__`に置換
- パスをフラットに保ち、URLエンコーディング問題を完全に回避

### バックエンド（Python）
- サーバーサイドルーティング用のフォールバックパス正規化を提供
- 異なるプロキシ設定間での一貫した動作を保証

## インストール

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/mochidroppot/ComfyUI-ProxyFix.git
```

## 使用方法

設定は不要です。ComfyUIが起動すると、拡張機能が自動的に修正を適用します。

## 動作確認

修正が正常に動作していることを確認するには：

1. jupyter-server-proxy経由でComfyUIを開く
2. ワークフローを作成
3. 保存を試行 - 405エラーなしで動作するはず

## デバッグ

デバッグモードを有効にするには、環境変数を設定してください：

```bash
export DEBUG_PROXYFIX=1
```

デバッグモードでは、ブラウザのコンソールとサーバーログに詳細な情報が表示されます。

## 互換性

- ComfyUI 0.3.57+
- jupyter-server-proxy
- URLエンコードされたパスをデコードするその他のリバースプロキシ

## 技術詳細

### 動作原理

1. **フロントエンド**: すべての`/api/userdata/`へのAPIコールをインターセプトし、`workflows/`を`workflows__SLASH__`に置換
2. **バックエンド**: `workflows__SLASH__`を`workflows/`に変換するミドルウェアを適用
3. **`__SLASH__`セパレーター**: ユーザーファイル名と競合しないユニークな識別子を使用

### ファイル構成

- `__init__.py`: バックエンドミドルウェアとComfyUI統合
- `web/fix-workflow-slash.js`: フロントエンド修正スクリプト
- `web/__init__.py`: フロントエンド拡張のマーカーファイル

## ライセンス

MIT License