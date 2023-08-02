from django.urls import path, include
from rest_framework.routers import DefaultRouter
from STA.views import *



urlpatterns = [
    path('login/', LoginApiView.as_view(), name='api_view'),
    path('signup/', UserSignUpViewSet.as_view()),
    path('',STAApiView.as_view())

]
