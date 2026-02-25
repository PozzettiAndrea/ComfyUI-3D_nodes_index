# ComfyUI_mittimiLoadPreset  
　  
> [!WARNING]
> I have solved some problems and revamped the functionality, so we have created a new custom node page.
> 
> **New node page is here. ->** [https://github.com/mittimi/ComfyUI_mittimiLoadPreset2](https://github.com/mittimi/ComfyUI_mittimiLoadPreset2)
> 
> いくつかの問題を解決し、機能を見直したので、新しいカスタムノードページを上記URLに作りました。  
> 
> This node will not be updated, so please use the above node.  
> こちらのノードは更新しませんので、上記のノードを使用してください。  
　  

＃＃＃ 日本語の説明は後半にあります ＃＃＃

The system selects and loads preset.

When using various types of models, isn't it troublesome to reset negative prompts and samplers every time you change models? With this node, you can instantly recall predefined prompts and parameters. Let’s take a look at how to use it.

## Usage
### 1) Create a Preset
First, create preset data in advance. There are samples in the presets folder within the custom node, so please refer to those.

Presets are saved in TOML format, and the file contains the following 11 items to set:

- PositivePromptA: Enter the positive prompt.
- PositivePromptC: Also a positive prompt.
- NegativePromptA: Enter the negative prompt.
- NegativePromptC: Also a negative prompt.
- CheckpointName: Enter the model name, including the file extension.
- ClipSet: Value of Clip Skip.
- VAE: Enter the VAE name, including the file extension.
- Steps: Number of steps.
- CFG: Enter the CFG value up to the first decimal place.
- SamplerName: Name of the sampler.
- Scheduler: Name of the scheduler.

If there are items you don't need to use, fill them in with appropriate values. You can leave prompts blank, like PositivePromptA = "".

Save the created TOML file in the presets folder.


### 2) Connect the Nodes
Before diving into detailed node descriptions in section 3), let's take a look at how the nodes are connected in practice. This will help you understand the later explanations better.
![Screenshot of sample02.](/assets/images/003.jpg)

This is the workflow of the sample sample02.json in the samples folder. The custom node LoadPresetForSettings selects a preset and passes the parameters to the SettingParameters node. The received parameters are displayed in each widget and are transmitted to the connected output ports.

For example, if you cannot find a node to connect the model name, right-click on the LoadCheckpoint node, and select Convert Widget to Input -> Convert_ckpt_name to input as shown in the red frame in the image below to display the input port.
![Screenshot of Convert Widget to Input.](/assets/images/004.jpg)

You don't have to connect all the output ports—just connect the ones you need.


### 3) Node Descriptions
As shown in the image below, there are two types of nodes with similar functions. The basic operation of both is the same.
![Screenshot of two main nodes.](/assets/images/img005.jpg)

The SettingParameters node works as described in section 2), while the LoadAndSettingParameters node is an integrated version that also includes preset selection. Here’s a brief explanation of why there are two types of nodes.

Both the SettingParameters node and the LoadAndSettingParameters node share a common feature: if you change the value displayed in the widget, that value will be reflected during queue execution. For example, if the preset has Clip Skip set to -2, but you want to run it with -1, simply change the value of ClipNum displayed in the SettingParameters node to -1. The preset only rewrites the widget display, and the output data is the value displayed on the widget.

However, it's important to note that with the SettingParameters node, the preset in the LoadPresetForSettings node will be loaded during ComfyUI’s queue execution. Therefore, any changes you made will be overwritten by the preset during execution. To prevent this, either remove connection from the LoadPresetForSettings node or mute it using the bypass function. However, this requires an extra step and is easy to forget.

On the other hand, the LoadAndSettingParameters node rewrites the widget display only when a preset is selected, so the parameters will not revert to their original state unless touched, allowing for fine tuning. You might think this is the only node you need, but it’s not that simple. However, this node automatically selects the preset when it’s created, so if you drag and drop an image to recreate a node from metadata, the widget values will change to those of the preset.

Therefore, I recommend choosing the node based on your work. Please refer to the workflow samples in the samples folder for more details.


### 4) Other
I’m not a professional, so if there are any bugs, please kindly share how to fix them.


