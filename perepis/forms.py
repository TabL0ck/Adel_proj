from .models import Reviews
from django.forms import ModelForm, TextInput, Textarea


class ReviewsForm(ModelForm):

    class Meta:

        model = Reviews
        fields = ['username', 'role', 'text']

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