from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User
from .serializers import CustomRegisterSerializer,CustomLoginSerializer,UserSerializer,CustomUserDetailsSerializer,UpdateProfileSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth.views import LoginView
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from dj_rest_auth.views import LoginView, UserDetailsView
from rest_framework import serializers

# Create your views here.
# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             # 회원가입 후 자동으로 로그인 처리
#             auth_login(request, user)
#             # 토큰 생성
#             token, _ = Token.objects.get_or_create(user=user)
#             print(token)
#             return redirect('boards:index')
#     else:
#         form = CustomUserCreationForm()
#     context ={
#         'form':form,
#     }
#     return render(request,'accounts/signup.html',context)

# 

class CustomRegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomRegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(request=request)
            auth_login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'message': '회원가입 완료', 'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomLoginView(LoginView):
    serializer_class = CustomLoginSerializer


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

# def login(request):
#     if request.method == "POST":
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             auth_login(request, form.get_user())
#             return redirect('boards:index')
#     else:
#         form = AuthenticationForm()
#     context = {
#         'form':form,
#     }
#     return render(request, 'accounts/login.html', context)


# def logout(request):
#     auth_logout(request)
#     return redirect('boards:index')

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def user_info(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


# class CustomUserDetailsView(UserDetailsView):
#     serializer_class = CustomUserDetailsSerializer
    
#     def update(self, request, *args, **kwargs):
#         partial = kwargs.pop('partial', False)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)
#         return Response(serializer.data)

#     def perform_update(self, serializer):
#         serializer.save()

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        serializer = UpdateProfileSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            print(f"Updated data: {user.username}, {user.email}, {user.nickname}, {user.age}, {user.money}, {user.salary}, {user.financial_products}")  # 디버깅용
            serializer.save()
            return Response({'message': '프로필이 업데이트되었습니다.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class UpdateProfileView(APIView):
#     permission_classes = [IsAuthenticated]

#     def patch(self, request):
#         user = request.user
#         # 클라이언트에서 전송된 데이터로 사용자 정보 업데이트
#         user.username = request.data.get('username', user.username)
#         user.email = request.data.get('email', user.email)
#         user.nickname=request.data.get('nickname', user.nickname)
#         user.age = request.data.get('age', user.age)
#         user.money = request.data.get('money', user.money)
#         user.salary = request.data.get('salary',user.salary)
#         user.financial_products = request.data.get('financial_products',user.financial_products)


#         user.save()
#         return Response({'message': '프로필이 업데이트되었습니다.'}, status=status.HTTP_200_OK)


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