# ComfyUI\_Gemini\_3\_Pro\_API\_node

Gemini\_3\_Pro\_API\_node for ComfyUI
===================================================================

GEMINI IMAGE GENERATION NODE - INSTALLATION GUIDE

===================================================================



This custom node allows you to generate images using Google's Gemini API

directly within ComfyUI, supporting resolutions up to 4K.



-------------------------------------------------------------------

QUICK START - COPY \& PASTE THESE COMMANDS

-------------------------------------------------------------------



1\. Navigate to your ComfyUI directory in terminal/command prompt



2\. For Windows (PowerShell or CMD):

&nbsp;  

&nbsp;  cd C:\\Users\\\[YourUsername]\\Documents\\ComfyUI

&nbsp;  .venv\\Scripts\\activate

&nbsp;  pip install --upgrade google-genai

&nbsp;  

3\. For Linux/Mac:

&nbsp;  

&nbsp;  cd ~/ComfyUI

&nbsp;  source venv/bin/activate

&nbsp;  pip install --upgrade google-genai



4\. Verify installation (optional):

&nbsp;  

&nbsp;  pip show google-genai



5\. Set API key as environment variable (recommended):

&nbsp;  

&nbsp;  Windows (PowerShell):

&nbsp;  $env:GOOGLE\_API\_KEY="YOUR\_API\_KEY\_HERE"

&nbsp;  

&nbsp;  Windows (CMD):

&nbsp;  set GOOGLE\_API\_KEY=YOUR\_API\_KEY\_HERE

&nbsp;  

&nbsp;  Linux/Mac:

&nbsp;  export GOOGLE\_API\_KEY="YOUR\_API\_KEY\_HERE"



6\. Restart ComfyUI



-------------------------------------------------------------------

REQUIREMENTS

-------------------------------------------------------------------



\- ComfyUI installed and working

\- Python 3.8 or higher

\- Google AI Studio API key (free tier available)

\- Internet connection



-------------------------------------------------------------------

INSTALLATION STEPS

-------------------------------------------------------------------



1\. INSTALL THE NODE

&nbsp;  

&nbsp;  Copy the "Google Gemini API" folder to your ComfyUI custom nodes directory:

&nbsp;  

&nbsp;  Windows: 

&nbsp;  C:\\Users\\\[YourUsername]\\Documents\\ComfyUI\\custom\_nodes\\

&nbsp;  

&nbsp;  Linux/Mac:

&nbsp;  ~/ComfyUI/custom\_nodes/



2\. INSTALL PYTHON DEPENDENCIES

&nbsp;  

&nbsp;  Open a terminal/command prompt and navigate to your ComfyUI directory, then run:

&nbsp;  

&nbsp;  Windows (PowerShell):

&nbsp;  .\\venv\\Scripts\\activate

&nbsp;  pip install --upgrade google-genai

&nbsp;  

&nbsp;  Linux/Mac:

&nbsp;  source venv/bin/activate

&nbsp;  pip install --upgrade google-genai

&nbsp;  

&nbsp;  IMPORTANT: You need google-genai version 1.51.0 or higher for 4K support.

&nbsp;  

&nbsp;  To verify the version:

&nbsp;  pip show google-genai



3\. GET YOUR GOOGLE API KEY

&nbsp;  

&nbsp;  a) Go to: https://aistudio.google.com/app/apikey

&nbsp;  b) Sign in with your Google account

&nbsp;  c) Click "Create API Key"

&nbsp;  d) Copy the generated key (starts with "AIza...")

&nbsp;  

&nbsp;  BILLING NOTE: Image generation requires billing to be enabled.

&nbsp;  - Free tier has ZERO quota for image generation

&nbsp;  - You MUST enable billing at: https://console.cloud.google.com/billing

&nbsp;  - Set up budget alerts to avoid unexpected charges



4\. CONFIGURE THE NODE

&nbsp;  

&nbsp;  Option A: In ComfyUI Node

&nbsp;  - Paste your API key directly into the "api\_key" field

&nbsp;  

&nbsp;  Option B: Environment Variable (Recommended for security)

&nbsp;  - Set GOOGLE\_API\_KEY environment variable

&nbsp;  - The node will automatically use it if the field says "INSERT\_API\_KEY\_HERE"

&nbsp;  

&nbsp;  Windows (PowerShell):

&nbsp;  $env:GOOGLE\_API\_KEY="YOUR\_API\_KEY\_HERE"

&nbsp;  

&nbsp;  Linux/Mac:

&nbsp;  export GOOGLE\_API\_KEY="YOUR\_API\_KEY\_HERE"



5\. RESTART COMFYUI

&nbsp;  

&nbsp;  After installing dependencies, restart ComfyUI completely.



-------------------------------------------------------------------

NODE FEATURES

-------------------------------------------------------------------



\- Models: 

&nbsp; \* gemini-3-pro-image-preview (recommended, supports 4K)

&nbsp; \* gemini-2.5-flash-image



\- Resolutions:

&nbsp; \* 1K: ~1024 pixels

&nbsp; \* 2K: ~2048 pixels  

&nbsp; \* 4K: ~4096 pixels (e.g., 5504x3072 for 16:9)



\- Aspect Ratios:

&nbsp; \* 1:1, 16:9, 4:3, 3:4, 9:16, 2:3, 3:2, 4:5, 5:4, 21:9



-------------------------------------------------------------------

BUDGET PROTECTION

-------------------------------------------------------------------



To avoid unexpected charges, set up a budget alert:



1\. Go to: https://console.cloud.google.com/billing

2\. Select your billing account

3\. Click "Budgets \& alerts" (left menu)

4\. Click "Create Budget"

5\. Set monthly limit (e.g., $5 or $10)

6\. Enable email alerts at 50%, 90%, 100%



Image generation costs vary by resolution. 4K images cost more than 1K.



-------------------------------------------------------------------

TROUBLESHOOTING

-------------------------------------------------------------------



ERROR: "RESOURCE\_EXHAUSTED" or "429" error

SOLUTION: Enable billing for your Google Cloud project. Free tier has

&nbsp;         zero quota for image generation.



ERROR: "GenerateContentResponse object has no attribute 'parts'"

SOLUTION: Outdated SDK. Run: pip install --upgrade google-genai



ERROR: "Image object has no attribute 'mode'"

SOLUTION: Update GeminiImageGen.py to latest version from this folder.



ERROR: "ImageConfig not found"

SOLUTION: Upgrade google-genai to 1.51.0+: pip install --upgrade google-genai



ERROR: Images always 1K regardless of setting

SOLUTION: Ensure google-genai is version 1.51.0 or higher.



-------------------------------------------------------------------

SUPPORT

-------------------------------------------------------------------



For issues with:

\- This node: Check the GeminiImageGen.py file for updates

\- Gemini API: https://ai.google.dev/gemini-api/docs/image-generation

\- Billing: https://console.cloud.google.com/billing



===================================================================

Last Updated: 2025-11-20

===================================================================



