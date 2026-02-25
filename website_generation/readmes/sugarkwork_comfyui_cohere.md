# comfyui_cohere

ComfyUI から cohere （Command R+）を使用するためのノードです。


ComfyUI の起動 bat ファイルを編集して、以下のように Cohere から取得した API キーを記述する必要があります。

    @echo off
    set COHERE_API_KEY=COHERE_API_KEY
    .\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build
    pause

# SimpleCohereNode

![image](https://github.com/sugarkwork/comfyui_cohere/assets/98699377/aaf17fc2-0109-48ca-8884-9a75638482e9)
