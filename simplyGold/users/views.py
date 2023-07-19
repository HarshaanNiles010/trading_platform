from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def index(request):
    pass

# def login_users(request):
    
#     if request.method == "POST":
#         user = authenticate(request, username=request.POST.get('username'),password=request.POST.get('password'))
#         if user is not None:
#             login(request,user)
#             return render(request,'authentication/success.html',{'name':"meh"})
#         else:
#             new_email = f"{request.POST.get('username')}@example.com"
#             new_user = User.objects.create_user(request.POST.get('username'),new_email,request.POST.get('password'))
#             return render(request,'authentication/fail.html',{'name':"ehhhh"})
#     return render(request,'authentication/login.html',{})

def user_signup(request):
    
    if request.method == "POST":
        user_email = request.POST['user_email']
        username = request.POST['username']
        password = request.POST['password']
        user_model = get_user_model()
        
        if not username.strip():
            messages.error(request,'Something went wrong')
            return render(request,'authentication/fail.html',{'name':"ehhhh"})
        
        if user_model.objects.filter(email = user_email).exists():
            messages.error(request,'Something went wrong')
            return render(request,'authentication/fail.html',{'name':"User Already exists"})
        user_obj = user_model.objects.create_user(request.POST.get('username'),request.POST.get('user_email'),request.POST.get('password'))
        user_obj.set_password(request.POST.get('password'))
        user_obj.username = request.POST.get('username')
        user_obj.save()
        user_auth = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        
        if user_auth:
            login(request,user_auth)
            return render(request,'authentication/success.html',{'name':"User signup succesfull"})
# change this value to render something
    return render(request,'authentication/login.html')

def user_login(request):
    
    if request.method == "POST":
        user_email = request.POST['user_email']
        username = request.POST['username']
        try:
            user_auth = authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
            login(request,user_auth)
            return render(request,'authentication/success.html',{'name':"User login succesfull"})
        except:
            messages.error(request,"User login failed")
            return render(request,'authentication/fail.html',{'name':"login failed"})
    else:
        return render(request,'authentication/login.html')

def user_logout(request):
    try:
        logout(request)
    except:
        messages.error(request,"Failed to logout")
    return render(request,'authentication/login.html')