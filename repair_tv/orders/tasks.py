from django.core.mail import send_mail

from .models import Order


def order_created_send_mail(order_pk):
    order = Order.objects.get(pk=order_pk)
    subject = 'Заказ {}'.format(order_pk)
    message = f'Привет {order.name},\n\nТы оформил заказ.\
                твой заказ {order_pk}.'
    mail_sent = send_mail(subject,
                          message,
                          'lyosha-2001@mail.ru',
                          [order.email])
    return mail_sent
