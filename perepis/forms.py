from .models import Reviews, EmailAddr
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, EmailInput

# Форма отзывов 
class ReviewsForm(ModelForm):

    class Meta:

        # Создание объекта модели
        model = Reviews
        # Поля, которые будут в форме
        fields = ['username', 'role', 'text', 'avatar']
        # Украшение для полей формы
        widgets = {
            'username' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Имя пользователя',
            }),
            'role' : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Роль пользователя',
            }),
            'text' : Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Текст отзыва',
            })
        }

# Форма для отправки сообщения на почту с index.html
class EmailReg(ModelForm):

    class Meta:
        # Создание объекта модели
        model = EmailAddr
        # Поля, которые будут в форме
        fields = ['email']
        # Украшение для полей формы
        widgets = {
            'email' : EmailInput(attrs={
                'placeholder' : 'Напишите ваш E-mail'
            })
        }