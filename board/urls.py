from django.urls import path,include
from . import views

app_name='board'
urlpatterns = [
    path('index/', views.index,name='index'),
    path('post/', views.post,name='post'),
    path('detail/<int:pk>', views.detail,name='detail'),
    path('comment/<int:pk>', views.comment,name='comment'),
    path('del_com/<int:pk1>/<int:pk2>', views.del_com,name='del_com'),
    path('update/<int:pk>', views.update,name='update'),
    path('delete/<int:pk>', views.delete,name='delete'),
]
