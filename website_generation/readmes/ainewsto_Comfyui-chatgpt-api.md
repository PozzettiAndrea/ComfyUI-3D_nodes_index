


> **Warning**
> 
> 插件只在windows11上测试，mac电脑后续我也会测试，如果其他系统有任何问题，可以提交issues
> 速度不快，因为官网速度也不快，所以需要点耐心。

# 插件 Node：

20250429：

`Chatgpt节点`: Comfyui_gpt_image_1_edit新增chats输出口，输出多轮对话。
新增clear_chats,当为Ture的时候，只能image输入什么图片修改什么图片，不支持显示上下文对话。
当为Flase的时候，支持对上一次生成的图片进行二次修改。支持显示上下文对话。并且支持多图模式下新增图片参考。

<details>
<summary>查看更新/Update </summary>  
 
![2eaf76b077612170647f6861e43e2af](https://github.com/user-attachments/assets/1c4c484f-c3c6-48c6-96c5-58c4ef4e59d5)

![6a43cb051fece84815ac6036bee3a4c](https://github.com/user-attachments/assets/f0fbf71e-8cfb-448e-87cd-1e147bb2f552)

</details> 


20250425：

`Chatgpt节点`: 
新增Comfyui_gpt_image_1和Comfyui_gpt_image_1_edit官方gpt_image_1模型api接口节点。

![image](https://github.com/user-attachments/assets/9d08d5fc-dde9-4523-955c-31652a74f1a5)

模型名都是gpt_image_1，区别只是分组不同：

一共四个分组：default默认分组为官方逆向，价格便宜，缺点就是不稳定，速度慢。按次收费。不支持额外参数选择。这个分组的apikey只能用于ComfyuiChatGPTApi节点。

其他三个组都是官方api组，最优惠的目前是ssvip组。分组需要再令牌里面去修改选择。这3个官方分组优点就是速度快，稳定性高。支持官方参数调整。
缺点就是贵，但是也比官方便宜。大家可以按照自己的情况选择。这3个分组的令牌的apikey只能用在下面2个新节点上面！！！

1. Comfyui_gpt_image_1 节点：文生图，有耕读参数调整，支持调整生图限制为low。

2. Comfyui_gpt_image_1_edit 节点：图生图，支持mask遮罩，支持多图参考。

<details>
<summary>查看更新/Update </summary>  
 
![3bc790641c44e373aca97ea4a1de47e](https://github.com/user-attachments/assets/1a7a0615-46e5-46b3-af04-32246a23d6f4)

![5efe58fcf7055d675962f40c1ad1cbb](https://github.com/user-attachments/assets/8a90eab5-4242-43bb-ae01-74493b90b6ce)

</details> 



20250424：

`Chatgpt节点`: 

ComfyuiChatGPTApi节点新增官方gpt-image-1，按次计费 0.06，
ComfyuiChatGPTApi节点新增chats输出口，输出多轮对话。
新增clear_chats,当为Ture的时候，只能image输入什么图片修改什么图片，不支持显示上下文对话。
当为Flase的时候，支持对上一次生成的图片进行二次修改。支持显示上下文对话。

<details>
<summary>查看更新/Update </summary>  

![cad243f2bf4a3aa11163f1a007db469](https://github.com/user-attachments/assets/ef0f6a34-3de7-42a2-8543-c1930575e1bb)

![bd6493050affdf156143c8dc5286988](https://github.com/user-attachments/assets/0906caf3-35ec-4061-bfc9-5f611a19abf2)

![e5b3d375b700dcbf921b12a8aa527c4](https://github.com/user-attachments/assets/75537100-e5d2-403c-b2e0-1f662680092f)


</details> 


`Chatgpt节点`: 

新增openai的comfyui-chatgpt-api节点，。
目前单图和多图输入，文本输入，生成图片，图片编辑.使用的是 https://ai.comfly.chat 的 api key
固定一次生成消耗0.06元（显示是逆向api，稳定性还不高，想尝鲜的可以注册网站用免费送的0.2美金玩玩）
速度不快，因为官网速度也不快，所以需要点耐心。 files输入接口还没有完善，先忽略。


 
![fdedd73cffa278d2a8cf81478b58e90](https://github.com/user-attachments/assets/36e78cdd-33b2-41ed-a15c-ad9c1886bede)


![0a2394c0b41efe190a5d0880f4c584b](https://github.com/user-attachments/assets/267fbe73-7113-4120-a829-a7aa2247bd4d)



# 🥵 Comfly的QQ群 / my wechat

![86601b471a343671e7240c74aa8e1fd](https://github.com/ainewsto/Comfyui_Comfly/assets/113163264/3e1c2d15-ba5b-4aa5-a76b-08f87e7c8e2c)

![86601b471a343671e7240c74aa8e1fd](https://github.com/ainewsto/Comfyui_Comfly/assets/113163264/fdc2f849-5937-4cce-a36d-8444ecca3030)


# :dizzy:插件有参考项目 Comfy Resources：

感谢原项目：
https://github.com/comfyanonymous/ComfyUI


## 🚀 About me
* website: https://comfly.chat
* Welcome valuable suggestions! 📧 **Email**: [3508432500@qq.com](mailto:1544007699@qq.com)
