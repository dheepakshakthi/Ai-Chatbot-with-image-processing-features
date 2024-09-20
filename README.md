<h1>Hercules-GPT</h1>
for image generation type : generate image 'your prompt' <br>
for caption generation type : generate caption <br>
for enhancing an image type : enhance image <br>
for trying the object detection feature type : detect objects 
<h2>About the project: </h2>
This is a ai chatbot application powered by google gemini. It has image processing features such as object detection, caption generation, image generation and image enhancement. 
Our primary goal for this project was to create a chabot which can analyze is environment with its image processing features and generate images.  <br><br>

<b>This project is just a prototype</b> <br>

The backend of this application is written using python language. We used python-flask to create this application, this application runs on local host. <br>
As said, google's gemini api is used for the chatbot. You can replace the api key with your own api key. <br><br>
![image](https://github.com/user-attachments/assets/011b02d8-68a2-4fd5-aa67-b44c6441c5c0)
<br><br>
Mask-R-CNN model and COCO dataset is used for object detection, BLIP image captioning model is used for cpation generation for images, Stable diffusion model is used for image generation and ESRGAN is used for enhancing the images.
<br><br>
You can change between "float32" and "float16" according to our need (float16 is faster). <br>
You can also change between "DPMSolverMultistepScheduler" and "EulerDiscreteScheduler".
![image](https://github.com/user-attachments/assets/3e310cc1-ed9b-4897-a771-e38190041857)
<br>use float16 for faster computational time. If you get black image as an ouput then use float32.<br>
The full path of the COCO anotations file "instances_val2017.json" should be given <br>
![image](https://github.com/user-attachments/assets/cf10800e-297a-4d93-8337-d6a165abd08f)
<br>
The full path of RRDB_ESRGAN_x4.pth file should be given <br>
![image](https://github.com/user-attachments/assets/8e720dc0-b700-4aa0-a9ac-2eb06aff378e) <br>
The full path of instances_val2017.json file should be given <br>
![image](https://github.com/user-attachments/assets/bce9b3cc-fc5a-457b-8909-16d8fe867f54)

<h2>Limitations:</h2>
- The image enhancement feature doesnt work on all png images but works on all jpg and jpeg images <br>
- The image enhancement feature is very slow due to implementation<br>
- laptops with GTX series graphics processors or any other graphics cards less than 6gb vram may need to use float32 in line 35 of app.py file (check if the generated image is a black image when using float16, if the image is not a black image then you can use float16 else use float32)<br>
- image generation and image enhancement features are not recomended to use in laptops/pc's without dedicated graphics<br>

<h2>Recomended System Requirements:</h2>
a PC or laptop with dedicated graphics card (with cuda cores)

<h1>Problems and fixes</h1>
feel free to contact if any problems are found in this prototype <br>
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
