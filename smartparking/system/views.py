from django.shortcuts import render, reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.core.exceptions import ValidationError
from .forms import *
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as user_login   
from django.contrib.auth.decorators import login_required
from datetime import timedelta
import datetime, time
import pytz
# Create your views here.
def index(request):
    return render(request, 'system/index.html', {})

def register(request):
    return  render(request, 'system/register.html', {})

def aboutus(request):
    return  render(request, 'system/aboutus.html', {})

def login(request):
    return render(request, 'system/login.html', {})


def userorders(request):
    return HttpResponse("userorders")



def adminlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                user_login(request,user)
                request.session['admin_id']=Admin.objects.filter(user_id = user.pk).first().id
                return HttpResponseRedirect(reverse('Admin:admindashboard'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse("INvalid Details")

    else:
        return render(request,'system/adminlogin.html',{})

def adminregistration(request):
    registered = False
    if(request.method == "POST"):
        user_form = UserForm(data=request.POST)
        admin_form = AdminForm(data=request.POST)

        if(user_form.is_valid() and admin_form.is_valid()):
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            admin = admin_form.save(commit=False)
            admin.user = user
            admin.save()
            registered = True
            return HttpResponseRedirect(reverse('Admin:adminlogin'))
        else:
            print(user_form.errors, admin_form.errors)
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
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            admin = admin_form.save(commit=False)
            admin.user = user
            admin.save()
            registered = True
            return HttpResponseRedirect(reverse('Admin:userlogin'))
        else:
            print(user_form.errors, admin_form.errors)
    else:
        user_form = UserForm()
        admin_form = CustomerForm()
    return render(request, 'system/adminregistration.html', {'user_form': user_form, 'admin_form': admin_form, 'registered': registered})

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                user_login(request,user)
                request.session['user_id'] = Customer.objects.filter(
                    user_id=user.pk).first().id
                return HttpResponseRedirect(reverse('Admin:userdashboard'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            return HttpResponse("INvalid Details")

    else:
        return render(request, 'system/userlogin.html', {})

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
    request.session['pid'] = parking_id
    parkingarea = Parking_area.objects.filter(id = parking_id)
    context = {
        'parkingarea' : parkingarea,
    }
    return render(request, 'system/aboutparkingarea.html', context)

def getstarttime(request):
    date_time = request.POST['entry-time']
    date_time = datetime.datetime.strptime(date_time, "%Y-%m-%dT%H:%M")
    date_time = pytz.timezone('Asia/Kolkata').localize(date_time, is_dst=None)
    return date_time

def getexittime(request):
    date_time = request.POST['exit-time']
    date_time = datetime.datetime.strptime(date_time, "%Y-%m-%dT%H:%M")
    date_time = pytz.timezone('Asia/Kolkata').localize(date_time, is_dst=None)
    return date_time

def check_availability(request):
    date_time = getstarttime(request)
    today = date_time.date()
    orders = Orders.objects.all().order_by('starting_time').order_by('ending_time').filter(time__date = today)
    end_time = getexittime(request)
    x = date_time
    parkingarea = Parking_area.objects.get(pk = request.session['pid'])
    while(x <= end_time):
        tmp = orders.filter(time__lte = x).filter(endtime__gte = x)
        if(len(tmp) >= parkingarea.number_of_parking_slots):
            return False
        x += timedelta(minutes = 1)

    openingtime = datetime.datetime.combine(today, parkingarea.opening_time)
    openingtime = pytz.timezone('Asia/Kolkata').localize(openingtime, is_dst=None)
    closingtime = datetime.datetime.combine(today, parkingarea.closing_time)
    closingtime = pytz.timezone('Asia/Kolkata').localize(closingtime, is_dst=None)
    
    if(openingtime <= date_time and date_time <= closingtime and openingtime <= end_time and end_time <= closingtime and date_time.date() >= datetime.date.today()):
        return True
    else:
        return False


def checkout(request):
    possible = check_availability(request)
    context = {
        'possible' : possible
    }
    return render(request, 'system/checkout.html', context)

def OrderSuccess(request):
    order = Orders(parking_area_id = request.session['pid'], customer = request.session['user_id'], vehicle_number = request.session['veh_no'], starting_time = getstarttime(request), ending_time = getexittime(request), status = False)
    order.save()
    return render(request, 'system/success.html', context)
