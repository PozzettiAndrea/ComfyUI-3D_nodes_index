"# daves_nodes" 
What is Daves Nodes?
Well there are times I need a node that doesnt exist and until now I have simply gone "darn, thats a shame".
Now I have decided when I need a node that I can not find already created, I will create it (if i can)

Nodes: 

Daves Text To List:
This simple node takes a large chunk of text and splits it at the points where a key word is placed. This allows a single piece of text to be split into multiple prompts. 
So why not use the few that exist? well they all split at new lines, I needed to have new lines intact and split at key points.

The main usage for this (for me) is when i take a prompt list from an AI. It takes time for a powerful AI to respond to a prompt, way longer than a single image takes to create... so I have the AI create 10 verations of my request and respond with a list seperated by the word <split> this is then turned into a list with this node. (blank lines are also removed)