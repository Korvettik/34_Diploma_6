from django.contrib.auth import login, logout
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from core.models import User
from core.serialazers import CreateUserSerializer, LoginSerializer, ProfileSerializer, UpdatePasswordSerializer


@extend_schema(
    description="Signup created user",
    summary="Signup user"
)
class SignupView(generics.CreateAPIView):
    """Создание пользователя"""
    serializer_class = CreateUserSerializer


class LoginView(generics.CreateAPIView):
    """Авторизация пользователя"""
    serializer_class = LoginSerializer
    @extend_schema(
        description="Create new user",
        summary="New user"
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request=request, user=user)
        return Response(ProfileSerializer(user).data)


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    """Просмотр, редактирование, удаление профиля"""
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ["get", "delete"]

    @extend_schema(
        description="Show all about user profile",
        summary="User profile"
    )
    def get_object(self) -> User:
        return self.request.user

    @extend_schema(
        description="Delete user profile",
        summary="Delete user"
    )
    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdatePasswordView(generics.UpdateAPIView):
    """Изменение пароля"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePasswordSerializer
    http_method_names = ["patch"]

    @extend_schema(
        description="Rewrite user password",
        summary="Password update"
    )
    def get_object(self):
        return self.request.user
