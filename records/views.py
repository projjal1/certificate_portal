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
        data=open('entry_file/entry.txt','r')
        for each in data:
            entry=each[:-1]
            fname='admin_files/'+entry+'.csv'
            data=pd.read_csv(fname)
            labels=data.pop('NAME')
            for each in labels:
                var=each.upper()
                if(user_upper==var):
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

        #whether or not to set event name(no for organizer)
        set_event_name=True
        if contest=='organizer':
            set_event_name=False


        l=len(usr)
        x=0
        if(l>=14):
            x=l-14
            x=x/2
        else:
            pass

        start=485-x*20

        img = Image.open(img_path)
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype("entry_file/arial.ttf",50)
        # draw.text((x, y),"Sample Text",(r,g,b))

        #changes made for organizer policy due to inconsistency in pixels
        if contest=='organizer':
            draw.text((start+180,470),usr,fill='black',font=font)
        else:
            draw.text((start,340),usr,fill='black',font=font)
        font = ImageFont.truetype("entry_file/arial.ttf",25)
        
        #print name for only non-organizer events
        if set_event_name==True:
            draw.text((530,465),contest,fill='black',font=font)
        
        img.save('output_files/output.jpg')

        with open(os.path.join(settings.BASE_DIR, 'output_files/output.jpg'), 'rb') as fp:
            response = HttpResponse(fp.read(), content_type='image/png')
            response['Content-Disposition'] = 'attachment; filename=output.jpg'
            return response
    
    else :
        return render(request,'user_dir.html')
