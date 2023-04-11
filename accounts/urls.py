from django.urls import path,include
from . import views
app_name='accounts'
urlpatterns = [
    path('', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
]
