from django.urls import path
from .views import *

app_name = "Admin"

urlpatterns = [
    path('',index,name="index"),
    path('adminregistration/',adminregistration,name="adminregistration"),
    path('adminlogin/',adminlogin,name="adminlogin"),
    path('userregistration/', userregistration, name="userregistration"),
    path('userlogin/', userlogin, name="userlogin"),
    path('userdashboard/', userdashboard, name="userdashboard"),
    path('userorders/', userorders, name="userorders"),
]
