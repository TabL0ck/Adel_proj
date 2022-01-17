from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpRequest
from .models import Reviews, EmailAddr, ProfileUser
from .forms import ReviewsForm, EmailReg, ProfileUser_reg, ProfileUser_login
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

# Обработчик перехода на index.html
def index(request):

    # Массив(пока что просто строка) ошибок
    error = ''

    # Отслеживание передачи данных методом POST
    if request.method == 'GET':
        # Создание объекта формы с переданными в нее значениями
        form = EmailReg(request.GET)
        # Проверка на валидность данных в форме
        if form.is_valid():
            # Сохранение формы в базе данных и редирект на index.html
            form.save()
            CSRF_token_save = EmailAddr.objects.get(email=request.GET['email'])
            #CSRF_token_save.csrfmiddlewaretoken = request.GET['csrfmiddlewaretoken']
            #CSRF_token_save.save()
            CSRF_token_save.delete(self)
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
        'form' : form,
        'auth' : request.user.is_authenticated
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
            temp = Reviews()
            user_prof = ProfileUser(username=request.user.username)
            
            print(user_prof.city)
            temp.create_review(user_prof.username, user_prof.role, request.POST['text'], user_prof.avatar)
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
        'auth' : request.user.is_authenticated
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
                print(form.errors)
                error = 'Неверно заполнена форма'


        email = request.GET["email"]
        form = ProfileUser_reg(initial={
            'email' : email
            })

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
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username or password is incorrect')
    #auth_menu_bar(request, context)
    return render(request, 'perepis/login.html', context)

def log_out(request):
    if not request.user.is_authenticated:
        return redirect('login')

    logout(request)
    return redirect('index')

def lk(request):

    if not request.user.is_authenticated:
        return redirect('login')

    city =[]
    role =[]
    age =[]

    if request.method == 'POST':

        print(request.POST['city'], request.POST['age'], request.POST['role'])
        if request.POST['city'] != '':
            city = ProfileUser.objects.all().filter(city=request.POST['city'])
            print(city)
        if request.POST['role'] != '':
            role = ProfileUser.objects.all().filter(role=request.POST['role'])
        if request.POST['age'] != '':
            age = ProfileUser.objects.all().filter(age=request.POST['age'])

        content = {
            'title': 'Личный кабинет',
            'auth' : request.user.is_authenticated,
            'city': city,
            'role': role,
            'age': age
        }
        return render(request, 'perepis/lk.html', content)



    # Словарь данных, которые передаються в email.verif.html
    content = {
        'title': 'Личный кабинет',
        'auth' : request.user.is_authenticated,
        'city': city,
        'role': role,
        'age': age
    }
    return render(request, 'perepis/lk.html', content)


def auth_menu_bar(request, context):
    if not request.user.is_authenticated:  # Проверка на авторизацию
        return context
    else:
        user = ProfileUser(username=request.user)
        context['profile'] = user
    return context
