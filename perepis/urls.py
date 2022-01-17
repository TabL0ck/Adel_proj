from django.urls import path
from . import views

# Список страниц, по которым можно переходить
urlpatterns = [
    path('', views.index, name="index"),
    path('write_review', views.write_review, name="write_review"),
    path(r'^email_verif/$', views.email_verif, name="email_verif"),
    path('login', views.log_in, name="login"),
    path('logout', views.log_out, name="logout"),
    path('lk', views.lk, name="lk")
]
