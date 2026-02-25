# TT_TextTools
Custom text tools for prompt generation in ComfyUI. These will allow you to manipulate text in different ways for better prompt making. The story combiner is the main one I use in my own work.

## TT_StoryCombiner  
For generating multiple prompts from sets of words. Lets you create a lot of variation in yourt prompts. You can create related, themed prompts, random each time. You can use your favourite chat-bot to generate the lines of text very quickly. This is randomised concatenation. You can choose between input node text, and text directly in the node. These can be mixed. Empty texts are ignored. The following screenshots are the same text(s), just randomised by the node.

![![WorkflowPreview]](https://github.com/zzubnik/TT_TextTools/blob/main/Samples/Screenshot%202025-04-02%20004045.png)

![![WorkflowPreview]](https://github.com/zzubnik/TT_TextTools/blob/main/Samples/Screenshot%202025-04-02%20010510.png)

![![WorkflowPreview]](https://github.com/zzubnik/TT_TextTools/blob/main/Samples/Screenshot%202025-04-02%20004227.png)

## TT_TextInput
A multi-line text box for feeding Story Combiner with text(s). Seen below, the nodes select a random line each time to contribute to the story.

![![WorkflowPreview]](https://github.com/zzubnik/TT_TextTools/blob/main/Samples/Screenshot%202025-04-02%20011420.png)

TextFileSelectorNode - Will select a random line from a user specified .txt file. This can be used instead of a text box.

## TT_TextReplacer

Replaces a word or a phrase with another.

![![WorkflowPreview]](https://github.com/zzubnik/TT_TextTools/blob/main/Samples/Screenshot%202025-04-03%20003700.png)
