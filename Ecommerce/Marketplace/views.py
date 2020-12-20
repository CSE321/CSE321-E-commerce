from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .models import *

<<<<<<< HEAD
=======

>>>>>>> 4755182152a233527cbbc3c9be9aa079e3201676
# Create your views here.
def index(request):
    return render(request, 'Marketplace/index.html', {
        "products": Product.objects.all()     # product has fields: name , id ,price ,seller ,image
    })


<<<<<<< HEAD
def login (request):

    if request.method == "Post":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'Marketplace/login.html',{
                "message":"wrong username or password"
            })


    return render(request, 'Marketplace/login.html')



=======
def login(request):
    return render(request, 'Marketplace/login.html')

>>>>>>> 4755182152a233527cbbc3c9be9aa079e3201676

def register(request):
    return render(request, 'Marketplace/register.html')
