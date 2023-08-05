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

# views here.

class UserSignUpViewSet(APIView):
    serializer_class = SignUpSerializer
    
    def post(self, request, *args, **kwargs):
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
        
        print('hi')
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
        # Your view logic here
        print(request.data)
        return Response({"message": "This is a protected view accessible to authenticated users."},status=status.HTTP_200_OK)