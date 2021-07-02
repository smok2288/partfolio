import celery
from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = 'Заказ № {}'.format(order_id)
    message = 'Дорогой {},\n\nВы успешно разместили заказ.\Ваш заказ {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message, 'smok_2@mail.ru', [order.email])
    return mail_sent