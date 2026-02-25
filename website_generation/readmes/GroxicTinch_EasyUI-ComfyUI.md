# Features
* Make a copy of a node without inputs or outputs, the widgets on the mirror node is two way synced to the original.
* Hide widgets you don't care about, or re-enable if you want it back.
* Rearrange widgets to put your favorite up the top.
* Jump from the mirror node to the original node.

# Why not just use Get and Set nodes instead?
Get and Set nodes are amazing, but:
* They create breaks in otherwise easy to follow paths
* You need to hide the Get node behind your input nodes if you are trying to minimize dead space
* It splits logic into groups, the "nice looking" part, and the important back end.

# NEED TO FIX
I still need to fix a few things, there are some pretty big bugs that I need to work on, mainly
* Reordering the widgets work when the workflow is saved, but if you just refresh the window then for some reason the order doesn't save properly
* Multi-line text cant be hidden
* Other custom widgets aren't supported and I don't know how I would go about fixing that without hard-coding them.

# TODO
- [ ] Hide title bar of mirror node.
- [ ] Fix the 10px under the last widget that I can't seem to remove.
- [ ] Allow combining of multiple real nodes into one mirror node.
