from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout

from .models import *


def index(request):

    if "orders" not in request.session:
        request.session["orders"] = []

    if request.method == "POST":
        products = Product.objects.filter(name=request.POST["search"])
        return render(request, 'Marketplace/index.html', {
            "products": products,
            "message": "Search results"
        })
    else:
        print(request.user)
        return render(request, 'Marketplace/index.html', {
            "products": Product.objects.all(),
            "message": "Shop all products"
        })


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'Marketplace/login.html', {
                "message": "wrong username or password"
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
            if request.POST["usertype"] == "option2":
                seller = Seller(user=user_data,
                                email=request.POST["email"],
                                address=request.POST["address"],
                                credit_card_number=request.POST["credit_card_number"])
                seller.save()
            else:
                customer = Customer(user=user_data,
                                    email=request.POST["email"],
                                    address=request.POST["address"],
                                    credit_card_number=request.POST["credit_card_number"])
                customer.save()
    context = {'form': form}
    return render(request, 'Marketplace/register.html', context)


# TODO save new reviews in the db
def product(request, id):
    if request.method == "POST":
        review = request.POST["review"]
    product = Product.objects.get(id=id)
    category = product.category
    reviews = Review.objects.filter(product=id)
    similar_products = Product.objects.filter(category=category).exclude(id=id)
    return render(request, 'Marketplace/product.html', {
        'product': product,
        'reviews': reviews,
        "similar_products": similar_products
    })
    

def dashboard(request):
    try:
        seller_id = request.user.seller.id
        products = Product.objects.filter(seller=seller_id)
        return render(request, 'Marketplace/register.html', {
            'products': products,
            })
    except:
        return HttpResponseRedirect(reverse("login"))


def cart(request):
    user_cart = []
    for orders in request.session["orders"]:
        product_id = orders["product_id"]
        quantity = orders["quantity"]
        user_cart.append([Product.objects.get(id=product_id), quantity])  #[[product , quntity] , [], []] => for order in cart  order[0].name oreder[1]
        return render(request, 'Marketplace/cart.html', {
            'cart': user_cart
        })


def addtocart(request, id):
    request.session["orders"] += [{"product_id ": id, "quantity": request.POST['quantity']}]
    print(request.session["orders"])
    return HttpResponseRedirect(reverse("index"))


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("index"))
