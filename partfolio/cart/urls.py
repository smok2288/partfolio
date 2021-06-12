from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart', views.cart_detail, name='cart'),
    path(r'add/(?P<product_id>\d+)/$',  views.add_cart, name='add_cart'),
    path(r'remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
]