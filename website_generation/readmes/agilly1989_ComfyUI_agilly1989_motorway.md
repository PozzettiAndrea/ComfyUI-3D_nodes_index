# BIG BROKEN WITH ASYNC WILL FIX WHEN I GET THE TIME/MOTIVATION 

# What is this?

CURRENTLY IN ACTIVE DEVELOPMENT (BETA)! IF THINGS BREAK ITS BECAUSE I BROKE IT.

This my implemenation of a "pipe" in ComfyUI. Is it better or worse than others? No idea.


# Big Update (2-Feb-25) - 1.1.0

* Added procedually generated Motorway Nodes
  * "Motorway-ed" Nodes can be found in the menu and ""most"" should work. Ones that wont work will be
    * Those who have custom JS
    * Output Nodes
* Changed the name for the Motorway to be more .... fun
* Tweaked some stuff

NOTE: Your flows might break, Sorry, I haven't "Finished" this project so please be paitent with me

# Installation
Open your `ComfyUI/custom_nodes` folder and git clone this repository

You can now also find it in ComfyUI Manager

# Usage
The node pattern is `Motorway [amount of inputs]x[amount of outputs]` so
* 1x5 would be 1 input and 5 outputs
* 0x3 would be 0 inputs and 3 outputs
* 420x69 would be 420 inputs and 69 outputs (not possible with current node code but you get the idea)
* etc

Type in a key to identify what that input is and use it later down the "Motorway", Load the `Example.json` into ComfyUI to see what I mean.

You must start with the "MotorwayStart" node

# Behind the Scenes
The motorway is ~~*literally* just a dict~~ now a custom class that gets passed on from node to node, so if you use an existing key later down the "Motorway" it will be overwritten

# Why Did I make this?
I didn't like how other "pipe" implementations were implemented.

# Compatibility

As far as I know, it should be compatible with all nodes, but if something breaks, tell me or "just don't use it"

# Will it break

Maybe, but "It works on my System"

# I want more inputs / outputs

If you go looking in `ramps/generated.py` you will see `MAX_IN` and `MAX_OUT`.. Enter whatever number you want (up to __52__)

# Feature Creep
* [ ] Move configuration values to a config file (`yaml`, `toml`, `ini`, `xml`, something)
* [ ] Motorway Merge (will probably be a "update A with B" thing)
* [x] Make it so it loads last and makes a clone of existing nodes so you don't need to add "Motorway" nodes
  * Will probably need patching of the node loading system to ensure that this loads last in the sequence, mega jank but will do the job

# Things I need to do
* [ ] Tidy up
* [x] Rename stuff maybe?
* [ ] Properly name nodes (haven't gotten around to it yet)

# Errors
If you see an error about `'MotorwayClass' object has no attribute 'hash_` that is because that key (as a sha256 hash) doesn't exist in the Motorway. Double check your key values.

# Help me please!

You can find me in the [Comfy Org discord](https://discord.com/invite/comfyorg) as `@agilly1989` or feel free to open an issue above. Do not DM me on Discord, you will be ignored.