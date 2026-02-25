# ComfyUI Model Downloader カスタムノード

HuggingFaceとCivitAIからモデルを直接ダウンロードできるComfyUIカスタムノードです。

## 3つのノード

### 1. Model Downloader (HF/CivitAI)
URL指定で個別ファイルまたは特定ディレクトリをダウンロード
- HuggingFace、CivitAI対応
- 柔軟なファイル指定

### 2. HuggingFace Directory Downloader 🆕
モデルIDでリポジトリ全体をダウンロード
- LLMやSDモデルに最適
- ディレクトリ構造を完全保持

### 3. Model Downloader from INI
INIファイルから一括ダウンロード
- 環境再現に最適
- プロジェクト管理

### インストール方法

### APIキーの設定（必須: CivitAI、オプション: HuggingFace）

多くのCivitAIモデルや、HuggingFaceのプライベート/Gatedモデルをダウンロードする場合、APIキーの設定が必要です。

#### config.iniファイルでの設定

```bash
cd ComfyUI/custom_nodes/model_downloader
cp config.ini.example config.ini
# config.iniを編集してAPIキーを記入
```

**config.ini の例:**
```ini
[API_KEYS]
# CivitAI API Key (多くのモデルで必須)
civitai_api_key = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# HuggingFace Token (プライベート/Gatedモデル用、オプション)
huggingface_token = hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

**APIキーの取得方法:**
- **CivitAI** (必須): https://civitai.com/user/account
  - "API Keys" セクションで "Add API Key" をクリック
  - 401 Unauthorized エラーを回避するために必要
  
- **HuggingFace** (オプション): https://huggingface.co/settings/tokens
  - "Read access to contents of all public gated repos you can access" を選択
  - プライベートリポジトリやGatedモデル（Llama 2, SDXL等）用

**セキュリティ上の注意:**
- config.iniにはAPIキーが含まれるため、Gitにコミットしないでください
- .gitignoreに自動的に追加されています

## 使い方

### ノード1: Model Downloader (HF/CivitAI)

個別のモデルをダウンロードするノードです。

#### ノードの追加

1. ComfyUIを起動
2. 右クリック → `Add Node` → `utils` → `Model Downloader (HF/CivitAI)`

### 入力パラメータ

#### 必須項目

- **url**: ダウンロードするモデルのURL
  - HuggingFace: `https://huggingface.co/username/repo/resolve/main/model.safetensors`
  - CivitAI: `https://civitai.com/api/download/models/123456`

- **subdirectory**: 保存先のサブディレクトリ（models以下）
  - 例: `checkpoints`, `loras`, `controlnet`, `embeddings`
  - **ネスト対応**: `loras/SDXL`, `controlnet/lineart`, `checkpoints/anime/sdxl`
  - スラッシュ(/)またはバックスラッシュ(\)でサブディレクトリを区切れます
  - セキュリティのため、`..`による親ディレクトリ参照は禁止されています

- **filename**: 保存するファイル名（省略可）
  - 空の場合はURLから自動検出

**自動バックアップ機能**
- ダウンロード情報は自動的にカスタムノード直下の `models.ini` に保存されます
- この`models.ini`は、ModelDownloaderFromINIノードで読み込んで一括ダウンロードに使用できます

#### オプション項目

- **exclude_files**: 除外するファイル名（カンマ区切り）
  - デフォルト: `README.md, .gitattributes`
  - ディレクトリダウンロード時のみ有効
  - 例: `README.md, .gitattributes, LICENSE, .git`
  - ファイル名の完全一致でフィルタリング

- **expected_hash**: SHA-256ハッシュ（検証用、省略可）
  - 指定すると、ダウンロード後にファイルの整合性を検証

- **max_retries**: 最大リトライ回数（デフォルト: 3）

**注意**: APIキーは`config.ini`ファイルで設定します（UIからの入力は不要）

### 出力

