from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def index (request):
    render(request ,'Marketplace/login.html' ,
    {
        "products" :Product.objects.all()
    })

def login (request):
    render(request ,'Marketplace/login.html')

def registe (request):
    render(request ,'Marketplace/register.html')

