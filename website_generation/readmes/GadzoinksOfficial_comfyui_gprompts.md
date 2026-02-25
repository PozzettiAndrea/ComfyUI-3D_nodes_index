# ComfyUI GPrompts Nodes

## Introduction
This package provides four custom nodes for ComfyUI that enhance prompt generation, string formatting, and image saving capabilities.

## Nodes Overview
- **GPrompts** - Create dynamic prompts with random or sequential selection. Also support wildcard files.
- **String Formatter** - Build custom output strings from multiple inputs and system variables
- **Save Image With Notes** - Save images with embedded workflow notes and metadata
- **Save Image To Immich Server** - Save images with embedded workflow notes to an Immich server.

---

## GPrompts Node

### Description
This is another dyanmic prompts node for Comfyui, I found most of the ones out there to be either
too complicated or too limiting, so I wrote my own.

### Prompt Format Syntax

### Basics
```

create a gprompts node and connect its output
to a clip node text input

Format of a dynamic prompt
{ cat | dog | jackalope  }     random selection
{{ green | yellow | red }}      sequential seletion

If you generate 4 images with "a stop light showing {{ green | yellow | red }}"
you will get a green light image, yellow, red, and then another green.

If you use "a stop light showing { green | yellow | red }", each image will have a 33% chance of any color.


Wildcards
wildcard files are either .txt or .json and go in comfyui/models/wildcards

you can use a wildcard file with a list of options
"a woman with {{__hair_color__}} {{__hair_style__}} hair"

This will use the contents of comfyui/models/wildcards/hair_color.txt
and hair_style.txt

assuming the files are
blonde
red
brown

and

long
short
pixie
mohawk

you will have 12 combinations. Set comfyui to generate 12 images and you will
see all combinations

json wildcard files
instead of text you can use a json file. For example  seasons.json
 simple --   { "doesnotmatter" : ["summer","winter","fall","spring" ] } 
 weighted --   { "whatever" : [ { "summer" : 6 } ,  { "spring" : 4 } ,  
          {"fall" : 3 } ,  { "winter" : 1 }  ] }
weighted is only relevant to {} random selection, with random the odds of 
getting  a choice are weight/total weights. so for summer odds are 6 out of 14.
for {{}} sequential you will get all 4 seasons.

A wildcard reference to __hair__hairstyles__ , will use the file models/wildcards/hair/hairstyles.txt ( or .json )

Version 2.0 Update
Nothing has changed in regards to core functionality, but the node now outputs the computed_prompt and the seed.

Advanced:
there is an optional dynaprompt output that can connect to a node that understands how to utiltize it to extract the dynamic prompt and the computed prompt.   see the gadzoinks custom node as an example .
Note: Dynaprompts don't seem to be used much so ignore this.

TODO:
 need to add support for wildcard files that include other wildcard files
```


# String Formatter

## Description
Builds an output strng from supplied inputs and from system variables.
for example if use connect prompt (or computed_prompt) to A and seed to B, then the format string "generating $a with seed $b on $hostname" you will generate a string a like "generating a smiling cat with seed 12345 on hal2000"

## 📝 System Variables Reference

This node provides access to various system variables that can be used in your workflows. Below is a complete list of available variables:

### 📅 Date & Time Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `datetime` | Full date and time | `2024-01-15 14:30:25` |
| `date` | Current date | `2024-01-15` |
| `time` | Current time | `14:30:25` |
| `time_24h` | 24-hour format time | `14:30` |
| `time_12h` | 12-hour format time | `02:30 PM` |
| `iso_datetime` | ISO format datetime | `2024-01-15T14:30:25.123456` |
| `timestamp` | Unix timestamp (seconds) | `1705329025` |
| `timestamp_ms` | Unix timestamp (milliseconds) | `1705329025123` |
| `year` | Full year | `2024` |
| `year_short` | Short year | `24` |
| `month` | Full month name | `January` |
| `month_num` | Month number | `01` |
| `day` | Day of month | `15` |
| `day_num` | Day number (alias for `day`) | `15` |
| `hour` | Hour | `14` |
| `minute` | Minute | `30` |
| `second` | Second | `25` |
| `am_pm` | AM/PM indicator | `PM` |
| `weekday` | Full weekday name | `Monday` |
| `weekday_short` | Short weekday name | `Mon` |

