from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path(r'create/', views.order_create, name='order_create'),
    path(r'^admin/order/(?P<order_id>\d+)/$', views.admin_order_detail, name='admin_order_detail'),
]