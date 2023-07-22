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

def login_users(request):
    
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            login(request,user)
            return render(request,'authentication/success.html',{'name':"meh"})
        else:
            new_email = f"{request.POST.get('username')}@example.com"
            new_user = User.objects.create_user(request.POST.get('username'),new_email,request.POST.get('password'))
            return render(request,'authentication/fail.html',{'name':"ehhhh"})
    return render(request,'authentication/login.html',{})

