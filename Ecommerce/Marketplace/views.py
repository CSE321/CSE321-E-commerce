from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.forms import inlineformset_factory
from .models import *
from .forms import CreateUserForm
from django.contrib.auth.forms import  UserCreationForm

# Create your views here.
type="Customer"
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

    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(request.POST)
            form.save()
            user_data = User.objects.get(username=form.cleaned_data["username"])
            if(request.POST["usertype"]=="option2"):
                seller =Seller(user=user_data ,email=request.POST["email"], address=request.POST["address"] ,credit_card_number=request.POST["credit_card_number"])
                seller.save()
            else:
                customer =Customer(user=user_data ,email=request.POST["email"], address=request.POST["address"] ,credit_card_number=request.POST["credit_card_number"])
                customer.save()
    context = {'form': form}
    return render(request, 'Marketplace/register.html', context)