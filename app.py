from flask import Flask, render_template, request, jsonify, send_file
import google.generativeai as ai
import io
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from diffusers import EulerDiscreteScheduler
from io import BytesIO
import base64
import torch
from PIL import Image
import torchvision.transforms as T
import torchvision
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from transformers import BlipProcessor, BlipForConditionalGeneration
import RRDBNet_arch as arch 
import glob
import numpy as np
import cv2
import os.path as osp
from pycocotools.coco import COCO

app = Flask(__name__)

if torch.cuda.is_available() == True:
    device = "cuda"
    print("using device CUDA")
else:
    device = "cpu"
    print("using device CPU")
    
API_KEY = 'API_KEY'

model_id = "CompVis/stable-diffusion-v1-4"
scheduler = DPMSolverMultistepScheduler.from_pretrained(model_id, subfolder="scheduler")
pipeline = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float32)
pipeline = pipeline.to(device)
pipeline.safety_checker = None

coco = COCO('PATH_TO_instances_val2017.json')  
cats = coco.loadCats(coco.getCatIds())
cat_id_to_name = {cat['id']: cat['name'] for cat in cats}

detection_model = torchvision.models.detection.maskrcnn_resnet50_fpn(weights=torchvision.models.detection.MaskRCNN_ResNet50_FPN_Weights.DEFAULT)
detection_model.eval()

model_id_2 = "Salesforce/blip-image-captioning-base"
capt_processor = BlipProcessor.from_pretrained(model_id_2)
capt_model = BlipForConditionalGeneration.from_pretrained(model_id_2).to(device)

model_path = 'PATH_TO_RRDB_ESRGAN_x4.pth'
en_model = arch.RRDBNet(3, 3, 64, 23, gc=32)
en_model.load_state_dict(torch.load(model_path), strict=True)
en_model.eval()
en_model = en_model.to(device)

def enhance_image(image):
    max_size = 1024 
    if max(image.size) > max_size:
        image.thumbnail((max_size, max_size), Image.ANTIALIAS)

    img = np.array(image)

    img = img / 255.0
    img = torch.from_numpy(np.transpose(img, (2, 0, 1))).float()
    img_LR = img.unsqueeze(0).to(device)

    with torch.no_grad():
        output = en_model(img_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()

    output = np.transpose(output, (1, 2, 0))
    output = (output * 255.0).round().astype(np.uint8)

    enhanced_image = Image.fromarray(output)
    return enhanced_image

def load_image(image_path):
    return Image.open(image_path).convert("RGB")

def generate_caption(image, model, processor, max_new_tokens=50):
    inputs = processor(image, return_tensors="pt").to(device)
    out = model.generate(**inputs, max_new_tokens=max_new_tokens)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    ai.configure(api_key=API_KEY)
    model = ai.GenerativeModel("gemini-pro")
    chat = model.start_chat()
    user_message = request.json.get('message')
    response = chat.send_message(user_message)
    response_text = response.text
    return jsonify({'response': response_text})

@app.route('/generate_image', methods=['POST'])
def generate_image():
    prompt = request.json.get('prompt')
    image = pipeline(prompt).images[0]
    
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    return jsonify({'image': img_str})

@app.route('/detect_objects', methods=['POST'])
def detect_objects():
    image_file = request.files['file']
    image = Image.open(image_file.stream)
    
    transform = T.Compose([
        T.ToTensor(),
    ])
    img_tensor = transform(image)
    img_tensor = img_tensor.unsqueeze(0)  

    with torch.no_grad():
        predictions = detection_model(img_tensor)

    fig, ax = plt.subplots(1, figsize=(12, 9))
    ax.imshow(image)

    for element in range(len(predictions[0]['boxes'])):
        box = predictions[0]['boxes'][element].cpu().numpy()
        score = predictions[0]['scores'][element].cpu().numpy()
        label_id = predictions[0]['labels'][element].cpu().numpy().item()
        label = cat_id_to_name.get(label_id, 'Unknown')

        threshold_score = 0.5
        if score >= threshold_score:
            rect = patches.Rectangle((box[0], box[1]), box[2] - box[0], box[3] - box[1], linewidth=2, edgecolor='r', facecolor='none')
            ax.add_patch(rect)
            plt.text(box[0], box[1] - 10, f'{label}: {score:.2f}', color='red', fontsize=12, weight='bold')

    plt.axis('off')

    buffered = BytesIO()
    plt.savefig(buffered, format="PNG")
    buffered.seek(0)
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return jsonify({'image': img_str})

@app.route('/generate_caption', methods=['POST'])
def generatecaption():
    file = request.files['file']

    image = load_image(file.stream)
    caption = generate_caption(image, capt_model, capt_processor, max_new_tokens=50)

    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return jsonify({'image': img_str, 'caption': caption})

@app.route('/enhance_image', methods=['POST'])
def handle_enhance_image():
    file = request.files['file']
    image = Image.open(file.stream)
    
    enhanced_image = enhance_image(image)
    
    buffered = BytesIO()
    enhanced_image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    return jsonify({'enhanced_image': img_str})

if __name__ == '__main__':
    app.run(debug=True)