from django.urls import path
from . import views 
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    path('' ,views.index ,name="index" ),
    path('login' ,views.login ,name="login"),
    path('register' ,views.register ,name="register"),
    path('product/<int:id>',views.product ,name="product"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('addtocart/<int:id>', views.addtocart, name="addtocart"),
    path('logout',views.logout,name="logout"),
    path('cart',views.cart,name="cart")


]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)