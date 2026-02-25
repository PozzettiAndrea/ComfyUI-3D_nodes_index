<h1 align="center">
    MultiModel for ComfyUI
    <br>
    <sub><sup><i>Flexible multi-model workflows, prompt engineering, and style management for ComfyUI</i></sup></sub>
    <br>
</h1>
<p align="center">
    <a href="#️-the-nodes">The Nodes</a> &nbsp; | &nbsp; <a href="#-styles">Styles</a>  &nbsp; | &nbsp; <a href="#-installation">Installation</a> &nbsp; | &nbsp; <a href="#-example-usage">Example Usage</a>
</p>
<hr>

A collection of nodes and utilities to make working with multiple models, custom parameters, and prompt styles in ComfyUI easier, faster, and more flexible.  
You are welcome to use and adapt them for your own workflows!

---

# ✴️ The Nodes

## ModelParamsPipeNode
> Create a "pipe" containing the selected model, CLIP, VAE, and all generation parameters (steps, CFG, sampler, scheduler, tags, etc).  
> Makes it easy to pass model settings between nodes.

## ParamsPipeUnpack
> Unpack all parameters and objects from a pipe: model, CLIP, VAE, steps, CFG, sampler, scheduler, tags.

## KSamplerPipeNode
> A sampler node that takes a pipe, conditioning, seed, denoise, and either latent or image_override.  
> Works with any model passed via the pipe.

## PromptBuilderNode
> Build final positive/negative texts and CLIP conditioning, taking into account styles (from JSON), base texts, tags, and img2txt.  
> Supports custom styles for advanced prompt engineering.

## ListSelectorNode
> Select an item from a list by index.  
> Useful for UI and dynamic workflows.

## DenoiseSelector
> Simple node for selecting the denoise value.

## ActiveModel
> Dummy node for JavaScript-side integration (client logic).

## MySwitchIndex (Multi Model Switch)
> Вузол для вибору одного з декількох вхідних сигналів. Працює у двох режимах:
> <ul>
>   <li><b>firstActive</b> — повертає перший не-порожній (не None) вхід та його індекс.</li>
>   <li><b>index</b> — повертає вхід із заданим індексом (1-базований), якщо він не порожній.</li>
> </ul>
> Динамічно керує кількістю входів через UI. Повертає обране значення та його індекс (або 0, якщо не знайдено).
> <br>
> <b>Корисно для мульти-модельних пайплайнів, умовної маршрутизації, вибору активного результату.</b>

---

# 🎨 Styles

- Styles are stored in the `Styles` folder inside this package.
- For dynamic style selection, the API endpoint `/multi_model/get_style_names` is used.
- A style is a JSON or YAML file containing an array of objects, each with `name`, `prompt`, and `negative_prompt` fields.

---

# ⚡ Installation


## Manual Install
1. Copy the `MultiModel` folder to `ComfyUI/custom_nodes/`.
2. Restart ComfyUI.

---

# 🚀 Example Usage

1. Add `ModelParamsPipeNode` to select your model and parameters.
2. Build prompts using `PromptBuilderNode` (optionally connect styles).
3. Use `KSamplerPipeNode` to generate images.
4. For multi-model pipelines, add several pipes and switch between them using `MySwitchIndex`.

---

# 🙏 Credits

- [ComfyUI](https://github.com/comfyanonymous/ComfyUI) – The base for node development and workflow.
- Authors and contributors of this package.

---

**Feedback, bug reports, and suggestions are welcome via GitHub Issues or your favorite chat!** 