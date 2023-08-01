from django.urls import path, include
from rest_framework.routers import DefaultRouter
from STA.views import *

router = DefaultRouter()
router.register('', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls))

]
