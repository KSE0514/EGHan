from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원가입 후 자동으로 로그인 처리
            auth_login(request, user)
            # 토큰 생성
            token, _ = Token.objects.get_or_create(user=user)
            print(token)
            return redirect('boards:index')
    else:
        form = CustomUserCreationForm()
    context ={
        'form':form,
    }
    return render(request,'accounts/signup.html',context)


def update(request):
    if request.method == "POST":
        user_form = CustomUserChangeForm(request.POST, instance = request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('boards:index')
    else:
        user_form = CustomUserChangeForm(instance = request.user)
    context = {
        'user_form':user_form,
    }
    return render(request, 'accounts/update.html', context)

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('boards:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('boards:index')



def change_password(request, user_pk):
    if request.method == "POST":
        password_form = PasswordChangeForm(request.user, request.POST)
        if password_form.is_valid():
            password_form.save()
            return redirect('boards:index')
    else:
        password_form = PasswordChangeForm(request.user)
    context = {
        'password_form':password_form,
    }
    return render(request, 'accounts/change_password.html', context)