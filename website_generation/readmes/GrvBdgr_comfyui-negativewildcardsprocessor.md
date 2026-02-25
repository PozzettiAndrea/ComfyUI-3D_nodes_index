# comfyui-negativewildcardsprocessor

Contains two prompt manipulation nodes for ComfyUI.

**Negative wildcards processor**
Moves any text from the positive prompt to the negative prompt, that is surrounded by <! !>.
Useful for creating wildcards that include negative prompts like this:
{ rain, <!umbrella,!> | sunshine, <!sunglasses,!> }

Example usage and connections:
![image](https://github.com/user-attachments/assets/0a38353b-7bec-4a5e-ba36-0883af3b21a8)

**Custom token processor**

Moves any text from the source prompt to the target prompt, that is surrounded by the given token.
Useful for creating wildcards where part of the prompt is used differently than the rest (eg. part of the prompt goes to a sampler using a certain model, while the rest of the prompt goes to a sampler with a different model).
If the token is "zyup", any text between <zyup .. zyup> will be moved from the source prompt to the target prompt (see example below).

Example usage and connections:
![image](https://github.com/user-attachments/assets/931e90ba-0636-4a54-8f2a-22d01fd0519c)
