from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth import authenticate
from django.views.decorators.http import require_http_methods,require_POST
from django.contrib.auth.hashers import check_password

from .models import User
from .forms import CustomUserChangeForm

area_list = ['서울시','부산시','고양시']
living_list = ['단독','공동']

# 로그인
@require_http_methods(['GET','POST'])
def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('main/')
        else:
            messages.error(request,'아이디와 비밀번호를 확인해주세요')
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
        messages.error(request,'비밀번호를 확인해주세요')
        return render(request,'accounts/signup.html')
    else:
        return render(request,'accounts/signup.html')
    
# 회원정보 수정
@require_http_methods(['GET','POST'])
def update(request):
    if request.method == 'POST':
        ## 일반정보 update
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()     

        ## 패스워드 update
        origin_password = request.POST["origin_password"]
        new_password = request.POST["new_password"]
        confirm_password = request.POST["confirm_password"]

        user = request.user

        if origin_password+new_password+confirm_password!="":
            if origin_password == "" or new_password=="" or confirm_password=="":
                messages.error(request,'비밀번호를 변경하려면 모든 빈칸을 작성해주세요')
            else:
                if check_password(origin_password, user.password)==False:
                    messages.error(request,'현재 비밀번호가 틀립니다')
                elif new_password!=confirm_password:
                    messages.error(request,'새 비밀번호를 확인 해주세요')
                elif origin_password==new_password:
                    messages.error(request,'현재 비밀번호와 변경 비밀번호가 동일합니다')
                else:
                    user.set_password(new_password)
                    user.save()
                    auth.login(request,user)
                    messages.success(request,'비밀번호가 변경되었습니다')
                    return redirect('main:main')
        else:
            return redirect('main:main')
    
    ## 화면 최초로 불러올시 Form 띄어주기
    form = CustomUserChangeForm(instance=request.user)

    context = {
        'form':form,
        'area_list': area_list,
        'living_list': living_list,
        'user':request.user,
    } 
    return render(request, 'accounts/update.html', context)

# 로그아웃
@require_POST
def logout(request):
    auth.logout(request)
    return render(request,'accounts/login.html')

# 회원탈퇴
@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth.logout(request) # session 지우기. 단 탈퇴후 로그아웃순으로 처리. 먼저 로그아웃하면 해당 request 객체 정보가 없어져서 삭제가 안됨.
    messages.success(request,"회원탈퇴가 완료되었습니다")
    return redirect('accounts:login')
