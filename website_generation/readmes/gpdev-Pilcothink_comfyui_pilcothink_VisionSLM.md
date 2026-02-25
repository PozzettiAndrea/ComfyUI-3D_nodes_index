# comfyUI_pilcothink_VisionSLM

Custom ComfyUI nodes to run SLM Vision models (DeepSeek-vl 1.3b chat, Qwen2-vl-2b-Instruct, Qwen2.5-vl 3b, qwen3-vl(2b,4b)[Instruct, Thinking] , Gemma-3-4b-it) with optional RAG support.
+
Support SLM Model (Qwen3-0.6b)


<img width="2596" height="1712" alt="image" src="https://github.com/user-attachments/assets/74130f20-7717-4a9a-a8c8-91776bcbed59" />
<img width="3323" height="1048" alt="image" src="https://github.com/user-attachments/assets/34375235-325c-449a-8396-eec99ed19673" />



- Models are downloaded into `Models/SLM_Vision/` when selected in the node.


# LICENSE
-utils/backends/DeepSeek-vl 
https://github.com/deepseek-ai/DeepSeek-VL, MIT LICENSE

-utils/backends/qwen_vl_utils
https://github.com/QwenLM/Qwen3-VL, Apache-2.0 license


# Tips

(1) If you choose the CPU option on the device, it will only work with float16. Other dtypes will result in errors.

(2) You can enable RAG functionality by placing your data in the rag_doc folder in .txt format.

(3) Since gemma-3-4b-it cannot be accessed on Hugging Face without logging in, you will need to configure it separately, or alternatively, download it directly from the repository and place it in the Models folder.

(4) If you want to unload the model from memory, simply switch off the 'Use Cache' option and execute the model again.

#Thank you
Please share any suggestions for improvements in the Issues section.
