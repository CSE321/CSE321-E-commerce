from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    credit_card_number = models.IntegerField()

    def __str__(self):
        return self.user.username 


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    credit_card_number = models.IntegerField()

    def __str__(self):
        return self.user.username 


class Checkout(models.Model):
    Payment_Method = (
        ('Cash', 'Cash'),
        ('Visa', 'Visa'),
    )
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),

    )
    Currency = (
        ('EGP', 'EGP'),
        ('$', '$'),
        ('€', '€'),
        ('£', '£'),

    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    status=models.CharField(max_length=64,null=True,choices=STATUS)
    payment_method=models.CharField(max_length=64,null=True,choices=Payment_Method)
    currency=models.CharField(max_length=5,null=True,choices= Currency)


class Product(models.Model):
    CATEGORY = (
       ('electronics', 'electronics'),
       ('cloth', 'cloth'),
       ('sport', 'sport'))
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    price = models.FloatField(null=True)
    image = models.ImageField(null=True, blank=True)
    seller = models.ForeignKey(Seller, null=True, on_delete=models.CASCADE)

    def _str_(self):
        return self.name 


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,blank=True,null=True)
    checkout = models.ForeignKey(Checkout,on_delete=models.SET_NULL,blank=True,null=True)

    def _str_(self):
        return self.checkout.id


class Review (models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    review = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def _str_(self):
        return f"{self.customer.username} review is {self.review} on product {self.product.name}"
