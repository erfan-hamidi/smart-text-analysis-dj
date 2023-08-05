from django.shortcuts import render
from rest_framework.views import APIView
from STA.serializers import SignUpSerializer, LoginSerializer
from STA.permissions import *
from STA.models import User
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# views here.

class UserSignUpAPI(generics.GenericAPIView):
    serializer_class = SignUpSerializer
    permission_classes = ()
    authentication_classes = ()
    
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })

class LoginApiView(APIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = LoginSerializer
    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':
            serializer = LoginSerializer(data=request.data)
            print(request.data)
            if serializer.is_valid():
                user = serializer.validated_data['user']
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class STAApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        if data['output-type'] == 'sem' :
            pass
        elif data['output-type'] == 'sum':
            pass
        elif data['output-type'] == 'spa':
            pass 
        else:
            return Response({
                'error' : 'invalid input',
            },status=status.HTTP_400_BAD_REQUEST)
        