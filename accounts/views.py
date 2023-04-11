from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
            return render(request,'accounts/login.html',{'error':'username or password is incorrect'})
    else:
        return render(request,'accounts/login.html')

# 회원가입
def signup(request):
    if request.method =='POST':
        if request.POST['password_1'] == request.POST['password_2']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password=request.POST['password_1'],
            )
            auth.login(request,user)
            return redirect('/')
        return render(request,'accounts/signup.html')
    else:
        form = UserCreationForm
        return render(request,'accounts/signup.html',{'form':form})