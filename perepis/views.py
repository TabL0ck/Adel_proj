from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reviews
from .forms import ReviewsForm


def index(request):

    reviews = Reviews.objects.all().order_by('-id')
    content = {
        'title' : 'Перепись населения',
        'reviews' : reviews,
    }

    return render(request, 'perepis/index.html',content)


def write_review(request):

    error = ''

    if request.method == 'POST':
        form = ReviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
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
        'title': 'da',
    }

    return render(request, 'perepis/email_verif.html', content)
