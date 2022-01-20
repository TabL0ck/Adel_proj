from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import CharField
from django.contrib import messages
from django.http import HttpRequest
from .models import Reviews, EmailAddr, ProfileUser
from .forms import ReviewsForm, EmailReg, EmailReg_csrf, ProfileUser_reg, ProfileUser_login
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required
from .module.email_bot import registration_email
from django.core.serializers.json import DjangoJSONEncoder
import json

# Обработчик перехода на index.html
def index(request):

    # Массив(пока что просто строка) ошибок
    error = ''

    print(request.META.get('REMOTE_ADDR'))

    # Отслеживание передачи данных методом POST
    if request.method == 'GET':
        # Создание объекта формы с переданными в нее значениями
        form = EmailReg(request.GET)
        # Проверка на валидность данных в форме
        if form.is_valid():
            # Отправка ссыкли с регистрацией
            registration_email(form.cleaned_data['email'], csrfmiddlewaretoken=request.GET['csrfmiddlewaretoken'])
            return redirect('index')
        else:
            # Вывод в консоль ошибки и добавлние ошибки в массив ошибок, да, да пока что это просто строка, поебать
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
        'form' : form,
        'auth' : request.user.is_authenticated,
        'user_pk' : request.user.pk
    }
    # Рендеринг страницы index.html
    return render(request, 'perepis/index.html',content)

# Обработчик перехода на write_review.html
def write_review(request):
    if not request.user.is_authenticated:
        return redirect('login')
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
            user_prof = ProfileUser.objects.get(username=request.user.username)
            temp = Reviews.objects.create(text=form.cleaned_data['text'], user=user_prof)
            temp.save()
            return redirect('index')
        else:
            # Вывод в консоль ошибки и добавлние ошибки в массив ошибок, да, да пока что это просто строка, поебать
            error = 'Неверно заполнена форма'
    # Создание объекта формы, которая передасться в write_review.html
    form = ReviewsForm()
    # Словарь данных, которые передаються в write_review.html
    content = {
        'title' : 'Отзыв', 
        'form' : form,
        'error' : error,
        'auth' : request.user.is_authenticated,
        'user_pk' : request.user.pk
    }
    # Рендеринг страницы write_review.html
    return render(request, 'perepis/write_review.html', content)


def email_verif(request):

        if request.user.is_authenticated:
            redirect('index')
        if request.method == 'POST':
            form = ProfileUser_reg(request.POST, request.FILES)
            # Проверка на валидность данных в форме
            if form.is_valid():
                # Сохранение формы в базе данных и редирект на index.html
                form.save()
                return redirect('index')
            else:
                # Вывод в консоль ошибки и добавлние ошибки в массив ошибок, да, да пока что это просто строка, поебать
                error = 'Неверно заполнена форма'


        email = request.GET["email"]
        form = ProfileUser_reg(initial={
            'email' : email
            })
        form = ProfileUser_reg()

        # Словарь данных, которые передаються в email.verif.html
        content = {
            'title': 'Регистрация',
            'form': form
        }
        return render(request, 'perepis/email_verif.html', content)

def log_in(request):

    if request.user.is_authenticated:
        redirect('index')

    form = ProfileUser_login()
    context = {
        'title': 'Login',
        'form': form
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(f'{request.user.pk}/lk')
        else:
            messages.error(request, 'Username or password is incorrect')
    #auth_menu_bar(request, context)
    return render(request, 'perepis/login.html', context)

def log_out(request):
    if not request.user.is_authenticated:
        return redirect('login')

    logout(request)
    return redirect('index')

class lk(DetailView):

    model= ProfileUser
    template_name = 'perepis/lk.html'
    context_object_name = 'profile'

class charts(DetailView):

    context_charts = {}

    model = ProfileUser
    template_name = 'perepis/charts.html'
    
    def get_context_data(self, **kwargs):
        profiles = ProfileUser.objects.all()
        edu_count = 0
        child_count = 0
        married_count = 0
        educations_degrees = 0
        male_count = 0
        female_count = 0
        for item in profiles:
            if item.education != 'Нет':
                edu_count += 1
            if item.child > 0:
                child_count += 1
            if item.in_relationship:
                married_count += 1
            if item.educations_degrees != 'Нет':
                educations_degrees += 1
            if item.sex == 'Муж':
                male_count += 1
            elif item.sex == 'Жен':
                female_count += 1

        context_charts = {
            'edu_count': edu_count,
            'child_count': child_count,
            'married_count': married_count,
            'educations_degrees': educations_degrees,
            'male_count': male_count,
            'female_count': female_count,
            'city': ProfileUser.objects.get(pk=self.request.user.id).city,
            'profile': ProfileUser.objects.get(pk=self.request.user.id)
        }
        return context_charts

class badge(DetailView):

    model = ProfileUser
    template_name = 'perepis/badge.html'
    context_object_name = 'profile'

class tree_view(DetailView):

    model = ProfileUser
    template_name = 'perepis/tree_view.html'
    context_object_name = 'profile'

def handle_404(request, exception):
    return render(request, 'perepis/404.html')

def handle_500(exception):
    return render(request, 'perepis/500.html')


def auth_menu_bar(request, context):
    if not request.user.is_authenticated:  # Проверка на авторизацию
        return context
    else:
        user = ProfileUser(username=request.user)
        context['profile'] = user
    return context
