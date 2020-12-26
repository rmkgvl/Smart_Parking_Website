from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from .forms import *
# Create your views here.
def index(request):
    return render(request, 'system/index.html', {})

def register(request):
    return  render(request, 'system/register.html', {})

def login(request):
    return render(request, 'system/login.html', {})


def userorders(request):
    return HttpResponse("userorders")



def adminlogin(request):
    return render(request,'system/adminlogin.html',{})

def adminregistration(request):
    registered = False
    if(request.method == "POST"):
        user_form = UserForm(data=request.POST)
        admin_form = AdminForm(data=request.POST)

        if(user_form.is_valid() and admin_form.is_valid()):
            form.save()
            user.set_password(user.password)
            user.save()
            admin = admin_form.save(commit=False)
            admin.user = user
            admin.save()
            registered = True
        else:
            print(user_form.errors, owner_form.errors)
    else:
        user_form = UserForm()
        admin_form = AdminForm()
    return render(request, 'system/adminregistration.html', {'user_form': user_form, 'admin_form': admin_form, 'registered': registered})


def userregistration(request):
    registered = False
    if(request.method == "POST"):
        user_form = UserForm(data=request.POST)
        admin_form = CustomerForm(data=request.POST)

        if(user_form.is_valid() and admin_form.is_valid()):
            form.save()
            user.set_password(user.password)
            user.save()
            admin = admin_form.save(commit=False)
            admin.user = user
            admin.save()
            registered = True
        else:
            print(user_form.errors, owner_form.errors)
    else:
        user_form = UserForm()
        admin_form = CustomerForm()
    return render(request, 'system/adminregistration.html', {'user_form': user_form, 'admin_form': admin_form, 'registered': registered})

def userlogin(request):
    return HttpResponse("user userlogin")

def addparkingarea(request):
    return HttpResponse("user userlogin")

def admindashboard(request):
    admindetails = Admin.objects.filter(id = request.session['admin_id']).first()
    if(admindetails == None):
        return HttpResponse("<h1> HACKER!!! <h1>")
    context = {
        'admindetails' : admindetails
    }
    return render(request, 'system/admindashboard.html', context)


def userdashboard(request):
    userdetails = Customer.objects.filter(id=request.session['user_id']).first()
    if(userdetails == None):
        return HttpResponse("<h1> HACKER!!! <h1>")
    context = {
        'userdetails': userdetails
    }
    return render(request, 'system/userdashboard.html', context)

def adminaddparkingarea(request):
    if request.method == 'POST':
        form = AddParkingArea(data=request.POST)
        if form.is_valid():
            object1 = form.save(commit=False)
            # request.id is the primary key of the owner ( I'm not sure how to get primary key from owner here.)
            object1.admin_id = Owner.objects.get(id=request.session['admin_id'])
            object1.save()
            return HttpResponseRedirect(reverse('admin:admindashboard'))
    else:
        form = AddSalon()
    return render(request, 'admin/adminaddparkingarea.html', {'form': form})


def viewparkingareas(request):
    parkingarea = Parking_area.objects.all()
    context = {
        'parkingarea' : parkingarea,
    }
    return render(request, 'system/parkingarea.html', context)

def aboutparkingarea(request, parking_id):
    parkingarea = Parking_area.objects.filter(id = parking_id)
    context = {
        'parkingarea' : parkingarea,
    }
    return render(request, 'system/aboutparkingarea.html', context)
