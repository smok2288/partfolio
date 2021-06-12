from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import first, User_Login_View, profile, RegisterUserView, RegisterDontView
app_name = 'main'

urlpatterns = [
    path('', first, name='first'),
    path('accounts/login/', User_Login_View.as_view(template_name='auth/login_form.html'), name='login'),
    path('accounts/profile', profile, name='profile'),
    path('accounts/logout/', LogoutView.as_view(next_page='main:first'), name='logout'),
    path('account/register_done',RegisterDontView.as_view(), name = 'register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name= 'register'),
]

