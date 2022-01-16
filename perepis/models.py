from django.db import models
from django.contrib.auth.models import User

from .module.img_crop import crop_img_to_review
from .module.email_bot import registration_email

# Функция возвращающая полный путь к файлу с аватаркой
def user_directory_path(instance,filename):
    return 'perepis/userprofile_avatars/{0}/{1}]'.format(instance.id,filename)

# Модель отзывов
class Reviews(models.Model):

    # Ник юзера, который оставил отзыв
    username = models.CharField('Имя пользователя', max_length=32)
    # Роль юзера, который оставил отзыв
    role = models.CharField('Роль пользователя', max_length=64)
    # Текст отзыва
    text = models.TextField('Текст отзыва')
    # Аватарка юзера, который оставил отзыв
    avatar = models.ImageField(default='perepis/no_avatar.png',upload_to=user_directory_path)

    # Вот именно так будет выводиться объект модели, при обращении к ней
    def __str__(self):

        return self.username

    # Запись данных в базу данных, реализуется в основном здесь
    def save(self):

        # Сохранение данных в бд
        super().save()
        # Обрезание пикчи 
        crop_img_to_review(self.avatar.path)

    # Отображение в панели админа
    class Meta:
        # Единственное число
        verbose_name = 'Review'
        # Множественное число
        verbose_name_plural = 'Rewiews'

# Модель Email адрессов
class EmailAddr(models.Model):

    # Email, на который придет письмо
    email = models.EmailField('E-mail адресс')

    # Вот именно так будет выводиться объект модели, при обращении к ней
    def __str__(self):

        return self.email

    # Запись данных в базу данных, реализуется в основном здесь
    def save(self):

        # Сохранение данных в бд
        super().save()
        # Отправка письма с ссылкой на регистрацию
        registration_email(self.email)


    # Отображение в панели админа
    class Meta:
        # Единственное число
        verbose_name = 'Email'
        # Множественное число
        verbose_name_plural = 'Emails'
