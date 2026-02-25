# KaleidiaNodes
A simple set of nodes I created for comfyui to make things easier for me.

There are two sets of nodes so far: file nodes, string nodes and a random prompt node.

## File Nodes
There are two nodes here so far, one for counting png files in the comfy output directory and one for reading a csv file within the project's file structure.

### File Counter
<img width="472" height="119" alt="image" src="https://github.com/user-attachments/assets/7cc3027c-bd80-4d9d-881d-27b88986c0c4" />

This is a simple node with an input of a path or just directory name and an output of type integer for the count of files there. 
It goes to the configured output directory and adds a directory if none of the provided name is present or goes into the provided folder and counts all png files present in there. It returns either that amount or the highest prefix in the beginning of files as I like to have a counter there ("00000 - prompt.png" is my preferred output file name). In the case that there are 8 files in the directory and the highest prefix is 00010, it will return 11 (the previous highest +1).

### CSV Reader
<img width="310" height="195" alt="image" src="https://github.com/user-attachments/assets/f31cc8da-7e52-46b8-a97d-f4babd3025bf" />

This node was supposed to be general csv file reader for files with the structure "name,prompt,negative_prompt". Due to the static nature of nodes in just python, it was changed and now reads the file "styles.csv" from the provided data directory. It then lists all names from that file in a combo / selection box and returns the prompt and negative prompt texts in their respective outputs. Further use of these outputs depends on the individual setup, for my use case, I replace the word *prompt* with an additional prompt providing subject and further info. All the positive sample prompts have the word *prompt* in the positive part and the negative prompt can be appended to a general negative prompt.

#### Custom Styles or Other Applications
There are numerous ways to use this node apart from just providing styles. You can extent or replace the entries in the styles.csv file however you like. The node just reads the first column as the name, the second as a prompt or first output and the third as a negative prompt or second output. As long as the structure is kept like this, there should be no problem with loading the file. Any additional columns should be ignored. Columns that start with *>>>>>>* are used in the file to organize different groups of styles, those are also ignored in the parsing process.

Sadly due to the static nature of the python nodes and me not tackling js to make it more dynamic, the filename is hardcoded at this point and no other file in the data folder will be loaded. 

Despite the name, the file can also be used to save and load reusable prompts with positive and negative parts. 

## String Nodes
There are three string nodes so far, one that formats an integer into a string with optional leading zeroes, one that generates a random integer and gives it out as either int or string and the the same with a floating point number.

### Int To String
<img width="448" height="282" alt="image" src="https://github.com/user-attachments/assets/9678a13b-72a0-43d7-a270-ce5bec3db370" />

This node gets an integer as input and can format it to a specified number of digits adding leading zeroes. It then outputs that number either as a formatted string or as an integer (basically passing the int through to be used for other calculations later). The added zeroes are optional and can be turned off with the *use digits* switch at the bottom. That does not change the digits of the provided integer.

### Random Int to String
This node generates a random integer in the provided range from min to max and outputs that as a string.
### Random Float to String
Similar to the integer node, it generates a random float in the range and returns the formatted string.

## Random Prompt nodes
There are two nodes for random input so far.

Both can handle {...|...|...} as well as wildcards in from of txt, yaml and json files. For txt files, it can find them in subfolders and can handle the * for selecting all files in a folder.
The nodes searches for wildcards in the standard wildcard folder under the root directory of ComfyUI. Json and yaml files can be used if they are inside that folder, nesting them inside subfolders is planned for future releases.

Both nodes handle complex prompts and have the functionality of add multiple results for a selection with the syntax of {numberOfItterations$$choice1|choice2...}, so a {2$$blue|red|green|yellow} would pick two of those choices and display them. 

The Nodes include an option of join style, so there you can pick if the results are separated by comma, dot, "and" or just an empty space. 

Both nodes also have a debug toggle to display debug output in the console. can be quite helpful to see how the results were chosen and in what order.

The options can be weighted in the style {0.7::red|blue|1.5::green}, so here it would prefer green over blue and blue over red. If no number is given the node assumes a 1::, a weight of 1. The weights do not need to add up to 1 or 100%. In the given example red would be rarely chosen as green is prefered and then blue has standard weight.

### Random Prompts
There is a simple node that just handles normal random operations. This mode just gathers all possible options for the expression and picks a random result.

<img width="472" alt="image" src="https://github.com/user-attachments/assets/1717fa45-2a9a-469e-8fda-5113b88f4b64" />

The node has a history function that remembers (only in the current session, not persistent over restarts of the UI) a specified number of used options, so if you have a long list of option in your wildcards it should not pick the same option in a row, the number set here gives the pool size after which the options are allowed again. For a wildcard with 30 entries and no repetitions the number can be set to 30 to get only unique results.

### Sequential Prompts
There is also the node that can handle a sequential setup:

<img width="472" alt="image" src="https://github.com/user-attachments/assets/1182fa2a-c73f-4cfa-bd9c-7b2054988fdb" />

This mode tries to pick results in order of all possible options. In case of nested terms "a {{blue|red} car|{yellow|green} bike}" it will create results like: "a blue car", "a red car", "a yellow bike" and "a green bike" before starting from the beginning in the same order. 

The mode on the top determents the algorithm for sorting. It uses a gear system that locks one part and only advances the other. On an prompt of {blue|red|yellow|green} {car|cat|tree} the first option will fix "blue" and go through all second options before switching to "red". The second option will do the opposite, fix "car" and go through the colors first before switching to "cat".

The "sequential passes" option is a number of passes in the internal system that should be sequential. This is a failsafe option for complex prompts with many wildcard references so that only the specified number of passes will be sequential and the rest just random as normal. Useful for character descriptions with leading categories like "game characters", "female"/"Male" and then a detailed descriptions but with some random elements there. So for a passes set to 2, it would go through all female and then all male characters but if the individual results have nested wildcards or choices, those will be handles randomly. best way here is to check the log with debug mode enabled.

The "index offset" is used to not start at 0 for the list. All possible choices will be put in a list and that usually starts at index 0, if we want to get results of index 3 and onwards, we can change the index offset to 3 and it will start with index 3. Keep in mind that the index persists on the same session, so if one run goes from index 0 to index 3, the next run without a restart will be at index 3. Every active and not deactived node will run even if it not connected, so some indicies can be off if the node was just disconnected from the workflow but not deactivated (turns purple on standard settings if deactivated). Debug will also run for nodes that are part of the workflow but not connected with cables, so either deactivate debug on disconnected nodes or disable them.
