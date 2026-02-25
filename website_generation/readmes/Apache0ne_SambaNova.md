# ComfyUI-SambaNova
The SambaNova API Node gives ComfyUI users the second fastest token output LLM's have to offer with context \
![image](https://github.com/user-attachments/assets/d3e7edbc-dec7-4c0e-9578-16a29a671126)\
The Nova APIv1 comes with a chat or completion type of chat. \
Chat is like all other chat bots where completion will take the users prompt and system prompt if used to make a mock chat between the LLM and user. \
This has not been used much myself so I dont know the perks of using completion chat. \
Nova also has a streaming mode feauture this is not usable as nodes in comfyUI run linear and can not update the show text node at the same time. \
I will try to find a way to make this feauture work in comfyUI (WIP)\
Gpt will help if you dont want to read the API docs. \
https://community.sambanova.ai/c/welcome/4 \
This is the speed of tokens chat for the top models. \
Getting Cerebras API (WIP) \
![image](https://github.com/user-attachments/assets/9af8233b-b385-4676-92d5-9674afb63ae6)
## CONS & PROS
Cons\
Not first place for speed of tokens\
405B model has a low 10 RPM(Request Per Minute) cap\
405B model has a low 8K token context cap, this is really low for this model\
Pros\
Llama 3.1 70B model has a 64k token limit for context, the highest ive seen for these API's but the model will lose most of its greatness around the 16k mark and heavy drop off at 32K\
Llama 3.1 8B model has a 16K token limit making it great for simple but long tasks again 8B model will lose most of its greatness around 8k so simple tasks only\
Llama 3.1 405B API at super fast speed for free, do I need to say more
## Dependencies
'requests' 
'pydantic' 
'fastapi' 
'sentry_sdk' 
'tenacity' 
'openai' 
'tiktoken'
'nthropic' 
## Installation
API KEY HERE: 
https://cloud.sambanova.ai/apis \
Place KEY inside Config file\
ComfyUI-Manager (Rec)\
Can Download from Comfy Manager\
IF using Windows Port version\
ComfyUI Folder\
```cmd pip install requests pydantic fastapi sentry_sdk tenacity openai tiktoken anthropic```\
Inside Custom_nodes Folder\
```git clone https://github.com/Apache0ne/ComfyUI-SambaNova.git```\
IF using Matrix \
Inside venv\Scripts\
```activate```\
```pip install requests pydantic fastapi sentry_sdk tenacity openai tiktoken anthropic```\
Inside Custom_nodes Folder\
```git clone https://github.com/Apache0ne/ComfyUI-SambaNova.git```
## Extra Info
TOS\
https://community.sambanova.ai/t/sambanova-cloud-terms-of-service/244 \
Dev TOS\
https://community.sambanova.ai/t/sambanova-developer-community-terms-of-use/133
