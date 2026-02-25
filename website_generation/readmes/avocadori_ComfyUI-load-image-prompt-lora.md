# ComfyUI YAML Image Cycler ノード

指定したカテゴリの画像を順番に巡回しながら、YAMLファイルに定義されたプロンプト、LoRA設定、マスクを一緒に出力するComfyUIカスタムノードです。

## 機能

- 指定フォルダ内の画像を順番に巡回表示
- YAMLファイルからプロンプトとLoRA設定を自動読み込み
- 画像に対応するマスクの自動検索・読み込み
- カテゴリ別の設定管理
- 複数のLoRA（最大3つ）に対応
- Set_LoadMaskノードへのマスク出力対応
- モジュラー設計による柔軟な使用方法

## ノード構成

### 1. YAML Image Cycler (Full)
- 画像、マスク、プロンプト、LoRA情報をすべて出力する統合ノード
- 従来の機能をすべて含む

### 2. YAML LoRA Extractor
- YAMLファイルからLoRA情報のみを抽出する専用ノード
- LoRA名前と重みを分離して出力
- WanVideo Lora Selectノードとの互換性を重視

### 3. YAML Image Cycler (Simple)
- 画像とマスクのみを出力するシンプルなノード
- 軽量で高速な画像巡回機能

## インストール方法

1. ComfyUIの`custom_nodes`フォルダ内に本フォルダをコピー
2. ComfyUIを再起動

## ファイル構成

```
yaml_image_cycler/
├── __init__.py                    # ノード登録ファイル
├── yaml_image_cycler.py           # 統合ノード（フル機能）
├── yaml_lora_extractor.py         # LoRA抽出専用ノード
├── yaml_image_cycler_simple.py    # シンプル画像巡回ノード
├── setting.yaml                   # 設定ファイル（サンプル）
└── README.md                     # このファイル
```

## 使用方法

### 1. フォルダ構成の準備

```
data/
├── character1/
│   ├── img001.png
│   ├── img002.jpg
│   ├── img003.webp
│   └── masks/              # マスクフォルダ（オプション）
│       ├── img001.png
│       ├── img002.png
│       └── img003.png
├── character2/
│   ├── portrait01.png
│   └── portrait02.jpg
├── background/
│   ├── landscape01.png
│   └── landscape02.png
└── masks/                  # 共通マスクフォルダ（オプション）
    └── background/
        ├── landscape01.png
        └── landscape02.png
```

### 2. YAML設定ファイルの編集

`setting.yaml`を編集して、各カテゴリの設定を定義：

```yaml
character1:
  prompt: "1girl, beautiful, anime style, detailed face"
  lora1: "<lora:character1_v1:0.8>"
  lora2: "<lora:anime_style:0.6>"
  lora3: ""
  mask_folder: "character1/masks"  # オプション: マスクフォルダを指定

character2:
  prompt: "1boy, handsome, realistic, portrait"
  lora1: "<lora:character2_v2:0.9>"
  lora2: "<lora:realistic_style:0.7>"
  lora3: "<lora:portrait_enhance:0.5>"
  # mask_folder未指定の場合は自動検索

background:
  prompt: "beautiful landscape, detailed background, high quality"
  lora1: "<lora:landscape_v1:0.8>"
  lora2: ""
  lora3: ""
  mask_folder: "masks/background"  # 共通マスクフォルダを指定
```

### 3. 推奨使用パターン

#### パターンA: 統合ノード使用
```
YAML Image Cycler (Full) → 各種出力先ノード
```
- すべての機能を1つのノードで使用
- シンプルな構成

#### パターンB: モジュラー構成（推奨）
```
YAML Image Cycler (Simple) → 画像・マスク出力
YAML LoRA Extractor → WanVideo Lora Select
```
- 機能分離による柔軟性
- LoRA設定の独立管理
- WanVideo Lora Selectとの完全互換

### 4. 各ノードの出力

#### YAML Image Cycler (Full)
- `image`: 巡回中の画像（ComfyUI IMAGE形式）
- `mask`: 対応するマスク（ComfyUI MASK形式）
- `prompt`: YAMLで定義されたプロンプト
- `lora1`, `lora2`, `lora3`: LoRA名前（文字列）

#### YAML LoRA Extractor
- `prompt`: YAMLで定義されたプロンプト
- `lora1_name`, `lora2_name`, `lora3_name`: LoRA名前
- `lora1_weight`, `lora2_weight`, `lora3_weight`: LoRA重み（浮動小数点）

#### YAML Image Cycler (Simple)
- `image`: 巡回中の画像（ComfyUI IMAGE形式）
- `mask`: 対応するマスク（ComfyUI MASK形式）
- `category`: 現在のカテゴリ名

## マスク機能の詳細

### マスクの自動検索

- 画像ファイル名と同じ名前のマスクファイルを自動検索
- マスクが見つからない場合は空のマスク（全て0）を自動生成
- マスクはグレースケール画像として読み込まれ、ComfyUI MASK形式に変換

### 対応マスク形式

- PNG (.png)
- JPEG (.jpg, .jpeg)
- BMP (.bmp)
- WebP (.webp)

### Set_LoadMaskノードとの連携

出力されたマスクはSet_LoadMaskノードに直接接続して使用できます。

## LoRA機能の詳細

### LoRA名前抽出

- `<lora:character1_v1:0.8>` → 名前: `character1_v1`, 重み: `0.8`
- WanVideo Lora Selectノードとの完全互換
- LoRAファイルの存在確認機能付き

### LoRAファイル検索

- ComfyUIの`models/loras`フォルダを自動検索
- 対応拡張子：`.safetensors`, `.ckpt`, `.pt`, `.pth`
- 見つからない場合は詳細な警告メッセージを表示

## 対応画像形式

- PNG (.png)
- JPEG (.jpg, .jpeg)
- BMP (.bmp)
- WebP (.webp)
- TIFF (.tiff)
- TGA (.tga)

## 注意事項

- 画像は各カテゴリフォルダ内でアルファベット順にソートされます
- 巡回状態は各カテゴリごとに独立して管理されます
- YAMLファイルが存在しない場合、カテゴリは手動入力になります
- 画像フォルダが存在しないか空の場合はエラーが発生します
- マスクファイルが見つからない場合は空のマスクが自動生成されます

## トラブルシューティング

### よくあるエラー

1. **「YAMLファイルが見つかりません」**
   - `yaml_path`で指定したファイルが存在するか確認
   - ファイルパスが正しいか確認

2. **「フォルダがありません」**
   - `parent_dir`で指定したフォルダが存在するか確認
   - カテゴリ名に対応するサブフォルダが存在するか確認

3. **「画像が見つかりません」**
   - 指定フォルダ内に対応形式の画像ファイルがあるか確認
   - ファイル拡張子が対応形式か確認

4. **「LORA models are expected to be in ComfyUI/models/loras」**
   - LoRAファイルが正しいフォルダに配置されているか確認
   - ファイル名がYAMLの設定と一致しているか確認

### デバッグ情報

各ノード実行時にコンソールに詳細な情報が出力されます：

```
[YAMLImageCycler] カテゴリ: character1, 画像: img001.png (1/3)
[YAMLLoRAExtractor] LoRA1: character1_v1 (重み: 0.8)
[YAMLImageCyclerSimple] マスク読み込み: img001.png
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。
