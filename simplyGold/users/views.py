from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
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
            return render(request,'authentication/fail.html',{'name':"ehhh"})
    return render(request,'authentication/login.html',{})