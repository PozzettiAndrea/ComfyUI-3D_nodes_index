# comfyui-CustomCodeNode

Provide custom nodes to let you write Python code snips directly in the ComfyUI web ui.

Writing a plugin to implement some less universal small functions is really **too** troublesome.

## Usage

- Write any Python code you want, but remember not to use `return` directly in code snippets. As an alternative, you can write a function that includes a `return` and call this function to achieve the early return.
- You can use a local variable with the same name as the input pin to obtain a certain input. Similarly, you can pass an object to subsequent nodes by assigning it to a variable with the same name as the output pin.
- To save running costs, ComfyUI will try to cache the results of input invariant nodes instead of running them every time. However, this feature cannot effectively capture potential output variations (such as when using random in your code snippets). Therefore, when you expect a code node to be executed every time, please enable the `AlwaysExecute`.