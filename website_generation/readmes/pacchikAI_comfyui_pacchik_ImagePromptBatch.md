# ImagePromptBatch
A simple comfyui Node for Loading images and thier prompts

Get it working
1. Download this folder (or git clone) into custom_nodes directory and restart Comfyui
2. load the JSON provided for example
3. Connect the Image Path node to load your image
4. Connec the Prompt to your prompt
5. install the missing nodes
6. create a folder anywhere example (home/user/test)
7. create your prompt.csv file (it should have 3 columns, 1st the index, second the name of the image and third the prompt that you want to load)
8. save all the images in the same folder
9. set the seed to 0; batch queue to the total number of files you want loaded (for example if you have 0-100 images, queue 100)
10.  every queue it will automatically change the image and prompt based on the index you have


THE SAMPLE CODE HERE IS PROVIDED “AS IS” AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE DEVELOPER OF THIS CODE BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) SUSTAINED BY YOU OR A THIRD PARTY, HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT ARISING IN ANY WAY OUT OF THE USE OF THIS SAMPLE CODE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
USE AT YOUR OWN RISK. PROVIDED TO USE HOW AND WHERE LEGALLY PERMITTED 
