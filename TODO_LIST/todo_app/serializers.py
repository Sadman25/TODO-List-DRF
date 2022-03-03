from django.contrib.auth.models import User
from rest_framework import serializers
from .models import todoList
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password",)
        extra_kwargs = {"password": {"write_only": True}}

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ('id', 'username', 'email', 'password')
        extra_kwargs = {"password": {"write_only": True}}

class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = todoList
        fields = '__all__'