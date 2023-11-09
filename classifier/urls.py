from django.urls import path, include
from rest_framework import routers
from .views import *

# router = routers.DefaultRouter()
# router.register(r'classifier', views.Post_APIView, 'classifier')

urlpatterns = [
    path('api/v1/', Post_APIView.as_view()),
]
