# Divergent Nodes // Custom ComfyUI Suite

Welcome to the Divergent Nodes collection. This isn't just another node pack; it's a curated set of tools designed to bridge the gap between "it works" and "it works beautifully." We focus on meaningful integrations, better utilities, and making your terminal output look as good as your generations.

## Let's Get You Set Up

### 1. Installation
Navigate to your `ComfyUI/custom_nodes/` directory and bring the repository home:
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/thedivergentai/divergent_nodes.git divergent_nodes
```
*(Already have it? Just run `git pull` inside the folder to get the latest tools.)*

### 2. Dependencies
We try to keep it light, but we need a few things to run.
```bash
cd divergent_nodes
pip install -r requirements.txt
```

### 3. Configuration (Gemini Node)
To use the Gemini node, you'll need a Google AI Studio API key.
*   **The Right Way:** Create a `config.json` file in this directory:
    ```json
    {
      "GOOGLE_API_KEY": "YOUR_API_KEY_HERE"
    }
    ```
*   **The Other Way:** We also support `.env` files if that's your preferred workflow.

Don't worry, both files are git-ignored by default. Your secrets stay secret.

---

## The Divergent Experience

### Enhanced Logging
Reading logs shouldn't feel like decoding the Matrix. We've overhauled the console output to be clean, colorful, and actually useful.
*   **Clear Context:** Every log is prefixed (e.g., `[👽 Gemini]`) so you know exactly who's talking.
*   **Visual Status:**
    *   ✅ **Green**: All systems go.
    *   ⚠️ **Yellow**: Heads up, check this.
    *   ❌ **Red**: Something broke.
    *   🎉 **Magenta**: Magic just happened (like a successful generation).

### The Toolbox
Here is what's currently inside the suite:

*   **Divergent Gemini** (`Divergent AI 👽/Gemini`)
    Direct access to Google's Gemini models. Supports vision input and "thinking" budgets for complex logic. It’s an LLM that actually listens.

*   **MusiQ Image Scorer** (`Divergent AI 👽/MusiQ`)
    Stop guessing if your generation is "good." This node uses Google's MusiQ models to objectively score aesthetic and technical quality.

*   **KoboldCpp Connector** (`Divergent AI 👽/KoboldCpp`)
    Connect to your local LLM stack running on KoboldCpp. simple, fast, local.

*   **LoRA Strength XY Plot** (`Divergent AI 👽/XY Plots`)
    Visual data is better data. Generate grids comparing different LoRAs against varying strengths to find that sweet spot instantly.

*   **CLIP Token Counter** (`Divergent AI 👽/Text Utils`)
    A simple utility to keep your prompt lengths in check. Know exactly what the model sees.

*   **Save Image Enhanced** (`Divergent AI 👽/Image`)
    A better save node. Custom folders, smart naming, and optional caption saving. Because file management matters.

---

## Going Deeper
Need examples or want to see the code?
*   **Wiki:** [Check the docs](divergent_nodes.wiki/Examples.md) for workflows and deep dives.
*   **Contribute:** Found a bug? Have an idea? [Read our guidelines](divergent_nodes.wiki/Contributing.md).

*Build something different.*
