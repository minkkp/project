from django.urls import path
from . import views
app_name='output'

urlpatterns = [
    path('result', views.result,name='result'),
    path('map', views.map,name='map'),
]
