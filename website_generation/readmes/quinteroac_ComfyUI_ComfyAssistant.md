# ComfyUI Assistant

An AI assistant for ComfyUI: control and explore your workflows with natural language from a chat in the bottom panel. The assistant lives in **Console** — open Console, then the **ComfyUI Assistant** tab to start chatting.

- Chat with an AI that understands ComfyUI and can add nodes, connect them, run workflows, and search your environment.
- Works with any OpenAI-compatible API (or Claude Code, Codex, Gemini CLI). Configure your provider in the Assistant tab.
- You can customize the assistant with user skills, personality, and goals; the extension also ships with base skills for workflows, tools, and research.
- **Personas** let you switch between named personalities tied to a provider: each persona is a `SOUL.md` in `user_context/personas/<slug>/` (name, description, provider in frontmatter). Use `/persona` to list, `/persona <name>` to switch, `/persona create` to add one, and `/persona del <name>` to remove.

📚 **Documentation:** [User docs](doc/README.md) (installation, configuration, commands, skills, tools) · [Developer docs](doc/dev_docs/README.md) (architecture, backend, frontend, standards).

## Quick Start

**[Quick Start Guide](QUICKSTART.md)** — Get running in a few minutes.

Open **Console** in the bottom panel, then the **ComfyUI Assistant** tab, and try:

- **Load a workflow** — Ask the assistant to load a workflow for any of the models supported by ComfyUI.

  ![Load workflow](doc/screenshots/load-workflow.png)

- **Create a workflow** — Ask the assistant to create a txt2img workflow with detailer and upscaler.

  ![Create workflow](doc/screenshots/create-workflow.png)

- **Describe and edit** — Chat about your workflow and ask for suggestions; you can ask the assistant to apply changes directly to the workflow.

  ![Describe workflow](doc/screenshots/describe-workflow.png)

- **Organize** — Ask the assistant to organize your workflow (layout and readability).

  ![Organize workflow](doc/screenshots/organize-workflow.png)

- **Prompt maker** — Brainstorm prompts with the assistant and ask it to run the workflow with that prompt.

  ![Prompt maker](doc/screenshots/prompt-maker.png)

## Installation

### Install from ComfyUI Manager (Recommended)

1. Open ComfyUI Manager in your ComfyUI interface.
2. Search for "ComfyUI AI Assistant".
3. Click **Install**.
4. Restart ComfyUI.

The Manager will automatically handle cloning the repository, installing Python dependencies, and building the frontend.

### Manual installation

1. Clone this repo into ComfyUI's `custom_nodes` folder.
2. Install Python dependencies: `pip install -r requirements.txt` (from the extension root).
3. Build the frontend: `cd ui && npm install && npm run build && cd ..`
4. Restart ComfyUI.

Full steps and options: [doc/installation.md](doc/installation.md). You can use an AI agent (Claude, Codex, Cursor, etc.) to run the install — see [Using an AI agent to install](doc/installation.md#using-an-ai-agent-to-install) in the install guide. For the agent's context: [.agents/skills/installation/SKILL.md](.agents/skills/installation/SKILL.md).

## Usage

Open the **ComfyUI Assistant** tab, set up your LLM provider (wizard on first use or [doc/configuration.md](doc/configuration.md)), and chat. The assistant can modify the workflow, run it, search nodes and models, and use the web and the ComfyUI Registry when needed.

- **Commands:** Slash commands like `/help`, `/clear`, `/new`, `/skill`, `/persona` — see [doc/commands.md](doc/commands.md).
- **What the assistant can do:** Graph actions, environment search, user skills, workflow execution, research — see [doc/base-tools.md](doc/base-tools.md).
- **Customization:** System and user context, skills, SOUL, goals — see [doc/](doc/README.md).
- **Personas:** Named personalities per provider (`user_context/personas/<slug>/SOUL.md` with YAML frontmatter). `/persona` lists them, `/persona <name>` switches, `/persona create` adds one, `/persona del <name>` removes. See [doc/configuration.md](doc/configuration.md).
- You can **switch provider or persona in the middle of a conversation**; the assistant keeps the same thread and context, so the new provider or persona continues from the existing chat.

## Recommended providers

- **Claude Opus 4.6** — Best for complex tasks (workflow design, multi-step reasoning). More expensive; use the Anthropic API or Open Router.
- **Gemini** — Good for most day-to-day tasks. Use Gemini CLI or the Open Router API.
- **Grok** — Great for prompt ideas and creative brainstorming. Use the x.ai API or Open Router.

Results can vary depending on which model you choose. **Frontier models** (e.g. latest Claude Opus, GPT-4 class, or top-tier Open Router models) generally give better workflow quality and fewer errors; smaller or older models may need more back-and-forth or manual tweaks.

See [doc/configuration.md](doc/configuration.md) for how to add and switch providers.

## Development

Frontend: `cd ui && npm run watch` (rebuilds on change; refresh the browser). Tests: `cd ui && npm test`.  
Architecture, backend, frontend, tools, and conventions: [doc/dev_docs/](doc/dev_docs/README.md).

## Resources

- [ComfyUI — JavaScript extensions](https://docs.comfy.org/custom-nodes/js/javascript_overview)
- [assistant-ui](https://www.assistant-ui.com/) · [Vercel AI SDK](https://sdk.vercel.ai/)

## Acknowledgements

ComfyUI Assistant builds on the following projects and libraries:

| Project | Purpose | Links |
|--------|---------|-------|
| **ComfyUI** | Host UI and workflow engine | [Docs](https://docs.comfy.org/) · [GitHub](https://github.com/comfyanonymous/ComfyUI) |
| **assistant-ui** | Chat UI and runtime | [Docs](https://www.assistant-ui.com/) · [GitHub](https://github.com/assistant-ui/assistant-ui) |
| **Vercel AI SDK** | LLM integration and streaming | [Docs](https://sdk.vercel.ai/) · [GitHub](https://github.com/vercel/ai) |
| **React** | UI framework | [Docs](https://react.dev/) |
| **Tailwind CSS** | Styling | [Docs](https://tailwindcss.com/) |
| **Vite** | Build tool | [Docs](https://vitejs.dev/) |
| **TypeScript** | Typing | [Docs](https://www.typescriptlang.org/) |
| **Zod** | Schema and validation | [Docs](https://zod.dev/) |
| **Radix UI** | Accessible components | [Docs](https://www.radix-ui.com/) |
| **Zustand** | State management | [Docs](https://zustand.docs.pmnd.rs/) |
| **OpenAI Python** | Backend LLM client (OpenAI-compatible APIs) | [GitHub](https://github.com/openai/openai-python) |
| **python-dotenv** | Environment config | [GitHub](https://github.com/theskumar/python-dotenv) |

## License

MIT
