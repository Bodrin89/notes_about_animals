from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed

from apps.users.models import User


class CreateUserSerializer(serializers.ModelSerializer):
    """Сериализатор для регистрации нового пользователя"""
    password = serializers.CharField(validators=[validate_password],
                                     write_only=True, style={'input_type': 'password'})
    password_repeat = serializers.CharField(write_only=True,
                                            style={'input_type': 'password'}, required=False)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password_repeat')

    def validate(self, attrs):
        """Проверка введенного повторно пароля на валидность"""
        if not attrs.get('password_repeat', None):
            raise ValidationError('Required field')
        if attrs['password'] != attrs['password_repeat']:
            raise ValidationError('Password does not match')
        return attrs

    def create(self, validated_data: dict):
        """Создание нового пользователя и сохранение его в БД с захэшированным паролем"""
        del validated_data['password_repeat']
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        return user


class LoginSerializer(serializers.ModelSerializer):
    """Сериализатор для входа по username и password"""
    password = serializers.CharField(validators=[validate_password],
                                     write_only=True, style={'input_type': 'password'})
    username = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        read_only_fields = ('id', 'email')

    def create(self, validated_data: dict) -> User:
        """Аутентификация пользователя"""
        if not (user := authenticate(
                username=validated_data.get('username', None),
                password=validated_data.get('password', None)
        )):
            raise AuthenticationFailed
        return user
