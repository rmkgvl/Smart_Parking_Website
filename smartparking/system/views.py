from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .forms import *
# Create your views here.
def index(request):
    return HttpResponse("index")

def adminlogin(request):
    return render(request,'system/adminlogin.html',{})

def adminregistration(request):
    registered = False
    message = []
    if(request.method=="POST"):
        form = AdminForm(data=request.POST)
        try:
            if(form.is_valid()):
                password1 = form.cleaned_data['password1']
                password2 = form.cleaned_data['password2']
                if(password1!=password2):
                    message=['passwords are not matching']
                else:
                    form.save()
                    registered=True
        except ValidationError as e:
            print(str(e))
    else:
        form = AdminForm()
    return render(request, 'system/adminregistration.html', {'form': form, 'registered': registered, 'message': message})


def userregistration(request):
    return HttpResponse("user registration")

def userlogin(request):
    return HttpResponse("user userlogin")

def userdashboard(request):
    return HttpResponse("user userdashboard")

def userorders(request):
    return HttpResponse("user userorders")
