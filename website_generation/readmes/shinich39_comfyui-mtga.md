# comfyui-mtga

Make Textarea Great Again

## Usage  

Support nodes 2.0

- Undo, Redo: Ctrl+Z, Ctrl+Shift+Z
- Comment: Ctrl+/
- Indent: Tab, Shift+Tab
- AutoComplete: See below for details...
- AutoPair: All brackets with commas
- AutoIndent: Press Enter inside of brackets
- LineBreak: Ctrl+Enter, Ctrl+Shift+Enter
- LineCopy: Ctrl+C with cursor on a character
- LineCut: Ctrl+X with cursor on a character
- LinePaste: Ctrl+V with cursor on a character after single line copy e.g., "blahblah...\n"
- LineRemove: Ctrl+Shift+K

<!-- - Beautify: Ctrl+B, Ctrl+Shift+B -->
- Control weight: Ctrl+ArrowUp, Ctrl+ArrowDown

## AutoComplete

Artists, Characters, tags from Danbooru tags.  
Word from Civitai metadata.  

- Artists: Starts with "@"
- Characters: Starts with "#"
- All tags: Starts with any characters
- Embeddings: Starts with "$"
- Loras: Starts with "$$"
- Checkpoints: Starts with "$$$"

## References

- [mtga-js](https://github.com/shinich39/mtga-js)
- [danbooru-tags-json](https://github.com/shinich39/danbooru-tags-json)
- [civitai-model-json](https://github.com/shinich39/civitai-model-json)