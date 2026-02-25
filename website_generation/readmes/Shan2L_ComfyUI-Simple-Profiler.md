


                    _____________  _____             _____      __     
                / ___/ __/ __/ / ___/__  _______ / __/ | /| / /     
                / /___\ \/ _/  / /__/ _ \/ __/ -_)\ \ | |/ |/ /      
            _____\___/___/___/__\___/\___/_/ _\__/___/_|__/|__/___  __
            /_  __/  _/  |/  / __/ _ \  / _ \/ /  / / / / ___/  _/ |/ /
            / / _/ // /|_/ / _// , _/ / ___/ /__/ /_/ / (_ // //    / 
            /_/ /___/_/  /_/___/_/|_| /_/  /____/\____/\___/___/_/|_/  


# Introduction

ComfyUI-Simple-Profiler is a pure backend custom node/plugin, which is used to record execution time for each node in a workflow.

It can also record the maximum device usage used during a give workflow.

All collected statistical information will be output in a .json or/and .csv file to facilatating thereafter query from web API. 

The profiling information can be fetched after the execution via address '/exec_timer/stat', more detailed use example see: [example.py](./example.py)


# How to Use 

1. Clone this repo to the `Path_to_ComfyUI/custom_nodes`

2. Restart your ComfyUI server.

3. Run a workflow from UI interface or API request.

4. The stat data of corresponding workflow will be output to the terminal of your server and become persistent in a .csv/.json file under outputs directory.


