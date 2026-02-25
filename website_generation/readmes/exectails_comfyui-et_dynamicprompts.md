ComfyUI - Dynamic Prompts
=============================================================================

Collection of custom nodes for ComfyUI implement functionality similar
to the Dynamic Prompts extension for A1111.

The nodes use the [Dynamic Prompts][1] Python module to generate prompts
the same way, and unlike the semi-official dynamic prompts nodes, the ones
in this repo are a little easier to utilize and allow the automatic
generation of all possible combinations without manual queuing.

Install
-----------------------------------------------------------------------------

**Option 1**

Install via [ComfyUI-Manager][2].

**Option 2**

Clone the repository into your ComfyUI custom_nodes directory and
install the requirements in your ComfyUI Python environment.
```text
git clone https://github.com/exectails/comfyui-et_dynamicprompts
cd comfyui-et_dynamicprompts
pip install -r requirements.txt
```

Nodes
-----------------------------------------------------------------------------

### Dynamic Prompt

Generates prompts and seeds based on text input. The node will either
generate a given number of prompts, choosing randomly from all possible
combinations, or return prompts for all possible combinations.

#### Random Prompts

The random mode generates a number of prompts, each one using randomly
chosen variations from all potential combinations.

**Example 1**

Output one prompt with three possibilities.

Input
```text
count: 1
text: "a {red|blue|green} dog"
```

Output
```python
["a red dog"]
```

**Example 2**

Output two prompts with three possibilities.

Input
```text
count: 2
text: "a {red|blue|green} dog"
```

Output
```python
["a green dog", "a red dog"]
```

**Example 3**

Output one prompt with six possibilities.

Input
```text
count: 1
text: "a {red|blue|green} dog and a {pink|yellow} cat"
```

Output
```python
["a blue dog and a yellow cat"]
```

#### Combinatorial Prompts

In this mode the node generates and returns a list of prompts that make
up every single possible combination of strings based on the input text.

**Example 1**

Output three prompts based on three possibilities.

Input
```text
"a {red|blue|green} dog"
```

Output
```python
["a red dog", "a blue dog", "a green dog"]
```

**Example 2**

Output six prompts based on six possibilities.

Input
```text
"a {red|blue|green} dog and a {pink|yellow} cat"
```

Output
```python
[
    "a red dog and a pink cat",
    "a red dog and a yellow cat",
    "a blue dog and a pink cat",
    "a blue dog and a yellow cat",
    "a green dog and a pink cat",
    "a green dog and a yellow cat",
]
```

For more information and examples, see the [Dynamic Prompts][1] repository.

#### Seeds

To give a degree of control over the seeds used in the generation
to the dynamic prompt, you may plug the result into the sampler's
seeds input. The seed will then be `fixed`, `sequential`, or `random`.

Fixing the seed is useful if you'd like to generate an image with
a certain subject but slight variations in colors or other details.
In this mode each prompt will receive the seed set on the node.

Sequential seeds start at the given seed for the first prompt and
increase by one for every subsequent one. This can be used to get
a degree of determinism, but without giving all prompts the same
seed.

Finally, random seeds are determined by the given seed, but are
randomly generated otherwise. It's very similar to sequential,
but less deterministic from the outside.


[1]: https://github.com/adieyal/dynamicprompts
[2]: https://github.com/ltdrdata/ComfyUI-Manager
