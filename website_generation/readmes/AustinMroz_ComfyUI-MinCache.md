# ComfyUI-mincache
Modifies the caching and execution order to minimize RAM usage
- Node outputs are deleted from the cache as soon as they are no longer needed. Thus, every node re-executes on every queue.
- Execution is modified to try and minimize the number of outputs which need to be cached at once.

At current, expect to have severely worse execution time unless the workflow being used would otherwise fail to execute.
