# ComfyUI Text Randomizer 1.0.0
<sub>[About](#comfyui-text-randomizer-100) | [Custom nodes](#custom-nodes) | [Workflows](#workflows) | [Tips](#tips)</sub>

A simple text randomizer for ComfyUI that can generate random and surprising results.

![image](https://github.com/user-attachments/assets/b4e98518-bc24-4ef1-80fc-c038e0eeb94e)


## Custom nodes
<sub>[About](#comfyui-text-randomizer-100) | [Custom nodes](#custom-nodes) | [Workflows](#workflows) | [Tips](#tips)</sub>

- ### Text randomizer
   The Text Randomizer node randomizes text placed between brackets. Options should be separated by `|`, and any text outside the brackets remains unchanged.

   **Example:** 
   Input text: `[man|girl], sitting on a [bench|grass]`.
   Possible outcomes:
   - man, sitting on a bench
   - girl, sitting on a bench
   - man, sitting on a grass
   - girl, sitting on a grass

   **Note:** You can nest brackets to create more varied outcomes.

- ### Text randomizer with check
   Similar to `Text Randomizer`, but it displays a warning if brackets or parentheses are mismatched. This check happens in real time, so you don’t need to run the workflow to see the errors.

   **Note:** The check works separately for brackets and parentheses. For example, input like `[ ( ] )` will pass the check.

- ### Get one text or another at random
   Returns one of two text options at random.

- ### Concatenate text
   Joins two pieces of text, adding `, ` between them.

- ### Show text
   Displays the final text you’ve generated. This is useful for debugging your prompts and checking what is fed into the TextEncoder.

## Workflows
<sub>[About](#comfyui-text-randomizer-100) | [Custom nodes](#custom-nodes) | [Workflows](#workflows) | [Tips](#tips)</sub>

You can find example workflows in the `/workflows` folder.

### workflow.json
Demonstrates how to achieve similar text outputs in different ways, either by grouping separate topics and concatenating texts or putting everything into one node.

![Zrzut ekranu 2025-03-02 200221](https://github.com/user-attachments/assets/c9d222b1-3dfe-43b1-a8e3-b4ca2080b13d)

### workflow2.json
Shows how to randomize two text nodes and return text from either one node or another.

![Zrzut ekranu 2025-03-02 203735](https://github.com/user-attachments/assets/e90f5d26-d23e-4fc4-b4d0-70eb3cf95d9e)

## Tips
<sub>[About](#comfyui-text-randomizer-100) | [Custom nodes](#custom-nodes) | [Workflows](#workflows) | [Tips](#tips)</sub>

- You can use `Text Randomizer with Check` as a simple tool to check brackets without connecting it to anything. Just paste your text inside to see if your brackets or parentheses match.

- By adding `|` at the end of the expression, you can create an empty option. For example (spaces added for clarity): `[ apple | banana | grapefruit | orange | ]` gives an equal chance to select "apple," "banana," "grapefruit," "orange," or nothing. \
\
   Other examples:

   - [apple|] gives a 50% chance of getting "apple" and 50% chance of getting nothing.
   - [apple||] gives a 33.3% chance of getting "apple" and a 66.6% chance of getting nothing.


