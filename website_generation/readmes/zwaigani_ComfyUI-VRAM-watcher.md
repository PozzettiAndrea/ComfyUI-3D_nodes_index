![VRAM Watcher (Bar)](images/vram-watcher.png)

# ComfyUI-VRAM-watcher

[English](#english) | [日本語](#日本語)

## English

A simple ComfyUI custom node that shows **VRAM / RAM usage bars** on the canvas.

- VRAM: read via `torch.cuda` (shows unavailable when CUDA is not available)
- RAM: on Linux via `/proc/meminfo`, otherwise via `psutil` when installed

### Install

In `ComfyUI/custom_nodes`:

```bash
git clone https://github.com/zwaigani/ComfyUI-VRAM-watcher.git
```

Restart ComfyUI.

### Usage

1. Start ComfyUI
2. Add node: **VRAM Watcher (Bar)** (category: `utils`)
3. Configure the widgets in the node

### Node Settings

- **Interval (s)**: polling interval
- **Display**: `%` or `MB`
- **Order**: `VRAM→RAM` / `RAM→VRAM`

### WARNING Messages

Below the bars, a small message panel shows warnings and clears automatically when usage goes down.

- `VRAM WARNING`
- `RAM WARNING`

Threshold widgets:

- **VRAM Warn (%)**: shows `VRAM WARNING` when VRAM usage is above this
- **VRAM Warn Free (GiB)**: shows `VRAM WARNING` when free VRAM is below this
- **RAM Warn (%)**: shows `RAM WARNING` when RAM usage is above this

Tip: OOM can happen even when usage is below 90%, so using **VRAM Warn Free (GiB)** is recommended.

### Dependencies

- Uses `torch` from your ComfyUI environment
- Uses `psutil` for RAM stats on non-Linux platforms (see `requirements.txt`)

### License

MIT License. See [LICENSE](LICENSE).

### Changelog / Releases

- Changes are tracked in [CHANGELOG.md](CHANGELOG.md).
- For a new release: update `CHANGELOG.md`, bump the version in `pyproject.toml`, create a git tag (e.g. `v1.0.1`), then publish a GitHub Release.

### Troubleshooting

- **VRAM shows unavailable**
  - `torch.cuda.is_available()` is false (CPU-only, CUDA not installed, unsupported GPU, etc.)
- **RAM shows unavailable on Windows/macOS**
  - `psutil` might not be installed

 

---

## 日本語

ComfyUI の画面上に **VRAM / RAM 使用量バー**を表示するためのシンプルなカスタムノードです。

- VRAM: `torch.cuda` から取得（CUDA が無い場合は unavailable 表示）
- RAM: Linux では `/proc/meminfo`、それ以外は `psutil` があれば取得

### インストール（git clone）

`ComfyUI/custom_nodes` で:

```bash
git clone https://github.com/zwaigani/ComfyUI-VRAM-watcher.git
```

ComfyUI を再起動。

### 使い方

1. ComfyUI を起動
2. ノード追加から **`VRAM Watcher (Bar)`** を追加（カテゴリ: `utils`）
3. ノード内のウィジェットで表示を調整

### ノードの設定

- **Interval (s)**: ポーリング間隔（秒）
- **Display**: `%` または `MB`
- **Order**: `VRAM→RAM` / `RAM→VRAM`

### WARNING メッセージ

バーの下にメッセージパネルが表示され、条件を満たすと WARNING が出ます。空きが戻れば自動で消えます。

- `VRAM WARNING`
- `RAM WARNING`

しきい値（ウィジェットで調整可能）:

- **VRAM Warn (%)**: VRAM 使用率が指定以上で `VRAM WARNING`
- **VRAM Warn Free (GiB)**: 空きVRAMが指定以下で `VRAM WARNING`
- **RAM Warn (%)**: RAM 使用率が指定以上で `RAM WARNING`

※ OOM は使用率が 90% 未満でも発生し得るため、`VRAM Warn Free (GiB)` の併用がおすすめです。

### 依存関係

- ComfyUI の環境に含まれる `torch` を利用します
- RAM 表示を Linux 以外でも有効にするため `psutil` を使用します（`requirements.txt`）

### トラブルシュート

- **VRAM が unavailable**
  - `torch.cuda.is_available()` が false の環境です（CPU 実行、CUDA 未導入、対応GPUなし等）
- **RAM が unavailable（Windows/macOS 等）**
  - `psutil` がインストールされていない可能性があります

### ライセンス

MIT License（[LICENSE](LICENSE)）。
