from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('main/',include('main.urls')),
    path('board/',include('board.urls')),
    path('output/',include('output.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
# MEDIA_URL로 들어오는 요청에 대해 MEDIA_ROOT 경로를 탐색
