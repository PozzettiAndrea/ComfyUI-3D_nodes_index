# Introduction
Some nodes for stable diffusion comfyui.Sometimes it helps conveniently to use less nodes for doing the same things.

If you use workflow in my "blogs" repo, you need to dowmload these nodes.I don't guarantee that the nodes will stay the same always. Some nodes maybe have been changed if you update the new version.
# How to install
## The repo
The same with others custom nodes. Just cd custom_nodes and then git clone.
## Translator model
If you use prompt translator to translate Chinese to English offline, you need download some models.
Download the translator models from https://huggingface.co/facebook/mbart-large-50-many-to-one-mmt/tree/main into folder named "model" of this repo.
The model folder tree of this repo:
model/
└── mbart-large-50-many-to-many-mmt__only_to_English/
    ├── pytorch_model.bin
    ├── config.json
    ├── sentencepiece.bpe.model
    ├── special_tokens_map.json
    ├── tmp2l0rt359
    └── tokenizer_config.json
## Environments
cd (this repo)
pip install -r requirements.txt

# Nodes Introductions
## tdxh_image
- "TdxhImageToSize": TdxhImageToSize can Convert an image to size.
- "TdxhImageToSizeAdvanced":TdxhImageToSizeAdvanced can Convert an image to size and it will let you choose what to follow:"only_width", "only_height", "both_width_and_height","width * height", "only_ratio","only_image","get_SDXL_best_size".
## tdxh_model
"TdxhLoraLoader":TdxhLoraLoader add a switch to the "LoraLoader", which shows as "bool_int" ( 0 -> OFF , 1 -> ON ), and when you set the strength it will let you choose what to follow: "only_strength_both", "strength_model_and_strength_clip".
## tdxh_data
"TdxhIntInput":TdxhIntInput returns the "INT" type.
"TdxhFloatInput":TdxhFloatInput returns the "FLOAT" type.
"TdxhStringInput":TdxhStringInput returns the "STRING" type.
"TdxhStringInputTranslator":TdxhStringInputTranslator returns the "STRING" type that has been translated. (You need to download Translator model!)
## tdxh_bool
"TdxhOnOrOff":TdxhOnOrOff returns the "NUMBER" and "INT" type. When switching to ON, it will return 1, when switching to OFF, it will return 0.
"TdxhBoolNumber":TdxhBoolNumber is the same as TdxhOnOrOff but let you choose what to follow: "control_by_master" is the main control, if OFF, return "bool_int",if ON, then only both "bool_int_from_master" and "bool_int" are 1, retrun 1. 
## tdxh_efficiency
"TdxhClipVison" : TdxhClipVison add a switch to the "CLIPVisionLoader"  and the "clip_vision".
"TdxhControlNetProcessor":TdxhControlNetProcessor add a switch to ControlNet nodes and let you can preprocess the image.(It needs AUX preprocessor nodes.)
"TdxhControlNetApply":TdxhControlNetApply add a switch to ControlNet nodes and make it efficiently.
"TdxhReference":TdxhReference make "reference_only" node more efficiently.
"TdxhImg2ImgLatent":TdxhImg2ImgLatent can switch between original(main) Latent and Image Latent ( OFF -> main Latent , ON -> Image Latent ).

# Thanks
Some codes are from The official [ComfyUI](https://github.com/comfyanonymous/ComfyUI.git) and other custom nodes like The [was-node-suite-comfyui](https://github.com/WASasquatch/was-node-suite-comfyui.git).
The translator's main code is from [prompt_translator](https://github.com/ParisNeo/prompt_translator.git).