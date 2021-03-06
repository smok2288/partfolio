from django.urls import path, re_path
from .views import product_list, product_detail
app_name = 'market'

urlpatterns = [
    path(r'^$', product_list, name='product_list'),
    re_path(r'^(?P<category_slug>[-\w]+)', product_list, name='product_list_by_category'),
    path(r'^(?P<id>\d+)/(?P<slug>[-w]+)/$', product_detail, name='product_detail'),
]