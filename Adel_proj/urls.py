from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Ну вот подключение приложений сайта
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('perepis.urls')),
]
# Подключение статических файлов
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Подключение медиа файлов
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
