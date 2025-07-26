from django.shortcuts import render
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    # permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            user_serializer = UserSerializer(user)
            return Response({
                'refresh' : str(refresh),
                'access' : str(refresh.access_token),
                'user' : user_serializer.data,
            })
        else:
            return Response({'detail': 'Invalid Credential, Please try again!!'}, status=401)

