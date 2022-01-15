from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('write_review', views.write_review, name="write_review"),
    path('email_verif', views.email_verif, name="email_verif"),
]
