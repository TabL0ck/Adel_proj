from django.contrib import admin
from .models import Reviews, EmailAddr, ProfileUser

# Добавление моделей в админку
admin.site.register(Reviews)
admin.site.register(EmailAddr)
admin.site.register(ProfileUser)
