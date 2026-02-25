# ComfyUI-ToDevice

ComfyUI 用のシンプルなデバイス変換ノード集です。

GPUで実行されているimageノードを、CPUへ移動させます。

CPUからGPUの移動も対応していますが、ComfyUIの起動オプションからCPUを消去してください。



## ノード一覧

- **ToCPU**: 入力画像テンソルを CPU に移動
- **ToGPU**: 入力画像テンソルを GPU に移動



## インストール方法

1. このリポジトリを `ComfyUI/custom_nodes/` に`git clone`
2. ComfyUI を再起動



## 使用方法

1. CPUで処理されるノードの直前に「**ToCPU**」を設置し、imageコネクタを接続してください。
```
   例： imageコネクタ
   　　　→「ToCPUノード」
   　　　　　→imageコネクタ
   　　　　　　　→「CPUで実行されるノード」
```

bash
```
cd ComfyUI/custom_nodes
git clone https://github.com/Noma-Machiko/ComfyUI-ToDevice.git
```
