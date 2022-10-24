from django.contrib.auth import login, logout
from rest_framework import generics, status, permissions
from rest_framework.response import Response

from core.models import User
from core.serialazers import CreateUserSerialiser, LoginSerializer, ProfileSerializer, UpdatePasswordSerializer


class SignupView(generics.CreateAPIView):
    serializer_class = CreateUserSerialiser


class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer

    def perform_create(self, serializer):
        login(request=self.request, user=serializer.save())


class ProfileView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self) -> User:
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdatePasswordView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePasswordSerializer

    def get_object(self):
        return self.request.user
