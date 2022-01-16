from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reviews
from .forms import ReviewsForm, EmailReg

# Обработчик перехода на index.html
def index(request):

    # Массив(пока что просто строка) ошибок
    error = ''

    # Отслеживание передачи данных методом POST
    if request.method == 'POST':
        # Создание объекта формы с переданными в нее значениями
        form = EmailReg(request.POST)
        # Проверка на валидность данных в форме
        if form.is_valid():
            # Сохранение формы в базе данных и редирект на index.html
            form.save()
            return redirect('index')
        else:
            # Вывод в консоль ошибки и добавлние ошибки в массив ошибок, да, да пока что это просто строка, поебать
            print(form.errors)
            error = 'Неверно заполнена форма'

    # Создание объекта формы, которая передасться в index.html
    form = EmailReg()

    # Создание объекта хранящего все отзывы имеющиеся в базе данных, а что если прям тут сократить список до 6?
    # Ну да так наверное даже проще и эффективнее
    reviews = Reviews.objects.all().order_by('-id')
    # Словарь данных, которые передаються в index.html
    content = {
        'title' : 'Перепись населения',
        'reviews' : reviews,
        'form' : form
    }
    # Рендеринг страницы index.html
    return render(request, 'perepis/index.html',content)

# Обработчик перехода на write_review.html
def write_review(request):
    # Массив(пока что просто строка) ошибок
    error = ''
    # Отслеживание передачи данных методом POST
    if request.method == 'POST':
        # Создание объекта формы с переданными в нее значениями
        # ВАЖНО!!!, не забывай добавлять аргумент request.FILES для передачи файлов в форму
        form = ReviewsForm(request.POST, request.FILES)
        # Проверка на валидность данных в форме
        if form.is_valid():
            # Сохранение формы в базе данных и редирект на index.html
            form.save()
            return redirect('index')
        else:
            # Вывод в консоль ошибки и добавлние ошибки в массив ошибок, да, да пока что это просто строка, поебать
            print(form.errors)
            error = 'Неверно заполнена форма'

    # Создание объекта формы, которая передасться в write_review.html
    form = ReviewsForm()
    # Словарь данных, которые передаються в write_review.html
    content = {
        'title' : 'Отзыв', 
        'form' : form,
        'error' : error
    }
    # Рендеринг страницы write_review.html
    return render(request, 'perepis/write_review.html', content)


def email_verif(request):
    # Словарь данных, которые передаються в email.verif.html
    content = {
        'title': 'Регистрация',
    }
    # Рендеринг страницы email_verif.html
    return render(request, 'perepis/email_verif.html', content)
