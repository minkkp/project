from django.urls import path,include
from . import views
app_name='main'

urlpatterns = [
    path('', views.main,name='main'),
    path('result', views.result,name='result'),
]
