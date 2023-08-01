from django.shortcuts import render
from rest_framework import viewsets, authentication
from STA.serializers import SignUpSerializer
from STA.permissions import *
from STA.models import User
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = SignUpSerializer
    permission_classes = (UserPermissions,)
    authentication_classes = (authentication.TokenAuthentication,)
    queryset = User.objects.all()

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES