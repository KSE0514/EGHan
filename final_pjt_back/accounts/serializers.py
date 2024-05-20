from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User
from dj_rest_auth.serializers import LoginSerializer
from django.contrib.auth import get_user_model

class CustomLoginSerializer(LoginSerializer):
    email = None

class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    financial_products = serializers.CharField(required=False,allow_null=True)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['nickname'] = self.validated_data.get('nickname','')
        data['age'] = self.validated_data.get('age', '')
        data['money'] = self.validated_data.get('money', '')
        data['salary'] = self.validated_data.get('salary', '')
        data['financial_products'] = self.validated_data.get('financial_products', '')
        return data

    def save(self, request):
        user = super().save(request)
        user.nickname = self.cleaned_data.get('nickname')
        user.age = self.cleaned_data.get('age')
        user.money = self.cleaned_data.get('money')
        user.salary = self.cleaned_data.get('salary')
        user.financial_products = self.cleaned_data.get('financial_products')
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['pk','username', 'email','nickname','age', 'money','salary', 'financial_products','password']