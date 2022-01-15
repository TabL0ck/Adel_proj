from django.db import models


class Reviews(models.Model):

    username = models.CharField('Имя пользователя', max_length=32)
    role = models.CharField('Роль пользователя', max_length=64)
    text = models.TextField('Текст отзыва')

    def __str__(self):

        return self.username

    class Meta:

        verbose_name = 'Review'
        verbose_name_plural = 'Rewiews'