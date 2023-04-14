from django.urls import path,include
from . import views
app_name='accounts'
urlpatterns = [
    path('', views.login,name='login'),
    path('signup/', views.signup,name='signup'),
    path('update/', views.update,name='update'),
    path('logout/', views.logout,name='logout'),
    path('delete/', views.delete,name='delete'),
]
