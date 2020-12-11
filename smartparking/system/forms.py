from django import forms
from django.db import models
from .models import *

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter last name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter email'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter phone number'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'confirm password'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter address'}),
            'age':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter age'})
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class ParkingAreaForm(forms.ModelForm):
    class Meta:
        model = Parking_area
        fields = '__all__'
        exclude = ('admin_id',)
