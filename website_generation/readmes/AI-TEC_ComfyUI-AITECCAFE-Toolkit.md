# ComfyUI-AITECCAFE-Toolkit

このリポジトリには、AITECCAFEによって開発されたComfyUI用のカスタムノードが含まれています。

## note紹介
[noteに投稿したノードの紹介文です](https://note.com/ai_tec/n/ne3d398fe9548)

## インストール

### ComfyUI Manager
1. ComfyUIを起動します。
2. ComfyUI Managerを開きます。
3. Custom Nodes Managerを開きます。
4. "AITECCAFE"で検索するなどして、ComfyUI_AITECCAFE_Toolkitをインストールします。
    ![ComfyUI Manager](https://github.com/AI-TEC/images/blob/main/0001.jpg)
5. ComfyUIを再起動します。

### コマンドライン
1. ComfyUIの `custom_nodes` フォルダに移動します。
2. 以下のコマンドを使用して、このリポジトリをクローンします。
   ```bash
   git clone https://github.com/AI-TEC/ComfyUI-AITECCAFE-Toolkit
   ```
3. 必要な依存関係をインストールします。
   ```bash
   pip install -r ComfyUI-AITECCAFE-Toolkit/requirements.txt
   ```
4. ComfyUIを再起動します。

## ノード一覧
<img src="https://github.com/AI-TEC/images/blob/main/0002.jpg" alt="Node List">
このToolkitには以下のノードが含まれています。

*   **ChatGPT Text Generator**: ChatGPT APIを使用してテキストを生成します。
*   **OpenAI Image Moderation**: OpenAIのモデレーションAPIを使用して画像を分析し、不適切なコンテンツを検出します。
*   **NSFW Checker**: opennsfw2を使用して画像を分析し、不適切なコンテンツを検出します。
*   **Sequential Image Loader**: 指定されたフォルダから画像をロードします。
*   **Sequential Media Loader**: 指定されたフォルダから画像または動画をロードします。
*   **Custom String Merge**: 複数の文字列を結合します。

## ChatGPT Text Generator
<img src="https://github.com/AI-TEC/images/blob/main/0003.jpg" alt="ChatGPT Text Generator">
このノードはGPT-4.1を利用して、回答がtextで出力されます。  

**APIキーは各自の責任で取り扱いに注意してご利用ください**  
**APIキーを入力した状態でワークフローを配布すると、他人がAPIキーを利用できる状態になります**  

*   **input text**: ChatGPT APIへ送るプロンプト
*   **role setting**: ChatGPT APIへ送るシステムプロンプト
*   **api_key**: OpenAIのAPIキー

## OpenAI Image Moderation
<img src="https://github.com/AI-TEC/images/blob/main/0004.jpg" alt="OpenAI Image Moderation">
このノードはOpenAIのomni-moderationを利用して、不適切コンテンツを検出しtextで出力します。  

block_flaggedを設定することで、不適切コンテンツが検出された場合にimage出力をブロックすることができます。  
検出されるスコアは目安として参考にしてください。  
**APIキーは各自の責任で取り扱いに注意してご利用ください**  
**APIキーを入力した状態でワークフローを配布すると、他人がAPIキーを利用できる状態になります**  

*   **api_key**: OpenAIのAPIキー
*   **output_format**: 結果の表示形式を選択  detail/simple/json
*   **language**: 言語の選択を行います  English/Japanese
*   **block_flagged**: 不適切コンテンツが検出された場合image出力をブロックする

*   ## NSFW Checker
<img src="https://github.com/AI-TEC/images/blob/main/0008.jpg" alt="NSFW Checker">
このノードはopennsfw2を利用して、不適切コンテンツを検出しtextで出力します。  

こちらのノードはAPIキーは不要で、ローカルで動作します。  
不適切コンテンツが検出された場合にimage出力をブロックすることができます。  
検出されるスコアは目安として参考にしてください。  

*   **block_nsfw**: NSFWをブロックするかどうか設定　pass through/block
*   **use_threshold**: score基準でブロックするかどうか  enabled/disabled
*   **threshold**: この値を超えた場合ブロックする  
**block_nsfwの設定が優先されます**　

## Sequential Image Loader
<img src="https://github.com/AI-TEC/images/blob/main/0007.jpg" alt="Sequential Image Loader">
このノードは指定されたフォルダ内の画像をロードすることができます

*   **folder_path**: 読み取りたい画像のあるフォルダのパス
*   **seed**: incrementを指定するとフォルダ内の画像をファイル名順に読み出すことができる
*   **include_subfolders**: サブフォルダの画像も読み出すかどうかを設定

## Sequential Media Loader
<img src="https://github.com/AI-TEC/images/blob/main/0006.jpg" alt="Sequential Media Loader">
このノードは指定されたフォルダ内のメディアをロードすることができます

*   **folder_path**: 読み取りたいメディアのあるフォルダのパス
*   **seed**: incrementを指定するとフォルダ内のメディアをファイル名順に読み出すことができる
*   **include_subfolders**: サブフォルダの画像も読み出すかどうかを設定
*   **frame_index**: 読み込みの開始フレームを設定
*   **load_all_frames**: すべてのフレームを読み込むかを設定
*   **max_frames**: 最大何フレームまで読み込むかを設定
*   **frame_step**: 何フレームごとに読み込むかを設定

## Custom String Merge
<img src="https://github.com/AI-TEC/images/blob/main/0005.jpg" alt="Custom String Merge">
このノードは3つのStringを１番から順にマージします

*   **use_string1**: string1を利用するかを設定
*   **use_string2**: string2を利用するかを設定
*   **use_string3**: string3を利用するかを設定
*   **string1**: 使用する文字列1
*   **string2**: 使用する文字列2
*   **string3**: 使用する文字列3

## 依存関係

- `openai`
- `opencv-python`
- `opennsfw2`
- `tensorflow`

## ライセンス

[LICENSE](LICENSE)ファイルを参照してください。

