from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import  UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    telephone = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)

    class Meta:
        model= User
        fields=['username','email','password1','password2']

