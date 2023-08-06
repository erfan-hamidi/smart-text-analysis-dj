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
from langdetect import detect
import h5py
import tensorflow as tf
import numpy as mp

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
        if data['output-type'] == 'sen' :
            lang = detect(data['input'])
            print(lang)
            if lang == 'fa':
                f = h5py.File('Per_Sen_Analysis_Model.hdf5','r')
            elif lang == 'en':
                new_model = tf.keras.models.load_model('C:\code\smart-text-analysis-dj\STA\EN_Sen_Analysis_Model.h5')
                new_model.summary()
                print(new_model.predict(mp.array(['The TensorFlow platform helps you implement best practices for data automation, model tracking, performance monitoring, and model retraining.Using production-level tools to automate and track model training over the lifetime of a product, service, or business process is critical to success. TFX provides software frameworks and tooling for full MLOps deployments, detecting issues as your data and models evolve over time.'])))
        elif data['output-type'] == 'sum':
            pass
        elif data['output-type'] == 'spa':
            pass 
        else:
            return Response({
                'error' : 'invalid input',
            },status=status.HTTP_400_BAD_REQUEST)
        