- **status**: ダウンロード結果のステータスメッセージ
- **file_path**: ダウンロードされたファイルの完全パス

### ノード2: HuggingFace Directory Downloader

HuggingFaceのリポジトリ全体をディレクトリ構造ごとダウンロードする専用ノードです。

#### 概要

**シンプルな使い方:**
- モデルID（例: `Qwen/Qwen2-VL-7B-Instruct`）を指定するだけ
- リポジトリ全体が`models/指定フォルダ/`以下にダウンロードされます
- ディレクトリ構造が完全に保持されます

**Model Downloaderとの違い:**
- Model Downloader: URL指定で個別ファイルや特定ディレクトリをダウンロード
- HuggingFace Directory Downloader: モデルIDのみでリポジトリ全体をダウンロード

#### ノードの追加

1. ComfyUIを起動
2. 右クリック → `Add Node` → `utils` → `HuggingFace Directory Downloader`

#### 入力パラメータ

##### 必須項目

- **model_id**: HuggingFaceのモデルID
  - 例: `Qwen/Qwen2-VL-7B-Instruct`
  - 例: `stabilityai/stable-diffusion-xl-base-1.0`
  - 例: `meta-llama/Llama-2-7b-hf`
  - フォーマット: `ユーザー名/リポジトリ名`

- **save_folder**: models以下の保存先フォルダ名
  - 例: `LLM` → `models/LLM/Qwen2-VL-7B-Instruct/`に保存
  - 例: `checkpoints/sdxl` → `models/checkpoints/sdxl/stable-diffusion-xl-base-1.0/`に保存
  - 例: `loras/anime` → `models/loras/anime/anime-lora-collection/`に保存
  - **自動的にリポジトリ名のサブフォルダが作成されます**

##### オプション項目

- **exclude_files**: 除外するファイル名（カンマ区切り）
  - デフォルト: `README.md, .gitattributes`
  - 例: `README.md, .gitattributes, LICENSE`
  - ファイル名の完全一致でフィルタリング

- **revision**: ブランチ/タグ名
  - デフォルト: `main`
  - 例: `v1.0`, `dev`, `legacy`

- **max_retries**: 最大リトライ回数（デフォルト: 3）

#### 出力

- **status**: ダウンロード結果のステータスメッセージ
- **download_path**: ダウンロード先のフルパス

#### ディレクトリ構造の保持

**HuggingFaceリポジトリの例:**
```
model-repo/
├─ config.json
├─ model.safetensors
├─ tokenizer/
│  ├─ tokenizer.json
│  └─ special_tokens_map.json
└─ scheduler/
   └─ scheduler_config.json
```

**ダウンロード後（save_folder: LLM, model_id: user/model-repo）:**
```
models/LLM/model-repo/
├─ config.json
├─ model.safetensors
├─ tokenizer/
│  ├─ tokenizer.json
│  └─ special_tokens_map.json
└─ scheduler/
   └─ scheduler_config.json
```

**リポジトリ名のサブフォルダが自動作成されます**
完全に同じディレクトリ構造が再現されます。

#### 使用例

##### 例1: LLMモデルのダウンロード

```
model_id: Qwen/Qwen2-VL-7B-Instruct
save_folder: LLM
→ models/LLM/Qwen2-VL-7B-Instruct/ にリポジトリ全体をダウンロード
```

##### 例2: Stable Diffusion XLモデル

```
model_id: stabilityai/stable-diffusion-xl-base-1.0
save_folder: checkpoints/sdxl
→ models/checkpoints/sdxl/stable-diffusion-xl-base-1.0/ にリポジトリ全体をダウンロード
```

##### 例3: 特定バージョンのダウンロード

```
model_id: meta-llama/Llama-2-7b-hf
save_folder: LLM
revision: v1.0
→ models/LLM/Llama-2-7b-hf/ にv1.0タグのリポジトリをダウンロード
```

