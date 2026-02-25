[**日本語**](./README_JP.md)

# ComfyUI-Jumper
Designed to integrate local ComfyUI with remote ComfyUI(ex: Runpod, Vast.ai)<br />
Pass string, images, audio between multiple ComfyUI via network.<br />
[YouTube Demo](https://youtu.be/VYwOMiZOJfU)<br />

*On Remote*
![example](https://github.com/myonmu0/ComfyUI-Jumper/blob/main/examples/remote.png)
*On Local*
![example](https://github.com/myonmu0/ComfyUI-Jumper/blob/main/examples/local.png)

## What can do?
- **Combining resource:** Instead of doing all job on 1 machine, you can do one part on local and another on remote.
 
- **Usability:** Depending on the case, receiving the remote generated data inside local ComfyUI may be convenient.

- **Privacy:** If run a workflow like the example on the remote, your data are NOT write on remote server disk, so the likelihood of your data(prompts, input image and video, generated image and video) to leak or expose to someone may reduce. If you expect privacy, don't connect your data to preview/save node in the remote.

## Install
```
cd ComfyUI/custom_nodes/
git clone https://github.com/myonmu0/ComfyUI-Jumper
```

## Usage
1. Rent one server, or start 2 ComfyUI on local.<br />

2. Open a port on remote, MUST use a secure channel like SSH Tunnel.
```
ssh root@REMOTE_IP -p REMOTE_PORT -NL 8282:localhost:8282
```
 - *Default port are 8282, however you can change this in nodes.py DEFAULT_ADDR val, or manually change on node.*
 - *If you will integrate local with local, skip this.*<br />

3. Start local and remote ComfyUI. As tutorial, load the examples/local.json to local ComfyUI, examples/remote.json to remote ComfyUI and run both to see if works.
 - *Accessing remote ComfyUI with SSH Tunnel are secure, easy and simple way that works on all cloud provider.*
 - *Accessing remote ComfyUI with browser's private/secret mode is a cleaner option because starts with 0 browser data, and ends with 0 data.*<br />

⚠️ **Known Issue:**
 Job cancel button don't work when this node are running, in such case restart ComfyUI.


## Details 
Select all node "mode" to "Client" on local, and "Server" on remote.

1 Jumper node chain on 1 workflow.

The node "order" determine the order of sending/receiving data, and must be chain correctly on both side. Don't forget to add at least 1 node on the end of Jumper node chain(like in the example)

| send_as | Size        | CPU         | About                                    |
| --------- | -------------  | --------------- | ------------------------------------------------- |
| png     | Small       |  Moderate   | Convert tensor to png before sending.	<sub>Progress bar: 1 = Conversion, 2 = Sending</sub>    |
| zlib    | Large       |  Moderate   | Compress tensor before sending.          |
| raw     | Very Large  |  Very Low   | Raw tensor are send.  | 

Audio nodes: "Send Audio", "Receive Audio"



