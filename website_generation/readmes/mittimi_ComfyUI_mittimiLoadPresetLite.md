# ComfyUI_mittimiLoadPresetLite

I'm testing now...


=== note ===

If RES4LYF is installed, it will not function properly.
Adding the last three lines of the following code to RES4LYF's init.py will restore normal operation.

```
new_scheduler_name = "bong_tangent"
if new_scheduler_name not in SCHEDULER_HANDLERS:
    bong_tangent_handler = SchedulerHandler(handler=sigmas.bong_tangent_scheduler, use_ms=True)
    SCHEDULER_HANDLERS[new_scheduler_name] = bong_tangent_handler  
    SCHEDULER_NAMES.append(new_scheduler_name)

new_scheduler_name = "beta57"
    if new_scheduler_name not in SCHEDULER_NAMES:
    SCHEDULER_NAMES.append(new_scheduler_name)
```

The source is as follows.
https://github.com/ClownsharkBatwing/RES4LYF/issues/161
