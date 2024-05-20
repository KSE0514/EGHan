from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from .models import User
from dj_rest_auth.serializers import LoginSerializer, UserDetailsSerializer
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

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'nickname', 'age', 'money', 'salary', 'financial_products']

class CustomUserDetailsSerializer(UserDetailsSerializer):
    nickname = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    financial_products = serializers.CharField(required=False,allow_null=True)
    
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + ('nickname','age', 'money', 'salary', 'financial_products')
    
    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()

        data_dict['age'] = self.validated_data.get('age', None)
        data_dict['nickname'] = self.validated_data.get('nickname', None)
        data_dict['salary'] = self.validated_data.get('salary', None)
        data_dict['money'] = self.validated_data.get('money', None)
        data_dict['financial_products'] = self.validated_data.get('financial_products', None)
        
        return data_dict
    
    def update(self, instance, validated_data):
            
        instance = super().update(instance, validated_data)
        # instance.username = validated_data.get('username', None)
        instance.age = validated_data.get('age', None)
        instance.money = validated_data.get('mopney', None)
        instance.salary = validated_data.get('salary', None)
        instance.nickname = validated_data.get('nickname', None)
        instance.financial_products = validated_data.get('financial_products', None)
        instance.save()
        return instance
    
    def save(self):
        # self.validated_data.pop('username', None)
        user = super().save()
        user.age = self.validated_data.get('age', None)
        user.nickname = self.validated_data.get('nickname', None)
        user.money = self.validated_data.get('money', None)
        user.wealth = self.validated_data.get('wealth', None)
        user.financial_products = self.validated_data.get('financial_products', None)
        user.save()
        return user