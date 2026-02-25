## 🧠 LLM Hub

Utilize the power of an LLM into ComfyUI to transform your text-to-image and text-to-video ideas into highly detailed prompts for generation while giving you full control. 

## 🤖 Usage

<img src="img/usage.png" alt="LLM Hub for ComfyUI">

## 📝 Requirements

- Create a directory named **`LLMs`** inside **`ComfyUI/models/text_encoders/`**
- Create a another new directory for each LLM with the model name inside **`LLMs`**.
- Place your LLM models in their respective directory.
- Every .safetensors model needs the .json files and the model should be named **`model.safetensors`**

How your directory structure should look like:
```
ComfyUI/
└── models/
    └── text_encoders/
        └── LLMs/
            └── GGUF_model/
                └── model.gguf
            └── safetensors_model/
                └── model.safetensors
                └── config.json
                └── tokenizer.json
                └── tokenizer_config.json
                └── generation_config.json (Optional)
                └── special_tokens_map.json (Optional)
```

GGUF models don't need to be named "model.gguf".

## 🛠️ Installation

- Run the following commands:

For activating venv:
```
cd path/to/your/ComfyUI
```
Linux:
```
source venv/bin/activate
```

Windows:
```
.venv\Scripts\activate
```

Go to your custom nodes folder:
```
cd custom_nodes
```

Afterwards clone the repo:
```
git clone https://github.com/claptrap0/ComfyUI_LLM_Hub
```

Go inside the node folder:
```
cd ComfyUI_LLM_Hub
```

If you are using a venv:
```
pip install -r --verbose requirements.txt
```
- You can delete **`"--verbose"`** if you don't want to see the process of the compiling.

For the portable version of ComfyUI:
```
C:/path/to/your/ComfyUI_portable/python_embedded/Scripts/pip.exe install -r requirements.txt
```

## ⚙️ LLM Settings 

It offers a range of configurable parameters allowing for precise control over the text generation process and model behavior.

The values on this node are also the defaults that `LLM Hub` uses when `LLM Settings` isn't connected.

Breif overview of the parameters:

- **`temperature:`** Controls the randomness of the output. Lower values (**e.g., 0.2-0.5**): Make the output more focused, predictable, and deterministic. 
  Ideal for tasks requiring factual, precise, or consistent responses. Higher values (**e.g., 0.7-1.0**): Increase creativity and randomness, allowing the model to take more risks. Can lead to more imaginative but potentially less coherent results.
  `Default: 0.8`
- **`top_p:`** Filters the set of possible next tokens by cumulative probability. The model only considers tokens whose cumulative probability sum up to `top_p`.Lower values (**e.g., 0.5**): Narrows the selection to only the most probable tokens, improving coherence and reducing the chance of irrelevant words.
  Higher values (**e.g., 0.9**): Allows for a broader range of tokens, increasing randomness. `Default: 0.8`
- **`top_k:`** Limits the sampling pool to the k most probable next tokens. Lower values (**e.g., 5-20**): Focuses generation on the top choices, making output more predictable.
  Higher values (**e.g., 50-100**): Expands the options, outputing more creative text. `Default: 10`
- **`repetition_penalty:`** Discourages the model from repeating words or phrases that have already appeared in the generated text. Values greater than 1 (**e.g., 1.1-1.5**): Penalize repeated tokens, making them less likely to be chosen again. Essential for preventing repetitive loops or boilerplate text.
  A value of 1: No penalty applied. `Default: 1.3`

## 📚 Resources

- <a href="https://rumn.medium.com/setting-top-k-top-p-and-temperature-in-llms-3da3a8f74832" target="_SEJ" rel="noreferrer">Parameter settings</a>
- <a href="https://github.com/0xeb/TheBigPromptLibrary" target="_SEJ" rel="noreferrer">System prompts, instructions, etc.</a>

## 📄 License
Released under the MIT License. Feel free to use and modify it for your projects, commercial or personal.
