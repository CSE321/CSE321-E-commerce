from django.db import models
from  django.contrib.auth.models import User 
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE ,null=True )
    email = models.CharField(max_length=200 ,null=True)
    address = models.CharField(max_length=200 ,null=True )
    credit_card_number =models.IntegerField()
    def __str__ (self):
        return self.user 

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE ,null=True )
    email = models.CharField(max_length=200 ,null=True)
    address = models.CharField(max_length=200 ,null=True )
    credit_card_number =models.IntegerField()   
    def __str__ (self):
        return self.user

class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    quantity=models.IntegerField(default=0,blank=True,null=True)
    date=models.DateTimeField(auto_now_add=True)
    checkout=models.ForeignKey(Checkout,on_delete=models.SET_NULL,blank=True,null=True)
    def __str__ (self):
        return self.checkout.id