from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from . models import User
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='이메일')
    nickname = forms.CharField(label='닉네임')
    age = forms.IntegerField(label='나이')
    money = forms.IntegerField(label='자산')
    class Meta(UserCreationForm.Meta):
        # 현재 django 프로젝트에 활성화된 User 객체를 반환하는 함수
        model = get_user_model()
        fields = ('username', 'nickname', 'email', 'age', 'money', 'salary')
class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'nickname', 'email', 'age', 'money', 'salary')