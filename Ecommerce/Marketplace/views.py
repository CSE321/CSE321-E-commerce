from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index (request):
    return render(request ,'Marketplace/index.html' ,
    {
        "products" : Product.objects.all() #product have  : name , id ,price ,seller ,image
    })


def login (request):
    return    render(request ,'Marketplace/login.html')

def register (request):
    return render(request ,'Marketplace/register.html')
