from django.urls import path, include
from rest_framework.routers import DefaultRouter
from STA.views import *



urlpatterns = [
    path('login/', UserLoginApiView.as_view()),
    path('', UserSignUpViewSet.as_view()),

]
