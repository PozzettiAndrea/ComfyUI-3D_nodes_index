# DanbooruPromptQuiz
![DanbooruPromptQuiz Preview](preview.png)  
日本語版READMEは[こちら](README.jp.md)。

- This node is for playing the game of guessing prompts by looking at images generated from prompts output by [TIPO](https://github.com/KohakuBlueleaf/z-tipo-extension), [Tagger](https://github.com/pythongosssss/ComfyUI-WD14-Tagger), etc.
- It compares the guessed prompts with the prompt tags output by TIPO, Tagger, etc., and outputs the following
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - Correct tags (True Positive)
  - Wrong tags (False Positive)
  - Missing tags (False Negative)

## Usage
- Generate prompts with TIPO, Tagger, etc.
- Generate an image based on the prompt.
- While looking at the generated image, guess the prompt entered in the “answer” field and enter it in the “input” field.
- When the “Submit” button is pressed, the percentage of correct answers and the tags that were answered correctly are output.
