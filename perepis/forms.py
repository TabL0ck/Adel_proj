from .models import Reviews, EmailAddr, ProfileUser
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, TextInput, Textarea, EmailInput, PasswordInput, CharField, CheckboxInput, BooleanField

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

    password1 = CharField(
        label=("Пароль"),
        widget=PasswordInput(attrs={
            'type' : 'password',
            'class' : 'form-control',
            'id' : 'floatingPassword',
            'placeholder' : 'Password',
            'name' : 'password1'
        }),
    )
    password2 = CharField(
        label=("Подтвердите пароль"),
        widget=PasswordInput(attrs={
            'type' : 'password',
            'class' : 'form-control',
            'id' : 'floatingPassword',
            'placeholder' : 'Password confirmation',
            'name' : 'password2'
        }),
        help_text=("Введите пароль повторно, для подтверждения.")
    )
    check_box = BooleanField(
        label=(""),
        widget=CheckboxInput(attrs={
            'type' : 'checkbox',
            'class' : 'form-check-input',
            'id' : 'exampleCheck1',
            'name' : 'checkbox'
        }),
    )
    class Meta:

        model = ProfileUser
        fields = ['email', 'username', 'password1', 'password2']

        widgets = {
          'username' : TextInput(attrs={
              'type' : 'text',
              'class' : 'form-control',
              'id' : 'floatingInput',
              'placeholder' : 'Login'
          }),
          'email' : EmailInput(attrs={
              'type' : 'email',
              'class' : 'form-control',
              'id' : 'floatingInput1',
              'placeholder' : 'name@example.com'
          })
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit and self.cleaned_data.get("check_box"):
            user.save()
        return user

class EmailReg_csrf(ModelForm):

    class Meta:
        model = EmailAddr
        fields = ['csrfmiddlewaretoken']

class ProfileUser_login(ModelForm):  

    class Meta:
        model = ProfileUser
        fields = ['username','password']

        widgets = {
            'username' : TextInput(attrs={
                'type' : 'text',
                'class' : 'form-control',
                'id' : 'floatingInput',
                'placeholder' : 'Login'
            }),
            'password' : PasswordInput(attrs={
                'type' : 'password',
                'class' : 'form-control',
                'id' : 'floatingPassword',
                'placeholder' : 'Password'
            })       
        }