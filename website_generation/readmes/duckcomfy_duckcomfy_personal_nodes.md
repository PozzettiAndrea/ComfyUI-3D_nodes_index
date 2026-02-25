# duckcomfy personal nodes

Random collection of nodes I use in my workflows, shared for replicability. A lot of those nodes were plundered from other sources to reduce the number of dependencies and be less vulnerable to malicious code/updates.

## Clip Chunk Manager (ALPHA)

Perhaps the only node in this pack with significant functionality you won't find elsewhere. It lets you use "BREAK" to manually split your prompt into CLIP chunks, but it also automatically adds explicit "BREAK" keywords wherever the CLIP would silently split your prompt. This happens whenever the text input loses focus. This helps you catch issues notably when the CLIP chunk boundary is in the middle of a tag. This was mostly coded by Claude (backed by a suite of manually provided test cases), so the code quality is awful. When I have time, I will refine it.
