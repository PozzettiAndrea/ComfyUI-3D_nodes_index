Jurdn's Groq Node

This is a very simple node. It utilizes the Groq API. (https://www.groq.com) 

Groq is currently a service which provides AI inference with a number of open source LLMs that are capable of doing prompt enhancement for both Flux or Stable Diffusion Prompts.

Both Gemma and llama are very effective, and I recommend using them.

Your API key, generated from groq.com (https://console.groq.com/keys) is stored in your groq_config.json.

The config file also contains a system prompt which works, but is the bare minimum. You may make changes to that system prompt and/or make changes to the prompt by editing the override field on the node itself within ComfyUI. Keep in mind that the LLM will require instructions to avoid conversation and only give the desired enhanced prompt. See the default system prompt included in the config file for an example.

Just type your prompt in the top textbox on the node and the text string output will have the API response. Route this response directly into a ClipTextEncoder or into a "Show" node to see what you're working with.

![image](https://github.com/user-attachments/assets/7a82465b-360c-4bbe-b924-cc71b36f7846)
