# ComfyUI_RH_LLM_API
**Very easy to use. LLM DeepSeek, OpenAI API compatible plugin**
## 
Because the vast majority of LLM APIs are compatible with OpenAI's API interface specifications, this plugin was created
Through triples, any LLM model compatible with the OpenAI interface can be accessed and called, such as deepseek, Qianwen, Doubao, GLM, MinMax, etc. API
- **baseurl**
- **apikey**
- **model**

## Update: Video reverse-prompt (video captioning)
- **Optional input `video`**: supports OpenAI-compatible `chat.completions` payload with `{"type":"video_url"}`.
- **No resize / no compression**: image keeps original resolution; video is read as-is and base64 encoded.

**Online Demo**
https://www.runninghub.ai/post/1890402871119368194
![image](https://github.com/user-attachments/assets/31b35db4-4d61-4767-a41c-6f1445fbea5e)
