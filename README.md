<h1>About the project: </h1>

This is a web ai chatbot powered by google gemini. It has image processing features such as object detection, caption generation and image generation. 
Our primary goal for this project was to create a chabot which can analyze is environment with its image processing features.  
This project is a prototype.

This application is written using python language. We used flask to create this as a web application, this application runs on local host. <br>
As said, google's gemini api is used for the chatbot. You can replace the api key with your own api key. <br><br>
![image](https://github.com/user-attachments/assets/011b02d8-68a2-4fd5-aa67-b44c6441c5c0)
<br><br>
Mask-R-CNN model and COCO dataset is used for object detection, BLIP image captioning model is used for cpation generation for images and Stable diffusion model is used for image generation.
<br><br>
You can change between "float32" and "float16" according to our need. <br>
You can also change between "DPMSolverMultistepScheduler" and "EulerDiscreteScheduler".
![image](https://github.com/user-attachments/assets/3e310cc1-ed9b-4897-a771-e38190041857)
<br><br>
The full path of the COCO anotations file "instances_val2017.json" should be given <br>
![image](https://github.com/user-attachments/assets/cf10800e-297a-4d93-8337-d6a165abd08f)
<br>

<h2>Recomended System Requirements:</h2>
a PC or laptop with dedicated graphics card (with cuda cores)
