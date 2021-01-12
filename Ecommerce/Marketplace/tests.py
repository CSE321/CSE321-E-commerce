from django.test import TestCase
from .models import *

class MarketplaceTestCase(TestCase):
    def setUp(self):
        u1= User.objects.create(username="Karim",password="123456789")
        c1= Customer.objects.create(user=u1)
        u2 = User.objects.create(username="Abdelrhman", password="1234567")
        c2 = Customer.objects.create(user=u2)
    def test_Password_Validity(self):
        u1=User.objects.get(username="Karim")
        c=Customer.objects.get(user=u1)
        self.assertEqual(c.password_validate(),True)

