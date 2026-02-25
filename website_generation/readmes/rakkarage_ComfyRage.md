# ComfyRage

## Example

![Screenshot](screenshot.png)

```
({cat, {collar|}|dog, {collar|leash, ({viewer_holding_leash|})|}, {bone||}}), [[ornate_border], simple_background] // test
```

## Install

Either:

- Search ComfyUI Manager for `ComfyRage` and Install.

Or:

- Clone into `ComfyUI/custom_nodes`.

## Nodes

### ⚙️Pre

ComfyUI expands random prompt syntax **only when the text is written directly into a CLIP text input**. When the prompt is refactored to prevent duplication or routed through sub-graphs, the random syntax is **not expanded**.

The **Pre** node expands it once so the final text can be reliably viewed, reused, and passed consistently to downstream nodes.

You can combine **Pre** with **Show** or **Debug** to inspect the output, or pass the expanded text directly to an encoder.

**Features:**

- **Strip comments:** /* // */: `/* comment1 */ tag1, tag2, // comment2`
- **Expand random:** {|}: `{tag1|tag2|tag3, {tag4|}}`
- **Expand de-emphasis:** []: `[more[less]]`

---

### ⚙️Show

ComfyUI provides **Preview Any** to display text as it flows through a workflow, but it doesn't persist, so eventually it becomes impossible to inspect.

The **Show** node lets you **inspect the text at any point**, without modifying it, which is useful for debugging or verifying prompts.

**Features:**

- Display text persistently in the node for inspection.
- Optionally pass input as output.

---

### ⚙️Debug

ComfyUI does not provide a way to visualize weights, such as de-emphasis or nested weighting.

The **Debug** node lets you **inspect prompt weights** helping you understand how the final prompt will be interpreted by the encoder.

**Features:**

- Display weights persistently in the node for inspection.
- Optionally pass input as output.

---

### ⚙️Notify

ComfyUI does not provide a way to notify the user when a run is complete.

The **Notify** node lets you **be alertered** with browser notification and sound. (Not adding **any** artifacts to image queue.)

**Features:**

- Display browser notification.
- Play sound.
