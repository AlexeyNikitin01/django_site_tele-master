from django.db import models

from django.contrib.auth.models import User

from main.models import TVSale


class Comment(models.Model):
    com_to_model = models.ForeignKey(TVSale, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commenter')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} comment: {self.comment}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'
        ordering = ['-created_date']