### 🎲 Random & Unique Identifiers
| Variable | Description | Example |
|----------|-------------|---------|
| `uuid` | Full UUID v4 | `123e4567-e89b-12d3-a456-426614174000` |
| `uuid_short` | First 8 chars of UUID | `123e4567` |
| `random_hex` | Random hex string (32-bit) | `a1b2c3d4` |
| `random_int` | Random 4-digit number | `7352` |
| `counter` | Sequential counter (6-digit, increments per execution) | `000042` |
| `batch_id` | Batch identifier (last 8 digits of timestamp_ms) | `90251234` |

### 🗂️ Path & Directory Variables
| Variable | Description | Example |
|----------|-------------|---------|
| `date_path` | Date formatted as path | `2024/01/15` |
| `datetime_path` | Datetime formatted as path | `20240115_143025` |
| `cwd` | Current working directory | `/path/to/comfyui` |
| `model_dir` | ComfyUI models directory | `/path/to/models` |
| `input_dir` | ComfyUI input directory | `/path/to/input` |
| `output_dir` | ComfyUI output directory | `/path/to/output` |
| `temp_dir` | ComfyUI temp directory | `/path/to/temp` |

### 💻 System Information
| Variable | Description | Example |
|----------|-------------|---------|
| `hostname` | Computer hostname | `my-workstation` |
| `node` | Network node name | `my-workstation` |
| `os` | Operating system with release | `Windows 10` |
| `system` | System name | `Windows` |
| `release` | System release | `10.0.19045` |
| `platform` | Full platform info | `Windows-10-10.0.19045` |
| `machine` | Machine type | `AMD64` |
| `processor` | Processor info | `Intel64 Family 6 Model 158` |
| `architecture` | System architecture | `64bit` |
| `cpu_count` | Number of CPU cores | `16` |
| `pid` | Process ID | `12345` |
| `python_version` | Python version | `3.10.12` |
| `user` | Current username | `username` |

### 🎮 GPU Information (if available)
| Variable | Description | Example |
|----------|-------------|---------|
| `cuda_available` | CUDA availability | `True` / `False` |
| `gpu_name` | GPU device name | `NVIDIA GeForce RTX 4090` |
| `gpu_count` | Number of GPUs detected | `1` |

# Save Image With Notes

## Description
This node modifies a copy of you workflow adding a notes node in the new workflow that is then saved inside the image.
You can add your own text with 'notes' input
or wire the  'computed_node' from Gprompts which creates a Note and saves the computed prompt in the exif json

Note: This node uses the standard comfyui Save Image node to do the actual saving.

# Save Image To Immich Server

## Description
Save image to an Immich server https://immich.app
This node modifies a copy of you workflow adding a notes node in the new workflow that is then saved inside the image.
You can add your own text with 'notes' input
or wire the  'computed_node' from Gprompts which creates a Note and saves the computed prompt in the exif json
Supports adding images to Albums, and adding tags.

## Configuration
Create an API Key in your Immich server.

Install the node in Comfyui and go to Settings, in Settings look for the "Gadzoiks" section.
Enter the "APi Key", the Hostname and Port.
Save Image to Disk: if disabled, the image is deleted from the comfyui server file system after uploading to Immich.
Default Album: Album to use if none specified in the Node
Defaul Tags: These Tags are combined with tags in the Node.

Node Settings
notes: takes a string and creates a Notes node that is added to the worksheet saved with the image. Often used with the String Formatter node.
Computed Prompt: ignore will be probably be removed
album: add image to album, will create album if it does not exist.
save_also: if enabled image is saved as normal with Comfyui. If disabled image on Comfyui is deleted.




