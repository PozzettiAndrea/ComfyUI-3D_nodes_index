# Prompt Verify

Prompt Verify is an interactive ComfyUI node that pauses a string flow and lets you edit the text in the browser before it continues. It is useful for quick manual tweaks to prompts, captions, or any string data without interrupting the pipeline.

## Key features
- Pauses a string and opens an inline editor in the UI for live edits.
- Submit edits with Shift+Enter, Or click on Submit button.
- Configurable timeout (default 60s, max 2400s). If the timeout elapses, the current text is sent automatically.
- Works with the built-in front-end; client and server communicate via prompt_verify_request / prompt_verify_response.

### Download Demo Video
[![Watch the demo](media/demo-thumbnail.png)](https://github.com/ialhabbal/ComfyUI-Prompt-Verify/blob/main/media/Promp-Verify.mp4?raw=true)

## How to install
1. Open ComfyUI Custom Nodes folder
2. Open a terminal window (cmd)
3. Type this: https://github.com/ialhabbal/ComfyUI-Prompt-Verify.git
4. Restart ComfyUI
5. Search for the node: Prompt Verify

## How to use
1. Connect a STRING input to the node's `text` socket. (i.e. florence2 Captioner)
2. (Optional) Provide initial text in the `editor` field to prefill the editor.
3. Set `timeout` to control how long the node waits for user edits (seconds).
4. When the node executes, the UI will show an editor. Make your changes and press Shift+Enter or click on the Submit button to submit.
5. If you don't submit before the timeout, the current text will be used and the node continues.

## Notes
- The node returns a single STRING output — the edited (or timed-out) text.
- Default timeout is 60s; maximum allowed timeout is 2400s.

Quick, and convenient text editing inside your ComfyUI flow.

MIT License,

Developed by: ialhabbal