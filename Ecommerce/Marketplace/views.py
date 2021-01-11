from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login 
from django.contrib.auth import logout as auth_logout 

from django.contrib.auth.forms import  UserCreationForm

from .models import *



def index(request):
    print(request.session["orders"])
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





def login (request):
    if(not request.user.is_authenticated ):
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
    else :
        return HttpResponseRedirect(reverse("index"))


def register(request):
    if(not request.user.is_authenticated ):
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
    else :
        return HttpResponseRedirect(reverse("index"))




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

    


def category(request ,cat):
    return render(request, 'Marketplace/index.html', {
            "products": Product.objects.filter(category = cat) ,"message":f"{cat} category "    
        })



def logout (request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("index"))



def dashboard(request):
    
    try :
        seller_id = request.user.seller.id
    except :
        return HttpResponseRedirect(reverse("login"))
    if request.method == "POST":
        product = Product(seller = seller_id  , name = requses.POST["name"] , price = request.POST["price"] ,stock= request.POST["stock"] ,image = request.POST["image"] ,category =request.POST["category"])
        product.save() 
    else :
        products = Product.objects.filter(seller = seller_id)
        return render(request ,'Marketplace/dashboard.html',{ 
            'products' :products 
    })




def addtocart (request ,id ):
    request.session["orders"] += [{"product_id " : id ,"quntity" :request.POST["quantity"]}]
    return HttpResponseRedirect(reverse("index"))



def cart (request):
    if request.method =="POST":
        if not request.user.is_authenticated :
            return HttpResponseRedirect(reverse("login"))
        cart = Checkout(customer=request.user.id , Payment_Method=request.POST["Payment_Method"])
        cart.save() 
        for orders in  request.session["orders"]:
            product_id=orders["product_id"]
            quntity =orders["quntity"]
            Order(product=product_id ,quantity=quantity ,checkout=cart.id).save()
    else:
        user_cart=[]
        for orders in  request.session["orders"]:
            product_id=orders["product_id"]
            quntity =orders["quntity"]
            user_cart.append([Product.objects.get(id=product_id) ,quntity])
        return render(request ,'Marketplace/cart.html',{
            'cart' :user_cart})


def addreview(request ,id):
    if not request.user.is_authenticated :
        return HttpResponseRedirect(reverse("login"))
    Review(user =request.user.id , review=request.POST["review"] , product=id )
        


    
