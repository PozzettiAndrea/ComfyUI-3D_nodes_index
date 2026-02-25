# ComfyUI-TempFileCleaner

An extension for [ComfyUI](https://github.com/comfyanonymous/ComfyUI) that deletes or moves files out of the `temp` directory to improve performance. Highly customizable.

Comfy automatically deletes the contents of your `temp` folder on startup, but if you amass a lot of files over the course of a session, it can degrade performance - particularly if any extensions, firewall software, etc. attempt to check the `temp` folder.

<img width="400" alt="screenshot" src="https://github.com/user-attachments/assets/90a77aec-8003-4fc8-9872-3769a6ed9bbe" />

---

### age_limit (int)

Any temp files that are older than this many minutes will be removed during the cleanup routine. Set to 0 to disable age-based cleanup.

### check_frequency (int)

How often to run the cleanup routine, in minutes.

### enable_logging (bool)

Print messages to the console for debugging purposes.

### max_files (int)

Maximum number of files allowed in the temp folder. Deletes oldest files in excess of this value. Set to 0 to disable quantity-based cleanup.

### trash_destination (string)

If specified, the cleanup routine will move files to this path instead of deleting them.
