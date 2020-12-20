from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login,logout
from .models import *
# Create your views here.
def index (request):
    return render(request ,'Marketplace/index.html' ,
    {
        "products" : Product.objects.all() #product have  : name , id ,price ,seller ,image
    })

def login (request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request , user)
            return render(request, 'Marketplace/index.html')
        else:
            return render(request, 'Marketplace/register.html')
    return render(request, 'Marketplace/login.html')

def register (request):
    return render(request ,'Marketplace/register.html')
