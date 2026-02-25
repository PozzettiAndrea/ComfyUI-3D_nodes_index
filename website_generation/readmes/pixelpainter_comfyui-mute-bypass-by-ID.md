# comfyui-mute-bypass-by-ID
This pack includes 5 custom nodes:
These nodes were made with love and passion for Comfyui. If you like these nodes, please think about giving me a star, or if inclined, feel free to buy me a coffee :) <a href="https://buymeacoffee.com/pixelpainter">buymeacoffee/pixelpainter</a>


Mute/Bypass (2 nodes): Can be used standalone or promoted/linked to subgraph widgets. They support targeting nested nodes by ID, even handling duplicate IDs in different Subgraphs correctly.

A/B Switch (2 nodes): Toggles between two target IDs (activating A mutes/bypasses B, and activating B mutes/bypasses A). Includes a standard and a multi-switch variant.<br/>

**02/23/2026**<br/>
**Added new Stacker node**<br/>
**Updated Readme.md**</br>
**Scroll to the end to see updated intrsuctions for the new node.**</br>

**12/29/2025**<br/>
**Major Version Update V2.0.0**
* This will now reliably mute or bypass any node in any Subgraph using the Subgraph ID and Node ID together.<br/>
* Comfyui can sometimes assign a duplicate ID for nodes in different subgraphs, this latest update fixes this issue.<br/>

**01/16/2026**<br/>
**Minor Version Update V2.1.0**<br/>
* Custom UI was causing instability, reverted to standard comfyui widgets.
* After a widget has been slected, re-clicking the picker retains the path of the target.<br/>
* Since the node target path is retained in the picker, I removed the path underneath the widget to save space, and remove clutter.<br/>
* Added target node ID path inside the picker ie [209:25:103] > [subgraph:subgraph:node target]<br/>
* The picker is now linkable and promotable.<br/>
* The A/B switch does not visually turn off and on, but remains the same color to indicate that the node is still active.<br/>
* Multiple nodes with the same widget name no longer cause a conflict error when promoting or linking.<br/><br/>

**5 Nodes**<br/>
**02/23/2026**<br/>
Please scroll to the end of the instructions for information on the new Stacker node.</br>

<img width="315" height="226" alt="image" src="https://github.com/user-attachments/assets/98360aee-2595-445b-90b2-63d696bda232" />

Top add a node ID click the dropdown and search by node ID or name, or select a subgraph and node to mute in the menu.

If you search by ID and you see 2 nodes with the same ID check the path for the Subgraph node you are looking for.

<img width="792" height="282" alt="image" src="https://github.com/user-attachments/assets/b7bd8877-c02a-4ddc-a546-9e287d331cbc" />

https://github.com/user-attachments/assets/7a7a38e4-573d-4ee0-aa29-c5f04d130e3c

**Node 2: Remote Mute Bypass Triple**  
This switch works the same as Node 1 but it will mute/bypass any combination of 1-3 nodes at the same time

<img width="1512" height="423" alt="image" src="https://github.com/user-attachments/assets/0c0c694d-46f1-4ab4-8324-fafd627ce5a0" />

**Node 3: Remote A/B mute/bypass switch**  
TThe remaining two nodes toggle between two target IDs (activating A mutes B, and activating B mutes A). Includes a standard and a multi-switch variant.

https://github.com/user-attachments/assets/bb9f56bf-f0e2-4828-8c6f-d82e291ac565

Node 4: Double Remote A/B mute/bypass switch
This is the same as Node 3, but it will take 2 A/B input ID's and will switch mute/bypass state between 2 pairs of nodes

https://github.com/user-attachments/assets/dd206b9d-5a56-4291-beda-97a83b5e031e

**02/23/2026**<br/>
**New Stacker Node**</br>
Centralized control over multiple Mute Bypass and AB nodes from a single panel.</br>
Drop your first Stacker node onto the canvas — it automatically adds all Mute/Bypass and A/B Mute/Bypass nodes, including those inside subgraphs. Use X to remove them.</br>
Modes: Use the header buttons to switch between User (individual control), Mute (all muted), or Bypass (all bypassed). Switching back to User restores each node's previous state.</br>
Row controls: Each row shows [Title] [M/B] [●] [→] [✕] — toggle mute/bypass mode, toggle active state, move to another stacker, or remove.</br>
Using Multiple stackers: Use X to remove from a Stacker. Use + Add to pick unstacked nodes. Use → to move nodes between stackers. Nodes at any subgraph depth are supported and tracked if relocated.</br>

https://github.com/user-attachments/assets/69ba448f-e785-46ff-b44a-c00512aa4d9b





