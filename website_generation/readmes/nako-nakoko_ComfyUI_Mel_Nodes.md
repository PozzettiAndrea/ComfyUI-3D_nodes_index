# ComfyUI-Mel-Nodes
Custom nodes with split, random, and select functions for easy visual and management of multiple cumbersome prompts

# mel_TextSplitNode
![Example Workflow](https://github.com/nako-nakoko/ComfyUI-Mel-Nodes/blob/main/sp1.jpeg)

First, there are two ways to divide a node. One is to divide it by letters or symbols specified by delimiter, and the other is to put “:” after the numbers, as shown in the image. In this node, each token is assigned a number internally. In the image, 2.3.5 is specified, so 1 for walking and 4 for smile. 6: is empty, so it is not treated as a token in this case. If # is placed at the beginning of a line, the line is treated as a comment and excluded from tokens; if # is placed in the middle of a line, the rest of the line is excluded.This is useful for leaving long prompt notes in the text.

・max_outputs is the number of tokens to output, e.g. 3 will output 3 tokens (if multiple tokens are output, they are automatically output with a , between them).

・selected_number specifies the tokens to be output as numbers, and multiple numbers can be specified, for example, 1 4 5. If max is 3 and the selected number is a single number and random is false, only the selected tokens will be selected; if true, the missing tokens will be selected at random. 

If the seed value is left unchanged, the output will be the same.

# mel_TextSplitNode２
![Example Workflow](https://github.com/nako-nakoko/ComfyUI-Mel-Nodes/blob/main/sp2.jpeg)

This node is a text box added to the above node, but the specification is a little different. If the number of selected numbers is more than the max value, only the max value will be output, and if the selected numbers are 4 3 for text1 and 6 for text2 as in the image, 3 and 6 will always be selected as a set, and if the number of tokens is less than the max value, they will be selected from the same set. If random is true, it is the same as the above node, but if it is false and max is greater than or equal to 2, a sequential number is chosen at random.

# mel_TextFilterNode

This node outputs an empty text if the number entered in “filter_number” is the same as the number set in “filter_values”, otherwise it outputs the connected text as is. This is mainly used when two or more TextSplitNodes are used, or when you do not want this one to be output at a particular prompt.

# mel_RandomIntNode

Outputs a value of type int up to any value between 1 and 100, the value can be random, incremented, or output as is with the upper value.

# ResolutionSwitcher
![Example Workflow](https://github.com/nako-nakoko/ComfyUI-Mel-Nodes/blob/main/reso.jpeg)

Outputs the predefined width and height values, or reverses the width and height output if switch is true
