
# ComfyUI Fooocus Inpaint Wrapper
The best inpaint I found is [Fooocus](https://github.com/lllyasviel/Fooocus)'s one, I've never been able to replicate these results on other GUIs. I did something very simple, this is a simple wrapper of practically all the Fooocus code, probably you could do something more refined, probably in the future I'll do something more refined and lightweight but for now it's like this :)

## Install
	cd ComfyUI/custom_nodes
	git clone https://github.com/iacoposk8/ComfyUI-Fooocus-Inpaint-Wrapper
	cd ../..
	.\python_embeded\python.exe -m pip install -r ComfyUI/custom_nodes/ComfyUI-Fooocus-Inpaint-Wrapper/Fooocus/requirements_versions.txt
The first time you run it, it will take longer because it will have to download the various models. Check the progress in the terminal.

## Quick start
There are two simple workflows in the folder of the same name, one called simple, where you will have to draw the mask by hand and the other that can generate it automatically
![simple workflow](Workflows/simple.png)
![automatic masking workflow](Workflows/automatic_masking.png)

## How does it work?
If Fooocus is updated in the future, you just need to copy the whole folder and insert it into the node. You can skip copying the models, because it will use the comfyui folder. Inside the copied folder you must also insert the launch.py ​​file that you find in this repository.
You will have to make some changes to the code. Some will be done automatically, you can find them inside the fooocus-inpaint-wrapper.py constructor
These must be done manually for now:
Edit `Fooocus/modules/async_worker.py`
and comment on the last line:
`#threading.Thread(target=worker, daemon=True).start()`
Then move a few lines up and remove:
`while True:` and `time.sleep(0.01)`

finally to have the percentage and the forecast find this code:

    async_task.yields.append(['preview', (
    	int(current_progress + async_task.callback_steps),
    	f'Sampling step {step + 1}/{total_steps}, image {current_task_id + 1}/{total_count} ...', y)])

and before this code add these lines:

    y_corrected = cv2.cvtColor(y, cv2.COLOR_RGB2BGR)
    cv2.imwrite(os.path.normpath('ComfyUI/custom_nodes/ComfyUI-Fooocus-Inpaint-Wrapper/image.png'), y_corrected)
    with open(os.path.normpath("ComfyUI/custom_nodes/ComfyUI-Fooocus-Inpaint-Wrapper/percentage.txt"), "w", encoding="utf-8") as file:
    	file.write(str(int(current_progress + async_task.callback_steps)))

Several things could change and these instructions could no longer be valid. However, what the code does is almost all in `Fooocus/launch.py` ​​where it creates the variable `args` and sends it to `Fooocus/modules/async_worker.py`. We can get the variable `args` by running Fooocus and modifying the file `Fooocus/webui.py` by modifying this function like this:

	def get_task(*args):
		args = list(args)
		args.pop(0)
	
		print(args)
		import sys
		sys.exit()
	
		return worker.AsyncTask(args=args)

From the interface we will launch a statement and we will see the variable `args` in the terminal.

Also there is a file called clean.py which I haven't tested much but it should delete all the __pycache__ folders, remove the config files and remove all absolute references