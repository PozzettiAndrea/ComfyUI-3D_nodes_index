# ComfyUI AutoMosaic

`ComfyUI AutoMosaic` は、YOLOセグメンテーションモデルを使用して画像内の特定の領域（例：局部の露出など）を自動で検出し、モザイク処理やぼかし、白塗りなどの処理を行う [ComfyUI](https://github.com/comfyanonymous/ComfyUI) 用のカスタムノードです。PSDファイルとして各レイヤーを分けて保存する機能も備えています。

## 機能
- **特定領域の自動検出**: Ultralytics YOLO セグメンテーションモデルを利用し、指定したクラス名に該当する領域のマスクを検出します。（デフォルトでは `sensitive_detect_v06.pt` を使用）
- **画像処理モード**: 検出された領域に対して以下の処理を選択可能です。
  - `mosaic` (モザイク処理)
  - `blur` (ぼかし処理)
  - `white` (白塗り処理)
  - `raw` (処理なし、そのままのマスク領域)
- **PSD保存機能**: 処理されたレイヤーと元の背景画像を分けて、1つのPSDファイルとして保存することが可能です。（処理の微調整に便利です）
- **モデルの自動ダウンロード機能**: デフォルトの指定モデル (`sensitive_detect_v06.pt`) が見つからない場合は、自動的に HuggingFace からダウンロードするため、手動でモデルを配置する手間が省けます。

## インストール

1. **リポジトリのクローン**
   ComfyUIの `custom_nodes` ディレクトリで以下のコマンドを実行します。
   ```bash
   cd ComfyUI/custom_nodes
   git clone <このリポジトリのURL> comfyui-auto-mosaic
   ```

2. **依存関係のインストール**
   仮想環境またはComfyUIの環境内で以下のライブラリをインストールします。
   ```bash
   pip install -r comfyui-auto-mosaic/requirements.txt
   ```
   依存パッケージ:
   - `ultralytics` (YOLO用)
   - `psd-tools` (PSD保存用)
   - `opencv-python-headless` (画像処理用)

## ノードのパラメータ (Inputs)

`AutoMosaic` ノードの設定項目は以下の通りです。

| パラメータ名 | タイプ | デフォルト | 説明 |
| :--- | :---: | :--- | :--- |
| **`image`** | `IMAGE` | (必須) | 入力画像。 |
| **`save_psd`** | `BOOLEAN` | `False` | `True` にすると、出力フォルダに結果をPSDファイルとして保存します（レイヤー分けあり）。 |
| **`filename_prefix`** | `STRING` | `"AutoMosaic"` | 保存される画像のファイル名のプレフィックス。 |
| **`confidence`** | `FLOAT` | `0.5` | YOLOの検出の信頼度（Confidence）の閾値。最小0.01、最大1.0。値を低くするとより多くの領域を検出しますが、誤検知が増える可能性があります。 |
| **`process_method`** | `COMBO` | `"mosaic"` | 適用するエフェクト。`["raw", "mosaic", "white", "blur"]` から選択します。 |
| **`factor`** | `INT` | `100` | モザイクやぼかしのブロックサイズ・強度を決定する係数。値が小さいほどブロックサイズ（モザイク1マスのサイズ）が大きくなります。 |
| **`target_class`** | `STRING` | `"pussy,penis"` | モデルが検出する対象クラスの名前。複数ある場合はカンマ `,` 区切りで指定します。 |

## 出力 (Outputs)

- **`IMAGE`**: 処理後の合成画像。ComfyUIの他のノード（Save ImageノードやPreview Imageノードなど）へ接続して使用します。

## スタンドアローン WebUI (ComfyUI不要)
ComfyUI本体を起動しなくても、本ノードの機能をブラウザから直接試せるスタンドアローンのGradioベースWebUIを同梱しています。
**Single Image（単一画像処理）**と、フォルダ内の画像（サブフォルダ含む）を一括で処理する**Batch Process（バッチ処理）**の2つのモードに対応しています。

1. **WebUIの起動**
   付属のバッチファイルを実行するだけで、必要な環境（Python仮想環境の作成、ライブラリのインストール）が自動でセットアップされ、WebUIが起動します。
   ```bash
   # Windowsの場合
   start_standalone.bat
   ```
   ※ 初回起動時に `config.txt` ファイルがない場合は自動生成され、メモ帳が開きます。必要なPythonとCUDAのバージョンを指定して保存してください。

2. **ブラウザでアクセス**
   コンソールに表示されるURL（例: `http://127.0.0.1:7860`）にブラウザでアクセスして操作します。

## 処理の仕組み
1. **モデルのロード**: もし `sensitive_detect_v06.pt` が `models/ultralytics` または `models/yolo` にない場合は、HuggingFaceから自動でダウンロードされます。
2. **セグメンテーションの実行**: 各画像に対し YOLO モデルがマスクとバウンディングボックスを予測します。
3. **設定された処理の適用**: 検出されたクラス名が `target_class` に含まれている場合、その領域を切り抜いて `process_method` と `factor` に基づく画像処理を加えます。
4. **合成**: 背景ベースレイヤーと各加工後のマスクレイヤーを下から順に重ねて出力用のテンソルとして返します。（`save_psd`が有効で出力可能な場合は、PSDレイヤーとしても保存されます）。

## 既知の問題 / 制限事項
- 複数画像のバッチ（Batched Tensors）が入力された場合も順番に処理し、対応する数の結果を出力します。ただし各画像の出力結果ファイル名は連番（`_00001` 等）で保存されます。
- `save_psd` を使用する場合、大量のレイヤーまたは高解像度画像を処理するとメモリやストレージを消費しやすくなります。

---
**謝辞**: このノードは Ultralytics の YOLO リポジトリおよび psd-tools の技術基盤によって支えられています。デフォルトのモデルは [sugarknight/sensitive-detect](https://huggingface.co/sugarknight/sensitive-detect) を使用しています。
