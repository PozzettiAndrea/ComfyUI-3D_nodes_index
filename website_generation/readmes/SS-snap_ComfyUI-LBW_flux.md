### 安装方法
   ```bash
   https://github.com/SS-snap/ComfyUI-LBW_flux.git
   ```
克隆仓库到你的自定义节点目录中
Clone the repository into your custom node directory

### 简述
#### 通过这个节点，你可以更方便的测试关于flux_lora不同块对最终结果的影响。这是一个具有实验性的测试，是根据inspire pack中分层预设得到的结果。但在我的测试下不同块确实会对结果产生不同的影响，虽然测试结果不具备稳定性。并且flux基于DIT框架，所以对层的定义也比较模糊，这样大家就很难得到一个非常确切的结果，也很难根据不同固定概念的lora总结出一些规律性经验，所以测试可能是徒劳的，但单个lora的概念或许还是有些规律可以找到。
#### Through this node, you can more easily test the impact of different blocks in flux_lora on the final result. This is an experimental test,  which are derived from thelayered presets in the inspire pack. However, in my tests, different blocks do indeed have varying effects on the results, although the test results lack stability.Since Flux is based on the DIT framework, the definition of layers is also quite vague, making it difficult to obtain a precise result. It's also hard to summarize any regular patterns from different fixed-concept LoRAs, so testing might be in vain. However, there may still be some patterns to discover within a single LoRA concept.

#### 这是Flux_LoRA的61个块，但最终前三个块被排除后只剩58个块
#### This is 61- 3 layers


（CLIP  T5 IN）	D00	D01	D02	D03	D04	D05	D06	D07	D08	D09	D10	D11	D12	D13	D14	D15	D16	D17	D18	S00	S01	S02	S03	S04	S05	S06	S07	S08	S09	S10	S11	S12	S13	S14	S15	S16	S17	S18	S19	S20	S21	S22	S23	S24	S25	S26	S27	S28	S29	S30	S31	S32	S33	S34	S35	S36	S37	OUT

### 使用方法
   ```bash
   https://github.com/ltdrdata/ComfyUI-Inspire-Pack
   ```
#### 你需要配合此仓库的 make / lora block weight节点共同使用

You can use the following syntax to zero out the weights of different layers:

For example, enter 6 in layer_or_multi_layer to set the weights of layer 6 to zero.
Enter 15-30 in layer_or_multi_layer to set the weights of layers 15 to 30 to zero. Make sure to use English input and the data type should be a string.

你可以使用以下语法进行不同层权重归零
例如：
在layer_or_multi_layer中填写6，代表第6层权重为0
在layer_or_multi_layer中填写15-30，代表第15-30层权重为0
要用英文输入法输入且数据类型为字符串类型
