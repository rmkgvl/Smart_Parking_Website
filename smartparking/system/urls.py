from django.urls import path
from .views import *

app_name = "Admin"

urlpatterns = [
    path('',index,name="index"),
    path('register/',register,name="register"),
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
]
