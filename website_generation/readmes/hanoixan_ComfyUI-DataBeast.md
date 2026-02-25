# ComfyUI-DataBeast
This repository offers various nodes for data-driven processing in Comfy-UI.

## Notice:
* V0.2: Changed major APIs to be more consistent, so that the DBGet* nodes return a DBItem, and all DBConvertTo* nodes expect a DBItem as input. DBConvertToString was modified to separate "filesafe" from "shortenizing".
* V0.1 Alpha release: While useful, the API of this module has not been solidified. Use at your own risk.

## Installation

1. Clone the repository: `git clone https://github.com/hanoixan/ComfyUI-DataBeast.git`
to your ComfyUI `custom_nodes` directory
2. Install dependencies: `pip install -r requirements.txt`
3. Restart the ComfyUI server

Once this project is stable, it will be available from the Custom Nodes Manager for easier installation.

## How to Use These Nodes

### Loading and accessing data
* DBLoadData loads the contents of a .csv, .json, or .yml file (for any other extension, the YAML parser is used) into a single dictionary that is exposed as a DBItem type. This contains a single 'item' member, which references the loaded dictionary.
* You can access individual value types of this dictionary through DBGetItem, which will return them as a string.
* DBGetBatchList lets you access any list in the root dictionary, and converts it into a ComfyUI batch list. The values of the current item in batch's current iteration can then be accessed through DBGetItem.

### Manipulating data
* DBConvertToInt, DBConvertToFloat, or DBConvertToString can be used to further cast the string value returned from DBGetItem into the target type.
* DBFloatExpression and DBStringExpression are convenience nodes for manipulating float and string data, respectively. They take the raw float and string types as inputs, not DBItems.

### Expression syntax
* For DBFloatExpression and DBStringExpression, the expressions are Python expressions limited to the passed in values a,b,c, and d.
  * Ex: The float expressions `a ** b` or  `(a + b / c) * d` or the string expressions `a + b` or `f"{a}_{b}"`
* For DBGetItem and DBGetBatchList, the key expression is evaluated after concatenating it onto the type held by the node.
  * Ex: A DBGetItem is connected to the root dictionary from a DBLoadData. The DBGetItem's key expression is `['defs']['color_list'][23]`. This means that the node will return the string representation of `doc_root['defs']['color_list'][23]`.
  * Ex: A .csv file is loaded. Because .csv files are automatically turned into a dictionary with a single `'items'` key containing the contents of the file as a list, the key expression `['items'][0]` will return the first item in this list as a string.

## Safety

These nodes use Python's eval(), which is in itself _dangerous_.

To protect against malicious code, the RestrictedPython module is used to compile the bytecode for each expression, only allowing access to:
* the passed in variables
* `safe_globals`
* a simple `_getitem_` implementation

This should mitigate against malicious code and make it generally safe to use, although there is still the possibility of a bad actor creating an expression that causes catastrophic CPU usage.

A future change may be to add a custom parser and/or detect and end long computations.

## Nodes

### General

> **DBLoadData**
>
> Load data from a .csv, .json, or .yml file. It will use the correct parser based on the file extension for .csv and .json. Any other extension will fall back to the .yml parser. This data can be accessed using Python dict and array expressions using DBGetItem and DBGetBatchList
> For .csv files, all rows are represented in a list under the top key value 'items'. I.e., use `['items']` as your DBGetBatchList key.
>
> Params:
>
> * path: Path to file to load. .json and .csv are treated as their formats, anything else is interepreted as YAML.
> * filter: Pattern filter. If exclusive is true, only include lines that DO NOT match this regex filter. If not exclusive, include ONLY lines that match this filter. If using capture groups and not exclusive, all capture groups will be concatenated into the final text for that line. If empty, allow everything.
>   * Ex: `([^#]+)#?` will match initial text until a #, and then ignore the rest. Everything in the capture group is retained.
>   * Ex: If you want to embed data into another text file, create a unique prefix for the data lines, and use this filter to extract only those lines: 
>     `[ \t]*mydata:(.*)` will filter everything after the `mydata:` prefix.
> * exclusive: Exclude with pattern if true, retaining everything else. If false, include only lines with the filter regex pattern, if there is one.
> 
> Returns:
> 
> * DBItem referencing a dictionary of the entire file that was loaded. 

> **DBGetItem**
> 
> Return the string representation of a simple value relative to the DBItem, using Python array access notation.
> 
> Params:
> 
> * source: Source DBItem to query. This can come from DBLoadData, DBGetItem, or DBGetBatchList.
> * expression: The key expression to apply to the source, if necessary.
>   * Ex: To get the 2nd index of the key \"foo\" assuming the source is a dictionary, the expression is: `['foo'][1]`
> 
> Returns:
> 
> * The DBItem representation of the requested value.

> **DBGetBatchList**
>
> Get a list from some key expression in the source DBItem. The list will drive batching in ComfyUI.
> 
> Params:
> 
> * source: Source item to get data from.
> * expression: Expression to get batch list. A Python expression that when appended onto the input data leads to a list in the loaded dictionary to generate the batch items from.
>   * Ex: If we assume inputs data is a dict with an 'items' key and list value, we would write: ['items']
> 
> Returns:
> 
> * Return a list of items from the key expression, in a way that ComfyUI will use as a batch list.

### Conversion

> **DBConvertToBool**
>
> Params:
> * input: DBItem from DBGet*
>
> Returns:
> * The boolean representation if possible, False if not