##### 例4: カスタム除外設定

```
model_id: runwayml/stable-diffusion-v1-5
save_folder: checkpoints
exclude_files: README.md, .gitattributes, LICENSE, model_index.json
→ models/checkpoints/stable-diffusion-v1-5/ に指定したファイルを除外してダウンロード
```

#### 注意事項

**HuggingFaceトークンについて:**
- 公開モデル: トークン不要
- プライベートリポジトリ/Gated Models: config.iniにトークンが必要
- トークンは自動的に使用されます

**既存ファイルのスキップ:**
- 同名ファイルが既に存在する場合、自動的にスキップされます
- 再ダウンロードしたい場合は、既存ファイルを削除してください

**ストレージ容量:**
- LLMモデルは数GB〜数十GBになる場合があります
- ダウンロード前に十分な空き容量があることを確認してください

### ノード3: Model Downloader from INI

models.iniファイルから複数のモデルを一括ダウンロードするノードです。

#### ノードの追加

1. ComfyUIを起動
2. 右クリック → `Add Node` → `utils` → `Model Downloader from INI`

#### 入力パラメータ

##### 必須項目

- **ini_file_path**: INIファイルのパス
  - 空欄の場合: カスタムノード直下の `models.ini` を使用（デフォルト）
  - 指定する場合: 任意のパスを指定可能
  - 対応形式:
    - `"E:\desktop\model1.ini"` (ダブルクォート付き、バックスラッシュ)
    - `E:\desktop\model2.ini` (クォートなし、バックスラッシュ)
    - `E:/desktop/model3.ini` (スラッシュ)
    - `models.ini` (相対パス - カスタムノードディレクトリからの相対)

##### オプション項目

- **max_retries**: 最大リトライ回数（デフォルト: 3）
- **skip_existing**: 既存ファイルをスキップ（デフォルト: True）
- **update_directory_ini**: ディレクトリ構造変更時にINIを更新（デフォルト: False）
  - ディレクトリダウンロードで、ファイル数やパスが変更された場合のみINIを更新

#### 出力

- **status**: 一括ダウンロードの結果サマリー
- **summary**: 詳細な統計情報

## 使用例

### 例1: HuggingFaceからLoRAをダウンロード

```
URL: https://huggingface.co/tori29umai/lineart/resolve/main/sdxl_BWLine.safetensors
Subdirectory: loras
Filename: sdxl_BWLine.safetensors
```

### 例2: CivitAIからControlNetをダウンロード

```
URL: https://civitai.com/api/download/models/515749?type=Model&format=SafeTensor
Subdirectory: controlnet
Filename: (空欄でOK - 自動検出)
Expected Hash: 58bae8a373d6a39b33a5d110c5b22894fc86b7b1e189b05b163e69446c7f48ee
```

### 例3: カスタムパスに保存

```
URL: https://huggingface.co/stabilityai/sdxl-turbo/resolve/main/sd_xl_turbo_1.0.safetensors
Subdirectory: checkpoints/sdxl
Filename: sdxl_turbo.safetensors
```

### 例4: ネストされたディレクトリに保存

```
URL: https://huggingface.co/tori29umai/lineart/resolve/main/sdxl_BWLine.safetensors
Subdirectory: loras/SDXL/lineart
Filename: sdxl_BWLine.safetensors
```

### 例5: 複数階層のディレクトリ構造

```
URL: https://huggingface.co/cagliostrolab/animagine-xl-3.1/resolve/main/animagine-xl-3.1.safetensors
Subdirectory: checkpoints/anime/sdxl/animagine
Filename: animagine-xl-3.1.safetensors
```

### 例6: HuggingFaceディレクトリごとダウンロード 🆕

```
URL: https://huggingface.co/2vXpSwA7/iroiro-lora/tree/main/qwen_lora
Subdirectory: loras/qwen
Filename: (空欄 - ディレクトリ内の全ファイルをダウンロード)
```

