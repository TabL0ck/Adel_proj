from django.db import models
from django.contrib.auth.models import User

from .module.img_crop import crop_img_to_review
from .module.email_bot import registration_email
from .module.choices import *


# Функция возвращающая полный путь к файлу с аватаркой
def user_directory_path(instance,filename):
    return 'perepis/userprofile_avatars/{0}/{1}]'.format(instance.id,filename)


# Модель Email адрессов
class EmailAddr(models.Model):

    # Email, на который придет письмо
    email = models.EmailField('E-mail')
    csrfmiddlewaretoken = models.CharField('CSRF токен', max_length=250, default='a')

    # Вот именно так будет выводиться объект модели, при обращении к ней
    def __str__(self):

        return self.email

    # Запись данных в базу данных, реализуется в основном здесь
    def save(self):

        # Сохранение данных в бд
        super().save()
        # Отправка письма с ссылкой на регистрацию
        registration_email(self.email, self.csrfmiddlewaretoken)


    # Отображение в панели админа
    class Meta:
        # Единственное число
        verbose_name = 'Email'
        # Множественное число
        verbose_name_plural = 'Emails'


class ProfileUser(User):

    avatar = models.ImageField('Аватарка', default='perepis/no_avatar.png',upload_to=user_directory_path)
    role = models.CharField('Образование', max_length=64 , default='Студент')
    education = models.CharField(default='Нет', max_length=64)
    age = models.PositiveIntegerField('Возраст', default=16)
    city = models.CharField(default='Севастополь', max_length=100)
    hometown = models.CharField(default='Севастополь', max_length=100)
    university = models.CharField(default='Севастопольский Государственный Университет', max_length=100)
    phone_number = models.CharField(default='+7(999)000111', max_length=100)
    child = models.PositiveSmallIntegerField(default=0)
    in_relationship = models.BooleanField(default=False)
    educations_degrees = models.CharField(default='Нет', max_length=100)
    sex = models.CharField(default='Муж', max_length=5)

    # Запись данных в базу данных, реализуется в основном здесь
    def save(self):

        # Сохранение данных в бд
        super().save()
        # Обрезание пикчи 
        crop_img_to_review(self.avatar.path)

# Модель отзывов
class Reviews(models.Model):

    # Текст отзыва
    text = models.TextField('Текст отзыва')
    # Аватарка юзера, который оставил отзыв
    user = models.ForeignKey(ProfileUser, on_delete=models.CASCADE)

    # Вот именно так будет выводиться объект модели, при обращении к ней
    def __str__(self):

        return self.text

    # Отображение в панели админа
    class Meta:
        # Единственное число
        verbose_name = 'Review'
        # Множественное число
        verbose_name_plural = 'Rewiews'

class Badge(models.Model):

    email = models.EmailField('E-mail')
    first_name = models.CharField('Имя', max_length=64)
    last_name = models.CharField('Фамилия', max_length=64)
    sex = models.CharField('Пол', choices=Sex_CHOICES, max_length=8, default='male')
    klass_11 = models.BooleanField('Среднее общее образование', default=False)
    PTU = models.BooleanField('Среднее профессиональное обраование', default=False)
    VUZ = models.BooleanField('Высшее профессиональное образование', default=False)
    married = models.CharField('Семейное положение', choices=Married_CHOICES, default="no_married", max_length=64)
    candidate_of_science = models.BooleanField('Кандидат наук', default=False)
    doctor_of_science = models.BooleanField('Доктор наук', default=False)
    child = models.CharField('Дети', choices=Child_CHOICES, default='no', max_length=64)
    region = models.CharField('Регион', choices=Region_CHOICES, default='84', max_length=64)
