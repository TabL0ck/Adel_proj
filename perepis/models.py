from django.db import models
from django.contrib.auth.models import User

import smtplib
from PIL import Image
from .email_conf import EMAIL_LOGIN, EMAIL_PASSWORD


def user_directory_path(instance,filename):
    return 'perepis/userprofile_avatars/{0}/{1}]'.format(instance.id,filename)

class Reviews(models.Model):

    username = models.CharField('Имя пользователя', max_length=32)
    role = models.CharField('Роль пользователя', max_length=64)
    text = models.TextField('Текст отзыва')
    avatar = models.ImageField(default='perepis/no_avatar.png',upload_to=user_directory_path)

    def __str__(self):

        return self.username

    def save(self):
        super().save()
        img = Image.open(self.avatar.path)
        if img.height > 88 or img.width > 77:
            output_size = (100,100)
            img.thumbnail(output_size)
            new_img = img.crop(((img.width- 77) // 2,(img.height - 88) // 2,(img.width + 77) // 2,(img.height + 88) // 2))
            new_img.save(self.avatar.path, quality=95)

    class Meta:

        verbose_name = 'Review'
        verbose_name_plural = 'Rewiews'


class EmailAddr(models.Model):

    email = models.EmailField('E-mail адресс')

    def __str__(self):

        return self.email

    def save(self):

        smtpObj = smtplib.SMTP('smtp.mail.ru', 587)
        smtpObj.starttls()
        smtpObj.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        smtpObj.sendmail(EMAIL_LOGIN, self.email, "Your registration link: 127.0.0.1:8000/email_verif")
        smtpObj.quit()

    class Meta:

        verbose_name = 'Email'
        verbose_name_plural = 'Emails'
