from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView

from .forms import RegisterUserForm

from django.core.signing import BadSignature

from .utilities import send_activation_notification, signer


# from blog.admin import PostAdmin


def first(request):
    request.session['first'] = 'Johan'
    print(request.session.get('first'))
    return render(request, 'first_page.html')


class User_Login_View(LoginView):
    tamplate_name = 'auth/login_form.html'


def profile(request):
    return render(request, 'auth/user_profile.html')


class RegisterUserView(FormView):
    model = User
    template_name = 'auth/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main:register_done')


class RegisterDontView(TemplateView):
    template_name = 'auth/register_done.html'


def ser_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'Bad_signature.html')
    user = get_object_or_404(User, username=username)

    if user.is_activated:
        template = 'maim/user_activated.html'
    else:
        template = 'main/user_activated_done.html'
        user.is_activated = True
        user.is_active = True
        user.save()

    return render(request, template)


def forms1(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'forms2.html')


def forms2(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'forms2.html')