> **DBConvertToInt**
>
> Params:
> * input: DBItem from DBGet*
>
> Returns:
> * The integer representation if possible, 0 if not

> **DBConvertToFloat**
>
> Params:
> * input: DBItem from DBGet*
> 
> Returns:
> * The float representation if possible, 0.0 if not

> **DBConvertToString**
>
> This will convert any input DBItem into a string representation. Lists and dictionaries are converted into JSON strings.
>
> This node can also create a string representation that can be used in a file path by removing non-alphanumeric characters and whitespace.
>
> It can also abbreviate the string by "shortenizing" it (not a technical term):  it will remove vowels, capitalize word starts, and add a small hash code to long strings.
>
> `filesafe` and `shortenize` can be combined.
>
> Params:
> * input: DBItem from DBGet*
> * filesafe: If true, remove non-alphanumeric characters, and separating with single `_`s.
> * shortenize: If true, provide an ultra-shortened version of the full string that saves space by removing vowels, and appending a 4-hex hash when strings exceed 64 characters.
> 
> Returns:
> * The string representation if possible, an empty string if not.

### Math

> **DBFloatExpression**
> 
> Evaluate a float expression.
> 
> Params:
> 
> * expression: Python math expression taking any of inputs a,b,c,d.
> * a: Input a.
> * b: Input b.
> * c: Input c.
> * d: Input d.
> 
> Returns:
> 
> * The result of the float expression.

### String

> **DBStringExpression**
> 
> Evaluate a string expression.
> 
> Params:
> 
> * expression: Python string expression taking any of inputs a,b,c,d.
> * a: Input a.
> * b: Input b.
> * c: Input c.
> * d: Input d.
> 
> Returns:
> 
> * The result of the string expression.

## The input data file format

The data file can be either CSV, JSON, or YAML. These are parsed and stored internally as a Python dictionary representation. This documentation uses YAML exclusively for examples.

The simplest usage of a file and DataBeast nodes is to access the document data by key, and/or batch a list of items in the document.

This example file is consumed by the DBLoadData node.
```
items:
  - prompt: A puppy wearing a yellow hat.
    cfg: 3
  - prompt: A cat wearing a red tie.
    cfg: 4
  - prompt: A bird wearing a silver star.
    cfg: 3.5
```

![image](image showing simple batching of a list of dictionaries)

A more advanced use case is to self-reference values within the file itself, as a way of meta-configuring your batch list items.
```
defs:
  color1: yellow
  color2: red
  color3: silver
items:
  - prompt: A puppy wearing a ${['defs']['color1']} hat.
    cfg: 3
  - prompt: A cat wearing a ${['defs']['color2']} tie.
    cfg: 4
  - prompt: A bird wearing a ${['defs']['color3']} star.
    cfg: 3.5
```

An even more advanced usage is to generate items in a list based on all permutations of a set of variables.
```
defs:
  color1: yellow
  color2: red
  color3: silver
items:
  db_exec: generate_permutation_list
  var:
    prompt:
      - "A puppy wearing a ${['defs']['color1']} hat."
      - "A cat wearing a ${['defs']['color2']} tie."
      - "A bird wearing a ${['defs']['color3']} star."
    cfg:
      min: 2
      max: 3
      steps: 4
  template:
    prompt: "$vars{['prompt']}"
    cfg: "$vars{['cfg']}"
```

Any dictionary containing the key 'db_exec' will run one of the db_exec built-in functions. In this case, we're running the 'generate_permutation_list' function, 
which will generate all permutations of the variables under the var section, per their specification. Here we have 'prompt' with 3 possible values stored in a list, 
and 'cfg' with a dictionary describing a ranged set of 4 values in the span [min, max]. That gives 12 permutations.

This will replace the 'db_exec' specification dictionary with a list of 12 versions of the dictionary specified in the 'template' section, with the inserted values
using the special `$vars{expression}` notation.

You may notice that 'cfg' is being specified as a string, but we'd really like it as a float. To make that happen, you can change these lines to:
```
    cfg:
      db_exec: to_float,
      expression: "$vars{['cfg']}"
```

'to_float' is another built-in db_exec function, and that specification dictionary is replaced with the float cast of the given string. After running, the input file
will effectively be parsed, processed, and stored in memory as:
```
defs:
  color1: yellow
  color2: red
  color3: silver
items:
  - prompt: "A puppy wearing a yellow hat."
    cfg: 2.0,
  - prompt: "A puppy wearing a yellow hat."
    cfg: 2.333,
  - prompt: "A puppy wearing a yellow hat."
    cfg: 2.666,
  - prompt: "A puppy wearing a yellow hat."
    cfg: 3.0,
  - prompt: "A cat wearing a blue tie."
    cfg: 2.0,
  - prompt: "A cat wearing a blue tie."
    cfg: 2.333,
  - prompt: "A cat wearing a blue tie."
    cfg: 2.666,
  - prompt: "A cat wearing a blue tie."
    cfg: 3.0,
  - prompt: "A bird wearing a silver star."
    cfg: 2.0,
  - prompt: "A bird wearing a silver star."
    cfg: 2.333,
  - prompt: "A bird wearing a silver star."
    cfg: 2.666,
  - prompt: "A bird wearing a silver star."
    cfg: 3.0,
```

While this is a simple example, you can use these primitives to generate lots of procedural data within this file format.

## Examples

TODO: should show how a .yml file is read and integrated into a complex ComfyUI workflow.
