from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path(r'^(?P<year>\d{4})/(?P<month>\d{3})/(?P<day>\d{2})/(?P<post>\[-\w])/$', views.post_detail, name='post_detail'),
]