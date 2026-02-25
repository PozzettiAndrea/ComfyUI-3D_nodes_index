### Quickly search and get images from Gelbooru/Danbooru/E621 without leaving ComfyUI

https://github.com/user-attachments/assets/f1abecce-d16a-47c7-a75a-f48a74381b48

Created with the help of ChatGPT and Gemini

UI based on the FL Load Image node (highly recommended) from https://github.com/filliptm/ComfyUI_Fill-Nodes

# Changelog:
- v3.2.0
	- Added a new option 'show_file_ext' -> reveals the file extension at the top-left corner of the thumbnail
 	- Fixed video triangle indicator not resizing proportionally with the thumbnail square

- v3.1.2
	- Improved window calculation for blurry frames filter

- v3.1.1
	- Fixed calculation of WINDOW_SIZE 

- v3.1.0
	- Some of the videos that previously were not parsing 'duration' are now parsing it correctly by falling back to FFprobe directly via url.
 	- Added a basic 'filter_blurry_frames' functionality to the Online Video Frame Extractor node. Its not as effective as I was hoping but it works in some cases - although it may damage the animation a little bit. It basically checks for blurriness levels of nearby frames and selects the one with the least. You should only experiment with this when handling real life footage - hand-drawn animations do not have motion-blur.

- v3.0.1
	- Fixed missing 'opencv-python' from requirements.txt

- v3.0.0
	- Added support for videos:
 		- Videos can be displayed at full resolution within the thumbnail's squares. You can also open them in fullscreen mode.
   		- When you have a video selected and you run this node -> the current position (in ms) will be sent as output.
     	- New node included: Online Video Frame Extractor (REQUIRES FFMPEG).
        - By sending the file_url and video_current_position outputs to the new node you can make short clips of specified number of frames and fps - starting at the specified time. Useful to make 121frames 24fps / 81frames 16fps, 5s clips for Hunyuan 1.5/WAN Video datasets.
        - When a video is active and video_current_position is > 0 -> the img output of the main node will be the frame at that given video position.
        - When 'select_random_result' is True -> videos will always output the first frame and video_current_position will be 0.
		- Limitations:
  			- GIFs do not contain a progress bar and therefore their 'video_current_position' will always be 0. (You can still send gifs to the extractor node and specify 'extract_time_start_ms' because that node will download the GIF and convert it to MP4 - both files are stored as temporary files inside Comfy's TEMP dir and they will be deleted after used).
     		- When extracting from a non-zero position with the extractor node -> the video will be downloaded as a temp file up to the point where extraction starts + min(videoDuration, extract_duration_range_ms).
       			- NOTE (for devs): I've tried to stream 'Range' requests byte data straight into FFMPEG to circumvent this limitation - unsuccessfully. If you are a dev and you know how to do this then feel free to make a PR.

- v2.2.2
	- Added thumbnail_quality feature

- v2.1.0
	- Fixed OR_tags not working on Danbooru

- v2.0.0
	- Added 'select_random_result' feature

- v1.0.0
	- Initial release
