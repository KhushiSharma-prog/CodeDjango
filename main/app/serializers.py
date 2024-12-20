from rest_framework import serializers
from .models import ProductCategory
from django.contrib.auth.models import User


class ProductCategorySerializer(serializers.ModelSerializer):
     class Meta:
        model = ProductCategory
        image = serializers.ImageField()  # image field for API
        fields = ['title', 'category', 'subcategory' , 'childcategory' , 'price' , 'quantity' , 'image' , 'description']
  # Adjust the fields you want to expose


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords must match"})
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
