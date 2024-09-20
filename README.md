<h1>Hercules-GPT</h1>
for image generation type : generate image 'prompt' <br>
for caption generation type : generate caption
<h2>About the project: </h2>
This is a web ai chatbot powered by google gemini. It has image processing features such as object detection, caption generation and image generation. 
Our primary goal for this project was to create a chabot which can analyze is environment with its image processing features.  
This project is a prototype.

This application is written using python language. We used flask to create this as a web application, this application runs on local host. <br>
As said, google's gemini api is used for the chatbot. You can replace the api key with your own api key. <br><br>
![image](https://github.com/user-attachments/assets/011b02d8-68a2-4fd5-aa67-b44c6441c5c0)
<br><br>
Mask-R-CNN model and COCO dataset is used for object detection, BLIP image captioning model is used for cpation generation for images and Stable diffusion model is used for image generation.
<br><br>
You can change between "float32" and "float16" according to our need (float16 is faster and recomended if you have vram less than or equal to 4gb). <br>
You can also change between "DPMSolverMultistepScheduler" and "EulerDiscreteScheduler".
![image](https://github.com/user-attachments/assets/3e310cc1-ed9b-4897-a771-e38190041857)
<br><br>
The full path of the COCO anotations file "instances_val2017.json" should be given <br>
![image](https://github.com/user-attachments/assets/cf10800e-297a-4d93-8337-d6a165abd08f)
<br>

<h2>Recomended System Requirements:</h2>
a PC or laptop with dedicated graphics card (with cuda cores)

<h1>Problems and fixes</h1>
Some of you guys might get an error like this one below: <br><br>
<pre>
Traceback (most recent call last):
  File "d:\testing\Web_Ai_Chatbot-master\app.py", line 4, in <module>
  File "d:\testing\Web_Ai_Chatbot-master\app.py", line 4, in <module>
    from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
    from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
  File "D:\testing\Web_Ai_Chatbot-master\.venv\lib\site-packages\diffusers\__init__.py", line 5, in <module>
  File "D:\testing\Web_Ai_Chatbot-master\.venv\lib\site-packages\diffusers\__init__.py", line 5, in <module>
    from .utils import (
  File "D:\testing\Web_Ai_Chatbot-master\.venv\lib\site-packages\diffusers\utils\__init__.py", line 100, in <module>
    from .peft_utils import (
  File "D:\testing\Web_Ai_Chatbot-master\.venv\lib\site-packages\diffusers\utils\peft_utils.py", line 28, in <module>
    import torch
  File "D:\testing\Web_Ai_Chatbot-master\.venv\lib\site-packages\torch\__init__.py", line 148, in <module>
    raise err
OSError: [WinError 126] The specified module could not be found. Error loading "D:\testing\Web_Ai_Chatbot-master\.venv\lib\site-packages\torch\lib\fbgemm.dll" or one of its dependencies.
</pre>
<br>
To solve this you can attach a file <b>"libomp140.x86_64.dll"</b> in the path <b>"C:\Windows\System32"</b> or install Visual Studio C/C++. The program will work after this fix. <br><br>
<b>Link to download the libomp140.x86_64.dll file : <a href="https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbXQwWXc0RWwwd01KczdtMDMtTTQ1bndmMW9FUXxBQ3Jtc0tuNUpsRVg0S1NYVmxrVk9JYllRV3JVQ3BadjBjTS1FeEhuNTdwY1ZYb1RIY3Ztd3M2Y0w0UUhqck5XSDAyeUJkT1h0S2QtN1lBM3lxZmlFOVlVY3k2aTZmU1ZRZy1Xb1Y2UW0xVXdtYVNvOV9GT0wxQQ&q=https%3A%2F%2Fgithub.com%2Frorymulcahey%2Flibomp140.x86_64.dll%2Fraw%2Fmain%2Flibomp140.x86_64.dll&v=npPdd7wk3Ok">libomp140.x86_64.dll</a></b>
