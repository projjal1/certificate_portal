from django.shortcuts import render
import pandas as pd
from PIL import Image

def add_entry(request):
    if(request.method=='POST'):
        title=request.POST['title']
        ds=request.FILES['file_ds']
        img=request.FILES['cert']

        filename=open('admin_files/entry.txt','a')
        filename.write(title+'\n')
        filename.close()
                
        data=pd.read_csv(ds)
        data.to_csv('admin_files/'+title+'.csv')

        img=Image.open(img)
        img.save('admin_files/'+title+'.jpg')

        return render(request,'upload.html',{'error':'Upload done'})

    else :
        return render(request,'upload.html')
