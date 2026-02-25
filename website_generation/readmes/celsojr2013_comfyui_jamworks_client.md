# comfyui_jamworks_client
A Simple Client for Jamworks Platform DAM Integration

# Jamworks
Jamworks is a platform with various applications serving B2B marketing execution tasks, such as production workflows, DAM and automations.
This integration aims to facilitate file transfers for comfyui environment, automation of tasks and even creation of complex workflows for task management.

# Nodes
## Jamworks_Login
Recieves username and password for client api calls, it gets an auth token to be used in other tasks

## Jamworks_Download
It downloads a node_id to a path, node is an entity inside Jamworks, like a file, a folder, a rendition, a task, anything -  not a Comfyui node ^_^ - 

## Shell_Command
It runs an arbitrary shell command in the comfyui server-side environment 
# BEWARE
Shell Commands are way too unrestricted and should be used only if you must do a task or execute an action that is not inside Comfyui scope. 
Incorrect usage may cause permanent system damage! Like run a "rm -rf /" command.
"With great power, comes great responsibilities"



