from django.urls import path
from .views import *
from django.conf.urls.static import static

app_name = "Admin"

urlpatterns = [
    path('',index,name="index"),
    path('register/',register,name="register"),
    path('aboutus/', aboutus, name="aboutus"),
    path('login/', login, name="login"),
    path('adminregistration/',adminregistration,name="adminregistration"),
    path('adminlogin/',adminlogin,name="adminlogin"),
    path('userregistration/', userregistration, name="userregistration"),
    path('userlogin/', userlogin, name="userlogin"),
    path('userdashboard/', userdashboard, name="userdashboard"),
    path('userorders/', userorders, name="userorders"),
    path('admindashboard/',admindashboard, name = "admindashboard"),
    path('parkingarea/',viewparkingareas, name = "parkingarea"),
    path('addparkingarea/',addparkingarea, name="addparkingarea"),
    path('aboutparkingarea/<int:parking_id>/', aboutparkingarea, name = "aboutparkingarea"),
    path('success/', OrderSuccess, name = "OrderSuccess"),
    path('checkout/', checkout, name = "checkout"),
    path('adminfreeslots/<int:parking_id>/',adminfreeslots, name = "adminfreeslots"),
    path('freed/',freed, name= "freed"),
]