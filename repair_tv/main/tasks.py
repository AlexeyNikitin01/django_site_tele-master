from django.core.mail import send_mail

from .models import RepairOrder


def repair_order_send_mail(order_pk):
    repair_order = RepairOrder.objects.get(pk=order_pk)
    subject = f'Заказ на ремонт {repair_order.pk}'
    message = f'Заказчик \n Имя: {repair_order.name} \n Фамилия: {repair_order.surname}' \
              f'\n Телефон: {repair_order.phone},' \
              f'\n Описание проблемы: {repair_order.description}.'
    mail_sent = send_mail(subject,
                          message,
                          'lyosha-2001@mail.ru',
                          ['lyosha-2001@mail.ru'])
    return mail_sent
