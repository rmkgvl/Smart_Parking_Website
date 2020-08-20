from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
import pyrebase


# Create your views here.
def index(request):
    return render(request,'authentication/base.html',{})

def user_login(request):
    return render(request,'authentication/login.html',{"login":"login"})

def user_register(request):
    return render(request,'authentication/login.html',{"register":"register"})

def user_login_submit(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    auth = firebase_auth.auth()
    user = auth.sign_in_with_email_and_password(email, password)
    print(user)
    if not user==None:
        return render(request,'authentication/base.html',{})
    else:
        return render(request,'authentication/login.html',{"message","Invalid login credentials"})
    


def user_register_submit(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    auth = firebase_auth.auth()
    user = auth.create_user_with_email_and_password(email, password)
    print(user)
    if not user==None:
        return render(request,'authentication/base.html',{})
    else:
        return render(request,'authentication/login.html',{"message","User could not be registered"})
    return render(request,'authentication/login.html',{})