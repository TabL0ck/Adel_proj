from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reviews
from .forms import ReviewsForm, EmailReg


def index(request):

    error = ''

    if request.method == 'POST':
        form = EmailReg(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
            error = 'Неверно заполнена форма'

    form = EmailReg()

    reviews = Reviews.objects.all().order_by('-id')
    content = {
        'title' : 'Перепись населения',
        'reviews' : reviews,
        'form' : form
    }

    return render(request, 'perepis/index.html',content)


def write_review(request):

    error = ''

    if request.method == 'POST':
        form = ReviewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.errors)
            error = 'Неверно заполнена форма'


    form = ReviewsForm()

    content = {
        'title' : 'Отзыв', 
        'form' : form,
        'error' : error
    }

    return render(request, 'perepis/write_review.html', content)


def email_verif(request):

    content = {
        'title': 'Регистрация',
    }

    return render(request, 'perepis/email_verif.html', content)
