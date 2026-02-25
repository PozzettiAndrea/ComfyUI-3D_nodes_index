ComfyUI - String Utils
=============================================================================

Collection of custom nodes for ComfyUI dedicated to the analysis and
transformation of text strings, such as for formatting and conversions
between types.

Install
-----------------------------------------------------------------------------

**Option 1**

Install via [ComfyUI-Manager][3].

**Option 2**

Clone the repository into your ComfyUI custom_nodes directory.
```text
git clone https://github.com/exectails/comfyui-et_stringutils
```

Nodes
-----------------------------------------------------------------------------

### Text Formatter

Several nodes with varying numbers of optional inputs that can be used
in conjunction with a formatting string to create the output. The node
uses standard [python string formatting][1].

The nodes are useful to compose prompts based on variable inputs and
can be combined with [dynamic prompts][2] for even more flexibility.

**Example**

Insert values into a string.

Format
```text
"Hello, {arg0}! Did you know? {arg1} is the answer to everything."
```

Input
```text
arg0: "John"
arg1: 42
```

Output
```text
"Hello, John! Did you know? 42 is the answer to everything."
```

### Replace Text

Replaces a string in a text with something else, using either plain text
replacement or regular expressions (regex).

**Example 1**

Replace a word in a text.

Input
```text
text: "Hello, John!"
replace: "John"
replacement: "Mr. Smith"
```

Output
```text
"Hello, Mr. Smith!"
```

**Example 2**

Replace a pattern in a text using regex and use a captured part in the
replacement.

Input
```text
text: "Hello, John! Did you know 42 is the answer to everything?"
replace: "([0-9]+) is"
replacement: "\1 is in fact"
```

Output
```text
"Hello, John! Did you know 42 is in fact the answer to everything?"
```

### ATOI/ITOA

Two simple nodes to convert strings to integers and vice versa.


[1]: https://docs.python.org/3/tutorial/inputoutput.html
[2]: https://github.com/exectails/comfyui-et_dynamicprompts
[3]: https://github.com/ltdrdata/ComfyUI-Manager
