[English](#English) | [日本語](#日本語)

---
# English

## Nodes

- Audio Pitch (Mono)

## Install

Move to ComfyUI\custom_nodes

```
git clone https://github.com/Takenoko3333/comfyui-audio-pitch.git
```

Restart ComfyUI.

## How to Use

- Search for "Audio Pitch" in the Node Library and place the Audio Pitch (Mono) node.
- Adjusting the pitch is basically achieved by changing only the n_steps value. Increasing the value raises the pitch, while decreasing it lowers the pitch.
- The adjustment range for n_steps is -24 to +24.

## Test Workflow

- Download the workflow and drag and drop it into ComfyUI.<br>
[https://github.com/Takenoko3333/comfyui-audio-pitch/blob/main/example_workflows/audio-pitch-sample.json](https://github.com/Takenoko3333/comfyui-audio-pitch/blob/main/example_workflows/audio-pitch-sample.json)
- Alternatively, searching for "pitch" in the ComfyUI templates will display "audio-pitch-sample". Clicking this will show the workflow.
- Test audio files are located in "ComfyUI\custom_nodes\comfyui-audio-pitch\example_workflows".
  Or download them from the following link.
  [https://github.com/Takenoko3333/comfyui-audio-pitch/tree/main/example_workflows](https://github.com/Takenoko3333/comfyui-audio-pitch/tree/main/example_workflows)

## Purpose

- Avoids memory leaks in torchaudio's PitchShift when using MMAudio output
- Stable pitch shifting processing in ComfyUI environments
- Mono processing optimization focused on integration with MMAudio

## Origin

- This project is based on audio-general-comfyui
- Originally licensed under the MIT License.
- Forked and modified to improve stability, reduce RAM usage, and ensure PreviewAudio compatibility.

## Main Changes

- Removed all torchaudio dependencies
- Implemented pure-CPU phase vocoder time-stretch
- Fixed RAM overflow issue when use MMAudio output on repeated execution
- Output shape fixed to (1, 1, T) (Mono)
- Added bypass at n_steps=0
- Default FFT size = 1024 (smoother output for short clips)

## License

- MIT
  
---
# 日本語

## ノード

- Audio Pitch (Mono)

## インストール

ComfyUI\custom_nodes に移動

```
git clone https://github.com/Takenoko3333/comfyui-audio-pitch.git
```

ComfyUI を再起動してください。

## 使用方法

- ノードライブラリで「Audio Pitch」を検索し、Audio Pitch (Mono) ノードを配置します。
- ピッチ調整は基本的に n_steps 値の変更のみで実現されます。値を大きくすると高音になり、小さくすると低音になります。
- n_steps の調整範囲は -24 から +24 です。

## 動作確認用ワークフロー

- ワークフローをダウンロードしComfyUIにドラッグアンドドロップしてください。
[https://github.com/Takenoko3333/comfyui-audio-pitch/blob/main/example_workflows/audio-pitch-sample.json](https://github.com/Takenoko3333/comfyui-audio-pitch/blob/main/example_workflows/audio-pitch-sample.json)
- もしくは、ComfyUIのテンプレートより"pitch"等で検索すると"audio-pitch-sample"が表示されます。これをクリックするとワークフローが表示されます。
- テスト用音源は"ComfyUI\custom_nodes\comfyui-audio-pitch\example_workflows"内にあります。<br>
  もしくは、以下よりダウンロードしてください。<br>
[https://github.com/Takenoko3333/comfyui-audio-pitch/tree/main/example_workflows](https://github.com/Takenoko3333/comfyui-audio-pitch/tree/main/example_workflows)

## 目的

- MMAudio 出力を使用する際の torchaudio PitchShift におけるメモリリークの回避
- ComfyUI 環境における安定したピッチシフト処理
- MMAudio との統合に焦点を当てたモノラル処理の最適化

## 由来

- 本プロジェクトは audio-general-comfyui を基にしています
- フォークし、安定性の向上、RAM 使用量の削減、PreviewAudio との互換性確保のために修正を加えました

## 主な変更点

- torchaudio 依存関係を全て削除
- 純粋な CPU ベースの位相ボコーダーによるタイムストレッチを実装
- MMAudio 出力を繰り返し実行時の RAM オーバーフロー問題を修正
- 出力形状を (1, 1, T) (モノラル) に固定
- n_steps=0 時のバイパス機能を追加
- デフォルト FFT サイズ = 1024 (短いクリップで滑らかな出力)

## ライセンス

- MIT
