from django.shortcuts import render
from rest_framework import viewsets, authentication
from STA.serializers import SignUpSerializer
from STA.permissions import *
from STA.models import User

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = SignUpSerializer
    permission_classes = (UserPermissions,)
    authentication_classes = (authentication.TokenAuthentication,)
    queryset = User.objects.all()

