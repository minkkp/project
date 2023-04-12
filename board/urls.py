from django.urls import path,include
from . import views

app_name='board'
urlpatterns = [
    path('index/', views.index,name='index'),
    path('post/', views.post,name='post'),
    path('detail/', views.post,name='detail'),
    path('update/', views.post,name='update'),
]