**動作:**
- `qwen_lora` ディレクトリ内の全ファイルを自動検出
- ディレクトリ構造を維持して `loras/qwen/` 以下に保存
- サブディレクトリも再帰的にダウンロード
- **既存ファイルは自動的にスキップ**（重複ダウンロードを防止）
- `update_directory_ini=False`（デフォルト）: models.iniは更新しない
- `update_directory_ini=True`: ディレクトリ構造が変更された場合のみmodels.iniを更新

**対応URL形式:**
```
https://huggingface.co/{user}/{repo}/tree/{revision}/{directory_path}

例:
- https://huggingface.co/2vXpSwA7/iroiro-lora/tree/main/qwen_lora
- https://huggingface.co/user/repo/tree/main
- https://huggingface.co/user/repo/tree/main/subfolder/deep
```

### 例7: HuggingFace Directory Downloaderでリポジトリ全体をダウンロード 🆕

**ノード:** HuggingFace Directory Downloader

#### 例7-1: LLMモデルのダウンロード

```
model_id: Qwen/Qwen2-VL-7B-Instruct
save_folder: LLM
revision: main
exclude_files: README.md, .gitattributes
```

**結果:**
```
models/LLM/Qwen2-VL-7B-Instruct/
├─ config.json
├─ model.safetensors
├─ tokenizer/
│  ├─ tokenizer.json
│  └─ special_tokens_map.json
├─ scheduler/
│  └─ scheduler_config.json
└─ ... (その他全ファイル)
```

#### 例7-2: Stable Diffusion XLモデル

```
model_id: stabilityai/stable-diffusion-xl-base-1.0
save_folder: checkpoints
```

**結果:**
```
models/checkpoints/stable-diffusion-xl-base-1.0/
├─ model_index.json
├─ scheduler/
├─ text_encoder/
├─ text_encoder_2/
├─ tokenizer/
├─ tokenizer_2/
├─ unet/
└─ vae/
```

#### 例7-3: 特定バージョンのダウンロード

```
model_id: meta-llama/Llama-2-7b-hf
save_folder: LLM
revision: v1.0
```

**結果:**
```
models/LLM/Llama-2-7b-hf/
└─ ... (v1.0のファイル)
```

#### Model Downloaderとの使い分け

**HuggingFace Directory Downloader（新しいノード）を使う場合:**
- リポジトリ全体をダウンロードしたい
- モデルIDがわかっている
- シンプルに使いたい

```
✅ model_id: Qwen/Qwen2-VL-7B-Instruct
✅ save_folder: LLM
```

**Model Downloader (HF/CivitAI)を使う場合:**
- 特定のファイルだけダウンロードしたい
- CivitAIからダウンロードしたい
- URLが既にある

```
✅ url: https://huggingface.co/.../file.safetensors
✅ subdirectory: checkpoints
```

## models.ini による環境再現

### 自動記録機能

モデルをダウンロードすると、自動的にカスタムノードディレクトリ直下の `models.ini` に記録されます。

**INIファイルの場所:**
```
ComfyUI/custom_nodes/model_downloader/models.ini
```

### models.iniの形式

#### 1. 個別ファイル形式（Model Downloader）

**Model Downloader (HF/CivitAI)を使用した場合：**

```ini
[sdxl_BWLine_safetensors]
url = https://huggingface.co/tori29umai/lineart/resolve/main/sdxl_BWLine.safetensors
subdirectory = loras/SDXL
filename = sdxl_BWLine.safetensors
filepath = loras/SDXL/sdxl_BWLine.safetensors
hash = 07c59708361b3e2e4f0b0c0f232183f5f39c32c31b6b6981b4392ea30d49dd57
timestamp = 2024-11-27 12:34:56
```

#### 2. HuggingFace Directory形式 🆕

**HuggingFace Directory Downloaderを使用した場合：**

