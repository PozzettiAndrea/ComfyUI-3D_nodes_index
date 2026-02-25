# u5_FreeVRAM - ComfyUI Memory Management Node

ComfyUI向けの高度なメモリ管理・VRAM最適化カスタムノードです。
既存のメモリ開放系のカスタムノードがどうにもうまく動かないので、改めて作りました。

 [English](docs/en/README.md) | [中文](docs/zh/README.md)  

## 📋 目次

- [概要](#概要)
- [機能](#機能)
- [インストール](#インストール)
- [基本的な使い方](#基本的な使い方)
- [Sequential Loaders](#sequential-loaders)
- [ベストプラクティス](#ベストプラクティス)
- [パラメータリファレンス](#パラメータリファレンス)
- [動作環境](#動作環境)
- [トラブルシューティング](#トラブルシューティング)
- [開発](#開発)
- [ライセンス](#ライセンス)

---
## 概要

u5_FreeVRAMは、ComfyUIワークフローにおけるメモリ管理を最適化し、限られたVRAMで複雑なワークフローを実現するためのカスタムノードパッケージです。

要するに、ワークフローの途中で任意にVRAMを開放したり、読み替えたりできるようにします。

---
### 主な用途

- **複雑なワークフロー**: 1ワークフロー内で複数種のモデルを順次実行（線画化→着色等）
- **バッチ処理**: メモリリークの防止
- **SaaS環境**: 共有GPU環境でのキャッシュクリア
---
## 機能
このcustom nodeには、主に2種類の機能があります。


### 1. FREE VRAM ノード

VRAMメモリのクリーンアップを提供します。

**クリーンアップ処理**:
- **モデルアンロード**: ロード済みモデルをメモリから解放
- **GPUキャッシュクリア**: CUDAキャッシュを空にしてVRAMを回復
- **実行キャッシュクリア**: ComfyUIの実行キャッシュをクリア
- **ガベージコレクション**: Pythonの未使用オブジェクトを回収

**スマート実行**:
- **閾値スキップ**: 指定した空きVRAMがある場合は処理をスキップ
- **非同期待機**: 最適なメモリ解放タイミングを自動検出

### 2. Sequential Loaders

モデルの順次ロードを実現し、VRAM使用量を最適化します。

通常、モデル等のローダーは入力ソケットを持たず、ワークフローのど頭で並列実行されますが、
ワークフローの途中で差し込めるようにしました。

**利用可能なローダー**:
- **Sequential Checkpoint Loader**: チェックポイントファイルの順次ロード
- **Sequential LoRA Loader**: LoRAファイルの順次ロード
- **Sequential CLIP Loader**: CLIPモデルの順次ロード（safetensors、全CLIPタイプ対応）
- **Sequential VAE Loader**: VAEモデルの順次ロード（safetensors、TAESD対応）
※GGUF形式には対応していません（無理でした）

**特徴**:
- ComfyUI標準機能のみ使用（外部依存なし）
- `trigger`入力による実行順序の制御
---
## インストール

1. gitを`custom_node`フォルダにCloneしてください。
```bash
git clone "https://github.com/u5dev/comfyUI_u5_VramFREE.git"
```

2. ComfyUIを再起動してください。

---
## 基本的な使い方

ノードメニューの`u5`カテゴリにノードが表示されます。

### FREE VRAM ノード

ワークフローの任意の位置に挿入してメモリをクリアします。

**使用方法**:
![alt text](docs/img/image-1.png)

```
# 中継ノードとして
[任意のノード] → [FREE VRAM] → [次のノード]
```

**パラメータ**:
- **Any** (入力・オプション): 任意のデータ型を受け取るパススルー入力
  - **未接続でも動作**: ワークフローの開始ノードとして配置可能
  - **接続時**: 入力データをそのまま出力に中継
- **MinFreeVRAMGB** (オプション): この値以上の空きVRAMがある場合はスキップ（デフォルト: 0.0）
※メモリの開放状況は非同期のラグがあるため、厳密ではありません。

**出力**:
- **Bypass(Relay)**: 入力データを中継（入力がない場合はNone）


---
## Sequential Loaders

Sequential Loadersは`trigger`入力を持ち、前のノードの完了を待ってからロードを開始します。
`trigger`に来たものは、そのまま`Bypass(Relay)`出力ソケットに渡されます。

使い方は、下記のワークフロー例を参考にしてください。

---
## ベストプラクティス

### 1. SaaS環境でのキャッシュクリア

**ユースケース**: 共有GPU環境で、前のユーザーのキャッシュを確実にクリアする

![alt text](docs/img/image.png)

```
[Start Workflow]
    ↓
[FREE VRAM (MinFreeVRAMGB=0.0)] ← 強制的にクリーンアップ
    ↓ trigger
[Sequential Checkpoint Loader] ← 解放後に読み込み
    ↓ (MODEL, CLIP, VAE)
[CLIP Text Encode (Prompt)]
    ↓ (CONDITIONING)
[KSampler]
    ↓ (LATENT)
[VAE Decode]
    ↓ (IMAGE)
[Save Image]
```

**ポイント**:
- ワークフロー開始直後にFreeVRAMを配置
- `MinFreeVRAMGB=0.0`で常にクリーンアップを強制
- Sequential Loaderを使用して順序を保証

### 2. 低VRAM環境での複数モデル実行（8GB以下）

**ユースケース**: image2imageを2PassのSDXLで実行


![alt text](docs/img/image-2.png)
```
1st Pass は下絵（img2imgの下地）を軽設定で生成してプレビュー。
2nd Pass は FreeVRAM のゲートを通してメモリを確保してから、
Checkpoint → LoRA → VAE を順次読み込み、本番設定で生成・保存。
```

**ポイント**:
共通：positive/negativeテキスト→CLIPエンコードし、両パスのサンプラーへ。

1st Pass：i2i用画像→1024x1024化→VAEエンコード→Kサンプラー(下絵生成)
　　↓
2nd Pass：latent(潜在)をFreeVRAM以降のトリガーに繋いで引き回す
　　↓
Sequential Checkpoint Loader（清書用）
　　↓
Sequential LoRA Loader（複数LoRA適用）
　　↓
Kサンプラー（※latentをバイパスしてきて、Kサンプラーまで引き込む）
　　↓
Sequential VAE Loader（清書用VAE）
　　↓
VAEデコード
　　↓
画像を保存

※1stは当たり出し、2ndでLoRAと別VAEを順次ロードして仕上げ、メモリ圧をFree VRAMで制御します。

---
## パラメータリファレンス

### FREE VRAM ノード

| パラメータ | 型 | 必須 | デフォルト | 説明 |
|-----------|-----|------|-----------|------|
| Any | ANY | ✗ (オプション) | None | パススルー入力（任意のデータ型）、未接続でも動作 |
| MinFreeVRAMGB | FLOAT | ✗ (オプション) | 0.0 | この値以上の空きVRAMがある場合はスキップ（GB） |

**出力**:
- **Bypass(Relay)**: 入力データをそのまま出力（入力なしの場合はNone）

**v1.1での変更点**:
- Any入力が**オプション**になり、開始ノードとして使用可能

### Sequential Checkpoint Loader

| パラメータ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| ckpt_name | COMBO | - | チェックポイントファイル名 |
| trigger | ANY | None | 実行順序制御用入力（オプション） |

**出力**:
- MODEL, CLIP, VAE, Bypass(Relay)

### Sequential CLIP Loader

| パラメータ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| clip_name | COMBO | - | CLIPファイル名（.safetensors） |
| type | COMBO | stable_diffusion | CLIPタイプ（stable_diffusion, qwen_image, etc.） |
| trigger | ANY | None | 実行順序制御用入力（オプション） |

**出力**:
- CLIP, Bypass(Relay)

**対応CLIPタイプ**:
- stable_diffusion (SD 1.x/2.x)
- stable_cascade (Stable Cascade)
- sdxl (SDXL)
- sd3 (SD3)
- flux (Flux)
- qwen_image (Qwen2-VL)
- など

### Sequential VAE Loader

| パラメータ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| vae_name | COMBO | - | VAEファイル名（.safetensors/.pt）またはTAESD variant |
| trigger | ANY | None | 実行順序制御用入力（オプション） |

**出力**:
- VAE, Bypass(Relay)

**対応VAE**:
- safetensors形式の標準VAE
- TAESD variants: taesd, taesdxl, taesd3, taef1

### Sequential LoRA Loader

| パラメータ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| model | MODEL | - | 入力モデル |
| clip | CLIP | - | 入力CLIP |
| lora_name | COMBO | - | LoRAファイル名 |
| strength_model | FLOAT | 1.0 | モデルへの適用強度 |
| strength_clip | FLOAT | 1.0 | CLIPへの適用強度 |
| trigger | ANY | None | 実行順序制御用入力（オプション） |

**出力**:
- MODEL, CLIP, Bypass(Relay)
---
## 動作環境

### 必須要件
- **ComfyUI**: 最新版推奨
- **Python**: 3.8以上
- **PyTorch**: ComfyUIに含まれるバージョン
- **GPU**: CUDA対応推奨（CPU版でも動作）

### オプション
- **psutil** 5.8.0以上: システムメモリ情報の詳細表示
  ```bash
  pip install psutil
  ```

### 推奨環境
- **VRAM**: ComfyUIでとりあえずKサンプラーが動かせるぐらい
- **RAM**: 同上
- **OS**: ComfyUIが動く環境
---
## トラブルシューティング

### メモリが解放されない

**原因と対策**:

1. **MinFreeVRAMGBが高すぎる**
   - 現在の空きVRAMを確認: `nvidia-smi`
   - `MinFreeVRAMGB=0.0`で強制実行をテスト

2. **他のプロセスがGPUを使用**
   - 他のComfyUIインスタンスを確認
   - ブラウザのハードウェアアクセラレーションを無効化
   - GPU使用アプリケーションを終了

3. **ComfyUIの実行キャッシュ**
   - ComfyUI Managerの"Free model and cache"と併用
   - ComfyUIを再起動

### Sequential Loadersが動作しない

**原因と対策**:

1. **trigger接続忘れ**
   - 全ての`trigger`入力/出力が正しく接続されているか確認
   - 接続が1つでも欠けると順序保証されない

2. **import エラー**
   - コンソールログを確認
   - ComfyUIを再起動
   - カスタムノードの再インストール

3. **ファイルが見つからない**
   - モデルファイルが正しいフォルダに配置されているか確認


**重要なログメッセージ(ComfyUI コンソール)**:
- `[FreeVRAM] Sequential Loaders loaded successfully` - 正常ロード
- `VRAM FREE (u5): Cleared: Models, Cache, GC | Freed: X.XX GB` - クリーンアップ成功


---
## ライセンス

詳細は[LICENSE](LICENSE)ファイルを参照してください。

---
## 謝辞

このプロジェクトは以下の技術を使用しています:
- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) - 強力なノードベースUIフレームワーク
- [PyTorch](https://pytorch.org/) - ディープラーニングフレームワーク

---

**バージョン**: 1.1.0
**最終更新**: 2025-10-02
**開発**: u5dev