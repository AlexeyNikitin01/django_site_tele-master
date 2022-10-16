from django.db import models
from django.contrib.auth.models import User

from main.models import TVSale


class Order(models.Model):
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=15)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email = models.EmailField()
    paid = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    postal_code = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Регистрация Заказа'
        verbose_name_plural = 'Регистрация заказов'
        ordering = ['-date_created']

    def __str__(self):
        return f'{self.pk}'

    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    product = models.ForeignKey(TVSale, related_name='order_items', on_delete=models.PROTECT)
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT)
    user_order = models.ForeignKey(User, related_name='user_order', on_delete=models.PROTECT, blank=True,
                                   null=True)
    price_tv = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    model_tv = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.pk}'

    def get_cost(self):
        return self.price_tv * self.quantity