Autor by mittimi (https://mittimi.blogspot.com)



# 日本語版　ComfyUI_mittimiLoadPreset の説明
様々な種類のモデルを使うようになると、モデルを変更する毎にいちいちネガティブプロンプトやサンプラーを設定し直すのは大変ではありませんか？
このノードを使えば、定型プロンプトや各パラメータを瞬時に呼び出すことができます。
では使い方を見てみましょう。

## 使い方
### 1) プリセットを作る
まず事前にプリセットデータを作ります。カスタムノード内の presets フォルダ内にサンプルがあるのであわせて参考にしてください。

プリセットはtomlで保存しますが、ファイルの中身は以下のように11の項目を設定するようになっています。

- PositivePromptA：ポジティブプロンプトを記入してください
- PositivePromptC：こちらもポジティブプロンプト
- NegativePromptA：ネガティブプロンプトを記入
- NegativePromptC：こちらもネガティブプロンプト
- CheckpointName：モデル名を拡張子も含めて記入
- ClipSet：Clip Skipの値
- VAE：VAE名を拡張子含めて記入
- Steps：ステップ数
- CFG：CFGの値を小数点第一位まで記入してください
- SamplerName：サンプラー名
- Scheduler：スケジューラ名

使わない項目がある場合も適当な値を入れておいてください。プロンプトは PositivePromptA = "" のように空白にしておけば良いです。

できたtomlファイルは presets フォルダ内に保存してください。


### 2) ノードをつなぐ
ノードの詳細な説明は 3)で行うとして、まずは実際につながっているノードを見てみましょう。そのほうが後の説明も理解しやすいと思います。
![Screenshot of sample02.](/assets/images/003.jpg)

これはsamplesフォルダにあるサンプル sample02.json のワークフローです。
カスタムノード LoadPresetForSettings でプリセットを選択し、SettingParapeters ノードにパラメータを受け渡します。
受け取ったパラメータは各ウィジットに表示され、出力ポートからつないだ先へ伝達していきます。

例えばモデル名など繋ぐ先が見当たらないものは、LoadCheckpointノードを右クリックし、以下画像の赤枠のように Convert Widget to Input -> Convert_ckpt_name to input を選択すると入力ポートが表示されます。
![Screenshot of Convert Widget to Input.](/assets/images/004.jpg)

出力ポートはすべてつなぐ必要はなく、繋ぎたいものだけを繋げば良いです。


### 3) ノードの説明
以下の画像のように、このカスタムノードには2種類のノードが存在します。どちらも基本動作は同じです。
![Screenshot of two main nodes.](/assets/images/img005.jpg)

SettingParametersノードは 2)で説明した通りですが、LoadAndSettingParametersノードはプリセット選択が合体した一体型です。
なぜわざわざ2種類のノードを作ったのか簡単に説明します。

SettingParametersノードとLoadAndSettingParametersノード、どちらのノードにも共通していることですが、パラメータが表示されているウィジットの値を変更すると、Queue実行時にはその値が反映されます。
例を挙げると、「プリセットはClip Skipが-2だけど、-1で実行したいな」と思ったら、SettingParametersノード内に表示されているClipNumの値を-1にするだけで済みます。要するにプリセットはウィジットの表示を書き換えるだけで、実行時は表示されたパラメータを出力する仕組みなのです。

ただしここからが重要なのですが、SettingParametersノードの場合はComfyUIのQueue実行時に、LoadPresetForSettingノードのプリセットが読み込まれます。なので書き換えた値は実行時にプリセットの内容に書き換えられてしまいます。
これを防ぐには、LoadPresetForSettingノードを外すかBypass機能でミュートすれば良いですが、ひと手間かかってしまうのと忘れやすいというのが欠点です。

では一体型のLoadAndSettingParametersノードはどうかと言うと、こちらはプリセット選択のタイミングでウィジットの表示が書き換わるため、そこに触れさえしなければ各パラメータは元に戻ったりしません。微調整し放題です。
ではこっちだけで良いじゃないか、というわけにはいかず。こちらはノードが作られたタイミングでプリセット選択が自動で行われる仕様になっており、例えば画像をドラッグ＆ドロップしてメタデータからノードを再現するような場合はウィジットの値はプリセットのものに変わってしまいます。

ですので、運用方法によって変えて頂ければと思います。
samplesフォルダ内にワークフローのサンプルがあるのでそちらも参考にしてください。


## 4) その他
私はプロではありません。バグがあった場合、直し方もコッソリ教えてください。

Autor by mittimi (https://mittimi.blogspot.com)
