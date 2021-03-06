from django.shortcuts import render
import pandas as pd
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
from django.http import HttpRequest,HttpResponse
import os
from django.conf import settings

def fetch(request):
    if (request.method=='POST'):
        user=request.POST['username']
        user_upper=user.upper()
        
        arr=[]
        data=open('admin_files/entry.txt','r')
        for each in data:
            entry=each[:-1]
            fname='admin_files/'+entry+'.csv'
            data=pd.read_csv(fname)
            labels=data.pop('NAME')
            for each in labels:
                if(user==each or user_upper==each):
                    arr.append(entry)
                    break

        return render(request,'validation.html',{'data':arr,'nm':user})
    else :
        return render(request,'user_dir.html')

def certificate_gen(request):
    if(request.method=='POST'):
        usr=request.POST['usr']
        contest=request.POST['contest']
        img_path='admin_files/'+contest+'.jpg'

        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("arial", 100)
        draw.text((1400,1400),usr,fill='black',font=font)
        img.save('output_files/output.jpg')

        with open(os.path.join(settings.BASE_DIR, 'output_files/output.jpg'), 'rb') as fp:
            response = HttpResponse(fp.read(), content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename=output.jpg'
            return response
    
    else :
        return render(request,'user_dir.html')
