# Introduction
GetFileNameFromURL is a ComfyUI custom node that extracts the filename from a URL. It can handle various URLs and is capable of handling redirects.
<img width="1026" alt="image" src="https://github.com/githubYiheng/ComfyUI_GetFileNameFromURL/assets/5706385/29e33bea-cfb3-4b26-b481-c3c97f6556f4">

# Features
Extracts filename from a URL
Handles 303 redirects
# Usage
In your terminal, navigate to the custom_nodes directory of your ComfyUI installation.
Clone this repository using the git clone command:
```bash
git clone https://github.com/githubYiheng/ComfyUI_GetFileNameFromURL.git
```
Restart ComfyUI.
In ComfyUI, locate the "Get FileName From URL" node.
Input the desired URL into the node's url field.
Run the node, and it will output both the extracted filename and the original URL.
# Inputs
* url (STRING): The URL from which to extract the filename.
# Outputs
* filename (STRING): The extracted filename.
* url (STRING): The input URL.
# Example
## Input: 
* https://example.com/path/to/file.jpg

## Output:

* filename: file.jpg
* url: https://example.com/path/to/file.jpg
# Dependencies
requests
cgi
