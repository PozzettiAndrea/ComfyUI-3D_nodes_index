## Overview

`PlaceholderReplacerByID` is a utility node designed to automate prompt assembly when working with artist IDs, style IDs, or any mapping of numbers → text labels. 

The node takes:

+ A list of prompt templates

+ A list of ID values

+ A mapping of ID → artist/style name

+ Optional automation controls

It then **replaces a literal placeholder token** (e.g., `[a1]`) inside each prompt with the artist name corresponding to the ID for that slot.

It supports:

+ Multi-prompt workflows

+ Auto-incremented IDs

+ Manual ID overrides

+ Mirroring the first prompt or first ID

+ Safe handling of missing or invalid IDs

Output includes:

+ The resolved prompts

+ Debug information
  
+ A compact list of primary IDs + artist names

# Features
**1. Literal placeholder replacement**

You define the placeholder token (default: `[a1]`).
For each prompt slot, the node replaces it with the mapped artist name.

**2. Multi-slot prompt processing**

You may include multiple prompts inside `prompt_list`, separated by a custom delimiter (default: `;;;;;`).

**3. Flexible ID handling**

The node supports three strategies:

**• Normal mode**

IDs come from the `id_sequences` list—one ID per prompt slot.

**• Auto-Step IDs**

Automatically generate IDs from a base value:
````
base, base+1, base+2, ...
````

**• Manual IDs mode**

Force IDs per slot using `manual_ids_list`.
If a slot is missing an override, it is assigned "`NOT_FOUND`" safely.

**4. Mirror modes**

+ **Mirror First Prompt:** use the first prompt string for all slots.

+ **Mirror First ID:** use the first ID for all slots.

**5. Debugging & introspection**

Outputs full processing logs and a summary of final ID→name pairs.


| Input                   | Type     | Description                                                |
| ----------------------- | -------- | ---------------------------------------------------------- |
| **id_sequences**        | INT_LIST | The ID list for slots. One entry per prompt.               |
| **prompt_list**         | STRING   | One or more templates separated by `prompt_delimiter`.     |
| **term_mappings**       | STRING   | Lines formatted as `1_artistName`.                         |
| **mirror_first_prompt** | BOOLEAN  | Use the first template for all slots.                      |
| **auto_step_ids**       | BOOLEAN  | Generate IDs automatically starting from `increment_base`. |
| **manual_ids**          | BOOLEAN  | Fully override slot IDs using `manual_ids_list`.           |
| **mirror_first_id**     | BOOLEAN  | Copy the first ID to all slots.                            |
| **manual_ids_list**     | STRING   | ID values separated by `;` for manual override.            |
| **increment_base**      | INT      | Starting value for auto-step IDs.                          |
| **placeholder_token**   | STRING   | Literal token inside templates to replace.                 |
| **prompt_delimiter**    | STRING   | Separator for splitting prompt templates.                  |

# Outputs

| Output               | Description                                                     |
| -------------------- | --------------------------------------------------------------- |
| **resolved_prompts** | All processed prompts, joined using `;;;;;`.                    |
| **debug_info**       | Text log of intermediate steps, applied rules, and parsed data. |
| **primary_ids**      | A `;`-separated list of `ID_name` or `NOT_FOUND`.               |

# Basic Example
**Setup**

**Prompts**

```
[a1] in watercolor style;;;;;[a1] in oil-painting style
```

**Term mappings**
````
1_van_gogh
2_monet
3_vermeer
````

**ID list**
````
1,2
````

**Placeholder**

````
[a1]
````

**Result**

Slot 1: ID=1 → “van_gogh”
Slot 2: ID=2 → “monet”

**Output**

````
van_gogh in watercolor style;;;;;monet in oil-painting style
````

# Example: Auto-step IDs

**Inputs**


+ `auto_step_ids = True`
+ `increment_base = 5`
+ 3 prompts


Auto-generated IDs become:
````
5, 6, 7
````

If the placeholder is `[a1]`, each prompt is filled with:


+ Slot 1 → name for ID 5
+ Slot 2 → name for ID 6
+ Slot 3 → name for ID 7



# Example: Manual ID Override

**manual_ids = True**

**manual_ids_list = "1;3"**
````
If you have 4 prompt slots, final IDs become:
[1], [3], ["NOT_FOUND"], ["NOT_FOUND"]
````

Prompts referring to "`NOT_FOUND`" produce literal "`NOT_FOUND`" or an empty replacement if placeholder has no match.

# Term Mapping Format

Each line must be:
````
ID_artistName
````

Examples:
````
14_krenz
21_shigenori_soejima
30_claude_monet
````

# Typical Workflow


**1.** Fill prompt_list with multiple templates separated by ;;;;;.


**2.** Provide ID list in id_sequences.


**3.** Paste your artist mapping list.


**4.** Define the literal placeholder token (e.g. [a1]).


**5.** Optionally enable mirror modes, auto-step, or manual-ID override.


**6.** Connect the output to your text prompt pipeline.
