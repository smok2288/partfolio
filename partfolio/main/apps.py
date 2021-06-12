from django.apps import AppConfig
from django.dispatch import Signal

from .utilities import send_activation_notification


class MainConfig(AppConfig):
    name = 'main'


user_registered = Signal(providing_args=['instance'])   # погуглить как обьявляется сигнал


def user_registered_dispatch(sender, **kwargs):
    send_activation_notification(kwargs['instance'])


user_registered.connect(user_registered_dispatch)