# Prompt Helpers

Inspired by [Prompt Palette](https://github.com/kambara/ComfyUI-PromptPalette), but remade from scratch with more features, bug fixes, and with Nodes 2.0 support.

## Quickstart

1. Install [ComfyUI](https://docs.comfy.org/)
2. Install [ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager)
3. Look up this extension in ComfyUI-Manager.
4. Restart ComfyUI.

# Features

## `Prompt Toggle` node

![](https://github.com/Pauan/comfyui-prompt-helpers/blob/d9d4296cb84fee029c371f7ad46a958f6404b2a1/img/Prompt%20Helper.png)

The `conditioning/helpers/Prompt Toggle` node is similar to `conditioning/CLIP Text Encode (Prompt)`, but enhanced with new features:

* It supports `BREAK` which splits a single large prompt into multiple chunks.

   * Many models like SDXL have a limit of 75 tokens per prompt. You can use `BREAK` to split a large prompt into smaller chunks, which means you can now have more than 75 tokens in your prompt.

   * You can use `BREAK` to prevent concepts from bleeding. For example, you can use a prompt like this:

      ```
      1girl,
      blue_eyes,
      dress,

      BREAK

      1boy,
      green_eyes,
      jacket,
      ```

      Because the `BREAK` splits the prompt into two separate chunks, this helps the AI to understand that the `blue_eyes` and `dress` belong to the girl, and the `green_eyes` and `jacket` belong to the boy.

   * You can use `BREAK` to separate your prompt into different sections (quality, background, artist style, composition, etc.)

      ```
      // Quality tags
      masterpiece,
      best quality,

      BREAK

      // Character tags
      1girl,
      1boy,

      BREAK

      // Composition tags
      absurdly_detailed_composition,
      dutch_angle,

      BREAK

      // Background tags
      sky,
      outside_border,

      BREAK

      // Artist tags
      konpeto,
      null_\(nyanpyoun\),
      tomoshibi_hidekazu,
      ```

      This clean separation can help the AI better understand different elements of the image.

* For each line in the prompt, it displays a checkbox which makes it very easy to enable or disable that line.
* For each line in the prompt, it displays the weight, and a `-` and `+` buttons which make it very easy to increase or decrease the weight of that line.
* It automatically cleans up the prompt, keeping it clean and readable, and preventing unnecessary tokens.

You can have multiple tags per line, making it easy to enable / disable the entire tag group, or you can put each tag onto a separate line.

You can also have freeform text, such as `An anime illustration of a girl and boy. They are standing next to a tree, with the sky in the background.`

## Develop

```shell
cd ComfyUI/custom_nodes
git clone https://github.com/Pauan/comfyui-prompt-helpers.git prompt_helpers
cd prompt_helpers
yarn install
yarn build
```

The backend nodes are in `src/prompt_helpers`

The frontend JS code is in `js/main.js`

Unit tests are in `tests`
