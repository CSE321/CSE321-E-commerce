from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
class test(TestCase):
    def setUp(self):
        ## Create Products
        p1 = Product.objects.create(name="Ball",price=100) ## Product with valid input
        p2 = Product.objects.create(name="Mobile",price=-100) ## invalid price
        p3= Product.objects.create(price=200) ## Missing name
        ##Create Users
        u1 = User.objects.create(username="Karim",password="123456789") ## valid input
        u2 = User.objects.create(username="Abdelrhman",password="1234567") ## invalid password
        u3 = User.objects.create(username="Ahmed",password="12345678") ## valid input
        u4 = User.objects.create(username="Mohamed",password="1234567") ## invalid password
        ## Create Customer
        c1=Customer.objects.create(user=u1,credit_card_number=5585)
        c2=Customer.objects.create(user=u2,credit_card_number=5525)
        ##Create Seller
        s1=Seller.objects.create(user=u3,credit_card_number=5585)
        s2=Seller.objects.create(user=u4,credit_card_number=5575)
        ## Create Checkout
        ch1=Checkout.objects.create(payment_method="Cash",customer=c1)
        ch2=Checkout.objects.create(payment_method="Paypal",customer=c2)
        ## Create Order
        o1=Order.objects.create(product=p1,quantity=2,checkout=ch1)
        o2=Order.objects.create(product=p2,quantity=0,checkout=ch2)
        o3=Order.objects.create(quantity=3,checkout=ch1)