from django import forms
from django.db import models
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'enter password'}),
        }
        
class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = ('first_name', 'last_name', 'phone_number', 'address', 'age')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter last name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter phone number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'enter address'}),
            'age':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter age'})
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name','last_name','phone_number','age')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter last name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter phone number'}),
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter age'})
        }


class ParkingAreaForm(forms.ModelForm):
    class Meta:
        model = Parking_area
        fields = '__all__'
        exclude = ('admin_id',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'enter address'}),
            'number_of_parking_slots':  forms.TextInput(attrs={'class': 'form-control', 'type': 'number','placeholder': 'enter address'}),
            'opening_time': forms.TimeInput({'class': 'form-control', 'placeholder': 'enter opening time'}),
            'closing_time': forms.TimeInput({'class': 'form-control', 'placeholder': 'enter closing time'}),
        }
