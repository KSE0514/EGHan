from rest_framework import serializers
from .models import DepositOptions, DepositProducts, SavingOptions, SavingProducts
from accounts.models import User

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'
        read_only_fields = ('user',)

class DepositOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only_fields = ('product',)


class SavingProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingProducts
        fields = '__all__'
        read_only_fields = ('user',)

class SavingOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingOptions
        fields = '__all__'
        read_only_fields = ('product',)


class UserSerializer(serializers.ModelSerializer):
    product_user = DepositProductsSerializer(many=True, read_only=True)
    savingproduct_user = SavingProductsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'product_user', 'savingproduct_user','nickname','age','salary','money','financial_products']