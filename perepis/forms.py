from .models import Reviews, EmailAddr
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea, EmailInput


class ReviewsForm(ModelForm):

    class Meta:

        model = Reviews
        fields = ['username', 'role', 'text', 'avatar']

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


class EmailReg(ModelForm):

    class Meta:
        model = EmailAddr
        fields = ['email']

        widgets = {
            'email' : EmailInput(attrs={
                'placeholder' : 'Напишите ваш E-mail'
            })
        }