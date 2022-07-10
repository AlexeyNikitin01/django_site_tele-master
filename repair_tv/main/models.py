from django.db import models
from django.urls import reverse


class RepairOrder(models.Model):
    name = models.CharField(max_length=10, verbose_name='Ваше имя')
    surname = models.CharField(max_length=10, blank=True, verbose_name='Ваша фамилия')
    phone = models.CharField(max_length=20, verbose_name='Ваш телефон')
    description = models.TextField(max_length=200, blank=True, verbose_name='Опишите проблему')
    date_order = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-date_order']


class TVSale(models.Model):
    model_tv = models.CharField(max_length=20)
    image_tv = models.ImageField()
    price_tv = models.FloatField()
    description_tv = models.TextField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    slug_tv = models.SlugField()

    def __str__(self):
        return f'{self.model_tv}'

    def get_absolute_url(self, pk):
        return reverse('sale_tv', kwargs={'pk': pk,
                                          'slug': self.slug_tv,
                                          })

    class Meta:
        verbose_name = "Телевизор на продажу"
        verbose_name_plural = "Телевизоры на продажу"
        ordering = ["-date_add", "model_tv"]
