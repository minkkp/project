from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_http_methods
from .models import User
from .forms import CustomUserChangeForm

# 로그인
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('main/')
        else:
            return render(request,'accounts/login.html')
    else:
        return render(request,'accounts/login.html')


# 회원가입
@require_http_methods(['GET','POST'])
def signup(request):
    if request.method =='POST':
        if request.POST['password_1'] == request.POST['password_2']:
            user = User.objects.create_user(
                user_id = request.POST['user_id'],
                password=request.POST['password_1'],
                user_area=request.POST['user_area'],
                user_living = request.POST['user_living'],)  
            auth.login(request,user)
            return redirect('main:main')
        return render(request,'accounts/signup.html')
    else:
        return render(request,'accounts/signup.html')

# 회원정보 수정
@require_http_methods(['GET','POST'])
def update(request):
    form = CustomUserChangeForm(instance=request.user)
    context = {
    	'form':form,
    } 
    return render(request, 'accounts/update.html', context)

# 로그아웃
def logout(request):
    pass