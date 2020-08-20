from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from authentication import views

app_name = 'authentication'

urlpatterns=[
    path('login/',views.user_login,name='login'),
    path('login-submit/',views.user_login_submit,name='login-submit'),
    path('register/',views.user_register,name='register'),
    path('register-submit/',views.user_register_submit,name='register-submit'),
]