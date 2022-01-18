from .models import Reviews, EmailAddr, ProfileUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, Textarea, EmailInput

# Форма отзывов 
class ReviewsForm(ModelForm):

    class Meta:

        # Создание объекта модели
        model = Reviews
        # Поля, которые будут в форме
        fields = ['text']
        # Украшение для полей формы
        widgets = {
                'text' : Textarea(attrs={
                'class' : 'form-control',
                'placeholder' : 'Текст отзыва',
                'name' : 'text'
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
                'placeholder' : 'Напишите ваш E-mail',
                'name' : 'email'
            })
        }

class ProfileUser_reg(UserCreationForm):

    class Meta:

        model = ProfileUser()
        fields = ['email', 'username', 'role', 'age', 'city', 'avatar', 'first_name']

class ProfileUser_login(UserCreationForm):  

    class Meta:
        model = ProfileUser
        fields = ['username']