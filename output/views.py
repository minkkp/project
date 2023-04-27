from django.shortcuts import render
from django.views.decorators.http import require_http_methods,require_POST,require_safe
from .models import *
from django.templatetags.static import static
from ultralytics import YOLO
from PIL import ImageDraw,ImageFont,Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from io import BytesIO
from json import dumps

def check_thr(pred):
    for index in range(len(pred[0].boxes.conf)):
        if float(pred[0].boxes.conf[index])<0.5:    
            return False
    return True

def check_cls(pred):
    check_detect = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0] 
    for index in range(len(pred[0].boxes.cls)):
        check_detect[int(pred[0].boxes.cls[index])]+=1
    return check_detect

def plot(img,pred):
    labels={0:'가구',1:'금속',2:'나무',3:'도기류',4:'비닐',5:'스티로폼',6:'유리',7:'의류',8:'자전거',9:'전자제품',10:'종이',11:'캔',12:'페트병',13:'플라스틱',14:'형광등'}

    for i,box in enumerate(pred[0].boxes.boxes):
        plot_img = ImageDraw.Draw(img)
        plot_img.rectangle((int(box[0]),int(box[1]),int(box[2]),int(box[3])),outline=(51,255,51),width=5)
        plot_img.text(xy=(int(box[0]),int(box[1])-35),text=labels[int(pred[0].boxes.cls[i])],fill=(255,0,0),font=ImageFont.truetype("static/font/malgunbd.ttf",30),align='center',stroke_width=2,stroke_fill=(255,255,255))
          
    output = BytesIO()
    img.save(output, format='JPEG', quality=100)
    output.seek(0)
    return InMemoryUploadedFile(output,'ImageField','result.jpg','image/jpeg',sys.getsizeof(output),None)

@require_http_methods(['GET','POST'])
def result(request):
    if request.method=='POST':    
        model = YOLO('static/model/v8m_ep75.pt')
     
        img = Image.open(request.FILES.get('image'))
        img = Image.Image.resize(img,(640,640)).convert('RGB')
        pred = model.predict(img)

        upload = Upload( 
            user_id = request.user,
            img_file = plot(img,pred),
            threshold=check_thr(pred)
        )

    upload.save()   
    context={'upload':upload,
             'detect':dumps(check_cls(pred))}
    return render(request,'output/result.html',context)

@require_http_methods(['GET','POST'])
def map(request):
    return render(request,'output/map.html')