from django.shortcuts import render
from rest_framework.views import APIView
from STA.serializers import SignUpSerializer, LoginSerializer
from STA.permissions import *
from STA.models import User
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from django.contrib.auth import login

# Create your views here.

class UserSignUpViewSet(APIView):
    serializer_class = SignUpSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": LoginSerializer(user, context=self.get_serializer_context()).data,
        "token": Token.objects.create(user)[1]
        })

class UserLoginApiView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(UserLoginApiView, self).post(request, format=None)