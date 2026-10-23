from django.shortcuts import render
from rest_framework import generics
from .serializers import SignupSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

class SignupView(generics.CreateAPIView):
    serializer_class = SignupSerializer

class LoginView(TokenObtainPairView):
    pass


