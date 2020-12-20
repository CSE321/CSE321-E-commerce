from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

from .models import *

# Create your views here.
def index(request):
    return render(request, 'Marketplace/index.html', {
        "products": Product.objects.all()     # product has fields: name , id ,price ,seller ,image
    })


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





def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}

    return render(request, 'Marketplace/register.html')
