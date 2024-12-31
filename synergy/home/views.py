from django.shortcuts import render
from .serializers import UserSerializer
from .models import UserProfile
from rest_framework import viewsets
# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer

