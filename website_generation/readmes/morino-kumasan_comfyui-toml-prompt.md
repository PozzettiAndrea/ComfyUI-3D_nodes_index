# comfyui-utils

ComfyUI custom nodes.

## Install

```
cd ComfyUI/custom_nodes
git clone git@github.com:morino-kumasan/comfyui-utils.git
cd ../../
python_embeded/python -m pip install -r ComfyUI/custom_nodes/comfyui-utils/requirements.txt
```

## How to use
See sample workflows.

## PromptDecode

### text

_t is prompt.
_k is available keys for random choice.
_w is weight for random choice with _k.
_e is chance(0.0~1.0) for all choice with _k.
_export is string to export to output.
_f is called by toml_key_name().
_post is post prompt key.

```
# key _t is prompt
[base]
_t="score_9, score_8_up, score_7_up, source_anime"

# direct string prompt
quality="best quality"

color=["dark", "light", "dark blue"]

[base.girl]
_t="""1girl, perfect anatomy, 
beautiful face, (detailed skin), (detailed face), (beautiful detailed eyes),  
shiny hair, $color hair"""
# $color is replaced with red, blue or blonde.

twintails = "twintails, <lora:twintails.safetensors:1>"
ponytails = "ponytails"
color=["red", "blue", "blonde"]

[base.boy]
_t = "1boy, muscular, $::color hair, formal suit"
# $color is replaced with dark, light or dark blue

# "base().test" equals "base._f.test"
[base._f]
_t = "base() is called"

test="test1"

# "random_weight.?" to select a or b or c
[random_weight]
_k = ["a", "b", "c"]
# random select weight
_w = [0.8, 0.1, 0.1]
a = "80%"
b = "10%"
c = "10%"

# "random_weight.*" to select a and b and c
[random_weight2]
_k = ["a", "b", "c"]
# each select ratio
_r = [0.8, 0.3, 0.3]
a = "80%"
b = "30%"
c = "30%"

# "post._post" equels "post._post.*.??"
[post]
_t = "main prompt"
_post = ["post_prompt.*", "::post_prompt2.?"]
[post.post_prompt]
_when = "base.boy"
_r = [0.1, 0.1, 1.0]
all1 = "10%"
all2 = "10%"
[post_prompt2]
_w = [0.5, 0.5]
one1 = "one1 or one2"
one2 = "one1 or one2"

[_exports]
key = "value"
```

### lora_info

```<lora:lora_name:strength>``` is replaced with prompt.

```
["<lora>"]
"lora.safetensors" = "lora prompt"
```

### key_name_list

```
// this is commont
# this is comment
/* this is comment */
quality          /* encode as "best quality" */
base, quality    /* encode as "score_9, score_8_up, score_7_up, source_anime, best quality" */
{base | quality} /* encode as "score_9, score_8_up, score_7_up, source_anime" or "best quality" */
base.girl        /* equals "base, base.girl", but not duplicate prompt. */
base.girl+boy    /* equals "base, base.girl, base.boy" */
base.?           /* equals "{base.girl | base.boy}" */
base.??          /* equals "{base.girl.twintails | base.girl.ponytails | base.boy}" */
<lora:lora.safetensors:1> /* load LoRA and encode as "lora prompt" */
<raw>
  /* raw positive prompt */
  this line is raw positive prompt.
</raw>
<neg>
  /* raw negative prompt */
  this line is raw negative prompt.
</neg>
<case>
  /* key_name1 if key name is already loaded else key_name2 */
  <when key=base.girl>
    key_name1
  </when>
  <else>
    key_name2
  </else>
</case>
<random a=0.1 b=0.9>
  /* 10%: key_a, 90%: key_b */
  <when key=a>key_a</when>
  <when key=b>key_b</when>
</random>
<?route fix base girl>    /* fix random choise, "base.??" is always "base.girl" */
<?route find base girl>   /* fix random choise, "base.??" is always tag including girl */
<?route remove base girl> /* fix random choise, "base.??" is always tag excluding girl */
<?export key value> /* export key=value */
<?set color black>                 /* _v.color = ["black"] */
<?set base.girl.color 'cyan blue'> /* base.girl._v.color = ["cyan blue"] */
<?grep color 'ark'>                /* _v.color = ["dark", "dark blue"] */
```

## MultipleLoraTagLoader

Output multiple LoRA tags. (max 10)

- Input
  - lora_name_0
    - LoRA filename.
  - strength_0
    - LoRA modify strengh.
  - lora_name_1
  - strength_1
  - ...
  - lora_name_9
  - strength_9
- Output
  - STRING
    - LoRA tag list separated by line break.
