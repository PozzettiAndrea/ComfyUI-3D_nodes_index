# ComfyUI Mobile Client

A mobile-friendly web client extension for ComfyUI that allows you to:
- View generated images in a responsive gallery
- Monitor queue status in real-time
- Edit and regenerate prompts
- Upload workflow JSON files
- Customize various settings for prompt generation

## Installation

### Method 1: Using ComfyUI-Manager

You can install directly from ComfyUI-Manager:

![Install from ComfyUI-Manager](https://i.imgur.com/8MRw7GW.png)

### Method 2: Manual Installation

1. Clone this repository into your ComfyUI's `custom_nodes` directory:

```
cd custom_nodes
git clone https://github.com/vkff5833/ComfyUI-MobileClient
```

2. Restart ComfyUI

### Common: After Installation
Access the client at: `http://SERVER/extensions/ComfyUI-MobileClient/index.html`

**Note: The "index.html" part of the URL cannot be omitted. Make sure to include it in the URL.**

## Features

### Gallery View
- Responsive image gallery with modal view
- Navigate between images using arrow keys
- View queue ID and regenerate previous prompts

### Queue Monitoring
- Real-time queue status display
- Configurable monitoring interval
- Visual indicators for running and pending tasks

### Prompt Editing
- Edit text prompts, parameters, and seed values
- Automatic seed randomization (optional)
- Customizable field patterns for different input types

### Settings
- Server connection configuration
- Customizable key patterns for form fields
- Adjustable queue monitoring interval
- Settings persistence in local storage

## Usage

### 1. Server Settings

Left top menu icon to open settings screen:

<img src="https://i.imgur.com/zPPPSKS.png" alt="Settings Screen" width="300" align="right"/>

- Server URL setting (default is `/`)
- Authentication setting (if needed)
- Prompt field pattern setting
- Queue monitoring interval adjustment

<br clear="right"/>

### 2. Workflow Upload and Image Generation

Main screen allows the following operations:

<img src="https://i.imgur.com/Lq7FS4W.png" alt="Main Interface" width="300"/>

- Drag & drop workflow JSON file or file selection
- Gallery display of generated images
- Real-time queue status monitoring
- Image regeneration and prompt editing

### 3. Prompt Editing

Click Generate button to open edit modal:

<img src="https://i.imgur.com/0kdh8jK.png" alt="Edit Modal" width="300" align="right"/>

- Text prompt editing
- Parameter value adjustment (steps, cfg, size, etc.)
- Seed value editing (auto randomization possible)
- "Regenerate" button for immediate execution

<br clear="right"/>

### Keyboard Shortcuts

Available keys when gallery is displayed:

- ←/→: Move to previous/next image
- ↑/↓: Move to previous/next queue item
- Enter: Edit selected image prompt
- Space: Regenerate selected image

---

# ComfyUI モバイルクライアント

ComfyUI用のモバイルフレンドリーなWebクライアント拡張機能です。以下の機能を提供します：
- レスポンシブなギャラリーでの生成画像の表示
- リアルタイムのキュー状態監視
- プロンプトの編集と再生成
- ワークフローJSONファイルのアップロード
- プロンプト生成のための各種設定のカスタマイズ

## インストール方法

### 方法1: ComfyUI-Managerを使用

ComfyUI-Managerから直接インストールできます:

![ComfyUI-Managerでのインストール](https://i.imgur.com/8MRw7GW.png)

### 方法2: 手動インストール

1. ComfyUIの`custom_nodes`ディレクトリにこのリポジトリをクローンします：

```
cd custom_nodes
git clone https://github.com/vkff5833/ComfyUI-MobileClient
```

2. ComfyUIを再起動します

### 共通: インストール後
以下のURLでアクセスします：`http://SERVER/extensions/ComfyUI-MobileClient/index.html`

**注意：URLの末尾の "index.html" は省略できません。必ずURLに含めてください。**

## 機能

### ギャラリービュー
- モーダルビュー付きのレスポンシブな画像ギャラリー
- 矢印キーによる画像間のナビゲーション
- キューIDの表示と過去のプロンプトの再生成

### キュー監視
- リアルタイムのキュー状態表示
- 監視間隔の設定
- 実行中・待機中タスクの視覚的表示

### プロンプト編集
- テキストプロンプト、パラメータ、シード値の編集
- 自動シードランダム化（オプション）
- 入力タイプごとのカスタマイズ可能なフィールドパターン

### 設定
- サーバー接続設定
- フォームフィールドのカスタマイズ可能なキーパターン
- キュー監視間隔の調整
- ローカルストレージでの設定保存

## 使用方法

### 1. サーバー設定

左上のメニューアイコンをクリックして設定画面を開きます：

<img src="https://i.imgur.com/zPPPSKS.png" alt="設定画面" width="300" align="right"/>

- サーバーURL設定（デフォルトは `/`）
- 認証設定（必要な場合）
- プロンプトフィールドのパターン設定
- キュー監視間隔の調整

<br clear="right"/>

### 2. ワークフローのアップロードと画像生成

メイン画面では以下の操作が可能です：

<img src="https://i.imgur.com/Lq7FS4W.png" alt="メインインターフェース" width="300"/>

- ワークフローJSONファイルのドラッグ＆ドロップまたはファイル選択
- 生成済み画像のギャラリー表示
- キュー状態のリアルタイム監視
- 画像の再生成やプロンプト編集

### 3. プロンプト編集

Generateボタンをクリックすると編集モーダルが開きます：

<img src="https://i.imgur.com/0kdh8jK.png" alt="編集モーダル" width="300" align="right"/>

- テキストプロンプトの編集
- パラメータ値の調整（steps、cfg、サイズなど）
- シード値の編集（自動ランダム化可能）
- 「Regenerate」ボタンを押すと編集モーダルを開かず即時に再生成します。

<br clear="right"/>

### キーボードショートカット

ギャラリー表示時に以下のキーが使用可能：

- ←/→：前/次の画像に移動
- ↑/↓：前/次のキューアイテムに移動
- Enter：選択中の画像のプロンプトを編集
- Space：選択中の画像を再生成
