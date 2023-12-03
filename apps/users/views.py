from django.contrib.auth import login, logout
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.serializers import CreateUserSerializer, LoginSerializer


class SingUpView(CreateAPIView):
    """Регистрация нового пользователя"""
    serializer_class = CreateUserSerializer


class LoginView(CreateAPIView):
    """Вход по имени и паролю"""
    serializer_class = LoginSerializer

    def create(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        login(request=request, user=serializer.save())
        return Response(serializer.data)


class LogoutView(APIView):
    """Выход из учетной записи"""

    def post(self, request) -> Response:
        logout(request)
        return Response({'detail': 'Logged out successfully.'})