```ini
[HF_DIR_Qwen2_VL_7B_Instruct]
type = huggingface_directory
model_id = Qwen/Qwen2-VL-7B-Instruct
save_folder = LLM
revision = main
exclude_files = README.md, .gitattributes
file_count = 45
timestamp = 2024-11-27 12:00:00
```

**重要:** 
- HuggingFace Directory Downloaderは**リポジトリ全体の情報のみ**を保存します
- 個別ファイルは保存しません（リポジトリ情報だけで再ダウンロード可能なため）
- これにより、models.iniがシンプルで管理しやすくなります

#### 3. 混在例

```ini
# HuggingFace Directoryダウンロード
[HF_DIR_Qwen2_VL_7B_Instruct]
type = huggingface_directory
model_id = Qwen/Qwen2-VL-7B-Instruct
save_folder = LLM
revision = main
exclude_files = README.md, .gitattributes

# 個別ファイルダウンロード
[sdxl_turbo_safetensors]
url = https://huggingface.co/stabilityai/sdxl-turbo/resolve/main/sd_xl_turbo_1.0.safetensors
subdirectory = checkpoints/sdxl
filename = sdxl_turbo.safetensors

# HuggingFace Directoryダウンロード
[HF_DIR_stable_diffusion_xl_base_1_0]
type = huggingface_directory
model_id = stabilityai/stable-diffusion-xl-base-1.0
save_folder = checkpoints
revision = main
```

### Model Downloader from INIでの処理

**自動認識:**
- `type = huggingface_directory`: HuggingFaceDirectoryDownloaderを使用
- `type` なしまたは `type = file`: ModelDownloaderを使用

**一括ダウンロード:**
```
Model Downloader from INI ノード
└─ ini_file_path: （空欄 - デフォルト）

結果:
✓ HuggingFace Directory形式を自動認識
✓ 通常のファイル形式も処理
✓ 全てのモデルを一括ダウンロード
```

