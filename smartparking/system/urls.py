from django.urls import path
from .views import index,userregistration,userlogin,userdashboard,userorders
urlpatterns = [
    path('',index,name="index"),
    path('userregistration/', userregistration, name="userregistration"),
    path('userlogin/', userlogin, name="userlogin"),
    path('userdashboard/', userdashboard, name="userdashboard"),
    path('userorders/', userorders, name="userorders"),
]
