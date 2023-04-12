from django.urls import path,include
from . import views

app_name='board'
urlpatterns = [
    path('index/', views.index,name='index'),
    path('post/', views.post,name='post'),
    path('detail/<int:pk>', views.detail,name='detail'),
    path('comment/<int:pk>', views.comment,name='comment'),
    path('update/', views.update,name='update'),
]
