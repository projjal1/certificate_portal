from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
import os
import platform

def base(request):
    return render(request,"home.html")

def login(request): 
    if request.method=="POST":
        user=auth.authenticate(username=request.POST['username'],password=request.POST['pass1'])
        if (user!=None):
            auth.login(request,user)
            return render(request,"home.html")
        else:
            return render(request,"log.html",{'error':'User does not exist or password is wrong.'})
    else:
        return render(request,"log.html")

def logout(request):
    auth.logout(request)
    return redirect("base")

def purge(request):
    if(request.method=='POST'):
        if(platform.system()=='Windows'):
            os.system('del /q /s admin_files')
            os.system('cat>admin_files/entry.txt')
        else :
            os.system('rm -r admin_files')
            os.system('echo.>admin_files/entry.txt')

        return redirect('base')
    
    else:
        x=0
        data=open('admin_files/entry.txt','r')
        for each in data:
            x+=1
        data.close()
        return render(request,'purge.html',{'ds':x})


