from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

from .models import *

# Create your views here.
def index(request):
    return render(request, 'Marketplace/index.html', {
        "products": Product.objects.all()     # product has fields: name , id ,price ,seller ,image
    })



def login (request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'Marketplace/login.html',{
                "message":"wrong username or password"
            })

    return render(request, 'Marketplace/login.html')




def register(request):
    return render(request, 'Marketplace/register.html')
