# comfyui-zeug

comfyui-zeug (German for "gear" or "stuff") is a collection of custom nodes for ComfyUI, designed to provide missing features and improve usability. It includes various utility nodes which make it easier to work with data and perform common tasks e.g. specifying width and height tuples, passthrough logging, and more.

## Installation
#### Manual
1. Clone the repository into your ComfyUI custom nodes directory (e.g. `D:\comfyui\custom_nodes`):
    ```bash
    git clone https://github.com/adrianschubek/comfyui-zeug
    ```
#### Manager
1. Open ComfyUI Manager and search for `zeug`.
2. Click on the install button next to `ComfyUI-Zeug`.
## Documentation
- [Values](#values)
- [Conversion (between types)](#conversion-between-types)
- [Transform](#transform)
- [Extra](#extra)

# Values
Basic data input nodes for creating and managing primitive data types.

### Int (ZeugInt)
**Description:** Provides an integer value as output.

#### Inputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| value  | integer | Integer input.    |

#### Outputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| int    | integer | Integer output.   |

### Float (ZeugFloat)
**Description:** Provides a float value as output.

#### Inputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| value  | float   | Float input.      |

#### Outputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| float  | float   | Float output.     |

### String (ZeugStr)
**Description:** Provides a string value as output.

#### Inputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| value  | string  | String input.     |

#### Outputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| string | string  | String output.    |

### Bool (ZeugBool)
**Description:** Provides a boolean value as output.

#### Inputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| value  | boolean | Boolean input.    |

#### Outputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| bool   | boolean | Boolean output.   |

---

# Conversion (between types)
Nodes that convert between different data types.

### Int to String (ZeugIntToStr)
**Description:** Converts an integer to a string.

#### Inputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| value  | integer | Integer input.    |

#### Outputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| string | string  | String output.    |

### String to Int (ZeugStrToInt)
**Description:** Converts a string to an integer.

#### Inputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| text   | string  | String input.     |

#### Outputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| int    | integer | Integer output.   |

### Float to String (ZeugFloatToStr)
**Description:** Converts a float to a string.

#### Inputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| value  | float   | Float input.      |

#### Outputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| string | string  | String output.    |

### String to Float (ZeugStrToFloat)
**Description:** Converts a string to a float.

#### Inputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| text   | string  | String input.     |

#### Outputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| float  | float   | Float output.     |

### Int to WidthHeight Tuple (ZeugIntToWxH)
**Description:** Converts two integers (width and height) into a tuple.

#### Inputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| width  | integer | Width value.      |
| height | integer | Height value.     |

#### Outputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| wxh    | WxH     | Tuple (width, height). |

### WidthHeight Tuple to Int (ZeugWxHToInt)
**Description:** Splits a tuple into width and height integers.

#### Inputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| wxh    | WxH     | Tuple input.      |

#### Outputs
| Name   | Type    | Description       |
|--------|---------|-------------------|
| width  | integer | Width value.      |
| height | integer | Height value.     |

---

# Transform
Transform nodes that modify or process data.

### Split String List (ZeugSplitStrList)
**Description:** Splits a string into a list of strings based on a delimiter.

#### Inputs
| Name           | Type    | Description               |
|----------------|---------|---------------------------|
| text           | string  | String to split.          |
| delimiter      | string  | Delimiter for splitting.  |
| strip_whitespace | boolean | Whether to strip whitespace. |

#### Outputs
| Name     | Type         | Description               |
|----------|--------------|---------------------------|
| strings  | list[string] | List of split strings.    |

### Join List Strings (ZeugJoinStrList)
**Description:** Joins a list of strings into a single string using a delimiter.

#### Inputs
| Name       | Type         | Description               |
|------------|--------------|---------------------------|
| strings    | list[string] | List of strings to join.  |
| delimiter  | string       | Delimiter for joining.    |

#### Outputs
| Name   | Type    | Description               |
|--------|---------|---------------------------|
| text   | string  | Joined string.            |

### Join Strings (ZeugJoinStr)
**Description:** Joins two strings with a delimiter.

#### Inputs
| Name       | Type    | Description               |
|------------|---------|---------------------------|
| string_a   | string  | First string.             |
| string_b   | string  | Second string.            |
| delimiter  | string  | Delimiter for joining.    |

#### Outputs
| Name   | Type    | Description               |
|--------|---------|---------------------------|
| string | string  | Joined string.            |

---

# Extra
Miscellaneous nodes that don't fit into other categories.

### Print (ZeugPrintPass)
**Description:** Prints a message to the console and passes the input unchanged.

#### Inputs
| Name       | Type    | Description               |
|------------|---------|---------------------------|
| input      | any     | Any input.                |
| prefix     | string  | Prefix for the message.   |
| message    | string  | Message to print.         |

#### Outputs
| Name   | Type    | Description               |
|--------|---------|---------------------------|
| output | any     | Pass-through input.       |

### Clean GPU (ZeugCleanGpuPass)
**Description:** Cleans GPU memory and passes the input unchanged.

#### Inputs
| Name   | Type    | Description               |
|--------|---------|---------------------------|
| input  | any     | Any input.                |

#### Outputs
| Name   | Type    | Description               |
|--------|---------|---------------------------|
| output | any     | Pass-through input.       |