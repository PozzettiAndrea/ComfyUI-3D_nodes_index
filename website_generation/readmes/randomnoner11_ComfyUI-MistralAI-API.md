# ComfyUI Mistral API Node

This node provides a straightforward way to interact with the [Mistral AI API](https://docs.mistral.ai/api/) for single-turn chat completion requests. It's designed for quickly sending prompts to Mistral's language models and receiving a single response.

## Key Features:

* **Direct API Interaction:** Sends a single request to the Mistral AI Chat Completion endpoint. No chat history is maintained by the node itself.
* **Context via Templates:**  You can supply context to the language model by loading pre-defined templates. This allows for implementing techniques like few-shot prompting.
* **Standalone Design:**  This node focuses specifically on basic Mistral API interaction, avoiding the inclusion of features you might not need.

## Screenshots:
*  ![](/screenshots/example-use-1.png)
   The node doesn't introduce any hidden prompt additions. You have complete control over the instruction and the request sent to the API.

* ![](/screenshots/example-use-2.png)
   For certain models, you can input images directly. The image will be downscaled to have a longest side of 1024 pixels before being processed.

* ![](/screenshots/example-use-3.png)
* ![](/screenshots/example-use-4.png)  
   A companion node lets you easily prepend content from files within a `/prompts` folder to your main prompt. This makes it convenient to save and load your own instruction sets for consistent prompting strategies. Keep in mind that no formatting validation is performed on the template content.

* ![](/screenshots/example-use-5.png)
   The node provides the raw text response from the API, allowing you to parse and utilize the output as needed in your workflow. For instance, you can request both plain text and structured information like tag prompts in a single request.

## Important Notes:

* **Model Selection:** The list of available models is fetched on launch. If the API check slows down your startup, edit the configuration variable in `nodes.py` to use the hardcoded list.
* **Vision Support:** Models that support image inputs are tagged with 🖼️ in the dropdown.
* **Seed Randomization:** Unless you explicitly provide a seed value in the node's settings, the seed for the language model's response will be randomized server-side by Mistral AI.
* **API Key:** You will need to save your Mistral AI API key in a file named `API-key.txt` within the node's directory for it to function correctly.

---

For visual clarity in the examples, the following nodes are used to display the output:

* **Show Text:** From [ComfyUI-Custom-Scripts](https://github.com/pythongosssss/ComfyUI-Custom-Scripts).
* **String Selector:** From the [ComfyUI-Impact-Pack](https://github.com/ltdrdata/ComfyUI-Impact-Pack).


### Tips for Usage:

* When working with smaller language models, experimenting with higher values for the penalty parameters (presence penalty, frequency penalty) might yield improved results.

---