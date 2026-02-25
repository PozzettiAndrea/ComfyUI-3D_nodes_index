# ComfyUI-DisableBrowserLogs

A simple extension for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that suppresses console messages from JavaScript. It blocks all levels--`log`, `info`, `error`, and so on--though you could easily customize it for your needs.

Use it with care and remember to disable it if you need to debug something.

## What's it good for?

Certain nodes or even Comfy itself can print thousands of messages per job, resulting in slower execution times and interface lag. Check your developer tools (F12) if this applies to you.

In my case, I was seeing tons of errors related to using Get-Set nodes as subgraph inputs. The workflow ran fine, except for slowdowns caused by the log statements. But now everything is nice and snappy.