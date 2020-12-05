from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("index")

def userregistration(request):
    return HttpResponse("user registration")

def userlogin(request):
    return HttpResponse("user userlogin")

def userdashboard(request):
    return HttpResponse("user userdashboard")

def userorders(request):
    return HttpResponse("user userorders")