[animagine-xl-3_1_safetensors]
url = https://huggingface.co/cagliostrolab/animagine-xl-3.1/resolve/main/animagine-xl-3.1.safetensors
subdirectory = checkpoints
filename = animagine-xl-3.1.safetensors
filepath = checkpoints/animagine-xl-3.1.safetensors
hash = e3c47aedb06418c6c331443cd89f2b3b3b34b7ed2102a3d4c4408a8d35aad6b0
timestamp = 2024-11-27 12:35:10
```

### 別PCでの環境再現手順

1. **元のPCでmodels.iniを取得**
   ```bash
   # models.iniをコピー
   cp ComfyUI/custom_nodes/model_downloader/models.ini ~/backup/
   ```

2. **新しいPCにmodels.iniを配置**
   ```bash
   # 新しいPCで（カスタムノードインストール後）
   cp ~/backup/models.ini ComfyUI/custom_nodes/model_downloader/
   ```

3. **ComfyUIで一括ダウンロード**
   - `Model Downloader from INI` ノードを追加
   - `ini_file_path` を空欄のまま実行（カスタムノード直下のmodels.iniを使用）
   - または、カスタムパスを指定

### 手動でmodels.iniを編集

models.iniを手動で編集して、カスタムモデルリストを作成することもできます。

```ini
[my_custom_model]
url = https://huggingface.co/username/repo/resolve/main/model.safetensors
subdirectory = loras
filename = custom_model.safetensors
hash = <optional_sha256_hash>
```

## 特徴

### URL自動判定

URLを入力すると、自動的にHuggingFaceかCivitAIかを判定し、適切な方法でダウンロードします。

### ネストされたディレクトリ対応

`loras/SDXL`や`checkpoints/anime/sdxl`のように、複数階層のサブディレクトリを指定できます。
- スラッシュ(`/`)またはバックスラッシュ(`\`)でディレクトリを区切れます
- 指定されたディレクトリ構造が存在しない場合は自動的に作成されます
- セキュリティのため、`..`による親ディレクトリ参照は禁止されています

例:
```
checkpoints/anime/sdxl/animagine  → models/checkpoints/anime/sdxl/animagine/
loras/SDXL                        → models/loras/SDXL/
controlnet/lineart/v2             → models/controlnet/lineart/v2/
```

### ハッシュ検証

SHA-256ハッシュを指定すると、ダウンロード後にファイルの整合性を自動検証します。
ハッシュが一致しない場合は自動的にリトライします。

### 既存ファイルの処理

同名のファイルが既に存在する場合:
1. ハッシュが指定されている → 検証して一致すればスキップ
2. ハッシュが指定されていない → 再ダウンロードせずにスキップ

### エラーハンドリング

- ネットワークエラー時は自動リトライ
- ハッシュ不一致時は自動リトライ
- 最大リトライ回数に達したらエラーメッセージを表示

## ノード比較表

| 特徴 | Model Downloader | HuggingFace Directory Downloader | Model Downloader from INI |
|------|-----------------|----------------------------------|---------------------------|
| **用途** | 個別ファイルまたは特定ディレクトリ | リポジトリ全体 | 一括ダウンロード |
| **入力** | URL | モデルID | INIファイル |
| **HuggingFace** | ✅ | ✅ | ✅ |
| **CivitAI** | ✅ | ❌ | ✅ |
| **ディレクトリ構造保持** | ✅ (部分的) | ✅ (完全) | ✅ |
| **シンプルさ** | 中 | 高 | 中 |
| **柔軟性** | 高 | 低 | 高 |
| **おすすめ用途** | 個別ファイル、CivitAI | LLM、SDモデル全体 | 環境再現、バッチ処理 |

### 使い分けガイド

**HuggingFace Directory Downloaderを使う:**
- ✅ LLMモデルを丸ごとダウンロードしたい
- ✅ Stable Diffusionモデル全体が必要
- ✅ モデルIDだけわかっている
- ✅ シンプルに使いたい

**Model Downloader (HF/CivitAI)を使う:**
- ✅ 特定のファイルだけ欲しい
- ✅ CivitAIからダウンロードしたい
- ✅ URLが既にある
- ✅ 細かく制御したい

**Model Downloader from INIを使う:**
- ✅ 複数のモデルを一括ダウンロードしたい
- ✅ 環境を再現したい
- ✅ プロジェクトごとにモデルを管理したい

## トラブルシューティング

### ダウンロードが失敗する

- インターネット接続を確認
- URLまたはモデルIDが正しいか確認
- CivitAIの場合、config.iniにAPIキーが設定されているか確認
- HuggingFaceのプライベート/Gatedモデルの場合、config.iniにトークンが設定されているか確認

### 401 Unauthorized エラー (CivitAI)

- config.iniにCivitAI APIキーを設定してください
- APIキーの取得: https://civitai.com/user/account

### 403 Forbidden エラー (HuggingFace)

- プライベートリポジトリまたはGated Modelの可能性があります
- HuggingFaceのモデルページで利用規約に同意してください
- config.iniにHuggingFaceトークンを設定してください

### HuggingFace Directory Downloaderでダウンロードが遅い

- LLMモデルは数GB〜数十GBあります
- 進捗表示を確認してください
- ネットワーク速度に依存します

### モデルIDが見つからない

- HuggingFaceのウェブサイトでモデルIDを確認してください
- フォーマット: `ユーザー名/リポジトリ名` (例: `Qwen/Qwen2-VL-7B-Instruct`)
- 大文字小文字を正確に入力してください

### ハッシュ検証が失敗する

- ハッシュ値が正しいか確認（大文字小文字は無視されます）
- ファイルが破損している可能性があるため、再ダウンロードを試す

### ファイルが見つからない

- ComfyUIの `models` ディレクトリを確認
- 指定したサブディレクトリが正しいか確認

